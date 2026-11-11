# DEV #1016112 — Identidade e temas no painel atual

## Identidade e fontes

- Filha: #1016112, `[DEV] [WEB] [USUARIO] Adequação visual do FinAI - Identidade e temas no painel atual`, em `task.md` neste diretório.
- Requisito pai: `docs/harness/features/1016101-adequacao-visual-do-finai/feature.md`, especialmente R1–R3, R5–R7 e CA1–CA5, CA7–CA9, nos limites desta filha.
- Contexto publicado: `docs/harness/scopes/2026-11-11-finai-mvp/scope.md`, seção Sequenciamento atual do fatiamento. Esta é a primeira entrega da fundação visual, pode começar na base atual e bloqueia a QA #1016117. Preservar numeração e relações; não interpretar publicação de requisito como implementação.
- Design principal: `design-input-001`, normalizado no caminho abaixo. Localizadores: `:root`, `.brand`, `#i-mark`, `.btn`, campos, `.panel`, diálogos, estados e manifesto dos nove viewports. `#overview` orienta a linguagem, sem transportar seus dados, ações ou composições financeiras.
- Adaptações já aprovadas: aplicar identidade às telas atuais, conservar claro/escuro/sistema e criar a variante escura coerente; nenhuma composição escura foi fornecida. As composições de navegação, acesso e configurações ficam nas filhas #1016113–#1016116.
- Instruções: `AGENTS.md`; skills `tailwindcss-development`, `inertia-react-development` e `testing-best-practices` em `.agents/skills`. `.ai/rules` não existe nesta inspeção; `.ai/guidelines` contém as regras de ações e anotações já incorporadas ao AGENTS.

## Referências visuais

- `docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md`

## Objetivo

Reconhecer a identidade FinAI no painel atual e nos componentes compartilhados, com cores, marca, tipografia, raios e estados consistentes em claro e escuro. Manter a preferência de aparência e seus mecanismos atuais, sem antecipar capacidades financeiras.

## Estado atual

- `resources/css/app.css` usa tokens neutros em `:root` e `.dark`, Instrument Sans, raio base de 10px e variantes menores. O vínculo dos tokens com utilitários Tailwind já existe em `@theme`.
- `resources/js/components/app-logo-icon.tsx` contém a marca Laravel; `app-logo.tsx` utiliza o nome compartilhado pelo Inertia e inverte a cor do símbolo no escuro. Layouts de autenticação também consomem o ícone. `app.tsx`/`ssr.tsx` têm fallback Laravel para o título; conferir somente os pontos de identidade efetivamente necessários, sem alterar notificações ou configuração global de nome por conveniência.
- `resources/views/app.blade.php` define fundos neutros antes de carregar o CSS e aponta ícones públicos. `vite.config.ts` configura Instrument Sans por meio de `laravel-vite-plugin/fonts`; não há `config/fonts.php`. Para cumprir corpo system-ui, remover o uso visual da fonte do starter e avaliar a remoção de seu carregamento sem substituir dependências.
- `dashboard.tsx` contém três regiões de placeholder e uma região maior, bordas neutras e `overflow-x-auto`. Não há dados financeiros a preencher. `AppLayout` usa `app-sidebar-layout`; `app-sidebar.tsx` mantém Dashboard e links externos existentes, que esta filha não reorganiza.
- `use-appearance.tsx`: `initializeTheme()` lê localStorage, inicializa sistema quando ausente, mantém cookie de 365 dias e aplica `.dark`/`colorScheme`. `updateAppearance()` persiste ambos os armazenamentos. O listener de `matchMedia` recalcula o tema usando a preferência atual, portanto escolhas explícitas já prevalecem. Preservar esse contrato; não migrar preferências.
- `appearance-tabs.tsx`, `input-error.tsx`, `text-link.tsx`, `user-info.tsx` e alguns consumidores compartilhados possuem cores fixas que escapam aos tokens. `ui/button.tsx`, `input.tsx`, `card.tsx`, `dialog.tsx`, `sheet.tsx`, menus e seletores centralizam estilos e estados Radix. `ui/sonner.tsx` usa tokens para fundo/texto/borda e `use-flash-toast.ts` mantém as mensagens e tipos funcionais.
- Inspeção renderizada: Playwright já instalado abriu `/login` no Herd em 1366×768, sem erro JavaScript, com logo Laravel, Instrument Sans e fundo branco neutro. A referência original foi renderizada em arquivo temporário, com scripts removidos, e a captura foi inspecionada. O dashboard autenticado não foi aberto nesta inspeção; sua estrutura foi lida no código. Não foram criadas contas no banco da aplicação.
- `route:list --except-vendor --method=GET` e `routes/web.php` confirmam inicial, login/cadastro/recuperação, dashboard, perfil, senha, aparência, dois fatores e passkeys; confirmação de senha e desafio são complementados pelo Fortify. Esse inventário orienta os consumidores, sem autorizar recomposição de todas as páginas nesta filha.

