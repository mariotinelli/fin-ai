#!/usr/bin/env python3
"""Execute planning.md phases with four gates and minimal resumable state."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import queue
import re
import shutil
import signal
import subprocess
import sys
import tempfile
import threading
import time
import uuid
from pathlib import Path, PurePosixPath
from typing import Any, Callable

sys.dont_write_bytecode = True
from ralph_runtime import EventSink, ProgressBuffer, RuntimeFailure, TaskLock, atomic_json, popen_group, sanitize, sanitize_text, SECRET_KEYS, terminate_process_tree
from verification_workspace import VerificationWorkspace, declared_artifacts
from verification_investigation import read_history
from failure_ledger import FailureLedger
from failure_triage import legacy_triage, normalize_triage


class ExecutionError(RuntimeError):
    pass


EVENTS: EventSink | None = None
LEDGER: FailureLedger | None = None
ACTIVE_PROCESS: subprocess.Popen[Any] | None = None
CANCELLED = False


def fail(message: str) -> None:
    raise ExecutionError(message)


def run(command: list[str], repo: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=repo, capture_output=True, text=True, encoding="utf-8", errors="replace", check=False)


def git(repo: Path, *arguments: str) -> str:
    result = run(["git", *arguments], repo)
    if result.returncode:
        fail(sanitize(result.stderr or result.stdout or f"git {' '.join(arguments)} failed"))
    return result.stdout.strip()


def repository_for(planning: Path) -> Path:
    result = subprocess.run(["git", "-C", str(planning.parent), "rev-parse", "--show-toplevel"], capture_output=True, text=True, encoding="utf-8", errors="replace", check=False)
    if result.returncode:
        fail("planning.md must be inside a Git repository")
    return Path(result.stdout.strip()).resolve()


def baseline_command(text: str) -> tuple[str, str]:
    baseline = re.search(r"^## Baseline\s*$\n(.*?)(?=^## |\Z)", text, re.MULTILINE | re.DOTALL)
    if not baseline:
        fail("planning.md must contain a Baseline section")
    commands = re.findall(r"^```([^\r\n]*)\r?\n(.*?)^```[ \t]*$", baseline.group(1), re.MULTILINE | re.DOTALL)
    if len(commands) != 1 or not commands[0][1].strip():
        fail("Baseline must contain exactly one fenced test command")
    language, command = commands[0]
    language = language.strip().lower()
    if language not in ("", "sh", "bash", "shell", "powershell", "pwsh", "cmd", "bat"):
        fail(f"unsupported baseline shell: {language}")
    return command.strip(), language or "bash"


def rendered_command(phase: str, heading: str = "Verificação renderizada") -> tuple[str, str] | None:
    sections = list(re.finditer(r"^### " + re.escape(heading) + r"[ \t]*\r?$", phase, re.MULTILINE))
    if not sections:
        return None
    if len(sections) != 1:
        fail(f"phase requires at most one {heading} section")
    body = re.split(r"^#{1,3} ", phase[sections[0].end():], maxsplit=1, flags=re.MULTILINE)[0].strip()
    if re.fullmatch(r"Não se aplica: [^\r\n]+", body):
        return None
    return baseline_command("## Baseline\n" + body + "\n")


def parse_planning(planning: Path) -> tuple[str, list[tuple[int, str, str]]]:
    if planning.name != "planning.md" or not planning.is_file() or planning.is_symlink():
        fail("expected an existing planning.md file")
    text = planning.read_text(encoding="utf-8")
    command, _ = baseline_command(text)
    matches = list(re.finditer(r"^## Fase (\d+)\s+[—-]\s+(.+?)\s*$", text, re.MULTILINE))
    if not matches:
        fail("planning.md must contain at least one phase")
    phases: list[tuple[int, str, str]] = []
    for index, match in enumerate(matches):
        number = int(match.group(1))
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        body = text[match.start():end].strip()
        if len(body.splitlines()) < 2:
            fail(f"Fase {number} must not be empty")
        phases.append((number, match.group(2).strip(), body))
        rendered_command(body)
        rendered_command(body, "Preflight da validação")
        rendered_command(body, "Verificação no host")
        rendered_command(body, "Reprodução da verificação")
        declared_artifacts(body)
    numbers = [phase[0] for phase in phases]
    if numbers != sorted(set(numbers)):
        fail("phase numbers must be unique and increasing")
    return command, phases


def visual_sources(repo: Path, planning: Path) -> list[Path]:
    text = planning.read_text(encoding="utf-8")
    # Ignore examples inside fences; only the actual plan declares required sources.
    text = re.sub(r"^(`{3,}|~{3,})[^\n]*\n.*?^\1[ \t]*$", "", text, flags=re.MULTILINE | re.DOTALL)
    sections = list(re.finditer(r"^## Referências visuais[ \t]*\r?$", text, re.MULTILINE))
    if len(sections) != 1:
        fail("planning.md requires exactly one Referências visuais section; review the plan before execution")
    body = re.split(r"^## ", text[sections[0].end():], maxsplit=1, flags=re.MULTILINE)[0].strip()
    if re.fullmatch(r"Não se aplica: [^\r\n]+", body):
        return []
    paths = []
    for line in body.splitlines():
        if not line.strip():
            continue
        match = re.fullmatch(r"- `([^`]+)`", line.strip())
        if match is None:
            fail("Referências visuais must list repository-relative Markdown paths or explain Não se aplica")
        name = match.group(1)
        relative = PurePosixPath(name)
        if relative.is_absolute() or re.match(r"^[A-Za-z]:", name) or "\\" in name or ".." in relative.parts or relative.as_posix() != name or relative.suffix.lower() != ".md":
            fail("visual sources must be repository-relative Markdown paths without traversal")
        candidate = repo / name
        if any(path.is_symlink() for path in (candidate, *candidate.parents) if path != repo and repo in path.parents):
            fail("visual sources must not use symlinks")
        if not candidate.resolve().is_relative_to(repo.resolve()) or not candidate.is_file():
            fail("a declared visual source is missing or outside the repository")
        if candidate not in paths:
            paths.append(candidate)
    if not paths:
        fail("Referências visuais must identify sources or explain Não se aplica")
    return paths


def task_context(repo: Path, planning: Path) -> str:
    paths = [planning]
    candidates = [planning.parent / "task.md", planning.parent.parent.parent / "feature.md", planning.parent.parent.parent / "bug.md", repo / "AGENTS.md"]
    current = planning.parent
    while current != repo and repo in current.parents:
        candidates.append(current / "AGENTS.md")
        current = current.parent
    for candidate in candidates:
        if candidate.is_file() and candidate not in paths:
            paths.append(candidate)
    for source in visual_sources(repo, planning):
        if source not in paths:
            paths.append(source)
    return "\n".join(f"- `{path.relative_to(repo).as_posix()}`" for path in paths)


def state_path_for(planning: Path) -> Path:
    return planning.parent / ".flow" / "ralph-state.json"


def load_state(path: Path, planning: Path) -> dict[str, Any]:
    if not path.exists():
        return {"version": 1, "planning": str(planning), "current_phase": None, "current_gate": None, "completed_phases": [], "phase_commits": {}}
    try:
        state = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exception:
        fail(f"invalid Ralph state; delete {path} to restart: {exception}")
    if not isinstance(state, dict) or state.get("version") != 1 or Path(str(state.get("planning", ""))).resolve() != planning:
        fail(f"Ralph state belongs to another planning; delete {path} to restart")
    if not isinstance(state.get("completed_phases"), list) or not isinstance(state.get("phase_commits"), dict):
        fail(f"invalid Ralph state; delete {path} to restart")
    return state


def save_state(path: Path, state: dict[str, Any], **updates: Any) -> None:
    state.update(updates)
    atomic_json(path, state)


def worktree_changes(repo: Path) -> str:
    return git(repo, "status", "--porcelain=v1", "--untracked-files=all")


def worktree_fingerprint(repo: Path, *, output_roots: list[str] | None = None) -> str:
    """Detect content changes even when porcelain still lists the same modified files."""
    result = hashlib.sha256()
    for arguments in (("rev-parse", "--verify", "HEAD"), ("diff", "--binary"), ("diff", "--cached", "--binary")):
        value = run(["git", *arguments], repo)
        if value.returncode and arguments[0] != "rev-parse":
            fail("cannot inspect repository contents for read-only verification")
        result.update(value.stdout.encode("utf-8"))
    files = run(["git", "ls-files", "--others", "--exclude-standard", "-z"], repo)
    if files.returncode:
        fail("cannot inspect untracked verification inputs")
    for name in sorted(filter(None, files.stdout.split("\0"))):
        compare = name.casefold() if os.name == "nt" else name
        roots = [(root.casefold() if os.name == "nt" else root) + "/" for root in output_roots or []]
        if any(compare.startswith(root) for root in roots):
            continue
        path = repo / name
        result.update(name.encode("utf-8"))
        result.update(os.readlink(path).encode("utf-8") if path.is_symlink() else path.read_bytes())
    return result.hexdigest()


def development_revision(repo: Path, body: str) -> str:
    return worktree_fingerprint(repo, output_roots=declared_artifacts(body))


def development_changes(repo: Path, body: str) -> bool:
    normalize = str.casefold if os.name == "nt" else lambda value: value
    roots = [normalize(root) + "/" for root in declared_artifacts(body)]
    return bool(git(repo, "diff", "HEAD", "--name-only")) or any(
        not any(normalize(path).startswith(root) for root in roots) for path in changed_paths(repo)
    )


def render(template: Path, values: dict[str, str]) -> str:
    text = template.read_text(encoding="utf-8")
    for key, value in values.items():
        if key in {"RENDERED_VERIFICATION", "VALIDATION_PREFLIGHT", "HOST_VERIFICATION", "DEVELOPMENT_REPORT", "EVIDENCE_REQUEST", "CORRECTION_REPORT", "INVESTIGATION_REPORT"} and len(value) > 50000 and "{{" + key + "}}" in text:
            if EVENTS is None:
                fail("runtime storage is required to preserve a large agent report")
            report = EVENTS.private_file(f"context-{key.lower()}-{uuid.uuid4()}.txt")
            report.write_text(value, encoding="utf-8")
            value = (
                f"Relatório integral preservado em {report}. "
                "Leia esse arquivo em modo somente leitura, por partes quando necessário, "
                "e consulte seus logs, imagens e mapeamentos de artefatos. "
                "Esta referência substitui somente a inclusão inline; nenhum resultado, "
                "critério ou evidência foi removido ou aprovado."
            )
        text = text.replace("{{" + key + "}}", value)
    return text


def stage_phase_changes(repo: Path, body: str) -> None:
    staged = run(["git", "add", "--update", "--", "."], repo)
    if staged.returncode:
        fail(f"Gate 4 could not stage tracked changes: {sanitize(staged.stderr or staged.stdout)}")
    candidates = run(["git", "ls-files", "--others", "--exclude-standard", "-z"], repo)
    if candidates.returncode:
        fail("Gate 4 could not inspect untracked changes")
    roots = declared_artifacts(body)
    normalize = str.casefold if os.name == "nt" else lambda value: value
    roots = [normalize(root) + "/" for root in roots]
    paths = [path for path in candidates.stdout.split("\0") if path and not any(normalize(path).startswith(root) for root in roots)]
    for offset in range(0, len(paths), 64):
        staged = run(["git", "--literal-pathspecs", "add", "--", *paths[offset:offset + 64]], repo)
        if staged.returncode:
            fail(f"Gate 4 could not stage new source: {sanitize(staged.stderr or staged.stdout)}")


def runner_command(package: Path) -> list[str]:
    configured = os.environ.get("RALPH_AGENT_COMMAND_JSON")
    if configured:
        try:
            value = json.loads(configured)
        except ValueError:
            fail("RALPH_AGENT_COMMAND_JSON must be a JSON argv array")
        if not isinstance(value, list) or not value or not all(isinstance(item, str) and item for item in value):
            fail("RALPH_AGENT_COMMAND_JSON must be a non-empty JSON argv array")
        return value
    return [sys.executable, str(package / "scripts" / "run_codex.py")]


def communicate(process: subprocess.Popen[Any], timeout: float) -> tuple[str, str, int]:
    global ACTIVE_PROCESS
    ACTIVE_PROCESS = process
    try:
        try:
            stdout, stderr = process.communicate(timeout=timeout)
        except subprocess.TimeoutExpired:
            terminate_process_tree(process)
            stdout, stderr = process.communicate()
            raise ExecutionError(f"process timed out after {timeout:g} seconds")
        if CANCELLED:
            raise ExecutionError("execution cancelled")
        return stdout or "", stderr or "", process.returncode
    finally:
        ACTIVE_PROCESS = None


def agent_gate(mode: str) -> str:
    return {"develop": "development", "validate": "validation", "diagnose-host": "host-diagnosis"}[mode]


def stream_agent(process: subprocess.Popen[Any], timeout: float, stdout_path: Path, stderr_path: Path, phase: int, mode: str) -> tuple[str, str, int]:
    """Drain both pipes concurrently; keep sanitized diagnostics even on interruption."""
    global ACTIVE_PROCESS
    ACTIVE_PROCESS = process
    outputs: list[list[str]] = [[], []]
    failures: list[Exception] = []
    progress_queue: queue.Queue[str] = queue.Queue()
    progress = ProgressBuffer()

    def drain(pipe: Any, path: Path, output: list[str]) -> None:
        try:
            with path.open("w", encoding="utf-8", newline="\n") as stream:
                for line in pipe:
                    safe = sanitize_text(line)
                    output.append(safe)
                    stream.write(safe)
                    stream.flush()
                    if safe.startswith("RALPH_PROGRESS:"):
                        progress_queue.put(safe)
        except Exception as error:
            failures.append(error)

    readers = [threading.Thread(target=drain, args=(pipe, path, output), daemon=True)
               for pipe, path, output in zip((process.stdout, process.stderr), (stdout_path, stderr_path), outputs)]
    started = time.monotonic()
    next_progress = started + 30

    def flush_progress(*, force: bool = False) -> None:
        while True:
            try:
                progress.offer(progress_queue.get_nowait())
            except queue.Empty:
                break
        message = progress.take(time.monotonic(), force=force)
        if message:
            emit("agent-update", phase=phase, gate=agent_gate(mode),
                 result="reported", report_path=stderr_path, details={"message": message})

    try:
        for reader in readers:
            reader.start()
        while process.poll() is None:
            now = time.monotonic()
            flush_progress()
            if CANCELLED or now - started >= timeout:
                terminate_process_tree(process)
                fail("execution cancelled" if CANCELLED else f"process timed out after {timeout:g} seconds")
            if now >= next_progress:
                emit("agent-progress", phase=phase, gate=agent_gate(mode),
                     result="running", report_path=stderr_path, duration_ms=int((now - started) * 1000))
                next_progress = now + 30
            time.sleep(0.1)
        if CANCELLED:
            fail("execution cancelled")
    finally:
        if process.poll() is None:
            terminate_process_tree(process)
        for reader in readers:
            reader.join(timeout=5)
        ACTIVE_PROCESS = None
        flush_progress(force=True)
    if any(reader.is_alive() for reader in readers):
        fail("agent output pipes did not close; diagnostics preserved")
    if failures:
        fail(f"cannot persist agent diagnostics: {failures[0]}")
    return "".join(outputs[0]), "".join(outputs[1]), process.returncode


def extract_error(stderr: str) -> str:
    decoder = json.JSONDecoder()
    for marker in reversed(list(re.finditer(r"^\s*ERROR:\s*", stderr, re.MULTILINE))):
        try:
            value, _ = decoder.raw_decode(stderr[marker.end():].lstrip())
        except ValueError:
            continue
        error = value.get("error") if isinstance(value, dict) else None
        message = error.get("message") if isinstance(error, dict) else None
        if isinstance(message, str) and message.strip():
            return sanitize(message)
    fallback = ""
    for line in reversed(stderr.splitlines()):
        candidate = line.strip()
        if candidate.startswith("ERROR:"):
            try:
                value = json.loads(candidate.removeprefix("ERROR:").strip())
                error = value.get("error") if isinstance(value, dict) else None
                message = error.get("message") if isinstance(error, dict) else None
                if isinstance(message, str) and message.strip():
                    return sanitize(message)
            except ValueError:
                pass
        if not fallback and re.match(r"(?:ERROR\b|FATAL\b|Failed\b|Traceback\b)", candidate, re.IGNORECASE):
            fallback = sanitize(candidate)
    return fallback or "o processo do agente terminou sem informar a causa"


def redact_result(value: Any) -> Any:
    if isinstance(value, str):
        return sanitize_text(value)
    if isinstance(value, list):
        return [redact_result(item) for item in value]
    if isinstance(value, dict):
        return {key: "[REDACTED]" if SECRET_KEYS.search(str(key)) else redact_result(item) for key, item in value.items()}
    return value


def invoke_agent(package: Path, repo: Path, mode: str, prompt: str, schema: Path, phase: int, timeout: float, model: str = "gpt-6.1-sol") -> dict[str, Any]:
    if EVENTS is None:
        fail("runtime log is unavailable")
    session = str(uuid.uuid4())
    prefix = f"phase-{phase}-{mode}-{session}"
    prompt_path = EVENTS.private_file(f"{prefix}-prompt.md")
    stdout_path = EVENTS.private_file(f"{prefix}-stdout.log")
    stderr_path = EVENTS.private_file(f"{prefix}-stderr.log")
    prompt_path.write_text(sanitize_text(prompt), encoding="utf-8", newline="\n")
    with tempfile.TemporaryDirectory(prefix="ralph-result-") as directory:
        result_path = Path(directory) / "result.json"
        command = [*runner_command(package), "--mode", mode, "--prompt", str(prompt_path), "--schema", str(schema), "--result", str(result_path), "--repo", str(repo)]
        environment = os.environ.copy()
        environment["RALPH_SESSION_ID"] = session
        environment["RALPH_MODEL"] = model
        process = popen_group(command, cwd=repo, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8", errors="replace", env=environment)
        try:
            stdout, stderr, returncode = stream_agent(process, timeout, stdout_path, stderr_path, phase, mode)
        except ExecutionError as error:
            fail(f"{sanitize(str(error))}. Diagnóstico: {stderr_path}; saída: {stdout_path}")
        if returncode:
            gate = {"develop": "Gate 1", "validate": "Gate 2", "diagnose-host": "Diagnóstico no host"}[mode]
            fail(f"{gate} falhou: {extract_error(stderr)} (código de saída {returncode}). Diagnóstico: {stderr_path}")
        try:
            result = json.loads(result_path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            try:
                result = json.loads(stdout.strip())
            except ValueError:
                fail(f"agent returned no valid JSON. Diagnóstico: {stderr_path}")
        if not isinstance(result, dict):
            fail(f"agent returned no JSON object. Diagnóstico: {stderr_path}")
        return redact_result(result)


def validate_result(result: dict[str, Any], mode: str) -> None:
    if mode == "develop":
        if result.get("status") not in {"completed", "blocked", "ready-for-host-checks"}:
            fail("development agent returned an invalid status")
        if result["status"] in {"blocked", "ready-for-host-checks"}:
            if not isinstance(result.get("summary"), str) or not result["summary"].strip():
                fail("development handoff requires a concrete reason in summary")
            checks = result.get("checks")
            if not isinstance(checks, list) or not checks or any(not isinstance(item, str) or not item.strip() for item in checks):
                fail("development handoff requires diagnostic checks")
        pending = result.get("pending_checks", [])
        if not isinstance(pending, list) or any(not isinstance(item, str) or item not in {"host", "rendered"} for item in pending) or len(set(pending)) != len(pending):
            fail("pending_checks must identify unique approved host/rendered checks")
        if result["status"] == "ready-for-host-checks" and not pending:
            fail("ready-for-host-checks requires explicit pending_checks")
        if result["status"] != "ready-for-host-checks" and pending:
            fail("only ready-for-host-checks can defer checks to the host")
    elif result.get("verdict") not in {"approved", "rejected"} or not isinstance(result.get("findings"), list):
        fail("validation agent returned an invalid result")
    if mode != "develop":
        visual = result.get("visual_validation")
        if not isinstance(visual, dict) or visual.get("status") not in {"verified", "not-applicable", "blocked"}:
            fail("validation agent must report visual_validation")
        evidence = visual.get("evidence")
        if not isinstance(evidence, list) or not evidence or any(not isinstance(item, str) or not item.strip() for item in evidence):
            fail("visual validation requires comparison evidence or an explicit reason")
        if result["verdict"] == "approved" and visual["status"] == "blocked":
            fail("validation cannot approve with required visual verification blocked")
        for finding in result["findings"]:
            if not isinstance(finding, dict) or finding.get("kind", "defect") not in {"defect", "verification-blocked", "evidence-missing"}:
                fail("validation finding requires a valid kind")
            if "failure_id" in finding and not isinstance(finding["failure_id"], str):
                fail("review failure identity must be a string")
            for field in ("behavior", "expected"):
                if field in finding and (not isinstance(finding[field], str) or not finding[field].strip()):
                    fail("review failure requires an observable behavior and expectation")
            if "test_refs" in finding and (not isinstance(finding["test_refs"], list) or any(not isinstance(value, str) or not value.strip() for value in finding["test_refs"])):
                fail("review failure references must be strings")
            if "blocker_condition" in finding and finding["blocker_condition"] not in {"none", "missing-runtime", "missing-credential", "unavailable-service", "requires-global-change", "scope-decision"}:
                fail("review blocker condition is invalid")
            for field in ("severity", "criterion", "evidence"):
                if not isinstance(finding.get(field), str) or not finding[field].strip():
                    fail("validation finding requires severity criterion and evidence")
            if finding.get("kind") == "evidence-missing" and (not isinstance(finding.get("plan_basis"), str) or not finding["plan_basis"].strip()):
                fail("missing evidence requires the approved plan excerpt in plan_basis")
            if finding.get("kind") == "evidence-missing" and visual["status"] != "blocked":
                fail("missing required visual evidence must report blocked visual validation")
        if result["verdict"] == "approved" and result["findings"]:
            fail("approved validation cannot contain defects or verification blockers")


def validation_action(result: dict[str, Any]) -> str:
    validate_result(result, "validate")
    if result["verdict"] == "approved":
        return "approved"
    visual_blocked = result["visual_validation"]["status"] == "blocked"
    # Historical custom runners lacked kinds: an untyped visual blocker must not
    # be guessed to be a code defect and trigger another development loop.
    if any(f.get("kind", "verification-blocked" if visual_blocked else "defect") == "defect" for f in result["findings"]):
        return "retry"
    if visual_blocked or any(f.get("kind") == "verification-blocked" for f in result["findings"]):
        if result["findings"] and all(f.get("kind") == "evidence-missing" for f in result["findings"]):
            return "prepare-evidence"
        return "blocked"
    fail("rejected validation requires a demonstrated defect or verification blocker")


def validate_evidence_scope(result: dict[str, Any], planning: str, phase_body: str) -> None:
    """Evidence gaps must point to this phase or its shared approved plan."""
    shared = re.split(r"^## Fase \d+\s+[—-]\s+", planning, maxsplit=1, flags=re.MULTILINE)[0]
    approved = " ".join((shared + "\n" + phase_body).split())
    for finding in result.get("findings", []):
        if finding.get("kind") == "evidence-missing" or (finding.get("kind") == "verification-blocked" and finding.get("blocker_condition") == "none"):
            basis = " ".join(str(finding.get("plan_basis", "")).split())
            if not basis or basis not in approved:
                fail("evidence request exceeds the approved phase/shared plan; review plan_basis without expanding capture scope")


def validation_report(result: dict[str, Any], *, defects_only: bool = False) -> str:
    lines = []
    for finding in result.get("findings", []):
        if isinstance(finding, dict):
            if defects_only and finding.get("kind", "verification-blocked" if result.get("visual_validation", {}).get("status") == "blocked" else "defect") != "defect":
                continue
            lines.append(f"- {finding.get('severity', 'unknown')}: {finding.get('criterion', 'criterion')} — {finding.get('evidence', 'no evidence')}")
    return "\n".join(lines) or str(result.get("summary", "validation rejected without details"))


def development_report(result: dict[str, Any]) -> str:
    lines = [str(result.get("summary", "Desenvolvimento sem relatório conclusivo."))]
    checks = result.get("checks", [])
    if isinstance(checks, list):
        lines.extend(f"- {item}" for item in checks if isinstance(item, str))
    return sanitize_text("\n".join(lines))


def run_tests(repo: Path, command: str, phase: int, timeout: float, language: str = "bash", *, environment: dict[str, str] | None = None, output_path: Path | None = None, label: str = "Gate 3") -> tuple[bool, str, Path]:
    if EVENTS is None:
        fail("runtime log is unavailable")
    output_path = output_path or EVENTS.private_file(f"phase-{phase}-tests.log")
    executable = "bash" if language in ("bash", "sh", "shell", "") else ("cmd" if language == "bat" else language)
    shell = shutil.which(executable)
    if shell is None:
        fail(f"{label} requires {executable} in PATH; tests were not started")
    if executable == "bash":
        syntax = run([shell, "--noprofile", "--norc", "-n", "-c", command], repo)
        if syntax.returncode:
            output_path.write_text(sanitize_text(syntax.stderr or syntax.stdout), encoding="utf-8")
            fail(f"{label} baseline has invalid Bash syntax; tests were not started. Diagnóstico: {output_path}")
        invocation = [shell, "--noprofile", "--norc", "-c", command]
    elif executable in ("powershell", "pwsh"):
        invocation = [shell, "-NoProfile", "-NonInteractive", "-Command", command]
    else:
        invocation = [shell, "/d", "/s", "/c", command]
    with output_path.open("w+", encoding="utf-8", errors="replace", newline="\n") as output:
        try:
            process = popen_group(invocation, cwd=repo, stdout=output, stderr=subprocess.STDOUT, text=True, encoding="utf-8", errors="replace", env=environment)
            _, _, returncode = communicate(process, timeout)
        finally:
            output.seek(0)
            content = sanitize_text(output.read())
            output.seek(0)
            output.truncate()
            output.write(content)
    if (executable == "bash" and returncode in (126, 127)) or (executable == "cmd" and returncode == 9009):
        fail(f"{label} operational failure: command unavailable or not executable (exit {returncode}); changes preserved. Diagnóstico: {output_path}")
    lines = [line for line in content.splitlines() if line.strip()]
    return returncode == 0, "\n".join(lines[-80:]) or f"test command exited with code {returncode}", output_path


def changed_paths(repo: Path) -> set[str]:
    paths: set[str] = set()
    for arguments in (("diff", "--name-only", "-z"), ("diff", "--cached", "--name-only", "-z"), ("ls-files", "--others", "--exclude-standard", "-z")):
        result = run(["git", *arguments], repo)
        if result.returncode:
            fail("cannot inspect verification source paths")
        paths.update(filter(None, result.stdout.split("\0")))
    return paths


def run_verification(repo: Path, command: str, phase_body: str, phase: int, timeout: float, language: str = "bash", *, environment: dict[str, str] | None = None, output_path: Path | None = None, label: str = "Gate 3") -> dict[str, Any]:
    """Share output ownership and source protection across all parent verifiers."""
    if EVENTS is None:
        fail("runtime log is unavailable")
    directory = EVENTS.root / f"phase-{phase}-artifacts-{uuid.uuid4()}"
    directory.mkdir(mode=0o700)
    log = output_path or EVENTS.private_file(f"phase-{phase}-verification-{uuid.uuid4()}.log")
    report: dict[str, Any] = {"status": "failed", "command_status": "not-started", "command_message": "", "message": "", "diagnosable": False,
                              "source_modified": False, "source_guard": "not-started", "source_changes": [], "artifacts": [], "directory": str(directory), "log": str(log)}
    workspace = VerificationWorkspace(repo, declared_artifacts(phase_body), directory)
    before = None
    paths_before: set[str] = set()
    guard_error = ""
    attempted = False
    try:
        workspace.prepare()
        before = worktree_fingerprint(repo)
        paths_before = changed_paths(repo)
        child_environment = (os.environ if environment is None else environment).copy()
        child_environment["RALPH_ARTIFACTS_DIR"] = str(workspace.generated)
        attempted = True
        passed, message, _ = run_tests(repo, command, phase, timeout, language, environment=child_environment, output_path=log, label=label)
        report.update(status="completed" if passed else "failed", command_status="completed" if passed else "failed",
                      command_message=message, message=message, diagnosable=not passed)
    except (ExecutionError, RuntimeFailure, OSError) as error:
        if attempted:
            report["command_status"] = "unavailable"
        report["command_message"] = report["message"] = sanitize_text(str(error))
    finally:
        try:
            workspace.finish()
        except (RuntimeFailure, OSError) as error:
            guard_error = "Artifact collection failed: " + sanitize_text(str(error))
        report["artifacts"] = workspace.artifacts
        if before is not None:
            try:
                report["source_guard"] = "preserved"
                if worktree_fingerprint(repo) != before:
                    paths_after = changed_paths(repo)
                    report["source_modified"] = True
                    report["source_guard"] = "modified"
                    report["source_changes"] = sorted(paths_before.symmetric_difference(paths_after) or paths_after)
                    guard_error = "verification modified repository source outside declared artifact directories; changes preserved. Paths: " + ", ".join(report["source_changes"]) + ("\n" + guard_error if guard_error else "")
            except (ExecutionError, OSError) as error:
                report["source_guard"] = "unavailable"
                guard_error += "\nSource inspection failed: " + sanitize_text(str(error))
        if guard_error:
            report.update(status="failed", diagnosable=False, message=guard_error + "\nOriginal command result: " + report["command_status"] + "\n" + report["command_message"])
        atomic_json(directory / "report.json", redact_result(report))
    if CANCELLED:
        fail(f"execution cancelled; verification outputs preserved: {directory / 'report.json'}")
    return report


def preserve_prior_artifacts(repo: Path, phase_body: str, phase: int) -> list[dict[str, str]]:
    roots = declared_artifacts(phase_body)
    if not roots:
        return []
    if EVENTS is None:
        fail("runtime log is unavailable")
    directory = EVENTS.root / f"phase-{phase}-prior-artifacts-{uuid.uuid4()}"
    directory.mkdir(mode=0o700)
    workspace = VerificationWorkspace(repo, roots, directory)
    try:
        workspace.prepare()
        return workspace.finish()
    finally:
        atomic_json(directory / "report.json", {"artifacts": workspace.artifacts})


def run_rendered_verification(repo: Path, phase_body: str, phase: int, timeout: float, *, heading: str = "Verificação renderizada", evidence_request: Path | None = None) -> dict[str, Any]:
    capture = rendered_command(phase_body, heading)
    if capture is None:
        return {"status": "not-configured", "images": [], "message": "Sem comando de captura no plano; usar evidências acessíveis existentes ou registrar bloqueio."}
    if EVENTS is None:
        fail("runtime evidence directory is unavailable")
    directory = EVENTS.root / f"phase-{phase}-rendered-{uuid.uuid4()}"
    directory.mkdir(mode=0o700)
    canonical = directory.resolve()
    log = directory / "capture.log"
    environment = os.environ.copy()
    environment["RALPH_EVIDENCE_DIR"] = str(directory.resolve())
    environment["RALPH_PHASE_NUMBER"] = str(phase)
    environment["RALPH_CAPTURE_MODE"] = "preflight" if heading == "Preflight da validação" else "validation"
    # Never inherit a request from a previous task or from the caller's shell.
    environment.pop("RALPH_EVIDENCE_REQUEST", None)
    if evidence_request is not None:
        environment["RALPH_EVIDENCE_REQUEST"] = str(evidence_request.resolve())
    report: dict[str, Any] = {"status": "failed", "directory": str(directory), "log": str(log), "images": []}
    try:
        with tempfile.TemporaryDirectory(prefix="ralph-capture-") as temporary:
            environment.update(TEMP=temporary, TMP=temporary, TMPDIR=temporary)
            outcome = run_verification(repo, capture[0], phase_body, phase, timeout, capture[1], environment=environment, output_path=log, label=heading)
        report["verification"] = outcome
        report["artifacts"] = outcome["artifacts"]
        report["message"] = outcome["message"]
        report["diagnosable"] = outcome["diagnosable"]
        if directory.is_symlink() or directory.resolve() != canonical:
            fail("capture directory was redirected")
        for path in directory.rglob("*"):
            if path.is_symlink() or not path.resolve().is_relative_to(canonical):
                fail("rendered evidence contains an unsafe path")
            if path.is_file() and path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}:
                report["images"].append(str(path.resolve()))
        if outcome["status"] == "completed" and report["images"]:
            report["status"] = "completed"
        elif outcome["status"] == "completed":
            report["message"] = "O comando terminou sem capturas renderizadas no RALPH_EVIDENCE_DIR."
    except (ExecutionError, OSError) as error:
        if CANCELLED:
            raise
        report["diagnosable"] = False
        report["message"] = sanitize_text(str(error))
    atomic_json(directory / "report.json", report)
    if report.get("verification", {}).get("source_modified"):
        fail(f"rendered verification modified repository source; changes preserved. Diagnóstico: {directory / 'report.json'}")
    return report


def run_host_checks(repo: Path, phase_body: str, phase: int, timeout: float, pending: list[str]) -> dict[str, Any]:
    """Complete only plan-declared checks, without allowing them to edit source."""
    if EVENTS is None:
        fail("runtime log is unavailable")
    report: dict[str, Any] = {"status": "failed", "checks": [], "message": "", "diagnosable": False}
    report_path = EVENTS.root.parent / f"phase-{phase}-host-checks.json"
    try:
        host = rendered_command(phase_body, "Verificação no host")
        if "host" in pending and host is None:
            fail("pending host check requires an approved Verificação no host command in planning.md")
        if "rendered" in pending and rendered_command(phase_body) is None:
            fail("pending rendered check requires an approved Verificação renderizada command in planning.md")
        if host is not None:
            log = EVENTS.private_file(f"phase-{phase}-host-checks-{uuid.uuid4()}.log")
            environment = os.environ.copy()
            for name in ("RALPH_CAPTURE_MODE", "RALPH_EVIDENCE_DIR", "RALPH_EVIDENCE_REQUEST"):
                environment.pop(name, None)
            with tempfile.TemporaryDirectory(prefix="ralph-host-check-") as temporary:
                environment.update(TEMP=temporary, TMP=temporary, TMPDIR=temporary)
                outcome = run_verification(repo, host[0], phase_body, phase, timeout, host[1], environment=environment, output_path=log, label="Verificação no host")
            report["checks"].append({"check": "host", **outcome})
            if outcome["status"] != "completed":
                report["diagnosable"] = outcome["diagnosable"]
                fail(f"Verificação no host falhou. Diagnóstico: {outcome['directory']}/report.json. {outcome['message']}")
        if "rendered" in pending:
            rendered = run_rendered_verification(repo, phase_body, phase, timeout)
            report["rendered"] = rendered
            report["checks"].append({"check": "rendered", "status": rendered["status"], "log": rendered.get("log")})
            if rendered["status"] != "completed":
                report["diagnosable"] = rendered.get("diagnosable", False)
                fail(f"Verificação renderizada no host incompleta. Diagnóstico: {rendered.get('log')}. {rendered.get('message', '')}")
        report["status"] = "completed"
        report["message"] = "Verificações declaradas no host concluídas; revisão independente pendente."
    except (ExecutionError, RuntimeFailure, OSError) as error:
        report["message"] = sanitize_text(str(error))
    atomic_json(report_path, redact_result(report))
    if CANCELLED:
        fail(f"execution cancelled; host diagnostics preserved: {report_path}")
    return report


def diagnose_host_failure(package: Path, repo: Path, values: dict[str, str], phase: int, timeout: float, model: str) -> dict[str, Any]:
    """Classify a failed executed check without granting write access or approval."""
    if EVENTS is None:
        fail("runtime log is unavailable")
    before = worktree_fingerprint(repo)
    try:
        result = invoke_agent(package, repo, "diagnose-host", render(package / "prompts" / "diagnose-host.md", values), package / "schemas" / "host-diagnosis.schema.json", phase, timeout, model)
        result = redact_result(result)
        atomic_json(EVENTS.root.parent / f"phase-{phase}-host-diagnosis.json", result)
        if "route" in result:
            triage = normalize_triage(result, repo, values.get("PLANNING_TEXT", ""), values.get("PHASE", ""))
            atomic_json(EVENTS.root.parent / f"phase-{phase}-host-triage.json", triage)
            return triage
        validate_result(result, "validate")
        if result["verdict"] != "rejected" or not result["findings"] or result["visual_validation"]["status"] != "not-applicable":
            fail("host diagnosis must report concrete defects/blockers without approving the phase or visual acceptance")
        if any(finding.get("kind") not in {"defect", "verification-blocked"} for finding in result["findings"]):
            fail("host diagnosis requires explicit defect or verification-blocked findings")
        investigation = result.get("investigation")
        if "investigation" in result:
            if not isinstance(investigation, dict) or not isinstance(investigation.get("requested"), bool) or investigation.get("cause") not in {"not-needed", "inconclusive-test", "environment", "scope"} or not isinstance(investigation.get("reason"), str):
                fail("diagnosis returned an invalid investigation request")
            if investigation["requested"] and (investigation["cause"] != "inconclusive-test" or not investigation["reason"].strip() or any(f["kind"] == "defect" for f in result["findings"])):
                fail("only inconclusive test failures without demonstrated defects can request reproduction")
        return legacy_triage(result)
    finally:
        if worktree_fingerprint(repo) != before:
            fail("read-only host diagnosis modified repository source; changes preserved")


def investigation_path(phase: int, context: str) -> Path:
    if EVENTS is None:
        fail("runtime log is unavailable")
    return EVENTS.root.parent / f"phase-{phase}-{context}-investigation.json"


def investigation_context(phase: int) -> str:
    if LEDGER is not None and LEDGER.data["phase"] == phase:
        return json.dumps(LEDGER.data, ensure_ascii=False, indent=2)
    return json.dumps({context: history for context in ("host", "tests") if (history := read_history(investigation_path(phase, context))) is not None}, ensure_ascii=False, indent=2)


def resolve_check_failure(package: Path, repo: Path, values: dict[str, str], phase_body: str, phase: int, attempt: int, context: str,
                          report: dict[str, Any], timeout: float, diagnosis_timeout: float, model: str,
                          confirm: Callable[[], dict[str, Any]]) -> dict[str, Any]:
    if EVENTS is None:
        fail("runtime log is unavailable")
    if LEDGER is None:
        fail("failure registry is unavailable")
    started = gate_started(phase, "host-diagnosis", attempt)
    diagnostic_values = {**values, "HOST_VERIFICATION": json.dumps(report, ensure_ascii=False, indent=2),
                         "INVESTIGATION_REPORT": investigation_context(phase)}
    diagnosis = diagnose_host_failure(package, repo, diagnostic_values, phase, diagnosis_timeout, model)
    failure_context = "rendered" if context == "host" and report.get("checks") and report["checks"][-1].get("check") == "rendered" else context
    identities = LEDGER.observe(diagnosis["failures"], redact_result(report), failure_context, worktree_fingerprint(repo))
    route = diagnosis["route"]
    action = {"correction": "correct", "development-investigation": "investigate", "blocked": "blocked"}[route]
    selected = [identity for identity, observation in zip(identities, diagnosis["failures"]) if observation["disposition"] == route]
    if action in {"correct", "investigate"}:
        LEDGER.queue("correction" if action == "correct" else "investigation", selected)
    gate_finished(phase, "host-diagnosis", attempt, "rejected" if action == "correct" else "pending" if action == "investigate" else "blocked", started, findings=diagnosis["findings"])
    return {"action": action, "report": report, "diagnosis": diagnosis, "history": None, "reason": "", "failure_ids": identities}


def queue_review_correction(review: dict[str, Any], report: dict[str, Any], context: str, repo: Path, *, kind: str = "correction") -> None:
    if LEDGER is None:
        fail("failure registry is unavailable")
    triage = legacy_triage(review)
    for item, finding in zip(triage["failures"], review["findings"]):
        for field in ("behavior", "expected", "test_refs"):
            if field in finding:
                item[field] = finding[field]
        if kind == "investigation" and finding.get("kind") in {"verification-blocked", "evidence-missing"} and finding.get("blocker_condition") == "none":
            item.update(disposition="development-investigation", blocker_type="none")
        claimed = finding.get("failure_id", "")
        if claimed:
            # The ledger verifies association. A guessed ID must never inherit an
            # unrelated quota or turn a valid new failure into a protocol blocker.
            item["existing_failure_id"] = claimed
    identities = LEDGER.observe(triage["failures"], redact_result(report), context, worktree_fingerprint(repo))
    disposition = "correction" if kind == "correction" else "development-investigation"
    selected = [identity for identity, item in zip(identities, triage["failures"]) if item["disposition"] == disposition]
    LEDGER.queue(kind, selected)


def run_investigation_probe(repo: Path, body: str, phase: int, timeout: float, suite: str, suite_shell: str, identities: list[str]) -> tuple[str, dict[str, Any]]:
    if LEDGER is None:
        fail("failure registry is unavailable")
    groups = [LEDGER.data["failures"][key] for key in identities]
    last = groups[0]["observations"][-1]
    context, original = last["context"], LEDGER.report(last)
    declared = rendered_command(body, "Reprodução da verificação")
    section = re.search(r"^### Reprodução da verificação[ \t]*$", body, re.MULTILINE)
    coverage = re.split(r"^#{1,3} ", body[section.end():], maxsplit=1, flags=re.MULTILINE)[0] if section else ""
    cases = set(re.findall(r"^- Caso: `([^`]+)`[ \t]*$", coverage, re.MULTILINE))
    expectations = set(re.findall(r"^- Esperado: `([^`]+)`[ \t]*$", coverage, re.MULTILINE))
    required = {reference for group in groups for reference in group["test_refs"]}
    emit("investigation-progress", phase=phase, gate="investigation", result="running", details={"step": "reproducing"})
    if declared is not None and required and required.issubset(cases) and {group["expected"] for group in groups}.issubset(expectations):
        result = run_verification(repo, declared[0], body, phase, timeout, declared[1], label="Reprodução da verificação")
    elif context == "tests" or (context == "validation" and rendered_command(body) is None):
        result = run_verification(repo, suite, body, phase, timeout, suite_shell)
    elif context == "rendered" or (context == "validation" and rendered_command(body) is not None) or original.get("checks", [{}])[-1].get("check") == "rendered":
        result = run_rendered_verification(repo, body, phase, timeout)
    else:
        result = run_host_checks(repo, body, phase, timeout, [])
    LEDGER.record_probe(identities, redact_result(result), worktree_fingerprint(repo))
    return context, result


def emit(event: str, **values: Any) -> None:
    if EVENTS is not None:
        EVENTS.emit(event, **values)


def gate_started(phase: int, gate: str, attempt: int) -> float:
    emit("gate-started", phase=phase, gate=gate, attempt=attempt, result="started")
    return time.monotonic()


def gate_finished(phase: int, gate: str, attempt: int, result: str, started: float, **details: Any) -> None:
    emit("gate-finished", phase=phase, gate=gate, attempt=attempt, duration_ms=int((time.monotonic() - started) * 1000), result=result, details=details or None)


def positive(value: str) -> float:
    try:
        parsed = float(value)
    except ValueError:
        raise argparse.ArgumentTypeError("must be a number")
    if not math.isfinite(parsed) or parsed <= 0:
        raise argparse.ArgumentTypeError("must be a positive finite number")
    return parsed


def signal_handler(_signum: int, _frame: Any) -> None:
    global CANCELLED
    CANCELLED = True
    if ACTIVE_PROCESS is not None:
        terminate_process_tree(ACTIVE_PROCESS)


def execute(arguments: argparse.Namespace) -> int:
    global EVENTS, LEDGER
    planning = Path(arguments.planning).resolve()
    suite, phases = parse_planning(planning)
    _, suite_shell = baseline_command(planning.read_text(encoding="utf-8"))
    repo = repository_for(planning)
    context = task_context(repo, planning)
    package = Path(__file__).resolve().parent.parent
    state_path = state_path_for(planning)
    state_relative = state_path.relative_to(repo).as_posix()
    if run(["git", "check-ignore", "--quiet", "--", state_relative], repo).returncode:
        fail(f"add /.flow/ to {planning.parent / '.gitignore'} before running Ralph")
    state = load_state(state_path, planning)
    git_dir = Path(git(repo, "rev-parse", "--git-dir"))
    git_dir = git_dir if git_dir.is_absolute() else (repo / git_dir).resolve()
    EVENTS = EventSink(git_dir, state_path, verbose=arguments.verbose)
    lock = TaskLock(state_path, git_dir / "ralph-locks")
    lock.acquire()
    try:
        for signum in (signal.SIGINT, signal.SIGTERM):
            signal.signal(signum, signal_handler)
        known = {number for number, _, _ in phases}
        state["completed_phases"] = [number for number in state["completed_phases"] if number in known]
        for number, title, body in phases:
            if number in state["completed_phases"]:
                continue
            prior_artifacts = preserve_prior_artifacts(repo, body, number)
            if state.get("current_phase") == number and state.get("current_gate") == "commit" and not worktree_changes(repo):
                state["completed_phases"].append(number)
                state["phase_commits"][str(number)] = git(repo, "rev-parse", "HEAD")
                save_state(state_path, state, current_phase=None, current_gate=None)
                emit("phase-resumed", phase=number, gate="commit", result="resumed")
                continue
            if worktree_changes(repo) and state.get("current_phase") != number:
                fail("worktree has changes unrelated to the resumable phase; commit or discard them before Ralph")
            previous_gate = state.get("current_gate") if state.get("current_phase") == number else None
            execution_id = state.get("current_execution_id") if previous_gate else None
            if execution_id is None:
                execution_id = str(uuid.uuid4())
            try:
                if str(uuid.UUID(str(execution_id))) != execution_id:
                    fail("invalid phase execution identity; preserve state before resuming")
            except ValueError:
                fail("invalid phase execution identity; preserve state before resuming")
            saved_development = EVENTS.root.parent / f"phase-{number}-development.json"
            initial_used = 0
            if previous_gate and saved_development.is_file():
                saved = json.loads(saved_development.read_text(encoding="utf-8"))
                validate_result(saved, "develop")
                initial_used = 1
            legacy_evidence = [str(investigation_path(number, context_name)) for context_name in ("host", "tests") if investigation_path(number, context_name).is_file()]
            LEDGER = FailureLedger(EVENTS.root.parent / f"phase-{number}-failures-{execution_id}.json", number,
                                   max_total=arguments.max_attempts, max_per_failure=arguments.max_failure_attempts,
                                   initial_used=initial_used, legacy_evidence=legacy_evidence)
            if prior_artifacts:
                LEDGER.data.setdefault("prior_artifacts", []).extend(redact_result(prior_artifacts))
                LEDGER.save()
            resume_validation = previous_gate in {"validation", "validation-blocked", "evidence-preparation", "evidence-blocked", "commit", "tests-blocked", "tests-diagnosis"}
            resume_host = previous_gate in {"host-checks", "host-checks-blocked", "host-diagnosis"}
            save_state(state_path, state, current_phase=number, current_execution_id=execution_id, current_gate="host-checks" if resume_host else "validation" if resume_validation else "development")
            emit("phase-started", phase=number, result="started")
            correction = str(state.get("last_failure", "")).strip() if previous_gate == "development" else ""
            if correction and not LEDGER.data.get("pending"):
                legacy = {"existing_failure_id": "", "criterion": "Pending phase correction", "behavior": "Legacy pending correction",
                          "expected": "Approved phase checks satisfied", "observed": correction, "test_refs": [], "evidence": [correction], "disposition": "correction"}
                identities = LEDGER.observe([legacy], {"status": "failed", "message": correction}, "validation", worktree_fingerprint(repo))
                LEDGER.queue("correction", identities)
            rendered: dict[str, Any] = {"status": "not-configured", "images": []}
            development_path = EVENTS.root.parent / f"phase-{number}-development.json"
            evidence_request_path = EVENTS.root.parent / f"phase-{number}-evidence-request.json"
            evidence_request = evidence_request_path if resume_validation and evidence_request_path.is_file() else None
            previous_rendered: dict[str, Any] = {}
            if evidence_request:
                saved_request = redact_result(json.loads(evidence_request.read_text(encoding="utf-8")))
                if not isinstance(saved_request, dict):
                    fail("saved evidence request must be a JSON object; changes preserved")
                validate_result(saved_request, "validate")
                validate_evidence_scope(saved_request, planning.read_text(encoding="utf-8"), body)
                previous_rendered = saved_request.get("rendered_verification", {})
                if not isinstance(previous_rendered, dict) or not isinstance(previous_rendered.get("images", []), list):
                    fail("saved rendered evidence report is invalid; changes preserved")
            development: dict[str, Any] = {"status": "unavailable", "message": "Relatório anterior indisponível; verificar evidências existentes e registrar lacunas."}
            if (resume_validation or resume_host) and development_path.is_file():
                try:
                    development = redact_result(json.loads(development_path.read_text(encoding="utf-8")))
                    if not isinstance(development, dict):
                        fail("saved development report must be a JSON object")
                except (OSError, ValueError) as error:
                    fail(f"cannot read saved development report; changes preserved: {sanitize(str(error))}")
            if resume_host:
                validate_result(development, "develop")
                if development.get("status") not in {"completed", "ready-for-host-checks"}:
                    fail("host resume requires an explicit ready or completed development report; changes preserved")
            preflight = run_rendered_verification(repo, body, number, arguments.render_timeout_minutes * 60, heading="Preflight da validação")
            if preflight["status"] == "failed":
                save_state(state_path, state, current_gate="host-checks-blocked" if resume_host else "validation-blocked" if resume_validation else "preflight-blocked")
                fail(f"Preflight da validação bloqueado; corrija o ambiente e retome. Diagnóstico: {preflight.get('log')}. {sanitize(str(preflight.get('message', '')))}")
            attempt = LEDGER.data["global_used"]
            while True:
                values = {"REPOSITORY": str(repo), "CONTEXT_PATHS": context, "PHASE": body, "PHASE_NUMBER": str(number), "CORRECTION_REPORT": correction,
                          "RENDERED_VERIFICATION": json.dumps(rendered, ensure_ascii=False, indent=2),
                          "VALIDATION_PREFLIGHT": json.dumps(preflight, ensure_ascii=False, indent=2), "PLANNING_TEXT": planning.read_text(encoding="utf-8")}
                prepared_rendered = None
                host_report: dict[str, Any] = {"status": "not-configured", "checks": []}
                if not resume_validation and not resume_host:
                    previous_rendered = {}
                    pending = LEDGER.data.get("pending")
                    work_kind = pending["kind"] if pending else "implementation"
                    work_ids = pending["failure_ids"] if pending else []
                    if pending:
                        values["CORRECTION_REPORT"] = LEDGER.pending_report()
                    work_gate = "development-investigation" if work_kind == "investigation" else "development"
                    started = time.monotonic()
                    template = package / "prompts" / {"implementation": "develop.md", "correction": "correct.md", "investigation": "investigate-development.md"}[work_kind]
                    report_available = False
                    handoff_accepted = False
                    intervention = None
                    revision_before = development_revision(repo, body)
                    try:
                        intervention = LEDGER.reserve(work_kind, work_ids, revision_before)
                        attempt = LEDGER.data["global_used"]
                        started = gate_started(number, work_gate, attempt)
                        save_state(state_path, state, current_gate=work_gate)
                        schema = "development-investigation.schema.json" if work_kind == "investigation" else "development-result.schema.json"
                        result = invoke_agent(package, repo, "develop", render(template, values), package / "schemas" / schema, number, arguments.dev_timeout_minutes * 60, arguments.model)
                        development = redact_result(result)
                        atomic_json(development_path, development)
                        report_available = True
                        validate_result(development, "develop")
                        LEDGER.finish(intervention, development, development_revision(repo, body))
                        if development["status"] == "blocked":
                            fail(f"Desenvolvimento bloqueado: {development_report(development)}")
                        if work_kind != "investigation" and not development_changes(repo, body):
                            fail(f"Gate 1 finished without repository changes. {development_report(development)}")
                        handoff_accepted = True
                        save_state(state_path, state, current_gate="host-checks")
                        gate_finished(number, work_gate, attempt, "pending" if development["status"] == "ready-for-host-checks" else "completed", started)
                        worker_artifacts = preserve_prior_artifacts(repo, body, number)
                        if worker_artifacts:
                            development["artifacts"] = redact_result(worker_artifacts)
                            atomic_json(development_path, development)
                            LEDGER.data.setdefault("prior_artifacts", []).extend(redact_result(worker_artifacts))
                            LEDGER.save()
                    except (ExecutionError, RuntimeFailure, OSError) as error:
                        reason = sanitize_text(str(error))
                        diagnostic = development_path if report_available else EVENTS.events_path
                        if intervention and LEDGER.data["interventions"][-1]["status"] == "started":
                            LEDGER.finish(intervention, {"status": "blocked", "summary": reason}, development_revision(repo, body))
                        save_state(state_path, state, current_gate="host-checks-blocked" if handoff_accepted else "development-investigation-blocked" if work_kind == "investigation" else "development-blocked", last_failure=reason)
                        gate_finished(number, "host-checks" if handoff_accepted else work_gate, attempt, "blocked", started, reason=reason, report_path=str(diagnostic))
                        fail(f"{sanitize(reason)} Diagnóstico: {diagnostic}. Corrija o impedimento e retome o mesmo comando; trabalho preservado.")
                    if work_kind == "investigation" and development_revision(repo, body) == revision_before:
                        observation = LEDGER.data["failures"][work_ids[0]]["observations"][-1]
                        original = LEDGER.report(observation)
                        resolution = resolve_check_failure(package, repo, values, body, number, attempt, observation["context"], original,
                                                           arguments.host_timeout_minutes * 60, arguments.validation_timeout_minutes * 60, arguments.model,
                                                           confirm=lambda: original)
                        if resolution["action"] in {"correct", "investigate"}:
                            save_state(state_path, state, current_gate="development", last_failure=LEDGER.pending_report())
                            continue
                        save_state(state_path, state, current_gate="development-investigation-blocked", last_failure=validation_report(resolution["diagnosis"]))
                        fail("development investigation established a blocker; evidence preserved")
                    if work_kind == "investigation" and development["investigation_outcome"]["kind"] == "evidence-prepared" and LEDGER.consume_probe(work_ids):
                        origin = LEDGER.data["failures"][work_ids[0]]["observations"][-1]["context"]
                        probe_timeout = {"host": arguments.host_timeout_minutes, "rendered": arguments.render_timeout_minutes, "tests": arguments.tests_timeout_minutes}.get(origin, arguments.host_timeout_minutes)
                        probe_context, probe = run_investigation_probe(repo, body, number, probe_timeout * 60, suite, suite_shell, work_ids)
                        if probe["status"] != "completed":
                            if not probe.get("diagnosable"):
                                save_state(state_path, state, current_gate="host-checks-blocked", last_failure=str(probe.get("message", "Probe unavailable")))
                                fail("investigation probe unavailable or unsafe; work and evidence preserved")
                            probe_values = {**values, "DEVELOPMENT_REPORT": json.dumps(development, ensure_ascii=False)}
                            resolution = resolve_check_failure(package, repo, probe_values, body, number, attempt, probe_context, probe,
                                                               arguments.host_timeout_minutes * 60, arguments.validation_timeout_minutes * 60, arguments.model,
                                                               confirm=lambda: probe)
                            if resolution["action"] in {"correct", "investigate"}:
                                save_state(state_path, state, current_gate="development", last_failure=LEDGER.pending_report())
                                continue
                            save_state(state_path, state, current_gate="host-checks-blocked", last_failure=validation_report(resolution["diagnosis"]))
                            fail("investigation established an external/scope blocker; evidence preserved")
                if not resume_validation and (resume_host or development.get("status") == "ready-for-host-checks" or rendered_command(body, "Verificação no host") is not None):
                    save_state(state_path, state, current_gate="host-checks")
                    started = gate_started(number, "host-checks", attempt)
                    host_report = run_host_checks(repo, body, number, arguments.host_timeout_minutes * 60, development.get("pending_checks", []))
                    diagnostic = EVENTS.root.parent / f"phase-{number}-host-checks.json"
                    if prior_artifacts:
                        host_report["prior_artifacts"] = prior_artifacts
                        atomic_json(diagnostic, host_report)
                    if host_report["status"] != "completed":
                        reason = str(host_report.get("message", "Verificações no host incompletas"))
                        if host_report.get("diagnosable"):
                            save_state(state_path, state, current_gate="host-diagnosis", last_failure=reason)
                            try:
                                resolution = resolve_check_failure(package, repo, values, body, number, attempt, "host", host_report,
                                                                   arguments.host_timeout_minutes * 60, arguments.validation_timeout_minutes * 60, arguments.model,
                                                                   confirm=lambda: run_host_checks(repo, body, number, arguments.host_timeout_minutes * 60, development.get("pending_checks", [])))
                            except (ExecutionError, RuntimeFailure, OSError, ValueError) as error:
                                reason = "Diagnóstico da falha no host indisponível: " + sanitize_text(str(error)) + "\nFalha original: " + reason
                            else:
                                diagnosis = resolution["diagnosis"]
                                if resolution["action"] in {"correct", "investigate"}:
                                    correction = "Corrija somente os defeitos demonstrados pela verificação no host, preservando o restante da fase:\n" + validation_report(diagnosis, defects_only=True) + f"\nRelatório da verificação: {diagnostic}"
                                    if resolution["history"]:
                                        correction += "\nInvestigação preservada: " + str(resolution["history"]["archive_path"])
                                    save_state(state_path, state, current_gate="development", last_failure=correction)
                                    gate_finished(number, "host-checks", attempt, "rejected", started, findings=diagnosis["findings"], report_path=str(diagnostic))
                                    if attempt == arguments.max_attempts:
                                        fail(f"Limite de {attempt} intervenções no Desenvolvimento da fase {number} atingido; encaminhamento e trabalho preservados. Diagnóstico: {diagnostic}")
                                    resume_host = False
                                    resume_validation = False
                                    previous_rendered = {}
                                    evidence_request = None
                                    if evidence_request_path.exists():
                                        evidence_request_path.unlink()
                                    continue
                                reason += "\n" + validation_report(diagnosis) + "\n" + resolution["reason"]
                        if host_report["status"] != "completed":
                            save_state(state_path, state, current_gate="host-checks-blocked", last_failure=reason)
                            gate_finished(number, "host-checks", attempt, "blocked", started, reason=reason, report_path=str(diagnostic))
                            fail(f"{sanitize(reason)} Relatório: {diagnostic}. Retome o mesmo comando após diagnosticar/corrigir o impedimento; Desenvolvimento preservado.")
                    prepared_rendered = host_report.get("rendered")
                    LEDGER.verified("host", redact_result(host_report), worktree_fingerprint(repo))
                    gate_finished(number, "host-checks", attempt, "completed", started, report_path=str(diagnostic))
                elif resume_validation and (development.get("status") == "ready-for-host-checks" or rendered_command(body, "Verificação no host") is not None):
                    saved_host = EVENTS.root.parent / f"phase-{number}-host-checks.json"
                    if saved_host.is_file():
                        host_report = redact_result(json.loads(saved_host.read_text(encoding="utf-8")))
                    if not isinstance(host_report, dict) or host_report.get("status") != "completed":
                        save_state(state_path, state, current_gate="host-checks-blocked")
                        fail("host verification report is missing or incomplete; resume the same command to rerun approved checks without development")
                resume_host = False
                resume_validation = False

                save_state(state_path, state, current_gate="validation")
                started = gate_started(number, "validation", attempt)
                restart_development = False
                for evidence_attempt in range(2):
                    rendered = prepared_rendered if evidence_attempt == 0 and prepared_rendered is not None else run_rendered_verification(repo, body, number, arguments.render_timeout_minutes * 60, evidence_request=evidence_request)
                    if rendered["status"] == "failed" and rendered.get("diagnosable"):
                        failed_render = {**rendered, "checks": [{"check": "rendered", "status": "failed", "log": rendered.get("log")}], "rendered": rendered}
                        resolution = resolve_check_failure(package, repo, values, body, number, attempt, "rendered", failed_render,
                                                           arguments.render_timeout_minutes * 60, arguments.validation_timeout_minutes * 60, arguments.model,
                                                           confirm=lambda: rendered)
                        if resolution["action"] in {"correct", "investigate"}:
                            save_state(state_path, state, current_gate="development", last_failure=LEDGER.pending_report())
                            restart_development = True
                            break
                        save_state(state_path, state, current_gate="validation-blocked", last_failure=validation_report(resolution["diagnosis"]))
                        fail("rendered verification established an external/scope blocker; evidence preserved")
                    if rendered["status"] == "completed":
                        LEDGER.verified("rendered", redact_result(rendered), worktree_fingerprint(repo))
                    if previous_rendered:
                        rendered["previous_reports"] = [previous_rendered]
                        rendered["images"] = list(dict.fromkeys([*previous_rendered.get("images", []), *rendered.get("images", [])]))
                    values["RENDERED_VERIFICATION"] = json.dumps(rendered, ensure_ascii=False, indent=2)
                    values["DEVELOPMENT_REPORT"] = json.dumps(development, ensure_ascii=False, indent=2)
                    values["HOST_VERIFICATION"] = json.dumps(host_report, ensure_ascii=False, indent=2)
                    values["INVESTIGATION_REPORT"] = investigation_context(number)
                    values["VALIDATION_PREFLIGHT"] = json.dumps(preflight, ensure_ascii=False, indent=2)
                    values["EVIDENCE_REQUEST"] = evidence_request.read_text(encoding="utf-8") if evidence_request else "Sem pedido anterior de capturas adicionais."
                    before = worktree_fingerprint(repo)
                    try:
                        validation = invoke_agent(package, repo, "validate", render(package / "prompts" / "validate.md", values), package / "schemas" / "validation-result.schema.json", number, arguments.validation_timeout_minutes * 60, arguments.model)
                        validate_result(validation, "validate")
                        validate_evidence_scope(validation, planning.read_text(encoding="utf-8"), body)
                    except (ExecutionError, RuntimeFailure, OSError) as error:
                        if worktree_fingerprint(repo) != before:
                            fail("Gate 2 modified the repository before failing; changes were preserved")
                        reason = sanitize_text(str(error))
                        save_state(state_path, state, current_gate="validation-blocked", last_failure=reason)
                        gate_finished(number, "validation", attempt, "blocked", started, reason=reason, rendered=rendered)
                        fail(f"Gate 2 indisponível por falha de configuração/runtime ou resultado inválido; retome após resolver o impedimento. {reason}")
                    if worktree_fingerprint(repo) != before:
                        fail("Gate 2 modified the repository")
                    action = validation_action(validation)
                    scoped_unknown = any(item.get("kind") in {"verification-blocked", "evidence-missing"} and item.get("blocker_condition") == "none" for item in validation["findings"])
                    if action != "retry" and scoped_unknown and (action != "prepare-evidence" or evidence_attempt or rendered_command(body) is None or rendered["status"] == "failed"):
                        queue_review_correction(validation, rendered, "validation", repo, kind="investigation")
                        save_state(state_path, state, current_gate="development", last_failure=LEDGER.pending_report())
                        restart_development = True
                        break
                    if action != "prepare-evidence":
                        if action in {"approved", "retry"} and evidence_request_path.exists():
                            evidence_request_path.unlink()
                            evidence_request = None
                        break
                    atomic_json(evidence_request_path, redact_result({**validation, "rendered_verification": rendered}))
                    evidence_request = evidence_request_path
                    if evidence_attempt or rendered_command(body) is None or rendered["status"] == "failed":
                        save_state(state_path, state, current_gate="evidence-blocked", last_failure=validation_report(validation))
                        gate_finished(number, "validation", attempt, "blocked", started, findings=validation.get("findings", []), evidence_request=str(evidence_request_path), rendered=rendered)
                        fail(f"Preparação de evidências incompleta; ajuste somente a fixture/captura aprovada e retome a Validação. Pedido: {evidence_request_path}. {sanitize(validation_report(validation))}")
                    save_state(state_path, state, current_gate="evidence-preparation")
                    emit("evidence-preparation", phase=number, gate="validation", attempt=attempt, result="started", report_path=evidence_request_path)
                    previous_rendered = rendered
                    # The next pass reuses the approved capture command, never a command from agent output.
                if restart_development:
                    continue
                save_state(state_path, state, current_gate="validation")
                if action == "approved" and rendered["status"] == "failed":
                    action = "blocked"
                if action == "blocked":
                    reason = validation_report(validation) + "\n" + str(rendered.get("message", ""))
                    diagnostic = str(rendered.get("log") or EVENTS.events_path)
                    save_state(state_path, state, current_gate="validation-blocked", last_failure=reason + "\nDiagnóstico: " + diagnostic)
                    gate_finished(number, "validation", attempt, "blocked", started, findings=validation.get("findings", []), rendered=rendered)
                    fail(f"Gate 2 interrompido por verificação bloqueada; corrija o ambiente/evidências e retome o mesmo comando. Diagnóstico: {diagnostic}. {sanitize(reason)}")
                if action == "retry":
                    queue_review_correction(validation, rendered, "validation", repo)
                    correction = validation_report(validation, defects_only=True)
                    save_state(state_path, state, current_gate="development", last_failure=correction)
                    gate_finished(number, "validation", attempt, "rejected", started, findings=validation.get("findings", []))
                    if attempt == arguments.max_attempts:
                        fail(f"phase development limit reached ({attempt}); validation findings and work preserved")
                    continue
                gate_finished(number, "validation", attempt, "approved", started)

                save_state(state_path, state, current_gate="tests")
                started = gate_started(number, "tests", attempt)
                outcome = run_verification(repo, suite, body, number, arguments.tests_timeout_minutes * 60, suite_shell)
                passed, report, report_path = outcome["status"] == "completed", outcome["message"], Path(outcome["log"])
                if not passed and not outcome["diagnosable"]:
                    save_state(state_path, state, current_gate="tests-blocked", last_failure=report)
                    fail(f"Gate 3 verification blocked; source and artifacts preserved. {sanitize(report)} Diagnóstico: {outcome['directory']}/report.json")
                if not passed:
                    save_state(state_path, state, current_gate="tests-diagnosis", last_failure=report)
                    try:
                        resolution = resolve_check_failure(package, repo, values, body, number, attempt, "tests", outcome,
                                                           arguments.tests_timeout_minutes * 60, arguments.validation_timeout_minutes * 60, arguments.model,
                                                           confirm=lambda: run_verification(repo, suite, body, number, arguments.tests_timeout_minutes * 60, suite_shell))
                    except (ExecutionError, RuntimeFailure, OSError, ValueError) as error:
                        reason = "Diagnóstico da suíte indisponível: " + sanitize_text(str(error))
                        save_state(state_path, state, current_gate="tests-blocked", last_failure=reason)
                        fail(f"{reason}. Resultado original preservado: {report_path}")
                    if resolution["action"] in {"correct", "investigate"}:
                        correction = "Corrija somente os defeitos demonstrados pela suíte:\n" + validation_report(resolution["diagnosis"], defects_only=True)
                        if resolution["history"]:
                            correction += "\nInvestigação preservada: " + str(resolution["history"]["archive_path"])
                        save_state(state_path, state, current_gate="development", last_failure=correction)
                        gate_finished(number, "tests", attempt, "rejected", started, findings=resolution["diagnosis"]["findings"])
                        if attempt == arguments.max_attempts:
                            fail(f"phase development limit reached ({attempt}); suite findings and work preserved. Diagnóstico: {report_path}")
                        continue
                    if resolution["action"] == "blocked":
                        reason = validation_report(resolution["diagnosis"]) + "\n" + resolution["reason"]
                        save_state(state_path, state, current_gate="tests-blocked", last_failure=reason)
                        gate_finished(number, "tests", attempt, "blocked", started, reason=reason)
                        fail(f"Suíte com causa não resolvida; trabalho e evidências preservados. {sanitize(reason)}")
                gate_finished(number, "tests", attempt, "approved", started)
                LEDGER.verified("tests", redact_result(outcome), worktree_fingerprint(repo))

                save_state(state_path, state, current_gate="commit")
                started = gate_started(number, "commit", attempt)
                stage_phase_changes(repo, body)
                if not git(repo, "diff", "--cached", "--name-only"):
                    fail("Gate 4 has no changes to commit")
                committed = run(["git", "commit", "--no-verify", "-m", f"feat: complete phase {number} - {title}"[:72].rstrip()], repo)
                if committed.returncode:
                    fail(f"Gate 4 commit failed: {sanitize(committed.stderr or committed.stdout)}")
                commit = git(repo, "rev-parse", "HEAD")
                state["completed_phases"].append(number)
                state["phase_commits"][str(number)] = commit
                state.pop("last_failure", None)
                state.pop("current_execution_id", None)
                save_state(state_path, state, current_phase=None, current_gate=None)
                gate_finished(number, "commit", attempt, "completed", started, commit=commit)
                emit("phase-finished", phase=number, gate="commit", attempt=attempt, result="completed")
                break
        emit("developer-reminder", result="success")
        return 0
    finally:
        lock.release()


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser()
    value.add_argument("planning")
    value.add_argument("--model", default="gpt-6.1-sol")
    value.add_argument("--max-attempts", type=int, default=6)
    value.add_argument("--max-failure-attempts", type=int, default=2)
    value.add_argument("--dev-timeout-minutes", type=positive, default=60.0)
    value.add_argument("--validation-timeout-minutes", type=positive, default=30.0)
    value.add_argument("--render-timeout-minutes", type=positive, default=10.0)
    value.add_argument("--host-timeout-minutes", type=positive, default=10.0)
    value.add_argument("--tests-timeout-minutes", type=positive, default=60.0)
    value.add_argument("--verbose", action="store_true")
    return value


def main() -> int:
    arguments = parser().parse_args()
    if arguments.max_attempts < 1 or arguments.max_failure_attempts < 1:
        print("Ralph interrompido: development limits must be positive integers", file=sys.stderr)
        return 1
    try:
        return execute(arguments)
    except (ExecutionError, RuntimeFailure, OSError, KeyError, IndexError, ValueError) as exception:
        print(f"Ralph interrompido: {sanitize(str(exception))}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
