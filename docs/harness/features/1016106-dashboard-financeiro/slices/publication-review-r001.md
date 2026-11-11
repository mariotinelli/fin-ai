# Prévia completa — Dashboard financeiro

Revisão001, ainda não aprovada. Uma decisão do tech lead cobre a decomposição, condições e exatamente as operações/vínculos abaixo. Nenhuma filha do Dashboard foi criada.

## Entregas e estimativas

| Entrega | Título | Esforço | Bloqueio de início |
| --- | --- | --- | --- |
| DEV | [DEV] [WEB] [USUARIO] Dashboard financeiro - Visão geral com saldo, balanço mensal e recentes | 4,5h | Cadastro/persistência #1016123 |
| QA | [QA] [WEB] [USUARIO] Dashboard financeiro | 2,5h | Novo DEV completo |

Total: **4,5h DEV + 2,5h QA = 7h** de esforço, não prazo de calendário.

A tela, cálculos e recortes formam uma entrega única verificável, dentro de6h. Não separar por camada ou fragmentar cartões/gráfico/recentes; reutilizar os fornecedores de cadastro,detalhes,histórico e manutenção. As avaliações independentes, analogias e justificativa final estão nas decisões da proposta,sem reestimar o trabalho que pertence a Transações.

## Dependências e vínculos exatos

