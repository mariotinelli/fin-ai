# Aplicação da revisão aprovada

Revisão semântica: `1223d205919faaa1c0b7b47343616f4b700c4b6d440e8b1c01926f80243f3e01`

## Impacto concreto


## Sequencing

- Projeto/versão: 65224/20355
- Campo: Sequencing (ID 2)
- Bloco: 1–9
- Pai: 1

- dev-1: 1
- dev-2: 2
- dev-3: 3
- dev-4: 4
- dev-5: 5
- dev-layout-revision-001: 6
- dev-translation-access: 7
- dev-translation-security: 8
- qa: 9

### Atualizações de numeração

- #1016134: 23 → 25
- #1016133: 22 → 24
- #1016132: 21 → 23
- #1016131: 20 → 22
- #1016130: 19 → 21
- #1016129: 18 → 20
- #1016107: 18 → 20
- #1016128: 17 → 19
- #1016127: 16 → 18
- #1016106: 16 → 18
- #1016126: 15 → 17
- #1016125: 14 → 16
- #1016124: 13 → 15
- #1016123: 12 → 14
- #1016105: 12 → 14
- #1016122: 11 → 13
- #1016121: 10 → 12
- #1016120: 9 → 11
- #1016119: 8 → 10
- #1016104: 8 → 10
- #1016117: 7 → 9

- **create-dev-translation-access-001** — `create` em nova tarefa
  - Motivo: Tradução e URLs aprovadas como complemento, preservando as tarefas e critérios anteriores.
  - Impactos: dev-1, dev-2, dev-3

```json
{
  "project_id": 65224,
  "parent_issue_id": 1016101,
  "tracker_id": 4,
  "status_id": 1,
  "priority_id": 4,
  "fixed_version_id": 20355,
  "subject": "[DEV] [WEB] [USUARIO] Adequação visual do FinAI - Acesso e navegação inicial em português",
  "description": "## Entrega\n\nTraduzir a página pública, painel e navegação compartilhada, cadastro, login, recuperação/redefinição e verificação de e-mail para pt-BR. Apresentar as URLs próprias dessas jornadas em português, mantendo /login e a compatibilidade dos caminhos e e-mails antigos.\n\n## Escopo e limites\n\nEsta entrega possui os textos e caminhos das jornadas iniciais, do painel e da navegação comum. A entrada alternativa por chave de acesso mantém seu encaixe no login; endpoints e estados próprios de chaves de acesso e 2FA pertencem à entrega Conta e segurança em português. Reutilizar o backend já em pt_BR. Preservar dados, operações, campos, regras e layout.\n\n## Critérios de aceite\n\n- Página pública, painel, menus comuns, breadcrumbs, títulos de documento, cadastro e telas de acesso/recuperação/verificação apresentam textos, placeholders, botões, feedback, tooltips e nomes acessíveis próprios em português brasileiro.\n- E-mails e mensagens próprias de recuperação e verificação estão em português; dados válidos e inválidos mantêm os mesmos efeitos, validações e restrições. Não alterar dados informados pelos usuários nem marcas.\n- Links, formulários, comunicações novas e retornos dessas jornadas usam os caminhos em português do mapa; /login e a página inicial permanecem nos mesmos endereços. Preservar os parâmetros e os valores transportados.\n- Todos os caminhos anteriores desta entrega continuam funcionais. E-mails antigos válidos de recuperação/verificação continuam utilizáveis até o prazo original; tokens ou assinaturas inválidos, adulterados ou expirados continuam recusados, sem duplicar operações.\n- Navegação, envio de formulários e retomada após autenticação mantêm métodos, acesso e resultados. A tradução não enfraquece restrições de visitante/usuário autenticado nem exigências de verificação existentes.\n- Textos traduzidos permanecem legíveis e ações acessíveis no claro, escuro e sistema e nos nove viewports já aprovados; não substituir a composição compartilhada nem introduzir corte, sobreposição ou rolagem horizontal.\n\n## Endereços abrangidos\n\nTodos os endereços antigos continuam funcionais, preservando métodos, parâmetros, prazos e proteções. Novos links, formulários, notificações e retornos usam os caminhos principais abaixo; /login permanece igual.\n\n| Endereço atual | Caminho principal |\n| --- | --- |\n| `/` | `/` |\n| `/login` | `/login` |\n| `/dashboard` | `/painel` |\n| `/register` | `/cadastro` |\n| `/logout` | `/sair` |\n| `/forgot-password` | `/recuperar-senha` |\n| `/reset-password` | `/redefinir-senha` |\n| `/reset-password/{token}` | `/redefinir-senha/{token}` |\n| `/verify-email` | `/verificar-email` |\n| `/verify-email/{id}/{hash}` | `/verificar-email/{id}/{hash}` |\n| `/email/verification-notification` | `/email/notificacao-de-verificacao` |\n\n## Dependências\n\nPode iniciar com o sistema atual. Integrar as jornadas de acesso e segurança e a navegação compartilhada para concluir o aceite conjunto. Esta entrega bloqueia a conclusão de #1016117 — [QA] [WEB] [USUARIO] Adequação visual do FinAI. Preservar a identidade e composição das entregas anteriores.\n\n## Referências\n\nFeature #1016101 — [WEB] [USUARIO] Adequação visual do FinAI; R2, R8–R11 e CA12–CA16; docs/harness/features/1016101-adequacao-visual-do-finai/feature.md.\n\n- conversation-input-003 — sources/conversation-input-003.md; idioma, URLs, compatibilidade e exceção /login.\n- conversation-input-004 — sources/conversation-input-004.md; estimativas corrigidas para2h e cobertura das configurações.\n\n<!-- project-slices-change-review:1223d205919faaa1c0b7b47343616f4b700c4b6d440e8b1c01926f80243f3e01 -->",
  "estimated_hours": 2,
  "custom_fields": [
    {
      "id": 2,
      "value": "7"
    }
  ]
}
```

