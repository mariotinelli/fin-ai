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
