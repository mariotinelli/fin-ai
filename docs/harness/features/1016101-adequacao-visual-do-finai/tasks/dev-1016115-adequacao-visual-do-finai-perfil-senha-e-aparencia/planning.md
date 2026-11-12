# DEV #1016115 — Perfil, senha e aparência

## Identidade e fontes

Filha #1016115: [DEV] [WEB] [USUARIO] Adequação visual do FinAI - Perfil, senha e aparência, conforme `task.md` neste diretório. Pai: `docs/harness/features/1016101-adequacao-visual-do-finai/feature.md`, R1–R3, R5, CA1–CA8 e V-Conta aplicáveis a estas superfícies.

Sequenciamento e dependências: `docs/harness/scopes/2026-11-11-finai-mvp/scope.md`, `slices/publication.md` e `slices/revision-application.md` da Feature. Preservar numeração e relações publicadas; esta filha bloqueia QA #1016117. Identidade #1016112 e estrutura original #1016113 têm implementação nesta base. A revisão de navegação é de #1016204; tradução integral e URLs são de #1016231/#1016232. Não incorporar essas entregas nem antecipar a Feature Acesso à conta pessoal.

Design-input-001 é a referência principal: tokens, `h1`, `.panel`, `.btn`, campos, mensagens, `dialog` e `:focus-visible`. Não há desenho específico de configurações: a adaptação aprovada preserva campos e operações e aplica a linguagem comum. Design-input-002 é contexto para integração com o shell; suas mudanças compartilhadas pertencem à tarefa complementar.

Instruções aplicáveis: `AGENTS.md`, `.ai/rules/index.md`, `.ai/rules/js.md`, `.ai/rules/css.md`; skills `inertia-react-development`, `tailwindcss-development`, `wayfinder-development`, `fortify-development` e `testing-best-practices`. Reconsultar documentação versionada antes de introduzir APIs. Boost/search-docs não estava disponível na inspeção; os contratos usados já existem no código instalado.

## Referências visuais

- `docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md`
- `docs/harness/features/1016101-adequacao-visual-do-finai/sources/design-input-002.md`

## Objetivo

Apresentar perfil, alteração de senha, aparência e confirmação de exclusão com identidade FinAI, mantendo navegação, validações, feedback, preferência de tema e efeitos atuais.

## Estado atual

- `resources/css/app.css` já implementa a paleta FinAI clara/escura, corpo system-ui, Georgia, controles de 8px, painéis de 16px e foco azul. Marca, shell e primitivas já existem; não refazer a fundação.
- `pages/user-profile/edit.tsx`, `pages/user-password/edit.tsx` e `pages/appearance/update.tsx` usam `AppLayout` e `SettingsLayout`, mas sua composição mantém títulos pequenos, seções sem painéis e hierarquia do starter. `components/delete-user.tsx` contém alerta e diálogo reutilizando Radix/PasswordInput, ainda sem composição própria FinAI. `appearance-tabs.tsx` já usa tokens, botões de 44px e seleção acessível.
- `layouts/settings/layout.tsx` também serve 2FA e passkeys. `Heading`, primitivas, `PasswordInput` e tema possuem consumidores externos. `DeleteUser` é consumido apenas no perfil; `AppearanceTabs` apenas na aparência. Um ajuste global de layout/títulos alteraria as irmãs.
- Perfil mantém nome/e-mail, erros, `processing`, toast de sucesso, aviso de e-mail não verificado e reenvio/status. Senha mantém senha atual/nova/confirmação, regras recebidas do servidor, limpeza e foco nos erros e toast. Exclusão mantém senha, foco no erro, cancelamento que limpa o formulário e redirecionamento à inicial no sucesso.
- `routes/web.php`: perfil exige `auth`; senha/aparência/exclusão exigem `auth,verified`; atualização de senha mantém throttle. `UserProfileController`, `UserPasswordController` e `UserController` delegam a Actions e já fornecem feedback. `UserEmailVerificationNotificationController::store` envia notificação e retorna à origem com status; não criar nova exigência de verificação.
- `hooks/use-appearance.tsx` conserva escolha em localStorage/cookie, inicializa o tema e acompanha media query quando sistema está selecionado. `tests/Browser/AppearanceTest.php` já comprova claro/escuro/sistema, recarga, navegação e mudança real do dispositivo.
- `tests/Browser/LayoutTest.php` cobre navegação perfil→aparência, toast de atualização e exclusão válida com remoção no banco. Os testes HTTP dos controllers cobrem perfil válido/inválido, unicidade e reset de verificação com notificação quando e-mail muda, senha atual incorreta e alteração válida, exclusão com senha ausente/incorreta e recusa a não verificado. Faltam provas renderizadas de cancelamento/fechamento/foco/erros de diálogo e integração visual de senha/reenvio.

