"""Version-scoped block numbering over sanitized MCP evidence; no remote transport."""
from __future__ import annotations

import copy
import hashlib
import json
import re
from pathlib import Path

from manage_slices import ContractError, canonical_bytes, digest, require_text, require_timestamp, contained_feature_path, file_digest, load_json

POLICY = "blocks-v1"


def fail(message):
    raise ContractError(message)


def positive(value, label):
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        fail(f"{label} must be a positive integer")
    return value


def named(issue, key):
    value = issue.get(key)
    return value.get("id") if isinstance(value, dict) else value


def number(issue, field_id):
    fields = issue.get("custom_fields")
    if not isinstance(fields, list):
        fail("Sequencing evidence requires complete custom_fields")
    matches = [f for f in fields if f.get("id") == field_id]
    if len(matches) > 1:
        fail("duplicate Sequencing field")
    raw = matches[0].get("value") if matches else None
    if raw is None or raw == "":
        return None
    if isinstance(raw, bool) or not re.fullmatch(r"[1-9][0-9]*", str(raw)):
        fail("nonblank Sequencing must be a positive integer")
    return int(raw)


def snapshot(value):
    """Require all statuses, exact project/version and complete paginated evidence."""
    project = value.get("project")
    if not isinstance(project, dict):
        fail("sequence snapshot requires project metadata")
    project_id = positive(project.get("id"), "project.id")
    version_id = positive(value.get("version_id"), "version_id")
    require_text(value.get("server"), "server")
    if value.get("status_scope") != "all":
        fail("sequence occupancy must include closed issues")
    fields = [f for f in project.get("issue_custom_fields", []) if f.get("name") == "Sequencing"]
    if len(fields) != 1 or fields[0].get("field_format") not in (None, "int", "integer", "string"):
        fail("Sequencing field is missing ambiguous or incompatible")
    field_id = positive(fields[0].get("id"), "Sequencing field id")
    pages = value.get("pages")
    issues = value.get("issues")
    if not isinstance(pages, list) or not pages or not isinstance(issues, list):
        fail("sequence occupancy requires paginated issues")
    offset = 0
    for index, page in enumerate(pages):
        if not isinstance(page, dict) or set(page) != {"offset", "limit", "count"}:
            fail("invalid sequence page evidence")
        limit = positive(page["limit"], "page limit")
        count = page["count"]
        if isinstance(count, bool) or not isinstance(count, int) or not 0 <= count <= limit or page["offset"] != offset:
            fail("incomplete sequence page evidence")
        if count < limit and index != len(pages) - 1:
            fail("sequence pagination continues after a short page")
        offset += count
    if value.get("total_count") != len(issues) or offset != len(issues):
        fail("sequence occupancy is not complete")
    by_id = {}
    for issue in issues:
        issue_id = positive(issue.get("id"), "issue.id")
        for field in ("project", "fixed_version", "tracker", "status"):
            positive(named(issue, field), f"issue.{field}")
        if named(issue, "parent") is not None:
            positive(named(issue, "parent"), "issue.parent")
        if issue_id in by_id or named(issue, "project") != project_id or named(issue, "fixed_version") != version_id:
            fail("sequence occupancy contains duplicate or out-of-scope issues")
        number(issue, field_id)
        by_id[issue_id] = issue
    return project_id, version_id, field_id, by_id


def preserved(issue, field_id):
    keys = ("id", "subject", "description", "estimated_hours", "start_date", "due_date")
    value = {key: issue.get(key) for key in keys}
    for key in ("project", "parent", "tracker", "status", "priority", "assigned_to", "category", "fixed_version"):
        value[key] = named(issue, key)
    value["custom_fields"] = sorted(
        [f for f in issue.get("custom_fields", []) if f.get("id") != field_id], key=lambda f: f["id"],
    )
    return value


def not_started(issue, status_id):
    if named(issue, "status") != status_id or not isinstance(issue.get("journals"), list):
        return False
    for journal in issue["journals"]:
        if not isinstance(journal, dict) or not isinstance(journal.get("details", []), list):
            return False
        for detail in journal.get("details", []):
            if not isinstance(detail, dict):
                return False
            if detail.get("name") == "status_id":
                values = [detail.get("old_value"), detail.get("new_value")]
                if any(v not in (None, "", str(status_id), status_id) for v in values):
                    return False
    return True