- **create-dev-translation-security-001** — `create` em nova tarefa
  - Motivo: Tradução e URLs aprovadas como complemento, preservando as tarefas e critérios anteriores.
  - Impactos: dev-4, dev-5

```json
{
  "project_id": 65224,
  "parent_issue_id": 1016101,
  "tracker_id": 4,
  "status_id": 1,
  "priority_id": 4,
  "fixed_version_id": 20355,
  "subject": "[DEV] [WEB] [USUARIO] Adequação visual do FinAI - Conta e segurança em português",
  "description": "## Entrega\n\nTraduzir perfil, senha, aparência, exclusão de conta, confirmação de senha, autenticação de dois fatores e chaves de acesso para pt-BR, incluindo seus estados, mensagens e endereços. Manter funcionando os caminhos antigos e integrar a entrada e os retornos das jornadas protegidas.\n\n## Escopo e limites\n\nEsta entrega possui as telas e endpoints atuais de configurações e segurança, incluindo os estados específicos de 2FA e chaves de acesso. Consome a identidade e a navegação comuns sem reimplementá-las. Não alterar credenciais, regras, permissões, expiração ou dados do usuário. /login permanece inalterada.\n\n## Critérios de aceite\n\n- Perfil, alteração de senha, aparência, exclusão, confirmação de senha, configuração/desafio de 2FA e gestão/entrada por chaves de acesso apresentam conteúdo próprio em português, inclusive diálogos, nomes acessíveis, estados vazios, processamento, cancelamento e erros.\n- Temas claro/escuro/sistema, escolha e persistência de aparência, validações e resultados das operações permanecem iguais. Tradução de rótulos não altera nome de chave de acesso informado pelo usuário, códigos de recuperação, QR, credenciais ou outros valores exatos.\n- URLs principais, links, formulários e chamadas das jornadas desta entrega usam o mapa em português; os endereços antigos continuam realizando as mesmas operações, preservando métodos e parâmetros. Não traduzir endpoints padronizados de protocolo ou infraestrutura.\n- Confirmar senha e autenticar por 2FA/chave de acesso mantêm as exigências e restrições atuais. Retomar uma ação protegida conduz ao destino correto em português; erro, cancelamento ou acesso indevido não concluem a ação.\n- Requisições enviadas a endpoints antigos continuam funcionais sem perda do método, duplicação de efeitos ou redução dos controles atuais de acesso e tentativas; mensagens próprias de falha permanecem em português.\n- Textos próprios permanecem legíveis e operações acessíveis nos temas e nove viewports existentes, com foco e rótulos em português. Diálogos nativos do navegador, sistema e autenticador preservam o controle de idioma desses ambientes.\n\n## Endereços abrangidos\n\nTodos os endereços antigos continuam funcionais, preservando métodos, parâmetros, prazos e proteções. Novos links, formulários, notificações e retornos usam os caminhos principais abaixo; /login permanece igual.\n\n| Endereço atual | Caminho principal |\n| --- | --- |\n| `/settings` | `/configuracoes` |\n| `/settings/profile` | `/configuracoes/perfil` |\n| `/settings/password` | `/configuracoes/senha` |\n| `/settings/appearance` | `/configuracoes/aparencia` |\n| `/settings/two-factor` | `/configuracoes/autenticacao-de-dois-fatores` |\n| `/settings/passkeys` | `/configuracoes/chaves-de-acesso` |\n| `/two-factor-challenge` | `/desafio-de-dois-fatores` |\n| `/user` | `/usuario` |\n| `/user/confirm-password` | `/usuario/confirmar-senha` |\n| `/user/confirmed-password-status` | `/usuario/status-de-confirmacao-de-senha` |\n| `/user/confirmed-two-factor-authentication` | `/usuario/confirmacao-de-autenticacao-de-dois-fatores` |\n| `/user/two-factor-authentication` | `/usuario/autenticacao-de-dois-fatores` |\n| `/user/two-factor-qr-code` | `/usuario/autenticacao-de-dois-fatores/codigo-qr` |\n| `/user/two-factor-secret-key` | `/usuario/autenticacao-de-dois-fatores/chave-secreta` |\n| `/user/two-factor-recovery-codes` | `/usuario/autenticacao-de-dois-fatores/codigos-de-recuperacao` |\n| `/user/passkeys` | `/usuario/chaves-de-acesso` |\n| `/user/passkeys/options` | `/usuario/chaves-de-acesso/opcoes` |\n| `/user/passkeys/{passkey}` | `/usuario/chaves-de-acesso/{passkey}` |\n| `/passkeys/login` | `/chaves-de-acesso/entrar` |\n| `/passkeys/login/options` | `/chaves-de-acesso/entrar/opcoes` |\n| `/passkeys/confirm` | `/chaves-de-acesso/confirmar` |\n| `/passkeys/confirm/options` | `/chaves-de-acesso/confirmar/opcoes` |\n\n## Dependências\n\nPode iniciar com o sistema atual. Integrar as jornadas de acesso e segurança e a navegação compartilhada para concluir o aceite conjunto. Esta entrega bloqueia a conclusão de #1016117 — [QA] [WEB] [USUARIO] Adequação visual do FinAI. Preservar a identidade e composição das entregas anteriores.\n\n## Referências\n\nFeature #1016101 — [WEB] [USUARIO] Adequação visual do FinAI; R2, R8–R11 e CA12–CA16; docs/harness/features/1016101-adequacao-visual-do-finai/feature.md.\n\n- conversation-input-003 — sources/conversation-input-003.md; idioma, URLs, compatibilidade e exceção /login.\n- conversation-input-004 — sources/conversation-input-004.md; estimativas corrigidas para2h e cobertura das configurações.\n\n<!-- project-slices-change-review:1223d205919faaa1c0b7b47343616f4b700c4b6d440e8b1c01926f80243f3e01 -->",
  "estimated_hours": 2,
  "custom_fields": [
    {
      "id": 2,
      "value": "8"
    }
  ]
}
```

