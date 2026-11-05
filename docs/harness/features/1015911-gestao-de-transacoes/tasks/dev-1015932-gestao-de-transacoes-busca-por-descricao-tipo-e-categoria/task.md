# [DEV] [WEB] [USUARIO] Gestão de transações - Busca por descrição, tipo e categoria

- Redmine: `#1015932`
- Tipo: `DEV`
- Tracker: Task (`4`)
- Item pai: `#1015911`
- Estimativa: `2h`

## Descrição

## Entrega

Permitir localizar registros do histórico por trecho da descrição, tipo e categoria, combinados com o período. Reutiliza navegação, paginação e consulta individual já entregues.

## Escopo e limites

Acrescenta busca e combinação de filtros ao histórico existente; não reconstrói ordenação, consulta individual ou paginação.

## Critérios de aceite

- R9, busca e filtros: trecho da descrição sem distinguir caixa/acentos; tipo/categoria/período restringem o mesmo conjunto. Limpar filtros mostra todo o histórico; manter filtros entre páginas e retornar à primeira ao alterar um filtro.
- CA5, busca combinada: descrição, tipo e categoria combinados com período retornam apenas registros correspondentes do usuário, preservando ordenação e paginação do histórico.
- CA6: busca sem resultados difere do histórico vazio e permite ajustar/limpar; limpar retorna histórico integral.

## Dependências

Para iniciar: ‘Gestão de transações - Histórico por período’. Para concluir: filtros combinados preservam sua ordenação e paginação, sem vazar registros de outra conta.

## Referências

Item pai Redmine #1015911; regras/critérios R9, CA5, CA6-busca.

<!-- project-slices-child:3a3229fe3e8792303d22b12c8052573e380a8465ad7429411b28f179d01c8bbc -->

## Relações

- `#1015931` blocks `#1015932`
- `#1015932` blocks `#1015936`