def allocate(evidence, parent, keys, *, fixed=None, managed=None, initial_status_id=1, study=False):
    project_id, version_id, field_id, issues = snapshot(evidence)
    parent_id = positive(parent.get("id"), "parent.id")
    if parent_id not in issues or named(parent, "project") != project_id or named(parent, "fixed_version") != version_id:
        fail("sequence parent must belong to the selected version snapshot")
    if preserved(parent, field_id) != preserved(issues[parent_id], field_id) or number(parent, field_id) != number(issues[parent_id], field_id):
        fail("parent snapshots disagree")
    if not keys or len(keys) != len(set(keys)) or any(not isinstance(k, str) or not k for k in keys):
        fail("sequence child keys must be unique")
    fixed = fixed or {}
    managed = set(managed or [])
    positions = []
    for key, issue_id in fixed.items():
        if key not in keys or issue_id not in issues or named(issues[issue_id], "parent") != parent_id:
            fail("fixed sequence must identify an existing child of this parent")
        value = number(issues[issue_id], field_id)
        if value is None:
            fail("existing unnumbered children require explicit migration")
        positions.append((keys.index(key), value))
    if positions:
        start = min(value for _, value in positions)
        positive(start, "block start")
    else:
        if number(parent, field_id) is not None:
            fail("an already numbered parent needs its existing managed child mapping")
        start = max((number(i, field_id) or 0 for i in issues.values()), default=0) + 1
    assignments = {key: start + index for index, key in enumerate(keys)}
    end = start + len(keys) - 1
    fixed_ids = set(fixed.values())
    foreign = [i for i in issues.values() if i["id"] not in fixed_ids | {parent_id} and number(i, field_id) is not None]
    collisions = [i for i in foreign if start <= number(i, field_id) <= end]
    updates = []
    for key, issue_id in fixed.items():
        issue = issues[issue_id]
        old = number(issue, field_id)
        if old != assignments[key]:
            if issue_id not in managed or not not_started(issue, initial_status_id):
                fail("block expansion would move a started or external child")
            updates.append({"issue_id": issue_id, "before": old, "after": assignments[key],
                            "baseline": preserved(issue, field_id), "unstarted_status_id": initial_status_id})
    if collisions:
        first = min(number(i, field_id) for i in collisions)
        delta = end - first + 1
        affected = sorted([i for i in foreign if number(i, field_id) >= first], key=lambda i: (number(i, field_id), i["id"]), reverse=True)
        for issue in affected:
            if issue["id"] not in managed or not not_started(issue, initial_status_id):
                fail("block expansion would move an external started or completed issue")
            updates.append({"issue_id": issue["id"], "before": number(issue, field_id), "after": number(issue, field_id) + delta,
                            "baseline": preserved(issue, field_id), "unstarted_status_id": initial_status_id})
    if not study and number(parent, field_id) != start:
        updates.append({"issue_id": parent_id, "before": number(parent, field_id), "after": start,
                        "baseline": preserved(parent, field_id), "unstarted_status_id": None})
    updates.sort(key=lambda update: (update["before"] or 0, update["issue_id"]), reverse=True)
    plan = {"policy": POLICY, "server": evidence["server"], "project_id": project_id, "version_id": version_id,
            "field_id": field_id, "parent_id": parent_id, "start": start, "end": end, "study": study,
            "assignments": assignments, "fixed": fixed, "updates": updates}
    plan["sha256"] = digest(plan)
    return plan


def validate(plan):
    if not isinstance(plan, dict) or plan.get("policy") != POLICY or plan.get("sha256") != digest({k: v for k, v in plan.items() if k != "sha256"}):
        fail("sequence plan differs from approved content")
    for key in ("project_id", "version_id", "field_id", "parent_id", "start", "end"):
        positive(plan[key], key)
    values = list(plan["assignments"].values())
    if values != list(range(plan["start"], plan["end"] + 1)):
        fail("sequence assignments must form a contiguous block")