## Escopo

Inclui composição localizada das três páginas e do diálogo/alerta, integração com tokens e componentes existentes, estados atuais, navegação de configurações e suporte de captura isolada. Exclui tradução e URLs, regras/backend de conta, novos feedbacks, mecanismos de tema, shell revisado, 2FA/passkeys, dados financeiros, novas dependências e configuração global.

## Arquitetura

Aplicar Tailwind nos componentes consumidores: painéis com fundo de superfície, borda e raio 16px; controles 8px; título principal Georgia responsivo 32–40px; subtítulos e descrições com hierarquia e espaços 8/16/24/32px da referência. Manter verde principal #145C46, erro #A12B36 e positivo #146345 pelos tokens existentes, usando a variante escura fornecida. Diálogo reutiliza a primitiva atual e sua semântica/modalidade; adequar conteúdo e espaçamento localmente, sem alterar `ui/dialog.tsx` por conveniência.

Criar uma variante opt-in de composição FinAI no layout de configurações, aplicada explicitamente somente às três páginas desta filha; preservar a aparência padrão das consumidoras 2FA/passkeys. Alternativamente, extrair um wrapper localizado reutilizando a navegação existente sem duplicar destinos. Não trocar o padrão global ou alterar `Heading` para todo o aplicativo. A navegação mantém os cinco destinos atuais, indicação ativa, labels e acesso por teclado. Testar as consumidoras externas para demonstrar preservação.

Conservar `<Form>`, Wayfinder, nomes/autocomplete dos campos, refs, reset, erros, processamento, reenvio e status. Não trocar transportes nem criar URLs hardcoded. `DeleteUser` mantém confirmação por senha, DialogClose, limpeza e foco; não acrescentar etapas de confirmação. Aparência mantém os três valores técnicos e o hook atual.

## Estratégia

Uma fase coesa adapta as três páginas, alerta e diálogo usando a base pronta; completa apenas lacunas de browser e suporte de captura. Não duplicar regras HTTP em toda a matriz de navegador. Capturas atuais e preflight provam disponibilidade, nunca aceite da implementação futura.

Cobertura renderizada: estados padrão das três páginas e diálogo aberto nos nove viewports 360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080, em claro e escuro. Estados adicionais aplicáveis serão capturados em 360×800 e 1366×768, em ambos os temas, para demonstrar composição estreita/ampla sem multiplicar cada transição por toda largura. Os estados de processamento são do Form real, controlando temporariamente o transporte no contexto isolado, sem trocar classes/DOM para simular aparência. Comparação independente abre as imagens e confronta design e adaptações; resultado incompleto/inacessível bloqueia aceite visual.

Suporte de captura desta filha será implementado em Desenvolvimento, reutilizando Python/Pest/RefreshDatabase das irmãs. Recriar usuário factory `withoutTwoFactor`, verificado ou não conforme cenário, autenticar independentemente e verificar rota protegida/conteúdo/ausência de erros JS. Usar `.env.testing` e configuração XML derivada, SSR desligado, hot file isolado; nenhum dado pessoal ou credencial real. Não iniciar `artisan serve`; o runner de browser administra seus próprios processos. Encerrar processos próprios e remover apenas temporários próprios. Metadados e imagens duráveis vão a `RALPH_EVIDENCE_DIR`.

