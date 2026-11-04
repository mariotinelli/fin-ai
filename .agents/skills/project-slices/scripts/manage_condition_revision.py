#!/usr/bin/env python3
"""Review and publish localized test-condition revisions using local evidence only."""
from __future__ import annotations

import argparse
import copy
import difflib
import hashlib
import io
import json
import sys
from pathlib import Path
from xml.etree import ElementTree as ET
from zipfile import BadZipFile, ZipFile

import manage_publication as publication
import publication_attachments as attachments
import manage_change_review as change_review
from manage_change_review import approved_sources
from manage_slices import (
    ContractError, SHA256_PATTERN, assert_safe_read, assert_safe_write, atomic_write, canonical_bytes,
    digest, fail, file_digest, load_json, reject_secrets, require_exact_path,
    require_text, require_timestamp, validate_feature_approval,
)
from test_conditions import WORD, conditions_markdown, document_requested, docx_bytes, validate_condition_history, validate_conditions


STATE_NAME = "slices-condition-revisions.json"


def root_for(path: Path) -> Path:
    if path.name != STATE_NAME or path.parent.name != ".flow":
        fail(f"state must be stored at <feature>/.flow/{STATE_NAME}")
    assert_safe_write(path)
    return path.absolute().parent.parent


def preserve(root: Path, content: bytes) -> dict:
    sha = hashlib.sha256(content).hexdigest()
    path = root / ".flow" / "condition-evidence" / f"{sha}.bin"
    assert_safe_write(path)
    if path.exists():
        if file_digest(path) != sha:
            fail("immutable condition evidence changed")
    else:
        atomic_write(path, content)
    return {"path": str(path), "sha256": sha}


def evidence(root: Path, path: str) -> dict:
    location = Path(path)
    assert_safe_read(location)
    value = load_json(location)
    reject_secrets(value)
    return preserve(root, canonical_bytes(value))


def saved(root: Path, reference: dict, *, binary: bool = False):
    publication.exact(reference, {"path", "sha256"}, "condition evidence")
    if not isinstance(reference["sha256"], str) or not SHA256_PATTERN.fullmatch(reference["sha256"]):
        fail("condition evidence requires a SHA-256 digest")
    expected = root / ".flow" / "condition-evidence" / f"{reference['sha256']}.bin"
    require_exact_path(Path(reference["path"]), expected, "condition evidence")
    if file_digest(expected) != reference["sha256"]:
        fail("immutable condition evidence changed")
    content = expected.read_bytes()
    return content if binary else json.loads(content)


def paragraphs(content: bytes) -> list[str]:
    if len(content) > 16 * 1024 * 1024:
        fail("DOCX is too large for local review")
    with ZipFile(io.BytesIO(content)) as archive:
        part = archive.getinfo("word/document.xml")
        if part.file_size > 8 * 1024 * 1024:
            fail("DOCX document XML is too large for local review")
        document = ET.fromstring(archive.read(part))
    result = []
    for paragraph in document.iter(f"{{{WORD}}}p"):
        pieces = []
        for node in paragraph.iter():
            if node.tag in {f"{{{WORD}}}t", f"{{{WORD}}}delText"}:
                pieces.append(node.text or "")
            elif node.tag in {f"{{{WORD}}}br", f"{{{WORD}}}tab"}:
                pieces.append("\n" if node.tag.endswith("}br") else "\t")
        if pieces:
            result.append("".join(pieces))
    return result


def word_comparison(original: bytes, edited: bytes) -> dict:
    before, after = paragraphs(original), paragraphs(edited)
    annotations = []
    with ZipFile(io.BytesIO(edited)) as archive:
        for name in ("word/document.xml", "word/comments.xml", "word/footnotes.xml", "word/endnotes.xml"):
            if name not in archive.namelist():
                continue
            if archive.getinfo(name).file_size > 8 * 1024 * 1024:
                fail("DOCX review XML is too large")
            tree = ET.fromstring(archive.read(name))
            for node in tree.iter():
                tag = node.tag.rsplit("}", 1)[-1]
                if tag in {"ins", "del", "moveFrom", "moveTo", "comment", "footnote", "endnote"}:
                    annotations.append({"part": name, "kind": tag, "text": "".join(node.itertext())})
    return {"before": before, "after": after,
            "diff": list(difflib.unified_diff(before, after, fromfile="vigente", tofile="Word", lineterm="")),
            "annotations": annotations}


