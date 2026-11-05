# [DEV] [WEB] [USUARIO] Acesso à conta - Confirmação de e-mail com nova tentativa

- Redmine: `#1015927`
- Tipo: `DEV`
- Tracker: Task (`4`)
- Item pai: `#1015909`
- Estimativa: `2h`

## Descrição

## Entrega

Completar a orientação de nova tentativa quando o envio de confirmação falhar no cadastro ou no reenvio, e quando um link de confirmação for recusado. Preservar o cadastro público, a confirmação pelo titular, a restrição financeira e o reenvio que já existem.

## Escopo e limites

Abrange cadastro, envio/reenvio e confirmação do e-mail. A política de senha pertence a ‘Acesso à conta - Política de senha no cadastro e na redefinição’; a recuperação de senha pertence a ‘Acesso à conta - Recuperação de senha com nova tentativa’.

## Critérios de aceite

- Cadastro válido cria uma única conta, envia o link e orienta confirmar o e-mail; receber o e-mail por si só não libera finanças.
- Conta não confirmada permanece sem acesso financeiro, com orientação para confirmar, reenviar o link ou sair.
- Titular com link válido da própria conta confirma o endereço e acessa a área inicial, autenticando-se antes quando necessário.
- Link de confirmação inválido não confirma o endereço nem libera acesso e apresenta orientação e caminho para solicitar outro.
- Link de confirmação expirado não confirma o endereço nem libera acesso e apresenta orientação e caminho para solicitar outro.
- Link de outra conta não confirma nenhum endereço indevido nem libera acesso e permite ao usuário solicitar confirmação da própria conta.
- Reabrir link ainda válido de uma conta já confirmada mantém a confirmação e permite seguir à área inicial.
- Falha de envio no cadastro informa a impossibilidade de concluir a etapa dependente do e-mail e orienta nova tentativa; repetir depois da falha não cria contas duplicadas.
- Falha no reenvio informa que o envio não foi concluído e orienta nova tentativa, sem mensagem de sucesso.
- Restabelecido o envio, a nova tentativa permite receber o link e concluir a confirmação.

## Dependências

Pode iniciar com cadastro e confirmação existentes. Para a jornada integrada, usar a política de senha entregue por ‘Acesso à conta - Política de senha no cadastro e na redefinição’.

## Referências

Item pai Redmine #1015909; regras/critérios CA4, CA10-confirmacao.

<!-- project-slices-child:ddf0296c61c38b8e25654e171f6f823ea2c83bb0a0dd78409f5837df906f00ba -->

## Relações

- `#1015927` blocks `#1015929`
