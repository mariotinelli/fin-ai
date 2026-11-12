#!/usr/bin/env python3
"""Execute planning.md phases with four gates and minimal resumable state."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
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
from typing import Any

sys.dont_write_bytecode = True
from ralph_runtime import EventSink, RuntimeFailure, TaskLock, atomic_json, popen_group, sanitize, sanitize_text, SECRET_KEYS, terminate_process_tree


class ExecutionError(RuntimeError):
    pass


EVENTS: EventSink | None = None
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


def worktree_fingerprint(repo: Path) -> str:
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
        path = repo / name
        result.update(name.encode("utf-8"))
        result.update(os.readlink(path).encode("utf-8") if path.is_symlink() else path.read_bytes())
    return result.hexdigest()


def render(template: Path, values: dict[str, str]) -> str:
    text = template.read_text(encoding="utf-8")
    for key, value in values.items():
        text = text.replace("{{" + key + "}}", value)
    return text


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


def stream_agent(process: subprocess.Popen[Any], timeout: float, stdout_path: Path, stderr_path: Path, phase: int, mode: str) -> tuple[str, str, int]:
    """Drain both pipes concurrently; keep sanitized diagnostics even on interruption."""
    global ACTIVE_PROCESS
    ACTIVE_PROCESS = process
    outputs: list[list[str]] = [[], []]
    failures: list[Exception] = []

    def drain(pipe: Any, path: Path, output: list[str]) -> None:
        try:
            with path.open("w", encoding="utf-8", newline="\n") as stream:
                for line in pipe:
                    safe = sanitize_text(line)
                    output.append(safe)
                    stream.write(safe)
                    stream.flush()
        except Exception as error:
            failures.append(error)

    readers = [threading.Thread(target=drain, args=(pipe, path, output), daemon=True)
               for pipe, path, output in zip((process.stdout, process.stderr), (stdout_path, stderr_path), outputs)]
    started = time.monotonic()
    next_progress = started + 30
    try:
        for reader in readers:
            reader.start()
        while process.poll() is None:
            now = time.monotonic()
            if CANCELLED or now - started >= timeout:
                terminate_process_tree(process)
                fail("execution cancelled" if CANCELLED else f"process timed out after {timeout:g} seconds")
            if now >= next_progress:
                emit("agent-progress", phase=phase, gate="development" if mode == "develop" else "validation",
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
            gate = "Gate 1" if mode == "develop" else "Gate 2"
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
        if finding.get("kind") == "evidence-missing":
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
    before = worktree_fingerprint(repo)
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
            passed, output, _ = run_tests(repo, capture[0], phase, timeout, capture[1], environment=environment, output_path=log, label=heading)
        report["message"] = output
        if directory.is_symlink() or directory.resolve() != canonical:
            fail("capture directory was redirected")
        for path in directory.rglob("*"):
            if path.is_symlink() or not path.resolve().is_relative_to(canonical):
                fail("rendered evidence contains an unsafe path")
            if path.is_file() and path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}:
                report["images"].append(str(path.resolve()))
        if passed and report["images"]:
            report["status"] = "completed"
        elif passed:
            report["message"] = "O comando terminou sem capturas renderizadas no RALPH_EVIDENCE_DIR."
    except (ExecutionError, OSError) as error:
        if CANCELLED:
            raise
        report["message"] = sanitize_text(str(error))
    if worktree_fingerprint(repo) != before:
        fail(f"rendered verification modified repository source; changes preserved. Diagnóstico: {log}")
    atomic_json(directory / "report.json", report)
    return report


def run_host_checks(repo: Path, phase_body: str, phase: int, timeout: float, pending: list[str]) -> dict[str, Any]:
    """Complete only plan-declared checks, without allowing them to edit source."""
    if EVENTS is None:
        fail("runtime log is unavailable")
    report: dict[str, Any] = {"status": "failed", "checks": [], "message": ""}
    report_path = EVENTS.root.parent / f"phase-{phase}-host-checks.json"
    try:
        host = rendered_command(phase_body, "Verificação no host")
        if "host" in pending and host is None:
            fail("pending host check requires an approved Verificação no host command in planning.md")
        if "rendered" in pending and rendered_command(phase_body) is None:
            fail("pending rendered check requires an approved Verificação renderizada command in planning.md")
        if host is not None:
            log = EVENTS.private_file(f"phase-{phase}-host-checks.log")
            before = worktree_fingerprint(repo)
            try:
                environment = os.environ.copy()
                for name in ("RALPH_CAPTURE_MODE", "RALPH_EVIDENCE_DIR", "RALPH_EVIDENCE_REQUEST"):
                    environment.pop(name, None)
                with tempfile.TemporaryDirectory(prefix="ralph-host-check-") as temporary:
                    environment.update(TEMP=temporary, TMP=temporary, TMPDIR=temporary)
                    passed, message, _ = run_tests(repo, host[0], phase, timeout, host[1], environment=environment, output_path=log, label="Verificação no host")
            finally:
                if worktree_fingerprint(repo) != before:
                    fail(f"host verification modified repository source; changes preserved. Diagnóstico: {log}")
            report["checks"].append({"check": "host", "status": "completed" if passed else "failed", "message": message, "log": str(log)})
            if not passed:
                fail(f"Verificação no host falhou; diagnostique ambiente ou defeito antes de corrigir código. Diagnóstico: {log}. {message}")
        if "rendered" in pending:
            rendered = run_rendered_verification(repo, phase_body, phase, timeout)
            report["rendered"] = rendered
            report["checks"].append({"check": "rendered", "status": rendered["status"], "log": rendered.get("log")})
            if rendered["status"] != "completed":
                fail(f"Verificação renderizada no host incompleta. Diagnóstico: {rendered.get('log')}. {rendered.get('message', '')}")
        report["status"] = "completed"
        report["message"] = "Verificações declaradas no host concluídas; revisão independente pendente."
    except (ExecutionError, RuntimeFailure, OSError) as error:
        report["message"] = sanitize_text(str(error))
    atomic_json(report_path, redact_result(report))
    if CANCELLED:
        fail(f"execution cancelled; host diagnostics preserved: {report_path}")
    return report


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
    global EVENTS
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
            if state.get("current_phase") == number and state.get("current_gate") == "commit" and not worktree_changes(repo):
                state["completed_phases"].append(number)
                state["phase_commits"][str(number)] = git(repo, "rev-parse", "HEAD")
                save_state(state_path, state, current_phase=None, current_gate=None)
                emit("phase-resumed", phase=number, gate="commit", result="resumed")
                continue
            if worktree_changes(repo) and state.get("current_phase") != number:
                fail("worktree has changes unrelated to the resumable phase; commit or discard them before Ralph")
            previous_gate = state.get("current_gate") if state.get("current_phase") == number else None
            resume_validation = previous_gate in {"validation", "validation-blocked", "evidence-preparation", "evidence-blocked"}
            resume_host = previous_gate in {"host-checks", "host-checks-blocked"}
            save_state(state_path, state, current_phase=number, current_gate="host-checks" if resume_host else "validation" if resume_validation else "development")
            emit("phase-started", phase=number, result="started")
            correction = str(state.get("last_failure", "")).strip() if previous_gate == "development" else ""
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
            for attempt in range(1, arguments.max_attempts + 1):
                values = {"REPOSITORY": str(repo), "CONTEXT_PATHS": context, "PHASE": body, "PHASE_NUMBER": str(number), "CORRECTION_REPORT": correction,
                          "RENDERED_VERIFICATION": json.dumps(rendered, ensure_ascii=False, indent=2),
                          "VALIDATION_PREFLIGHT": json.dumps(preflight, ensure_ascii=False, indent=2)}
                prepared_rendered = None
                host_report: dict[str, Any] = {"status": "not-configured", "checks": []}
                if not resume_validation and not resume_host:
                    previous_rendered = {}
                    started = gate_started(number, "development", attempt)
                    template = package / "prompts" / ("correct.md" if correction else "develop.md")
                    report_available = False
                    try:
                        result = invoke_agent(package, repo, "develop", render(template, values), package / "schemas" / "development-result.schema.json", number, arguments.dev_timeout_minutes * 60, arguments.model)
                        development = redact_result(result)
                        atomic_json(development_path, development)
                        report_available = True
                        validate_result(development, "develop")
                        if development["status"] == "blocked":
                            fail(f"Desenvolvimento bloqueado: {development_report(development)}")
                        if not worktree_changes(repo):
                            fail(f"Gate 1 finished without repository changes. {development_report(development)}")
                    except (ExecutionError, RuntimeFailure, OSError) as error:
                        reason = sanitize_text(str(error))
                        diagnostic = development_path if report_available else EVENTS.events_path
                        save_state(state_path, state, current_gate="development-blocked", last_failure=reason)
                        gate_finished(number, "development", attempt, "blocked", started, reason=reason, report_path=str(diagnostic))
                        fail(f"{sanitize(reason)} Diagnóstico: {diagnostic}. Corrija o impedimento e retome o mesmo comando; trabalho preservado.")
                    gate_finished(number, "development", attempt, "pending" if development["status"] == "ready-for-host-checks" else "completed", started)
                if not resume_validation and (resume_host or development.get("status") == "ready-for-host-checks" or rendered_command(body, "Verificação no host") is not None):
                    save_state(state_path, state, current_gate="host-checks")
                    started = gate_started(number, "host-checks", attempt)
                    host_report = run_host_checks(repo, body, number, arguments.host_timeout_minutes * 60, development.get("pending_checks", []))
                    diagnostic = EVENTS.root.parent / f"phase-{number}-host-checks.json"
                    if host_report["status"] != "completed":
                        reason = str(host_report.get("message", "Verificações no host incompletas"))
                        save_state(state_path, state, current_gate="host-checks-blocked", last_failure=reason)
                        gate_finished(number, "host-checks", attempt, "blocked", started, reason=reason, report_path=str(diagnostic))
                        fail(f"{sanitize(reason)} Relatório: {diagnostic}. Retome o mesmo comando após diagnosticar/corrigir o impedimento; Desenvolvimento preservado.")
                    prepared_rendered = host_report.get("rendered")
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
                for evidence_attempt in range(2):
                    rendered = prepared_rendered if evidence_attempt == 0 and prepared_rendered is not None else run_rendered_verification(repo, body, number, arguments.render_timeout_minutes * 60, evidence_request=evidence_request)
                    if previous_rendered:
                        rendered["previous_reports"] = [previous_rendered]
                        rendered["images"] = list(dict.fromkeys([*previous_rendered.get("images", []), *rendered.get("images", [])]))
                    values["RENDERED_VERIFICATION"] = json.dumps(rendered, ensure_ascii=False, indent=2)
                    values["DEVELOPMENT_REPORT"] = json.dumps(development, ensure_ascii=False, indent=2)
                    values["HOST_VERIFICATION"] = json.dumps(host_report, ensure_ascii=False, indent=2)
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
                    correction = validation_report(validation, defects_only=True)
                    save_state(state_path, state, current_gate="development", last_failure=correction)
                    gate_finished(number, "validation", attempt, "rejected", started, findings=validation.get("findings", []))
                    if attempt == arguments.max_attempts:
                        fail(f"Gate 2 rejected phase {number} {attempt} times; changes were preserved")
                    continue
                gate_finished(number, "validation", attempt, "approved", started)

                save_state(state_path, state, current_gate="tests")
                started = gate_started(number, "tests", attempt)
                passed, report, report_path = run_tests(repo, suite, number, arguments.tests_timeout_minutes * 60, suite_shell)
                if not passed:
                    correction = f"A suíte completa falhou. Corrija estas falhas:\n\n{report}"
                    save_state(state_path, state, current_gate="development", last_failure=correction)
                    gate_finished(number, "tests", attempt, "rejected", started, normalized_failures=[report])
                    if attempt == arguments.max_attempts:
                        fail(f"Gate 3 failed phase {number} {attempt} times. Diagnóstico: {report_path}")
                    continue
                gate_finished(number, "tests", attempt, "approved", started)

                save_state(state_path, state, current_gate="commit")
                started = gate_started(number, "commit", attempt)
                staged = run(["git", "add", "--all"], repo)
                if staged.returncode:
                    fail("Gate 4 could not stage phase changes")
                if not git(repo, "diff", "--cached", "--name-only"):
                    fail("Gate 4 has no changes to commit")
                committed = run(["git", "commit", "--no-verify", "-m", f"feat: complete phase {number} - {title}"[:72].rstrip()], repo)
                if committed.returncode:
                    fail(f"Gate 4 commit failed: {sanitize(committed.stderr or committed.stdout)}")
                commit = git(repo, "rev-parse", "HEAD")
                state["completed_phases"].append(number)
                state["phase_commits"][str(number)] = commit
                state.pop("last_failure", None)
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
    value.add_argument("--max-attempts", type=int, default=3)
    value.add_argument("--dev-timeout-minutes", type=positive, default=60.0)
    value.add_argument("--validation-timeout-minutes", type=positive, default=30.0)
    value.add_argument("--render-timeout-minutes", type=positive, default=10.0)
    value.add_argument("--host-timeout-minutes", type=positive, default=10.0)
    value.add_argument("--tests-timeout-minutes", type=positive, default=60.0)
    value.add_argument("--verbose", action="store_true")
    return value


def main() -> int:
    arguments = parser().parse_args()
    if arguments.max_attempts < 1:
        print("Ralph interrompido: --max-attempts must be a positive integer", file=sys.stderr)
        return 1
    try:
        return execute(arguments)
    except (ExecutionError, RuntimeFailure, OSError, KeyError, IndexError, ValueError) as exception:
        print(f"Ralph interrompido: {sanitize(str(exception))}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
