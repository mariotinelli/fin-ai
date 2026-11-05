# Publicação das filhas de [WEB] [USUARIO] Dashboard financeiro

Item pai Redmine: `1015912`

## Campos nativos aprovados

- Projeto: `65224`
- Pai nativo: `1015912`
- Tracker da mãe: Feature (`2`)
- Tracker DEV: Task (`4`)
- Tracker QA: Deliverable (`5`)
- Status inicial: New (`1`)
- Prioridade inicial: Normal (`4`, regra fixa)
- Categoria herdada: `None`
- Versão herdada: `20355`
- Responsável, início e vencimento: vazios

## Campos nativos e descrições

### [DEV] [WEB] [USUARIO] Dashboard financeiro - Indicadores e consulta por mês

- Chave interna: `dev-1`
- Tipo: DEV
- Estimativa: 1.5h
- Payload SHA-256: `8b3272f501149be7f783fa97f34bbed1ce904b5a2a6192e4903c2b2c09226c37`

## Entrega

Substituir os placeholders por saldo geral e totais mensais reais do titular, com seleção do mês, comparação simples e resultado mensal coerentes. Reutilizar os cálculos de Gestão de transações.

## Escopo e limites

Não reimplementa cálculo de competência, não antecipa futuras nem cria projeções/relatórios avançados. Recentes é outra entrega; a preservação do seu conjunto na troca de mês é conferida na integração.

## Critérios de aceite

- Elegíveis são somente transações próprias não excluídas e com data até hoje em America/Sao_Paulo; dashboard exige autenticação e e-mail confirmado.
- Saldo geral soma receitas elegíveis menos despesas de todo histórico, aceita negativo e não muda por selecionar outro mês; sem saldo inicial separado.
- Totais mensais somam receitas/despesas elegíveis por data dentro do mês selecionado; atual só até hoje, passado seus registros, futuro sem antecipação.
- Comparação simples de receitas/despesas e resultado mensal usam exatamente os totais dos indicadores; resultado=receitas−despesas. Sem projeções, tendências ou relatórios avançados.
- Ao abrir o dashboard consultar valores atuais; mês inicial é o atual em Brasília, sem usar o calendário UTC incorretamente.
- Exibir valores em reais com duas casas, identificando saldo geral e mês selecionado.
- Abrir no mês atual de Brasília e mostrar só números/registros do titular autenticado e confirmado.
- Saldo, totais e resultado mensal correspondem a R2/R3/R6, inclusive negativo.
- Trocar mês altera somente totais/comparativo do período, não saldo geral nem conjunto de recentes.
- Sem movimentações mostrar R$0,00 e orientação de primeiro cadastro; só futuras mostrar zeros reais e orientação de agendamentos no histórico; mês vazio zera só totais, preservando saldo e recentes globais.
- Indicadores mostram carregamento durante consulta; falha mostra indisponibilidade e tentar novamente, sem substituir por zeros aparentando dados reais; sucesso posterior mostra valores reais.
- Nenhum usuário acessa indicadores de outra conta, inclusive tentativa direta de trocar identificador.

## Dependências

