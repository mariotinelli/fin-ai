# [DEV] [WEB] [USUARIO] Dashboard financeiro - Visão geral com saldo, balanço mensal e recentes

- Redmine: `#1016127`
- Tipo: `DEV`
- Tracker: Task (`4`)
- Item pai: `#1016106`
- Estimativa: `4.5h`

## Descrição

## Entrega

Transformar o dashboard placeholder em uma Visão geral financeira real do titular, integrando saldo acumulado, indicadores/balanço mensais, cinco recentes e ações fornecidas por Transações numa tela completa e verificável.

## Escopo e limites

Responsável pelas consultas, composição e atualização dos indicadores da Visão geral. Reutilizar persistência, cadastro, detalhes, histórico e manutenção dos fornecedores, sem reimplementar suas regras. Não criar gráfico temporal, relatório novo, saldo inicial ou chat/IA.

## Critérios de aceite

- Ao abrir Visão geral, apresentar saldo geral de todas as receitas menos todas as despesas do titular e totais/contagens do mês corrente local; valores em reais e datas brasileiras, sem dados fictícios ou de outra conta.
- Selecionar outro mês/ano atualiza apenas receitas,despesas,contagens,duas barras e resultado daquele período. Saldo geral e até cinco recentes continuam considerando todo o histórico.
- Balanço mostra legenda e valores de Receitas/Despesas, maior soma positiva na extensão de referência e outra proporcional; tipo zerado não causa cálculo inválido. Resultado mensal é receitas menos despesas, incluindo negativo ou zero com movimentos.
- Sem registros, apresentar zeros e orientação para primeiro cadastro; com histórico fora do mês escolhido, zerar somente indicadores mensais e preservar saldo/recentes. Mês sem movimento usa estado vazio do gráfico; receitas/despesas iguais e positivas conservam barras e contagens.
- Recentes traz no máximo cinco registros reais por data decrescente e depois cadastro mais recente, com descrição,categoria,data,valor e tipo/sinal, sem completar com exemplos; abrir detalhes e Ver todas usa as jornadas próprias de transações.
- Nova transação reutiliza o cadastro fornecido; edição/exclusão reutilizam a manutenção dos detalhes. Após cada sucesso, atualizar todos os indicadores e recentes conforme seus recortes. Falha/cancelamento não antecipa valores como se salvos; acessar/atualizar a página consulta o estado atual do sistema, sem definir polling contínuo entre sessões.
- Falha da consulta informa indisponibilidade e nova tentativa, sem saldo zero ou histórico vazio como sucesso; restaurada a consulta, recuperar os valores reais.
- Toda consulta,contagem,total,gráfico e lista é do titular; visitantes e não-confirmados não acessam. Não introduzir saldo inicial manual, múltiplas contas ou relatório avançado.
- Preservar #overview da referência: cabeçalho/mês/Nova transação,três cartões com destaque no saldo,balanço,convite do assistente e recentes/Ver todas. Consumir identidade FinAI em claro/escuro/sistema e adaptar para computador/tablet/celular com lista compacta e dados completos nos detalhes.
- Convite visual do assistente permanece com ação indisponível antes da entrega responsável, sem simular chat nem criar dependência de implementação do assistente.

## Dependências

Início bloqueado por [DEV] [WEB] [USUARIO] Gestão de transações - Cadastro de receitas e despesas com conferência do registro (#1016123). Para concluir Ver todas, integrar Histórico, filtros e paginação (#1016124); para concluir atualização após edição/exclusão, integrar Edição e exclusão confirmada (#1016125). Estes dois não impedem iniciar agregados e composição depois do primeiro fornecedor. A base visual verificada é transitiva via #1016123; não repetir aresta direta. Assistente financeiro não é bloqueador; sua ação fica indisponível até estar entregue.

## Referências

Item pai Redmine #1016106; regras/critérios R1, R2, R3, R4, R5, R6, R7, R8, CA1, CA2, CA3, CA4, CA5, CA6, CA7, CA8, CA9, CA10.

- design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; #overview,#balance,#income,#expense,#graph,#month-result,#recent,#month,#open-chat; render,sorted,list e estilos .stats/.overview-grid/.assistant-teaser/media queries.
- Adaptações aprovadas: dados do sistema em vez de localStorage; base clara/escura/sistema; convite sem simulação de IA; sem composição financeira antecipada pela Feature visual.

<!-- project-slices-child:7c4209fb5c9c3110463fc942d97997253652d2a8e389fe04dea745577ea62e22 -->

## Relações

- `#1016127` blocks `#1016128`
