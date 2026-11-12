"""Gera a matriz aprovada usando formulários reais e banco de testes isolado."""
from __future__ import annotations

import json
import os
import shutil
import struct
import subprocess
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

from PIL import Image, ImageDraw

VIEWPORTS = ((360, 800), (390, 844), (430, 932), (600, 960), (820, 1180), (1024, 768), (1366, 768), (1440, 900), (1920, 1080))
ADDITIONAL = {
    'profile': ('error', 'success', 'unverified', 'resent', 'processing'),
    'password': ('error', 'success', 'processing'),
    'deletion': ('error', 'processing'),
}


def matrix() -> list[list]:
    cases = [[surface, 'default', theme, width, height]
             for surface in ('profile', 'password', 'appearance', 'deletion')
             for theme in ('light', 'dark') for width, height in VIEWPORTS]
    cases += [[surface, state, theme, width, height]
              for surface, states in ADDITIONAL.items() for state in states
              for theme in ('light', 'dark') for width, height in ((360, 800), (1366, 768))]
    cases += [['appearance', 'system', theme, 1366, 768] for theme in ('light', 'dark')]
    cases += [['profile', 'hover', theme, 1366, 768] for theme in ('light', 'dark')]
    assert len(cases) == 116
    return cases


def name(case: list) -> str:
    surface, state, theme, width, height = case
    return f'{surface}-{state}-{theme}-{width}x{height}.png'


def main() -> int:
    repo = Path.cwd().resolve()
    output = Path(os.environ['RALPH_EVIDENCE_DIR']).resolve()
    artifacts = Path(os.environ['RALPH_ARTIFACTS_DIR']).resolve()
    output.mkdir(parents=True, exist_ok=True)
    artifacts.mkdir(parents=True, exist_ok=True)
    request = os.environ.get('RALPH_EVIDENCE_REQUEST')
    if request:
        data = json.loads(Path(request).read_text(encoding='utf-8-sig'))
        if not isinstance(data, dict):
            raise ValueError('Pedido de evidências precisa ser um objeto JSON')
        print('Pedido suplementar lido como dados; será recriada a matriz aprovada inteira.', flush=True)
    cases = matrix()
    environment = os.environ.copy()
    php = Path.home() / '.config/herd/bin/php85/php.exe'
    if not php.is_file():
        raise RuntimeError('PHP 8.5 do Herd indisponível')
    environment['APP_ENV'] = 'testing'
    environment['PATH'] = str(php.parent) + os.pathsep + environment['PATH']
    environment.setdefault('PLAYWRIGHT_BROWSERS_PATH', str(Path(environment['LOCALAPPDATA']) / 'ms-playwright'))
    with tempfile.TemporaryDirectory(prefix='finai-settings-', dir=repo / 'tmp') as directory:
        temporary = Path(directory)
        fixture = temporary / 'PersonalSettingsEvidenceTest.php'
        shutil.copyfile(Path(__file__).with_name('capture-fixture.php'), fixture)
        matrix_path = temporary / 'matrix.json'
        matrix_path.write_text(json.dumps(cases), encoding='utf-8')
        environment['RALPH_CAPTURE_MATRIX'] = str(matrix_path)
        environment['RALPH_SCREENSHOT_PREFIX'] = os.path.relpath(output, repo / 'tests/Browser/Screenshots').replace('\\', '/')
        config = ET.parse(repo / 'phpunit.xml')
        config.getroot().attrib.pop('bootstrap', None)
        for entry in config.iter('directory'):
            if entry.text:
                entry.text = (repo / entry.text).resolve().as_posix()
        config_path = temporary / 'phpunit.xml'
        config.write(config_path, encoding='utf-8', xml_declaration=True)
        command = [str(php), 'vendor/bin/pest', '--configuration', str(config_path), str(fixture), '--compact',
                   '--cache-directory', str(artifacts / 'capture-pest-cache'), '--log-junit', str(artifacts / 'capture.xml')]
        process = subprocess.Popen(command, cwd=repo, env=environment)
        print(f'Processo próprio de captura: PID {process.pid}', flush=True)
        try:
            result = process.wait()
        finally:
            if process.poll() is None:
                process.terminate()
                try:
                    process.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    process.kill()
                    process.wait()
        if result:
            return result
    entries = [json.loads(line) for line in (output / 'captures.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
    by_name = {Path(entry['path']).name: entry for entry in entries}
    expected = {name(case) for case in cases}
    if not expected.issubset(by_name):
        raise RuntimeError('Metadados incompletos: ' + ', '.join(sorted(expected - by_name.keys())))
    for case in cases:
        image = output / name(case)
        header = image.read_bytes()[:24]
        if len(header) != 24 or header[:8] != b'\x89PNG\r\n\x1a\n':
            raise RuntimeError('PNG inválido: ' + image.name)
        width, height = struct.unpack('>II', header[16:24])
        if width != case[3] or height < case[4]:
            raise RuntimeError('Dimensões diferentes do solicitado: ' + image.name)
    # Mantém os originais e monta pares em escala 1:1, com identificação legível.
    montages = []
    for surface in ('profile', 'password', 'appearance', 'deletion'):
        for theme in ('light', 'dark'):
            selected = [case for case in cases if case[0] == surface and case[2] == theme and case[3] in (360, 1366)]
            images = [Image.open(output / name(case)).convert('RGB') for case in selected]
            try:
                canvas = Image.new('RGB', (max(image.width for image in images), sum(image.height + 40 for image in images)), 'white')
                draw = ImageDraw.Draw(canvas)
                top = 0
                for case, image in zip(selected, images):
                    draw.text((12, top + 10), name(case), fill='black')
                    canvas.paste(image, (0, top + 40))
                    top += image.height + 40
                montage = output / f'montagem-{surface}-{theme}.png'
                canvas.save(montage)
                montages.append(str(montage))
            finally:
                for image in images:
                    image.close()
    (output / 'captures.json').write_text(json.dumps(list(by_name.values()), ensure_ascii=False, indent=2), encoding='utf-8')
    (output / 'montagens.json').write_text(json.dumps(montages, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'CAPTURE_OK: {len(expected)} imagens e {len(montages)} montagens verificadas em {output}', flush=True)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
