"""Track observable failures and finite development work independently of gates."""
from __future__ import annotations

import copy
import json
import re
import unicodedata
import uuid
from pathlib import Path
from typing import Any

from ralph_runtime import RuntimeFailure, atomic_json


def normalized(value: str) -> str:
    return " ".join(unicodedata.normalize("NFKC", value).casefold().split())


def references(values: list[str]) -> set[str]:
    return {normalized(re.sub(r":\d+(?=::|$)", "", value.replace("\\", "/"))) for value in values}


class FailureLedger:
    def __init__(self, path: Path, phase: int, *, max_total: int = 6, max_per_failure: int = 2,
                 initial_used: int = 0, legacy_evidence: list[str] | None = None) -> None:
        self.path = path
        self.max_total = max_total
        self.max_per_failure = max_per_failure
        if path.is_symlink():
            raise RuntimeFailure("failure ledger must not be a symlink")
        if path.exists():
            self.data = json.loads(path.read_text(encoding="utf-8"))
            if not isinstance(self.data, dict) or self.data.get("version") != 2 or self.data.get("phase") != phase or not isinstance(self.data.get("global_used"), int) or self.data["global_used"] < 0 or not isinstance(self.data.get("failures"), dict) or not isinstance(self.data.get("interventions"), list):
                raise RuntimeFailure("invalid failure ledger; preserve history and inspect before resuming")
            for key, value in self.data["failures"].items():
                if not isinstance(value, dict) or value.get("id") != key or not isinstance(value.get("interventions"), int) or value["interventions"] < 0:
                    raise RuntimeFailure("invalid failure identity/counter in ledger")
            migrated = self.data.get("migrated_initial_used", self.data["global_used"] - len(self.data["interventions"]))
            if migrated not in {0, 1} or self.data["global_used"] != migrated + len(self.data["interventions"]):
                raise RuntimeFailure("inconsistent global intervention counter; do not reset history to resume")
            for job in self.data["interventions"]:
                if not isinstance(job, dict) or job.get("kind") not in {"implementation", "correction", "investigation"} or not isinstance(job.get("failure_ids"), list) or any(key not in self.data["failures"] for key in job["failure_ids"]):
                    raise RuntimeFailure("invalid recorded intervention")
            for key, group in self.data["failures"].items():
                if group["interventions"] != sum(key in job["failure_ids"] for job in self.data["interventions"]):
                    raise RuntimeFailure("inconsistent per-failure intervention counter")
        else:
            self.data = {"version": 2, "phase": phase, "global_used": initial_used, "migrated_initial_used": initial_used, "failures": {}, "interventions": [],
                         "pending": None, "revisions": [], "legacy_evidence": legacy_evidence or [], "verifications": []}
            self.save()

    def save(self) -> None:
        atomic_json(self.path, self.data)

    def note_revision(self, revision: str) -> None:
        if not self.data["revisions"] or self.data["revisions"][-1] != revision:
            self.data["revisions"].append(revision)

    def preserve_report(self, report: dict[str, Any]) -> str:
        path = self.path.parent / f"phase-{self.data['phase']}-failure-evidence-{uuid.uuid4()}.json"
        atomic_json(path, report)
        return str(path)

    def report(self, observation: dict[str, Any]) -> dict[str, Any]:
        path = Path(observation["report_path"])
        if path.is_symlink() or not path.resolve().is_relative_to(self.path.parent.resolve()) or not path.is_file():
            raise RuntimeFailure("failure report is missing or outside private task runtime")
        data = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise RuntimeFailure("invalid preserved failure report")
        return data

    @staticmethod
    def same(group: dict[str, Any], observation: dict[str, Any]) -> bool:
        if normalized(group["expected"]) != normalized(observation["expected"]):
            return False
        same_behavior = normalized(group["behavior"]) == normalized(observation["behavior"]) and normalized(group["criterion"]) == normalized(observation["criterion"])
        return same_behavior or bool(references(group["test_refs"]) & references(observation["test_refs"]))

    def observe(self, observations: list[dict[str, Any]], report: dict[str, Any], context: str, revision: str) -> list[str]:
        self.note_revision(revision)
        report_path = self.preserve_report(report)
        identities = []
        for observation in observations:
            for field in ("criterion", "behavior", "expected", "observed"):
                if not isinstance(observation.get(field), str) or not observation[field].strip():
                    raise RuntimeFailure("failure observation requires criterion, behavior, expected and observed result")
            for field in ("test_refs", "evidence"):
                if not isinstance(observation.get(field), list) or any(not isinstance(value, str) or not value.strip() for value in observation[field]):
                    raise RuntimeFailure("failure observation requires valid references/evidence")
            if not observation["evidence"]:
                raise RuntimeFailure("failure identity requires observed evidence")
            existing = observation.get("existing_failure_id", "")
            if existing:
                group = self.data["failures"].get(existing)
                if group is None or not self.same(group, observation):
                    observation = {**observation, "unverified_failure_id": existing}
                    group = next((item for item in self.data["failures"].values() if self.same(item, observation)), None)
            else:
                group = next((item for item in self.data["failures"].values() if self.same(item, observation)), None)
            if group is None:
                identity = str(uuid.uuid4())
                group = {"id": identity, "criterion": observation["criterion"], "behavior": observation["behavior"], "expected": observation["expected"],
                         "test_refs": observation["test_refs"], "interventions": 0, "contexts": [], "observations": [], "reproduction_used": False, "status": "active"}
                self.data["failures"][identity] = group
            identity = group["id"]
            group["status"] = "active"
            group["last_revision"] = revision
            if context not in group["contexts"]:
                group["contexts"].append(context)
            group["test_refs"] = list(dict.fromkeys([*group["test_refs"], *observation["test_refs"]]))
            group["observations"].append({"failure": copy.deepcopy(observation), "report_path": report_path, "context": context, "revision": revision})
            identities.append(identity)
        self.save()
        return identities

    def queue(self, kind: str, identities: list[str]) -> None:
        if kind not in {"correction", "investigation"} or not identities or any(value not in self.data["failures"] for value in identities):
            raise RuntimeFailure("invalid focused development request")
        self.data["pending"] = {"kind": kind, "failure_ids": list(dict.fromkeys(identities))}
        self.save()

    def reserve(self, kind: str, identities: list[str], revision: str) -> str:
        identities = list(dict.fromkeys(identities))
        if kind not in {"implementation", "correction", "investigation"} or (kind != "implementation" and not identities):
            raise RuntimeFailure("focused development requires an identified failure")
        if self.data["global_used"] >= self.max_total:
            raise RuntimeFailure(f"phase development limit reached ({self.max_total}); work and failure history preserved")
        for identity in identities:
            group = self.data["failures"].get(identity)
            if group is None:
                raise RuntimeFailure("unknown failure identity in intervention")
            if group["interventions"] >= self.max_per_failure:
                raise RuntimeFailure(f"failure intervention limit reached ({self.max_per_failure}): {group['behavior']}; evidence preserved")
        if any(job["status"] == "no-progress" and job["kind"] == kind and job["failure_ids"] == identities and job.get("after") == revision for job in self.data["interventions"][-1:]):
            raise RuntimeFailure("previous focused intervention produced no new evidence or source changes; supply new context before repeating it")
        self.note_revision(revision)
        identity = str(uuid.uuid4())
        self.data["global_used"] += 1
        for key in identities:
            self.data["failures"][key]["interventions"] += 1
        self.data["interventions"].append({"id": identity, "kind": kind, "failure_ids": identities, "before": revision, "status": "started"})
        self.save()  # Reserve before opening a worker; interrupted work is not free credit.
        return identity

    def finish(self, intervention: str, result: dict[str, Any], revision: str) -> None:
        job = next((item for item in self.data["interventions"] if item["id"] == intervention), None)
        if job is None or job["status"] != "started":
            raise RuntimeFailure("invalid intervention completion")
        job.update(status=result.get("status", "invalid"), after=revision, report_path=self.preserve_report(result),
                   result={key: copy.deepcopy(result[key]) for key in ("status", "summary", "investigation_outcome") if key in result})
        self.note_revision(revision)
        if job["kind"] == "correction" and result.get("status") in {"completed", "ready-for-host-checks"} and job["before"] == revision:
            job["status"] = "no-progress"
            self.save()
            raise RuntimeFailure("focused correction returned unchanged source; preserve the failure instead of repeating an empty handoff")
        if job["kind"] == "investigation" and result.get("status") in {"completed", "ready-for-host-checks"}:
            evidence = result.get("investigation_outcome")
            valid = isinstance(evidence, dict) and evidence.get("kind") in {"cause-established", "evidence-prepared"}
            valid = valid and all(isinstance(evidence.get(key), list) and evidence[key] and all(isinstance(item, str) and item.strip() for item in evidence[key]) for key in ("findings", "evidence"))
            if not valid or (job["before"] == revision and evidence["kind"] == "evidence-prepared"):
                job["status"] = "no-progress"
                self.save()
                raise RuntimeFailure("development investigation must provide verifiable new findings or actual instrumentation changes")
            repeated = any(previous is not job and previous["kind"] == "investigation" and previous["failure_ids"] == job["failure_ids"] and previous.get("after") == revision and previous.get("result", {}).get("investigation_outcome") == evidence for previous in self.data["interventions"])
            if job["before"] == revision and repeated:
                job["status"] = "no-progress"
                self.save()
                raise RuntimeFailure("development investigation repeated the same evidence without progress")
        if result.get("status") in {"completed", "ready-for-host-checks"}:
            self.data["pending"] = None
        self.save()

    def verified(self, context: str, report: dict[str, Any], revision: str) -> None:
        if report.get("status") != "completed":
            raise RuntimeFailure("failed verification cannot resolve an observed failure")
        self.note_revision(revision)
        contexts = {context}
        if context == "host" and report.get("rendered", {}).get("status") == "completed":
            contexts.add("rendered")
        for group in self.data["failures"].values():
            if contexts.intersection(group["contexts"]):
                group["status"] = "verified"
        self.data["verifications"].append({"context": context, "revision": revision, "report_path": self.preserve_report(report)})
        self.save()

    def pending_report(self) -> str:
        pending = self.data.get("pending")
        if not pending:
            return ""
        relevant = set(pending["failure_ids"])
        return json.dumps({"request": pending, "failures": [self.data["failures"][key] for key in pending["failure_ids"]],
                           "interventions": [job for job in self.data["interventions"] if relevant.intersection(job["failure_ids"])],
                           "prior_artifacts": self.data.get("prior_artifacts", [])}, ensure_ascii=False, indent=2)

    def consume_probe(self, identities: list[str]) -> bool:
        groups = [self.data["failures"][key] for key in dict.fromkeys(identities)]
        if not groups or any(group["reproduction_used"] for group in groups):
            return False
        for group in groups:
            group["reproduction_used"] = True
        self.save()
        return True

    def record_probe(self, identities: list[str], report: dict[str, Any], revision: str) -> None:
        path = self.preserve_report(report)
        for key in dict.fromkeys(identities):
            self.data["failures"][key].setdefault("probes", []).append({"revision": revision, "report_path": path})
        self.save()