def qa_snapshot(source: dict, snapshot: dict, *, open_required: bool = False) -> dict:
    issue = publication.issue_object(snapshot)
    if issue.get("id") != source["qa_id"]:
        fail("snapshot belongs to another QA")
    fields = publication.comparable_issue(issue)
    baseline = source["publication"]["revisions"][-1]
    if fields["project_id"] != baseline["native_fields"]["project_id"] or fields["parent_issue_id"] != baseline["parent_baseline"]["issue_id"]:
        fail("QA project or parent changed")
    if fields["tracker_id"] != baseline["native_fields"]["qa_tracker_id"]:
        fail("QA tracker changed")
    attachments.attachments(issue)
    if open_required:
        attachments.ensure_open(issue, snapshot.get("statuses"))
    return issue


def preserved_qa(before: dict, after: dict) -> None:
    if publication.issue_fingerprint(before) != publication.issue_fingerprint(after):
        fail("QA fields or relations changed outside the approved conditions revision")
    preserved_attachments(before, after)


def revision_qa(root: Path, source: dict, revision: dict, after: dict, application: dict | None = None) -> None:
    before = revision["baseline"]
    if application is not None:
        from manage_revision_application import condition_qa_baseline
        before = condition_qa_baseline(saved(root, application), revision, before)
    preserved_qa(before, after)


def preserved_attachments(before: dict, after: dict) -> None:
    existing = {a["id"]: a for a in attachments.attachments(after)}
    if any(existing.get(a["id"]) != a for a in attachments.attachments(before)):
        fail("QA lost or changed a pre-existing attachment")


def preserved_revision_attachments(revision: dict, issue: dict) -> None:
    preserved_attachments(revision["baseline"], issue)
    for operation in revision["operations"].values():
        for attempt in operation["attempts"]:
            if "baseline" in attempt:
                preserved_attachments(attempt["baseline"], issue)


def note_for(revision: dict, qa_id: int) -> str:
    doc = revision["document"]
    if doc is None:
        return (f"Condições de teste vigentes: revisão {revision['number']:03d}, entrega em Markdown.\n\n"
                + conditions_markdown(revision["proposal"]) + "\n"
                + f"[project-slices-conditions:{qa_id}:{revision['number']}:{digest(revision['proposal'])}]")
    return (f"Condições de teste vigentes: revisão {revision['number']:03d}, arquivo {doc['filename']}.\n"
            f"SHA-256: {doc['sha256']}\n"
            f"[project-slices-conditions:{qa_id}:{revision['number']}:{doc['sha256']}]")


def document(root: Path, revision: dict, source: dict) -> tuple[dict | None, bytes]:
    proposal = revision["proposal"]
    if not document_requested(proposal):
        return None, b""
    content = docx_bytes(proposal, revision["number"], digest(proposal), revision["source_approval"],
                         decomposition_revision=source["slices"]["current_revision"])
    filename = f"condicoes-teste-r{revision['number']:03d}.docx"
    return {"path": str(root / "slices" / filename), "filename": filename,
            "filesize": len(content), "sha256": hashlib.sha256(content).hexdigest(),
            "revision": revision["number"], "proposal_sha256": digest(proposal), "target_key": "qa",
            "description": f"Condições de teste — revisão {revision['number']:03d}"}, content


def preview(revision: dict, source: dict) -> str:
    doc = revision["document"]
    title = "Revisão das condições" if revision.get("change_review") is not None else "Revisão localizada das condições"
    if doc is None:
        return (f"# {title} — r{revision['number']:03d}\n\n"
                f"QA: #{source['qa_id']}\n\nMotivo: {revision['reason']}\n\n"
                f"Fonte estruturada: `{digest(revision['proposal'])}`\n\n"
                f"## Nota a publicar\n\n{note_for(revision, source['qa_id'])}\n\n"
                "A aprovação autoriza esta nota com as condições; descrição, campos, relações e anexos existentes são preservados.\n")
    return (f"# {title} — r{revision['number']:03d}\n\n"
            f"QA: #{source['qa_id']}\n\nMotivo: {revision['reason']}\n\n"
            f"Arquivo: [{doc['filename']}]({Path(doc['path']).as_uri()})\n\n"
            f"SHA-256: {doc['sha256']}\n\nDescrição do anexo: {doc['description']}\n\n"
            f"Fonte estruturada: `{digest(revision['proposal'])}`\n\n"
            f"## Nota a publicar após conferir o anexo\n\n{note_for(revision, source['qa_id'])}\n\n"
            "A aprovação autoriza somente este anexo e esta nota; os demais campos, relações e anexos são preservados.\n")


