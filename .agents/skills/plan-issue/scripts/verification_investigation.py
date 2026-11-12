"""Bound inconclusive check investigation without converting a retry into approval."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Callable

from ralph_runtime import RuntimeFailure, atomic_json, sanitize_text


def read_history(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("original"), dict) or data["original"].get("status") != "failed" or data.get("used") is not True:
        raise RuntimeFailure("invalid investigation history; preserve evidence and inspect before resuming")
    return data


def resolve_failure(report: dict[str, Any], *, history_path: Path, archive_path: Path,
                    diagnose: Callable[[dict[str, Any], dict[str, Any] | None], dict[str, Any]],
                    reproduce: Callable[[], dict[str, Any]], confirm: Callable[[], dict[str, Any]],
                    same_inputs: Callable[[], bool]) -> dict[str, Any]:
    history = read_history(history_path)
    last_diagnosis: dict[str, Any] = {}

    def classify(current: dict[str, Any]) -> str:
        nonlocal last_diagnosis
        last_diagnosis = diagnose(current, history)
        return "correct" if any(item.get("kind") == "defect" for item in last_diagnosis.get("findings", [])) else "blocked"

    def outcome(action: str, current: dict[str, Any], reason: str = "") -> dict[str, Any]:
        return {"action": action, "report": current, "diagnosis": last_diagnosis, "history": history, "reason": reason}

    if not report.get("diagnosable") or report.get("source_modified"):
        return outcome("blocked", report, "Operational or source-safety failure is not eligible for automatic reproduction.")
    if classify(report) == "correct":
        return outcome("correct", report)
    request = last_diagnosis.get("investigation", {})
    if not isinstance(request, dict):
        return outcome("blocked", report, "Invalid investigation request; no reproduction is authorized.")
    if not request.get("requested"):
        return outcome("blocked", report)
    if request.get("requested") is not True or request.get("cause") != "inconclusive-test" or not isinstance(request.get("reason"), str) or not request["reason"].strip():
        return outcome("blocked", report, "Only an explicit inconclusive test diagnosis can request reproduction.")
    if history is not None:
        return outcome("blocked", report, "Automatic reproduction budget already used; original failure and all evidence remain pending review.")
    history = {"used": True, "status": "reproducing", "conclusion": "undetermined", "original": report,
               "reproduction": None, "confirmation": None, "request": request, "archive_path": str(archive_path)}

    def persist() -> None:
        atomic_json(archive_path, history)
        atomic_json(history_path, history)

    def stop(current: dict[str, Any], reason: str) -> dict[str, Any]:
        history.update(status="blocked", reason=reason)
        persist()
        return outcome("blocked", current, reason)

    persist()  # Consume the budget before launching another process, including interruption.
    try:
        if not same_inputs():
            return stop(report, "Verification inputs changed; results cannot establish intermittent behavior.")
        reproduction = reproduce()
        history["reproduction"] = reproduction
        persist()
        if not same_inputs():
            return stop(reproduction, "Verification inputs changed during reproduction; work preserved.")
        if reproduction.get("status") != "completed":
            if reproduction.get("diagnosable") and classify(reproduction) == "correct":
                history.update(status="defect", conclusion="defect-demonstrated")
                persist()
                return outcome("correct", reproduction)
            return stop(reproduction, "Failure remains unresolved after the single controlled reproduction.")
        history["status"] = "confirming"
        persist()
        confirmation = confirm()
        history["confirmation"] = confirmation
        persist()
        if not same_inputs():
            return stop(confirmation, "Verification inputs changed during confirmation; work preserved.")
        if confirmation.get("status") != "completed":
            if confirmation.get("diagnosable") and classify(confirmation) == "correct":
                history.update(status="defect", conclusion="defect-demonstrated")
                persist()
                return outcome("correct", confirmation)
            return stop(confirmation, "Required full verification failed again; no further automatic reproduction is allowed.")
        history.update(status="completed", conclusion="not-reproduced")
        persist()
        return outcome("recovered", confirmation, "Original failure was not reproduced; independent acceptance remains required.")
    except (RuntimeError, OSError, ValueError) as error:
        history.update(status="interrupted", reason=sanitize_text(str(error)))
        persist()
        raise
