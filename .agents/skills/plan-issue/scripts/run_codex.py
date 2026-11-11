#!/usr/bin/env python3
"""Open one fresh Codex execution with a structured result contract."""
from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
from ralph_runtime import sanitize


def cli_compatibility(codex: str, repo: str, sandbox: str) -> str | None:
    """Inspect the installed CLI's public flags without starting a model session."""
    try:
        probe = subprocess.run(
            [codex, "exec", "--help"], cwd=repo, capture_output=True,
            text=True, encoding="utf-8", errors="replace", timeout=15, check=False,
        )
    except subprocess.TimeoutExpired:
        return "Tempo limite ao consultar o Codex; verifique instalação e configuração com codex exec --help."
    except OSError:
        return "Não foi possível iniciar o Codex configurado; verifique CODEX_BIN ou a instalação no PATH."
    if probe.returncode:
        detail = sanitize(probe.stderr or probe.stdout or f"exit {probe.returncode}")
        return f"Falha ao consultar instalação/configuração do Codex: {detail}"
    help_text = re.sub(r"\x1b\[[0-?]*[ -/]*[@-~]", "", probe.stdout or "")
    required = ("--model", "--config", "--sandbox", "--output-schema", "--output-last-message")
    missing = [flag for flag in required if not re.search(r"(?m)^\s*(?:-\w,\s*)?" + re.escape(flag) + r"(?:\s|=|$)", help_text)]
    if missing or sandbox not in help_text:
        return "Codex incompatível com este runner: faltam " + ", ".join(missing or [sandbox]) + ". Atualize o CLI ou selecione um runner compatível; permissões não foram ampliadas."
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("develop", "validate"), required=True)
    parser.add_argument("--prompt", required=True)
    parser.add_argument("--schema", required=True)
    parser.add_argument("--result", required=True)
    parser.add_argument("--repo", required=True)
    parser.add_argument("--model", default=os.environ.get("RALPH_MODEL", "gpt-6.1-sol"))
    arguments = parser.parse_args()

    sandbox = "workspace-write" if arguments.mode == "develop" else "read-only"
    configured_codex = os.environ.get("CODEX_BIN")
    codex = configured_codex or shutil.which("codex") or "codex"
    incompatibility = cli_compatibility(codex, arguments.repo, sandbox)
    if incompatibility:
        print("ERROR: " + incompatibility, file=sys.stderr)
        return 64
    command = [
        codex,
        "exec",
        "--model",
        arguments.model,
        "--config",
        'model_reasoning_effort="medium"',
        "--sandbox",
        sandbox,
        "--output-schema",
        str(Path(arguments.schema).resolve()),
        "--output-last-message",
        str(Path(arguments.result).resolve()),
        "-",
    ]
    prompt = Path(arguments.prompt).read_text(encoding="utf-8")
    completed = subprocess.run(
        command,
        cwd=arguments.repo,
        input=prompt,
        text=True,
        encoding="utf-8",
        errors="strict",
        check=False,
    )
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