def facade(source: dict, revision: dict) -> dict:
    # Reuse the MCP upload/attachment response validator without changing the initial publication.
    value = copy.deepcopy(source["publication"])
    value["revisions"][-1]["test_document"] = revision["document"]
    return value


def matched_attachment(revision: dict, issue: dict) -> dict | None:
    preserved_revision_attachments(revision, issue)
    doc = revision["document"]
    before = {a["id"] for a in revision["baseline"]["attachments"]}
    after = attachments.attachments(issue)
    known = revision["operations"]["upload"]["attempts"][-1]["result"]["upload"].get("id")
    candidates = [a for a in after if a["id"] not in before and all(a.get(k) == doc[k] for k in ("filename", "filesize", "description"))]
    if known is not None:
        if any(a["id"] == known and a not in candidates for a in after):
            fail("uploaded attachment ID has divergent metadata")
        candidates = [a for a in candidates if a["id"] == known]
    elif any(a["id"] not in before and a.get("filename") == doc["filename"] and a not in candidates for a in after):
        fail("attachment evidence is divergent")
    if len(candidates) > 1:
        fail("attachment evidence is ambiguous")
    return candidates[0] if candidates else None


def attachment_verified(revision: dict, issue: dict) -> bool:
    return revision["document"] is None or matched_attachment(revision, issue) is not None


def matched_note(revision: dict, issue: dict, qa_id: int) -> dict | None:
    journals = issue.get("journals")
    if not isinstance(journals, list) or any(not isinstance(j, dict) for j in journals):
        fail("readback must explicitly include complete QA journals")
    ids = [publication.positive_int(j.get("id"), "journal.id") for j in journals]
    if len(ids) != len(set(ids)):
        fail("duplicate journal IDs")
    expected = note_for(revision, qa_id)
    marker = expected.splitlines()[-1]
    if any(marker in str(j.get("notes", "")) and j.get("notes") != expected for j in journals):
        fail("current document note has divergent content; discuss reconciliation")
    candidates = [j for j in journals if j.get("notes") == expected]
    if len(candidates) > 1:
        fail("current document note is ambiguous; discuss reconciliation")
    return candidates[0] if candidates else None


def initial_source(root: Path) -> dict:
    slices_path = root / ".flow" / "slices-state.json"
    publication_path = root / ".flow" / "slices-publication.json"
    slices, _, published, _ = approved_sources(slices_path, publication_path)
    if not {"test_document", "conditions_delivery"} & published["revisions"][-1].keys():
        fail("historical QA without published conditions requires the explicit adoption workflow")
    readback = Path(published["readback"]["path"])
    if file_digest(readback) != published["readback"]["sha256"]:
        fail("initial publication readback changed")
    return {"slices": preserve(root, slices_path.read_bytes()), "publication": preserve(root, publication_path.read_bytes()),
            "readback": preserve(root, readback.read_bytes()),
            "slices_live_sha256": file_digest(slices_path), "publication_live_sha256": file_digest(publication_path)}


def source_data(root: Path, references: dict) -> dict:
    publication.exact(references, {"slices", "publication", "readback", "slices_live_sha256", "publication_live_sha256"}, "revision sources")
    slices = saved(root, references["slices"])
    published = saved(root, references["publication"])
    if any(references[key]["sha256"] != references[f"{key}_live_sha256"] for key in ("slices", "publication")):
        fail("baseline references differ from approved source bytes")
    from manage_slices import validate_state
    validate_state(slices)
    publication.validate_publication_state(published, check_files=False)
    revision = slices["revisions"][-1]
    approvals = [a for a in slices["approvals"] if a["status"] == "valid" and a["revision"] == revision["number"]]
    if slices["status"] != "approved" or len(approvals) != 1 or published["status"] != "completed":
        fail("conditions revision requires a completed approved publication")
    current = published["revisions"][-1]
    if current["slicing_revision"] != revision["number"] or current["slicing_approval_sha256"] != digest(approvals[0]) or not {"test_document", "conditions_delivery"} & current.keys():
        fail("conditions baseline differs from approved publication")
    readback = saved(root, references["readback"])
    qa_id = publication.child_remote_id(published, "qa")
    original_qa = [c for c in readback["children"] if c.get("id") == qa_id]
    if references["readback"]["sha256"] != published["readback"]["sha256"] or len(original_qa) != 1:
        fail("initial publication QA evidence differs")
    return {"slices": slices, "publication": published, "proposal": revision["proposal"], "original_qa": original_qa[0],
            "qa_id": publication.child_remote_id(published, "qa"), "actor": approvals[0]["approved_by"]}


