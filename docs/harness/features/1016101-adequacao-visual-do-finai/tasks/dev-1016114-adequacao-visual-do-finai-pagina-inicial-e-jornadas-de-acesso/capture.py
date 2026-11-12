"""Gera a matriz aprovada de acesso com banco e contextos de navegador isolados."""
from __future__ import annotations

import json
import os
import shutil
import struct
import subprocess
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path


STATES = {
    "inicial": ("visitante", "autenticado"),
    "cadastro": ("padrao", "erro", "processamento"),
    "login": ("padrao", "credenciais-invalidas", "processamento", "senha-redefinida"),
    "recuperacao": ("padrao", "erro", "processamento", "sucesso"),
    "redefinicao": ("padrao", "erro", "token-invalido", "processamento"),
    "verificacao": ("padrao", "processamento", "reenviado"),
}
VIEWPORTS = ((360, 800), (390, 844), (430, 932), (600, 960), (820, 1180),
             (1024, 768), (1366, 768), (1440, 900), (1920, 1080))
REFERENCE = "docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md"


def main() -> int:
    repo = Path.cwd().resolve()
    output = Path(os.environ["RALPH_EVIDENCE_DIR"]).resolve()
    artifacts = Path(os.environ["RALPH_ARTIFACTS_DIR"]).resolve()
    output.mkdir(parents=True, exist_ok=True)
    artifacts.mkdir(parents=True, exist_ok=True)
    request = os.environ.get("RALPH_EVIDENCE_REQUEST")
    if request:
        # O pedido é somente dado; todos os estados aprovados são recriados.
        data = json.loads(request) if request.lstrip().startswith("{") else json.loads(Path(request).read_text(encoding="utf-8"))
        if not isinstance(data, dict) or not isinstance(data.get("findings"), list):
            raise ValueError("Pedido de evidências inválido: objeto com findings obrigatório")
        if not all(key in data for key in ("plan_basis", "rendered_verification")):
            raise ValueError("Pedido de evidências sem base do plano ou verificação renderizada")
        print("Pedido recebido; recriando a cobertura aprovada integral.", flush=True)

    expected = {
        (screen, state, f"{width}x{height}", theme)
        for screen, states in STATES.items() for state in states
        for width, height in VIEWPORTS for theme in ("light", "dark")
    } | {
        ("login", state, "1366x768", theme)
        for state in ("hover-recuperacao", "hover-principal") for theme in ("light", "dark")
    }
    names = {f"{screen}-{state}-{theme}-{viewport}.png" for screen, state, viewport, theme in expected}
    report = output / "captures.jsonl"
    if report.exists() or any((output / name).exists() for name in names):
        raise RuntimeError("Destino já contém esta matriz; preserve os artefatos e forneça um diretório dedicado vazio")

    php = Path.home() / ".config/herd/bin/php85/php.exe"
    if not php.is_file():
        raise RuntimeError("PHP 8.5 do Herd indisponível")
    environment = os.environ.copy()
    environment["PATH"] = str(php.parent) + os.pathsep + environment["PATH"]
    environment["APP_ENV"] = "testing"
    environment["RALPH_EVIDENCE_DIR"] = str(output)
    environment["RALPH_SCREENSHOT_PREFIX"] = os.path.relpath(output, repo / "tests/Browser/Screenshots").replace("\\", "/")
    environment.setdefault("PLAYWRIGHT_BROWSERS_PATH", str(Path(environment["LOCALAPPDATA"]) / "ms-playwright"))

    with tempfile.TemporaryDirectory(prefix="finai-access-", dir=repo / "tmp") as directory:
        temporary = Path(directory)
        fixture = temporary / "AccessEvidenceTest.php"
        shutil.copyfile(Path(__file__).with_name("capture-fixture.php"), fixture)
        config = ET.parse(repo / "phpunit.xml")
        config.getroot().attrib["bootstrap"] = (repo / "vendor/autoload.php").as_posix()
        for entry in config.iter("directory"):
            if entry.text:
                entry.text = (repo / entry.text).resolve().as_posix()
        config_path = temporary / "phpunit.xml"
        config.write(config_path, encoding="utf-8", xml_declaration=True)
        command = [str(php), "vendor/bin/pest", "--configuration", str(config_path),
                   str(fixture), "--compact", "--cache-directory", str(artifacts / "pest-capture-cache"),
                   "--log-junit", str(artifacts / "access-rendered.xml")]
        process = subprocess.Popen(command, cwd=repo, env=environment)
        (artifacts / "capture-process.json").write_text(json.dumps({"pid": process.pid}), encoding="utf-8")
        print(f"Processo Pest criado: PID {process.pid}", flush=True)
        try:
            code = process.wait()
        finally:
            if process.poll() is None:
                # Somente a árvore criada por esta execução, inclusive em interrupção.
                subprocess.run(["taskkill", "/PID", str(process.pid), "/T", "/F"], check=False)
                process.wait()
        if code:
            return code

    entries = [json.loads(line) for line in report.read_text(encoding="utf-8").splitlines() if line.strip()]
    actual = {(e["screen"], e["state"], e["viewport"], e["theme"]) for e in entries}
    if len(entries) != 364 or actual != expected:
        raise RuntimeError("Metadados não cobrem exatamente as 364 capturas aprovadas")
    if {Path(e["path"]).name for e in entries} != names:
        raise RuntimeError("Nomes de imagens divergentes da matriz aprovada")
    for entry in entries:
        path = Path(entry["path"])
        if path.parent != output or entry["reference"] != REFERENCE + " # .brand, h1, .panel, input, .btn, .notice, .error, :focus-visible; adaptação de acesso em planning.md/Arquitetura":
            raise RuntimeError("Destino ou referência de captura inválidos")
        header = path.read_bytes()[:24]
        if len(header) != 24 or header[:8] != b"\x89PNG\r\n\x1a\n":
            raise RuntimeError("PNG ausente ou inválido: " + path.name)
        width, height = struct.unpack(">II", header[16:24])
        requested_width, requested_height = map(int, entry["viewport"].split("x"))
        if width != requested_width or height < requested_height:
            raise RuntimeError("Dimensões da imagem diferentes do viewport: " + path.name)
    print(f"CAPTURE_OK: 364 imagens e metadados verificados em {output}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