def check_live(plan, evidence, bindings=None, *, final=False, changes=None):
    validate(plan)
    project_id, version_id, field_id, issues = snapshot(evidence)
    if (evidence["server"], project_id, version_id, field_id) != (plan["server"], plan["project_id"], plan["version_id"], plan["field_id"]):
        fail("sequence snapshot destination differs from approved plan")
    bindings = {**plan["fixed"], **(bindings or {})}
    known_ids = set(bindings.values()) | {plan["parent_id"]}
    update_ids = {u["issue_id"] for u in plan["updates"]}
    changes = changes or {}
    for update in plan["updates"]:
        issue = issues.get(update["issue_id"])
        expected = {**update["baseline"], **changes.get(update["issue_id"], {})}
        if issue is None or preserved(issue, field_id) != expected:
            fail("numbering update would change an issue with a divergent baseline")
        if update["unstarted_status_id"] is not None and "status" not in changes.get(update["issue_id"], {}) and not not_started(issue, update["unstarted_status_id"]):
            fail("numbering update target has started")
        allowed = {update["after"]} if final else {update["before"], update["after"]}
        if number(issue, field_id) not in allowed:
            fail("numbering update diverges from approved before/after values")
    targets = {u["after"]: u["issue_id"] for u in plan["updates"] if u["issue_id"] != plan["parent_id"]}
    for issue in issues.values():
        value = number(issue, field_id)
        if issue["id"] in known_ids or value is None:
            continue
        if issue["id"] not in update_ids and (plan["start"] <= value <= plan["end"] or value in targets):
            fail("concurrent issue occupies an approved sequence position")
    for key, issue_id in bindings.items():
        issue = issues.get(issue_id)
        accepted = {plan["assignments"].get(key)}
        if not final:
            accepted.update(u["before"] for u in plan["updates"] if u["issue_id"] == issue_id)
        if key not in plan["assignments"] or issue is None or named(issue, "parent") != plan["parent_id"] or number(issue, field_id) not in accepted:
            fail("published child Sequencing differs from the approved block")
    if final:
        if set(bindings) != set(plan["assignments"]):
            fail("sequence final verification requires every child")
        parent = issues.get(plan["parent_id"])
        if parent is None or (not plan["study"] and number(parent, field_id) != plan["start"]):
            fail("parent Sequencing does not mark the block start")


def attributes(plan, key):
    validate(plan)
    return [{"id": plan["field_id"], "value": str(plan["assignments"][key])}]


def check_dependencies(plan, edges, evidence):
    _, _, field_id, issues = snapshot(evidence)
    changed = {u["issue_id"]: u["after"] for u in plan["updates"]}
    existing = {issue_id: plan["assignments"][key] for key, issue_id in plan["fixed"].items()}

    def value(endpoint):
        if isinstance(endpoint, str):
            return plan["assignments"].get(endpoint)
        return existing.get(endpoint, changed.get(endpoint, number(issues[endpoint], field_id) if endpoint in issues else None))

    for source, target in edges:
        before, after = value(source), value(target)
        if before is not None and after is not None and before >= after:
            fail("approved dependencies require an order incompatible with contiguous numbering blocks")
        if isinstance(source, int) and source in issues and before is None:
            fail("allocate the supplier block before its dependent business work")


def bind_policy(feature_dir):
    """New flow states opt in explicitly; absence retains historical payloads."""
    for name in ("feature-state.json", "bug-state.json"):
        path = Path(feature_dir) / ".flow" / name
        if path.is_file():
            return json.loads(path.read_text(encoding="utf-8")).get("sequencing_policy") == POLICY
    return False


def git_directory(state_path):
    for parent in Path(state_path).resolve().parents:
        marker = parent / ".git"
        if marker.is_dir():
            return marker
        if marker.is_file():
            raw = marker.read_text(encoding="utf-8").strip()
            if not raw.startswith("gitdir: "):
                fail("invalid Git worktree marker")
            git_dir = (parent / raw[8:]).resolve()
            common = git_dir / "commondir"
            return (git_dir / common.read_text(encoding="utf-8").strip()).resolve() if common.is_file() else git_dir
    fail("sequence publication requires a Git repository")


def lock(state_path, plan, *, release=False):
    key = hashlib.sha256(canonical_bytes([plan["server"], plan["project_id"], plan["version_id"]])).hexdigest()
    directory = git_directory(state_path) / "remsoft-sequencing"
    if directory.is_symlink():
        fail("unsafe sequence lock directory")
    directory.mkdir(exist_ok=True)
    path = directory / (key + ".lock")
    owner = {"state": str(Path(state_path).resolve()), "plan": plan["sha256"]}
    if path.is_symlink():
        fail("unsafe sequence lock")
    if path.exists():
        if json.loads(path.read_text(encoding="utf-8")) != owner:
            fail("another publication owns this project/version sequence lock")
        if release:
            path.unlink()
        return
    if not release:
        try:
            with path.open("x", encoding="utf-8") as stream:
                json.dump(owner, stream)
        except FileExistsError:
            fail("another publication acquired this sequence lock")