- **update-translation-qa-estimate-001** — `update` em New (#1016117)
  - Motivo: alteração localizada aprovada
  - Impactos: qa

```json
{
  "estimated_hours": 2
}
```

- **relation-dev-translation-access-qa-001** — `relation-add` em nova tarefa
  - Motivo: A tradução da jornada deve ser concluída para finalizar a QA integrada.
  - Impactos: blocks:dev-3:qa

```json
{
  "issue_id": "dev-translation-access",
  "issue_to_id": 1016117,
  "relation_type": "blocks"
}
```

- **relation-dev-translation-security-qa-001** — `relation-add` em nova tarefa
  - Motivo: A tradução da jornada deve ser concluída para finalizar a QA integrada.
  - Impactos: blocks:dev-4:qa, blocks:dev-5:qa

```json
{
  "issue_id": "dev-translation-security",
  "issue_to_id": 1016117,
  "relation_type": "blocks"
}
```

## Condições de teste

QA: #1016117
Arquivo: [condicoes-teste-r004.docx](file:///C:/Users/maari/Herd/github/fin-ai/docs/harness/features/1016101-adequacao-visual-do-finai/slices/condicoes-teste-r004.docx)
SHA-256: `4dd935464d9247f1c5dfe7d5c80085017c1cb8d71ece726b53b62d7df517384f`
Descrição do anexo: Condições de teste — revisão 004

Nota de vigência:

Condições de teste vigentes: revisão 004, arquivo condicoes-teste-r004.docx.
SHA-256: 4dd935464d9247f1c5dfe7d5c80085017c1cb8d71ece726b53b62d7df517384f
[project-slices-conditions:1016117:4:4dd935464d9247f1c5dfe7d5c80085017c1cb8d71ece726b53b62d7df517384f]


Tarefas concluídas permanecem imutáveis. Relações e filhas fora do delta permanecem preservadas.


## Resultado conferido

Publicação concluída: #1016231 (2h, Sequencing7), #1016232 (2h, Sequencing8), QA #1016117 (2h, Sequencing9), bloqueios #874/#875 e documento revisão004 com35 condições, anexo3317 e nota91127. Posições1–6, tarefas encerradas e documentos anteriores preservados;21 deslocamentos de numeração conferidos. Total das três estimativas:6h.
