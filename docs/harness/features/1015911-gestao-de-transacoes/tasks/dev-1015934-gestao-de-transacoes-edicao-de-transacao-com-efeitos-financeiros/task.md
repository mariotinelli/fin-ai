# [DEV] [WEB] [USUARIO] Gestão de transações - Edição de transação com efeitos financeiros

- Redmine: `#1015934`
- Tipo: `DEV`
- Tracker: Task (`4`)
- Item pai: `#1015911`
- Estimativa: `2h`

## Descrição

## Entrega

Permitir corrigir todos os campos do mesmo registro próprio, reaproveitando formulário e consulta individual. A entrega inclui integrar e verificar o efeito financeiro real da alteração e atualizar a consulta.

## Escopo e limites

Não duplica o registro nem reimplementa a regra de saldo. Salvar campos sem integrar e verificar os efeitos financeiros não conclui esta entrega.

## Critérios de aceite

- Editar todos os campos próprios em qualquer data; tipo, valor, categoria e data atualizam valores aplicáveis. Passada/hoje para futura retira efeito; futura para hoje/passada inclui.
- CA7: detalhes próprios oferecem edição; outra conta não pode alterar por tela ou identificador direto.
- Editar campo válido atualiza o mesmo registro e seus efeitos; mover passada para futura retira contribuição e inverso inclui.
- CA9: cancelar edição conserva registro e totais anteriores.
- CA10: falha ao editar não altera parcialmente nem mostra sucesso; registro removido/indisponível não pode ser alterado e não revela dados de terceiros.
- CA12: registros com dados iguais possuem edição independente.
- Fluxos alternativos: edição inválida preserva formulário, mostra erros e não altera dados; limites R1–R3 e troca de tipo/categoria aplicam-se também à edição.
- Conclusão exige efeitos integrados: na massa de referência com saldo R$ 85,00 em 01/12, mover a receita de R$ 100,00 de 30/11 para 02/12 resulta em saldo -R$ 15,00; trazê-la de volta restaura R$ 85,00. A consulta do mesmo registro e o histórico refletem a alteração.
- Na edição, recusar valor fora de R$ 0,01 a R$ 999.999.999,99 ou mais de duas casas sem arredondar; descrição vazia ou acima de120 caracteres após aparar; data inválida ou fora de01/01/1900 a31/12/9999; campos obrigatórios ausentes e categoria incompatível. Preservar formulário e registro anterior.

## Dependências

Para iniciar: ‘Gestão de transações - Cadastro e conferência de uma transação própria’, com formulário e consulta individual. Para concluir: integrar ‘Gestão de transações - Agendamentos e competência financeira’ e ‘Gestão de transações - Histórico por período’, verificando valores antes/depois e atualização das consultas. Persistência isolada não basta para encerrar.

## Referências

Item pai Redmine #1015911; regras/critérios R7, CA7-edicao, CA8, CA9-edicao, CA10-edicao, CA12-edicao, F-edicao-validacao.

<!-- project-slices-child:e3d1f9909b0443a7e718476478cffb5f73f90ab126f6e4b4baed19a9ec2878e0 -->

## Relações

- `#1015930` blocks `#1015934`
- `#1015934` blocks `#1015936`
