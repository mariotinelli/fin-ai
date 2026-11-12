# DEV #1016114 — Página inicial e jornadas de acesso

## Identidade e fontes

- Filha #1016114: `[DEV] [WEB] [USUARIO] Adequação visual do FinAI - Página inicial e jornadas de acesso`, em `task.md` neste diretório. Pai: `docs/harness/features/1016101-adequacao-visual-do-finai/feature.md`; aplicar R1, R2, R3, R5, R6, CA1, CA2, CA5, CA6, CA7 e CA8 às superfícies desta filha.
- Sequenciamento: `docs/harness/scopes/2026-11-11-finai-mvp/scope.md` e `docs/harness/features/1016101-adequacao-visual-do-finai/slices/publication.md`. A fundação visual precede as Features de negócio; esta filha bloqueia QA #1016117. Identidade #1016112 e estrutura #1016113 já possuem implementação nesta base. O complemento #1016204 é dono da revisão do shell autenticado; não incorporá-lo aqui nem alterar relações ou numeração.
- Fonte principal: design-input-001, especialmente `.brand`, `.brand-mark`, `.brand-ai`, `h1`, `.panel`, `.btn`, `label`, `input`, `.notice`, `.error` e `:focus-visible` do `index.html`. Não há desenho específico de página inicial ou autenticação; a adaptação aprovada aplica essa linguagem preservando campos, ações, mensagens e destinos existentes.
- design-input-002 é leitura de contexto: altera o shell autenticado, não cria uma composição pública ou formulário de acesso. Preservar a integração e a responsabilidade de #1016204.
- Instruções: `AGENTS.md`, `.ai/rules/index.md`, `.ai/rules/js.md`, `.ai/rules/css.md` e skills `inertia-react-development`, `tailwindcss-development`, `wayfinder-development`, `fortify-development` e `testing-best-practices`. Componentes usam utilitários Tailwind locais; `app.css` fica reservado a tokens e estilos base compartilhados.

## Referências visuais

- `docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md`
- `docs/harness/features/1016101-adequacao-visual-do-finai/sources/design-input-002.md`

## Objetivo

Apresentar a identidade FinAI na página pública, cadastro, login, solicitação de recuperação, redefinição de senha e verificação de e-mail, conservando os fluxos e restrições atuais, as alternativas de autenticação e os temas claro, escuro e sistema.

## Estado atual

- `resources/css/app.css` já fornece fundo claro #F5F7F8, superfícies brancas, texto #172622, secundário #52615C, verde #145C46, positivo #146345, erro #A12B36, borda #D6DFDB e destaque #E4F0E9, corpo system-ui, serif Georgia, controles 8px e painéis 16px. A variante escura FinAI também existe. `components/app-logo.tsx` e `app-logo-icon.tsx` implementam marca reutilizável; não refazer essa base.
- `pages/welcome.tsx` ainda contém a composição Laravel do starter, cores literais claras/escuras, SVGs de Laravel, fonte Instrument Sans externa e links para documentação, Laracasts e deploy. A navegação distingue visitante (login/cadastro) de autenticado (dashboard). Captura real em 1366×768, aberta nesta preparação, confirmou a arte Laravel vermelha e a composição genérica.
- `layouts/auth-layout.tsx` usa `auth/auth-simple-layout.tsx`: conteúdo centrado com largura `max-w-sm`, ícone isolado, título `text-xl font-medium` e sem painel da referência. Login renderizado e aberto em 1366×768 confirmou paleta FinAI herdada, entrada por passkey e ausência do nome completo da marca/título Georgia.
- As cinco páginas de acesso estão em `pages/session/create.tsx`, `user/create.tsx`, `user-email-reset-notification/create.tsx`, `user-password/create.tsx` e `user-email-verification-notification/create.tsx`. Usam `<Form>`, estados `errors`/`processing`, primitivas compartilhadas e funções Wayfinder. Cadastro tem nome, e-mail, senha e confirmação; login tem e-mail, senha, lembrar e passkey; redefinição recebe token e e-mail somente leitura. Conservar esses contratos.
- `AuthLayout` também serve `user-password-confirmation/create.tsx` e `user-two-factor-authentication-challenge/show.tsx`, pertencentes a #1016116. `PasskeyVerify`, `PasswordInput`, `Button`, `Input`, `InputError` e `TextLink` têm consumidores fora desta filha; mudanças globais atingiriam segurança/configurações.
- `routes/web.php` registra cadastro/login/recuperação/redefinição com `guest`; verificação/reenvio/saída com `auth`. `SessionController` entrega alternativas disponíveis, autentica, conserva lembrar/intended e encaminha a 2FA quando habilitado. Recuperação devolve a mesma mensagem genérica para conta existente ou inexistente; redefinição mantém token, validações e retorno para login com status; verificação mantém reenvio, saída e redirecionamento de já verificados. Fortify fornece confirmação de senha e desafio 2FA, não substitui esses controllers locais.
- `tests/Browser/LayoutTest.php` já cobre login → cadastro com passkey presente e redefinição real com token, resultado no banco e retorno ao login. `WelcomeTest.php` verifica conteúdo atual Laravel. Os testes HTTP dos seis controllers já cobrem sucesso, erros, sessão e restrições; a lacuna está na composição renderizada, apresentação de estados e navegação pública completa após a adaptação.