## Baseline

Comando completo equivalente a `composer test`, expandido para PowerShell para preservar todos os verificadores e limites no Windows; scripts internos usam atribuições POSIX. Build prepara assets e Wayfinder. PHP 8.5 é selecionado apenas no processo; configurações derivadas preservam regras e redirecionam caches ao diretório privado. PHPStan explicita `analyse` para reconhecer caminhos Windows.
```powershell
$env:Path = "$env:USERPROFILE\.config\herd\bin\php85;$env:Path"
$env:XDEBUG_MODE = 'coverage'
& bun run build
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
$utf8 = [System.Text.UTF8Encoding]::new($false)
$rectorConfiguration = Join-Path $env:RALPH_ARTIFACTS_DIR 'rector.php'
$rectorSource = (Join-Path (Get-Location).Path 'rector.php').Replace('\', '/').Replace("'", "\'")
[System.IO.File]::WriteAllText($rectorConfiguration, "<?php return (require '$rectorSource')->withCache(cacheDirectory: getenv('RALPH_ARTIFACTS_DIR').'/rector-cache');", $utf8)
$phpstanConfiguration = Join-Path $env:RALPH_ARTIFACTS_DIR 'phpstan.neon'
$phpstanSource = (Join-Path (Get-Location).Path 'phpstan.neon').Replace('\', '/').Replace("'", "''")
$phpstanCache = (Join-Path $env:RALPH_ARTIFACTS_DIR 'phpstan-cache').Replace('\', '/').Replace("'", "''")
[System.IO.File]::WriteAllText($phpstanConfiguration, "includes:`n    - '$phpstanSource'`nparameters:`n    tmpDir: '$phpstanCache'`n", $utf8)
& php vendor/bin/pint --parallel --test --cache-file "$env:RALPH_ARTIFACTS_DIR/pint.cache"
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& php vendor/bin/rector --dry-run --config $rectorConfiguration
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& bun run test:lint
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& php vendor/bin/phpstan analyse --configuration $phpstanConfiguration
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& bun run test:types
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& php vendor/bin/pest --type-coverage --min=100 "--type-coverage-json=$env:RALPH_ARTIFACTS_DIR/type-coverage.json"
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& php vendor/bin/pest --parallel --coverage --exactly=100.0 --cache-directory "$env:RALPH_ARTIFACTS_DIR/pest-cache" --log-junit "$env:RALPH_ARTIFACTS_DIR/suite.xml"
exit $LASTEXITCODE
```

Pré-requisitos conferidos em 12/11/2026: PHP 8.5.12/Herd, Xdebug 3.5.0, Bun 1.4.4, Node 26.1.0, Python 3.12.3, dependências instaladas e PostgreSQL de testes definido por `.env.testing`/`phpunit.xml`. `composer show --direct`: Laravel 13.42.0, Inertia Laravel 3.7.0, Fortify 1.42.0, Wayfinder 0.1.23, Pest 5.3.5, Browser 5.2.0, Pint 1.32.2, Rector 2.8.4, Larastan 3.14.0. Frontend: React 19, Inertia 3, Tailwind 4, Playwright 1.65.0. CI (`.github/workflows/tests.yml`) faz build e `composer test` em Linux/PHP 8.5/PCOV; o comando local mantém a composição e cobertura exigidas.

| Verificador | Composição/configuração | Resultado inicial observado em 12/11/2026 |
| --- | --- | --- |
| Build e Wayfinder | `bun run build`, `vite.config.ts` | Aprovado |
| Formatação PHP | Pint `--parallel --test`, cache privado | Aprovado |
| Refatoração em conferência | Rector `--dry-run`, regras originais/cache privado | Aprovado, 0 alterações e 0 erros |
| Formatação/lint frontend | `bun run test:lint`: fmt check e lint sem fix | Aprovado |
| Análise PHP | PHPStan/Larastan `analyse`, nível max | Aprovado, 0 erros |
| Tipos frontend | `bun run test:types`, tsc `--noEmit` | Aprovado |
| Cobertura de tipos PHP | Pest `--type-coverage --min=100` | Aprovado, 100%, 279,40s |
| Testes e cobertura | Pest Browser/Unit/Feature paralelo `--coverage --exactly=100.0` | Aprovado: 202 testes, 834 asserções, 67,859s, cobertura 100% |

