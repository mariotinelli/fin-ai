"""Capture the approved phase-two states with isolated Laravel browser fixtures."""
from __future__ import annotations

import json
import os
import shutil
import struct
import subprocess
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path


STATES = (
    "login-positive", "recovery-positive", "verification-positive", "profile-unverified",
    "profile-verification-positive", "two-factor-authentication-link", "two-factor-recovery-link",
)
VIEWPORTS = ((360, 800), (390, 844), (430, 932), (600, 960), (820, 1180), (1024, 768), (1366, 768), (1440, 900), (1920, 1080))


def main() -> int:
    repo = Path.cwd().resolve()
    output = Path(os.environ["RALPH_EVIDENCE_DIR"]).resolve()
    output.mkdir(parents=True, exist_ok=True)
    preflight = os.environ.get("RALPH_CAPTURE_MODE") == "preflight"
    request = os.environ.get("RALPH_EVIDENCE_REQUEST")
    if request:
        data = json.loads(Path(request).read_text(encoding="utf-8"))
        if not isinstance(data, dict) or not isinstance(data.get("findings"), list):
            raise ValueError("Invalid evidence request: expected an object with findings")
        print(f"Pedido de evidências recebido ({len(data['findings'])} achados); gerando toda a cobertura aprovada.", flush=True)

    environment = os.environ.copy()
    php = Path.home() / ".config/herd/bin/php85/php.exe"
    if not php.is_file():
        raise RuntimeError("PHP 8.5 do Herd indisponível; captura interrompida")
    environment["PATH"] = str(php.parent) + os.pathsep + environment["PATH"]
    environment.setdefault("PLAYWRIGHT_BROWSERS_PATH", str(Path(environment["LOCALAPPDATA"]) / "ms-playwright"))
    environment["APP_ENV"] = "testing"
    environment["RALPH_EVIDENCE_DIR"] = str(output)
    if not preflight:
        build = subprocess.run([shutil.which("bun") or "bun", "run", "build"], cwd=repo, env=environment, check=False)
        if build.returncode:
            return build.returncode

    with tempfile.TemporaryDirectory(prefix="finai-evidence-", dir=repo / "tmp") as directory:
        temporary = Path(directory)
        fixture = temporary / "PhaseTwoEvidenceTest.php"
        shutil.copyfile(Path(__file__).with_name("capture-fixture.php"), fixture)
        config = ET.parse(repo / "phpunit.xml")
        config.getroot().attrib.pop("bootstrap", None)
        for entry in config.iter("directory"):
            if entry.text:
                entry.text = (repo / entry.text).resolve().as_posix()
        config_path = temporary / "phpunit.xml"
        config.write(config_path, encoding="utf-8", xml_declaration=True)
        environment["RALPH_SCREENSHOT_PREFIX"] = os.path.relpath(output, repo / "tests/Browser/Screenshots").replace("\\", "/")
        command = [str(php), "vendor/bin/pest", "--configuration", str(config_path), str(fixture), "--compact", "--filter", "authenticated preflight" if preflight else "approved missing state"]
        result = subprocess.run(command, cwd=repo, env=environment, check=False)
        if result.returncode:
            return result.returncode

    expected = {f"preflight-{theme}.png" for theme in ("light", "dark")} if preflight else {
        f"{state}-{theme}-{width}x{height}.png"
        for state in STATES for theme in ("light", "dark") for width, height in VIEWPORTS
    }
    for name in sorted(expected):
        image = output / name
        if not image.is_file():
            raise RuntimeError("Estado esperado sem captura: " + name)
        header = image.read_bytes()[:24]
        if header[:8] != b"\x89PNG\r\n\x1a\n" or len(header) != 24:
            raise RuntimeError("Captura PNG inválida: " + name)
        width, height = struct.unpack(">II", header[16:24])
        if width < 360 or height < 1:
            raise RuntimeError("Captura ilegível: " + name)
        if not preflight and width != int(name.rsplit("-", 1)[1].split("x")[0]):
            raise RuntimeError("Viewport diferente do solicitado: " + name)
    if not preflight:
        entries = [json.loads(line) for line in (output / "captures.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
        if {Path(entry["path"]).name for entry in entries} != expected:
            raise RuntimeError("O relatório não cobre exatamente todos os estados aprovados")
    print(f"CAPTURE_OK: {len(expected)} imagens verificadas em {output}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