def replay(root: Path, state: dict) -> tuple[dict, list[dict]]:
    publication.exact(state, {"schema_version", "source", "events"}, "conditions revision state")
    if state["schema_version"] != 1 or not isinstance(state["events"], list):
        fail("invalid conditions revision state")
    reject_secrets(state)
    source = source_data(root, state["source"])
    revisions = []
    history = copy.deepcopy(source["slices"]["revisions"])
    previous = digest(state["source"])
    for event in state["events"]:
        publication.exact(event, {"action", "actor", "at", "data", "previous_sha256", "sha256"}, "revision event")
        if event["previous_sha256"] != previous or event["sha256"] != digest({k: v for k, v in event.items() if k != "sha256"}):
            fail("conditions revision history hash differs")
        previous = event["sha256"]
        require_text(event["actor"], "actor")
        require_timestamp(event["at"], "at")
        action, data = event["action"], event["data"]
        if action == "propose":
            publication.exact(data, {"proposal", "reason", "snapshot", "word_review", "unchanged_behavior"} | ({"change_review"} if "change_review" in data else set()), "conditions proposal")
            if revisions and revisions[-1]["status"] != "completed" and revisions[-1]["operations"]:
                fail("remote progress must be reconciled before another proposal")
            candidate = data["proposal"]
            if not isinstance(candidate, dict):
                fail("conditions proposal must be an object")
            latest = next((r["proposal"] for r in reversed(revisions) if r["status"] == "completed"), source["proposal"])
            review_ref = data.get("change_review")
            if review_ref is not None:
                review = approved_change(root, review_ref, current=False)
                if review["classification"] == "functional":
                    change_review.validate_condition_delta(review, candidate)
                else:
                    expected = copy.deepcopy(latest)
                    expected["feature"]["requirement_sha256"] = review["current_requirement"]["sha256"]
                    expected["requirements"] = review["conditions"]["requirements"]
                    if data["unchanged_behavior"] is not True or {k: v for k, v in candidate.items() if k != "test_conditions"} != {k: v for k, v in expected.items() if k != "test_conditions"}:
                        fail("editorial continuity requires unchanged behavior and the approved requirement")
            elif {k: v for k, v in candidate.items() if k != "test_conditions"} != {k: v for k, v in latest.items() if k != "test_conditions"} or data["unchanged_behavior"] is not True:
                fail("resolve changed or contradictory behavior in the requirement before localized approval")
            try:
                validate_conditions(candidate)
                history.append({"proposal": candidate})
                validate_condition_history(history)
            except ValueError as error:
                fail(str(error))
            require_text(data["reason"], "reason")
            qa = qa_snapshot(source, saved(root, data["snapshot"]), open_required=True)
            parent = saved(root, data["snapshot"]).get("parent", {})
            if parent.get("id") != source["proposal"]["feature"]["issue_id"]:
                fail("proposal snapshot requires the current parent execution status")
            publication.named_id(parent, "status")
            preserved_attachments(source["original_qa"], qa)
            if revisions:
                last_published = next((r for r in reversed(revisions) if r["status"] == "completed"), None)
                if last_published:
                    preserved_revision_attachments(last_published, qa)
                    if not attachment_verified(last_published, qa) or matched_note(last_published, qa, source["qa_id"]) is None:
                        fail("QA no longer contains the current document and note")
            if data["word_review"] is not None:
                review = data["word_review"]
                publication.exact(review, {"original", "edited", "comparison_sha256", "resolution"}, "Word review")
                original = saved(root, review["original"], binary=True)
                edited = saved(root, review["edited"], binary=True)
                latest = next((r["document"] for r in reversed(revisions) if r["status"] == "completed"), source["publication"]["revisions"][-1].get("test_document"))
                if latest is None or review["original"]["sha256"] != latest["sha256"] or digest(word_comparison(original, edited)) != review["comparison_sha256"]:
                    fail("Word comparison does not match the current document")
                require_text(review["resolution"], "Word incorporation and ambiguity resolution")
            revisions.append({"number": source["slices"]["current_revision"] + len(revisions) + 1,
                              "proposal": candidate, "reason": data["reason"], "baseline": qa,
                              "status": "proposed", "operations": {}, "source_approval": None, "parent_baseline": parent})
            if review_ref is not None:
                revisions[-1]["change_review"] = review_ref
            continue
        if not revisions:
            fail("revision event requires a recorded proposal")
        revision = revisions[-1]
        if action in {"approve-source", "reject", "approve-publication"}:
            if event["actor"] != source["actor"]:
                fail("only the decomposition tech lead may approve or reject conditions")
        if action == "approve-source":
            publication.exact(data, {"proposal_sha256"}, "source decision")
            if revision["status"] != "proposed" or data["proposal_sha256"] != digest(revision["proposal"]):
                fail("source decision differs from the proposed conditions")
            revision.update(status="source-approved", source_approval={"approved_by": event["actor"], "approved_at": event["at"]})
        elif action == "reject":
            publication.exact(data, {"reason"}, "rejection")
            require_text(data["reason"], "rejection reason")
            if revision["operations"] or revision["status"] in {"completed", "rejected"}:
                fail("cannot reject a completed revision or discard remote progress")
            revision["status"] = "rejected"
        elif action in {"prepare-document", "prepare-preview"}:
            publication.exact(data, {"document", "preview_sha256"}, "document preview")
            if revision["status"] != "source-approved":
                fail("document generation requires approved structured conditions")
            expected, _ = document(root, revision, source)
            revision["document"] = expected
            if data["document"] != expected or data["preview_sha256"] != digest(preview(revision, source)):
                fail("document preview differs from approved source")
            revision.update(status="prepared", preview_sha256=data["preview_sha256"])
        elif action == "approve-publication":
            publication.exact(data, {"preview_sha256"}, "publication decision")
            if revision["status"] != "prepared" or data["preview_sha256"] != revision["preview_sha256"]:
                fail("publication approval differs from the exact preview")
            revision["status"] = "approved"
        elif action.startswith(("begin-", "finish-", "observe-")):
            operation_event(root, source, revision, event)
        elif action == "complete":
            publication.exact(data, {"snapshot"} | ({"application"} if "application" in data else set()), "revision readback")
            required_operations = ("upload", "attachment", "note") if revision.get("document") is not None else ("note",)
            if revision["status"] != "publishing" or any(revision["operations"].get(k, {}).get("status") != "completed" for k in required_operations):
                fail("revision requires its verified conditions note and any requested attachment")
            snapshot = saved(root, data["snapshot"])
            issue = qa_snapshot(source, snapshot)
            revision_qa(root, source, revision, issue, data.get("application"))
            parent = snapshot.get("parent", {})
            initial = revision["parent_baseline"]
            if parent.get("id") != initial["id"] or publication.named_id(parent, "status") != publication.named_id(initial, "status"):
                fail("parent execution status changed")
            if not attachment_verified(revision, issue) or matched_note(revision, issue, source["qa_id"]) is None:
                fail("final readback lacks current document or note")
            revision["status"] = "completed"
        else:
            fail("unknown conditions revision event")
    return source, revisions


