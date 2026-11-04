# Entrevista — Gestão de transações

Item 2/4 do catálogo aprovado. Cadastrar, editar, excluir e consultar receitas e despesas pessoais com categorias predefinidas e persistência isolada por usuário. Dependência Acesso à conta concluída no fluxo de requisitos, issue #1015909. Design apenas visual; comportamentos do protótipo não são decisões de produto.

## Rodada 1

Q4 — Campos e moeda: proposta de tipo (receita/despesa), valor em reais, descrição, categoria e data da movimentação, todos obrigatórios. Valor positivo; o tipo define entrada ou saída. Confirmar conjunto ou informar ajustes. Moeda BRL proposta pelo contexto brasileiro e referência visual, ainda sem decisão.

Q5 — Data futura: proposta de registrar somente movimentações já realizadas, com data de hoje ou passada. Alternativa: admitir movimentações futuras, exigindo definir quando afetam saldo e totais. Recomendação de não admitir futuras no MVP para manter os totais restritos ao realizado.

Pendências posteriores: categorias predefinidas, consulta e filtros, regras de edição e exclusão. Respostas ainda não recebidas.


## Resposta à rodada 1

Usuário: “q4. concordo q5. futuras também acho viavel”. Q4 resolvida com os campos obrigatórios propostos e valor positivo em reais. Q5 resolvida quanto à permissão de datas futuras; não implica recebimento/pagamento automático, recorrência ou uma regra de cálculo já aprovada.

## Rodada 2 — Q6 aberta

Q6 — Quando movimentações futuras afetam saldo e totais? Opções: (A) entram automaticamente na data informada, permanecendo fora dos totais até então; (B) ficam pendentes até confirmação de recebimento/pagamento pelo usuário, inclusive após a data prevista. Recomenda-se A para manter o MVP simples e baseado em data. B requer estado pendente/realizado e uma ação de confirmação. Exemplo: despesa de R$ 100 prevista para dia 20 entra nos totais no dia 20 em A, ou apenas quando confirmada em B. Outra regra pode ser indicada pelo usuário.

Decisão afeta o significado das transações e orientará posteriormente dashboard e consultas da IA. Não acrescenta por si só uma nova capacidade ao catálogo. Pendentes para rodadas seguintes: categorias, filtros, edição e exclusão.


## Resposta à rodada 2

Usuário: “concordo”, após recomendação explícita da opção A. Q6 resolvida: inclusão automática na data informada; futuras não entram no saldo e totais antes dessa data, sem confirmação manual. A resposta não autoriza recorrência, parcelamento ou pagamento efetivo externo.

## Rodada 3 — categorias e histórico

Q7 — Proposta de categorias predefinidas: receitas (Salário, Freelance, Rendimentos, Outras receitas); despesas (Alimentação, Moradia, Transporte, Saúde, Educação, Lazer, Compras, Outras despesas). Lista inspirada nos nomes da referência visual, apresentada como proposta, não requisito extraído do protótipo. Categorias distintas por tipo; sem criação ou edição pelo usuário conforme limite do catálogo. Confirmar lista ou ajustar nomes.

Q8 — Proposta para consulta: mês de referência com opção de todo o histórico, busca por descrição e filtros por tipo e categoria; mostrar também futuras com indicação de agendamento, mantendo-as fora dos totais antes da data. Recomenda-se para permitir localizar e corrigir tanto registros passados como futuros. Confirmar ou indicar outra necessidade.

Pendências posteriores: limites de valor/descrição, calendário de referência (data em que futuras entram nos totais), ordenação e paginação, edição/exclusão e seus efeitos. Nenhuma resposta foi presumida para Q7 e Q8.


## Resposta à rodada 3

Usuário: “concordo”. Q7 e Q8 resolvidas conforme as propostas: categorias separadas por tipo e consulta por mês/todo o histórico, descrição, tipo e categoria, incluindo futuras identificadas como agendadas.

## Rodada 4 — calendário e alterações

Q9 — Usar o horário de Brasília (America/Sao_Paulo) para definir hoje e a virada da data, de modo que uma transação do dia 20 conte a partir do início desse dia nesse calendário, independentemente do local de acesso? Recomendação de calendário único para um MVP em reais; alternativa de calendário individual exigiria definir a escolha do usuário.

Q10 — Permitir editar todos os campos de qualquer transação própria, passada ou futura, e excluir após confirmação, recalculando os totais imediatamente? Mover uma data passada para futura retira o valor dos totais atuais; excluir retira a movimentação do histórico e dos cálculos, sem opção de desfazer no MVP. Recomendação de correção direta; alternativa de restringir alterações de registros passados muda o resultado funcional.

Permanecem para proposta final os detalhes de limites de entrada, ordenação e paginação; não há decisões adicionais presumidas nesta rodada.


## Resposta à rodada 4 e revisão

Usuário: “concordo”. Q9 e Q10 resolvidas. Requisito completo preparado para revisão. R2 e R9 apresentam limites e detalhes de consulta como propostas explícitas; não foram atribuídas respostas adicionais ao usuário. Busca completa na Sprint 1 retornou somente #1015909 Acesso à conta, sem similaridade de objetivo com Gestão de transações. Sem categorias no projeto. Sequencing 2 = baseline 0 + posição 2. Plano inclui relação de bloqueio #1015909 para a nova issue. Nenhuma mutação remota executada.


Requisito e operações aprovados pelo usuário: “aprovado”. Consentimento registrado em 2026-11-04T19:31:04.975934+00:00.


Publicação concluída: #1015911, Sprint 1, Sequencing 2, status New preservado. Descrição integral validada; relação blocks #1015909 → #1015911, ID 763, confirmada nas duas issues.
