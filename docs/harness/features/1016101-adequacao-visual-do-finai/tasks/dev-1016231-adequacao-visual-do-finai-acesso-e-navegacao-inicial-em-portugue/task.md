# [DEV] [WEB] [USUARIO] Adequação visual do FinAI - Acesso e navegação inicial em português

- Redmine: `#1016231`
- Tipo: `DEV`
- Tracker: Task (`4`)
- Item pai: `#1016101`
- Estimativa: `2h`
- Sequencing: `7`

## Descrição

## Entrega

Traduzir a página pública, painel e navegação compartilhada, cadastro, login, recuperação/redefinição e verificação de e-mail para pt-BR. Apresentar as URLs próprias dessas jornadas em português, mantendo /login e a compatibilidade dos caminhos e e-mails antigos.

## Escopo e limites

Esta entrega possui os textos e caminhos das jornadas iniciais, do painel e da navegação comum. A entrada alternativa por chave de acesso mantém seu encaixe no login; endpoints e estados próprios de chaves de acesso e 2FA pertencem à entrega Conta e segurança em português. Reutilizar o backend já em pt_BR. Preservar dados, operações, campos, regras e layout.

## Critérios de aceite

- Página pública, painel, menus comuns, breadcrumbs, títulos de documento, cadastro e telas de acesso/recuperação/verificação apresentam textos, placeholders, botões, feedback, tooltips e nomes acessíveis próprios em português brasileiro.
- E-mails e mensagens próprias de recuperação e verificação estão em português; dados válidos e inválidos mantêm os mesmos efeitos, validações e restrições. Não alterar dados informados pelos usuários nem marcas.
- Links, formulários, comunicações novas e retornos dessas jornadas usam os caminhos em português do mapa; /login e a página inicial permanecem nos mesmos endereços. Preservar os parâmetros e os valores transportados.
- Todos os caminhos anteriores desta entrega continuam funcionais. E-mails antigos válidos de recuperação/verificação continuam utilizáveis até o prazo original; tokens ou assinaturas inválidos, adulterados ou expirados continuam recusados, sem duplicar operações.
- Navegação, envio de formulários e retomada após autenticação mantêm métodos, acesso e resultados. A tradução não enfraquece restrições de visitante/usuário autenticado nem exigências de verificação existentes.
- Textos traduzidos permanecem legíveis e ações acessíveis no claro, escuro e sistema e nos nove viewports já aprovados; não substituir a composição compartilhada nem introduzir corte, sobreposição ou rolagem horizontal.

## Endereços abrangidos

Todos os endereços antigos continuam funcionais, preservando métodos, parâmetros, prazos e proteções. Novos links, formulários, notificações e retornos usam os caminhos principais abaixo; /login permanece igual.

| Endereço atual | Caminho principal |
| --- | --- |
| `/` | `/` |
| `/login` | `/login` |
| `/dashboard` | `/painel` |
| `/register` | `/cadastro` |
| `/logout` | `/sair` |
| `/forgot-password` | `/recuperar-senha` |
| `/reset-password` | `/redefinir-senha` |
| `/reset-password/{token}` | `/redefinir-senha/{token}` |
| `/verify-email` | `/verificar-email` |
| `/verify-email/{id}/{hash}` | `/verificar-email/{id}/{hash}` |
| `/email/verification-notification` | `/email/notificacao-de-verificacao` |

## Dependências

Pode iniciar com o sistema atual. Integrar as jornadas de acesso e segurança e a navegação compartilhada para concluir o aceite conjunto. Esta entrega bloqueia a conclusão de #1016117 — [QA] [WEB] [USUARIO] Adequação visual do FinAI. Preservar a identidade e composição das entregas anteriores.

## Referências

Feature #1016101 — [WEB] [USUARIO] Adequação visual do FinAI; R2, R8–R11 e CA12–CA16; docs/harness/features/1016101-adequacao-visual-do-finai/feature.md.

- conversation-input-003 — sources/conversation-input-003.md; idioma, URLs, compatibilidade e exceção /login.
- conversation-input-004 — sources/conversation-input-004.md; estimativas corrigidas para2h e cobertura das configurações.

<!-- project-slices-change-review:1223d205919faaa1c0b7b47343616f4b700c4b6d440e8b1c01926f80243f3e01 -->

[project-slices-revision:1223d205919faaa1c0b7b47343616f4b700c4b6d440e8b1c01926f80243f3e01:create-dev-translation-access-001]

## Relações

- `#1016231` blocks `#1016117`