Suíte completa terminou com código 0, sem modificar fontes versionadas. Depreciação preexistente de `withSetProviders()` no Rector não altera o escopo. Artefatos de planejamento ficaram fora das fontes em diretório temporário privado; o executor recria os próprios destinos duráveis por execução.

Preflight autenticado executado com suporte já instalado e assets produzidos pelo build acima: 1 teste, 11 asserções, 5,139s, código 0 e dois PNGs claro/escuro do dashboard protegido. PNG claro aberto e legível. Captura atual de perfil não verificado usando fixture existente de #1016112: 1 teste, 90 asserções, 5,552s, código 0, 18 imagens nos nove viewports/dois temas; abertas desktop claro 1366×768 e mobile escuro 360×800. Confirmam marca/paleta já fornecidas e a composição ainda sem painéis de perfil e hierarquia própria, com acesso a aviso e ações. Senha/aparência/diálogo foram inspecionados no código e nos testes existentes; não se declara comparação visual atual dessas superfícies. A matriz de 116 imagens pós-implementação exige o novo suporte da fase e ainda não foi executada.

## Riscos

Layout, títulos e primitivas compartilhados alcançam 2FA/passkeys e acesso; manter adesão explícita/localizada evita regressão fora da filha. Textos permanecem como estão até a tarefa própria de tradução. Não esconder overflow com clipping para aprovar capturas: conteúdo e foco precisam continuar alcançáveis em 360px.

Exclusão e atualização de senha são operações sensíveis: testes só no banco de testes, preservando senha atual, resets, redirects, autenticação e verificação atuais. Formulários têm senhas com IDs iguais em contextos diferentes; o diálogo deve manter seu foco próprio e os seletores do teste devem respeitar o modal. Nenhuma migração ou mudança de dependências prevista.

Capturas transitórias exigem estado real e assertivas; uma imagem padrão com nome de erro/processamento não comprova cobertura. Obstáculo de runtime/captura não comprova defeito do produto e impede a comparação enquanto não resolvido. A revisão do shell e a tradução permanecem nas tarefas donas, sem ampliar esta fase.

## Fase 1 — Configurações pessoais com identidade FinAI

### Objetivo

Entregar composição FinAI localizada em perfil, senha, aparência e exclusão, preservando todos os resultados e controles atuais.

### Dependências

Plano revisado/preparado em Git; baseline e preflight disponíveis. Integrar identidade #1016112 e estrutura original #1016113 já presentes. Não criar bloqueio de início ausente na tarefa; não implementar #1016204, #1016231/#1016232 ou futura Feature Acesso à conta pessoal. A aceitação conjunta da revisão do shell pertence à sua própria entrega e QA.

### Mudanças esperadas

Adequar títulos, superfícies, espaçamento, grupos de campos/ações, avisos e diálogo ao design usando componentes atuais. Aplicar variante localizada do layout somente às três páginas; manter navegação e estados ativos. Conservar Form/Wayfinder, erros, resets, foco, processamento, toast, reenvio e preferência de tema. Completar captura isolada e testes de browser apenas nas lacunas de interação percebida.

### Arquivos prováveis

`resources/js/pages/user-profile/edit.tsx`, `resources/js/pages/user-password/edit.tsx`, `resources/js/pages/appearance/update.tsx`, `resources/js/components/delete-user.tsx`, `resources/js/layouts/settings/layout.tsx` ou wrapper localizado em `layouts/settings/`. `appearance-tabs.tsx` somente se a composição exigir, sem mudar hook/valores. `tests/Browser/LayoutTest.php`, `AppearanceTest.php` e novo teste Pest de configurações se necessário, criado com Artisan. `capture.py` e `capture-fixture.php` ao lado deste plano. Não há necessidade prevista de mudar controllers, Actions, rotas, app.css ou primitivas globais.