## Escopo

Inclui apenas as seis superfícies, marca visível, títulos, painéis, formulários, espaçamentos, links e estados atuais, integração visual da entrada por passkey e suporte de captura isolada para aceite. Mantém conteúdo funcional, textos funcionais, campos, mensagens, métodos HTTP, rotas, políticas e resultados.

Exclui mudanças de autenticação, backend, validação ou tradução funcional; estados próprios de passkeys/2FA/confirmação de senha; formulários de perfil/configurações; revisão do shell autenticado; novos destinos ou dados financeiros, promessas de funcionalidades futuras, armazenamento local ou IA simulada. Não alterar dependências ou configuração global.

## Arquitetura

- Reusar tokens/primitivas/marca existentes. Adaptar a marca pública à referência `.brand` (nome finai e símbolo), títulos de destaque Georgia com hierarquia 32–40px responsiva, corpo system-ui, superfícies com borda e raio 16px, controles com raio 8px e ações principais com altura mínima 44px. Usar espaços da referência (8/16/24/32/48px) proporcionais à largura, foco visível e estados de erro/sucesso. Essas são adaptações das telas sem desenho próprio; não copiar dashboard financeiro para a inicial.
- Preservar o conteúdo funcional da inicial e todos os links/destinos atuais, inclusive documentação, Laracasts e deploy, com apresentação subordinada à marca FinAI. Substituir arte/identidade genérica Laravel e cores literais pela identidade fornecida; não inventar marketing, dados ou operações. Se o texto atual menciona Laravel como conteúdo informativo, essa menção não é uma nova marca do produto nem precisa ser removida para trocar a identidade visual.
- Criar uma composição de acesso reutilizável em `resources/js/layouts/auth/` e aplicá-la explicitamente às cinco páginas desta entrega. Manter o layout atual para confirmação de senha/desafio 2FA; não trocar o template global de `AuthLayout` ou mudar primitivas por conveniência. Reutilizar partes compatíveis de `auth-card-layout.tsx` após conferir seus consumidores. A composição nova recebe título/descrição e filhos, preservando a forma atual de layout Inertia.
- Alterações de classes permanecem nos componentes consumidores; não criar seletores globais de página em `app.css`. `AppLogo` pode ser composto localmente sem mudar sua apresentação em sidebar ou outras superfícies. `PasskeyVerify` e suas operações permanecem intactos; adequar somente o encaixe externo no login.
- Conservar `<Form>`, nomes/atributos de campos, `resetOnSuccess`, `disableWhileProcessing`, transform de token/e-mail, `PasswordInput`, status e condições `canRegister`/`canResetPassword`. Usar Wayfinder e `<Link>` existentes, sem URLs de aplicação hardcoded. Não corrigir problemas funcionais anteriores como parte da estilização sem alinhamento.
- A aparência usa o mecanismo existente de `use-appearance.tsx`, inicialização no app e cookies/localStorage; nenhuma preferência nova, seletor ou alteração de persistência. A variante escura segue os tokens FinAI, com conteúdo e ações equivalentes.

## Estratégia

