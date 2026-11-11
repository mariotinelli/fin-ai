# [DEV] [WEB] [USUARIO] Adequação visual do FinAI - Identidade e temas no painel atual

- Redmine: `#1016112`
- Tipo: `DEV`
- Tracker: Task (`4`)
- Item pai: `#1016101`
- Estimativa: `2h`

## Descrição

## Entrega

Aplicar a marca e a identidade FinAI aos componentes compartilhados e ao dashboard atual, preservando os mecanismos existentes de aparência. A base atual é neutra e ainda contém a marca do starter; esta entrega deve produzir uma base visual inspecionável em claro, escuro e sistema.

## Escopo e limites

Responsável pela aparência compartilhada: marca, tipografia, paleta, raios, bordas, sombras, controles e seus estados. A composição da navegação pertence à entrega de estrutura; as composições particulares das outras telas pertencem às entregas correspondentes. Não transformar o dashboard placeholder em dashboard financeiro.

## Critérios de aceite

- No painel atual e nos componentes compartilhados, apresentar marca FinAI e, no claro, fundo #F5F7F8, superfícies brancas, texto #172622, secundário #52615C, principal #145C46, positivo #146345, negativo #A12B36, bordas #D6DFDB e destaque #E4F0E9, títulos Georgia, corpo system-ui, controles com raio8px e painéis16px; preservar proporções, espaçamentos e estados aplicáveis da referência.
- No escuro, adaptar fundos, superfícies, bordas, textos e estados à identidade FinAI com leitura e distinção visual, sem conservar a aparência neutra do starter.
- Manter claro, escuro e acompanhar o sistema, preferência persistida conforme comportamento atual e reação às mudanças do dispositivo somente quando sistema estiver selecionado.
- Aplicar linguagem comum de hover, foco, ativo, desabilitado, carregamento, erro e feedback aos componentes existentes, preservando os significados e interações.
- O painel continua sem números ou operações financeiras novas, e a base não apresenta rótulos de armazenamento apenas local ou assistente simulado.
- Nas superfícies desta entrega, conferir os nove viewports (360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080), temas claro e escuro, estados aplicáveis e ausência de rolagem horizontal da página; manter acesso às ações atuais, rótulos e foco visível.

## Dependências

Pode iniciar com a base atual. Fornece identidade e aparência compartilhada às entregas Estrutura e navegação responsiva atuais, Página inicial e jornadas de acesso, Perfil, senha e aparência e Dois fatores e passkeys. A aceitação desta base é demonstrada no painel atual; a QA conjunta verifica a aplicação em todas as composições.

## Referências

Item pai Redmine #1016101; regras/critérios R1, R2, R3, R5, R6, CA1, CA2, CA5, CA7.

- design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; :root, .brand, .btn, campos, diálogos, cores/tipografia; #overview como referência de linguagem, sem transportar suas capacidades futuras
- Adaptações aprovadas: todas as telas atuais, claro/escuro/sistema preservados; telas futuras nas próximas Features.

<!-- project-slices-child:6a99b56c0c8da3f45cb25f4895645e08c8ca645ba2db68b160e66aa3fa80fe09 -->

## Relações

- `#1016112` blocks `#1016117`