def bindings(state):
    result = {}
    for key, operation in state.get("operations", {}).items():
        if key.startswith("create:") and operation.get("status") == "completed":
            result[key[7:]] = operation["remote_id"]
    if (state.get("operation") or {}).get("status") == "completed":
        result["study"] = state["operation"]["remote_id"]
    for revision in state.get("revisions", []):
        for operation in revision.get("operations", []):
            if operation["action"] == "create":
                record = state["operations"].get(operation["key"], {})
                if record.get("status") == "completed":
                    result[operation["task_key"]] = record["remote_id"]
    return result


def requirement_state(feature_dir):
    for name in ("feature-state.json", "bug-state.json"):
        path = Path(feature_dir) / ".flow" / name
        if path.is_file():
            return path, load_json(path)
    fail("sequencing requires the canonical requirement state")


def assert_scope_order(feature_dir, evidence):
    path, state = requirement_state(feature_dir)
    link = state.get("scope_item")
    if not link:
        return
    harness = next((p for p in path.parents if p.name == "harness" and p.parent.name == "docs"), None)
    if harness is None:
        fail("scope sequencing requires the canonical docs/harness layout")
    scope_path = (harness / link["state_path"]).resolve()
    if not scope_path.is_relative_to(harness):
        fail("scope sequencing reference leaves docs/harness")
    scope = load_json(scope_path)
    order = scope["suggested_order"]
    current = link["catalog_item_id"]
    progress = {item["catalog_item_id"]: item for item in scope["item_progress"]}
    _, _, field_id, issues = snapshot(evidence)
    for item_id in order[:order.index(current)]:
        item = progress[item_id]
        issue = issues.get(item.get("issue_id"))
        if issue is None or number(issue, field_id) is None:
            fail("allocate preceding scope items before this block")


def prepare_config(feature_dir, config, parent, keys, *, fixed=None, study=False, initial_status_id=1):
    if not isinstance(config, dict) or "snapshot" not in config or set(config) - {"snapshot", "managed_publications"}:
        fail("sequencing config requires snapshot and optional managed_publications")
    evidence_path = contained_feature_path(Path(feature_dir), config["snapshot"], "sequencing snapshot")
    if ".work" not in evidence_path.relative_to(Path(feature_dir).absolute()).parts[:1]:
        fail("sequencing snapshot must be inside .work")
    evidence = load_json(evidence_path)
    assert_scope_order(feature_dir, evidence)
    managed = set()
    sources = []
    from manage_publication import validate_publication_state, child_remote_id
    for raw_path in config.get("managed_publications", []):
        source_path = Path(raw_path).resolve()
        # Only canonical state files in this repository may authorize shifting issues.
        repository = next((p for p in Path(feature_dir).resolve().parents if (p / ".git").exists()), None)
        if repository is None or not source_path.is_relative_to(repository) or source_path.name != "slices-publication.json":
            fail("managed numbering sources must be canonical publications in this repository")
        source = load_json(source_path)
        validate_publication_state(source, check_files=False)
        if source["schema_version"] != 3 or source["status"] != "completed":
            fail("only completed new-policy publications authorize numbering-only replanning")
        source_plan = source["revisions"][-1]["sequencing"]
        if (source_plan["server"], source_plan["project_id"], source_plan["version_id"]) != (evidence["server"], evidence["project"]["id"], evidence["version_id"]):
            fail("managed numbering source belongs to another destination")
        ids = [source_plan["parent_id"], *[child_remote_id(source, child["key"]) for child in source["revisions"][-1]["children"]]]
        application_path = source_path.parent / "slices-revision-application.json"
        if application_path.exists():
            from manage_revision_application import validate_state as validate_application
            application = load_json(application_path)
            validate_application(application, check_authority=False)
            if application["status"] != "completed" or "sequencing" not in application["revisions"][-1]:
                fail("numbering replan requires the completed current new-policy application")
            ids += [item["remote_id"] for update in application["artifact_updates"] for item in update["items"]]
            source_path = application_path
        managed.update(ids)
        sources.append({"path": str(source_path), "sha256": file_digest(source_path), "issue_ids": ids})
    result = allocate(evidence, parent, keys, fixed=fixed, managed=managed, initial_status_id=initial_status_id, study=study)
    result["managed_publications"] = sources
    result["snapshot_sha256"] = digest(evidence)
    result["sha256"] = digest({k: v for k, v in result.items() if k != "sha256"})
    return result


