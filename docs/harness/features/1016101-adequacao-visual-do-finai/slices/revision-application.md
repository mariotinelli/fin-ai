# Aplicação da revisão aprovada

Revisão semântica: `c45d623d1d604562cbf782d40089d17185ad695169c9da7171e3ddeca4a2f63c`

## Impacto concreto

- **create-layout-revision-001** — `create` em nova tarefa
  - Motivo: Novo design aprovado após conclusão da entrega original de estrutura; complemento sem alterar a tarefa encerrada.
  - Impactos: dev-2

```json
{
  "project_id": 65224,
  "parent_issue_id": 1016101,
  "tracker_id": 4,
  "status_id": 1,
  "priority_id": 4,
  "fixed_version_id": 20355,
  "subject": "[DEV] [WEB] [USUARIO] Adequação visual do FinAI - Atualização do layout desktop, tablet e celular",
  "description": "## Entrega\n\nAtualizar a estrutura compartilhada da área autenticada ao design revisado: barra inferior no celular, navegação lateral compacta no tablet e conteúdo contornado no desktop e tablet. O layout atual usa navegação superior nas larguras menores; marca, identidade, temas e operações já existem e serão preservados.\n\n## Escopo e limites\n\nAbrange a navegação e a estrutura compartilhadas do dashboard atual e das configurações existentes. Preservar os campos e ações de cada página; a composição específica das jornadas de acesso, perfil e segurança permanece nas tarefas responsáveis. Usar apenas os destinos atualmente implementados. A alteração não antecipa páginas, operações ou controles financeiros do protótipo.\n\n## Critérios de aceite\n\n- Até 767px, apresentar a marca no topo e a navegação principal fixa na base, em largura total, com 56px mais a área segura inferior; ícones de 24px, alvos de pelo menos 44px, sem legenda visual e com nomes acessíveis, indicação do destino ativo e foco visível.\n- De 768 a 1024px inclusive, apresentar navegação lateral compacta de 72px mais a área segura lateral, marca compacta e alvos de pelo menos 48px, com conteúdo ao lado e sem barra inferior. A lateral acompanha a altura disponível e permite acessar seus controles mesmo com pouco espaço vertical.\n- A partir de 1025px, manter a navegação lateral desktop e seu recolhimento atual. A partir de 768px, comparar com o novo design o entorno contínuo, o conteúdo com contorno de 1px, raio de 16px, margem de 8px e cabeçalho transparente, preservando a geometria e os espaçamentos aplicáveis da referência.\n- Navegar nos destinos atuais e acessar menu da conta, configurações, links e saída em todas as larguras, inclusive por teclado. Preservar restrições de acesso, campos, validações e resultados das ações existentes; adaptar a apresentação dos controles que o protótipo oculta, mantendo-os disponíveis.\n- Rolar até o fim da página, focar campos e ações e abrir menus e diálogos sem a barra inferior encobrir conteúdo, mensagens, controles ou foco. Respeitar as áreas seguras do dispositivo e evitar rolagem horizontal da página.\n- Preservar a identidade pronta e os temas claro, escuro e acompanhar o sistema, sua preferência persistida e a reação à mudança do dispositivo apenas em sistema. Manter estados ativo, hover, foco, desabilitado e carregamento aplicáveis.\n- Conferir o layout nas telas autenticadas atuais em 360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080, nos temas claro e escuro. Verificar também 767/768px e 1024/1025px ao redimensionar após recolher a navegação desktop, mantendo acesso aos controles e aplicação do modo correto.\n- O dashboard atual mantém seu conteúdo e sua finalidade, sem novos destinos ou dados financeiros demonstrativos, rótulos de armazenamento apenas local ou assistente simulado.\n\n## Dependências\n\nPode iniciar com a identidade e estrutura existentes das tarefas #1016112 — Identidade e temas no painel atual e #1016113 — Estrutura e navegação responsiva atuais, ambas encerradas. Integrar a nova estrutura às páginas atuais sem alterar a responsabilidade de #1016114 — Página inicial e jornadas de acesso, #1016115 — Perfil, senha e aparência e #1016116 — Dois fatores e passkeys. A conclusão desta entrega é necessária para finalizar #1016117 — [QA] [WEB] [USUARIO] Adequação visual do FinAI.\n\n## Referências\n\nFeature #1016101 — [WEB] [USUARIO] Adequação visual do FinAI; R2, R3, R4, R5, R6, R7, CA2, CA3, CA4, CA5, CA6, CA7, CA8, CA9, CA10 e CA11 do requisito aprovado.\n\n- design-input-002 — docs/harness/features/1016101-adequacao-visual-do-finai/sources/design-input-002.md; index.html, regras finais responsivas, .sidebar, .sidebar nav, .workspace, .topbar e áreas seguras.\n- design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; paleta, tipografia e demais componentes preservados.\n- conversation-input-002 — docs/harness/features/1016101-adequacao-visual-do-finai/sources/conversation-input-002.md; solicitação de complemento e esclarecimento de tablet.\n\n\n<!-- project-slices-change-review:c45d623d1d604562cbf782d40089d17185ad695169c9da7171e3ddeca4a2f63c -->",
  "estimated_hours": 3,
  "custom_fields": [
    {
      "id": 2,
      "value": "6"
    }
  ]
}
```

