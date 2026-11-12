# [DEV] [WEB] [USUARIO] Adequação visual do FinAI - Atualização do layout desktop, tablet e celular

- Redmine: `#1016204`
- Tipo: `DEV`
- Tracker: Task (`4`)
- Item pai: `#1016101`
- Estimativa: `3h`
- Sequencing: `6`

## Descrição

## Entrega

Atualizar a estrutura compartilhada da área autenticada ao design revisado: barra inferior no celular, navegação lateral compacta no tablet e conteúdo contornado no desktop e tablet. O layout atual usa navegação superior nas larguras menores; marca, identidade, temas e operações já existem e serão preservados.

## Escopo e limites

Abrange a navegação e a estrutura compartilhadas do dashboard atual e das configurações existentes. Preservar os campos e ações de cada página; a composição específica das jornadas de acesso, perfil e segurança permanece nas tarefas responsáveis. Usar apenas os destinos atualmente implementados. A alteração não antecipa páginas, operações ou controles financeiros do protótipo.

## Critérios de aceite

- Até 767px, apresentar a marca no topo e a navegação principal fixa na base, em largura total, com 56px mais a área segura inferior; ícones de 24px, alvos de pelo menos 44px, sem legenda visual e com nomes acessíveis, indicação do destino ativo e foco visível.
- De 768 a 1024px inclusive, apresentar navegação lateral compacta de 72px mais a área segura lateral, marca compacta e alvos de pelo menos 48px, com conteúdo ao lado e sem barra inferior. A lateral acompanha a altura disponível e permite acessar seus controles mesmo com pouco espaço vertical.
- A partir de 1025px, manter a navegação lateral desktop e seu recolhimento atual. A partir de 768px, comparar com o novo design o entorno contínuo, o conteúdo com contorno de 1px, raio de 16px, margem de 8px e cabeçalho transparente, preservando a geometria e os espaçamentos aplicáveis da referência.
- Navegar nos destinos atuais e acessar menu da conta, configurações, links e saída em todas as larguras, inclusive por teclado. Preservar restrições de acesso, campos, validações e resultados das ações existentes; adaptar a apresentação dos controles que o protótipo oculta, mantendo-os disponíveis.
- Rolar até o fim da página, focar campos e ações e abrir menus e diálogos sem a barra inferior encobrir conteúdo, mensagens, controles ou foco. Respeitar as áreas seguras do dispositivo e evitar rolagem horizontal da página.
- Preservar a identidade pronta e os temas claro, escuro e acompanhar o sistema, sua preferência persistida e a reação à mudança do dispositivo apenas em sistema. Manter estados ativo, hover, foco, desabilitado e carregamento aplicáveis.
- Conferir o layout nas telas autenticadas atuais em 360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080, nos temas claro e escuro. Verificar também 767/768px e 1024/1025px ao redimensionar após recolher a navegação desktop, mantendo acesso aos controles e aplicação do modo correto.
- O dashboard atual mantém seu conteúdo e sua finalidade, sem novos destinos ou dados financeiros demonstrativos, rótulos de armazenamento apenas local ou assistente simulado.

## Dependências

Pode iniciar com a identidade e estrutura existentes das tarefas #1016112 — Identidade e temas no painel atual e #1016113 — Estrutura e navegação responsiva atuais, ambas encerradas. Integrar a nova estrutura às páginas atuais sem alterar a responsabilidade de #1016114 — Página inicial e jornadas de acesso, #1016115 — Perfil, senha e aparência e #1016116 — Dois fatores e passkeys. A conclusão desta entrega é necessária para finalizar #1016117 — [QA] [WEB] [USUARIO] Adequação visual do FinAI.

## Referências

Feature #1016101 — [WEB] [USUARIO] Adequação visual do FinAI; R2, R3, R4, R5, R6, R7, CA2, CA3, CA4, CA5, CA6, CA7, CA8, CA9, CA10 e CA11 do requisito aprovado.

- design-input-002 — docs/harness/features/1016101-adequacao-visual-do-finai/sources/design-input-002.md; index.html, regras finais responsivas, .sidebar, .sidebar nav, .workspace, .topbar e áreas seguras.
- design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; paleta, tipografia e demais componentes preservados.
- conversation-input-002 — docs/harness/features/1016101-adequacao-visual-do-finai/sources/conversation-input-002.md; solicitação de complemento e esclarecimento de tablet.


<!-- project-slices-change-review:c45d623d1d604562cbf782d40089d17185ad695169c9da7171e3ddeca4a2f63c -->

[project-slices-revision:c45d623d1d604562cbf782d40089d17185ad695169c9da7171e3ddeca4a2f63c:create-layout-revision-001]

## Relações

- `#1016204` blocks `#1016117`