def operation_event(root: Path, source: dict, revision: dict, event: dict) -> None:
    action, data = event["action"], event["data"]
    verb, kind = action.split("-", 1)
    if kind not in {"upload", "attachment", "note"} or revision["status"] not in {"approved", "publishing"}:
        fail("operation requires an approved document publication")
    has_document = revision["document"] is not None
    if kind in {"upload", "attachment"} and not has_document:
        fail("this revision publishes Markdown conditions without an attachment")
    operations = revision["operations"]
    op = operations.setdefault(kind, {"status": "pending", "attempts": [], "observations": []})
    if op["status"] == "completed":
        fail("confirmed operation must not be repeated")
    if verb == "begin":
        publication.exact(data, (set() if kind == "upload" else {"snapshot"}) | ({"application"} if "application" in data else set()), "operation intention")
        if kind == "upload":
            if "attachment" in operations:
                fail("cannot reupload after an attachment intention")
        else:
            if has_document and operations.get("upload", {}).get("status") != "completed":
                fail("attachment requires confirmed upload")
            if has_document and kind == "note" and operations.get("attachment", {}).get("status") != "completed":
                fail("current document note requires verified attachment")
            issue = qa_snapshot(source, saved(root, data["snapshot"]), open_required=True)
            revision_qa(root, source, revision, issue, data.get("application"))
            if kind == "note" and not attachment_verified(revision, issue):
                fail("current document note requires the verified attachment in the fresh snapshot")
            found = matched_attachment(revision, issue) if kind == "attachment" else matched_note(revision, issue, source["qa_id"])
            if found is not None:
                fail("operation already present; observe it before retry")
            if op["attempts"] and (not op["observations"] or op["observations"][-1]["attempt"] != len(op["attempts"]) or op["observations"][-1]["outcome"] != "absent"):
                fail("retry requires readback reconciliation of the previous attempt")
        op["attempts"].append({"outcome": "in-flight", "result": None, **({"baseline": issue} if kind != "upload" else {})})
        revision["status"] = "publishing"
    elif verb == "finish":
        publication.exact(data, {"attempt", "result"}, "operation response")
        if data["attempt"] != len(op["attempts"]) or not op["attempts"] or op["attempts"][-1]["result"] is not None:
            fail("result must finish the current in-flight attempt")
        if kind == "note":
            fail("note results require journal observation, not a textual MCP acknowledgement")
        result = saved(root, data["result"])
        outcome = attachments.result_outcome(facade(source, revision), kind, result)
        op["attempts"][-1].update(result=result, outcome=outcome)
        if kind == "upload" and outcome == "completed":
            op["status"] = "completed"
    elif verb == "observe":
        publication.exact(data, {"snapshot"} | ({"application"} if "application" in data else set()), "operation observation")
        if kind == "upload" or not op["attempts"]:
            fail("observation requires an unresolved attachment or note intention")
        issue = qa_snapshot(source, saved(root, data["snapshot"]))
        revision_qa(root, source, revision, issue, data.get("application"))
        preserved_revision_attachments(revision, issue)
        found = matched_attachment(revision, issue) if kind == "attachment" else matched_note(revision, issue, source["qa_id"])
        op["observations"].append({"attempt": len(op["attempts"]), "outcome": "matched" if found else "absent", "remote_id": found["id"] if found else None})
        if found:
            op["status"] = "completed"
    else:
        fail("unknown operation action")


