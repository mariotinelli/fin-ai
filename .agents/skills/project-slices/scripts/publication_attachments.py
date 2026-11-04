"""Local document approval and attachment reconciliation; no remote access."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from manage_slices import ContractError, assert_safe_read, canonical_bytes, digest, file_digest, load_json, require_text, require_timestamp, reject_secrets
from test_conditions import docx_bytes


def api():
    # Imported lazily so the CLI and its contract consumers share the same helpers.
    import manage_publication
    return manage_publication


def fail(message: str) -> None:
    raise ContractError(message)


def has_progress(state: dict) -> bool:
    return any(op.get("attempts") for op in state["operations"].values())


def document_for(slices_path: Path, revision: dict, approval: dict) -> dict:
    if "test_conditions" not in revision["proposal"]:
        fail("new publication requires approved test conditions and DOCX")
    filename = f"condicoes-teste-r{revision['number']:03d}.docx"
    path = slices_path.parent.parent / "slices" / filename
    assert_safe_read(path)
    content = path.read_bytes()
    if content != docx_bytes(revision["proposal"], revision["number"], revision["proposal_sha256"], approval):
        fail("DOCX differs from the approved structured source; incorporate and review Word edits first")
    return {
        "path": str(path.absolute()), "filename": filename, "filesize": len(content),
        "sha256": hashlib.sha256(content).hexdigest(), "revision": revision["number"],
        "proposal_sha256": revision["proposal_sha256"], "target_key": "qa",
        "description": f"Condições de teste — revisão {revision['number']:03d}",
    }


def validate_document(current: dict) -> None:
    p = api()
    doc = current["test_document"]
    p.exact(doc, {"path", "filename", "filesize", "sha256", "revision", "proposal_sha256", "target_key", "description"}, "test document")
    p.positive_int(doc["revision"], "document revision")
    p.positive_int(doc["filesize"], "document filesize")
    filename = f"condicoes-teste-r{doc['revision']:03d}.docx"
    expected = Path(current["slices_state_path"]).parent.parent / "slices" / filename
    if doc["revision"] != current["slicing_revision"] or doc["filename"] != filename or doc["path"] != str(expected.absolute()) or doc["target_key"] != "qa":
        fail("test document differs from its approved revision or canonical path")
    for name in ("sha256", "proposal_sha256"):
        if not isinstance(doc[name], str) or len(doc[name]) != 64 or any(c not in "0123456789abcdef" for c in doc[name]):
            fail("invalid document hash")
    if doc["description"] != f"Condições de teste — revisão {doc['revision']:03d}":
        fail("document description must identify its revision")


def verify_file(current: dict, revision: dict, approval: dict) -> None:
    if "test_document" in current and document_for(Path(current["slices_state_path"]), revision, approval) != current["test_document"]:
        fail("approved publication DOCX changed")


def preview(current: dict) -> str:
    doc = current["test_document"]
    qa = next(child for child in current["children"] if child["key"] == "qa")
    destination = f"#{qa['remote_id']} — {qa['title']} (QA adotada)" if qa.get("source") == "adopted" else qa["title"]
    return "\n## Documento a anexar — incluído nesta aprovação final\n\n" + "\n".join([
        f"- Destino: {destination}", f"- Arquivo: [{doc['filename']}]({Path(doc['path']).as_uri()})",
        f"- Revisão: {doc['revision']:03d}", f"- Tamanho: {doc['filesize']} bytes",
        f"- SHA-256: `{doc['sha256']}`", f"- Descrição do anexo: {doc['description']}",
        "- A aprovação autoriza acrescentar exatamente este documento, preservando os demais campos e anexos da QA.",
    ]) + "\n"


def ensure_open(issue: dict, statuses: Any) -> None:
    status_id = api().named_id(issue, "status")
    matches = [s for s in statuses if isinstance(s, dict) and s.get("id") == status_id] if isinstance(statuses, list) else []
    if len(matches) != 1 or not isinstance(matches[0].get("is_closed"), bool):
        fail("QA requires unambiguous native is_closed status evidence")
    if matches[0]["is_closed"]:
        fail("QA is completed; discuss the impact with the tech lead before attaching")


def check_adopted(current: dict) -> None:
    qa = next(c for c in current["children"] if c["key"] == "qa")
    if qa.get("source") == "adopted":
        snapshot = load_json(Path(current["existing_children_review"]["snapshot_path"]))
        issue = next(i for i in snapshot["children"] if i["id"] == qa["remote_id"])
        metadata = load_json(Path(current["metadata_baseline"]["path"]))
        ensure_open(issue, metadata["statuses"])


def attachments(issue: dict) -> list[dict]:
    values = issue.get("attachments")
    if not isinstance(values, list) or any(not isinstance(a, dict) for a in values):
        fail("readback must explicitly include the complete QA attachments")
    ids = [api().positive_int(a.get("id"), "attachment.id") for a in values]
    if len(ids) != len(set(ids)):
        fail("duplicate attachment IDs in evidence")
    return values


def evidence(current: dict, path: str) -> tuple[dict, dict]:
    location = api().current_evidence_path(current, path, "attachment evidence")
    snapshot = load_json(location)
    reject_secrets(snapshot)
    return snapshot, {"path": str(location.absolute()), "sha256": file_digest(location)}


def saved_evidence(current: dict, reference: dict) -> dict:
    api().exact(reference, {"path", "sha256"}, "attachment evidence reference")
    snapshot, actual = evidence(current, reference["path"])
    if actual != reference:
        fail("attachment evidence changed")
    return snapshot


def upload_result(state: dict) -> dict:
    op = state["operations"].get("upload:qa", {})
    if op.get("status") != "completed" or not op.get("attempts"):
        fail("attachment requires a confirmed upload")
    return op["attempts"][-1]["result"]


def match_attachment(state: dict, issue: dict, baseline: dict) -> dict | None:
    p = api()
    current = state["revisions"][-1]
    doc = current["test_document"]
    qa = p.current_child(state, "qa")
    if issue.get("id") != p.child_remote_id(state, "qa"):
        fail("attachment readback belongs to another issue")
    p.compare_issue(qa, issue, current["parent_baseline"], current["native_fields"])
    before = attachments(baseline)
    after = attachments(issue)
    by_id = {a["id"]: a for a in after}
    if any(by_id.get(a["id"]) != a for a in before):
        fail("QA lost or changed a pre-existing attachment")
    known_id = upload_result(state)["upload"].get("id")
    previous_ids = {a["id"] for a in before}
    candidates = [a for a in after if a["id"] not in previous_ids and all(a.get(k) == doc[k] for k in ("filename", "filesize", "description"))]
    if known_id is not None:
        if known_id in by_id and (known_id in previous_ids or by_id[known_id] not in candidates):
            fail("uploaded attachment ID has divergent metadata")
        candidates = [a for a in candidates if a["id"] == known_id]
    elif any(a["id"] not in previous_ids and a.get("filename") == doc["filename"] and a not in candidates for a in after):
        fail("attachment evidence is divergent; discuss reconciliation with the tech lead")
    if len(candidates) > 1:
        fail("attachment evidence is ambiguous; discuss reconciliation with the tech lead")
    return candidates[0] if candidates else None


def validate_operations(state: dict, check_files: bool = True) -> None:
    p = api()
    current = state["revisions"][-1]
    for rev in state["revisions"]:
        if "test_document" in rev:
            validate_document(rev)
    document_revisions = [r["number"] for r in state["revisions"] if "test_document" in r]
    if document_revisions and any("test_document" not in r and "conditions_delivery" not in r for r in state["revisions"][min(document_revisions) - 1:]):
        fail("publication cannot drop its document contract")
    for key, kind in (("upload:qa", "upload"), ("attachment:qa", "attachment")):
        if key not in state["operations"]:
            continue
        if "test_document" not in current:
            fail("attachment operation requires an approved document contract")
        op = state["operations"][key]
        p.exact(op, {"kind", "attempts", "observations", "status", "remote_id"}, "document operation")
        if op["kind"] != kind or op["status"] not in {"pending", "completed"} or not isinstance(op["attempts"], list) or not op["attempts"] or not isinstance(op["observations"], list):
            fail("invalid document operation")
        for index, attempt in enumerate(op["attempts"], 1):
            base = {"id", "attempted_at", "payload_sha256", "observations_before", "outcome"}
            if kind == "attachment":
                base |= {"baseline", "payload"}
            extra = {"response_recorded_at", "result"} if "result" in attempt else set()
            p.exact(attempt, base | extra, "document attempt")
            if attempt["id"] != index or attempt["outcome"] not in {"in-flight", "completed", "failed", "unknown"}:
                fail("invalid document attempt history")
            require_timestamp(attempt["attempted_at"], "attempted_at")
            if not isinstance(attempt["observations_before"], int) or not 0 <= attempt["observations_before"] <= len(op["observations"]):
                fail("invalid observation boundary")
            expected_hash = digest(current["test_document"]) if kind == "upload" else digest(attempt["payload"])
            if attempt["payload_sha256"] != expected_hash:
                fail("document operation payload changed")
            if kind == "attachment":
                expected_payload = attachment_payload(state)
                if attempt["payload"] != expected_payload:
                    fail("attachment payload differs from approved upload or QA")
                if index > 1:
                    previous = op["attempts"][index - 2]
                    preceding = op["observations"][previous["observations_before"]:attempt["observations_before"]]
                    if previous["outcome"] in {"in-flight", "unknown"} and (not preceding or preceding[-1]["outcome"] != "absent" or preceding[-1]["attempt"] != previous["id"]):
                        fail("attachment retry lacks reconciliation of the previous attempt")
                    if any(o["outcome"] == "matched" for o in op["observations"][:attempt["observations_before"]]):
                        fail("confirmed attachment must not be repeated")
                if check_files:
                    before = saved_evidence(current, attempt["baseline"])
                    check_qa(state, before, require_open=True)
            if extra:
                require_timestamp(attempt["response_recorded_at"], "response_recorded_at")
                if attempt["outcome"] != result_outcome(state, kind, attempt["result"]):
                    fail("document result differs from recorded outcome")
            elif attempt["outcome"] != "in-flight":
                fail("document attempt outcome lacks its MCP result")
            if kind == "upload" and attempt["outcome"] == "completed" and index != len(op["attempts"]):
                fail("confirmed upload must not be repeated")
        for observation in op["observations"]:
            p.exact(observation, {"outcome", "observed_at", "snapshot", "attempt", "remote_id"}, "attachment observation")
            require_timestamp(observation["observed_at"], "observed_at")
            if kind != "attachment" or observation["outcome"] not in {"matched", "absent"} or not isinstance(observation["attempt"], int) or not 1 <= observation["attempt"] <= len(op["attempts"]):
                fail("invalid attachment observation")
            if check_files:
                observed = saved_evidence(current, observation["snapshot"])
                before = saved_evidence(current, op["attempts"][observation["attempt"] - 1]["baseline"])
                match = match_attachment(state, p.issue_object(observed), p.issue_object(before))
                if observation["remote_id"] != (match["id"] if match else None) or observation["outcome"] != ("matched" if match else "absent"):
                    fail("attachment observation differs from its evidence")
        confirmed = op["attempts"][-1]["outcome"] == "completed" if kind == "upload" else bool(op["observations"] and op["observations"][-1]["outcome"] == "matched")
        if (op["status"] == "completed") != confirmed:
            fail("document completion lacks confirmation")
        expected_id = op["attempts"][-1].get("result", {}).get("upload", {}).get("id") if kind == "upload" else (op["observations"][-1]["remote_id"] if confirmed else None)
        if op["remote_id"] != expected_id:
            fail("document remote ID differs from confirmed result")
    if "test_document" in current and state["status"] == "completed":
        if state["operations"].get("attachment:qa", {}).get("status") != "completed":
            fail("publication requires a verified QA attachment")
        if check_files:
            readback = saved_evidence(current, {k: state["readback"][k] for k in ("path", "sha256")})
            verify_complete(state, readback)


def result_outcome(state: dict, kind: str, result: dict) -> str:
    p = api()
    if result.get("stage") != ("upload" if kind == "upload" else "attach"):
        fail("MCP result belongs to another stage")
    outcome = result.get("outcome")
    if outcome in {"not_sent", "rejected", "unconfirmed"}:
        p.exact(result, {"stage", "outcome", "error"}, "MCP failure")
        p.exact(result["error"], {"code", "message", "http_status"}, "sanitized MCP error")
        require_text(result["error"]["code"], "error code")
        require_text(result["error"]["message"], "error message")
        return "unknown" if outcome == "unconfirmed" else "failed"
    if kind == "upload":
        p.exact(result, {"stage", "outcome", "upload", "file"}, "MCP upload")
        if outcome != "uploaded":
            fail("invalid upload outcome")
        upload = result["upload"]
        p.exact(upload, {"token"} | ({"id"} if "id" in upload else set()), "MCP upload reference")
        require_text(upload["token"], "upload token")
        if "id" in upload:
            p.positive_int(upload["id"], "upload.id")
        doc = state["revisions"][-1]["test_document"]
        if result["file"] != {k: doc[k] for k in ("filename", "filesize", "sha256")}:
            fail("MCP uploaded bytes differ from approved document")
        return "completed"
    p.exact(result, {"stage", "outcome", "issue_id", "verification_required"}, "MCP attachment")
    if outcome != "accepted" or result["issue_id"] != p.child_remote_id(state, "qa") or result["verification_required"] is not True:
        fail("invalid attachment acceptance")
    return "unknown"  # Acceptance never proves association; readback is mandatory.


def attachment_payload(state: dict) -> dict:
    doc = state["revisions"][-1]["test_document"]
    return {"issue_id": api().child_remote_id(state, "qa"), "token": upload_result(state)["upload"]["token"], "filename": doc["filename"], "description": doc["description"]}


def check_qa(state: dict, snapshot: dict, *, require_open: bool) -> dict:
    p = api()
    current = state["revisions"][-1]
    issue = p.issue_object(snapshot)
    if issue.get("id") != p.child_remote_id(state, "qa"):
        fail("attachment evidence belongs to another QA")
    if require_open:
        ensure_open(issue, snapshot.get("statuses"))
    p.compare_issue(p.current_child(state, "qa"), issue, current["parent_baseline"], current["native_fields"])
    attachments(issue)
    return issue


def verify_complete(state: dict, snapshot: dict) -> None:
    if "test_document" not in state["revisions"][-1]:
        if "conditions_delivery" not in state["revisions"][-1] and state["status"] != "completed" and not has_progress(state):
            fail("historical publication without remote progress requires test conditions and a new final preview")
        return
    op = state["operations"].get("attachment:qa", {})
    if op.get("status") != "completed":
        fail("publication requires a verified QA attachment")
    current = state["revisions"][-1]
    baseline = saved_evidence(current, op["attempts"][-1]["baseline"])
    qa_id = api().child_remote_id(state, "qa")
    matches = [i for i in snapshot["children"] if i.get("id") == qa_id]
    if len(matches) != 1:
        fail("final readback lacks QA")
    match = match_attachment(state, matches[0], api().issue_object(baseline))
    if match is None or match["id"] != op["remote_id"]:
        fail("final readback lacks the verified QA attachment")


def command(arguments: argparse.Namespace) -> None:
    p = api()
    path = Path(arguments.state)
    state = load_json(path)
    p.validate_publication_state(state)
    current = state["revisions"][-1]
    if "test_document" not in current or state["status"] not in {"approved", "publishing"}:
        fail("attachment operations require an approved document publication")
    action = arguments.action
    kind = "upload" if "upload" in action else "attachment"
    key = f"{kind}:qa"
    at = require_timestamp(arguments.at, "operation timestamp")
    if action.startswith("begin"):
        p.require_remote_authority(state)
        op = p.operation(state, key, kind)
        if kind == "upload":
            if op["status"] == "completed" or state["operations"].get("attachment:qa", {}).get("attempts"):
                fail("confirmed upload or attempted attachment must not be uploaded again")
            payload = {"path": current["test_document"]["path"], "expected_sha256": current["test_document"]["sha256"]}
            payload_sha = digest(current["test_document"])
            extra = {}
        else:
            p.check_retry(op)
            payload = attachment_payload(state)
            snapshot, reference = evidence(current, arguments.snapshot)
            check_qa(state, snapshot, require_open=True)
            # Preserve all earlier attachment baselines across retries.
            if op["attempts"]:
                previous = saved_evidence(current, op["attempts"][0]["baseline"])
                if match_attachment(state, p.issue_object(snapshot), p.issue_object(previous)) is not None:
                    fail("attachment already present; reconcile it before retry")
            payload_sha = digest(payload)
            extra = {"baseline": reference, "payload": payload}
        attempt = {"id": len(op["attempts"]) + 1, "attempted_at": at, "payload_sha256": payload_sha, "observations_before": len(op["observations"]), "outcome": "in-flight", **extra}
        op["attempts"].append(attempt)
        state["status"] = "publishing"
        state["status_history"].append({"status": "publishing", "recorded_at": at})
        output = {"attempt_id": attempt["id"], "tool": "redmine_upload_file" if kind == "upload" else "redmine_attach_file", "arguments": payload}
    elif action.startswith("finish"):
        op = state["operations"].get(key, {})
        if op.get("status") == "completed" or not op.get("attempts") or op["attempts"][-1]["id"] != arguments.attempt or op["attempts"][-1]["outcome"] != "in-flight":
            fail("result must finish the current in-flight document attempt")
        result, _ = evidence(current, arguments.result)
        outcome = result_outcome(state, kind, result)
        op["attempts"][-1].update(outcome=outcome, response_recorded_at=at, result=result)
        if kind == "upload" and outcome == "completed":
            op.update(status="completed", remote_id=result["upload"].get("id"))
        output = {"stage": kind, "outcome": outcome}
    else:
        op = state["operations"].get(key, {})
        if not op.get("attempts") or op["status"] == "completed":
            fail("observation requires an unresolved attachment attempt")
        snapshot, reference = evidence(current, arguments.snapshot)
        baseline = saved_evidence(current, op["attempts"][-1]["baseline"])
        match = match_attachment(state, p.issue_object(snapshot), p.issue_object(baseline))
        outcome = "matched" if match else "absent"
        op["observations"].append({"outcome": outcome, "observed_at": at, "snapshot": reference, "attempt": op["attempts"][-1]["id"], "remote_id": match["id"] if match else None})
        if match:
            op.update(status="completed", remote_id=match["id"])
        output = {"stage": kind, "outcome": outcome}
    p.validate_publication_state(state)
    p.atomic_write(path, canonical_bytes(state) + b"\n")
    print(json.dumps(output, ensure_ascii=False))


def register(commands) -> None:
    for action in ("begin-upload", "finish-upload", "begin-attachment", "finish-attachment", "observe-attachment"):
        parser = commands.add_parser(action)
        parser.add_argument("state")
        parser.add_argument("--at", required=True)
        if action.startswith("finish"):
            parser.add_argument("--attempt", type=int, required=True)
            parser.add_argument("--result", required=True)
        elif action != "begin-upload":
            parser.add_argument("--snapshot", required=True)
        parser.set_defaults(run=command, action=action)


def validate_previous(current: dict, previous: dict) -> None:
    for key in ("upload:qa", "attachment:qa"):
        old = previous["operations"].get(key)
        if old is None:
            continue
        new = current["operations"].get(key, {})
        if len(new.get("attempts", [])) < len(old["attempts"]) or new.get("observations", [])[:len(old["observations"])] != old["observations"]:
            fail("document operation history was removed or rewritten")
        if old["status"] == "completed" and new != old:
            fail("confirmed document operation must remain unchanged")
        for before, after in zip(old["attempts"], new.get("attempts", [])):
            if before["outcome"] != "in-flight" and before != after:
                fail("recorded document response was rewritten")
            stable = {k: v for k, v in before.items() if k not in {"outcome", "response_recorded_at", "result"}}
            if any(after.get(k) != v for k, v in stable.items()):
                fail("document attempt intention was rewritten")