### Limites

Sem novos dados, mensagens funcionais, campos, regras, permissões, confirmação, mecanismos de tema, operações ou tradução. Conservar conteúdo funcional e destinos atuais, inclusive acesso a 2FA/passkeys. Não redesenhar irmãs pela modificação implícita do layout. Fixtures não alteram rotas públicas nem usam dados reais.

### Estratégia

Conferir consumidores e documentação compatível; compor usando tokens, marca e primitivas prontos. Manter estilos locais em Tailwind; wrappers não alteram o transporte. Reusar cobertura HTTP; acrescentar browser para confirmar que formas/modais recompostos mantêm interação e foco. Cada browser chama `assertNoJavaScriptErrors()`.

Implementar captura com usuário e dados independentes por cenário, `RefreshDatabase`, bootstrap real e SSR/hot file de testes isolados. Para erros, executar solicitação inválida e esperar a mensagem; para sucesso, executar operação válida e esperar feedback; para processamento, reter transporte depois de `Form` marcar processing, capturar desabilitado e liberar/encerrar com segurança. Não alterar DOM/classes para fabricar estados. Reenvio usa usuário não verificado e preserva retorno ao perfil/status. Avisos não permitem contornar `verified` em senha/exclusão.

Conservar originais e gerar montagens identificadas por superfície/tema/estado para facilitar comparação, mantendo resolução legível e acesso aos PNGs individuais; não usar miniaturas ilegíveis como aceite. A fonte CSS normalizada é a referência de componentes sem desenho próprio; o validador pode comparar seus tokens/composição sem executar o protótipo. Salvar PNGs legíveis e metadados `path`, `reference`, `screen`, `state`, `viewport`, `theme`. Validar que a rota protegida/conteúdo correto renderizou, dimensões e conjunto esperado; retorno ao login falha. Quando `RALPH_EVIDENCE_REQUEST` existir, ler JSON UTF-8 como dados e recriar a matriz aprovada inteira ou os estados pedidos, preservando evidências anteriores. Não executar texto do pedido. Temporários em `tmp` são próprios; evidências persistentes usam `RALPH_EVIDENCE_DIR`, diagnósticos/caches/JUnit usam `RALPH_ARTIFACTS_DIR`; encerrar apenas processos próprios, inclusive em falhas/interrupções.

### Aceite

- As três páginas e o alerta/diálogo de exclusão exibem paleta, títulos Georgia, corpo system-ui, painéis/controles, bordas, foco e estados compatíveis com design-input-001 e adaptações de Arquitetura. Variante escura usa a identidade FinAI existente. Nenhum formulário, operação ou destino removido.
- Matriz visual principal: perfil padrão, senha padrão, aparência padrão e diálogo de exclusão aberto nos nove viewports e dois temas de Estratégia (72 imagens). Estados adicionais em 360×800 e 1366×768, claro/escuro: perfil com erro, sucesso, e-mail não verificado, reenvio confirmado e processamento; senha com erro de senha atual/confirmação, sucesso e processamento; diálogo com senha incorreta e processamento (10 estados, 40 imagens). A matriz principal verifica geometria/responsividade em todas as larguras exigidas; os adicionais exercitam mensagens e transições nas composições estreita/ampla. O estado de aparência padrão usa a opção explícita correspondente ao tema. Exibir foco real no estado padrão de cada superfície e diálogo, sem multiplicar por todo elemento focável.
- Evidências adicionais em 1366×768: aparência com sistema selecionado e dispositivo claro/escuro (2 imagens), hover na ação de salvar perfil em claro/escuro (2 imagens), total de 116. Não exigir matriz completa para cada regra de validação, elemento focável ou estado interno de 2FA/passkeys. Cancelamento/fechamento e exclusão válida são comprovados por interação/testes, sem criar uma tela extra na matriz visual.
- Em toda matriz, página sem rolagem horizontal, mensagens e ações legíveis/alcançáveis por teclado/rolagem vertical, foco visível sem clipping e conteúdo/ações equivalentes entre temas. Dialog pode rolar verticalmente mantendo confirmação e cancelamento acessíveis. Navegação conserva perfil/senha/aparência/2FA/passkeys e destino ativo; consumidoras irmãs conservam sua composição padrão.
- Perfil válido persiste nome/e-mail e mostra feedback atual; inválido preserva dados e mostra erro. Alteração de e-mail conserva reset de verificação; aviso e reenvio continuam acessíveis ao não verificado, retornando ao perfil com status. Não acrescentar regra de bloqueio do perfil.
- Senha válida altera hash e mantém feedback/reset; senha atual errada e confirmação incompatível mostram erros e foco atuais, sem modificar a senha. Preservar as restrições e throttle existentes.
- Exclusão só acontece após confirmação e senha correta; cancelar, fechar por botão ou Escape e erro de senha preservam conta/sessão. Diálogo mantém foco contido, retorna foco ao disparador e permite reabrir conforme comportamento atual. Sucesso remove o usuário e retorna à inicial como visitante; posterior acesso a destino protegido exige login.
- Claro, escuro e sistema continuam selecionáveis, conservados em recarga/navegação; mudança do dispositivo altera somente sistema. Reusar prova existente em `AppearanceTest.php`, sem modificar o hook por conveniência.
- Validação independente abre e compara as imagens exigidas com a referência e adaptações. Capturas ausentes/inacessíveis ou comparação pendente bloqueiam aceite visual, mesmo com testes verdes. Shell revisado e traduções não são critérios de aprovação desta fase.

