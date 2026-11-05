# [DEV] [WEB] [USUARIO] Gestão de transações - Histórico por período

- Redmine: `#1015931`
- Tipo: `DEV`
- Tracker: Task (`4`)
- Item pai: `#1015911`
- Estimativa: `2h`

## Descrição

## Entrega

Permitir descobrir e percorrer as próprias transações por período, abrindo a consulta individual já entregue no cadastro. Inclui mês atual, outro mês, histórico integral, ordenação, paginação e contagem.

## Escopo e limites

Não refaz a leitura individual nem a validação do cadastro. Busca textual e filtros de tipo/categoria pertencem à entrega específica; paginação e seleção de período já funcionam nesta entrega.

## Critérios de aceite

- CA6: histórico sem registros orienta primeiro cadastro.
- R10 e dados percebidos, histórico: exibir descrição, tipo, valor em reais com centavos, categoria e data brasileira de cada registro, número de resultados e acesso à consulta individual já entregue.
- R9, navegação: ordenar por data da movimentação decrescente e cadastro mais recente em empate; páginas de 50 registros, permitindo percorrer todo o conjunto do período.
- CA5, período: iniciar histórico no mês atual, permitir outro mês ou todo histórico; mudar período retorna à primeira página.
- CA7 e permissões, descoberta: histórico e seus resultados não revelam registros de outra conta e levam somente à consulta individual autorizada.

## Dependências

Para iniciar: ‘Gestão de transações - Cadastro e conferência de uma transação própria’, que fornece registros e consulta individual. Para concluir: navegação por período/páginas abre essa mesma consulta.

## Referências

Item pai Redmine #1015911; regras/critérios CA6-vazio, R10-historico, R9-navegacao, CA5-periodo, CA7-historico.

<!-- project-slices-child:9a277061dc1c74bce9f00ee75edd4395c1bdddc17ff3fc04f8f62d62f2ac2bc0 -->

## Relações

- `#1015930` blocks `#1015931`
- `#1015931` blocks `#1015932`
- `#1015931` blocks `#1015936`
