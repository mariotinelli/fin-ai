# Publicação das filhas de [WEB] [USUARIO] Dashboard financeiro

Item pai Redmine: `1016106`

## Campos nativos aprovados

- Projeto: `65224`
- Pai nativo: `1016106`
- Tracker da mãe: Feature (`2`)
- Tracker DEV: Task (`4`)
- Tracker QA: Deliverable (`5`)
- Status inicial: New (`1`)
- Prioridade inicial: Normal (`4`, regra fixa)
- Categoria herdada: `None`
- Versão herdada: `20355`
- Responsável, início e vencimento: vazios

## Campos nativos e descrições

### [DEV] [WEB] [USUARIO] Dashboard financeiro - Visão geral com saldo, balanço mensal e recentes

- Chave interna: `dev-1`
- Tipo: DEV
- Estimativa: 4.5h
- Payload SHA-256: `3f36fead1c7cdf5de7d09ea34fca49ebc5a2c576507de44a92f7a9f3db122eea`

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


### [QA] [WEB] [USUARIO] Dashboard financeiro

- Chave interna: `qa`
- Tipo: QA
- Estimativa: 2.5h
- Payload SHA-256: `82d8be03d70ba819977a839b99f0d8e0c67bbf88c37aab50371d27d0720eee6e`

## Objetivo

Verificar a Visão geral financeira completa com cálculos e recortes corretos,dados reais próprios,manutenção integrada,estados e composição visual aprovados.

## Jornadas integradas

