# DEV #1016113 — Estrutura e navegação responsiva atuais

## Identidade e fontes

- Filha #1016113: `[DEV] [WEB] [USUARIO] Adequação visual do FinAI - Estrutura e navegação responsiva atuais`, em `task.md` neste diretório.
- Pai: `docs/harness/features/1016101-adequacao-visual-do-finai/feature.md`, R1, R2, R4, R7, CA1, CA6, CA7 e CA9, nos limites desta filha.
- Sequenciamento publicado em `docs/harness/scopes/2026-11-11-finai-mvp/scope.md`: fundação visual antes das Features de negócio; esta filha integra #1016112 e bloqueia QA #1016117. Não alterar numeração ou relações.
- Referência principal `design-input-001`: `.app`, `.sidebar`, `.workspace`, `.topbar`, `.brand`, `.nav-link`, `main` e media queries 767/1023/1200/1440. O original é `C:/Users/maari/Downloads/FinAI-Controle-Financeiro.zip`; usar a fonte normalizada abaixo como leitura obrigatória.
- Adaptações aprovadas: aplicar a estrutura às telas atuais, preservar claro/escuro/sistema e destinos existentes; não reproduzir navegação financeira futura, armazenamento local ou conta simulada. Menu de usuário/configurações/saída permanecem acessíveis inclusive onde a referência oculta seu rodapé.
- Instruções: `AGENTS.md` e skills `tailwindcss-development`, `inertia-react-development`, `wayfinder-development` e `testing-best-practices`. `.ai/rules` não existe nesta inspeção.

## Referências visuais

- `docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md`

## Objetivo

Adequar o shell autenticado à geometria e organização responsiva FinAI, preservando navegação, configurações, menu do usuário, saída e restrições de acesso.

## Estado atual

- A identidade de #1016112 já está implementada: `resources/css/app.css` define cores FinAI, corpo system-ui, serif Georgia, controles 8 px, painéis 16 px e variante escura; `app-logo.tsx` e `app-logo-icon.tsx` fornecem a marca. O histórico contém o merge `b5d655a` dessa entrega. Não refazer tokens/identidade nesta tarefa.
- `resources/js/layouts/app-layout.tsx` usa `app/app-sidebar-layout.tsx`; este compõe `AppShell`, `AppSidebar`, `AppContent` e `AppSidebarHeader`. O shell usa `SidebarProvider` com preferência `sidebarOpen` recebida do Inertia.
- `components/ui/sidebar.tsx` define largura 16 rem, variante inset com margens/raio, desktop a partir de 768 px e sheet móvel. `app-sidebar-header.tsx` tem altura 64 px, reduzida no modo recolhido. Isso diverge dos limiares e da geometria do design.
- `app-sidebar.tsx` oferece Dashboard, Repository e Documentation, além de `NavUser`; `nav-main.tsx` indica destino ativo e mostra Platform. `nav-user.tsx` abre menu Radix pelo seletor `data-test="sidebar-menu-button"`. `user-menu-content.tsx` usa Wayfinder para Settings e Log out, faz limpeza móvel e `router.flushAll()` na saída. Preservar esses destinos e operações.
- `layouts/settings/layout.tsx` fornece navegação Profile, Password, Two-Factor Auth, Passkeys e Appearance. Sua composição interna e formulários pertencem às irmãs #1016115/#1016116; nesta filha verificar integração com o shell, sem redesenhá-los.
- `routes/web.php`: dashboard e configurações de senha/aparência/2FA/passkeys exigem auth+verified; perfil exige auth. Passkeys ainda exige confirmação de senha no controller. Nenhuma nova rota é necessária.
- `app-header.tsx`/`app-header-layout.tsx` são uma alternativa existente, mas não são o layout usado pelas páginas atuais. Não trocar para essa alternativa presumindo fidelidade: ela também tem header 64 px e sheet móvel. Reutilizar apenas elementos compatíveis.
- O preflight autenticado com factory isolada abriu o dashboard em 1366×768, validou os temas e salvou duas capturas. A imagem clara foi aberta: marca FinAI já presente, sidebar inset de 256 px e cabeçalho estreito ainda visíveis. A comparação primária usa CSS/estrutura da referência normalizada; a implementação atual não é autoridade visual.

## Escopo

