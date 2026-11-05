# [DEV] [WEB] [USUARIO] Gestão de transações - Agendamentos e competência financeira

- Redmine: `#1015933`
- Tipo: `DEV`
- Tracker: Task (`4`)
- Item pai: `#1015911`
- Estimativa: `2h`

## Descrição

## Entrega

Identificar agendamentos nas consultas e aplicar a competência financeira em America/Sao_Paulo. Entrega a transição visível de agendada e os resultados de saldo e totais da capacidade interna, verificáveis sem dashboard.

## Escopo e limites

Não acrescenta dashboard, tela de saldo, endpoint público, API consumível ou comando de produto para inspeção. O histórico/consulta individual mostram agendada; valores são verificados na capacidade interna da aplicação. Não executa pagamentos externos.

## Critérios de aceite

- Data define competência em America/Sao_Paulo; futura é agendada, aparece no histórico e não afeta saldo/totais até início da data. Inclusão automática, sem confirmação manual nem pagamento externo.
- Saldo é receitas menos despesas de registros não excluídos até hoje; totais mensais usam data dentro do mês e até hoje. Mês futuro não realiza movimentações; saldo negativo permitido, sem saldo inicial separado.
- R10: futuras mostram identificação de agendada, seguem ordenação por data sem fila separada; identificação cessa na data.
- Futura aparece agendada e não afeta saldo nem totais, mesmo na consulta de seu mês futuro.
- Ao chegar a data em America/Sao_Paulo, compõe valores de R6 sem confirmação e perde marcação de agendada.
- Com receita de R$ 100,00 e despesa de R$ 30,00 em 30/11, mais receita de R$ 20,00 e despesa de R$ 5,00 em 01/12, o saldo às 23:59:59 de 30/11 em Brasília é R$ 70,00 e os totais de dezembro são zero. Às 00:00:00 de 01/12, saldo R$ 85,00 e totais de dezembro R$ 20,00/R$ 5,00; novembro permanece R$ 100,00/R$ 30,00. Registros excluídos e de outra conta não entram.

## Dependências

Para iniciar: ‘Gestão de transações - Cadastro e conferência de uma transação própria’. Para concluir: integrar a indicação de agendada em ‘Gestão de transações - Histórico por período’ e conferir saldo/totais na capacidade interna com dados persistidos e passagem controlada da data.

## Referências

Item pai Redmine #1015911; regras/critérios R5, R6, R10-agendada, CA3, CA4.

<!-- project-slices-child:c83da98eac23c9f162e6d09b8430ce2df12450f714ea8a765202ba0324aa76f5 -->

## Relações

- `#1015930` blocks `#1015933`
- `#1015933` blocks `#1015936`