- Acumulado e mês corrente: Usar receitas/despesas em meses distintos com somas conhecidas e abrir a página. Resultado esperado: Saldo de todo o histórico; totais/contagens somente do mês corrente local.
- Troca de mês e ano: Selecionar outro mês/ano mantendo massa conhecida. Resultado esperado: Atualizar totais/contagens,barras e resultado do período; não alterar saldo geral ou recentes de todo o histórico.
- Calendário local: Em contexto de fronteira de mês local diferente deUTC,abrir e consultar os períodos. Resultado esperado: Mês corrente e recorte coerentes com o calendário local do fornecedor de transações.
- Negativo: Usar despesas superiores às receitas no histórico e/ou no mês. Resultado esperado: Saldo/resultado negativos com sinal e valor corretos,sem limitar a zero.
- Zero com movimentos: Usar receitas e despesas iguais e positivas no mês. Resultado esperado: Resultado zero com contagens/barras correspondentes,não estado sem movimento.
- Reais e centavos: Consultar transações com centavos e soma conhecida. Resultado esperado: Valores em reais e precisão/apresentação corretas;datas em formato brasileiro,tipos/sinais distinguíveis.
- Histórico totalmente vazio: Abrir com conta sem registros. Resultado esperado: Saldo/totais/resultados zero,contagens vazias,orientação de primeiro cadastro e gráfico em estado inicial,sem exemplos.
- Mês vazio com histórico: Selecionar mês sem transações numa conta que tenha registros em outros meses. Resultado esperado: Indicadores mensais zerados/gráfico vazio;saldo e recentes continuam usando todo o histórico.
- Proporções das barras: Usar somas diferentes positivas e comparar legenda,valores e extensões. Resultado esperado: Maior soma ocupa referência e outra proporcional,com duas barras identificadas corretamente.
- Um tipo zerado: Usar um tipo sem soma e outro positivo no período. Resultado esperado: Gráfico e valores apresentáveis,sem divisão/cálculo inválido. Ausência completa de transações usa estado vazio.
- Cinco recentes e empate: Usar mais de cinco registros com datas empatadas e cadastros em ordem conhecida. Resultado esperado: No máximo os cinco mais recentes por data e cadastro; mês selecionado não filtra a lista.
- Menos de cinco: Abrir com menos de cinco registros reais. Resultado esperado: Mostrar somente existentes,sem completar com exemplos.
- Detalhes e histórico: Abrir detalhes de um recente e acionar Ver todas. Resultado esperado: Levar aos dados próprios e ao histórico do fornecedor,com todos os campos acessíveis no detalhe.
- Cadastro pelo dashboard: Salvar nova transação usando a ação da página e comparar antes/depois. Resultado esperado: Atualizar saldo,indicadores mensais,barras,resultado e recentes conforme os recortes aplicáveis e o estado salvo.
- Edição pelo detalhe: Editar transação pelos detalhes acessíveis a partir da página,incluindo mudança de mês/tipo/data aplicável. Resultado esperado: Recalcular os indicadores e posição nos recentes segundo dados persistidos,sem duplicação ou recortes incorretos.
- Exclusão pelo detalhe: Excluir transação pela jornada fornecida e comparar números/lista. Resultado esperado: Refletir remoção persistida em todos os indicadores aplicáveis e recentes.
- Cancelamento e falha de operação: Cancelar ou provocar falha de cadastro/edição/exclusão nas jornadas reutilizadas. Resultado esperado: Não antecipar valores ou lista como se a alteração tivesse sido salva.
- Falha de consulta e retomada: Provocar falha de consulta,restabelecer e tentar novamente. Resultado esperado: Indicar indisponibilidade/nova tentativa,sem zero ou vazio como sucesso;após retomada,exibir valores reais.
- Titulares distintos: Abrir e consultar sob duas contas com dados diferentes,inclusive acesso direto aos dados consultados. Resultado esperado: Totais,contagens,gráfico e recentes somente do titular;nenhum dado alheio influencia os números.
- Visitante e não-confirmado: Tentar abrir o dashboard sem sessão e com conta não confirmada. Resultado esperado: Restringir conforme a Feature de acesso,sem apresentar finanças.
- Composição responsiva e temas: Comparar com design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md (#overview,.stats,.overview-grid,.assistant-teaser e lista) em computador/tablet/celular e claro/escuro/sistema,incluindo estados vazios/falhas. Resultado esperado: Preservar cabeçalho/mês/ação,três cartões/saldo destacado,balanço,convite e recentes;lista compacta no celular mantém detalhes acessíveis e identidade FinAI.
- Convite do assistente: Abrir a página antes da entrega do Assistente e observar sua ação. Resultado esperado: Convite visual permanece indisponível para uso,sem chat/IA simulados nem bloqueio do aceite do dashboard.
- Atualizar dados salvos: Alterar registros no sistema e acessar/atualizar novamente Visão geral. Resultado esperado: Buscar o estado persistido atual;respeitar recortes e não usar dados locais como fonte financeira;não exigir polling contínuo entre sessões.

## Regras e permissões

- Saldo/recentes usam todo o histórico;totais/contagens/gráfico/resultado usam o mês selecionado;datas seguem o calendário do fornecedor.
- Somente dados persistidos do titular;visitantes/não-confirmados restritos;sem números de demonstração ou saldo inicial manual.
- Operações financeiras são reutilizadas;atualizar após sucesso,não após falha/cancelamento. Assistente é independente e sua ação fica indisponível antes da entrega.

## Impactos relacionados

- Conferir integração com os três fornecedores de Transações sem refazer toda sua QA ou reconstruir formulários.
- Mudar mês não deve alterar recentes ou saldo;manutenção pode afetar meses/posição e precisa atualizar o recorte correto.
- Consumir a base visual verificada e testar composição/estados próprios do dashboard nos três portes de dispositivo e temas.

## Critérios de conclusão

- Executar CT-001 aCT-023 do documento aprovado,registrando resultado observado e evidência por condição.
- Verificar valores conhecidos,recortes,estados,isolamento,integrações e visual;reportar desvios/impedimentos sem aprovar condição não executada.
- Manter o DOCX da revisão aprovado associado à QA e registrar preparação,resultados e reteste delimitado.

## Referências

Item pai Redmine #1016106; regras/critérios R1, R2, R3, R4, R5, R6, R7, R8, CA1, CA2, CA3, CA4, CA5, CA6, CA7, CA8, CA9, CA10.

<!-- project-slices-child:e2d59a8988b6495ba2b5f86861fcbdf8931959455e3c253a0d453043132ab26e -->


## Bloqueios nativos

- [DEV] [WEB] [USUARIO] Dashboard financeiro - Visão geral com saldo, balanço mensal e recentes bloqueia [QA] [WEB] [USUARIO] Dashboard financeiro (`blocks`).

# Condições de teste

## Contexto

Titulares A/B com transações próprias em meses/anos distintos e totais conhecidos, saldo/resultado negativo, valores iguais positivos, um tipo zerado, mês vazio com histórico fora dele e conta totalmente vazia. Usar mais de cinco registros com datas empatadas e ordem de cadastro conhecida. Fornecedores de transações e base visual devem estar implementados para executar o aceite integrado. Preparar falha de consulta e operações canceladas/com falha; conferir computador/tablet/celular e claro/escuro/sistema. Nenhum teste foi executado nesta preparação; registrar evidência ou impedimento posterior.

## Cálculos e períodos

### CT-001 — Acumulado e mês corrente

Verificação: Usar receitas/despesas em meses distintos com somas conhecidas e abrir a página.

Resultado esperado: Saldo de todo o histórico; totais/contagens somente do mês corrente local.

Origem no requisito: R1: Saldo geral = soma de todas as receitas do titular menos soma de todas as despesas do titular em todo o histórico persistido. Não há saldo inicial manual, conciliação bancária ou saldo por múltiplas contas nesta entrega. O seletor de mês não altera o saldo geral.; R2: Receitas e despesas do mês são as somas por tipo das transações cuja data pertence ao mês e ano selecionados. Contagens correspondem à quantidade de transações de cada tipo no período. Resultado do mês = receitas do mês menos despesas do mês.; R3: Iniciar no mês corrente e permitir escolher outro mês e ano. As datas e o mês corrente seguem o mesmo calendário local da gestão de transações. O dashboard não altera datas nem cria registros; somente movimentações realizadas são persistidas conforme a Feature responsável.; CA1: Com receitas e despesas em meses diferentes, abrir Visão geral; o saldo geral corresponde à diferença de todo o histórico e os totais/contagens mensais correspondem somente ao mês corrente.

### CT-002 — Troca de mês e ano

Verificação: Selecionar outro mês/ano mantendo massa conhecida.

Resultado esperado: Atualizar totais/contagens,barras e resultado do período; não alterar saldo geral ou recentes de todo o histórico.

Origem no requisito: R1: Saldo geral = soma de todas as receitas do titular menos soma de todas as despesas do titular em todo o histórico persistido. Não há saldo inicial manual, conciliação bancária ou saldo por múltiplas contas nesta entrega. O seletor de mês não altera o saldo geral.; R2: Receitas e despesas do mês são as somas por tipo das transações cuja data pertence ao mês e ano selecionados. Contagens correspondem à quantidade de transações de cada tipo no período. Resultado do mês = receitas do mês menos despesas do mês.; R3: Iniciar no mês corrente e permitir escolher outro mês e ano. As datas e o mês corrente seguem o mesmo calendário local da gestão de transações. O dashboard não altera datas nem cria registros; somente movimentações realizadas são persistidas conforme a Feature responsável.; R5: Recentes apresenta os cinco registros mais recentes de todo o histórico, ordenados por data decrescente e depois pelo cadastro mais recente, como na gestão de transações. Com menos de cinco, mostrar somente os existentes. Trocar o mês não filtra essa lista.; CA2: Selecionar outro mês e ano; atualizar receitas, despesas, contagens, barras e resultado do período, mantendo saldo geral e recentes independentes do filtro mensal.

### CT-003 — Calendário local

Verificação: Em contexto de fronteira de mês local diferente deUTC,abrir e consultar os períodos.

Resultado esperado: Mês corrente e recorte coerentes com o calendário local do fornecedor de transações.

Origem no requisito: R3: Iniciar no mês corrente e permitir escolher outro mês e ano. As datas e o mês corrente seguem o mesmo calendário local da gestão de transações. O dashboard não altera datas nem cria registros; somente movimentações realizadas são persistidas conforme a Feature responsável.; CA1: Com receitas e despesas em meses diferentes, abrir Visão geral; o saldo geral corresponde à diferença de todo o histórico e os totais/contagens mensais correspondem somente ao mês corrente.; CA2: Selecionar outro mês e ano; atualizar receitas, despesas, contagens, barras e resultado do período, mantendo saldo geral e recentes independentes do filtro mensal.

### CT-004 — Negativo

Verificação: Usar despesas superiores às receitas no histórico e/ou no mês.

Resultado esperado: Saldo/resultado negativos com sinal e valor corretos,sem limitar a zero.

Origem no requisito: R1: Saldo geral = soma de todas as receitas do titular menos soma de todas as despesas do titular em todo o histórico persistido. Não há saldo inicial manual, conciliação bancária ou saldo por múltiplas contas nesta entrega. O seletor de mês não altera o saldo geral.; R2: Receitas e despesas do mês são as somas por tipo das transações cuja data pertence ao mês e ano selecionados. Contagens correspondem à quantidade de transações de cada tipo no período. Resultado do mês = receitas do mês menos despesas do mês.; R7: Apresentar valores em reais e datas em formato brasileiro. Distinguir receitas e despesas por identificação, sinal e aparência, mantendo a linguagem visual FinAI. Não usar números de demonstração ou resultados derivados de outro titular.; CA3: Consultar cenário com despesas superiores às receitas; apresentar saldo geral e/ou resultado mensal negativos corretamente. Com valores iguais e positivos, mostrar resultado zero com os registros e barras correspondentes.

### CT-005 — Zero com movimentos

Verificação: Usar receitas e despesas iguais e positivas no mês.

Resultado esperado: Resultado zero com contagens/barras correspondentes,não estado sem movimento.

Origem no requisito: R2: Receitas e despesas do mês são as somas por tipo das transações cuja data pertence ao mês e ano selecionados. Contagens correspondem à quantidade de transações de cada tipo no período. Resultado do mês = receitas do mês menos despesas do mês.; R4: O balanço compara receitas e despesas do mês em duas barras, com legenda e valores. A maior soma positiva ocupa a extensão de referência e a outra é proporcional; total zero não causa cálculo inválido. Sem transações no mês, apresentar estado vazio próprio em vez de barras fictícias.; CA3: Consultar cenário com despesas superiores às receitas; apresentar saldo geral e/ou resultado mensal negativos corretamente. Com valores iguais e positivos, mostrar resultado zero com os registros e barras correspondentes.; CA5: Comparar o gráfico com os totais mensais; legenda, valores e proporções das duas barras correspondem às somas. Um tipo com soma zero e outro positivo continua apresentável; ausência completa de movimentos usa o estado vazio.

### CT-006 — Reais e centavos

Verificação: Consultar transações com centavos e soma conhecida.

Resultado esperado: Valores em reais e precisão/apresentação corretas;datas em formato brasileiro,tipos/sinais distinguíveis.

Origem no requisito: R1: Saldo geral = soma de todas as receitas do titular menos soma de todas as despesas do titular em todo o histórico persistido. Não há saldo inicial manual, conciliação bancária ou saldo por múltiplas contas nesta entrega. O seletor de mês não altera o saldo geral.; R2: Receitas e despesas do mês são as somas por tipo das transações cuja data pertence ao mês e ano selecionados. Contagens correspondem à quantidade de transações de cada tipo no período. Resultado do mês = receitas do mês menos despesas do mês.; R7: Apresentar valores em reais e datas em formato brasileiro. Distinguir receitas e despesas por identificação, sinal e aparência, mantendo a linguagem visual FinAI. Não usar números de demonstração ou resultados derivados de outro titular.; CA1: Com receitas e despesas em meses diferentes, abrir Visão geral; o saldo geral corresponde à diferença de todo o histórico e os totais/contagens mensais correspondem somente ao mês corrente.

## Estados e gráfico

### CT-007 — Histórico totalmente vazio

Verificação: Abrir com conta sem registros.

Resultado esperado: Saldo/totais/resultados zero,contagens vazias,orientação de primeiro cadastro e gráfico em estado inicial,sem exemplos.

Origem no requisito: R1: Saldo geral = soma de todas as receitas do titular menos soma de todas as despesas do titular em todo o histórico persistido. Não há saldo inicial manual, conciliação bancária ou saldo por múltiplas contas nesta entrega. O seletor de mês não altera o saldo geral.; R2: Receitas e despesas do mês são as somas por tipo das transações cuja data pertence ao mês e ano selecionados. Contagens correspondem à quantidade de transações de cada tipo no período. Resultado do mês = receitas do mês menos despesas do mês.; R4: O balanço compara receitas e despesas do mês em duas barras, com legenda e valores. A maior soma positiva ocupa a extensão de referência e a outra é proporcional; total zero não causa cálculo inválido. Sem transações no mês, apresentar estado vazio próprio em vez de barras fictícias.; CA4: Sem registros, apresentar zeros e orientação de início, sem valores fictícios. Em um mês sem movimento, mas com histórico em outros meses, apresentar somente os indicadores mensais vazios, preservando saldo e recentes do histórico.

### CT-008 — Mês vazio com histórico

Verificação: Selecionar mês sem transações numa conta que tenha registros em outros meses.

Resultado esperado: Indicadores mensais zerados/gráfico vazio;saldo e recentes continuam usando todo o histórico.

Origem no requisito: R1: Saldo geral = soma de todas as receitas do titular menos soma de todas as despesas do titular em todo o histórico persistido. Não há saldo inicial manual, conciliação bancária ou saldo por múltiplas contas nesta entrega. O seletor de mês não altera o saldo geral.; R2: Receitas e despesas do mês são as somas por tipo das transações cuja data pertence ao mês e ano selecionados. Contagens correspondem à quantidade de transações de cada tipo no período. Resultado do mês = receitas do mês menos despesas do mês.; R4: O balanço compara receitas e despesas do mês em duas barras, com legenda e valores. A maior soma positiva ocupa a extensão de referência e a outra é proporcional; total zero não causa cálculo inválido. Sem transações no mês, apresentar estado vazio próprio em vez de barras fictícias.; R5: Recentes apresenta os cinco registros mais recentes de todo o histórico, ordenados por data decrescente e depois pelo cadastro mais recente, como na gestão de transações. Com menos de cinco, mostrar somente os existentes. Trocar o mês não filtra essa lista.; CA4: Sem registros, apresentar zeros e orientação de início, sem valores fictícios. Em um mês sem movimento, mas com histórico em outros meses, apresentar somente os indicadores mensais vazios, preservando saldo e recentes do histórico.

### CT-009 — Proporções das barras

Verificação: Usar somas diferentes positivas e comparar legenda,valores e extensões.

Resultado esperado: Maior soma ocupa referência e outra proporcional,com duas barras identificadas corretamente.

Origem no requisito: R4: O balanço compara receitas e despesas do mês em duas barras, com legenda e valores. A maior soma positiva ocupa a extensão de referência e a outra é proporcional; total zero não causa cálculo inválido. Sem transações no mês, apresentar estado vazio próprio em vez de barras fictícias.; CA5: Comparar o gráfico com os totais mensais; legenda, valores e proporções das duas barras correspondem às somas. Um tipo com soma zero e outro positivo continua apresentável; ausência completa de movimentos usa o estado vazio.

### CT-010 — Um tipo zerado

Verificação: Usar um tipo sem soma e outro positivo no período.

Resultado esperado: Gráfico e valores apresentáveis,sem divisão/cálculo inválido. Ausência completa de transações usa estado vazio.

Origem no requisito: R4: O balanço compara receitas e despesas do mês em duas barras, com legenda e valores. A maior soma positiva ocupa a extensão de referência e a outra é proporcional; total zero não causa cálculo inválido. Sem transações no mês, apresentar estado vazio próprio em vez de barras fictícias.; CA5: Comparar o gráfico com os totais mensais; legenda, valores e proporções das duas barras correspondem às somas. Um tipo com soma zero e outro positivo continua apresentável; ausência completa de movimentos usa o estado vazio.

## Recentes e integração

### CT-011 — Cinco recentes e empate

Verificação: Usar mais de cinco registros com datas empatadas e cadastros em ordem conhecida.

Resultado esperado: No máximo os cinco mais recentes por data e cadastro; mês selecionado não filtra a lista.

Origem no requisito: R5: Recentes apresenta os cinco registros mais recentes de todo o histórico, ordenados por data decrescente e depois pelo cadastro mais recente, como na gestão de transações. Com menos de cinco, mostrar somente os existentes. Trocar o mês não filtra essa lista.; CA6: Com mais de cinco registros e datas empatadas, conferir os cinco recentes conforme R5. Com menos registros, não completar a lista com exemplos. Abrir detalhes e Ver todas leva aos dados próprios usando a gestão de transações.

### CT-012 — Menos de cinco

Verificação: Abrir com menos de cinco registros reais.

Resultado esperado: Mostrar somente existentes,sem completar com exemplos.

Origem no requisito: R5: Recentes apresenta os cinco registros mais recentes de todo o histórico, ordenados por data decrescente e depois pelo cadastro mais recente, como na gestão de transações. Com menos de cinco, mostrar somente os existentes. Trocar o mês não filtra essa lista.; CA6: Com mais de cinco registros e datas empatadas, conferir os cinco recentes conforme R5. Com menos registros, não completar a lista com exemplos. Abrir detalhes e Ver todas leva aos dados próprios usando a gestão de transações.

### CT-013 — Detalhes e histórico

Verificação: Abrir detalhes de um recente e acionar Ver todas.

Resultado esperado: Levar aos dados próprios e ao histórico do fornecedor,com todos os campos acessíveis no detalhe.

Origem no requisito: R5: Recentes apresenta os cinco registros mais recentes de todo o histórico, ordenados por data decrescente e depois pelo cadastro mais recente, como na gestão de transações. Com menos de cinco, mostrar somente os existentes. Trocar o mês não filtra essa lista.; R6: Consultas, contagens e totais usam somente transações persistidas do titular. Ao acessar ou atualizar a Visão geral, buscar o estado salvo no sistema. Após concluir operações financeiras iniciadas no dashboard, atualizar seus valores e lista. Esta entrega não define atualização automática contínua entre sessões.; CA6: Com mais de cinco registros e datas empatadas, conferir os cinco recentes conforme R5. Com menos registros, não completar a lista com exemplos. Abrir detalhes e Ver todas leva aos dados próprios usando a gestão de transações.

### CT-014 — Cadastro pelo dashboard

Verificação: Salvar nova transação usando a ação da página e comparar antes/depois.

Resultado esperado: Atualizar saldo,indicadores mensais,barras,resultado e recentes conforme os recortes aplicáveis e o estado salvo.

Origem no requisito: R6: Consultas, contagens e totais usam somente transações persistidas do titular. Ao acessar ou atualizar a Visão geral, buscar o estado salvo no sistema. Após concluir operações financeiras iniciadas no dashboard, atualizar seus valores e lista. Esta entrega não define atualização automática contínua entre sessões.; CA7: Cadastrar, editar e excluir uma transação pelas ações disponíveis no dashboard; após cada sucesso, saldo, totais, contagens, barras, resultado e recentes refletem os registros salvos segundo seus respectivos recortes. Cancelamento ou falha não aplica alteração fictícia.

### CT-015 — Edição pelo detalhe

Verificação: Editar transação pelos detalhes acessíveis a partir da página,incluindo mudança de mês/tipo/data aplicável.

Resultado esperado: Recalcular os indicadores e posição nos recentes segundo dados persistidos,sem duplicação ou recortes incorretos.

Origem no requisito: R6: Consultas, contagens e totais usam somente transações persistidas do titular. Ao acessar ou atualizar a Visão geral, buscar o estado salvo no sistema. Após concluir operações financeiras iniciadas no dashboard, atualizar seus valores e lista. Esta entrega não define atualização automática contínua entre sessões.; CA7: Cadastrar, editar e excluir uma transação pelas ações disponíveis no dashboard; após cada sucesso, saldo, totais, contagens, barras, resultado e recentes refletem os registros salvos segundo seus respectivos recortes. Cancelamento ou falha não aplica alteração fictícia.

### CT-016 — Exclusão pelo detalhe

Verificação: Excluir transação pela jornada fornecida e comparar números/lista.

Resultado esperado: Refletir remoção persistida em todos os indicadores aplicáveis e recentes.

Origem no requisito: R6: Consultas, contagens e totais usam somente transações persistidas do titular. Ao acessar ou atualizar a Visão geral, buscar o estado salvo no sistema. Após concluir operações financeiras iniciadas no dashboard, atualizar seus valores e lista. Esta entrega não define atualização automática contínua entre sessões.; CA7: Cadastrar, editar e excluir uma transação pelas ações disponíveis no dashboard; após cada sucesso, saldo, totais, contagens, barras, resultado e recentes refletem os registros salvos segundo seus respectivos recortes. Cancelamento ou falha não aplica alteração fictícia.

### CT-017 — Cancelamento e falha de operação

Verificação: Cancelar ou provocar falha de cadastro/edição/exclusão nas jornadas reutilizadas.

Resultado esperado: Não antecipar valores ou lista como se a alteração tivesse sido salva.

Origem no requisito: R6: Consultas, contagens e totais usam somente transações persistidas do titular. Ao acessar ou atualizar a Visão geral, buscar o estado salvo no sistema. Após concluir operações financeiras iniciadas no dashboard, atualizar seus valores e lista. Esta entrega não define atualização automática contínua entre sessões.; CA7: Cadastrar, editar e excluir uma transação pelas ações disponíveis no dashboard; após cada sucesso, saldo, totais, contagens, barras, resultado e recentes refletem os registros salvos segundo seus respectivos recortes. Cancelamento ou falha não aplica alteração fictícia.

## Permissões e apresentação

### CT-018 — Falha de consulta e retomada

Verificação: Provocar falha de consulta,restabelecer e tentar novamente.

Resultado esperado: Indicar indisponibilidade/nova tentativa,sem zero ou vazio como sucesso;após retomada,exibir valores reais.

Origem no requisito: R6: Consultas, contagens e totais usam somente transações persistidas do titular. Ao acessar ou atualizar a Visão geral, buscar o estado salvo no sistema. Após concluir operações financeiras iniciadas no dashboard, atualizar seus valores e lista. Esta entrega não define atualização automática contínua entre sessões.; CA8: Provocar falha de consulta; apresentar indisponibilidade e nova tentativa sem afirmar saldo zero ou ausência de registros. Restabelecer a consulta e tentar novamente recupera os valores reais.

### CT-019 — Titulares distintos

Verificação: Abrir e consultar sob duas contas com dados diferentes,inclusive acesso direto aos dados consultados.

Resultado esperado: Totais,contagens,gráfico e recentes somente do titular;nenhum dado alheio influencia os números.

Origem no requisito: R6: Consultas, contagens e totais usam somente transações persistidas do titular. Ao acessar ou atualizar a Visão geral, buscar o estado salvo no sistema. Após concluir operações financeiras iniciadas no dashboard, atualizar seus valores e lista. Esta entrega não define atualização automática contínua entre sessões.; R7: Apresentar valores em reais e datas em formato brasileiro. Distinguir receitas e despesas por identificação, sinal e aparência, mantendo a linguagem visual FinAI. Não usar números de demonstração ou resultados derivados de outro titular.; CA9: Usar contas com dados distintos; cada uma visualiza somente seus próprios totais, contagens, gráfico e recentes. Visitantes e contas sem confirmação não acessam o dashboard conforme a Feature de acesso.

### CT-020 — Visitante e não-confirmado

Verificação: Tentar abrir o dashboard sem sessão e com conta não confirmada.

Resultado esperado: Restringir conforme a Feature de acesso,sem apresentar finanças.

Origem no requisito: CA9: Usar contas com dados distintos; cada uma visualiza somente seus próprios totais, contagens, gráfico e recentes. Visitantes e contas sem confirmação não acessam o dashboard conforme a Feature de acesso.

### CT-021 — Composição responsiva e temas

Verificação: Comparar com design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md (#overview,.stats,.overview-grid,.assistant-teaser e lista) em computador/tablet/celular e claro/escuro/sistema,incluindo estados vazios/falhas.

Resultado esperado: Preservar cabeçalho/mês/ação,três cartões/saldo destacado,balanço,convite e recentes;lista compacta no celular mantém detalhes acessíveis e identidade FinAI.

Origem no requisito: R8: Preservar a composição #overview do design: cabeçalho, mês, ação Nova transação, três cartões de resumo com destaque no saldo geral, balanço do mês, convite do assistente e últimas movimentações com Ver todas. Usar a base visual aprovada, incluindo claro, escuro e acompanhar o sistema; no celular, adaptar grade, navegação e lista compacta sem perder acesso aos detalhes.; CA10: Conferir a composição da Visão geral em computador, tablet e celular nos temas claro, escuro e acompanhar o sistema; manter hierarquia, destaque do saldo, cartões, balanço e lista do design. O convite do assistente não simula uma funcionalidade antes da entrega responsável.

### CT-022 — Convite do assistente

Verificação: Abrir a página antes da entrega do Assistente e observar sua ação.

Resultado esperado: Convite visual permanece indisponível para uso,sem chat/IA simulados nem bloqueio do aceite do dashboard.

Origem no requisito: R8: Preservar a composição #overview do design: cabeçalho, mês, ação Nova transação, três cartões de resumo com destaque no saldo geral, balanço do mês, convite do assistente e últimas movimentações com Ver todas. Usar a base visual aprovada, incluindo claro, escuro e acompanhar o sistema; no celular, adaptar grade, navegação e lista compacta sem perder acesso aos detalhes.; CA10: Conferir a composição da Visão geral em computador, tablet e celular nos temas claro, escuro e acompanhar o sistema; manter hierarquia, destaque do saldo, cartões, balanço e lista do design. O convite do assistente não simula uma funcionalidade antes da entrega responsável.

### CT-023 — Atualizar dados salvos

Verificação: Alterar registros no sistema e acessar/atualizar novamente Visão geral.

Resultado esperado: Buscar o estado persistido atual;respeitar recortes e não usar dados locais como fonte financeira;não exigir polling contínuo entre sessões.

Origem no requisito: R6: Consultas, contagens e totais usam somente transações persistidas do titular. Ao acessar ou atualizar a Visão geral, buscar o estado salvo no sistema. Após concluir operações financeiras iniciadas no dashboard, atualizar seus valores e lista. Esta entrega não define atualização automática contínua entre sessões.; CA7: Cadastrar, editar e excluir uma transação pelas ações disponíveis no dashboard; após cada sucesso, saldo, totais, contagens, barras, resultado e recentes refletem os registros salvos segundo seus respectivos recortes. Cancelamento ou falha não aplica alteração fictícia.

## Documento a anexar — incluído nesta aprovação final

- Destino: [QA] [WEB] [USUARIO] Dashboard financeiro
- Arquivo: [condicoes-teste-r001.docx](file:///C:/Users/maari/Herd/github/fin-ai/docs/harness/features/1016106-dashboard-financeiro/slices/condicoes-teste-r001.docx)
- Revisão: 001
- Tamanho: 6310 bytes
- SHA-256: `51075c45dbc5f374be9f6a7615984f577ad5d7c5f9fbc5371484fceded4637f9`
- Descrição do anexo: Condições de teste — revisão 001
- A aprovação autoriza acrescentar exatamente este documento, preservando os demais campos e anexos da QA.