def approved_change(root: Path, reference: dict, *, current: bool) -> dict:
    publication.exact(reference, {"path", "sha256", "source_path", "review_sha256"}, "requirement review reference")
    require_exact_path(Path(reference["source_path"]), root / ".flow" / "slices-change-review.json", "requirement review")
    if file_digest(Path(reference["path"])) != reference["sha256"]:
        fail("requirement review evidence changed")
    state = load_json(Path(reference["source_path"] if current else reference["path"]))
    change_review.validate_state(state, check_current=current)
    review = state["revisions"][-1]
    if review["review_sha256"] != reference["review_sha256"] or "conditions" not in review:
        fail("requirement review was superseded or has no conditions impact")
    if not any(d["revision"] == review["number"] and d["decision"] == "approved" for d in state["decisions"]):
        fail("conditions require an approved semantic requirement review")
    return review


def review_reference(root: Path, value: str) -> dict:
    path = Path(value).absolute()
    require_exact_path(path, root / ".flow" / "slices-change-review.json", "requirement review")
    state = load_json(path)
    frozen = change_review.freeze_evidence(path, root / ".flow" / "review-evidence")
    reference = {"path": str(frozen), "sha256": file_digest(frozen), "source_path": str(path),
                 "review_sha256": state["revisions"][-1]["review_sha256"]}
    approved_change(root, reference, current=True)
    return reference


def authority(root: Path, state: dict, source: dict, revision: dict | None = None, *, check_document: bool = False) -> None:
    for key, name in (("slices", "slices-state.json"), ("publication", "slices-publication.json")):
        if file_digest(root / ".flow" / name) != state["source"][f"{key}_live_sha256"]:
            fail("approved source changed; reconcile requirement or publication before continuing")
    _, _, flow_state, approval, _ = validate_feature_approval(root)
    expected = source["proposal"] if revision is None else revision["proposal"]
    if revision is not None and revision.get("change_review") is not None:
        review = approved_change(root, revision["change_review"], current=True)
        expected_sha = review["current_requirement"]["sha256"]
    else:
        expected_sha = expected["feature"]["requirement_sha256"]
    if approval["subject_sha256"] != expected_sha or flow_state["redmine"]["issue_id"] != source["proposal"]["feature"]["issue_id"]:
        fail("requirement changed; resolve it before localized conditions approval")
    if check_document and revision and revision.get("document") is not None:
        if file_digest(Path(revision["document"]["path"])) != revision["document"]["sha256"]:
            fail("DOCX changed after preview; incorporate Word edits and approve a new revision")


def append_event(state: dict, action: str, actor: str, at: str, data: dict) -> None:
    event = {"action": action, "actor": require_text(actor, "actor"), "at": require_timestamp(at, "at"),
             "data": data, "previous_sha256": state["events"][-1]["sha256"] if state["events"] else digest(state["source"])}
    event["sha256"] = digest(event)
    state["events"].append(event)


