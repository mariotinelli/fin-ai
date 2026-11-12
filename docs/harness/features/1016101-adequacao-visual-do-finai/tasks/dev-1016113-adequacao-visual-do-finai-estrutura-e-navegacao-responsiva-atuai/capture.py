import json, os, struct, subprocess, tempfile, xml.etree.ElementTree as ET
from pathlib import Path
repo = Path.cwd()
output = Path(os.environ['RALPH_EVIDENCE_DIR']).resolve()
output.mkdir(parents=True, exist_ok=True)
environment = os.environ.copy()
php = Path.home() / '.config/herd/bin/php85/php.exe'
environment['PATH'] = str(php.parent) + os.pathsep + environment['PATH']
environment['APP_ENV'] = 'testing'
environment['PLAYWRIGHT_BROWSERS_PATH'] = str(Path(environment['LOCALAPPDATA']) / 'ms-playwright')
environment['RALPH_SCREENSHOT_PREFIX'] = os.path.relpath(output, repo / 'tests/Browser/Screenshots').replace('\\', '/')
request = environment.get('RALPH_EVIDENCE_REQUEST')
if request:
    report = json.loads(Path(request).read_text(encoding='utf-8'))
    assert isinstance(report, dict) and isinstance(report.get('findings'), list), 'Pedido de evidências inválido'
    print('Pedido recebido; recriando toda a cobertura aprovada.', flush=True)
artifacts = Path(environment['RALPH_ARTIFACTS_DIR']).resolve()
subprocess.run(['bun', 'run', 'build'], env=environment, check=True)
fixture = r'''<?php
declare(strict_types=1);
use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Support\Facades\Vite;
use Tests\TestCase;
pest()->extend(TestCase::class)->use(RefreshDatabase::class)->in(__DIR__);
it('captures the authenticated shell', function (string $route): void {
    config(['inertia.ssr.enabled' => false]);
    Vite::useHotFile(__DIR__.'/no-hot-file');
    $user = User::factory()->withoutTwoFactor()->create();
    $this->actingAs($user)->withSession(['auth.password_confirmed_at' => time()]);
    $page = visit(route($route));
    foreach (['light', 'dark'] as $theme) {
        $page->script("localStorage.setItem('appearance', '$theme')");
        $page->refresh()->assertScript('window.location.pathname', parse_url(route($route), PHP_URL_PATH));
        foreach ([[360,800],[390,844],[430,932],[600,960],[820,1180],[1024,768],[1366,768],[1440,900],[1920,1080]] as [$width,$height]) {
            $page->refresh()->resize($width,$height)->assertNoJavaScriptErrors()
                ->assertScript('document.documentElement.style.colorScheme', $theme)
                ->assertScript('document.documentElement.scrollWidth <= innerWidth', true);
            $states = $route === 'dashboard' ? ['default','menu-open','menu-keyboard'] : ['default'];
            if ($route === 'dashboard' && $width === 1366) {
                $states[] = 'desktop-collapsed';
            }
            foreach ($states as $state) {
                if ($state === 'desktop-collapsed') {
                    $page->click('[data-sidebar="trigger"]')
                        ->assertVisible('.finai-navigation[data-collapsible="icon"]')
                        ->assertScript('Math.round(document.querySelector(".finai-navigation").getBoundingClientRect().width)', 80)
                        ->assertScript('document.documentElement.scrollWidth <= innerWidth', true);
                } elseif ($state !== 'default') {
                    if ($page->script('Array.from(document.querySelectorAll("[data-test=sidebar-menu-button]")).every(el => el.getClientRects().length === 0)')) {
                        $page->click('[data-sidebar="trigger"]');
                    }
                    if ($state === 'menu-open') {
                        $page->click('@sidebar-menu-button');
                    } else {
                        $page->keys('@sidebar-menu-button', 'Enter')->keys('[role="menu"]', 'ArrowDown');
                    }
                    $page->assertVisible('[role="menu"]')->assertSee('Settings')->assertSee('Log out');
                    if ($state === 'menu-keyboard') {
                        $page->assertScript('document.activeElement.getAttribute("role") === "menuitem"', true);
                    }
                }
                $name = str_replace('.', '-', $route).'-'.$state.'-'.$theme.'-'.$width.'x'.$height.'.png';
                $page->screenshot(filename: getenv('RALPH_SCREENSHOT_PREFIX').'/'.$name);
                $entry = ['path'=>getenv('RALPH_EVIDENCE_DIR').'/'.$name,'reference'=>'docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md','screen'=>$route,'state'=>$state,'viewport'=>$width.'x'.$height,'theme'=>$theme];
                $line = json_encode($entry, JSON_THROW_ON_ERROR|JSON_UNESCAPED_SLASHES);
                file_put_contents(getenv('RALPH_EVIDENCE_DIR').'/captures.jsonl', $line.PHP_EOL, FILE_APPEND);
                echo $line.PHP_EOL;
                if ($state === 'desktop-collapsed') {
                    $page->click('[data-sidebar="trigger"]')
                        ->assertScript('document.querySelector(".finai-navigation").getAttribute("data-collapsible")', null);
                } elseif ($state !== 'default') {
                    $page->keys('[role="menu"]', 'Escape');
                }
            }
        }
    }
    $this->assertAuthenticatedAs($user);
})->with(['dashboard','user-profile.edit','password.edit','appearance.edit','two-factor.show','user-passkey.index']);
'''
with tempfile.TemporaryDirectory(prefix='shell-evidence-', dir=repo / 'tmp') as directory:
    temporary = Path(directory)
    test = temporary / 'ShellEvidenceTest.php'
    test.write_text(fixture, encoding='utf-8')
    config = ET.parse(repo / 'phpunit.xml')
    config.getroot().attrib.pop('bootstrap', None)
    for entry in config.iter('directory'):
        if entry.text:
            entry.text = (repo / entry.text).resolve().as_posix()
    config_path = temporary / 'phpunit.xml'
    config.write(config_path, encoding='utf-8', xml_declaration=True)
    subprocess.run([str(php),'vendor/bin/pest','--configuration',str(config_path),str(test),'--compact','--cache-directory',str(artifacts/'pest-cache'),'--log-junit',str(artifacts/'rendered.xml')],env=environment,check=True)
entries = [json.loads(line) for line in (output/'captures.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
assert len(entries) == 146 and len({entry['path'] for entry in entries}) == 146, 'Cobertura incompleta'
for entry in entries:
    header = Path(entry['path']).read_bytes()[:24]
    assert header[:8] == b'\x89PNG\r\n\x1a\n' and len(header) == 24, 'PNG inválido'
    width, height = struct.unpack('>II', header[16:24])
    assert width == int(entry['viewport'].split('x')[0]) and height > 0, 'Imagem ilegível ou viewport incorreta'
print(f'CAPTURE_OK: {len(entries)} imagens protegidas e metadados em {output}', flush=True)