### Verificação focada

- `UserProfileControllerTest.php`: preservar atualização/persistência, obrigatórios/formato/unicidade, e-mail próprio e reset de verificação. `UserPasswordControllerTest.php`: preservar alteração/hash/feedback, senha atual ausente/incorreta, nova senha obrigatória e recusa ao não verificado. Cobertura HTTP não demonstra foco/modal; não duplicar a matriz inteira no browser.
- `UserControllerTest.php`: exclusão válida com guest/remoção e erros ausente/incorreta, não verificado preservado. `UserEmailVerificationNotificationControllerTest.php`: notificação e status, não envio a já verificado. `ShellAccessTest.php`: guest recusado, perfil permitido a não verificado e senha/aparência recusadas. Completar HTTP apenas se faltar proteção após exclusão ou confirmação incompatível relevante; sem novas políticas.
- `LayoutTest.php`: preservar navegação perfil→aparência, toast e exclusão válida; `AppearanceTest.php` já cobre os três modos, recarga, mudança real de media query e navegação. Completar browser para senha válida/inválida e feedback/foco, perfil inválido/reenvio e diálogo com erro, cancelamento/botão/Escape, foco e acesso protegido após exclusão. Conferir 2FA/passkeys existentes para que opt-in visual não altere essas consumidoras.
- Não escrever testes que comparem strings de classes ou copiem implementação. Rodar cada teste modificado e os comandos abaixo. Se houver PHP modificado, aplicar `vendor/bin/pint --dirty --format agent` em Desenvolvimento, revisar diff e manter verificadores em modo conferência.

### Inventário das saídas de verificação

Aplicável a preflight, host, renderizada e Gate 3, inclusive erro/interrupção. Conferidos scripts/configuração do projeto e `Pest/Browser/Support/Screenshot.php`, `Trace.php`, `BrowserExpectationFailedException.php`, plugins de cache/type-coverage instalados. Pint usa cache privado; Rector/PHPStan recebem configuração derivada para cache privado, preservando regras. Frontend fmt/lint são check-only e tsc não emite. Pest envia cache/JUnit/type-coverage JSON a `RALPH_ARTIFACTS_DIR`; cobertura de código é exibida no log, sem HTML. Caches internos das dependências permanecem ignorados.