- Criar `blocks` de [DEV] [WEB] [USUARIO] Gestão de transações - Cadastro de receitas e despesas com conferência do registro (#1016123) para o novo DEV de Dashboard,que consumirá os registros reais. Fonte específica publicada em New,sem pressupor implementação.
- Criar `blocks` do novo DEV para a nova QA do Dashboard.
- Os extremos novos serão exclusivamente os IDs devolvidos para estas duas criações,com os títulos/conteúdo desta prévia.
- Histórico #1016124 e manutenção #1016125 são necessários para concluir Ver todas e atualização após operações,mas não impedem iniciar agregados/composição depois do cadastro. O DEV não estará concluído sem essas integrações no aceite.
- Não criar aresta visual direta redundante: QA visual #1016117 já bloqueia #1016123. Não criar bloqueio pelo Assistente; manter seu convite visual indisponível antes da entrega responsável.
- Grafo relevante completo reutilizado da leitura final das19issues após Sequencing,com21relações; os dois novos vínculos não formam ciclos. Após criação,reler grafo antes de configurar relação externa. Mudança material exige delta; vinculação apenas aos IDs retornados já está abrangida.

## Sequencing — regra já autorizada pelo usuário

- Campo nativo Sequencing (2),em ordem contínua dos blocos do catálogo.
- Dashboard ainda sem filhas: permanece vazio até a publicação das duas filhas.
- Após publicação: mãe #1016106 =15; novo DEV =15; nova QA =16. Próximo número17.
- A regra mãe/primeira filha iguais e incremento das demais inclui QA. Assistente ainda sem filhas permanece vazio.
- Aplicar por operação separada que altera somente o campo Sequencing e verifica os demais campos,sem reescrever payloads/aprovações históricos. Recalcular/conferir o mapa no momento da publicação para detectar qualquer concorrência material.

## Campos e operações autorizáveis

- Pai nativo #1016106,[WEB] [USUARIO] Dashboard financeiro; estado New preservado.
- Criar uma Task DEV (4) e uma Deliverable QA (5),FinAi (65224),Sprint1 (20355),sem categoria,responsável ou datas.
- Filhas em New (1),prioridade Normal (4),com estimated_hours desta prévia.
- Criar/reconciliar os dois vínculos descritos,sem duplicar,alterar estados de pai/fornecedores ou relações anteriores.
- Gerar DOCX da fonte aprovada,fazer upload e associar somente à nova QA,preservando demais campos/anexos.
- Aplicar o Sequencing no mapa acima conforme a política já solicitada,sem alteração de conteúdo funcional.
- Pai consultado com children:sem filhas a adotar/excluir. Nenhuma task antiga é contexto/alvo.
- Descrições completas abaixo são a autoridade funcional. Após consentimento,helpers acrescentam marcadores técnicos de recuperação e vinculam metadados de aprovação/documento/IDs,sem nova confirmação equivalente. Diferença material interrompe para revisão.

## Documento de condições incluído nesta decisão

DOCX obrigatório com complemento Markdown: slices/condicoes-teste-r001.docx e slices/condicoes-teste-r001.md. Destino [QA] [WEB] [USUARIO] Dashboard financeiro,nova filha desta publicação.

Fonte: as23condições integrais desta revisão. Conforme a skill,o arquivo oficial é gerado após consentimento,o hash é vinculado ao plano e a associação é verificada no readback. Esta decisão autoriza geração/upload/anexo da mesma fonte,sem editar conteúdo; diferença material exige nova prévia.

## Descrições completas e campos por filha

### [DEV] [WEB] [USUARIO] Dashboard financeiro - Visão geral com saldo, balanço mensal e recentes

```json
{
  "project_id": 65224,
  "parent_issue_id": 1016106,
  "tracker_id": 4,
  "status_id": 1,
  "subject": "[DEV] [WEB] [USUARIO] Dashboard financeiro - Visão geral com saldo, balanço mensal e recentes",
  "assigned_to_id": null,
  "start_date": null,
  "due_date": null,
  "estimated_hours": 4.5,
  "priority_id": 4,
  "fixed_version_id": 20355
}
```

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


### [QA] [WEB] [USUARIO] Dashboard financeiro

```json
{
  "project_id": 65224,
  "parent_issue_id": 1016106,
  "tracker_id": 5,
  "status_id": 1,
  "subject": "[QA] [WEB] [USUARIO] Dashboard financeiro",
  "assigned_to_id": null,
  "start_date": null,
  "due_date": null,
  "estimated_hours": 2.5,
  "priority_id": 4,
  "fixed_version_id": 20355
}
```

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


## Condições de teste integrais

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

## Cobertura, inspeção e estimativas

A tabela completa está em [slices.md](slices.md). Uma entrega é responsável por todas as regras e critérios; as capacidades fornecidas por Transações e pela fundação visual são consumidas,sem duplicação.

- Fonte de escopo: requisito canônico #1016106, design normalizado e decisões anteriores; nenhuma task antiga é contexto ou prova de implementação.
- Inspeção por leitura do código, do protótipo e dos fornecedores publicados. Nenhum teste ou jornada foi executado. A rota/layout existente não comprova dashboard financeiro; fornecedores New não são capacidade pronta.
- Uma única entrega DEV é vertical e cobre a Visão geral completa em menos de6h. Não separar por consulta, gráfico ou frontend/backend: cartões,balanço e recentes formam uma mesma tela verificável. Reutilizar formulários/manutenção e duas barras simples, sem biblioteca analítica ou nova persistência.
- Avaliação independente A, estimate_visual_delivery:DEV3,5h eQA2h; destacou composição demonstrada, consultas próprias e reuso de transações. Avaliação B, estimate_visual_reuse:DEV4,5h eQA2,5h; destacou recortes distintos, estados e integração. Não receberam número candidato nem resultado da outra avaliação.
- Estimativa final do agente responsável:DEV4,5h para consultas próprias, composição responsiva, recortes e integração de cadastro/manutenção com estados;QA2,5h para preparar resultados conhecidos, conferir recortes/recentes, operações/falhas/titularidade/visual e registrar reteste delimitado. Total7h. É análise de trabalho restante, sem média automática ou tempo executado.
- Calibrações humanas anteriores foram consideradas como referências específicas: visualDEV2h/QA1,5h; acessoDEV1,5h/2h/2h eQA1h; transaçõesDEV2h cada/QA1,5h. Não são tempos medidos ou padrão universal; nenhum desconto por IA foi presumido.
- Bloqueio externo real: primeira capacidade persistida #1016123, sem criar provisório no pai porque existe fornecedor específico. Histórico #1016124 e manutenção #1016125 são integrações de conclusão, sem impedirem iniciar o restante; o DEV não pode ser declarado concluído sem seus critérios integrados. QA depende desse DEV completo. Não duplicar o marco visual transitivo nem criar bloqueio pelo Assistente.
- Política atual do usuário: Sequencing contínuo em ordem de catálogo, mãe/primeira filha com mesmo número, QA também incrementa, Features sem filhas vazias. Próximo número15: planejar mãeDashboard15,DEV15,QA16 e próximo17, mantendo o pai vazio até publicar filhas e reaplicar a regra ao conjunto. Não reescrever aprovações anteriores ou a sequência de criações histórica.
- Publicação proposta: uma Task DEV e uma Deliverable QA,New/Normal,pai1016106,versãoSprint1,sem responsável/datas; um vínculo DEV→QA e um #1016123→DEV, com IDs exclusivamente retornados nesta publicação. Gerar/anexar DOCX aprovado à QA; aplicar Sequencing em operação separada conforme política já autorizada, preservando outros campos.