Uma fase coesa entrega inicial e cinco páginas de acesso com um layout localizado, sem expor alteração visual parcial às páginas de segurança das irmãs. Primeiro conferir consumidores e fluxos; depois compor com a base pronta; por fim executar verificações no host e comparar evidências com as referências e adaptações acima.

Cobertura visual desta fase: as seis superfícies nos nove viewports 360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080, em claro e escuro, nos estados aplicáveis definidos em Aceite. Essa matriz inclui os estados de erro/sucesso/processamento listados, não todas as combinações possíveis de regras de validação. Não multiplicar automaticamente por variantes internas de passkey/2FA ou pela revisão de shell de #1016204.

O suporte de captura será implementado durante Desenvolvimento nesta filha, reaproveitando o padrão Python/Pest/RefreshDatabase de #1016112/#1016113. As imagens de planejamento comprovam acesso; não comprovam aceite do resultado. O preflight abaixo usa suporte já existente, autentica uma factory e verifica dashboard protegido. A captura final deverá recriar independentemente visitantes/autenticados não verificados, tokens e estados, sem credenciais pessoais ou dados de produção. O validador abre PNGs e compara visualmente; geração bem-sucedida e suíte verde não substituem essa análise.

## Baseline

Comando completo equivalente ao agregado `composer test`, expandido para PowerShell no Windows. `package.json` usa atribuições POSIX nos scripts do Bun e `composer.json` usa uma atribuição POSIX em `test:unit`; o comando conserva todos os verificadores e seus limites sem depender do shell interno do Composer. Build prepara assets e Wayfinder antes de lint/tipagem/browser. PHP 8.5 é selecionado apenas no processo. As configurações derivadas abaixo só redirecionam caches, mantendo regras originais; PHPStan explicita `analyse` para reconhecer caminhos Windows.

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

Pré-requisitos conferidos em 12/11/2026: PHP 8.5.12 do Herd com Xdebug 3.5.0; Bun 1.4.4, Node 26.1.0, Python 3.12, PowerShell, dependências e Chromium Playwright instalados; PostgreSQL de testes definido por `.env.testing`/`phpunit.xml`. Não expor configurações sensíveis nem executar preparação destrutiva do ambiente. `composer show --direct`: Laravel 13.42.0, Inertia Laravel 3.7.0, Fortify 1.42.0, Wayfinder 0.1.23, Pest 5.3.5, Browser 5.2.0, Pint 1.32.2, Rector 2.8.4 e Larastan 3.14.0. `package.json`: React 19, Inertia React 3, Tailwind 4, Vite+ 1.5.1 e Playwright 1.65.0. A CI em `.github/workflows/tests.yml` faz build seguido de `composer test` em Linux/PHP 8.5/PCOV; o comando local preserva a composição e cobertura exigidas.

| Verificador | Composição/configuração | Resultado inicial |
| --- | --- | --- |
| Assets e Wayfinder | `bun run build`, `vite.config.ts` | Aprovado |
| Formatação PHP | Pint `--parallel --test`, `pint.json` | Aprovado |
| Refatoração em conferência | Rector `--dry-run`, `rector.php` | Aprovado, 0 alterações e 0 erros |
| Formatação/lint frontend | `bun run test:lint`: `vp fmt --check resources/` e `vp lint` | Aprovado |
| Análise PHP | PHPStan/Larastan com `analyse`, `phpstan.neon` | Aprovado, 0 erros |
| Tipos frontend | `tsc --noEmit` | Aprovado |
| Cobertura de tipos PHP | Pest `--type-coverage --min=100` | Aprovado, 100%, 278,12s |
| Testes e cobertura PHP | Pest Browser/Unit/Feature em paralelo, `--coverage --exactly=100.0` | Aprovado: 197 testes, 776 asserções, 64,37s e cobertura 100% |

A suíte completa terminou com código 0 em 12/11/2026, sem modificar arquivos versionados. A depreciação de `withSetProviders()` no Rector é preexistente e não altera o escopo. Capturas atuais da inicial/login via Playwright no Herd retornaram HTTP 200 e ausência de overflow em 1366×768; imagens foram abertas.