## Escopo

Inclui tokens claros/escuros, marca compartilhada, hierarquia tipográfica, raio de controles 8px e painéis 16px, bordas/sombras/espaçamentos aplicáveis, aparência dos componentes existentes e do dashboard placeholder. Inclui preservação de preferências, foco, rótulos e estados de interação.

Não inclui nova navegação, mudança de destinos, páginas financeiras, números ilustrativos, operações financeiras, rótulos de armazenamento local ou assistente simulado, mudanças de autenticação, permissões, mensagens funcionais ou validações. A composição de cada tela irmã permanece com sua entrega; ajustes de componentes compartilhados podem refletir nelas e devem preservar sua operação.

## Arquitetura

- Reutilizar o vínculo semântico de `app.css` com Tailwind v4 e a ativação `.dark`. Definir cores claras exatas: fundo #F5F7F8, superfície #FFFFFF, texto #172622, secundário #52615C, principal #145C46, positivo #146345, negativo #A12B36, borda #D6DFDB e destaque #E4F0E9. Preservar foco visível com a referência #1D5DB0 no claro; derivar contraste adequado no escuro.
- Mapear corpo system-ui e títulos de destaque Georgia sem converter todos os rótulos e títulos pequenos em serifados. Usar a escala do design (4/8/16/24/32/48/64px), controles com altura aplicável de 44px e hierarquia da fonte, sem impor geometria da navegação futura.
- Separar semanticamente raios de controle e painel; verificar os consumidores de `rounded-md/lg/xl` em vez de mudar um único raio e presumir que todos atingiram 8/16px. Preservar avatares circulares e outros formatos específicos.
- Reproduzir o símbolo vetorial `#i-mark` e a distinção da palavra da referência nos componentes existentes; conservar nome acessível, dimensões adequadas ao espaço atual e boa leitura em ambos os temas. Ajustar ícone público somente onde servir à identidade compartilhada, sem adicionar geração de imagens ou bibliotecas.
- A variante escura é decisão de implementação dentro da adaptação aprovada: superfícies verdes profundas, texto claro e estados distinguíveis, sem deixar o starter neutro. Registrar a comparação e as cores efetivamente usadas no resultado da validação, sem criar documentos extras.
- Análise de alcance: tokens e primitivas atingem acesso, perfil, senha, aparência, dois fatores, passkeys, menus, diálogos e toast. Manter props, variantes, eventos, submissões, mensagens e contratos Radix; corrigir cores fixas nos componentes compartilhados necessários. Não usar seletores globais de geometria que recomponham páginas irmãs nem editar lógica PHP para um ajuste visual.
- Usar os mecanismos existentes de Inertia/Wayfinder; não criar URLs fixas ou endpoints para demonstração. Antes de mudanças dependentes de APIs, consultar `search-docs` da versão instalada. Nesta inspeção foram consultados padrões Tailwind de tokens/escuro e testes de browser Pest.

## Estratégia

Duas fases sequenciais, cada uma inspecionável e pronta para commit: primeiro identidade e temas demonstrados no painel; depois completar estados dos controles e comprovar preservação da aparência. Verificações visuais usam browser/Playwright/Pest já instalados, sem nova dependência, rota de catálogo ou tela demonstrativa.

Comparar o resultado renderizado com o CSS/HTML normalizado do design, recriando referência estática temporária sem executar scripts do protótipo, quando necessário. Capturas temporárias e leitura de estilos computados auxiliam a comparação; gerar screenshot sem inspecioná-la não é aceite. Para superfícies autenticadas, usar fixtures com `User::factory()->withoutTwoFactor()` e sessão do Pest, conforme `tests/Browser/LayoutTest.php`, no ambiente de testes. Nunca depender de credenciais pessoais ou criar conta persistente via tinker.