def preview(plan):
    lines = ["", "## Sequencing", "", f"- Projeto/versão: {plan['project_id']}/{plan['version_id']}",
             f"- Campo: Sequencing (ID {plan['field_id']})", f"- Bloco: {plan['start']}–{plan['end']}",
             f"- Pai: {'sem número até concluir o fatiamento' if plan['study'] else plan['start']}", ""]
    lines += [f"- {key}: {value}" for key, value in plan["assignments"].items()]
    if plan["updates"]:
        lines += ["", "### Atualizações de numeração", ""]
        lines += [f"- #{u['issue_id']}: {u['before']} → {u['after']}" for u in plan["updates"]]
    return "\n".join(lines) + "\n"


def register_commands(commands):
    for name in ("begin-numbering", "finish-numbering", "observe-numbering"):
        command = commands.add_parser(name)
        command.add_argument("state")
        command.add_argument("--index", type=int, required=True)
        command.add_argument("--at", required=True)
        if name != "finish-numbering":
            command.add_argument("--snapshot", required=True)
        if name == "finish-numbering":
            command.add_argument("--attempt", type=int, required=True)
            command.add_argument("--outcome", choices=("completed", "failed", "unknown"), required=True)
        if name == "observe-numbering":
            command.add_argument("--outcome", choices=("matched", "absent"), required=True)
        command.set_defaults(numbering_action=name, run=command_numbering)
    release = commands.add_parser("release-numbering")
    release.add_argument("state")
    release.set_defaults(run=command_release)


def command_release(arguments):
    path = Path(arguments.state)
    state = load_json(path)
    if "change_review" in state["revisions"][-1]:
        from manage_revision_application import validate_state
        validate_state(state, check_authority=False)
        complete = state["status"] == "completed"
    elif "operation" in state:
        from manage_study import validate_state
        validate_state(state)
        complete = state["status"] in {"awaiting-result", "result-recorded", "resumed"}
    else:
        from manage_publication import validate_publication_state
        validate_publication_state(state)
        complete = state["status"] == "completed"
    if not complete or not state.get("readback"):
        fail("release requires a completed verified publication; resume pending work instead")
    if "sequencing" not in state["revisions"][-1]:
        fail("legacy publication has no block-policy lock")
    lock(path, state["revisions"][-1]["sequencing"], release=True)
    print(json.dumps({"status": "released"}))


def command_numbering(arguments):
    from manage_publication import validate_publication_state, require_remote_authority, current_evidence_path
    from manage_slices import atomic_write, require_timestamp
    path = Path(arguments.state)
    state = load_json(path)
    if "change_review" in state["revisions"][-1]:
        from manage_revision_application import validate_state
        validate_state(state)
        current = state["revisions"][-1]
        if not any(a.get("proposal_sha256") == current["proposal_sha256"] for a in state["plan_approvals"]):
            fail("numbering requires current revision-plan approval")
    elif "operation" in state:
        from manage_study import validate_state
        validate_state(state)
        if state["status"] not in {"approved", "publishing"}:
            fail("numbering requires current Study approval")
    else:
        validate_publication_state(state)
        require_remote_authority(state)
    at = require_timestamp(arguments.at, "numbering timestamp")
    result = None
    if arguments.numbering_action == "finish-numbering":
        finish_update(state, arguments.index, arguments.attempt, arguments.outcome, at)
    else:
        current = state["revisions"][-1]
        if "change_review" in current:
            from manage_revision_application import evidence_path
            evidence = load_json(evidence_path(path.parent.parent, arguments.snapshot, "numbering snapshot"))
        elif "input_check_path" in current:
            from manage_study import evidence_path
            evidence = load_json(evidence_path(Path(current["input_check_path"]).parent.parent, arguments.snapshot, "numbering snapshot"))
        else:
            evidence = load_json(current_evidence_path(current, arguments.snapshot, "numbering snapshot"))
        if arguments.numbering_action == "begin-numbering":
            result = begin_update(path, state, arguments.index, evidence, at)
        else:
            observe_update(state, arguments.index, evidence, arguments.outcome, at)
    validate_operations(state)
    atomic_write(path, canonical_bytes(state) + b"\n")
    print(json.dumps(result or {"status": "recorded"}, ensure_ascii=False))