Inclui shell autenticado compartilhado, sidebar/topo responsivos, cabeçalho, região de conteúdo, indicação ativa, integração da marca/temas existentes e acesso ao menu do usuário e aos destinos atuais por mouse e teclado. Inclui suporte de captura temporária e testes de regressão da navegação alterada.

Exclui redefinição de marca/tema, novos destinos Transações/Assistente, números/dados financeiros, formulários/operações financeiras, mudanças de rotas/autenticação/permissões e recomposição dos formulários de acesso/configurações das irmãs.

## Arquitetura

- Desktop acima de 1200 px: sidebar 240 px, topbar 80 px, workspace flexível e conteúdo limitado a 1440 px conforme `.workspace`/`main`. De 1024 a 1200 px usar sidebar 208 px; até 1023 px reorganizar navegação no topo, sem o drawer lateral do starter como experiência principal. até 767 px empilhar marca e navegação; distribuir somente os destinos existentes, sem fabricar três colunas vazias para páginas futuras.
- Reproduzir espaçamentos da referência: main 32 px na base desktop, 24 px até 1200 px, 24 px vertical/16 px horizontal até 767 px e 48 px a partir 1440 px; conferir padding do topo e alinhamentos na fonte. Evitar padding duplicado entre shell e páginas; ajustes pontuais em `dashboard.tsx` podem remover somente duplicação geométrica.
- Reusar tokens e componentes FinAI/Radix, `<Link>` e funções Wayfinder existentes. Manter nomes funcionais, rótulos acessíveis, semântica de links/botões, foco e método POST da saída. Conservar hooks de teste existentes quando representarem a mesma ação.
- Recolhimento é mecanismo existente: preservar acesso a destinos/menu e capacidade de alternar onde apresentada, sem deixar um cookie antigo forçar geometria incompatível na navegação superior. A geometria de referência deve ser demonstrada no estado expandido; se houver estado recolhido desktop, preservar sua operação e verificar transições sem overflow.
- Alcance: o shell é consumidor de dashboard, perfil, senha, aparência, dois fatores e passkeys. Mudanças globais em primitivas/sidebar/hooks só se necessárias a esse shell; não mudar o limiar global de `use-mobile` sem inspecionar seus demais consumidores. Preferir regras locais do shell quando a alteração global atingir outros controles. Acesso público usa layouts próprios e não deve receber a estrutura autenticada.
- A navegação secundária das configurações continua funcional. A adaptação do menu do usuário no topo móvel é necessária para conservar Settings/Log out quando a referência esconde sidebar-bottom. Isso é adaptação aprovada de preservação de ações, não nova operação.

## Estratégia

Uma fase coesa entrega a estrutura e seu comportamento responsivo. Partir dos componentes atuais e confrontar com as regras explícitas da referência, reaproveitando identidade e operações. Evitar testes que repitam valores CSS; cobrir em browser a navegação/menu/saída e inspecionar visualmente a geometria com capturas do host pai.

Cobertura visual aprovada: estado padrão dos seis destinos autenticados (dashboard, perfil, senha, aparência, 2FA e passkeys), nos nove viewports 360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900, 1920×1080 e nos temas claro/escuro. Adicionalmente, menu do usuário aberto por ponteiro e aberto por teclado com foco em item, no dashboard, nos mesmos nove viewports e dois temas. Não estender automaticamente essa matriz a erros/formulários internos das irmãs. Estados adicionais efetivamente alterados, como recolhido desktop ou hover, precisam de inspeção focada e evidência representativa nas larguras em que existem, sem multiplicar todas as telas por esses estados.

As capturas abaixo usam factories/RefreshDatabase e sessão isolada no ambiente testing, sem credenciais pessoais ou gravação no banco da aplicação. Pest administra seus próprios servidores/browser; o wrapper não encerra processos externos. As imagens e o JSONL de metadados ficam em `RALPH_EVIDENCE_DIR`; arquivos temporários ficam em `tmp/`, ignorado pelo Git, e são removidos. O validador permanece somente leitura e deve abrir as imagens e comparar com a referência, inclusive adaptação escura aprovada. Screenshot produzido ou suíte verde não substitui comparação visual.

## Baseline

Comando completo equivalente ao `composer test`, expandido para PowerShell no Windows. Seleção de PHP 8.5 e atribuição de XDEBUG_MODE são processuais, sem alterar configuração global. Scripts internos POSIX de frontend são interpretados pelo Bun; a atribuição POSIX do script Composer de testes é substituída pelo equivalente abaixo. Nenhum verificador corrige fontes:

