# [DEV] [WEB] [USUARIO] Gestão de transações - Exclusão confirmada com efeito único

- Redmine: `#1015935`
- Tipo: `DEV`
- Tracker: Task (`4`)
- Item pai: `#1015911`
- Estimativa: `2h`

## Descrição

## Entrega

Permitir confirmar ou cancelar exclusão de registro próprio. A entrega remove sua contribuição financeira uma única vez, atualiza as consultas e preserva registros distintos com dados iguais.

## Escopo e limites

Não oferece desfazer nem reimplementa os cálculos. Remover dados sem conferir seu efeito financeiro e sua repetição não conclui esta entrega.

## Critérios de aceite

- Excluir somente após confirmação, removendo do histórico e cálculos, sem desfazer.
- CA7: detalhes próprios oferecem exclusão; outra conta não pode excluir por tela ou identificador direto.
- CA9: cancelar exclusão mantém dados/totais; confirmar remove do histórico/cálculos sem desfazer.
- CA12: exclusão de registros iguais é independente; repetir exclusão de registro removido não produz novo efeito nos totais.
- Fluxos alternativos: falha ao persistir exclusão não apresenta sucesso nem aplica alteração parcial; orienta nova tentativa.
- Conclusão exige efeitos integrados: na massa de referência com saldo R$ 85,00 em 01/12, excluir a despesa de R$ 30,00 produz R$ 115,00. Repetir a mesma exclusão mantém R$ 115,00; cancelar ou falhar antes de concluir mantém R$ 85,00.

## Dependências

Para iniciar: ‘Gestão de transações - Cadastro e conferência de uma transação própria’, com consulta individual e propriedade. Para concluir: integrar ‘Gestão de transações - Agendamentos e competência financeira’ e ‘Gestão de transações - Histórico por período’, verificando remoção do efeito, repetição sem novo efeito e atualização das consultas.

## Referências

Item pai Redmine #1015911; regras/critérios R8, CA7-exclusao, CA9-exclusao, CA12-exclusao, F-exclusao-falha.

<!-- project-slices-child:5194399bf9ef458eeee0e3c08122258a6ff78b8aa739f97a08665d831f62ea74 -->

## Relações

- `#1015930` blocks `#1015935`
- `#1015935` blocks `#1015936`
