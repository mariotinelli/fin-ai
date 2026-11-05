# [DEV] [WEB] [USUARIO] Assistente financeiro com IA - Totais por período e categoria

- Redmine: `#1015944`
- Tipo: `DEV`
- Tracker: Task (`4`)
- Item pai: `#1015913`
- Estimativa: `3h`

## Descrição

## Entrega

Ampliar a conversa para totais de receitas e despesas por período/categoria, declarando os critérios e esclarecendo ambiguidades. Reutilizar a competência e os dados de Gestão de transações.

## Escopo e limites

Não duplica regras de competência ou usa valores calculados pela IA como fonte de verdade. Intervalos e filtros do chat são próprios desta consulta, sem publicar API.

## Critérios de aceite

- Consultar totais de receitas/despesas por período e categoria. Reconhecer hoje, ontem, este mês, mês passado, datas/intervalos explícitos e todo histórico.
- Consulta independente de totais sem período usa este mês e declara o padrão; continuação explícita pode reutilizar filtros; dúvida exige esclarecimento.
- Saldo/totais usam só próprios não excluídos até hoje. Intervalos incluem início/fim; invertido/ambíguo pede correção.
- Resposta de totais identifica período/filtros, distingue contabilizado de agendado e usa reais com centavos.
- Totais respeitam padrões, filtros e períodos explícitos de R8–R12, inclusive todo histórico.
- Total zero real/ausência difere de falha de leitura, que informa indisponibilidade.
- Nova consulta de totais reflete edição/exclusão na interface, sem reutilizar resposta financeira antiga.

## Dependências

Para iniciar: ‘Assistente financeiro com IA - Conversa persistida e saldo real’. Para concluir: dados próprios de #1015930 e competência de #1015933; integrar períodos/continuação na conversa e conferir alterações/exclusões fornecidas por #1015934/#1015935.

## Referências

Item pai Redmine #1015913; regras/critérios R8-totais, R9-totais, R10-totais, R12-totais, CA9-totais, CA10-totais, CA11-totais.

<!-- project-slices-child:04d68964791ad92a5b4f70692fd9b201a39b63af37bc276f1db20a79fc90e91c -->

## Relações

- `#1015943` blocks `#1015944`
- `#1015944` blocks `#1015949`
