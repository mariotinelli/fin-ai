# [QA] [WEB] [USUARIO] Dashboard financeiro

- Redmine: `#1015940`
- Tipo: `QA`
- Tracker: Deliverable (`5`)
- Item pai: `#1015912`
- Estimativa: `1.5h`

## Descrição

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

## Relações

- `#1015937` blocks `#1015940`
- `#1015938` blocks `#1015940`
- `#1015939` blocks `#1015940`
