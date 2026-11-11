# [DEV] [WEB] [USUARIO] Gestão de transações - Histórico, filtros e paginação

- Redmine: `#1016124`
- Tipo: `DEV`
- Tracker: Task (`4`)
- Item pai: `#1016105`
- Estimativa: `2h`

## Descrição

## Entrega

Criar a consulta completa das transações persistidas do titular, com mês, busca, tipo/categoria, contagem total, ordenação e páginas de50. Integrar lista responsiva, acesso aos detalhes e estados de vazio/sem resultado/indisponibilidade, usando os registros fornecidos pelo cadastro.

## Escopo e limites

Responsável pela consulta/lista, filtros, contagens e paginação; reutilizar cadastro e detalhes, sem repetir persistência ou implementar manutenção. Cada campo da lista/detalhes deve vir do registro próprio real.

## Critérios de aceite

- Iniciar no mês corrente local e permitir outro mês/ano. Combinar mês, trecho de descrição sem diferenças de caixa/acentos, tipo e categoria; campo sem filtro considera todos os seus valores, e contagem refere-se ao resultado inteiro.
- Limpar filtros remove também o mês e permite todo o histórico. Alterar filtro volta à primeira página; registro salvo fora do recorte ativo continua persistido e pode ser encontrado ao alterar/limpar filtros.
- Ordenar por data decrescente e, em empate, cadastro mais recente. Mostrar até50itens/página com Anterior/Próxima e indicação de página, impedindo ultrapassar limites e ajustando página após mudança dos resultados.
- Sem qualquer registro, orientar o primeiro cadastro; com histórico mas sem correspondência, orientar alterar/limpar filtros. Falha de carga apresenta indisponibilidade e nova tentativa, nunca lista vazia como se a consulta tivesse funcionado.
- Lista desktop apresenta descrição,categoria,data,valor com sinal/tipo e ação de detalhes; no celular, usar lista compacta mantendo todos os cinco campos nos detalhes. Abrir pela descrição ou ação leva ao registro real.
- Consultar/listar/contar/detalhar considera somente o titular; acessos diretos a registros alheios,inexistentes ou removidos não revelam dados e orientam voltar/atualizar a consulta. Restringir visitante e não-confirmado.
- Nas novas superfícies, preservar a composição aplicável do design e consumir a identidade FinAI fornecida, em computador/tablet/celular, claro/escuro/sistema, sem reconstruir marca, temas ou navegação compartilhada.

## Dependências

Início bloqueado por Cadastro de receitas e despesas com conferência do registro, que fornece a primeira capacidade persistida e seus detalhes; fixtures não substituem esse fornecedor. O marco visual é transitivo por esse cadastro. Para concluir atualizações após manutenção, integrar com Edição e exclusão confirmada, sem bloqueio de início entre essas duas entregas.

## Referências

Item pai Redmine #1016105; regras/critérios R1, R5, R6, R8, R9, CA5, CA6, CA7, CA8, CA10-Consulta, CA11-Consulta, CA12.

- design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; #transactions,.filters,.transaction,.pagination; renderHistory,sorted,list,clear-filters e media queries
- Adaptações aprovadas: persistência no sistema e por titular, somente datas até hoje, categorias do design mantidas e variante escura da base visual.

<!-- project-slices-child:1e5aa58d1fc926719abde9b0141f9d1827890daf302bc3d7135b8a0d410bec32 -->

## Relações

- `#1016123` blocks `#1016124`
- `#1016124` blocks `#1016126`
