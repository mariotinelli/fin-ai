# [DEV] [WEB] [USUARIO] Acesso à conta - Recuperação de senha com nova tentativa

- Redmine: `#1015928`
- Tipo: `DEV`
- Tracker: Task (`4`)
- Item pai: `#1015909`
- Estimativa: `2h`

## Descrição

## Entrega

Completar a recuperação de senha com orientação quando o envio falhar e uma opção de novo pedido quando o link for inválido, expirado ou já utilizado. Preservar a resposta genérica, a validade de 60 minutos, o uso único e a restrição de contas sem e-mail confirmado.

## Escopo e limites

Abrange solicitação e redefinição de senha esquecida. A composição da senha pertence a ‘Acesso à conta - Política de senha no cadastro e na redefinição’; envio de confirmação pertence a ‘Acesso à conta - Confirmação de e-mail com nova tentativa’.

## Critérios de aceite

- Solicitar recuperação apresenta que um link será enviado se a conta existir, sem distinguir conta existente de inexistente; para conta existente, envia ao e-mail cadastrado.
- Falha no envio orienta nova tentativa sem afirmar conclusão do envio ou revelar explicitamente se a conta existe.
- Depois de restabelecer o envio, nova solicitação permite ao titular receber um link utilizável.
- Link de recuperação inválido não altera senha e oferece caminho para solicitar outro.
- Link de recuperação expirado após 60 minutos não altera senha e oferece caminho para solicitar outro.
- Link já utilizado com sucesso não altera senha novamente e oferece caminho para solicitar outro.
- Link válido, dentro de 60 minutos e ainda não usado, com nova senha e confirmação válidas, permite redefinir e retorna ao login.
- Após redefinição, nova senha permite novos logins e senha anterior não; o link utilizado deixa de funcionar.
- Redefinição não confirma e-mail e mantém a restrição financeira das contas não confirmadas.

## Dependências

Pode iniciar com a recuperação existente. Para concluir a jornada integrada, usar a política de senha entregue por ‘Acesso à conta - Política de senha no cadastro e na redefinição’.

## Referências

Item pai Redmine #1015909; regras/critérios CA9, CA10-recuperacao.

<!-- project-slices-child:28aa773b04bfe04f5fc70806ce834f75a777f973a592ffc8d7a532349e237cbd -->

## Relações

- `#1015928` blocks `#1015929`