def validate_history(state, check_files):
    history = state.get("sequencing_history", [])
    if not isinstance(history, list):
        fail("sequencing history must be an array")
    current = state["revisions"][-1]
    flow = Path(current["slices_state_path"] if "slices_state_path" in current else current["publication"]["path"]).parent.resolve()
    for entry in history:
        required = {"authority_sha256", "values", "recorded_at", "previous_state", "previous_sha256"}
        if not isinstance(entry, dict) or not required <= set(entry) or set(entry) - required - {"after_revision", "artifacts"}:
            fail("invalid numbering-only history")
        if not re.fullmatch(r"[a-f0-9]{64}", entry["authority_sha256"]) or not re.fullmatch(r"[a-f0-9]{64}", entry["previous_sha256"]):
            fail("numbering-only history requires content hashes")
        path = Path(entry["previous_state"])
        if path.resolve() != flow / "sequencing-history" / (entry["previous_sha256"] + ".json"):
            fail("numbering archive must stay inside the canonical .flow directory")
        if check_files and file_digest(path) != entry["previous_sha256"]:
            fail("numbering history archive changed")
        require_timestamp(entry["recorded_at"], "numbering history timestamp")
        if not isinstance(entry["values"], dict) or not entry["values"]:
            fail("numbering history requires changed issues")
        for issue_id, value in entry["values"].items():
            if not re.fullmatch(r"[1-9][0-9]*", issue_id):
                fail("invalid numbering history issue id")
            positive(value, "history sequence")


def renumbered_files(plan, evidence, at, *, skip_parent=False):
    """Stage authorized numbering-only receipts/artifacts without rewriting old approvals."""
    from manage_publication import validate_publication_state
    _, _, field_id, issues = snapshot(evidence)
    changed = {u["issue_id"]: u["after"] for u in plan["updates"]}
    files = {}
    for reference in plan.get("managed_publications", []):
        if skip_parent and plan["parent_id"] in reference["issue_ids"]:
            continue
        path = Path(reference["path"])
        if file_digest(path) != reference["sha256"]:
            fail("managed publication changed since numbering preview")
        state = load_json(path)
        application = "change_review" in state["revisions"][-1]
        if application:
            from manage_revision_application import validate_state as validate_application
            validate_application(state, check_authority=False)
            source = load_json(Path(state["revisions"][-1]["publication"]["path"]))
            artifacts = {a["remote_id"]: copy.deepcopy(a) for a in source["artifacts"]}
            for update in state["artifact_updates"]:
                artifacts.update({a["remote_id"]: copy.deepcopy(a) for a in update["items"]})
            for issue_id, artifact in state.get("numbering_artifacts", {}).items():
                artifacts[int(issue_id)] = copy.deepcopy(artifact)
            artifacts = list(artifacts.values())
        else:
            validate_publication_state(state)
            artifacts = state["artifacts"]
        values = {str(i): changed[i] for i in reference["issue_ids"] if i in changed}
        if not values:
            continue
        # Keep immutable source bytes for the numbering-only revision's audit trail.
        archive = path.parent / "sequencing-history" / (reference["sha256"] + ".json")
        files[archive] = path.read_bytes()
        receipt = {"authority_sha256": plan["sha256"], "values": values, "recorded_at": at,
                   "previous_state": str(archive), "previous_sha256": reference["sha256"]}
        if application:
            receipt.update(after_revision=state["revisions"][-1]["number"], artifacts=[])
        state["sequencing_history"].append(receipt)
        for artifact in artifacts:
            value = values.get(str(artifact["remote_id"]))
            if value is None:
                continue
            artifact_path = Path(artifact["path"])
            original = artifact_path.read_text(encoding="utf-8")
            revised, count = re.subn(r"^- Sequencing: `[1-9][0-9]*`$", f"- Sequencing: `{value}`", original, count=1, flags=re.MULTILINE)
            if count != 1 or number(issues[artifact["remote_id"]], field_id) != value:
                fail("numbering artifact or remote value is missing")
            content = revised.encode("utf-8")
            files[artifact_path] = content
            previous_sha256 = artifact["sha256"]
            artifact["sha256"] = hashlib.sha256(content).hexdigest()
            if application:
                receipt["artifacts"].append({**copy.deepcopy(artifact), "previous_sha256": previous_sha256})
                state.setdefault("numbering_artifacts", {})[str(artifact["remote_id"])] = artifact
        files[path] = canonical_bytes(state) + b"\n"
    return files


