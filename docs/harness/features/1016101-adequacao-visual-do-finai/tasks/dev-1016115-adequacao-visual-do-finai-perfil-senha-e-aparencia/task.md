# [DEV] [WEB] [USUARIO] Adequação visual do FinAI - Perfil, senha e aparência

- Redmine: `#1016115`
- Tipo: `DEV`
- Tracker: Task (`4`)
- Item pai: `#1016101`
- Estimativa: `2h`

## Descrição

## Entrega

Adequar perfil, alteração de senha, preferência de aparência e o diálogo atual de exclusão da conta à identidade FinAI. Reutilizar as operações e os componentes atuais, preservando validações, feedback e confirmação/cancelamento.

## Escopo e limites

Não alterar dados, regras de senha, permissões ou o efeito de exclusão. Esta entrega possui a composição das páginas de perfil/senha/aparência; o mecanismo e a aparência compartilhada dos temas vêm de Identidade e temas no painel atual.

## Critérios de aceite

- Perfil, formulário de senha, página de aparência e diálogo de exclusão usam a paleta, tipografia, hierarquia, campos, botões, erros e superfícies FinAI.
- Alterar perfil e senha com entradas válidas/inválidas mantém resultados e mensagens funcionais; avisos de verificação de e-mail e reenvio presentes no perfil permanecem quando aplicáveis.
- Excluir a conta continua exigindo a confirmação existente; cancelar/fechar preserva a conta; erro e sucesso mantêm seu comportamento atual com aparência adequada.
- Claro, escuro e acompanhar o sistema continuam selecionáveis; retornar à aplicação conserva preferência, e mudança do dispositivo altera a aparência apenas em sistema.
- Manter navegação entre configurações e acesso às ações atuais sem criar novas regras de confirmação de e-mail ou autenticação.
- Nas superfícies desta entrega, conferir os nove viewports (360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080), temas claro e escuro, estados aplicáveis e ausência de rolagem horizontal da página; manter acesso às ações atuais, rótulos e foco visível.

## Dependências

Pode iniciar a adequação das páginas atuais. Para concluir o aceite, integrar Identidade e temas no painel atual e Estrutura e navegação responsiva atuais. A preservação funcional não depende de implementar a futura Feature Acesso à conta pessoal.

## Referências

Item pai Redmine #1016101; regras/critérios R1, R2, R3, R5, CA1, CA2, CA3, CA4, CA5, CA6, CA7, CA8, V-Conta.

- design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; .btn, inputs, mensagens, dialog e tokens; adaptação aprovada para perfil/configurações sem composição específica
- Adaptações aprovadas: todas as telas atuais, claro/escuro/sistema preservados; telas futuras nas próximas Features.

<!-- project-slices-child:ea4e10505df2d89c9f381b42663c41f98a483195bdfe4f27e677bf99b37f647e -->

## Relações

- `#1016115` blocks `#1016117`