Preflight autenticado do host aprovado: build, 1 teste, 11 asserções e 2 PNGs claro/escuro legíveis de dashboard protegido, código 0. A primeira prova detectou ausência do diretório ignorado `tmp`, exigido pelo wrapper existente antes do bootstrap; o comando final cria esse diretório explicitamente e passou na repetição. Isso não exigiu alteração no suporte antigo nem no produto. Evidências da preparação foram salvas em diretórios temporários fora das fontes; o executor recria evidências próprias e duráveis no Git runtime em cada execução. A captura final das 364 imagens depende da implementação do suporte desta fase e não foi executada nesta preparação.

## Riscos

- O layout compartilhado serve telas fora do escopo: isolar a nova composição nas cinco consumidoras é necessário para não antecipar #1016116. Não alterar primitivas globais ou o shell para resolver problemas locais.
- Login e cadastro possuem vários controles; em 360×800 o conteúdo pode exigir rolagem vertical. Conservar acesso ao fim do formulário e foco visível, sem esconder ações ou apenas mascarar overflow horizontal.
- Tokens e-mail/token da redefinição e mensagens de recuperação têm implicações de segurança; preservar o transform e a mensagem genérica, sem registrar valores sensíveis em metadados/capturas.
- Estados transitórios precisam ser gerados pelo fluxo real do formulário. Instrumentação de captura só pode controlar o transporte no teste e deve liberar a solicitação, sem trocar classes/DOM para fabricar um estado.
- Sem migração, nova permissão ou operação. Falha de acesso/captura é impedimento de verificação enquanto não houver defeito demonstrado; não tratar captura pendente como aceite visual.

## Fase 1 — Página pública e jornadas de acesso com identidade FinAI

### Objetivo

Adequar as seis superfícies com composição FinAI responsiva e coerente, preservando conteúdo funcional, autenticação, recuperação, verificação e navegação atuais.

### Dependências

Plano aprovado e preparado no Git, baseline e preflight disponíveis. Reusar identidade/temas implementados em #1016112 e integração atual de #1016113. #1016204 conserva a revisão do shell; #1016116 conserva estados de passkey/2FA/confirmação de senha. Não criar bloqueio de início que a tarefa publicada não possui.

### Mudanças esperadas

Adaptar `welcome.tsx` à marca, paleta, tipografia e componentes FinAI, preservando links/condições/conteúdo funcional. Implementar composição de acesso localizada e usá-la nas cinco páginas; adequar títulos, painéis, mensagens, alinhamento de campos e ações em claro/escuro. Manter todos os controles, incluindo lembrar, visibilidade de senha, entrada por passkey, links de retorno/cadastro/recuperação, reenvio e saída.

Completar suporte de captura nesta pasta (`capture.py` e fixture de teste, se necessária) e cobertura de browser apenas para lacunas observáveis: navegação pública e entre formulários, erros visíveis, processamento/desabilitado, sucesso e integração de aparência. Reusar testes HTTP existentes para regras e resultados no banco, sem replicar toda sua matriz no navegador.

### Arquivos prováveis

`resources/js/pages/welcome.tsx`; `pages/session/create.tsx`; `pages/user/create.tsx`; `pages/user-email-reset-notification/create.tsx`; `pages/user-password/create.tsx`; `pages/user-email-verification-notification/create.tsx`; composição nova em `resources/js/layouts/auth/` e componentes locais reutilizáveis se necessários. `tests/Browser/WelcomeTest.php`, `tests/Browser/LayoutTest.php` e teste Pest de jornadas, criado por Artisan se a cobertura justificar arquivo separado. Suporte de captura em `capture.py`/`capture-fixture.php` ao lado deste plano. Não há necessidade prevista de alterar controllers, rotas, tokens globais ou primitives.

### Limites

Preservar mensagens e nomes funcionais atuais, campos/regras/destinos/métodos HTTP, mecanismos de sessão/2FA/passkey, preferência de aparência e conteúdo funcional da inicial. Não redesenhar as telas das irmãs ou implementar revisão de shell. Não acrescentar operações financeiras ou dependências. Testes usam factories/banco testing; captura não cria rota pública nem lê dados pessoais.

### Estratégia

Conferir as versões e documentação antes de APIs novas; manter o padrão Inertia de layout e Form com Wayfinder. Compor a nova aparência por utilitários Tailwind locais e reutilizar tokens. Preservar testes e hooks existentes que representam a mesma ação. Testes novos/alterados seguem `testing-best-practices`, usam `assertNoJavaScriptErrors()` e cobrem resultados percebidos, não classes CSS.