Em cada fase de UI, conferir os nove viewports (360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080), claro e escuro, nas superfícies e estados alterados. Registrar diferenças aprovadas e evidência por conjunto de viewport/tema/estado na validação do executor. Comparação obrigatória bloqueada pelo ambiente impede aprovação da fase; testes funcionais não a substituem.

## Baseline

Comando completo equivalente aos scripts de `composer test`, expandido para PowerShell no Windows. Seleciona PHP 8.5 instalado pelo Herd também no ambiente sem perfil do Gate 3 e substitui apenas a atribuição POSIX de `XDEBUG_MODE` pelo equivalente PowerShell. Nenhuma etapa usa modo de correção. Cada código de saída é propagado:

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

Pré-requisitos observados: PHP 8.5.12 em `%USERPROFILE%/.config/herd/bin/php85`, Xdebug 3.5 com coverage, Bun 1.4.4, Node 26.1.0, dependências já instaladas, Playwright com Chromium disponível. Terminal padrão resolve PHP 8.4.27; a seleção acima é obrigatória. PostgreSQL de teste é definido por `.env.testing`/`phpunit.xml`, sem copiar valores sensíveis para este plano. Não executar preparação destrutiva do `orca.yaml`.

Versões PHP confirmadas por `composer show --direct`: Laravel 13.40.0, Inertia Laravel 3.7.0, Wayfinder 0.1.23, Pest 5.3.5, plugin Browser 5.2.0, Pint 1.32.1, Rector 2.8.4 e Larastan 3.14.0. `package.json` declara React 19, Inertia React 3, Tailwind 4, Vite+ 1.4.0 e TypeScript 7; manter o lock instalado.

| Verificador | Composição/configuração | Resultado observado em 11/11/2026 |
| --- | --- | --- |
| Formatação PHP | Pint `--parallel --test`, `pint.json` | Aprovado |
| Refatoração em modo de conferência | Rector `--dry-run`, `rector.php` | Aprovado; totais reportados: 0 alterações, 0 erros |
| Formatação/lint frontend | `bun run test:lint`: `vp fmt --check resources/` e `vp lint`, opções em `vite.config.ts` | Aprovado |
| Análise PHP | PHPStan/Larastan, nível max, `phpstan.neon` | Aprovado, 0 erros |
| Tipos frontend | `bun run test:types`: `tsc --noEmit` | Aprovado |
| Cobertura de tipos PHP | Pest `--type-coverage --min=100` | Aprovado, 100,0% (239,14s) |
| Testes e cobertura PHP | Pest `--parallel --coverage --exactly=100.0`; suites Browser, Unit e Feature, fonte `app`, `phpunit.xml` | Aprovado: 177 testes, 559 asserções, 56,344s e cobertura total 100,0% |

Resultado inicial: suíte completa aprovada, processo encerrado com código 0. Após a execução, nenhuma alteração em arquivo versionado; somente os dois artefatos deste planejamento estão pendentes. Este resultado não dispensa os Gates 2 e 3 de cada fase.

A CI `.github/workflows/tests.yml` executa build antes de `composer test`, com PHP 8.5/PCOV e Node 24 em Linux; não alegar equivalência ambiental com esta execução Windows/Xdebug. O build não integra o script `composer test`; executá-lo como verificação focada após mudanças de assets e conferir o diff de arquivos gerados. Avisos preexistentes observados: uma extensão OPcache incompatível é tentada na inicialização do PHP 8.5 e Rector informa depreciação de `withSetProviders()`. Não houve impedimento nas etapas concluídas; não alterar ini global ou dependências para ocultar avisos.

## Riscos

