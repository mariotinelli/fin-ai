#!/usr/bin/env python3
"""Open one fresh Codex execution with a structured result contract."""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from contextlib import ExitStack
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


def permission_profile_config(cleanup: ExitStack) -> str:
    codex_home = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex")))
    source = codex_home / "config.toml"
    content = source.read_text(encoding="utf-8") if source.exists() else ""
    lines = []
    section = ""
    for line in content.splitlines(keepends=True):
        if line.lstrip().startswith("["):
            section = line.strip().split("#", 1)[0].strip()
        if not section and re.match(r"\s*(sandbox_mode|default_permissions)\s*=", line):
            continue
        if section == "[sandbox_workspace_write]":
            continue
        lines.append(line)
    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", prefix="ralph-runtime-", suffix=".config.toml", dir=codex_home, delete=False
    ) as config:
        config.write("".join(lines))
        path = Path(config.name)
    cleanup.callback(path.unlink, missing_ok=True)
    return path.name.removesuffix(".config.toml")


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
        "--output-schema",
        str(Path(arguments.schema).resolve()),
        "--output-last-message",
        str(Path(arguments.result).resolve()),
        "-",
    ]
    prompt = Path(arguments.prompt).read_text(encoding="utf-8")
    environment = os.environ.copy()
    with ExitStack() as cleanup:
        if os.name == "nt":
            config_profile = permission_profile_config(cleanup)
            command[2:2] = ["--ignore-user-config", "--profile", config_profile, "--config", 'windows.sandbox="mxc"']
            if "PLAYWRIGHT_BROWSERS_PATH" not in environment and environment.get("LOCALAPPDATA"):
                environment["PLAYWRIGHT_BROWSERS_PATH"] = str(Path(environment["LOCALAPPDATA"]) / "ms-playwright")
            profile = "ralph-validation" if arguments.mode == "validate" else "ralph-development"
            parent = ":read-only" if arguments.mode == "validate" else ":workspace"
            command[2:2] = [
                "--config", f'permissions.{profile}.extends="{parent}"',
                "--config", f"permissions.{profile}.network.enabled=true",
                "--config", f'default_permissions="{profile}"',
            ]

        if os.name == "nt" and arguments.mode == "validate":
            temporary_directory = cleanup.enter_context(tempfile.TemporaryDirectory(prefix="ralph-validation-"))
            environment.update(TEMP=temporary_directory, TMP=temporary_directory, TMPDIR=temporary_directory)
            writable_path = json.dumps(Path(temporary_directory).as_posix())
            command[2:2] = [
                "--config", f'permissions.ralph-validation.filesystem={{{writable_path}="write"}}',
            ]
            prompt += (
                "\n\nAmbiente de validação: o repositório permanece em somente leitura. "
                f"Grave capturas e artefatos temporários somente em {temporary_directory}. "
                "TEMP, TMP e TMPDIR apontam para essa pasta, removida ao encerrar a validação. "
                "Acesso de rede está disponível para inspecionar a aplicação local. "
                "Não execute operações que alterem dados da aplicação durante a revisão.\n"
            )
        elif os.name != "nt":
            command[2:2] = ["--sandbox", sandbox]

        completed = subprocess.run(
            command,
            cwd=arguments.repo,
            input=prompt,
            text=True,
            encoding="utf-8",
            errors="strict",
            check=False,
            env=environment,
        )
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