Captura: usar Pest com fixture temporária em `tmp`, configuração XML derivada com caminhos absolutos e `RefreshDatabase`, `APP_ENV=testing`, SSR desligado e hot file de testes isolado. Criar usuários por factory `withoutTwoFactor()`, não verificados quando necessário, e tokens por broker real. Não abrir servidor adicional com `artisan serve`; Pest administra seus processos e o Herd permanece disponível.

Para processamento, acionar o `<Form>` real com dados válidos e segurar temporariamente o envio XHR no contexto exclusivo do teste, depois de o Inertia ativar `processing`; capturar os controles visivelmente desabilitados/spinner e liberar o transporte, verificando o resultado real. Não injetar estado React, trocar texto/classes/DOM ou simular sucesso no componente. Erros/sucessos devem vir de solicitações reais ou sessão de teste fiel aos contratos já cobertos; registrar qual mecanismo foi usado. Se a instrumentação não puder produzir um estado, falhar com o impedimento específico.

O suporte aceita `RALPH_EVIDENCE_REQUEST` como dados JSON (`findings`, `plan_basis`, `rendered_verification`) e refaz a cobertura aprovada; não executa texto recebido. Salvar PNGs legíveis e `captures.jsonl` com path/reference/screen/state/viewport/theme em `RALPH_EVIDENCE_DIR`, sem credenciais/tokens/cookies. Conferir quantidade/conjunto esperado, dimensões, tema, rota e marcadores de cada estado; redirecionamento inesperado, erro JS, overflow ou imagem ausente falham. Fechar apenas processos/contextos criados pelo comando, inclusive em falha, e preservar artefatos para diagnóstico.

### Aceite

- Marca completa FinAI reconhecível nas seis superfícies; títulos Georgia, corpo system-ui, cores/bordas/raios/espaçamentos e estados compatíveis com a referência e adaptações de Arquitetura. A inicial preserva as operações e conteúdo funcional atuais, sem arte de marca starter ou capacidades financeiras antecipadas.
- Matriz visual: nove viewports e dois temas de Estratégia para cada estado a seguir: inicial visitante e autenticado; cadastro padrão, erro de validação e processamento; login padrão, credenciais inválidas, processamento e status de senha redefinida; recuperação padrão, erro de validação, processamento e sucesso genérico; redefinição padrão, erros de senha/confirmação, token inválido e processamento; verificação padrão, reenvio em processamento e confirmação de reenvio. São 20 estados, 18 combinações de viewport/tema por estado, totalizando 360 capturas. O estado autenticado da inicial usa usuário de teste; verificação usa não verificado. Não exigir estados próprios de passkey/2FA nem novas mensagens onde não existem.
- Nos formulários dessa matriz, capturar o estado padrão com foco real em um controle e conferir acesso por teclado até a última ação; conservar foco visível, rótulos, hover e controles habilitados/desabilitados aplicáveis. Evidência adicional representativa no login: hover no link de recuperação e no botão principal, separadamente, em 1366×768/claro e escuro (4 imagens adicionais; conjunto final de 364 imagens). Não multiplicar todos os estados por todos os elementos focáveis.
- Em todos os casos da matriz, nenhum overflow horizontal real, controles e mensagens legíveis e ações alcançáveis por rolagem vertical, sem clipping de foco. Claro/escuro têm conteúdo/ações equivalentes; modo sistema conserva o mecanismo existente e acompanha o dispositivo sem substituir escolha explícita.
- Os caminhos inicial → login/cadastro, login → recuperação/cadastro, recuperação → login e marca → inicial continuam disponíveis; autenticado na inicial continua com acesso ao dashboard. Login mantém lembrar, passkey e encaminhamento atual a 2FA. Cadastro válido, login válido, recuperação válida e redefinição válida mantêm resultado/retorno atuais; inválidos apresentam as mensagens atuais. Verificação mantém reenvio, status e saída com nova exigência de login após sair.
- Visitantes e autenticados mantêm restrições `guest`/`auth`; usuário já verificado continua redirecionado do aviso ao dashboard. Token inválido e recuperação de conta inexistente conservam comportamento/mensagem atuais. Confirmação de senha e desafio 2FA conservam composição e operações porque não passam ao layout novo.
- Comparação visual independente deve abrir as capturas e confrontar cada estado exigido com design-input-001 e adaptações aprovadas, registrando resultado verificado. Evidência inacessível/incompleta mantém aceite visual bloqueado; suíte funcional aprovada não o substitui.