def adapt_expected(state, issue):
    result = copy.deepcopy(issue)
    plan = state["revisions"][-1].get("sequencing")
    if plan:
        for index, update in enumerate(plan["updates"]):
            if update["issue_id"] == issue["id"] and state.get("sequencing_operations", {}).get(str(index), {}).get("status") == "completed":
                fields = copy.deepcopy(result.get("custom_fields", []))
                matches = [f for f in fields if f["id"] == plan["field_id"]]
                if matches:
                    matches[0]["value"] = str(update["after"])
                else:
                    fields.append({"id": plan["field_id"], "value": str(update["after"])})
                result["custom_fields"] = fields
    return result


def normalize_numbering_metadata(state, issue):
    """Allow only server metadata generated by this approved field update."""
    result = copy.deepcopy(issue)
    plan = state["revisions"][-1].get("sequencing")
    if not plan:
        return result
    for index, update in enumerate(plan["updates"]):
        if update["issue_id"] != issue["id"] or state.get("sequencing_operations", {}).get(str(index), {}).get("status") != "completed":
            continue
        result.pop("updated_on", None)
        if "journals" in result:
            def generated(journal):
                details = journal.get("details", [])
                return not journal.get("notes") and bool(details) and all(
                    d.get("property") == "cf" and str(d.get("name")) == str(plan["field_id"])
                    and str(d.get("old_value") or "") == str(update["before"] or "") and str(d.get("new_value")) == str(update["after"])
                    for d in details
                )
            result["journals"] = [journal for journal in result["journals"] if not generated(journal)]
    return result


def prepare_revision(feature_dir, config, published, previous, operations, initial_status_id):
    current = published["revisions"][-1]
    known = bindings(published)
    known.update(current["sequencing"]["fixed"])
    qa_keys = {child["key"] for child in current["children"] if child["kind"] == "qa"}
    if previous:
        for update in previous.get("artifact_updates", []):
            known.update({item["task_key"]: item["remote_id"] for item in update["items"]})
            qa_keys.update(item["task_key"] for item in update["items"] if item["kind"] == "qa")
    evidence_path = contained_feature_path(Path(feature_dir), config["snapshot"], "sequencing snapshot")
    evidence = load_json(evidence_path)
    _, _, field_id, issues = snapshot(evidence)
    keys = sorted(known, key=lambda key: number(issues[known[key]], field_id))
    created = [o for o in operations if o["action"] == "create"]
    new_dev = [o["task_key"] for o in created if not o["attributes"]["subject"].startswith("[QA] ")]
    new_qa = [o["task_key"] for o in created if o["attributes"]["subject"].startswith("[QA] ")]
    if new_dev and not new_qa:
        available = [key for key in keys if key in qa_keys and not_started(issues[known[key]], initial_status_id)]
        if not available:
            fail("new DEV work requires a new QA or an unstarted managed QA")
        qa_key = available[-1]
        keys.remove(qa_key)
        keys += new_dev + [qa_key]
    else:
        keys += new_dev + new_qa
    parent = issues[current["parent_baseline"]["issue_id"]]
    return prepare_config(feature_dir, config, parent, keys, fixed=known, initial_status_id=initial_status_id)


def expected_changes(state):
    result = {}
    for revision in state.get("revisions", []):
        for operation in revision.get("operations", []):
            record = state.get("operations", {}).get(operation["key"], {})
            if record.get("status") != "completed" or operation["action"] not in {"update", "cancel"}:
                continue
            values = result.setdefault(operation["issue_id"], {})
            for field, value in operation["attributes"].items():
                if field in {"subject", "description", "estimated_hours"}:
                    values[field] = value
                elif field == "status_id":
                    values["status"] = value
    return result


def before_create(state_path, state, evidence):
    plan = state["revisions"][-1].get("sequencing")
    if plan is None:
        return
    if evidence is None:
        fail("new sequencing publication requires fresh --sequencing-snapshot")
    check_live(plan, evidence, bindings(state), changes=expected_changes(state))
    for index in range(len(plan["updates"])):
        if state.get("sequencing_operations", {}).get(str(index), {}).get("status") != "completed":
            fail("complete approved numbering updates before creating children")
    lock(state_path, plan)


