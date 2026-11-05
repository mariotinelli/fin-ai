# [DEV] [WEB] [USUARIO] Assistente financeiro com IA - Confirmação única e reconciliação

- Redmine: `#1015948`
- Tipo: `DEV`
- Tracker: Task (`4`)
- Item pai: `#1015913`
- Estimativa: `3h`

## Descrição

## Entrega

Converter a versão atual confirmada por botão em uma única transação própria, reconhecendo repetições e reconciliando resultados incertos antes de qualquer nova gravação.

## Escopo e limites

Não deduplica operações distintas apenas por dados iguais. Não considera resposta incerta como ausência de gravação. Não exige dashboard implementado para persistir a mesma transação que ele consumirá.

## Critérios de aceite

- Somente botão Confirmar da versão atual grava. Repetir mesma proposta cria no máximo uma transação; nova proposta distinta com dados iguais pode criar outro registro.
- Sucesso de registro só após persistência conhecida; futura significa agendada, não pagamento/recebimento realizado.
- Confirmar válida cria um único registro próprio e sucesso após persistência; repetição após voltar ao chat não duplica.
- Confirmar futura grava agendada, fora dos totais até a data, quando entra pela regra de Gestão de transações.
- Falha conhecida mantém proposta para tentar de novo sem sucesso falso; resultado incerto exige conferir gravação antes de repetir, sem duplicar o já efetivado.
- Versão antiga, proposta cancelada ou já confirmada não pode gravar novamente, mesmo após recarregar.

## Dependências

Para iniciar: ‘Assistente financeiro com IA - Preparação e retomada de proposta’. Para concluir: versão/cancelamento de ‘Assistente financeiro com IA - Correção e cancelamento de proposta’, criação real #1015930 e competência #1015933. Concorrência, repetição e reconciliação devem produzir no máximo uma transação por proposta.

## Referências

Item pai Redmine #1015913; regras/critérios R5, R12-confirmacao, CA5, CA6, CA13-gravacao, F-versao-cancelada.

<!-- project-slices-child:15435d8d2652285df0bc9c6f13bd3463885dae29533ac295b1b38666521a09a4 -->

## Relações

- `#1015946` blocks `#1015948`
- `#1015948` blocks `#1015949`