### Verificação focada

- `tests/Browser/LayoutTest.php`: conservar login → cadastro, passkey presente e redefinição real que confere hash salvo e retorno ao login. `WelcomeTest.php`: preservar sua finalidade e verificar marca/operações atuais; não apagar testes ou remover conteúdo funcional para adequar a asserção.
- `SessionControllerTest.php`: sucesso com/sem lembrar, credenciais inválidas, campos obrigatórios, 2FA, logout e redirect de autenticado. `UserControllerTest.php`: cadastro válido com usuário/senha persistidos, obrigatórios/formato/duplicidade e redirect de autenticado. Reusar essa cobertura HTTP.
- `UserEmailResetNotificationTest.php`: envio, mesma mensagem para inexistente, obrigatoriedade/formato e redirect de autenticado. `UserPasswordControllerTest.php`: token válido com hash atualizado, token inválido, e-mail inexistente, obrigatórios/confirmação e redirect de autenticado. `UserEmailVerificationNotificationControllerTest.php`/`UserEmailVerificationTest.php`: aviso/reenvio/status, usuário já verificado, verificação e assinatura inválida. Preservar essas provas; não acrescentar novas políticas.
- Acrescentar browser apenas para a lacuna de percurso público completo, apresentação de erro/sucesso/processamento e ações por teclado após a nova composição. Cobrir modo sistema navegando entre inicial e acesso e preservação de escolha explícita; `AppearanceTest.php` já cobre persistência e reação ao dispositivo nas configurações, sem precisar duplicar aquela matriz. Reusar `ShellAccessTest.php` para destinos protegidos e conferir guest em verificação se a lacuna exigir teste HTTP.
- Rodar cada teste editado e as verificações no host abaixo. Gate 3 executa a suíte completa do Baseline. Se houver PHP modificado, aplicar `vendor/bin/pint --dirty --format agent` durante desenvolvimento e revisar o diff; comandos verificadores abaixo permanecem em modo conferência.

### Inventário das saídas de verificação

Inventário válido para preflight, host, captura e Gate 3, incluindo falhas e interrupções. Fontes inspecionadas: `composer.json`, `package.json`, `vite.config.ts`, `pint.json`, `rector.php`, `phpstan.neon`, `phpunit.xml`, `tests/Pest.php`, plugins de cache do Pest/type-coverage e `Pest/Browser/Support/Screenshot.php`, `Trace.php` e `BrowserExpectationFailedException.php` instalados.

| Verificador | Saída normal | Falha/interrupção e destino |
| --- | --- | --- |
| Build/Wayfinder | Manifesto/assets em `public/build`; módulos gerados em `resources/js/actions`, `routes` e `wayfinder` | Log e arquivos parciais nos mesmos diretórios; só conteúdo não rastreado gerado pertence ao verificador |
| Pint | Log e cache em `RALPH_ARTIFACTS_DIR/pint.cache` | Mesmo destino, sem corrigir fontes por `--test` |
| Rector/PHPStan | Configurações derivadas/caches em `RALPH_ARTIFACTS_DIR`; regras preservadas | Logs/diffs/caches parciais no mesmo destino; caches históricos em `tmp` declarados |
| Frontend fmt/lint/types | Diagnósticos no log; `tsc --noEmit` não emite arquivos | Mesmo log; nenhum `--fix`; temporários internos permanecem nas áreas das dependências |
| Pest/type coverage | Log, JSON de type coverage e JUnit/cache direcionáveis para `RALPH_ARTIFACTS_DIR`; caches internos ignorados das dependências | Logs/relatórios parciais; cobertura percentual no terminal, sem HTML solicitado; arquivos internos não são diretórios de fonte a declarar |
| Browser | Imagens de aceite e metadados em `RALPH_EVIDENCE_DIR` | Falha de asserção gera PNG em `tests/Browser/Screenshots`; traces quando habilitados em `tests/Browser/Traces`; vídeo não configurado. Preservar ambos como saídas, sem ignorar imagens globalmente |
| Bootstrap Laravel/fixtures | Caches/views/sessões em `storage/framework`, logs em `storage/logs` e caches em `bootstrap/cache`; fixture temporária em `tmp` | Mesmos caminhos; suporte remove apenas seus temporários/processos. Arquivos rastreados, `.gitignore` e baselines continuam protegidos |

