# [DEV] [WEB] [USUARIO] Acesso à conta pessoal - Recuperação de senha com nova tentativa

- Redmine: `#1016121`
- Tipo: `DEV`
- Tracker: Task (`4`)
- Item pai: `#1016104`
- Estimativa: `2h`

## Descrição

## Entrega

Completar os estados de recuperação quando o envio falhar ou o link de redefinição for inválido, expirado ou já usado. O pedido genérico e o broker já existem; falta retomada sem apresentar envio ou alteração como concluídos indevidamente.

## Escopo e limites

Responsável pela solicitação/redefinição esquecida e seus novos pedidos. Preservar resposta genérica, validade de 60 minutos, uso único, retorno ao login e estado de confirmação do e-mail. Não reimplementar a política de senha nem ampliar autenticação.

## Critérios de aceite

- Com envio disponível, pedir recuperação para conta existente ou inexistente mantém a mesma resposta genérica; o titular cadastrado recebe o link.
- Falha no envio orienta nova tentativa sem afirmar sucesso ou revelar explicitamente existência da conta; depois de restabelecer, novo pedido permite receber link utilizável.
- Link inválido, expirado após 60 minutos ou já utilizado não altera senha e oferece novo pedido; novo link válido permite retomar.
- Link próprio, não usado e válido, com senha conforme a política compartilhada e confirmação igual, redefine e retorna ao login; senha nova funciona e a anterior não permite novos logins.
- Redefinir conta não confirmada não confirma e-mail nem libera a área do produto; preservar validações e erros, sem alteração indevida.
- Nas telas e estados alterados, consumir marca, tipografia, paleta, campos, botões, erros e feedback da base FinAI em computador, tablet e celular, nos temas claro, escuro e acompanhar o sistema, sem reconstruir identidade ou layouts do fornecedor.

## Dependências

Início bloqueado pelo aceite integrado [QA] [WEB] [USUARIO] Adequação visual do FinAI (#1016117), dependente dos cinco DEV visuais e representante da base implementada e verificada. Pode iniciar com a recuperação existente após a liberação visual. Para concluir a redefinição integrada, usar Cadastro e redefinição com política de senha consistente. Login, saída e confirmação seguem nas jornadas existentes/entrega responsável, sem bloqueio interno de início.

## Referências

Item pai Redmine #1016104; regras/critérios R2, R3, R4, R5, R8, CA2, CA8, CA9, CA10, CA11, CA11-Recuperacao, R9, CA12.

- design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; referência clara e adaptações aprovadas na Feature visual #1016101; linguagem de formulários, mensagens e ações de retomada. Não há composição própria de acesso no ZIP.
- Fornecedor de composição: [DEV] [WEB] [USUARIO] Adequação visual do FinAI - Página inicial e jornadas de acesso (#1016114); aceite integrado: [QA] [WEB] [USUARIO] Adequação visual do FinAI (#1016117).

<!-- project-slices-child:bd2fc0acd7b807c6b0d262d31b0d76dea8d6393fdab9c405982b0f7df7b95456 -->

## Relações

- `#1016121` blocks `#1016122`
