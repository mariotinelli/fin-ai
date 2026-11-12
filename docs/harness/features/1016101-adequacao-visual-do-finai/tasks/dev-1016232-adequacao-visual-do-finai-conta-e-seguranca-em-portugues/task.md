# [DEV] [WEB] [USUARIO] Adequação visual do FinAI - Conta e segurança em português

- Redmine: `#1016232`
- Tipo: `DEV`
- Tracker: Task (`4`)
- Item pai: `#1016101`
- Estimativa: `2h`
- Sequencing: `8`

## Descrição

## Entrega

Traduzir perfil, senha, aparência, exclusão de conta, confirmação de senha, autenticação de dois fatores e chaves de acesso para pt-BR, incluindo seus estados, mensagens e endereços. Manter funcionando os caminhos antigos e integrar a entrada e os retornos das jornadas protegidas.

## Escopo e limites

Esta entrega possui as telas e endpoints atuais de configurações e segurança, incluindo os estados específicos de 2FA e chaves de acesso. Consome a identidade e a navegação comuns sem reimplementá-las. Não alterar credenciais, regras, permissões, expiração ou dados do usuário. /login permanece inalterada.

## Critérios de aceite

- Perfil, alteração de senha, aparência, exclusão, confirmação de senha, configuração/desafio de 2FA e gestão/entrada por chaves de acesso apresentam conteúdo próprio em português, inclusive diálogos, nomes acessíveis, estados vazios, processamento, cancelamento e erros.
- Temas claro/escuro/sistema, escolha e persistência de aparência, validações e resultados das operações permanecem iguais. Tradução de rótulos não altera nome de chave de acesso informado pelo usuário, códigos de recuperação, QR, credenciais ou outros valores exatos.
- URLs principais, links, formulários e chamadas das jornadas desta entrega usam o mapa em português; os endereços antigos continuam realizando as mesmas operações, preservando métodos e parâmetros. Não traduzir endpoints padronizados de protocolo ou infraestrutura.
- Confirmar senha e autenticar por 2FA/chave de acesso mantêm as exigências e restrições atuais. Retomar uma ação protegida conduz ao destino correto em português; erro, cancelamento ou acesso indevido não concluem a ação.
- Requisições enviadas a endpoints antigos continuam funcionais sem perda do método, duplicação de efeitos ou redução dos controles atuais de acesso e tentativas; mensagens próprias de falha permanecem em português.
- Textos próprios permanecem legíveis e operações acessíveis nos temas e nove viewports existentes, com foco e rótulos em português. Diálogos nativos do navegador, sistema e autenticador preservam o controle de idioma desses ambientes.

## Endereços abrangidos

Todos os endereços antigos continuam funcionais, preservando métodos, parâmetros, prazos e proteções. Novos links, formulários, notificações e retornos usam os caminhos principais abaixo; /login permanece igual.

| Endereço atual | Caminho principal |
| --- | --- |
| `/settings` | `/configuracoes` |
| `/settings/profile` | `/configuracoes/perfil` |
| `/settings/password` | `/configuracoes/senha` |
| `/settings/appearance` | `/configuracoes/aparencia` |
| `/settings/two-factor` | `/configuracoes/autenticacao-de-dois-fatores` |
| `/settings/passkeys` | `/configuracoes/chaves-de-acesso` |
| `/two-factor-challenge` | `/desafio-de-dois-fatores` |
| `/user` | `/usuario` |
| `/user/confirm-password` | `/usuario/confirmar-senha` |
| `/user/confirmed-password-status` | `/usuario/status-de-confirmacao-de-senha` |
| `/user/confirmed-two-factor-authentication` | `/usuario/confirmacao-de-autenticacao-de-dois-fatores` |
| `/user/two-factor-authentication` | `/usuario/autenticacao-de-dois-fatores` |
| `/user/two-factor-qr-code` | `/usuario/autenticacao-de-dois-fatores/codigo-qr` |
| `/user/two-factor-secret-key` | `/usuario/autenticacao-de-dois-fatores/chave-secreta` |
| `/user/two-factor-recovery-codes` | `/usuario/autenticacao-de-dois-fatores/codigos-de-recuperacao` |
| `/user/passkeys` | `/usuario/chaves-de-acesso` |
| `/user/passkeys/options` | `/usuario/chaves-de-acesso/opcoes` |
| `/user/passkeys/{passkey}` | `/usuario/chaves-de-acesso/{passkey}` |
| `/passkeys/login` | `/chaves-de-acesso/entrar` |
| `/passkeys/login/options` | `/chaves-de-acesso/entrar/opcoes` |
| `/passkeys/confirm` | `/chaves-de-acesso/confirmar` |
| `/passkeys/confirm/options` | `/chaves-de-acesso/confirmar/opcoes` |

## Dependências

Pode iniciar com o sistema atual. Integrar as jornadas de acesso e segurança e a navegação compartilhada para concluir o aceite conjunto. Esta entrega bloqueia a conclusão de #1016117 — [QA] [WEB] [USUARIO] Adequação visual do FinAI. Preservar a identidade e composição das entregas anteriores.

## Referências

Feature #1016101 — [WEB] [USUARIO] Adequação visual do FinAI; R2, R8–R11 e CA12–CA16; docs/harness/features/1016101-adequacao-visual-do-finai/feature.md.

- conversation-input-003 — sources/conversation-input-003.md; idioma, URLs, compatibilidade e exceção /login.
- conversation-input-004 — sources/conversation-input-004.md; estimativas corrigidas para2h e cobertura das configurações.

<!-- project-slices-change-review:1223d205919faaa1c0b7b47343616f4b700c4b6d440e8b1c01926f80243f3e01 -->

[project-slices-revision:1223d205919faaa1c0b7b47343616f4b700c4b6d440e8b1c01926f80243f3e01:create-dev-translation-security-001]

## Relações

- `#1016232` blocks `#1016117`
