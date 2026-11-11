# [DEV] [WEB] [USUARIO] Adequação visual do FinAI - Estrutura e navegação responsiva atuais

- Redmine: `#1016113`
- Tipo: `DEV`
- Tracker: Task (`4`)
- Item pai: `#1016101`
- Estimativa: `2h`

## Descrição

## Entrega

Adequar estrutura, cabeçalho, navegação e menu do usuário da área autenticada à composição FinAI responsiva, mantendo os destinos atualmente disponíveis. A sidebar e o menu móvel atuais diferem da geometria e organização superior da referência.

## Escopo e limites

Responsável pela disposição compartilhada e adaptações por largura, sem redefinir marca ou tema. Não criar destinos Transações/Assistente nem números, formulários ou operações financeiras.

## Critérios de aceite

- No desktop, apresentar geometria compatível com sidebar240px, cabeçalho80px e conteúdo da referência nos espaços aplicáveis; em larguras intermediárias e celulares, reorganizar a navegação no topo conforme o design.
- Manter acesso aos destinos atuais, configurações, menu do usuário e saída, com indicação do destino ativo onde aplicável. Não criar links para páginas futuras.
- Integrar a identidade e os temas fornecidos por Identidade e temas no painel atual, mantendo conteúdo e ações equivalentes entre claro e escuro.
- Os caminhos e restrições de acesso existentes permanecem iguais; navegação e menus continuam utilizáveis por teclado com foco visível.
- Nas superfícies desta entrega, conferir os nove viewports (360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080), temas claro e escuro, estados aplicáveis e ausência de rolagem horizontal da página; manter acesso às ações atuais, rótulos e foco visível.

## Dependências

Pode iniciar com a estrutura atual e a referência. Para concluir o aceite visual, integrar Identidade e temas no painel atual. As composições de acesso e configurações integram esta estrutura quando aplicável, sem bloqueio técnico de início entre essas entregas.

## Referências

Item pai Redmine #1016101; regras/critérios R1, R2, R4, R7, CA1, CA6, CA7, CA9.

- design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; .app, .sidebar, .topbar, navegação, main e @media(767/1023/1200/1440)
- Adaptações aprovadas: todas as telas atuais, claro/escuro/sistema preservados; telas futuras nas próximas Features.

<!-- project-slices-child:19b60cef9e054af246cc9ee77739b942f53571e540f6427bdd41eb25ab29067f -->

## Relações

- `#1016113` blocks `#1016117`