- Tokens globais e alturas de controles podem causar recortes ou overflow em telas consumidoras. Inspecionar as superfícies afetadas, especialmente no viewport de 360px; corrigir a primitiva quando possível, sem absorver a composição das filhas seguintes.
- Cores utilitárias fixas podem conservar ilhas do starter e sobrepor os tokens, inclusive no logo, placeholders, erros, avatar e preferência de aparência. Revisar os consumidores em ambos os temas.
- Inicialização Blade e CSS devem concordar para evitar fundo neutro antes da hidratação. Não reescrever persistência nem alterar cookie como efeito de estilo.
- Os testes PHP de aparência cobrem compartilhamento do cookie, mas não reação do browser a `matchMedia` nem persistência via interface. Essa lacuna será coberta na fase 2 sem testes que apenas repitam valores CSS.
- Sem migrações, novos privilégios ou alteração de dados de negócio. Preservar testes e proteção das rotas. Se faltar comparação visual autenticada ou o ambiente impedir a suíte, registrar bloqueio; não converter isso em aceite.

## Fase 1 — Marca, tokens e painel nos dois temas

### Objetivo

Disponibilizar a identidade FinAI compartilhada e demonstrá-la no dashboard atual, mantendo seus placeholders e operações existentes.

### Dependências

Plano aprovado, runtime do Baseline e acesso ao browser e aos assets atuais. Nenhum fornecedor anterior de implementação; esta própria tarefa fornece a base às próximas entregas.

### Mudanças esperadas

Aplicar tokens claros e adaptação escura, corpo system-ui, títulos de destaque Georgia, raios semânticos, bordas, sombras e marca vetorial da fonte. Alinhar o fundo inicial Blade ao tema. Adequar os placeholders e superfícies do dashboard para que a identidade seja inspecionável sem adicionar dados ou ações. Ajustar os pontos compartilhados de marca e eventuais ícones de aplicação necessários; preservar a organização da navegação.

### Arquivos prováveis

`resources/css/app.css`, `resources/js/components/app-logo.tsx`, `app-logo-icon.tsx`, `heading.tsx`, `resources/js/pages/dashboard.tsx`, `resources/views/app.blade.php`, `resources/js/app.tsx`, `ssr.tsx`, `vite.config.ts` e ícones existentes em `public/`. Somente consumidores de marca que precisem adaptar dimensões/cores, sem recomposição de páginas de acesso.

### Limites

Não transportar saldo, receitas, despesas, seletor de mês, ações de transação ou assistente do protótipo. Não reorganizar sidebar/topbar, alterar rotas, contratos de autenticação ou fontes de nome compartilhado com mensagens de backend. Não modificar preferências de aparência.

### Estratégia

Partir dos tokens e do símbolo fornecidos, conferir onde utilitários atuais os sobrescrevem e adaptar o painel e marca compartilhada. Preservar semântica/acessibilidade dos links e o estado de navegação atual. Executar build com PHP 8.5 disponível ao Wayfinder. Não criar testes automatizados só para conferir cor ou layout estático.

### Aceite

- Painel e marca compartilhada reconhecíveis como FinAI, com cores claras exatas, fundo/superfície distintos, tipografia e proporções aplicáveis da referência; controles 8px e painéis 16px conforme o uso.
- Escuro com identidade própria, leitura, bordas e superfícies distinguíveis, mesma informação e ações do claro.
- Dashboard mantém placeholders, sem conteúdo financeiro, rótulos locais/simulação ou destinos futuros.
- Comparação renderizada com `:root`, `.brand`/`#i-mark` e superfícies de `#overview`, respeitando a adaptação autorizada do painel sem capacidades futuras. Conferir nove viewports e dois temas, foco e ausência de rolagem horizontal da página. A geometria completa de navegação será entregue por #1016113; não alegar seu aceite aqui.

### Verificação focada

`bun run build` com PHP 8.5 no PATH, tipos/lint dos arquivos alterados e inspeção em browser do painel autenticado usando fixture de teste. Fazer smoke dos consumidores da marca em login e configurações, sem exigir a composição final das filhas seguintes. `tests/Browser/LayoutTest.php` já verifica acesso a configurações, aparência, passkeys, toast, exclusão e redefinição; seu teste de layout usa usuário `withoutTwoFactor()` e comprova caminhos existentes, não fidelidade visual. A captura inicial de login serve de evidência do estado anterior, não como referência a preservar. A suíte completa continua obrigatória no Gate 3.

## Fase 2 — Estados compartilhados e preservação da aparência

### Objetivo

