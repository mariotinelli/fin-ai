# [DEV] [WEB] [USUARIO] Adequação visual do FinAI - Página inicial e jornadas de acesso

- Redmine: `#1016114`
- Tipo: `DEV`
- Tracker: Task (`4`)
- Item pai: `#1016101`
- Estimativa: `2h`

## Descrição

## Entrega

Adequar a página pública atual e as telas de cadastro, login, solicitação de recuperação, redefinição e confirmação de e-mail à identidade FinAI, preservando seu conteúdo funcional e suas ações. Aplicar a linguagem de formulário da referência onde não existe composição própria dessas telas.

## Escopo e limites

A composição e estados destas páginas pertencem a esta entrega. Preservar a presença/encaixe da entrada por passkey no login; os estados próprios de passkeys, 2FA e confirmação de senha pertencem a Dois fatores e passkeys. Não alterar políticas de acesso, campos, validações ou mensagens funcionais.

## Critérios de aceite

- Página pública, cadastro, login, recuperação, redefinição e verificação de e-mail apresentam marca, títulos, campos, botões, links e espaçamento coerentes com FinAI, sem identidade visual genérica do starter.
- As telas sem composição própria do ZIP usam a mesma linguagem visual, preservando campos, finalidade e destinos.
- Com dados válidos e inválidos, estados de processamento, mensagens de erro/sucesso e reenvio, manter o comportamento funcional existente e aplicar o visual correspondente.
- Os caminhos de cadastro/login/recuperação/retorno e a presença das alternativas atuais de autenticação continuam disponíveis; visitantes e autenticados mantêm as restrições atuais.
- Conferir as páginas nos temas claro e escuro integrados à base; o modo sistema continua utilizando a preferência vigente.
- Nas superfícies desta entrega, conferir os nove viewports (360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080), temas claro e escuro, estados aplicáveis e ausência de rolagem horizontal da página; manter acesso às ações atuais, rótulos e foco visível.

## Dependências

Pode iniciar a composição das páginas atuais. Para concluir, integrar Identidade e temas no painel atual e, onde houver navegação autenticada, Estrutura e navegação responsiva atuais. Integrar o encaixe da entrada por passkey com Dois fatores e passkeys, sem relação nativa de bloqueio de início.

## Referências

Item pai Redmine #1016101; regras/critérios R1, R2, R3, R5, R6, CA1, CA2, CA5, CA6, CA7, CA8, V-Publica, V-Acesso.

- design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; .brand, títulos, campos, botões e mensagens do index.html; adaptação aprovada para página inicial e telas de acesso sem desenho específico
- Adaptações aprovadas: todas as telas atuais, claro/escuro/sistema preservados; telas futuras nas próximas Features.

<!-- project-slices-child:33e135b9ae4f883e40abc7699ce25cb1fbc9c8619a3abe35eccae6a90f1eb2f1 -->

## Relações

- `#1016114` blocks `#1016117`