```powershell
$env:Path = "$env:USERPROFILE\.config\herd\bin\php85;$env:Path"
$env:XDEBUG_MODE = 'coverage'
& php vendor/bin/pint --parallel --test
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& php vendor/bin/rector --dry-run
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& bun run test:lint
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& php vendor/bin/phpstan
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& bun run test:types
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& php vendor/bin/pest --type-coverage --min=100
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& php vendor/bin/pest --parallel --coverage --exactly=100.0
exit $LASTEXITCODE
```

Pré-requisitos observados em 11/11/2026: PHP 8.5.12 no Herd, Xdebug 3.5 com cobertura; Bun 1.4.4, Node 26.1.0, Python 3.12 e PowerShell no PATH; dependências instaladas; banco de testes definido por `.env.testing`/`phpunit.xml`. Não copiar valores sensíveis nem executar preparação destrutiva do `orca.yaml`. `composer show --direct` confirma Laravel 13.42.0, Inertia Laravel 3.7.0, Wayfinder 0.1.23, Pest 5.3.5, Browser 5.2.0, Pint 1.32.2, Rector 2.8.4, Larastan 3.14.0. `package.json`/instalação: Inertia React 3, React 19, Tailwind 4, Vite+1.5.1, TS 7 e Playwright 1.65.0.

O cache não continha Chromium 1254 exigido por Playwright 1.65.0: o primeiro preflight falhou antes de abrir a página. A preparação `bunx playwright install chromium` disponibilizou os binários dessa versão sem mudar dependências/fontes/configuração. O preflight seguinte passou (1 teste, 11 asserções, 2 imagens protegidas verificadas). Antes da execução, preservar disponibilidade desses binários no host pai.

| Verificador | Composição/configuração | Resultado inicial |
| --- | --- | --- |
| Formatação PHP | Pint `--parallel --test`, `pint.json` | Aprovado |
| Refatoração em conferência | Rector `--dry-run`, `rector.php` | Aprovado, 0 alterações/0 erros |
| Formatação/lint frontend | `bun run test:lint`: `vp fmt --check resources/` e `vp lint` | Aprovado |
| Análise PHP | PHPStan/Larastan, `phpstan.neon` | Aprovado, 0 erros |
| Tipos frontend | `bun run test:types`, `tsc --noEmit` | Aprovado |
| Cobertura de tipos PHP | Pest `--type-coverage --min=100` | Aprovado, 100% (228,97 s) |
| Testes e cobertura PHP | Pest `--parallel --coverage --exactly=100.0`; Browser/Unit/Feature e fonte app no `phpunit.xml` | Aprovado: 180 testes, 631 asserções, 50,13 s, cobertura 100% |

Resultado inicial: suíte completa aprovada com código 0; nenhum arquivo versionado alterado. A prova final do comando renderizado também passou: 6 testes, 480 asserções e 144 capturas protegidas verificadas em 74,04 s, além do build. Essa prova inclui recarregar cada viewport para fechar estados transitórios anteriores e proteger capturas preexistentes. As capturas retratam a base anterior e comprovam viabilidade do mecanismo, não aceite da futura implementação.

A CI `.github/workflows/tests.yml` faz build antes de `composer test`, em Linux/PHP 8.5/PCOV/Node 24; o build não integra o agregado local e será conferência focada. Avisos preexistentes de OPcache incompatível e depreciação `withSetProviders()` do Rector não justificam mudar ini/dependências.

## Riscos

- Mudar limiares só no CSS mantendo hooks do drawer em 768 px pode produzir duas navegações ou menu inacessível em 820 px. Tratar comportamento e composição em conjunto, conferir redimensionamento e foco.
- `overflow-x-clip` pode esconder ações sem corrigir a causa; comprovar acesso e layout real, não apenas ausência de scrollbar. Nomes longos/menu não podem sair da viewport.
- Ajustes no shell atingem todas as configurações; conservar seus campos, mensagens e operações. Não absorver composição interna das irmãs, nem redefinir a base visual de #1016112.
- Não há migração ou nova permissão. Preservar proteção de rotas e sessão; logout deve invalidar acesso ao destino protegido. Limites de ambiente/evidência impedem aprovação visual e não demonstram defeito funcional por si só.