def command(args: argparse.Namespace) -> None:
    path = Path(args.state).absolute()
    root = root_for(path)
    action = args.action
    state = load_json(path) if path.exists() else {"schema_version": 1, "source": initial_source(root), "events": []}
    if not isinstance(state, dict):
        fail("conditions revision state must be an object")
    if path.exists() and not state.get("events"):
        fail("persisted conditions revision history cannot be empty")
    source, revisions = replay(root, state)
    current = revisions[-1] if revisions else None
    if action == "validate":
        if not path.exists():
            fail("conditions revision state does not exist")
        if args.previous:
            old = load_json(Path(args.previous))
            replay(root, old)
            if state["source"] != old["source"] or state["events"][:len(old["events"])] != old["events"]:
                fail("conditions revision history is append-only")
        print(json.dumps({"status": current["status"] if current else "empty", "revisions": len(revisions),
                          "current_proposal": next((r["proposal"] for r in reversed(revisions) if r["status"] == "completed"), source["proposal"]),
                          "current_conditions": next((r["proposal"]["test_conditions"] for r in reversed(revisions) if r["status"] == "completed"), source["proposal"]["test_conditions"]),
                          "current_document": next((r["document"] for r in reversed(revisions) if r["status"] == "completed"), source["publication"]["revisions"][-1].get("test_document"))}))
        return
    if action == "compare-word":
        approved = next((r for r in reversed(revisions) if r["status"] == "completed"), None)
        if args.change_review:
            approved = {"proposal": source["proposal"], "change_review": review_reference(root, args.change_review)}
        authority(root, state, source, approved)
        require_exact_path(Path(args.output), root / ".work" / "word-review.json", "Word comparison output")
        latest = next((r["document"] for r in reversed(revisions) if r["status"] == "completed"), source["publication"]["revisions"][-1].get("test_document"))
        original = Path(args.original)
        edited = Path(args.edited)
        if latest is None or file_digest(original) != latest["sha256"]:
            fail("Word comparison requires an unchanged copy of the current published document")
        assert_safe_read(edited)
        comparison = word_comparison(original.read_bytes(), edited.read_bytes())
        output = {"original": preserve(root, original.read_bytes()), "edited": preserve(root, edited.read_bytes()),
                  "comparison_sha256": digest(comparison), "comparison": comparison}
        reject_secrets(output)
        atomic_write(Path(args.output), canonical_bytes(output) + b"\n")
        print(json.dumps(output, ensure_ascii=False))
        return
    # Recording received results and observations remains possible after local changes.
    review_ref = None
    if action == "propose" and args.change_review:
        review_ref = review_reference(root, args.change_review)
    if action not in {"finish-upload", "finish-attachment", "observe-attachment", "observe-note", "reject"}:
        candidate_authority = current
        if action == "propose":
            candidate_authority = next((r for r in reversed(revisions) if r["status"] == "completed"), None)
            if review_ref is not None:
                candidate_authority = {"proposal": source["proposal"], "change_review": review_ref}
        authority(root, state, source, candidate_authority, check_document=action.startswith("begin-") or action == "approve-publication")
    if current and current.get("change_review") is not None and (action.startswith("begin-") or action == "approve-publication"):
        review = approved_change(root, current["change_review"], current=True)
        if review["classification"] == "functional":
            from manage_revision_application import condition_application_authority
            condition_application_authority(root, current, require_operations=action.startswith("begin-"))
    data = {}
    pending_files = {}
    if action == "propose":
        candidate = load_json(Path(args.proposal))
        word_review = None
        if args.word_review:
            report = load_json(Path(args.word_review))
            word_review = {k: report[k] for k in ("original", "edited", "comparison_sha256")}
            word_review["resolution"] = require_text(args.resolution, "Word resolution")
        data = {"proposal": candidate, "reason": args.reason, "snapshot": evidence(root, args.snapshot),
                "word_review": word_review, "unchanged_behavior": args.unchanged_behavior}
        if review_ref is not None:
            data["change_review"] = review_ref
    elif action == "approve-source":
        data = {"proposal_sha256": args.sha256}
    elif action == "reject":
        data = {"reason": args.reason}
    elif action in {"prepare-document", "prepare-preview"}:
        if not current or current["status"] != "source-approved":
            fail("document generation requires approved structured conditions")
        doc, content = document(root, current, source)
        if doc is not None:
            output = Path(doc["path"])
            assert_safe_write(output)
            if output.exists() and file_digest(output) != doc["sha256"]:
                fail("existing DOCX differs; preserve Word edits and record a new revision")
            pending_files[output] = content
        temporary = {**current, "document": doc}
        data = {"document": doc, "preview_sha256": digest(preview(temporary, source))}
        preview_path = root / "slices" / f"conditions-revision-r{current['number']:03d}.md"
        pending_files[preview_path] = preview(temporary, source).encode("utf-8")
    elif action == "approve-publication":
        if not current or "document" not in current:
            fail("publication requires an exact document preview")
        preview_path = root / "slices" / f"conditions-revision-r{current['number']:03d}.md"
        assert_safe_read(preview_path)
        if preview_path.read_text(encoding="utf-8") != preview(current, source):
            fail("publication preview changed; prepare a new revision")
        data = {"preview_sha256": args.sha256}
    elif action.startswith("finish-"):
        data = {"attempt": args.attempt, "result": evidence(root, args.result)}
    elif action != "begin-upload":
        data = {"snapshot": evidence(root, args.snapshot)}
    if "snapshot" in data and action != "propose" and current and current.get("change_review") is not None:
        review = approved_change(root, current["change_review"], current=False)
        if review["classification"] == "functional":
            application_path = root / ".flow" / "slices-revision-application.json"
            data["application"] = evidence(root, str(application_path))
    append_event(state, action, args.actor, args.at, data)
    source, revisions = replay(root, state)
    current = revisions[-1]
    publication.atomic_batch_write({**pending_files, path: canonical_bytes(state) + b"\n"})
    output = {"status": current["status"], "revision": current["number"], "proposal_sha256": digest(current["proposal"])}
    if "document" in current:
        output.update(document=current["document"], preview_sha256=current["preview_sha256"])
    if action.startswith("begin-"):
        kind = action.split("-", 1)[1]
        output["attempt_id"] = len(current["operations"][kind]["attempts"])
        if kind == "upload":
            tool, arguments = "redmine_upload_file", {"path": current["document"]["path"], "expected_sha256": current["document"]["sha256"]}
        elif kind == "attachment":
            upload = current["operations"]["upload"]["attempts"][-1]["result"]["upload"]
            tool, arguments = "redmine_attach_file", {"issue_id": source["qa_id"], "token": upload["token"], "filename": current["document"]["filename"], "description": current["document"]["description"]}
        else:
            tool, arguments = "redmine_add_comment", {"issue_id": source["qa_id"], "notes": note_for(current, source["qa_id"])}
        output.update(tool=tool, arguments=arguments)
    print(json.dumps(output, ensure_ascii=False))


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="action", required=True)
    for action in ("propose", "approve-source", "reject", "prepare-document", "prepare-preview", "approve-publication", "begin-upload", "finish-upload",
                   "begin-attachment", "finish-attachment", "observe-attachment", "begin-note", "observe-note", "complete", "compare-word", "validate"):
        child = commands.add_parser(action)
        child.add_argument("state")
        if action not in {"validate", "compare-word"}:
            child.add_argument("--actor", required=True)
            child.add_argument("--at", required=True)
        if action == "propose":
            child.add_argument("proposal")
            child.add_argument("--unchanged-behavior", action="store_true")
            child.add_argument("--word-review")
            child.add_argument("--resolution")
        if action in {"propose", "reject"}:
            child.add_argument("--reason", required=True)
        if action in {"propose", "begin-attachment", "observe-attachment", "begin-note", "observe-note", "complete"}:
            child.add_argument("--snapshot", required=True)
        if action in {"approve-source", "approve-publication"}:
            child.add_argument("--sha256", required=True)
        if action.startswith("finish-"):
            child.add_argument("--attempt", type=int, required=True)
            child.add_argument("--result", required=True)
        if action == "compare-word":
            for name in ("original", "edited", "output"):
                child.add_argument(f"--{name}", required=True)
        if action in {"propose", "compare-word"}:
            child.add_argument("--change-review")
        if action == "validate":
            child.add_argument("--previous")
    try:
        command(parser.parse_args())
        return 0
    except (ContractError, ValueError, KeyError, TypeError, OSError, ET.ParseError, BadZipFile):
        # Do not echo untrusted document contents, paths with credentials, or remote errors.
        error = sys.exc_info()[1]
        print(f"condition revision rejected: {error}" if isinstance(error, ContractError) else "condition revision rejected: invalid local input or unavailable file", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
