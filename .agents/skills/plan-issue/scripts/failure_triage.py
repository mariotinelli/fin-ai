"""Validate routing evidence without requiring an established root cause."""
from __future__ import annotations

import re
from pathlib import Path, PurePosixPath
from typing import Any

from ralph_runtime import RuntimeFailure


ROUTES = {"correction", "development-investigation", "blocked"}


def selected_route(failures: list[dict[str, Any]]) -> str:
    return next((route for route in ("correction", "development-investigation", "blocked") if any(item["disposition"] == route for item in failures)), "blocked")


def normalize_triage(result: dict[str, Any], repo: Path, planning: str, phase_body: str) -> dict[str, Any]:
    if result.get("verdict") == "approved" or result.get("route") not in ROUTES or not isinstance(result.get("summary"), str) or not result["summary"].strip():
        raise RuntimeFailure("triage requires an explicit supported route and summary, never phase approval")
    failures = result.get("failures")
    if not isinstance(failures, list) or not failures:
        raise RuntimeFailure("triage requires observed failures")
    shared = re.split(r"^## Fase \d+\s+[—-]\s+", planning, maxsplit=1, flags=re.MULTILINE)[0]
    phase_text = " ".join((shared + "\n" + phase_body).split())
    rerouted = False
    def investigate_scope(item: dict[str, Any]) -> None:
        nonlocal rerouted
        item["unverified_basis"] = {key: item.get(key, "") for key in ("basis_source", "basis_path", "basis_quote")}
        item.update(disposition="development-investigation", blocker_type="none", blocker_condition="none", basis_source="mandatory-verifier")
        rerouted = True
    for item in failures:
        if not isinstance(item, dict):
            raise RuntimeFailure("invalid triage failure")
        for key in ("criterion", "behavior", "expected", "observed"):
            if not isinstance(item.get(key), str) or not item[key].strip():
                raise RuntimeFailure("triage requires an observable criterion, behavior, expectation and result")
        if not isinstance(item.get("existing_failure_id", ""), str) or item.get("disposition") not in ROUTES:
            raise RuntimeFailure("invalid failure identity or disposition")
        for key in ("test_refs", "evidence"):
            if not isinstance(item.get(key), list) or any(not isinstance(value, str) or not value.strip() for value in item[key]):
                raise RuntimeFailure("invalid failure references/evidence")
        if not item["evidence"]:
            raise RuntimeFailure("routing requires concrete evidence")
        if item.get("blocker_type") not in {"none", "external", "scope"}:
            raise RuntimeFailure("triage cannot decide safety or intervention budgets")
        condition = item.get("blocker_condition", "none")
        if condition not in {"none", "missing-runtime", "missing-credential", "unavailable-service", "requires-global-change", "scope-decision"}:
            raise RuntimeFailure("invalid blocker condition")
        if item["disposition"] == "blocked" and condition == "none":
            item.update(disposition="development-investigation", blocker_type="none")
            rerouted = True
        if item["disposition"] == "blocked" and item["blocker_type"] == "none":
            raise RuntimeFailure("unknown cause is not an external/scope blocker; use development investigation")
        if item["disposition"] != "blocked" and item["blocker_type"] != "none":
            raise RuntimeFailure("blocked external/scope work cannot be silently authorized")
        if item["disposition"] == "blocked" and ((item["blocker_type"] == "scope") != (condition == "scope-decision")):
            raise RuntimeFailure("blocker condition contradicts its owner")
        source = item.get("basis_source")
        quote = item.get("basis_quote", "")
        if not isinstance(quote, str):
            raise RuntimeFailure("invalid scope basis")
        if source == "phase":
            if not quote.strip() or " ".join(quote.split()) not in phase_text:
                if item["disposition"] != "blocked":
                    investigate_scope(item)
        elif source == "standard":
            name = item.get("basis_path", "")
            relative = PurePosixPath(name)
            if not name or relative.is_absolute() or relative.as_posix() != name or ".." in relative.parts or "\\" in name or ":" in name or any(part.casefold() in {".git", ".flow", ".ssh"} or part.casefold().startswith(".env") for part in relative.parts):
                raise RuntimeFailure("invalid repository standard path")
            candidate = repo / name
            if any(path.is_symlink() for path in (candidate, *candidate.parents) if path != repo and repo in path.parents) or not candidate.resolve().is_relative_to(repo.resolve()):
                raise RuntimeFailure("repository standard path is unsafe")
            if not candidate.is_file() or not quote.strip() or " ".join(quote.split()) not in " ".join(candidate.read_text(encoding="utf-8").split()):
                if item["disposition"] != "blocked":
                    investigate_scope(item)
        elif source == "mandatory-verifier":
            if item["disposition"] == "correction":
                investigate_scope(item)
        else:
            raise RuntimeFailure("failure requires a phase, standard or mandatory verifier basis")
    route = selected_route(failures)
    if result["route"] != route and not rerouted:
        raise RuntimeFailure("triage route contradicts the actionable failure dispositions")
    return envelope(route, result["summary"], failures)


def envelope(route: str, summary: str, failures: list[dict[str, Any]]) -> dict[str, Any]:
    findings = [{"kind": "defect" if item["disposition"] == "correction" else "verification-blocked", "severity": "medium",
                 "criterion": item["criterion"], "evidence": "\n".join(item["evidence"]), "plan_basis": item.get("basis_quote", "")} for item in failures]
    return {"route": route, "summary": summary, "failures": failures, "verdict": "rejected", "findings": findings,
            "evidence": ["Failed approved verification and current phase inspected"],
            "visual_validation": {"status": "not-applicable", "evidence": ["Triage is not phase or visual approval"]}}


def legacy_triage(result: dict[str, Any]) -> dict[str, Any]:
    failures = []
    for finding in result["findings"]:
        disposition = "correction" if finding["kind"] == "defect" else "blocked"
        # Old inconclusive responses carry no stable scope/behavior identity. Preserve
        # them as blockers instead of fabricating authority or inheriting old quotas.
        failures.append({"existing_failure_id": "", "criterion": finding["criterion"], "behavior": finding["criterion"],
                         "expected": "Configured criterion satisfied: " + finding["criterion"], "observed": finding["evidence"],
                         "test_refs": [], "evidence": [finding["evidence"]], "disposition": disposition,
                         "blocker_type": "none" if disposition == "correction" else "legacy-protocol", "basis_source": "legacy", "basis_quote": finding.get("plan_basis", "")})
    return envelope(selected_route(failures), result["summary"], failures)