## Fase 1 — Shell e navegação responsiva da área autenticada

### Objetivo

Entregar sidebar/topo, cabeçalho e conteúdo compatíveis com FinAI, com todos os destinos atuais e menu do usuário utilizáveis em desktop, tablet e celular.

### Dependências

Plano aprovado, baseline e preflight disponíveis. Identidade/temas de #1016112 já integrados nesta base; usar essa implementação. Preservar relações publicadas e limites das irmãs.

### Preflight da validação

Reusar suporte existente que recria fixture autenticada e verifica dashboard protegido em claro/escuro, escrevendo e lendo PNGs em `RALPH_EVIDENCE_DIR`. Executado com sucesso nesta inspeção após preparar Chromium 1254. Ralph fornece `RALPH_CAPTURE_MODE=preflight` e diretório privado. O suporte usa PHP 8.5 do Herd e os assets existentes; se faltarem assets/browser/bootstrap, parar antes de desenvolver.

```powershell
python 'docs/harness/features/1016101-adequacao-visual-do-finai/tasks/dev-1016112-adequacao-visual-do-finai-identidade-e-temas-no-painel-atual/capture.py'
exit $LASTEXITCODE
```

### Verificação renderizada

O comando abaixo gera fixture temporária independente, compila assets e captura a matriz aprovada. Preservar o seletor de ação `sidebar-menu-button` ou equivalente visível com o mesmo hook; não criar ações só para a captura. Se houver `RALPH_EVIDENCE_REQUEST`, ler como JSON e executar novamente a cobertura completa aprovada, sem executar texto recebido. Qualquer estado ausente, redirect para login, erro JS, overflow ou imagem ilegível falha. Não alterar código para completar evidências durante esta etapa.

```powershell
@'
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
failure_image = repo / 'tests/Browser/Screenshots/it_captures_the_authenticated_shell.png'
screenshots = failure_image.parent
if screenshots.is_dir() and any(path.is_file() for path in screenshots.rglob('*')):
    raise RuntimeError('Capturas preexistentes: preservar e resolver antes de capturar')
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
            foreach ($route === 'dashboard' ? ['default','menu-open','menu-keyboard'] : ['default'] as $state) {
                if ($state !== 'default') {
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
                if ($state !== 'default') {
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
    try:
        subprocess.run([str(php),'vendor/bin/pest','--configuration',str(config_path),str(test),'--compact'],env=environment,check=True)
    finally:
        if failure_image.is_file():
            failure_image.replace(output / 'capture-failure.png')
entries = [json.loads(line) for line in (output/'captures.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
assert len(entries) == 144 and len({entry['path'] for entry in entries}) == 144, 'Cobertura incompleta'
for entry in entries:
    header = Path(entry['path']).read_bytes()[:24]
    assert header[:8] == b'\x89PNG\r\n\x1a\n' and len(header) == 24, 'PNG inválido'
    width, height = struct.unpack('>II', header[16:24])
    assert width == int(entry['viewport'].split('x')[0]) and height > 0, 'Imagem ilegível ou viewport incorreta'
print(f'CAPTURE_OK: {len(entries)} imagens protegidas e metadados em {output}', flush=True)
'@ | python -
exit $LASTEXITCODE
```

### Mudanças esperadas

Adaptar composição compartilhada e seus breakpoints, dimensões, bordas e espaçamento à referência. Integrar marca/temas existentes, navegação superior nas larguras intermediárias/móveis, indicação de destino ativo e menu do usuário com configurações e saída sempre alcançáveis. Preservar links externos existentes em local acessível. Remover margens inset/duplicação de padding que contradigam a geometria, sem recompor conteúdo interno das irmãs.

Adicionar somente cobertura relevante às decisões alteradas: navegar pelo shell e abrir menu com mouse/teclado em desktop/tablet/celular; visitar Settings e seus destinos e voltar ao Dashboard; conferir indicador ativo, fechar menu/devolver foco e sair, comprovando que destino protegido volta a exigir login. Preservar testes existentes; não testar apenas classes ou larguras declaradas.

### Arquivos prováveis

