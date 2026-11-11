# [DEV] [WEB] [USUARIO] Acesso à conta pessoal - Confirmação de e-mail com acesso restrito e retomada

- Redmine: `#1016120`
- Tipo: `DEV`
- Tracker: Task (`4`)
- Item pai: `#1016104`
- Estimativa: `2h`

## Descrição

## Entrega

Completar a confirmação de e-mail, do envio inicial à retomada, e impedir que contas não confirmadas acessem perfil e demais funcionalidades. Confirmação própria e reenvio já existem; faltam restrição integral e orientação nas falhas de link/envio.

## Escopo e limites

Responsável pelo envio inicial, jornada restrita de confirmação/reenvio/saída, links de confirmação e restrição da área do produto. Preservar login, lembrar e recuperação atuais. A política de senha e a retomada da recuperação são fornecidas pelas outras entregas.

## Critérios de aceite

- Cadastro público válido cria uma única conta, envia confirmação e orienta o titular; receber o e-mail não libera o produto antes de confirmar.
- Conta não confirmada, com sessão normal ou lembrada, não acessa diretamente área inicial, perfil, configurações ou funcionalidades do produto. Mantém confirmação, reenvio, saída e caminho de recuperação; pode sair e usar a jornada pública existente quando necessário, sem novo mecanismo autenticado.
- Titular com link próprio válido confirma e acessa a área inicial, autenticando-se quando necessário. Reabrir link ainda válido de conta já confirmada conserva a confirmação.
- Links inválidos, expirados ou de outra conta não confirmam endereço indevido nem liberam o sistema; apresentar orientação e caminho para solicitar novo link próprio.
- Falha de envio no cadastro/reenvio informa que o envio não concluiu e orienta nova tentativa, sem sucesso fictício. Após restabelecimento, retomar sem contas duplicadas nem titular sem caminho de confirmação/recuperação.
- Preservar credenciais corretas/incorretas, destino solicitado, lembrar, bloqueio após cinco falhas e saída; contas confirmadas continuam usando operações permitidas.
- Nas telas e estados alterados, consumir marca, tipografia, paleta, campos, botões, erros e feedback da base FinAI em computador, tablet e celular, nos temas claro, escuro e acompanhar o sistema, sem reconstruir identidade ou layouts do fornecedor.

## Dependências

Início bloqueado pelo aceite integrado [QA] [WEB] [USUARIO] Adequação visual do FinAI (#1016117), dependente dos cinco DEV visuais e representante da base implementada e verificada. Após a liberação visual, pode iniciar sem esperar os demais DEV de acesso. Para concluir a jornada integrada, usar Cadastro e redefinição com política de senha consistente e Recuperação de senha com nova tentativa.

## Referências

Item pai Redmine #1016104; regras/critérios R1, R2, R4, R6, R7, R8, CA1, CA3, CA4, CA5, CA6, CA7, CA11, CA11-Confirmacao, R9, CA12.

- design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; referência clara e adaptações aprovadas na Feature visual #1016101; linguagem de formulários, mensagens e ações de retomada. Não há composição própria de acesso no ZIP.
- Fornecedor de composição: [DEV] [WEB] [USUARIO] Adequação visual do FinAI - Página inicial e jornadas de acesso (#1016114); aceite integrado: [QA] [WEB] [USUARIO] Adequação visual do FinAI (#1016117).

<!-- project-slices-child:c86412d342a4fb0adf10944bdc67406276c436c7274d2ee53af73e118f914fd2 -->

## Relações

- `#1016120` blocks `#1016122`