- **update-layout-qa-estimate-001** — `update` em New (#1016117)
  - Motivo: alteração localizada aprovada
  - Impactos: qa

```json
{
  "estimated_hours": 2.25
}
```

- **relation-layout-qa-001** — `relation-add` em nova tarefa
  - Motivo: A revisão do layout compartilhado deve estar concluída para finalizar a QA integrada da Feature.
  - Impactos: blocks:dev-2:qa

```json
{
  "issue_id": "dev-layout-revision-001",
  "issue_to_id": 1016117,
  "relation_type": "blocks"
}
```

## Condições de teste

QA: #1016117
Arquivo: [condicoes-teste-r003.docx](file:///C:/Users/maari/Herd/github/fin-ai/docs/harness/features/1016101-adequacao-visual-do-finai/slices/condicoes-teste-r003.docx)
SHA-256: `f278e8d71ed37226e4b92f4377bf27585508e742eaad690e955d3ca181418b04`
Descrição do anexo: Condições de teste — revisão 003

Nota de vigência:

Condições de teste vigentes: revisão 003, arquivo condicoes-teste-r003.docx.
SHA-256: f278e8d71ed37226e4b92f4377bf27585508e742eaad690e955d3ca181418b04
[project-slices-conditions:1016117:3:f278e8d71ed37226e4b92f4377bf27585508e742eaad690e955d3ca181418b04]


Tarefas concluídas permanecem imutáveis. Relações e filhas fora do delta permanecem preservadas.


## Sequencing

- Projeto/versão: 65224/20355
- Campo: Sequencing (ID 2)
- Bloco: 1–7
- Pai: 1

- dev-1: 1
- dev-2: 2
- dev-3: 3
- dev-4: 4
- dev-5: 5
- dev-layout-revision-001: 6
- qa: 7

### Atualizações de numeração

- #1016134: 22 → 23
- #1016133: 21 → 22
- #1016132: 20 → 21
- #1016131: 19 → 20
- #1016130: 18 → 19
- #1016129: 17 → 18
- #1016107: 17 → 18
- #1016128: 16 → 17
- #1016127: 15 → 16
- #1016106: 15 → 16
- #1016126: 14 → 15
- #1016125: 13 → 14
- #1016124: 12 → 13
- #1016123: 11 → 12
- #1016105: 11 → 12
- #1016122: 10 → 11
- #1016121: 9 → 10
- #1016120: 8 → 9
- #1016119: 7 → 8
- #1016104: 7 → 8
- #1016117: 6 → 7


Autorização: Mário Tinelli aprovou nesta conversa a publicação e a proposta Sequencing6 para nova DEV,7 para QA e deslocamento das posições7–22 para8–23. Históricos das21 issues deslocadas confirmam New e ausência de início; as duas Closed e posições1–5 ficam intactas. Os esquemas e payloads históricos v2 permanecem preservados; esta revisão registra a numeração atual aprovada.


## Resultado conferido

Publicação concluída: DEV #1016204 (3h, Sequencing6), QA #1016117 (2,25h, Sequencing7), relação de bloqueio #873 e anexo3305 com condições revisão003. As21 alterações de numeração foram lidas e conferidas; posições1–5 e tarefas encerradas preservadas. Documento anterior e relações existentes mantidos. Estados de aplicação e condições completed.
