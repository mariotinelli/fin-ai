# [DEV] [WEB] [USUARIO] Adequação visual do FinAI - Dois fatores e passkeys

- Redmine: `#1016116`
- Tipo: `DEV`
- Tracker: Task (`4`)
- Item pai: `#1016101`
- Estimativa: `2h`

## Descrição

## Entrega

Adequar configuração e desafio de dois fatores, confirmação de senha e gestão/entrada/confirmação de passkeys, incluindo os estados e diálogos atuais, à identidade FinAI. Preservar os mecanismos de autenticação existentes.

## Escopo e limites

Esta entrega possui composições e estados específicos de QR/chave manual/OTP/códigos, confirmação de senha e passkeys. Não adicionar métodos de autenticação, trocar validações ou redesenhar o restante do login; sua presença é integrada com Página inicial e jornadas de acesso.

## Critérios de aceite

- Configuração/desafio2FA, confirmação de senha e passkeys apresentam identidade FinAI no claro e escuro, mantendo conteúdo e ações equivalentes.
- Preservar os estados atuais de QR/chave manual, confirmação OTP, códigos de recuperação, ativação/desativação, carregamento e erros; o QR continua legível no tema escuro.
- Preservar passkeys vazias/preenchidas, indisponibilidade do navegador quando aplicável, registro, entrada/verificação, remoção, cancelamento e erros existentes, com seus resultados e controles atuais.
- Diálogos mantêm abertura/fechamento, rótulos, foco visível e operação por teclado; cancelamentos e falhas não passam a concluir ações indevidamente.
- Preservar as permissões e a exigência atual de confirmação de senha, sem ampliar ou remover recursos.
- Nas superfícies desta entrega, conferir os nove viewports (360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080), temas claro e escuro, estados aplicáveis e ausência de rolagem horizontal da página; manter acesso às ações atuais, rótulos e foco visível.

## Dependências

Pode iniciar com os recursos e telas atuais. Para concluir, integrar a identidade de Identidade e temas no painel atual e a estrutura aplicável de Estrutura e navegação responsiva atuais; integrar a entrada por passkey com Página inicial e jornadas de acesso. Não há bloqueio nativo de início entre esses DEV.

## Referências

Item pai Redmine #1016101; regras/critérios R1, R2, R3, R5, CA1, CA2, CA5, CA6, CA7, CA8, V-Seguranca.

- design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; .btn, inputs, dialog, mensagens e tokens; adaptação aprovada para telas e estados de segurança atuais sem desenho específico
- Adaptações aprovadas: todas as telas atuais, claro/escuro/sistema preservados; telas futuras nas próximas Features.

<!-- project-slices-child:a5a374b364dd6cea34af98b3991a2408d2ec1884bde790962ffdadd6fd821c76 -->

## Relações

- `#1016116` blocks `#1016117`