Build/Wayfinder geram `public/build`, `resources/js/actions`, `resources/js/routes` e `resources/js/wayfinder`, inclusive parciais em falha. Browser gera screenshots de falha em `tests/Browser/Screenshots`; traces em `tests/Browser/Traces` se habilitados (não estão habilitados nesta base). Não há gravação de vídeo configurada. Captura usa prefixo relativo permitido pelo suporte instalado para gravar imagens diretamente no diretório privado de evidências; metadados/PNG ficam lá e são validados. Cache/fixtures/configuração temporária próprios ficam em `tmp`; logs Laravel em `storage/logs`. Fontes rastreadas/baselines continuam protegidas em qualquer raiz; não classificar arquivos novos fora delas por extensão. O executor preserva saídas e mapeia os caminhos privados antes de avaliar segurança das fontes, mesmo quando a assertiva falha.

### Artefatos de verificação

- `public/build`
- `resources/js/actions`
- `resources/js/routes`
- `resources/js/wayfinder`
- `tests/Browser/Screenshots`
- `tests/Browser/Traces`
- `storage/logs`
- `tmp`

### Preflight da validação

Usa suporte existente de #1016112, bootstrap/banco testing e dashboard autenticado em claro/escuro, sem depender do novo suporte desta filha. Relatório do pai estabelece disponibilidade; não repetir dentro do agente. Não demonstra aceite visual pós-implementação.

```powershell
$env:Path = "$env:USERPROFILE\.config\herd\bin\php85;$env:Path"
& bun run build
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
New-Item -ItemType Directory -Force -Path 'tmp' -ErrorAction Stop | Out-Null
python 'docs/harness/features/1016101-adequacao-visual-do-finai/tasks/dev-1016112-adequacao-visual-do-finai-identidade-e-temas-no-painel-atual/capture.py'
exit $LASTEXITCODE
```

### Verificação no host

Conferência frontend e provas focadas no banco de testes. Se apenas a execução dos comandos faltar por sandbox, retornar `ready-for-host-checks` e `pending_checks: ["host", "rendered"]`; fixture incompleta não constitui handoff pronto. O diretório Browser inclui novos testes sem presumir nome de arquivo.

```powershell
$env:Path = "$env:USERPROFILE\.config\herd\bin\php85;$env:Path"
$env:APP_ENV = 'testing'
$env:PLAYWRIGHT_BROWSERS_PATH = "$env:LOCALAPPDATA\ms-playwright"
& bun run build
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& bun run test:lint
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& bun run test:types
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& php vendor/bin/pest --compact --cache-directory "$env:RALPH_ARTIFACTS_DIR/pest-cache" --log-junit "$env:RALPH_ARTIFACTS_DIR/focused.xml" tests/Browser tests/Feature/Controllers/UserProfileControllerTest.php tests/Feature/Controllers/UserPasswordControllerTest.php tests/Feature/Controllers/UserControllerTest.php tests/Feature/Controllers/UserEmailVerificationNotificationControllerTest.php tests/Feature/ShellAccessTest.php
exit $LASTEXITCODE
```

### Verificação renderizada

Implementar o suporte abaixo durante Desenvolvimento conforme Estratégia/Aceite. Recriar as quatro superfícies padrão nos nove viewports/dois temas e os dez estados adicionais nos dois viewports/dois temas, mais sistema/hover representativos, e confirmar os 116 PNGs/metadados. Se pedido suplementar existir, completar os estados aprovados sem editar comportamento do produto; o validador só lê as evidências. Suporte ausente ou matriz incompleta após handoff interrompe, sem reduzir critérios.

```powershell
$env:Path = "$env:USERPROFILE\.config\herd\bin\php85;$env:Path"
$env:APP_ENV = 'testing'
$env:PLAYWRIGHT_BROWSERS_PATH = "$env:LOCALAPPDATA\ms-playwright"
& bun run build
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
New-Item -ItemType Directory -Force -Path 'tmp' -ErrorAction Stop | Out-Null
python 'docs/harness/features/1016101-adequacao-visual-do-finai/tasks/dev-1016115-adequacao-visual-do-finai-perfil-senha-e-aparencia/capture.py'
exit $LASTEXITCODE
```
