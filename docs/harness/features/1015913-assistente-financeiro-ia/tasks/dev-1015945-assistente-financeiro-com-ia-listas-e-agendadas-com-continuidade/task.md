# [DEV] [WEB] [USUARIO] Assistente financeiro com IA - Listas e agendadas com continuidade

- Redmine: `#1015945`
- Tipo: `DEV`
- Tracker: Task (`4`)
- Item pai: `#1015913`
- Estimativa: `3h`

## Descrição

## Entrega

Permitir consultar movimentações realizadas e agendadas com filtros, quantidade total e continuidade de dez registros por resposta, sempre sobre dados atuais.

## Escopo e limites

Lista comum não antecipa agendadas; inclusão expressa as distingue. Não mistura totais da página com o conjunto completo nem cria relatórios avançados.

## Critérios de aceite

- Listar por período, tipo e categoria e listar agendadas, usando hoje/ontem/este mês/mês passado/datas/intervalos/todo histórico quando solicitados.
- Lista independente sem período usa este mês; agendadas sem período usa todas futuras. Continuação explícita conserva filtros; dúvida pede esclarecer.
- Listas comuns excluem agendadas salvo inclusão expressa; quando incluídas, distinguir futuras dos contabilizados sem somá-las a valores realizados.
- Até10 registros por resposta, data decrescente/cadastro mais recente em empate, quantidade total e Ver mais. Manter filtros e consultar dados reais; novos critérios iniciam nova lista. Totais usam conjunto completo, não página.
- Resposta de listas identifica período/filtros, mostra dados reais e distingue agendados; não cria transações/categorias/valores fictícios.
- Listas respeitam períodos/filtros e inclusão explícita de futuras, com critérios visíveis.
- Lista sem registros informa ausência; leitura que falha informa indisponibilidade, sem resultados fabricados.
- Nova consulta/lista ou Ver mais usa registros atuais, refletindo alterações/exclusões.
- Mais10 permite Ver mais mantendo filtros e quantidade total; página não representa todo conjunto e totais não são só da página.

## Dependências

Para iniciar: ‘Assistente financeiro com IA - Conversa persistida e saldo real’. Para concluir: integrar interpretação de períodos e critérios de ‘Assistente financeiro com IA - Totais por período e categoria’, registros #1015930 e competência #1015933. Ver mais deve consultar dados reais atuais.

## Referências

Item pai Redmine #1015913; regras/critérios R8-listas, R9-listas, R10-listas, R11, R12-listas, CA9-listas, CA10-listas, CA11-listas, CA12.

<!-- project-slices-child:90832b7848641d7d0bd09717feacf28e10e28500453e4cbd945408464e0a1b22 -->

## Relações

- `#1015943` blocks `#1015945`
- `#1015945` blocks `#1015949`