Completar a linguagem visual dos controles existentes e demonstrar que claro, escuro e sistema continuam funcionando e persistindo.

### Dependências

Fase 1 concluída. Usar seus tokens e componentes; não refazer a base nem ampliar a navegação.

### Mudanças esperadas

Adequar primitivas e consumidores compartilhados necessários: botões, inputs, checkbox, seletores, menus, diálogos/sheets, cards, alertas, erro de campo, links, avatar, skeleton/spinner e toast, incluindo hover, foco, ativo, desabilitado, carregamento e feedback quando existentes. Remover cores neutras/fixas que contradigam a identidade, incluindo `appearance-tabs.tsx`, preservando valores, rótulos e eventos. Reusar o mecanismo de tema; mudar sua lógica somente se um defeito observado impedir o comportamento aprovado.

Adicionar cobertura de browser enxuta para a lacuna real de aparência: selecionar cada modo pela interface, recarregar e manter a escolha; simular mudança de preferência do dispositivo em sistema e com claro/escuro explícitos, observando a aparência renderizada. Cobrir navegação posterior preservando o modo e ausência de erros JavaScript. Não duplicar os testes PHP de cookies nem usar testes para repetir a implementação CSS.

### Arquivos prováveis

`resources/js/components/ui/` nas primitivas afetadas, `input-error.tsx`, `text-link.tsx`, `user-info.tsx`, `appearance-tabs.tsx`, consumidores compartilhados com cores fixas e `resources/css/app.css`. `tests/Browser/AppearanceTest.php` ou ampliação localizada de `LayoutTest.php`; `use-appearance.tsx` apenas se necessário e comprovado.

### Limites

Não alterar campos, regras, mensagens, endpoints, operações, permissões ou fluxo de autenticação; não recompor telas de perfil, senha, dois fatores, passkeys ou acesso. Não criar catálogo visível de componentes nem novas dependências. Estados ausentes no produto não exigem novas capacidades só para demonstrar aparência.

### Estratégia

Mapear as primitivas aos controles/diálogos da referência e manter contratos de props/eventos e acessibilidade Radix. Validar estados em telas existentes com dados isolados de teste; a exclusão deve poder ser cancelada na inspeção visual. Criar eventual teste novo com Artisan/Pest seguindo convenções, após consultar documentação de APIs do browser para emulação de sistema e os arquivos aplicáveis de `testing-best-practices`. Não depender de esperas fixas.

### Aceite

- Controles e feedback existentes apresentam linguagem comum da referência, com raios, foco, estados e identificação de positivo/negativo, em ambos os temas. Textos funcionais, rótulos acessíveis, teclado, abrir/fechar/cancelar e ações continuam disponíveis.
- Light, Dark e System continuam selecionáveis; a preferência persiste ao recarregar. Sistema acompanha mudança do dispositivo; escolhas explícitas não são substituídas. Verificar visualmente a aparência aplicada, além do armazenamento.
- Nos nove viewports e dois temas, comparar painel e os estados dos componentes efetivamente alterados em suas telas consumidoras com `.btn`, campos, avisos e diálogos do design. Conferir leitura, foco, ações acessíveis e ausência de overflow de página; não declarar aceite da composição das filhas irmãs.
- Nenhuma mudança de dados/segurança e nenhuma capacidade financeira nova. Comparação visual registrada como verificada; se indisponível, fase bloqueada, mesmo com testes funcionais verdes.

### Verificação focada

Executar o teste de aparência novo/alterado isoladamente e após cada edição. Reusar `tests/Unit/Middleware/HandleAppearanceTest.php` (dark/light/system e default de cookie), `tests/Browser/LayoutTest.php` (fluxos reais, toast e diálogos), `tests/Feature/Controllers/SessionControllerTest.php` (sessão válida, credenciais inválidas e desafio), `UserProfileControllerTest.php` (renderização, persistência e validação) conforme o alcance dos componentes. Esses testes não comprovam sozinhos cor, contraste ou a reação ao dispositivo. Preservar `WelcomeTest.php` e seu propósito; a página inicial dedicada pertence à filha #1016114. Rodar `bun run build` após mudanças de assets, comparação renderizada dos estados alterados e suíte completa do Baseline no Gate 3. Se houver PHP alterado, cumprir Pint antes de finalizar.