O executor arquiva saídas anteriores/atuais e fornece os mapeamentos duráveis, inclusive se o comando falhar. Não apagar diagnósticos existentes, não declarar a pasta da tarefa como saída e não deslocar fontes/baselines rastreadas. Uma falha de asserção com PNG gerado é falha do comando e não, por si, alteração insegura de fonte; ambos os resultados devem permanecer separados.

### Artefatos de verificação

- `tests/Browser/Screenshots`
- `tests/Browser/Traces`
- `public/build`
- `resources/js/actions`
- `resources/js/routes`
- `resources/js/wayfinder`
- `tmp`
- `storage/framework`
- `storage/logs`
- `bootstrap/cache`

### Preflight da validação

Suporte já existente de #1016112: build e captura autenticada isolada de dashboard em claro/escuro; confirma bootstrap/browser, ausência de redirect para login e PNGs legíveis. `RALPH_CAPTURE_MODE=preflight` e diretórios privados são fornecidos pelo executor. Não repetir esse preflight dentro da sessão de desenvolvimento; o relatório do pai já estabelece disponibilidade. Não depende da nova composição nem comprova seu aceite.

```powershell
$env:Path = "$env:USERPROFILE\.config\herd\bin\php85;$env:Path"
& bun run build
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
New-Item -ItemType Directory -Force -Path 'tmp' -ErrorAction Stop | Out-Null
python 'docs/harness/features/1016101-adequacao-visual-do-finai/tasks/dev-1016112-adequacao-visual-do-finai-identidade-e-temas-no-painel-atual/capture.py'
exit $LASTEXITCODE
```

### Verificação no host

Build antes de lint/tipagem/browser; comandos de conferência e testes com banco isolado. O hot file de `tests/Pest.php` evita ler/alterar `public/hot`. O novo teste de jornadas, se criado, fica em `tests/Browser` e é incluído pelo diretório. Se só faltar executar checks por limitação do sandbox, devolver `ready-for-host-checks` com `pending_checks: ["host", "rendered"]`; implementação/fixtures incompletas não são prontidão.

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
& php vendor/bin/pest --compact --cache-directory "$env:RALPH_ARTIFACTS_DIR/pest-cache" --log-junit "$env:RALPH_ARTIFACTS_DIR/focused.xml" tests/Browser tests/Feature/Controllers/SessionControllerTest.php tests/Feature/Controllers/UserControllerTest.php tests/Feature/Controllers/UserPasswordControllerTest.php tests/Feature/Controllers/UserEmailResetNotificationTest.php tests/Feature/Controllers/UserEmailVerificationNotificationControllerTest.php tests/Feature/Controllers/UserEmailVerificationTest.php tests/Feature/ShellAccessTest.php
exit $LASTEXITCODE
```

### Verificação renderizada

O suporte abaixo será implementado em Desenvolvimento nesta filha conforme Estratégia e Aceite; sua ausência depois do handoff é impedimento, não permissão para reduzir a matriz. Deve recriar os 20 estados em todas as 18 combinações, mais os hovers representativos, validar PNGs/metadados e tratar pedido suplementar como dados. Cada execução começa com build porque o executor preserva/limpa as saídas geradas entre comandos. Comparação independente usa essas imagens sem iniciar navegador na sessão somente leitura.

```powershell
$env:Path = "$env:USERPROFILE\.config\herd\bin\php85;$env:Path"
$env:APP_ENV = 'testing'
$env:PLAYWRIGHT_BROWSERS_PATH = "$env:LOCALAPPDATA\ms-playwright"
& bun run build
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
New-Item -ItemType Directory -Force -Path 'tmp' -ErrorAction Stop | Out-Null
python 'docs/harness/features/1016101-adequacao-visual-do-finai/tasks/dev-1016114-adequacao-visual-do-finai-pagina-inicial-e-jornadas-de-acesso/capture.py'
exit $LASTEXITCODE
```