`resources/js/layouts/app/app-sidebar-layout.tsx`, `components/app-shell.tsx`, `app-content.tsx`, `app-sidebar.tsx`, `app-sidebar-header.tsx`, `nav-main.tsx`, `nav-user.tsx`, `user-menu-content.tsx`, `nav-footer.tsx` e componentes de navegação existentes. `components/ui/sidebar.tsx` e hooks relacionados somente se necessário após analisar consumidores; `resources/css/app.css` apenas regras geométricas locais. `pages/dashboard.tsx` apenas para retirar espaçamento duplicado. `tests/Browser/LayoutTest.php` ou um teste Pest de navegação criado por Artisan; testes HTTP apenas para lacunas de acesso identificadas.

### Limites

Não redefinir tokens/marca, remover destinos existentes, criar páginas financeiras ou simular operações. Não mudar controllers, rotas, métodos HTTP, preferências de aparência ou regras de acesso. Não redesenhar formulários de perfil/senha/2FA/passkeys. Não mudar dependências. Suporte de captura opera apenas no ambiente de testes, sem rota pública ou credencial pessoal.

### Estratégia

Conferir as versões instaladas e documentação antes de APIs novas. Reusar identidade e menu Radix, preservando as ações Wayfinder/Inertia e limpeza de navegação. Revisar interações de largura/estado/cookie e consumidores antes de mudar primitives/hooks globais. Para testes, seguir `testing-best-practices`, usar factory `withoutTwoFactor()`, sessão de confirmação quando requerida e browser para comportamento JavaScript. Rodar cada teste afetado após sua edição e build após assets.

### Aceite

- Desktop expandido reproduz sidebar 240 px, header 80 px, conteúdo e espaçamentos aplicáveis; intervalo 1024–1200 usa adaptação 208 px. até 1023 apresenta navegação superior; até 767 reorganiza marca/links conforme design, mantendo as ações atuais.
- Dashboard, configurações, links externos, menu do usuário e saída permanecem acessíveis, com estado ativo quando aplicável. Nenhuma página ou informação financeira é antecipada. Conteúdo e ações equivalentes em claro/escuro, identidade herdada de #1016112 e preferência de aparência preservada.
- Nas seis superfícies e matriz visual especificadas em Estratégia, imagens atuais legíveis e comparação com `.app`/`.sidebar`/`.topbar`/`main` e media queries da fonte; conferir organização, alinhamento, legibilidade e ausência de rolagem horizontal real. Para o dashboard, também comparar menu aberto por ponteiro e por teclado/foco na mesma matriz; demais estados efetivamente alterados têm inspeção representativa conforme Estratégia. Não exigir recomposição visual interna das irmãs.
- Mouse/teclado alcançam destinos e menu; foco visível, seleção, fechamento/Escape e retorno de foco funcionam. Redimensionar entre navegação superior/lateral não perde operações. Se estado recolhido existir, sua operação desktop e recuperação ao expandir continuam acessíveis.
- Visitante não acessa destinos protegidos; usuário não verificado conserva restrições atuais; saída encerra sessão e nova tentativa de acesso exige login. Não alterar fixtures para esconder regressões de acesso.
- Validação visual deve ser registrada como verificada após abrir imagens. Ambiente ou captura incompleta mantém fase bloqueada; funcional verde não é aceite visual.

### Verificação focada

`bun run build` com PHP 8.5 no PATH e comparação renderizada aprovada acima. Executar teste de navegação novo/alterado, `tests/Browser/LayoutTest.php` e `tests/Browser/AppearanceTest.php` conforme alcance. LayoutTest já cobre renderização de perfil/aparência, passkeys com confirmação e ações/toast/exclusão, mas não navegação responsiva/menu/teclado/logout via UI: cobrir somente essa lacuna. AppearanceTest cobre seleção/persistência e reação a preferência de sistema; preservá-lo.

`tests/Feature/Controllers/SessionControllerTest.php` comprova saída POST com redirect e sessão guest; `UserPasskeyControllerTest.php` cobre confirmação de senha e redirecionamento do não verificado. Testes existentes não demonstram toda a matriz de visitantes de dashboard/configurações; acrescentar dataset HTTP enxuto apenas se necessário à preservação, sem duplicar testes já existentes. Conferir profile auth versus demais auth+verified e manter rotas intactas. Rodar suíte completa do Baseline no Gate 3; se houver PHP alterado, cumprir Pint antes de finalizar. Nenhuma nova verificação é dispensada pelo resultado inicial.


