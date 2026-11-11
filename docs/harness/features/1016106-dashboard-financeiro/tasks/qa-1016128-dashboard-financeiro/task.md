# [QA] [WEB] [USUARIO] Dashboard financeiro

- Redmine: `#1016128`
- Tipo: `QA`
- Tracker: Deliverable (`5`)
- Item pai: `#1016106`
- Estimativa: `2.5h`

## Descrição

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

## Relações

- `#1016127` blocks `#1016128`