Para iniciar: layout e autenticação existentes e requisitos funcionais aprovados permitem preparar apresentação e casos de teste. Para concluir: consumir dados/cálculos reais de ‘[DEV] [WEB] [USUARIO] Gestão de transações - Agendamentos e competência financeira (#1015933)’, alimentados por ‘[DEV] [WEB] [USUARIO] Gestão de transações - Cadastro e conferência de uma transação própria (#1015930)’; integração com ‘Dashboard financeiro - Movimentações recentes e detalhes’ verifica que trocar mês não muda recentes. Não concluir com dados simulados.

## Referências

Item pai Redmine #1015912; regras/critérios R1, R2, R3, R6, R7-abertura, R8-valores, CA1, CA2, CA3, CA6-indicadores, CA9-indicadores, CA10-indicadores.

<!-- project-slices-child:1ba44f48352382b8269a32a367c27279a9eb94b263cd596ed7920a5779769918 -->


### [DEV] [WEB] [USUARIO] Dashboard financeiro - Movimentações recentes e detalhes

- Chave interna: `dev-2`
- Tipo: DEV
- Estimativa: 1.5h
- Payload SHA-256: `ab3a45493aa13508bf18f101835835eac0f2b9fc48dded05f149328ecbb00994`

## Entrega

Apresentar as cinco movimentações elegíveis mais recentes do titular, independentemente do mês dos indicadores, com abertura da consulta individual existente.

## Escopo e limites

Não cria outra tela de detalhes nem usa o mês selecionado para restringir a lista. Operações e retorno integrado pertencem à entrega específica.

## Critérios de aceite

- Recentes usa todo histórico elegível, independente do mês, data decrescente e cadastro mais recente em empate, limite5; com menos5 exibe todos e futuras só entram na data.
- Identificar que recentes considera todo histórico até hoje; listar descrição, tipo, valor, categoria e data, com campos completos nos detalhes se layout compacto reduzir a lista.
- Mostrar cinco elegíveis mais recentes por data/cadastro ou todos se menos5, incluindo outros meses.
- Sem elegíveis recentes fica vazio; só futuras não preenche recentes com agendadas e informa consulta pelo histórico.
- Abrir detalhes reutiliza a consulta de Gestão de transações, sem construir leitura duplicada.
- Lista mostra carregamento/indisponibilidade e nova tentativa quando sua leitura falha; não confundir falha com lista realmente vazia.
- Recentes/detalhes não revelam registros alheios; transação removida antes de abrir informa indisponibilidade e permite atualizar a lista.

## Dependências

Para iniciar: layout e contrato funcional aprovados permitem preparar lista e casos de teste. Para concluir: integrar registros/leitura individual de ‘[DEV] [WEB] [USUARIO] Gestão de transações - Cadastro e conferência de uma transação própria (#1015930)’ e elegibilidade de ‘[DEV] [WEB] [USUARIO] Gestão de transações - Agendamentos e competência financeira (#1015933)’; lista e detalhe devem usar dados reais, sem implementar essas capacidades novamente.

## Referências

Item pai Redmine #1015912; regras/critérios R4, R8-recentes, CA5, CA6-recentes, CA7-detalhes, CA9-recentes, CA10-recentes.

<!-- project-slices-child:581857ee0b7442f1d5cf5e4d402d194495ee2d791c6972678eaccc9b8556822e -->


### [DEV] [WEB] [USUARIO] Dashboard financeiro - Operações e atualização do dashboard

- Chave interna: `dev-3`
- Tipo: DEV
- Estimativa: 1.5h
- Payload SHA-256: `a2248955fcd414bb6437e0a85bddeb887e93afb3e572a547c90320fc9b299165`

## Entrega

Conectar cadastro e histórico existentes ao dashboard e atualizar os indicadores e recentes após operações concluídas ou retorno, preservando valores ao cancelar ou falhar.

## Escopo e limites

Não reimplementa cadastro, edição, exclusão ou histórico. Sem atualização contínua da tela ociosa nem sincronização instantânea entre dispositivos.

## Critérios de aceite

- Duplicados permitidos contam individualmente; edição/exclusão recalculam indicadores e podem mudar recentes.
- Ao retornar de outras áreas e após alteração concluída no dashboard consultar valores atuais. Tela ociosa na virada só precisa atualizar ao ser consultada novamente; não exige polling nem sincronização instantânea entre dispositivos.
- Futuras não entram em indicadores/recentes antes da data; próxima consulta após início da data em Brasília inclui automaticamente, sem confirmar pagamento/recebimento.
- Nova transação reutiliza cadastro; Ver todas abre histórico integral, sem transportar filtro mensal que contradiga recentes globais.
- Cadastro/edição/exclusão concluídos a partir do dashboard atualizam números/recentes sem recarga manual; cancelar conserva valores; retornar de outras áreas consulta dados atuais.
- Fluxos alternativos: só refletir alterações efetivamente persistidas; cancelamento ou falha das operações não gera alteração financeira falsa.

## Dependências

Para iniciar: ‘Dashboard financeiro - Indicadores e consulta por mês’ e ‘Dashboard financeiro - Movimentações recentes e detalhes’ fornecem os blocos a conectar. Para concluir: integrar ‘[DEV] [WEB] [USUARIO] Gestão de transações - Cadastro e conferência de uma transação própria (#1015930)’, ‘[DEV] [WEB] [USUARIO] Gestão de transações - Histórico por período (#1015931)’, ‘[DEV] [WEB] [USUARIO] Gestão de transações - Edição de transação com efeitos financeiros (#1015934)’ e ‘[DEV] [WEB] [USUARIO] Gestão de transações - Exclusão confirmada com efeito único (#1015935)’, com os cálculos de ‘[DEV] [WEB] [USUARIO] Gestão de transações - Agendamentos e competência financeira (#1015933)’. Operações reais e seus efeitos devem estar verificados; navegação isolada não conclui.

## Referências

Item pai Redmine #1015912; regras/critérios R5, R7-retorno, CA4, CA7-atalhos, CA8, F-persistencia.

<!-- project-slices-child:85ff1eb34d7c936fc3d8273754e6f5adfd026391a6e043c0e0071e22afa996fb -->


### [QA] [WEB] [USUARIO] Dashboard financeiro

- Chave interna: `qa`
- Tipo: QA
- Estimativa: 1.5h
- Payload SHA-256: `c50c39e14c9a3f876b6bf76bd1b40ab33991157612708df3721892c64b384cbe`

## Objetivo

Verificar indicadores, recentes e operações integradas do dashboard com dados reais do próprio usuário.

## Jornadas integradas

- CT-001: Com duas contas, registros excluídos/futuros e sessão ausente/não confirmada, abrir dashboard. Resultado esperado: Somente titular habilitado acessa seus dados elegíveis; não inclui excluídos, futuros ou dados alheios.
- CT-002: Usar receita100/despesa30 em novembro e receita20/despesa5 em dezembro, hoje01/12; trocar meses e testar conta apenas com despesa10. Resultado esperado: Saldo85 em ambos os meses; conta só com despesa tem saldo-10; não há saldo inicial.
- CT-003: Na massa de referência selecionar novembro, dezembro e janeiro futuro, com uma receita futura999 em02/12. Resultado esperado: Novembro100/30; dezembro20/5; janeiro0/0; futura999 não entra.
- CT-004: Preparar seis elegíveis de meses diferentes, dois na mesma data com cadastros distintos, mais futura/excluída; repetir com três elegíveis e trocar mês. Resultado esperado: Exibe cinco na ordem definida ou os três existentes; troca de mês não altera conjunto; futura/excluída ausentes.
- CT-005: Cadastrar dois registros iguais a partir do dashboard, editar um e excluir o outro, verificando indicadores e recentes a cada conclusão. Resultado esperado: Ambos inicialmente contam; operações independentes atualizam números e seleção recentes sem contribuições obsoletas.
- CT-006: Comparar valores exibidos no resumo e indicadores para novembro100/30 e dezembro20/5, além de resultado negativo. Resultado esperado: Resumo usa mesmos totais; resultados70 e15 respectivamente, e negativo quando despesas excedem receitas.
- CT-007: Abrir durante intervalo em que UTC já é outro dia/mês mas Brasília ainda não; conferir mês e números. Resultado esperado: Seleciona mês de Brasília e dados reais atuais do titular.
- CT-008: Manter tela aberta na virada local, voltar a consultá-la; alterar transação em outra área e retornar. Resultado esperado: Próxima consulta incorpora data/operações; não depende de recarga manual após operação concluída nele, nem exige atualização contínua ociosa.
- CT-009: Conferir zero, centavos, positivos e negativos e rótulos do período. Resultado esperado: Valores em R$ com duas casas e escopo global/mensal claro.
- CT-010: Conferir rótulo dos recentes e abrir detalhes de um registro com campos reduzidos na lista compacta. Resultado esperado: Escopo global explícito e todos os campos disponíveis na leitura individual reutilizada.
- CT-011: Testar titular A, titular B, visitante e conta não confirmada no calendário controlado. Resultado esperado: Apenas acesso autorizado; nenhuma mistura entre contas e período inicial correto.
- CT-012: Comparar números visuais com massa persistida conhecida e resultado interno fornecido por transações. Resultado esperado: Correspondência exata sem cálculo paralelo divergente no dashboard.
- CT-013: Com elegíveis em meses diferentes, alternar seletor e comparar todos os blocos. Resultado esperado: Somente indicadores mensais/comparativo mudam pela seleção.
- CT-014: Massa: novembro100 receita/30 despesa; dezembro01 receita20/despesa5. Consultar30/11 23:59:59 e01/12 00:00:00 em Brasília. Resultado esperado: Saldo70→85; antes dezembro0/0 e registros01/12 fora dos recentes; depois dezembro20/5 e tornam-se elegíveis sem confirmação.
- CT-015: Criar mais5 elegíveis com empate, conferir IDs e ordem; repetir com menos5 e período selecionado distinto. Resultado esperado: Lista correta e global, sem preencher com registros fictícios.
- CT-016: Comparar conta vazia, conta só futura e conta com dados em outro mês; selecionar também mês futuro. Resultado esperado: Estados distinguem ausência geral, somente agendamentos e mês vazio; saldo/recentes de outros meses não desaparecem.
- CT-017: Abrir conta sem registros e só futuras. Resultado esperado: Lista vazia coerente e orientação adequada; nenhuma movimentação futura tratada como realizada.
- CT-018: Abrir registro recente e conferir dados na consulta individual fornecida. Resultado esperado: Mesmos dados e autorização; usa entrega Cadastro e conferência de uma transação própria #1015930.
- CT-019: Selecionar mês distinto e usar Ver todas; usar Nova transação e acesso de primeiro cadastro/agendamentos. Resultado esperado: Histórico integral de #1015931 e cadastro de #1015930 abrem corretamente, sem filtro mensal indevido.
- CT-020: Exercer as três operações reais e seus cancelamentos, além de alterar em outra área e retornar. Resultado esperado: Consulta atualizada após sucesso, preservada ao cancelar; nenhum dado simulado serve como aceite.
- CT-021: Controlar atraso e falha da leitura de indicadores, tentar novamente após restabelecer. Resultado esperado: Carregamento visível, erro distinguível de zero real e recuperação correta.
- CT-022: Provocar atraso/falha na consulta de recentes e repetir com leitura disponível. Resultado esperado: Estado de leitura apropriado e lista real recuperada.
- CT-023: Como B, tentar solicitar números de A. Resultado esperado: Acesso alheio negado ou resultado restrito a B, sem exposição.
- CT-024: Como B tentar detalhe de A; remover registro apresentado antes de abri-lo e atualizar lista. Resultado esperado: Sem dados alheios; indisponibilidade clara e lista pode ser atualizada.
- CT-025: Provocar cancelamento e falha controlada de persistência em cadastro, edição e exclusão iniciados pelo dashboard. Resultado esperado: Valores anteriores preservados; não apresentar alteração que não foi persistida.

## Regras e permissões

- Elegíveis são somente transações próprias não excluídas e com data até hoje em America/Sao_Paulo; dashboard exige autenticação e e-mail confirmado.
- Saldo geral soma receitas elegíveis menos despesas de todo histórico, aceita negativo e não muda por selecionar outro mês; sem saldo inicial separado.
- Totais mensais somam receitas/despesas elegíveis por data dentro do mês selecionado; atual só até hoje, passado seus registros, futuro sem antecipação.
- Recentes usa todo histórico elegível, independente do mês, data decrescente e cadastro mais recente em empate, limite5; com menos5 exibe todos e futuras só entram na data.
- Duplicados permitidos contam individualmente; edição/exclusão recalculam indicadores e podem mudar recentes.
- Comparação simples de receitas/despesas e resultado mensal usam exatamente os totais dos indicadores; resultado=receitas−despesas. Sem projeções, tendências ou relatórios avançados.
- Ao abrir o dashboard consultar valores atuais; mês inicial é o atual em Brasília, sem usar o calendário UTC incorretamente.
- Ao retornar de outras áreas e após alteração concluída no dashboard consultar valores atuais. Tela ociosa na virada só precisa atualizar ao ser consultada novamente; não exige polling nem sincronização instantânea entre dispositivos.
- Exibir valores em reais com duas casas, identificando saldo geral e mês selecionado.
- Identificar que recentes considera todo histórico até hoje; listar descrição, tipo, valor, categoria e data, com campos completos nos detalhes se layout compacto reduzir a lista.

## Impactos relacionados

- Reutilizar operações/cálculos de Gestão de transações; a conclusão exige as capacidades reais #1015930, #1015931, #1015933, #1015934 e #1015935 integradas.
- Preservar a independência de saldo/recentes frente ao seletor de mês e o isolamento do usuário em consultas e detalhes.
- Sem exigir atualização contínua ociosa, projeções, API adicional ou funcionamento do assistente.

## Critérios de conclusão

- Executar CT-001 a CT-025, registrando massa, instante de Brasília, resultado esperado/observado e evidências de interface/integração.
- Conferir as três operações reais, cancelamentos/falhas, retorno de outras áreas e nova consulta após virada; mocks não substituem prova de integração das fornecedoras.
- Falhas de consulta devem ser distintas de dados vazios; cada nova tentativa bem-sucedida deve recuperar os valores reais.
- Registrar desvios reproduzíveis e impedimentos de capacidade/ambiente. Tarefa fornecedora publicada ou em New não comprova integração concluída.

## Referências

Item pai Redmine #1015912; regras/critérios R1, R2, R3, R4, R5, R6, R7-abertura, R7-retorno, R8-valores, R8-recentes, CA1, CA2, CA3, CA4, CA5, CA6-indicadores, CA6-recentes, CA7-detalhes, CA7-atalhos, CA8, CA9-indicadores, CA9-recentes, CA10-indicadores, CA10-recentes, F-persistencia.

<!-- project-slices-child:dfd7dd3b0367dba0e0cd2b439f386f2bfdfe6eadf905b8c776a749edd059ae06 -->


## Bloqueios nativos

- [DEV] [WEB] [USUARIO] Dashboard financeiro - Indicadores e consulta por mês bloqueia [DEV] [WEB] [USUARIO] Dashboard financeiro - Operações e atualização do dashboard (`blocks`).
- [DEV] [WEB] [USUARIO] Dashboard financeiro - Movimentações recentes e detalhes bloqueia [DEV] [WEB] [USUARIO] Dashboard financeiro - Operações e atualização do dashboard (`blocks`).
- [DEV] [WEB] [USUARIO] Dashboard financeiro - Indicadores e consulta por mês bloqueia [QA] [WEB] [USUARIO] Dashboard financeiro (`blocks`).
- [DEV] [WEB] [USUARIO] Dashboard financeiro - Movimentações recentes e detalhes bloqueia [QA] [WEB] [USUARIO] Dashboard financeiro (`blocks`).
- [DEV] [WEB] [USUARIO] Dashboard financeiro - Operações e atualização do dashboard bloqueia [QA] [WEB] [USUARIO] Dashboard financeiro (`blocks`).

# Condições de teste

## Contexto

Preparar duas contas confirmadas, uma não confirmada, dados persistidos de novembro/dezembro, futuras/excluídas, mais de5 elegíveis e empates por data. Relógio controlado em America/Sao_Paulo, falhas de leitura/persistência reproduzíveis. Verificar números na interface contra massa independente e capacidades reais das tarefas1015930/31/33/34/35; não concluir com dados simulados. Cada cenário começa com massa própria. Não foram executadas estas condições.

### CT-001 — R1 — Indicadores e consulta por mês

Verificação: Com duas contas, registros excluídos/futuros e sessão ausente/não confirmada, abrir dashboard.

Resultado esperado: Somente titular habilitado acessa seus dados elegíveis; não inclui excluídos, futuros ou dados alheios.

Origem no requisito: R1: Elegíveis são somente transações próprias não excluídas e com data até hoje em America/Sao_Paulo; dashboard exige autenticação e e-mail confirmado.

### CT-002 — R2 — Indicadores e consulta por mês

Verificação: Usar receita100/despesa30 em novembro e receita20/despesa5 em dezembro, hoje01/12; trocar meses e testar conta apenas com despesa10.

Resultado esperado: Saldo85 em ambos os meses; conta só com despesa tem saldo-10; não há saldo inicial.

Origem no requisito: R2: Saldo geral soma receitas elegíveis menos despesas de todo histórico, aceita negativo e não muda por selecionar outro mês; sem saldo inicial separado.

### CT-003 — R3 — Indicadores e consulta por mês

Verificação: Na massa de referência selecionar novembro, dezembro e janeiro futuro, com uma receita futura999 em02/12.

Resultado esperado: Novembro100/30; dezembro20/5; janeiro0/0; futura999 não entra.

Origem no requisito: R3: Totais mensais somam receitas/despesas elegíveis por data dentro do mês selecionado; atual só até hoje, passado seus registros, futuro sem antecipação.

### CT-004 — R4 — Movimentações recentes e detalhes

Verificação: Preparar seis elegíveis de meses diferentes, dois na mesma data com cadastros distintos, mais futura/excluída; repetir com três elegíveis e trocar mês.

Resultado esperado: Exibe cinco na ordem definida ou os três existentes; troca de mês não altera conjunto; futura/excluída ausentes.

Origem no requisito: R4: Recentes usa todo histórico elegível, independente do mês, data decrescente e cadastro mais recente em empate, limite5; com menos5 exibe todos e futuras só entram na data.

### CT-005 — R5 — Operações e atualização do dashboard

Verificação: Cadastrar dois registros iguais a partir do dashboard, editar um e excluir o outro, verificando indicadores e recentes a cada conclusão.

Resultado esperado: Ambos inicialmente contam; operações independentes atualizam números e seleção recentes sem contribuições obsoletas.

Origem no requisito: R5: Duplicados permitidos contam individualmente; edição/exclusão recalculam indicadores e podem mudar recentes.

### CT-006 — R6 — Indicadores e consulta por mês

Verificação: Comparar valores exibidos no resumo e indicadores para novembro100/30 e dezembro20/5, além de resultado negativo.

Resultado esperado: Resumo usa mesmos totais; resultados70 e15 respectivamente, e negativo quando despesas excedem receitas.

Origem no requisito: R6: Comparação simples de receitas/despesas e resultado mensal usam exatamente os totais dos indicadores; resultado=receitas−despesas. Sem projeções, tendências ou relatórios avançados.

### CT-007 — R7-abertura — Indicadores e consulta por mês

Verificação: Abrir durante intervalo em que UTC já é outro dia/mês mas Brasília ainda não; conferir mês e números.

Resultado esperado: Seleciona mês de Brasília e dados reais atuais do titular.

Origem no requisito: R7-abertura: Ao abrir o dashboard consultar valores atuais; mês inicial é o atual em Brasília, sem usar o calendário UTC incorretamente.

### CT-008 — R7-retorno — Operações e atualização do dashboard

Verificação: Manter tela aberta na virada local, voltar a consultá-la; alterar transação em outra área e retornar.

Resultado esperado: Próxima consulta incorpora data/operações; não depende de recarga manual após operação concluída nele, nem exige atualização contínua ociosa.

Origem no requisito: R7-retorno: Ao retornar de outras áreas e após alteração concluída no dashboard consultar valores atuais. Tela ociosa na virada só precisa atualizar ao ser consultada novamente; não exige polling nem sincronização instantânea entre dispositivos.

### CT-009 — R8-valores — Indicadores e consulta por mês

Verificação: Conferir zero, centavos, positivos e negativos e rótulos do período.

Resultado esperado: Valores em R$ com duas casas e escopo global/mensal claro.

Origem no requisito: R8-valores: Exibir valores em reais com duas casas, identificando saldo geral e mês selecionado.

### CT-010 — R8-recentes — Movimentações recentes e detalhes

Verificação: Conferir rótulo dos recentes e abrir detalhes de um registro com campos reduzidos na lista compacta.

Resultado esperado: Escopo global explícito e todos os campos disponíveis na leitura individual reutilizada.

Origem no requisito: R8-recentes: Identificar que recentes considera todo histórico até hoje; listar descrição, tipo, valor, categoria e data, com campos completos nos detalhes se layout compacto reduzir a lista.

### CT-011 — CA1 — Indicadores e consulta por mês

Verificação: Testar titular A, titular B, visitante e conta não confirmada no calendário controlado.

Resultado esperado: Apenas acesso autorizado; nenhuma mistura entre contas e período inicial correto.

Origem no requisito: CA1: Abrir no mês atual de Brasília e mostrar só números/registros do titular autenticado e confirmado.

### CT-012 — CA2 — Indicadores e consulta por mês

Verificação: Comparar números visuais com massa persistida conhecida e resultado interno fornecido por transações.

Resultado esperado: Correspondência exata sem cálculo paralelo divergente no dashboard.

Origem no requisito: CA2: Saldo, totais e resultado mensal correspondem a R2/R3/R6, inclusive negativo.

### CT-013 — CA3 — Indicadores e consulta por mês

Verificação: Com elegíveis em meses diferentes, alternar seletor e comparar todos os blocos.

Resultado esperado: Somente indicadores mensais/comparativo mudam pela seleção.

Origem no requisito: CA3: Trocar mês altera somente totais/comparativo do período, não saldo geral nem conjunto de recentes.

### CT-014 — CA4 — Operações e atualização do dashboard

Verificação: Massa: novembro100 receita/30 despesa; dezembro01 receita20/despesa5. Consultar30/11 23:59:59 e01/12 00:00:00 em Brasília.

Resultado esperado: Saldo70→85; antes dezembro0/0 e registros01/12 fora dos recentes; depois dezembro20/5 e tornam-se elegíveis sem confirmação.

Origem no requisito: CA4: Futuras não entram em indicadores/recentes antes da data; próxima consulta após início da data em Brasília inclui automaticamente, sem confirmar pagamento/recebimento.

### CT-015 — CA5 — Movimentações recentes e detalhes

Verificação: Criar mais5 elegíveis com empate, conferir IDs e ordem; repetir com menos5 e período selecionado distinto.

Resultado esperado: Lista correta e global, sem preencher com registros fictícios.

Origem no requisito: CA5: Mostrar cinco elegíveis mais recentes por data/cadastro ou todos se menos5, incluindo outros meses.

### CT-016 — CA6-indicadores — Indicadores e consulta por mês

Verificação: Comparar conta vazia, conta só futura e conta com dados em outro mês; selecionar também mês futuro.

Resultado esperado: Estados distinguem ausência geral, somente agendamentos e mês vazio; saldo/recentes de outros meses não desaparecem.

Origem no requisito: CA6-indicadores: Sem movimentações mostrar R$0,00 e orientação de primeiro cadastro; só futuras mostrar zeros reais e orientação de agendamentos no histórico; mês vazio zera só totais, preservando saldo e recentes globais.

### CT-017 — CA6-recentes — Movimentações recentes e detalhes

Verificação: Abrir conta sem registros e só futuras.

Resultado esperado: Lista vazia coerente e orientação adequada; nenhuma movimentação futura tratada como realizada.

Origem no requisito: CA6-recentes: Sem elegíveis recentes fica vazio; só futuras não preenche recentes com agendadas e informa consulta pelo histórico.

### CT-018 — CA7-detalhes — Movimentações recentes e detalhes

Verificação: Abrir registro recente e conferir dados na consulta individual fornecida.

Resultado esperado: Mesmos dados e autorização; usa entrega Cadastro e conferência de uma transação própria #1015930.

Origem no requisito: CA7-detalhes: Abrir detalhes reutiliza a consulta de Gestão de transações, sem construir leitura duplicada.

### CT-019 — CA7-atalhos — Operações e atualização do dashboard

Verificação: Selecionar mês distinto e usar Ver todas; usar Nova transação e acesso de primeiro cadastro/agendamentos.

Resultado esperado: Histórico integral de #1015931 e cadastro de #1015930 abrem corretamente, sem filtro mensal indevido.

Origem no requisito: CA7-atalhos: Nova transação reutiliza cadastro; Ver todas abre histórico integral, sem transportar filtro mensal que contradiga recentes globais.

### CT-020 — CA8 — Operações e atualização do dashboard

Verificação: Exercer as três operações reais e seus cancelamentos, além de alterar em outra área e retornar.

Resultado esperado: Consulta atualizada após sucesso, preservada ao cancelar; nenhum dado simulado serve como aceite.

Origem no requisito: CA8: Cadastro/edição/exclusão concluídos a partir do dashboard atualizam números/recentes sem recarga manual; cancelar conserva valores; retornar de outras áreas consulta dados atuais.

### CT-021 — CA9-indicadores — Indicadores e consulta por mês

Verificação: Controlar atraso e falha da leitura de indicadores, tentar novamente após restabelecer.

Resultado esperado: Carregamento visível, erro distinguível de zero real e recuperação correta.

Origem no requisito: CA9-indicadores: Indicadores mostram carregamento durante consulta; falha mostra indisponibilidade e tentar novamente, sem substituir por zeros aparentando dados reais; sucesso posterior mostra valores reais.

### CT-022 — CA9-recentes — Movimentações recentes e detalhes

Verificação: Provocar atraso/falha na consulta de recentes e repetir com leitura disponível.

Resultado esperado: Estado de leitura apropriado e lista real recuperada.

Origem no requisito: CA9-recentes: Lista mostra carregamento/indisponibilidade e nova tentativa quando sua leitura falha; não confundir falha com lista realmente vazia.

### CT-023 — CA10-indicadores — Indicadores e consulta por mês

Verificação: Como B, tentar solicitar números de A.

Resultado esperado: Acesso alheio negado ou resultado restrito a B, sem exposição.

Origem no requisito: CA10-indicadores: Nenhum usuário acessa indicadores de outra conta, inclusive tentativa direta de trocar identificador.

### CT-024 — CA10-recentes — Movimentações recentes e detalhes

Verificação: Como B tentar detalhe de A; remover registro apresentado antes de abri-lo e atualizar lista.

Resultado esperado: Sem dados alheios; indisponibilidade clara e lista pode ser atualizada.

Origem no requisito: CA10-recentes: Recentes/detalhes não revelam registros alheios; transação removida antes de abrir informa indisponibilidade e permite atualizar a lista.

### CT-025 — F-persistencia — Operações e atualização do dashboard

Verificação: Provocar cancelamento e falha controlada de persistência em cadastro, edição e exclusão iniciados pelo dashboard.

Resultado esperado: Valores anteriores preservados; não apresentar alteração que não foi persistida.

Origem no requisito: F-persistencia: Fluxos alternativos: só refletir alterações efetivamente persistidas; cancelamento ou falha das operações não gera alteração financeira falsa.

## Documento a anexar — incluído nesta aprovação final

- Destino: [QA] [WEB] [USUARIO] Dashboard financeiro
- Arquivo: [condicoes-teste-r002.docx](file:///C:/Users/maari/Herd/github/fin-ai/docs/harness/features/1015912-dashboard-financeiro/slices/condicoes-teste-r002.docx)
- Revisão: 002
- Tamanho: 6216 bytes
- SHA-256: `bcb4e299b2d3b3ed2e914360bc1f3d622d5ea4a548b3919a24aee231f938629c`
- Descrição do anexo: Condições de teste — revisão 002
- A aprovação autoriza acrescentar exatamente este documento, preservando os demais campos e anexos da QA.
