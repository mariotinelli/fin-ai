#!/usr/bin/env python3
"""Prepare one local requirement/publication preview and bind its approved operations."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path, PurePosixPath

sys.dont_write_bytecode = True

from artifact_paths import artifact_root, checked_path, contained_path


ISSUE = "{{created_issue_id}}"


def encode(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def digest(value):
    return hashlib.sha256(value).hexdigest()


def safe(value):
    # Do not echo offending content in a diagnostic.
    if re.search(r'(?i)(authorization\s*:|bearer\s+|api[_ -]?key|password\s*[=:]|token\s*[=:])', json.dumps(value)):
        raise ValueError("publication plan contains credential material")


def canonical_path(value, item_type):
    if not isinstance(value, str) or "\\" in value or ":" in value or ".." in PurePosixPath(value).parts:
        raise ValueError("invalid planned canonical path")
    prefix = "docs/harness/features/" if item_type == "Feature" else "docs/harness/bugs/"
    if not value.startswith(prefix) or not value.endswith(f"/{item_type.lower()}.md") or ".work" in PurePosixPath(value).parts:
        raise ValueError("planned canonical path must identify the durable requirement")
    if value.count(ISSUE) > 1:
        raise ValueError("ambiguous issue binding")


def replace_issue(value, issue_id):
    if isinstance(value, dict):
        return {key: replace_issue(entry, issue_id) for key, entry in value.items()}
    if isinstance(value, list):
        return [replace_issue(entry, issue_id) for entry in value]
    if isinstance(value, str) and ISSUE in value:
        if isinstance(issue_id, bool) or not isinstance(issue_id, int) or issue_id < 1:
            raise ValueError("binding requires the persisted created issue ID")
        return issue_id if value == ISSUE else value.replace(ISSUE, str(issue_id))
    return value


def prepare(state, document, path, reviewer, attributes=None, before=None, relations=None):
    from render_publication import START, END, functional_sections, projection, split_managed, issue_snapshot

    if not isinstance(reviewer, str) or not reviewer.strip() or ISSUE in document or ISSUE in reviewer:
        raise ValueError("invalid reviewer or reserved issue binding in requirement")
    item_type = state["item_type"]
    canonical_path(path, item_type)
    title = document.splitlines()[0].removeprefix("# ").strip()
    if title != state["delivery"]["title"]:
        raise ValueError("canonical title differs from proposed delivery")
    content = "\n" + "\n\n".join(f"## {name}\n\n{body}" for name, body in functional_sections(document, item_type)) + "\n"
    redmine = state["redmine"]
    if before is None:
        if redmine.get("issue_id") is not None or state["remote_operations"]["create"]["status"] == "completed":
            raise ValueError("existing issue must not be created again")
        if not isinstance(attributes, dict):
            raise ValueError("creation preview requires proposed attributes")
        allowed = {"project_id", "tracker_id", "status_id", "category_id", "fixed_version_id", "custom_fields"}
        if set(attributes) - allowed:
            raise ValueError("creation attributes contain unpreviewed fields")
        expected = {"project_id": redmine["project_id"], "tracker_id": redmine["tracker_id"], "status_id": redmine["initial_status_id"], "category_id": redmine["category"]["id"]}
        if redmine.get("version") is not None:
            expected["fixed_version_id"] = redmine["version"]["id"]
        if any(attributes.get(key) != value for key, value in expected.items()):
            raise ValueError("creation attributes differ from proposed context")
        prefix, suffix = f'<!-- project-flow:run {state["run_id"]} -->\n', ""
        create = {"attributes": {**attributes, "subject": title, "description": prefix + START + content + END}}
        issue_id = ISSUE
        baseline = content
        if ISSUE not in path:
            raise ValueError("new issue path must show the created issue ID binding")
    else:
        before = issue_snapshot(before)
        if str(before["id"]) != str(redmine.get("issue_id")) or before["subject"] != title or attributes is not None:
            raise ValueError("publication baseline belongs to another issue or creation was requested twice")
        prefix, baseline, suffix = split_managed(before["description"])
        issue_id, create = before["id"], None
        if ISSUE in path:
            raise ValueError("existing issue preview must use its known canonical path")
    changes = {"description": prefix + START + projection(document, item_type, path, reviewer) + END + suffix}
    if redmine.get("version") is not None:
        changes["fixed_version_id"] = redmine["version"]["id"]
    publish = {"issue_id": issue_id, "changes": changes}
    result = {
        "schema_version": 1, "run_id": state["run_id"], "item_type": item_type,
        "requirement_sha256": digest(document.encode("utf-8")), "reviewer": reviewer, "issue_subject": title,
        "canonical_path": path, "baseline_managed_sha256": digest(baseline.encode("utf-8")),
        "create": create, "publish": publish, "relations": relations or [],
    }
    check_plan(result)
    return result


def check_plan(plan):
    from render_publication import split_managed

    keys = {"schema_version", "run_id", "item_type", "requirement_sha256", "reviewer", "issue_subject", "canonical_path", "baseline_managed_sha256", "create", "publish", "relations"}
    if not isinstance(plan, dict) or set(plan) != keys or plan["schema_version"] != 1:
        raise ValueError("invalid publication plan")
    safe(plan)
    canonical_path(plan["canonical_path"], plan["item_type"])
    for key in ("requirement_sha256", "baseline_managed_sha256"):
        if not isinstance(plan[key], str) or not re.fullmatch(r"[0-9a-f]{64}", plan[key]):
            raise ValueError("invalid plan fingerprint")
    publish = plan["publish"]
    if not isinstance(publish, dict) or set(publish) != {"issue_id", "changes"} or set(publish["changes"]) not in ({"description"}, {"description", "fixed_version_id"}):
        raise ValueError("publication plan may update only the description and selected version")
    split_managed(publish["changes"]["description"])
    if plan["create"] is not None:
        create = plan["create"]
        if not isinstance(create, dict) or set(create) != {"attributes"} or publish["issue_id"] != ISSUE:
            raise ValueError("invalid planned creation")
        if set(create["attributes"]) - {"project_id", "tracker_id", "status_id", "category_id", "fixed_version_id", "custom_fields", "subject", "description"}:
            raise ValueError("creation attributes contain unpreviewed fields")
        split_managed(create["attributes"]["description"])
        if ISSUE in json.dumps(create):
            raise ValueError("creation payload cannot depend on its future issue ID")
    seen = set()
    if not isinstance(plan["relations"], list):
        raise ValueError("planned relations must be an array")
    for relation in plan["relations"]:
        if not isinstance(relation, dict) or set(relation) != {"key", "payload"} or relation["key"] in seen:
            raise ValueError("invalid or repeated planned relation")
        payload = relation["payload"]
        if set(payload) != {"issue_id", "issue_to_id", "relation_type"} or payload["relation_type"] != "blocks":
            raise ValueError("invalid planned dependency relation")
        for key in ("issue_id", "issue_to_id"):
            if payload[key] != ISSUE and (isinstance(payload[key], bool) or not isinstance(payload[key], int) or payload[key] < 1):
                raise ValueError("invalid planned relation endpoint")
        seen.add(relation["key"])


def bind(plan, name, issue_id=None, baseline=None):
    from render_publication import START, END, issue_snapshot, split_managed

    check_plan(plan)
    if name == "create":
        if plan["create"] is None:
            raise ValueError("creation is not included in this approval")
        return plan["create"]
    if name == "publish":
        payload = replace_issue(plan["publish"], issue_id)
        if str(payload["issue_id"]) != str(issue_id):
            raise ValueError("publication target differs from persisted issue")
        if baseline is None:
            raise ValueError("publication binding requires a fresh issue baseline")
        baseline = issue_snapshot(baseline)
        safe(baseline)
        if str(baseline["id"]) != str(issue_id) or baseline["subject"] != plan["issue_subject"]:
            raise ValueError("baseline belongs to another issue")
        prefix, managed, suffix = split_managed(baseline["description"])
        if digest(managed.encode("utf-8")) != plan["baseline_managed_sha256"]:
            raise ValueError("managed requirement divergence requires delta review")
        _, approved, _ = split_managed(payload["changes"]["description"])
        payload["changes"]["description"] = prefix + START + approved + END + suffix
        return payload
    relation = next((entry for entry in plan["relations"] if entry["key"] == name), None)
    if relation is None:
        raise ValueError("operation is not included in the approved preview")
    return replace_issue(relation["payload"], issue_id)


def load_plan(approval, root):
    path = contained_path(root, approval["plan_path"])
    if not approval["plan_path"].replace("\\", "/").startswith(".flow/publications/"):
        raise ValueError("approved plans must be retained in .flow/publications")
    raw = path.read_bytes()
    if digest(raw) != approval["subject_sha256"]:
        raise ValueError("approved publication plan bytes changed")
    plan = json.loads(raw)
    check_plan(plan)
    return plan


def validate_authorizations(state, state_path, *, historical=False):
    from artifact_layout import approved_document
    from render_publication import functional_sections, split_managed, projection

    root = artifact_root(state_path)
    approvals = {a["id"]: a for a in state["approvals"]}
    for approval in approvals.values():
        if approval["kind"] == "requirement":
            snapshot_path = approval["document_path"]
            if not snapshot_path.startswith(".flow/publications/") or digest(contained_path(root, snapshot_path).read_bytes()) != approval["subject_sha256"]:
                raise ValueError("approved requirement snapshot changed")
    plans = {key: load_plan(a, root) for key, a in approvals.items() if a["kind"] == "publication-plan"}
    valid = [key for key in plans if approvals[key]["status"] == "valid"]
    if len(valid) > 1:
        raise ValueError("only one current publication plan may be approved")
    for key, plan in plans.items():
        approval = approvals[key]
        if plan["run_id"] != state["run_id"] or plan["item_type"] != state["item_type"] or plan["reviewer"] != approval["approved_by"]:
            raise ValueError("plan identity or reviewer differs from approval")
        if approval["status"] != "valid":
            continue
        canonical = [a for a in approvals.values() if a["kind"] == "requirement" and a["status"] == "valid"]
        if len(canonical) != 1 or any(canonical[0][field] != approval[field] for field in ("approved_by", "approved_at")) or canonical[0]["subject_sha256"] != plan["requirement_sha256"]:
            raise ValueError("one preview consent must cover the canonical requirement and operations")
        snapshot = contained_path(root, canonical[0]["document_path"])
        if not canonical[0]["document_path"].startswith(".flow/publications/") or digest(snapshot.read_bytes()) != plan["requirement_sha256"]:
            raise ValueError("approved requirement snapshot changed")
        document_path = contained_path(root, state["item_type"].lower() + ".md")
        document = snapshot.read_bytes().decode("utf-8")
        if not historical:
            approved_document(document_path, plan["requirement_sha256"])
        if plan["issue_subject"] != document.splitlines()[0].removeprefix("# ").strip():
            raise ValueError("plan title differs from canonical requirement")
        _, managed, _ = split_managed(plan["publish"]["changes"]["description"])
        if managed != projection(document, state["item_type"], plan["canonical_path"], plan["reviewer"]):
            raise ValueError("publication plan does not contain the complete canonical requirement")
        if plan["create"] is not None:
            attributes = plan["create"]["attributes"]
            if attributes["subject"] != state["delivery"]["title"]:
                raise ValueError("creation title differs from approved delivery")
            _, initial, _ = split_managed(attributes["description"])
            expected = "\n" + "\n\n".join(f"## {name}\n\n{body}" for name, body in functional_sections(document, state["item_type"])) + "\n"
            if initial != expected or digest(initial.encode("utf-8")) != plan["baseline_managed_sha256"]:
                raise ValueError("creation must already contain the complete functional requirement")
            redmine = state["redmine"]
            context = {"project_id": redmine["project_id"], "tracker_id": redmine["tracker_id"], "status_id": redmine["initial_status_id"], "category_id": redmine["category"]["id"]}
            if redmine.get("version") is not None:
                context["fixed_version_id"] = redmine["version"]["id"]
            if any(attributes.get(field) != value for field, value in context.items()):
                raise ValueError("planned creation differs from approved context")
        if state["redmine"].get("version") is not None and plan["publish"]["changes"].get("fixed_version_id") != state["redmine"]["version"]["id"]:
            raise ValueError("publication plan differs from the selected version")
        for decision in (state.get("classification"), state.get("similarity"), state["redmine"].get("category")):
            if not isinstance(decision, dict) or not decision.get("confirmed_by") or not decision.get("confirmed_at"):
                raise ValueError("preview selections must record their approval provenance")
        if state["classification"].get("confirmed_type") != state["item_type"]:
            raise ValueError("preview classification must be confirmed")
    if "requirement-approved" in state["completed_phases"] and not valid:
        raise ValueError("approved requirement requires a current publication plan")
    operations = [("create", state["remote_operations"]["create"]), ("publish", state["remote_operations"]["publish"])]
    operations += [(entry["key"], entry) for entry in state["remote_operations"].get("relations", [])]
    for name, operation in operations:
        if operation["status"] == "pending":
            continue
        if name == "create" and state["creation_timing"] == "before-interview" and "plan_approval_id" not in operation:
            if not any(a["kind"] == "create-payload" and a["subject_sha256"] == operation["payload_sha256"] and all(a[field] == operation[field] for field in ("approved_by", "approved_at")) and (a["status"] == "valid" or operation["status"] == "completed") for a in approvals.values()):
                raise ValueError("early creation requires its explicit payload approval")
            continue
        approval_id = operation.get("plan_approval_id")
        if approval_id not in plans or (operation["status"] != "completed" and approval_id not in valid):
            raise ValueError("operation requires a valid preview authorization")
        if any(operation[field] != approvals[approval_id][field] for field in ("approved_by", "approved_at")):
            raise ValueError("operation approval differs from its preview consent")
        baseline = None
        if name == "publish":
            raw = contained_path(root, operation["baseline_path"]).read_bytes()
            if digest(raw) != operation["baseline_sha256"]:
                raise ValueError("publication baseline changed")
            baseline = json.loads(raw)
        payload = bind(plans[approval_id], name, (state["redmine"] or {}).get("issue_id"), baseline)
        if digest(encode(payload)) != operation["payload_sha256"]:
            raise ValueError("operation payload is not authorized by the approved preview")
        if name not in {"create", "publish"} and (payload["issue_id"], payload["issue_to_id"], payload["relation_type"]) != (operation["source_issue_id"], operation["target_issue_id"], operation["relation_type"]):
            raise ValueError("relation identity differs from approved preview")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("prepare", "bind"))
    parser.add_argument("state", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--canonical-path")
    parser.add_argument("--reviewer")
    parser.add_argument("--attributes", type=Path)
    parser.add_argument("--before", type=Path)
    parser.add_argument("--relations", type=Path)
    parser.add_argument("--approval-id")
    parser.add_argument("--operation", default="publish")
    args = parser.parse_args()
    try:
        from validate_state import validate
        state = validate(args.state)
        if state["schema_version"] != 5:
            raise ValueError("publication plans require requirement state v5; retain legacy approvals on resume")
        root = artifact_root(args.state)
        document = contained_path(root, state["item_type"].lower() + ".md")
        before = json.loads(args.before.read_bytes()) if args.before else None
        inputs = {p.resolve() for p in (args.state, document, args.attributes, args.before, args.relations) if p}
        if args.action == "prepare":
            result = prepare(state, document.read_bytes().decode("utf-8"), args.canonical_path, args.reviewer,
                             json.loads(args.attributes.read_bytes()) if args.attributes else None,
                             before, json.loads(args.relations.read_bytes()) if args.relations else None)
        else:
            approval = next((a for a in state["approvals"] if a["id"] == args.approval_id and a["kind"] == "publication-plan" and a["status"] == "valid"), None)
            if approval is None:
                raise ValueError("binding requires the recorded preview approval")
            inputs.add(contained_path(root, approval["plan_path"]).resolve())
            if args.operation == "create" and state["redmine"].get("issue_id") is not None:
                raise ValueError("a recorded issue must not be created again")
            result = bind(load_plan(approval, root), args.operation, state["redmine"].get("issue_id"), before)
        output = checked_path(args.output, root=root)
        if output in inputs or output.exists():
            raise ValueError("output must be a new file distinct from retained inputs")
        raw = encode(result)
        with output.open("xb") as stream:
            stream.write(raw)
        print(digest(raw))
    except (OSError, ValueError, TypeError, KeyError, UnicodeDecodeError) as error:
        print(f"invalid: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