def update_operation(state, index):
    plan = state["revisions"][-1]["sequencing"]
    if not isinstance(index, int) or not 0 <= index < len(plan["updates"]):
        fail("unknown numbering update")
    operation = state.setdefault("sequencing_operations", {}).setdefault(str(index), {"status": "pending", "attempts": [], "observations": []})
    return plan, plan["updates"][index], operation


def begin_update(state_path, state, index, evidence, at):
    plan, update, operation = update_operation(state, index)
    if operation["status"] == "completed":
        fail("completed numbering update must not be repeated")
    if any(state.get("sequencing_operations", {}).get(str(i), {}).get("status") != "completed" for i in range(index)):
        fail("numbering updates must execute in their approved order")
    if operation["attempts"] and operation["attempts"][-1]["outcome"] in {"in-flight", "unknown"}:
        latest = operation["attempts"][-1]
        if not operation["observations"][latest["observations_before"]:] or operation["observations"][-1]["outcome"] != "absent":
            fail("unknown numbering update requires reconciliation before retry")
    check_live(plan, evidence, bindings(state))
    _, _, field_id, issues = snapshot(evidence)
    if number(issues[update["issue_id"]], field_id) != update["before"]:
        fail("numbering update no longer matches its approved before value")
    lock(state_path, plan)
    attempt = len(operation["attempts"]) + 1
    operation["attempts"].append({"id": attempt, "outcome": "in-flight", "at": at, "observations_before": len(operation["observations"])})
    return {"attempt_id": attempt, "issue_id": update["issue_id"], "changes": {"custom_fields": [{"id": field_id, "value": str(update["after"])}]}}


def finish_update(state, index, attempt, outcome, at):
    _, _, operation = update_operation(state, index)
    if not operation["attempts"] or operation["attempts"][-1]["id"] != attempt or operation["attempts"][-1]["outcome"] != "in-flight":
        fail("numbering result must finish the current attempt")
    if outcome not in {"completed", "failed", "unknown"}:
        fail("invalid numbering update outcome")
    operation["attempts"][-1].update(outcome=outcome, finished_at=at)
    if outcome == "completed":
        operation["status"] = "completed"


def observe_update(state, index, evidence, outcome, at):
    plan, update, operation = update_operation(state, index)
    if operation["status"] == "completed" or not operation["attempts"] or operation["attempts"][-1]["outcome"] not in {"in-flight", "unknown"}:
        fail("numbering reconciliation requires an unknown pending attempt")
    check_live(plan, evidence, bindings(state))
    _, _, field_id, issues = snapshot(evidence)
    value = number(issues[update["issue_id"]], field_id)
    if outcome not in {"matched", "absent"} or value != update["after" if outcome == "matched" else "before"]:
        fail("numbering reconciliation differs from the observed field")
    operation["observations"].append({"outcome": outcome, "at": at, "snapshot_sha256": digest(evidence)})
    if outcome == "matched":
        operation["status"] = "completed"


def validate_operations(state):
    plan = state["revisions"][-1].get("sequencing")
    if plan is None:
        if state.get("sequencing_operations"):
            fail("legacy publication cannot contain numbering updates")
        return
    validate(plan)
    for key, operation in state.get("sequencing_operations", {}).items():
        if not key.isdigit() or not 0 <= int(key) < len(plan["updates"]):
            fail("invalid numbering operation key")
        if operation.get("status") not in {"pending", "completed"}:
            fail("invalid numbering operation status")
        for index, attempt in enumerate(operation.get("attempts", []), 1):
            if attempt.get("id") != index or attempt.get("outcome") not in {"in-flight", "completed", "failed", "unknown"}:
                fail("invalid numbering attempt history")
        if operation["status"] == "completed" and not (any(a["outcome"] == "completed" for a in operation["attempts"]) or any(o.get("outcome") == "matched" for o in operation.get("observations", []))):
            fail("numbering completion requires a result or matched observation")
    if state.get("status") in {"completed", "awaiting-result", "result-recorded", "resumed"}:
        if any(state.get("sequencing_operations", {}).get(str(index), {}).get("status") != "completed" for index in range(len(plan["updates"]))):
            fail("verified publication requires reconciled numbering updates")
