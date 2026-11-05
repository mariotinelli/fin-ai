# Revisão funcional — Gestão de transações — r005

Prévia pendente da revisão do tech lead. Nenhuma filha de Gestão de transações foi publicada. O requisito aprovado permanece intacto.

## O que mudou

- Cadastro inclui leitura do registro persistido e reabertura do mesmo endereço após sair/entrar. Histórico descobre o conjunto e abre essa mesma consulta; não entrega detalhes novamente.
- Histórico já inclui mês atual/outro mês/todos, ordenação, contagem e paginação de50. Busca apenas acrescenta descrição/tipo/categoria e preserva a navegação.
- Competência fornece indicação visível de agendada e prova numérica da capacidade interna, sem dashboard ou API adicional.
- As relações nativas abaixo expressam impedimentos de início. Condições de conclusão ficam explícitas nos critérios: edição e exclusão precisam integrar histórico e cálculos e provar os efeitos.
- A quantidade de seis cortes resultou dessas jornadas. Receita/despesa não foram separadas porque compartilham formulário, validações, propriedade e leitura. O teto foi conferido depois da definição e da estimativa, sem forçar quantidade ou diminuir horas para caber.

## Estimativas, reaproveitamento e incertezas

| Tarefa | Horas | Trabalho previsto | Reaproveitamento e verificação |
| --- | --- | --- | --- |
| Cadastro e conferência | 3h | Persistência/propriedade/categorias; formulário/validações; leitura individual/retorno autenticado; cancelamento/falha; regressões; revisão. | Reutiliza auth, layout, inputs e diálogos. Verificar centavos sem arredondamento e aceitação das datas extremas nos controles escolhidos. |
| Histórico por período | 2h | Consulta/ordem/paginação; apresentação/navegação/períodos; regressões/revisão. | Reutiliza leitura individual. Cobrir empates, 50/51 registros, mudança de mês e isolamento. |
| Busca e filtros | 2h | Comparação textual; combinação/limpeza/páginas; interface; regressões/revisão. | Reutiliza paginação. Resolver e verificar comparação sem acentos no SQLite efetivo; não presumir que collation padrão atende. |
| Agendamentos e competência | 2h | Data/classificação; cálculo por conta/período; integração visual; integração numérica; revisão. | Reutiliza registros e consultas. Cobrir UTC versus Brasília, virada do mês, futuras, excluídas, centavos e saldo negativo. |
| Edição com efeitos | 2h | Formulário/atualização; efeitos integrados; falhas/permissões/cancelamento; regressões/revisão. | Reutiliza validações, leitura individual e cálculo. Testes devem exercer edição real, não apenas alterar massa diretamente. |
| Exclusão com efeito único | 2h | Confirmação/atualização da interface; exclusão/indisponibilidade/repetição; efeitos/isolamento/regressões; revisão. | Reutiliza diálogo e cálculo. Cobrir repetição, falha e registros distintos com dados iguais. |
| QA integrada | 2h | Preparação; cadastro/limites; histórico/busca; competência; edição/exclusão; permissões/falhas; evidências. | Requer execução reproduzível da suíte e ambiente de interface com dados/falhas controláveis. Provisionar infraestrutura não está escondido nestas horas. |

Valores corrigidos por instrução explícita do tech lead: DEV 3/2/2/2/2/2h e QA 2h. Total DEV: **13h**. Total geral: **15h**. As estimativas independentes anteriores permanecem no histórico; estes valores não resultam de novo cálculo de esforço. Entregas, verificações e incertezas permanecem iguais.

## Como conferir os cálculos sem dashboard

Usuário autenticado com e-mail confirmado. Preparar duas contas, todas as categorias, valores/descrições/datas de limite, mais de50 registros, datas passadas/atuais/futuras, virada controlada em America/Sao_Paulo e falhas de persistência controladas. Condições futuras de QA, sem alegação de execução. Verificar na interface a indicação de agendada e usar testes de integração reproduzíveis da capacidade interna de cálculo, com banco de teste real, relógio controlado e sem substituir cálculo ou consulta por respostas simuladas. Não usar dashboard, endpoint novo ou script avulso. Registrar comando da suíte, revisão testada, massa, instante, esperado e observado. Massa M: usuário A com receita R$ 100,00 e despesa R$ 30,00 em 30/11/2026; receita R$ 20,00 e despesa R$ 5,00 em 01/12/2026; receita R$ 7,00 excluída em 30/11. Usuário B com receita R$ 900,00 em 30/11. Relógio em America/Sao_Paulo. Cada cenário recomeça da massa, sem depender do resultado de outro. Para efeitos de edição/exclusão, executar a operação real da aplicação antes de consultar os cálculos; alteração direta da massa não comprova integração da mutação.

| Cenário independente | Resultado esperado |
| --- | --- |
| Massa M em30/11/2026 23:59:59 Brasília | Saldo R$70; novembro receita100/despesa30; dezembro0/0; registros de01/12 agendados |
| Mesma massa em01/12/2026 00:00:00 Brasília | Saldo R$85; novembro100/30; dezembro20/5; registros de01/12 deixam de ser agendados |
| Em01/12, mover receita100 de30/11 para02/12 e devolver | Saldo85→-15→85; novembro receitas100→0→100 |
| Em01/12, alterar despesa30 para40 | Saldo75; novembro despesas40 |
| Em01/12, mudar despesa30 para receita30/categoria compatível | Saldo145; novembro receitas130/despesas0 |
| Em01/12, excluir despesa30 e repetir exclusão | Saldo85→115→115; novembro despesas0 |
| Cancelar ou falhar sem concluir edição/exclusão na massa original | Saldo85 e dados anteriores preservados |
| Conta só com despesa10 / receitas0,10+0,20 e despesa0,01 | Saldo-10 / saldo0,29 exato |

Os cenários com exclusão/edição usam a operação real da aplicação e depois consultam a capacidade de cálculo; não basta simular a alteração diretamente na massa. Não se exige script separado nem nova superfície de produto. A implementação posterior escolherá os arquivos e a organização dos testes existentes; a exigência aqui é a evidência do comportamento.

## Dependências para iniciar e para concluir

| Entrega | Para iniciar | Para concluir |
| --- | --- | --- |
| Cadastro/conferência | Auth existente | Salvar, ler persistência e reabrir após login |
| Histórico | Cadastro/conferência | Percorrer períodos/páginas e abrir leitura existente |
| Busca | Histórico | Combinar filtros e preservar navegação |
| Competência | Cadastro/conferência | Prova numérica e indicação integrada ao histórico |
| Edição | Cadastro/conferência | Histórico atualizado + cálculo integrado + efeitos antes/depois comprovados |
| Exclusão | Cadastro/conferência | Histórico atualizado + cálculo integrado + efeito único comprovado |
| QA | Todas as DEV completas | Evidências de interface e integração de todas as condições |

# Fatiamento de [WEB] [USUARIO] Gestão de transações

Revisão: 5  
Hash: `57ded1e557d2f64d63892edb9d4feecbce1944ffb5f362ebc4e779664fc6bb92`

## Prévia numerada

1. **[DEV] [WEB] [USUARIO] Gestão de transações - Cadastro e conferência de uma transação própria** — 3h
   - Entrega: Permitir cadastrar receita ou despesa e conferir imediatamente os campos lidos do registro persistido. O titular pode guardar o endereço dessa consulta individual, sair, entrar novamente e reabrir o mesmo registro para confirmar sua persistência.
   - Bloqueado por: Nenhum
   - Bloqueios externos: Nenhum
2. **[DEV] [WEB] [USUARIO] Gestão de transações - Histórico por período** — 2h
   - Entrega: Permitir descobrir e percorrer as próprias transações por período, abrindo a consulta individual já entregue no cadastro. Inclui mês atual, outro mês, histórico integral, ordenação, paginação e contagem.
   - Bloqueado por: 1
   - Bloqueios externos: Nenhum
3. **[DEV] [WEB] [USUARIO] Gestão de transações - Busca por descrição, tipo e categoria** — 2h
   - Entrega: Permitir localizar registros do histórico por trecho da descrição, tipo e categoria, combinados com o período. Reutiliza navegação, paginação e consulta individual já entregues.
   - Bloqueado por: 2
   - Bloqueios externos: Nenhum
4. **[DEV] [WEB] [USUARIO] Gestão de transações - Agendamentos e competência financeira** — 2h
   - Entrega: Identificar agendamentos nas consultas e aplicar a competência financeira em America/Sao_Paulo. Entrega a transição visível de agendada e os resultados de saldo e totais da capacidade interna, verificáveis sem dashboard.
   - Bloqueado por: 1
   - Bloqueios externos: Nenhum
5. **[DEV] [WEB] [USUARIO] Gestão de transações - Edição de transação com efeitos financeiros** — 2h
   - Entrega: Permitir corrigir todos os campos do mesmo registro próprio, reaproveitando formulário e consulta individual. A entrega inclui integrar e verificar o efeito financeiro real da alteração e atualizar a consulta.
   - Bloqueado por: 1
   - Bloqueios externos: Nenhum
6. **[DEV] [WEB] [USUARIO] Gestão de transações - Exclusão confirmada com efeito único** — 2h
   - Entrega: Permitir confirmar ou cancelar exclusão de registro próprio. A entrega remove sua contribuição financeira uma única vez, atualiza as consultas e preserva registros distintos com dados iguais.
   - Bloqueado por: 1
   - Bloqueios externos: Nenhum

## Cobertura

| Regra ou critério | Destino | Evidência |
| --- | --- | --- |
| R1: Tipo receita/despesa, valor positivo em reais, descrição, categoria e data são obrigatórios; tipo determina entrada ou saída. | Slice 1 | Capacidade financeira ausente na inspeção de app, rotas, migrações e páginas. Cadastro e conferência de uma transação própria é o único dono da entrega; preservações e integração são conferidas nos critérios, sem reimplementar leitura individual ou cálculo. |
| R2: Valor entre R$ 0,01 e R$ 999.999.999,99 com até duas casas; não arredondar entrada com precisão maior. Descrição entre 1 e 120 caracteres após aparar extremidades. Data válida de 01/01/1900 a 31/12/9999. | Slice 1 | Capacidade financeira ausente na inspeção de app, rotas, migrações e páginas. Cadastro e conferência de uma transação própria é o único dono da entrega; preservações e integração são conferidas nos critérios, sem reimplementar leitura individual ou cálculo. |
| R3: Oferecer somente receitas: Salário, Freelance, Rendimentos, Outras receitas; despesas: Alimentação, Moradia, Transporte, Saúde, Educação, Lazer, Compras, Outras despesas. Sem manutenção de categorias. | Slice 1 | Capacidade financeira ausente na inspeção de app, rotas, migrações e páginas. Cadastro e conferência de uma transação própria é o único dono da entrega; preservações e integração são conferidas nos critérios, sem reimplementar leitura individual ou cálculo. |
| R4: Vincular cadastro ao usuário autenticado com e-mail confirmado, sem aceitar outro proprietário; persistência permanece após sair e entrar. | Slice 1 | Capacidade financeira ausente na inspeção de app, rotas, migrações e páginas. Cadastro e conferência de uma transação própria é o único dono da entrega; preservações e integração são conferidas nos critérios, sem reimplementar leitura individual ou cálculo. |
| R5: Data define competência em America/Sao_Paulo; futura é agendada, aparece no histórico e não afeta saldo/totais até início da data. Inclusão automática, sem confirmação manual nem pagamento externo. | Slice 4 | Capacidade financeira ausente na inspeção de app, rotas, migrações e páginas. Agendamentos e competência financeira é o único dono da entrega; preservações e integração são conferidas nos critérios, sem reimplementar leitura individual ou cálculo. |
| R6: Saldo é receitas menos despesas de registros não excluídos até hoje; totais mensais usam data dentro do mês e até hoje. Mês futuro não realiza movimentações; saldo negativo permitido, sem saldo inicial separado. | Slice 4 | Capacidade financeira ausente na inspeção de app, rotas, migrações e páginas. Agendamentos e competência financeira é o único dono da entrega; preservações e integração são conferidas nos critérios, sem reimplementar leitura individual ou cálculo. |
| R7: Editar todos os campos próprios em qualquer data; tipo, valor, categoria e data atualizam valores aplicáveis. Passada/hoje para futura retira efeito; futura para hoje/passada inclui. | Slice 5 | Capacidade financeira ausente na inspeção de app, rotas, migrações e páginas. Edição de transação com efeitos financeiros é o único dono da entrega; preservações e integração são conferidas nos critérios, sem reimplementar leitura individual ou cálculo. |
| R8: Excluir somente após confirmação, removendo do histórico e cálculos, sem desfazer. | Slice 6 | Capacidade financeira ausente na inspeção de app, rotas, migrações e páginas. Exclusão confirmada com efeito único é o único dono da entrega; preservações e integração são conferidas nos critérios, sem reimplementar leitura individual ou cálculo. |
| R9: R9, busca e filtros: trecho da descrição sem distinguir caixa/acentos; tipo/categoria/período restringem o mesmo conjunto. Limpar filtros mostra todo o histórico; manter filtros entre páginas e retornar à primeira ao alterar um filtro. | Slice 3 | Capacidade financeira ausente na inspeção de app, rotas, migrações e páginas. Busca por descrição, tipo e categoria é o único dono da entrega; preservações e integração são conferidas nos critérios, sem reimplementar leitura individual ou cálculo. |
| R10-campos: R10 e dados percebidos, consulta individual: conferir descrição, tipo, valor em reais com centavos, categoria e data brasileira do registro persistido, inclusive ao reabrir após novo login. | Slice 1 | Capacidade financeira ausente na inspeção de app, rotas, migrações e páginas. Cadastro e conferência de uma transação própria é o único dono da entrega; preservações e integração são conferidas nos critérios, sem reimplementar leitura individual ou cálculo. |
| R10-agendada: R10: futuras mostram identificação de agendada, seguem ordenação por data sem fila separada; identificação cessa na data. | Slice 4 | Capacidade financeira ausente na inspeção de app, rotas, migrações e páginas. Agendamentos e competência financeira é o único dono da entrega; preservações e integração são conferidas nos critérios, sem reimplementar leitura individual ou cálculo. |
| CA1: Salvar receita/despesa válida cria um registro próprio, mostra sucesso e mantém dados após novo acesso. | Slice 1 | Capacidade financeira ausente na inspeção de app, rotas, migrações e páginas. Cadastro e conferência de uma transação própria é o único dono da entrega; preservações e integração são conferidas nos critérios, sem reimplementar leitura individual ou cálculo. |
| CA2: Ausências, categoria incompatível, valores/datas fora de R2 e descrição vazia/longa impedem salvar, mostram erros e preservam o formulário. | Slice 1 | Capacidade financeira ausente na inspeção de app, rotas, migrações e páginas. Cadastro e conferência de uma transação própria é o único dono da entrega; preservações e integração são conferidas nos critérios, sem reimplementar leitura individual ou cálculo. |
| CA3: Futura aparece agendada e não afeta saldo nem totais, mesmo na consulta de seu mês futuro. | Slice 4 | Capacidade financeira ausente na inspeção de app, rotas, migrações e páginas. Agendamentos e competência financeira é o único dono da entrega; preservações e integração são conferidas nos critérios, sem reimplementar leitura individual ou cálculo. |
| CA4: Ao chegar a data em America/Sao_Paulo, compõe valores de R6 sem confirmação e perde marcação de agendada. | Slice 4 | Capacidade financeira ausente na inspeção de app, rotas, migrações e páginas. Agendamentos e competência financeira é o único dono da entrega; preservações e integração são conferidas nos critérios, sem reimplementar leitura individual ou cálculo. |
| CA5: CA5, busca combinada: descrição, tipo e categoria combinados com período retornam apenas registros correspondentes do usuário, preservando ordenação e paginação do histórico. | Slice 3 | Capacidade financeira ausente na inspeção de app, rotas, migrações e páginas. Busca por descrição, tipo e categoria é o único dono da entrega; preservações e integração são conferidas nos critérios, sem reimplementar leitura individual ou cálculo. |
| CA6-vazio: CA6: histórico sem registros orienta primeiro cadastro. | Slice 2 | Capacidade financeira ausente na inspeção de app, rotas, migrações e páginas. Histórico por período é o único dono da entrega; preservações e integração são conferidas nos critérios, sem reimplementar leitura individual ou cálculo. |
| CA6-busca: CA6: busca sem resultados difere do histórico vazio e permite ajustar/limpar; limpar retorna histórico integral. | Slice 3 | Capacidade financeira ausente na inspeção de app, rotas, migrações e páginas. Busca por descrição, tipo e categoria é o único dono da entrega; preservações e integração são conferidas nos critérios, sem reimplementar leitura individual ou cálculo. |
| CA7-consulta: CA7, consulta individual: titular habilitado consulta todos os campos do próprio registro; identificador de outra conta não revela seus dados. | Slice 1 | Capacidade financeira ausente na inspeção de app, rotas, migrações e páginas. Cadastro e conferência de uma transação própria é o único dono da entrega; preservações e integração são conferidas nos critérios, sem reimplementar leitura individual ou cálculo. |
| CA7-edicao: CA7: detalhes próprios oferecem edição; outra conta não pode alterar por tela ou identificador direto. | Slice 5 | Capacidade financeira ausente na inspeção de app, rotas, migrações e páginas. Edição de transação com efeitos financeiros é o único dono da entrega; preservações e integração são conferidas nos critérios, sem reimplementar leitura individual ou cálculo. |
| CA7-exclusao: CA7: detalhes próprios oferecem exclusão; outra conta não pode excluir por tela ou identificador direto. | Slice 6 | Capacidade financeira ausente na inspeção de app, rotas, migrações e páginas. Exclusão confirmada com efeito único é o único dono da entrega; preservações e integração são conferidas nos critérios, sem reimplementar leitura individual ou cálculo. |
| CA8: Editar campo válido atualiza o mesmo registro e seus efeitos; mover passada para futura retira contribuição e inverso inclui. | Slice 5 | Capacidade financeira ausente na inspeção de app, rotas, migrações e páginas. Edição de transação com efeitos financeiros é o único dono da entrega; preservações e integração são conferidas nos critérios, sem reimplementar leitura individual ou cálculo. |
| CA9-cadastro: CA9: cancelar cadastro não modifica registros nem totais. | Slice 1 | Capacidade financeira ausente na inspeção de app, rotas, migrações e páginas. Cadastro e conferência de uma transação própria é o único dono da entrega; preservações e integração são conferidas nos critérios, sem reimplementar leitura individual ou cálculo. |
| CA9-edicao: CA9: cancelar edição conserva registro e totais anteriores. | Slice 5 | Capacidade financeira ausente na inspeção de app, rotas, migrações e páginas. Edição de transação com efeitos financeiros é o único dono da entrega; preservações e integração são conferidas nos critérios, sem reimplementar leitura individual ou cálculo. |
| CA9-exclusao: CA9: cancelar exclusão mantém dados/totais; confirmar remove do histórico/cálculos sem desfazer. | Slice 6 | Capacidade financeira ausente na inspeção de app, rotas, migrações e páginas. Exclusão confirmada com efeito único é o único dono da entrega; preservações e integração são conferidas nos critérios, sem reimplementar leitura individual ou cálculo. |
| CA10-cadastro: CA10: falha ao cadastrar não grava parcialmente nem mostra sucesso; orienta nova tentativa. | Slice 1 | Capacidade financeira ausente na inspeção de app, rotas, migrações e páginas. Cadastro e conferência de uma transação própria é o único dono da entrega; preservações e integração são conferidas nos critérios, sem reimplementar leitura individual ou cálculo. |
| CA10-edicao: CA10: falha ao editar não altera parcialmente nem mostra sucesso; registro removido/indisponível não pode ser alterado e não revela dados de terceiros. | Slice 5 | Capacidade financeira ausente na inspeção de app, rotas, migrações e páginas. Edição de transação com efeitos financeiros é o único dono da entrega; preservações e integração são conferidas nos critérios, sem reimplementar leitura individual ou cálculo. |
| CA10-consulta: CA10: registro indisponível não revela dados de terceiros e a interface informa indisponibilidade. | Slice 1 | Capacidade financeira ausente na inspeção de app, rotas, migrações e páginas. Cadastro e conferência de uma transação própria é o único dono da entrega; preservações e integração são conferidas nos critérios, sem reimplementar leitura individual ou cálculo. |
| CA12-cadastro: CA12: duas operações distintas com dados iguais podem criar duas transações, sem deduplicação automática. | Slice 1 | Capacidade financeira ausente na inspeção de app, rotas, migrações e páginas. Cadastro e conferência de uma transação própria é o único dono da entrega; preservações e integração são conferidas nos critérios, sem reimplementar leitura individual ou cálculo. |
| CA12-edicao: CA12: registros com dados iguais possuem edição independente. | Slice 5 | Capacidade financeira ausente na inspeção de app, rotas, migrações e páginas. Edição de transação com efeitos financeiros é o único dono da entrega; preservações e integração são conferidas nos critérios, sem reimplementar leitura individual ou cálculo. |
| CA12-exclusao: CA12: exclusão de registros iguais é independente; repetir exclusão de registro removido não produz novo efeito nos totais. | Slice 6 | Capacidade financeira ausente na inspeção de app, rotas, migrações e páginas. Exclusão confirmada com efeito único é o único dono da entrega; preservações e integração são conferidas nos critérios, sem reimplementar leitura individual ou cálculo. |
| CA11: Categorias disponíveis correspondem exatamente a R3; trocar tipo não mantém categoria incompatível silenciosamente nem permite concluir com ela. | Slice 1 | Capacidade financeira ausente na inspeção de app, rotas, migrações e páginas. Cadastro e conferência de uma transação própria é o único dono da entrega; preservações e integração são conferidas nos critérios, sem reimplementar leitura individual ou cálculo. |
| F-edicao-validacao: Fluxos alternativos: edição inválida preserva formulário, mostra erros e não altera dados; limites R1–R3 e troca de tipo/categoria aplicam-se também à edição. | Slice 5 | Capacidade financeira ausente na inspeção de app, rotas, migrações e páginas. Edição de transação com efeitos financeiros é o único dono da entrega; preservações e integração são conferidas nos critérios, sem reimplementar leitura individual ou cálculo. |
| F-exclusao-falha: Fluxos alternativos: falha ao persistir exclusão não apresenta sucesso nem aplica alteração parcial; orienta nova tentativa. | Slice 6 | Capacidade financeira ausente na inspeção de app, rotas, migrações e páginas. Exclusão confirmada com efeito único é o único dono da entrega; preservações e integração são conferidas nos critérios, sem reimplementar leitura individual ou cálculo. |
| R10-historico: R10 e dados percebidos, histórico: exibir descrição, tipo, valor em reais com centavos, categoria e data brasileira de cada registro, número de resultados e acesso à consulta individual já entregue. | Slice 2 | Capacidade financeira ausente na inspeção de app, rotas, migrações e páginas. Histórico por período é o único dono da entrega; preservações e integração são conferidas nos critérios, sem reimplementar leitura individual ou cálculo. |
| R9-navegacao: R9, navegação: ordenar por data da movimentação decrescente e cadastro mais recente em empate; páginas de 50 registros, permitindo percorrer todo o conjunto do período. | Slice 2 | Capacidade financeira ausente na inspeção de app, rotas, migrações e páginas. Histórico por período é o único dono da entrega; preservações e integração são conferidas nos critérios, sem reimplementar leitura individual ou cálculo. |
| CA5-periodo: CA5, período: iniciar histórico no mês atual, permitir outro mês ou todo histórico; mudar período retorna à primeira página. | Slice 2 | Capacidade financeira ausente na inspeção de app, rotas, migrações e páginas. Histórico por período é o único dono da entrega; preservações e integração são conferidas nos critérios, sem reimplementar leitura individual ou cálculo. |
| CA7-historico: CA7 e permissões, descoberta: histórico e seus resultados não revelam registros de outra conta e levam somente à consulta individual autorizada. | Slice 2 | Capacidade financeira ausente na inspeção de app, rotas, migrações e páginas. Histórico por período é o único dono da entrega; preservações e integração são conferidas nos critérios, sem reimplementar leitura individual ou cálculo. |

Formato das condições: Markdown e DOCX.

## Condições de teste

Estas condições integram a aprovação da decomposição. A validação estrutural não substitui a revisão semântica do tech lead.

### Contexto

Usuário autenticado com e-mail confirmado. Preparar duas contas, todas as categorias, valores/descrições/datas de limite, mais de50 registros, datas passadas/atuais/futuras, virada controlada em America/Sao_Paulo e falhas de persistência controladas. Condições futuras de QA, sem alegação de execução. Verificar na interface a indicação de agendada e usar testes de integração reproduzíveis da capacidade interna de cálculo, com banco de teste real, relógio controlado e sem substituir cálculo ou consulta por respostas simuladas. Não usar dashboard, endpoint novo ou script avulso. Registrar comando da suíte, revisão testada, massa, instante, esperado e observado. Massa M: usuário A com receita R$ 100,00 e despesa R$ 30,00 em 30/11/2026; receita R$ 20,00 e despesa R$ 5,00 em 01/12/2026; receita R$ 7,00 excluída em 30/11. Usuário B com receita R$ 900,00 em 30/11. Relógio em America/Sao_Paulo. Cada cenário recomeça da massa, sem depender do resultado de outro. Para efeitos de edição/exclusão, executar a operação real da aplicação antes de consultar os cálculos; alteração direta da massa não comprova integração da mutação.

#### CT-001 — R1 — Cadastro e conferência de uma transação própria

Verificação: Cadastrar separadamente receita e despesa válidas e omitir cada campo obrigatório.

Resultado esperado: Dados válidos salvam; ausência de qualquer campo impede salvar com erro.

Origem no requisito: R1: Tipo receita/despesa, valor positivo em reais, descrição, categoria e data são obrigatórios; tipo determina entrada ou saída.

#### CT-002 — R2 — Cadastro e conferência de uma transação própria

Verificação: Testar limites monetários, zero/negativo/acima do máximo e três casas; descrição vazia, espaços, 1,120,121 caracteres; datas limites, fora delas e inválidas.

Resultado esperado: Limites inclusivos válidos são aceitos; demais entradas são recusadas sem arredondamento silencioso e com formulário preservado.

Origem no requisito: R2: Valor entre R$ 0,01 e R$ 999.999.999,99 com até duas casas; não arredondar entrada com precisão maior. Descrição entre 1 e 120 caracteres após aparar extremidades. Data válida de 01/01/1900 a 31/12/9999.

#### CT-003 — R3 — Cadastro e conferência de uma transação própria

Verificação: Conferir as listas para ambos os tipos e procurar ações de criar, renomear ou excluir categoria.

Resultado esperado: Listas correspondem exatamente às categorias aprovadas e não permitem manutenção.

Origem no requisito: R3: Oferecer somente receitas: Salário, Freelance, Rendimentos, Outras receitas; despesas: Alimentação, Moradia, Transporte, Saúde, Educação, Lazer, Compras, Outras despesas. Sem manutenção de categorias.

#### CT-004 — R4 — Cadastro e conferência de uma transação própria

Verificação: Cadastrar como A e tentar escolher B como proprietário; sair e entrar como A para consultar; tentar cadastrar sem sessão e sem e-mail confirmado.

Resultado esperado: Registro pertence apenas a A e permanece persistido; proprietário alheio não é aceito e usuários não habilitados não operam.

Origem no requisito: R4: Vincular cadastro ao usuário autenticado com e-mail confirmado, sem aceitar outro proprietário; persistência permanece após sair e entrar.

#### CT-005 — R5 — Agendamentos e competência financeira

Contexto: Verificação de valores pela capacidade interna conforme contexto e massa M; evidência reproduzível da integração, sem interface financeira adicional.

Verificação: Na massa M, conferir indicação e cálculos às 23:59:59 de30/11 e às00:00:00 de01/12 em Brasília, quando UTC já está no próximo dia antes da virada local.

Resultado esperado: Antes: saldo70, novembro receitas100/despesas30, dezembro0/0; futuras agendadas. Depois: saldo85, novembro100/30, dezembro20/5; registros de01/12 deixam de ser agendados sem confirmação ou pagamento externo.

Origem no requisito: R5: Data define competência em America/Sao_Paulo; futura é agendada, aparece no histórico e não afeta saldo/totais até início da data. Inclusão automática, sem confirmação manual nem pagamento externo.

#### CT-006 — R6 — Agendamentos e competência financeira

Contexto: Verificação de valores pela capacidade interna conforme contexto e massa M; evidência reproduzível da integração, sem interface financeira adicional.

Verificação: Comparar a capacidade interna com a massa M antes/depois da virada, excluídos e outra conta presentes. Em cenários separados usar apenas despesa10; e receitas0,10+0,20 com despesa0,01.

Resultado esperado: Massa M retorna70 antes e85 depois; excluída7 e contaB900 não entram. Somente despesa10 retorna saldo-10. Centavos retornam saldo0,29 exato. Não existe saldo inicial separado.

Origem no requisito: R6: Saldo é receitas menos despesas de registros não excluídos até hoje; totais mensais usam data dentro do mês e até hoje. Mês futuro não realiza movimentações; saldo negativo permitido, sem saldo inicial separado.

#### CT-007 — R7 — Edição de transação com efeitos financeiros

Contexto: Verificação de valores pela capacidade interna conforme contexto e massa M; evidência reproduzível da integração, sem interface financeira adicional.

Verificação: Em01/12 na massa M, pela operação real de edição, mover receita100 para02/12 e depois devolver a30/11. Em cenários independentes, mudar despesa30 para40, e mudar despesa30 para receita30 com categoria compatível.

Resultado esperado: Datas: saldo85→-15→85, novembro receitas100→0→100. Valor: saldo75 e novembro despesa40. Tipo: saldo145 e novembro receitas130/despesas0. Mesmo registro atualizado, sem duplicação.

Origem no requisito: R7: Editar todos os campos próprios em qualquer data; tipo, valor, categoria e data atualizam valores aplicáveis. Passada/hoje para futura retira efeito; futura para hoje/passada inclui.

#### CT-008 — R8 — Exclusão confirmada com efeito único

Contexto: Verificação de valores pela capacidade interna conforme contexto e massa M; evidência reproduzível da integração, sem interface financeira adicional.

Verificação: Em01/12 na massa M, confirmar pela aplicação a exclusão da despesa30; conferir consulta individual, histórico e capacidade de cálculo.

Resultado esperado: Registro indisponível/removido, saldo115, novembro receitas100/despesas0, dezembro20/5; sem desfazer.

Origem no requisito: R8: Excluir somente após confirmação, removendo do histórico e cálculos, sem desfazer.

#### CT-009 — R9 — Busca por descrição, tipo e categoria

Verificação: Usar mais de 50 registros e descrições acentuadas; buscar trecho com caixa/acentos diferentes, combinar filtros, navegar, mudar filtro e limpar.

Resultado esperado: Resultados próprios respeitam combinações e ordem; páginas têm até 50, mantêm filtros, alteração retorna à primeira e limpeza retorna ao histórico integral.

Origem no requisito: R9: R9, busca e filtros: trecho da descrição sem distinguir caixa/acentos; tipo/categoria/período restringem o mesmo conjunto. Limpar filtros mostra todo o histórico; manter filtros entre páginas e retornar à primeira ao alterar um filtro.; R9-navegacao: R9, navegação: ordenar por data da movimentação decrescente e cadastro mais recente em empate; páginas de 50 registros, permitindo percorrer todo o conjunto do período.

#### CT-010 — Campos na consulta individual e no histórico

Verificação: Salvar transação e conferir a leitura individual; depois acessar o mesmo registro pelo histórico.

Resultado esperado: Tipo, valor em reais/centavos, descrição, categoria e data brasileira coincidem nas duas entradas; histórico reutiliza a consulta individual.

Origem no requisito: R10-campos: R10 e dados percebidos, consulta individual: conferir descrição, tipo, valor em reais com centavos, categoria e data brasileira do registro persistido, inclusive ao reabrir após novo login.; R10-historico: R10 e dados percebidos, histórico: exibir descrição, tipo, valor em reais com centavos, categoria e data brasileira de cada registro, número de resultados e acesso à consulta individual já entregue.

#### CT-011 — R10-agendada — Agendamentos e competência financeira

Verificação: Consultar histórico misturando datas futuras, atuais e passadas e atravessar a data prevista.

Resultado esperado: Futuras se integram à ordem cronológica e deixam de ser agendadas na data, sem fila separada.

Origem no requisito: R10-agendada: R10: futuras mostram identificação de agendada, seguem ordenação por data sem fila separada; identificação cessa na data.

#### CT-012 — CA1 — Cadastro e conferência de uma transação própria

Verificação: Cadastrar receita e despesa; conferir os campos persistidos na consulta individual. Guardar seu endereço, sair, entrar novamente e reabri-lo sem depender da busca ou do histórico.

Resultado esperado: Sucesso corresponde à gravação e o titular reencontra os mesmos dados persistidos; não depende de memória do formulário.

Origem no requisito: CA1: Salvar receita/despesa válida cria um registro próprio, mostra sucesso e mantém dados após novo acesso.

#### CT-013 — CA2 — Cadastro e conferência de uma transação própria

Verificação: Enviar formulário com cada classe de erro e corrigir sem redigitar campos válidos.

Resultado esperado: Não cria registro inválido; exibe erros e conserva dados para correção.

Origem no requisito: CA2: Ausências, categoria incompatível, valores/datas fora de R2 e descrição vazia/longa impedem salvar, mostram erros e preservam o formulário.

#### CT-014 — CA3 — Agendamentos e competência financeira

Contexto: Verificação de valores pela capacidade interna conforme contexto e massa M; evidência reproduzível da integração, sem interface financeira adicional.

Verificação: Na massa M em30/11 consultar internamente totais de dezembro e conferir registros futuros nas consultas individuais e histórico.

Resultado esperado: Receita20/despesa5 de01/12 permanecem agendadas; dezembro0/0 e saldo70, embora o mês futuro seja selecionado.

Origem no requisito: CA3: Futura aparece agendada e não afeta saldo nem totais, mesmo na consulta de seu mês futuro.

#### CT-015 — CA4 — Agendamentos e competência financeira

Contexto: Verificação de valores pela capacidade interna conforme contexto e massa M; evidência reproduzível da integração, sem interface financeira adicional.

Verificação: Reexecutar a consulta na massa M imediatamente antes/depois da virada local, sem editar registros, clicar em confirmação ou esperar a virada real.

Resultado esperado: Virada controlada altera saldo70→85 e dezembro0/0→20/5; indicação de agendada desaparece na consulta correspondente.

Origem no requisito: CA4: Ao chegar a data em America/Sao_Paulo, compõe valores de R6 sem confirmação e perde marcação de agendada.

#### CT-016 — CA5 — Busca por descrição, tipo e categoria

Verificação: Usar duas contas e períodos distintos; abrir consulta inicial, trocar mês/todos e combinar filtros.

Resultado esperado: Padrão mês atual; resultados somente da conta e correspondentes, com ordenação/paginação correta.

Origem no requisito: CA5: CA5, busca combinada: descrição, tipo e categoria combinados com período retornam apenas registros correspondentes do usuário, preservando ordenação e paginação do histórico.; CA5-periodo: CA5, período: iniciar histórico no mês atual, permitir outro mês ou todo histórico; mudar período retorna à primeira página.

#### CT-017 — CA6-vazio — Histórico por período

Verificação: Abrir histórico de conta sem nenhuma movimentação.

Resultado esperado: Apresenta estado vazio e caminho para cadastrar.

Origem no requisito: CA6-vazio: CA6: histórico sem registros orienta primeiro cadastro.

#### CT-018 — CA6-busca — Busca por descrição, tipo e categoria

Verificação: Em conta com registros, aplicar busca sem correspondência e limpar filtros.

Resultado esperado: Informa ausência de correspondência e permite retomar todo histórico.

Origem no requisito: CA6-busca: CA6: busca sem resultados difere do histórico vazio e permite ajustar/limpar; limpar retorna histórico integral.

#### CT-019 — CA7-consulta — Histórico por período

Verificação: Como B, tentar o endereço individual de A e percorrer o histórico; como A, reabrir o próprio registro após novo login.

Resultado esperado: Consulta individual e descoberta ficam limitadas ao titular; acesso alheio não expõe dados.

Origem no requisito: CA7-consulta: CA7, consulta individual: titular habilitado consulta todos os campos do próprio registro; identificador de outra conta não revela seus dados.; CA7-historico: CA7 e permissões, descoberta: histórico e seus resultados não revelam registros de outra conta e levam somente à consulta individual autorizada.

#### CT-020 — CA7-edicao — Edição de transação com efeitos financeiros

Verificação: Editar registro próprio e tentar alterar o de outra conta por acesso direto.

Resultado esperado: Somente proprietário habilitado altera; tentativa alheia não muda dados nem revela conteúdo.

Origem no requisito: CA7-edicao: CA7: detalhes próprios oferecem edição; outra conta não pode alterar por tela ou identificador direto.

#### CT-021 — CA7-exclusao — Exclusão confirmada com efeito único

Verificação: Solicitar exclusão própria e tentar excluir registro alheio.

Resultado esperado: Ação disponível ao titular; acesso alheio não remove nem revela dados.

Origem no requisito: CA7-exclusao: CA7: detalhes próprios oferecem exclusão; outra conta não pode excluir por tela ou identificador direto.

#### CT-022 — CA8 — Edição de transação com efeitos financeiros

Contexto: Verificação de valores pela capacidade interna conforme contexto e massa M; evidência reproduzível da integração, sem interface financeira adicional.

Verificação: Editar os cinco campos pela aplicação, conferir consulta individual/histórico e resultados internos antes/depois; incluir a massa M e as transições de CT-007.

Resultado esperado: Identidade e propriedade preservadas; consultas atualizadas e cálculos coincidem com a nova contribuição. Edição não pode ser concluída apenas com prova de gravação.

Origem no requisito: CA8: Editar campo válido atualiza o mesmo registro e seus efeitos; mover passada para futura retira contribuição e inverso inclui.

#### CT-023 — CA9-cadastro — Cadastro e conferência de uma transação própria

Contexto: Verificação de valores pela capacidade interna conforme contexto e massa M; evidência reproduzível da integração, sem interface financeira adicional.

Verificação: Preencher cadastro e cancelar.

Resultado esperado: Nenhum registro novo nem alteração financeira.

Origem no requisito: CA9-cadastro: CA9: cancelar cadastro não modifica registros nem totais.

#### CT-024 — CA9-edicao — Edição de transação com efeitos financeiros

Contexto: Verificação de valores pela capacidade interna conforme contexto e massa M; evidência reproduzível da integração, sem interface financeira adicional.

Verificação: Na massa M em01/12, alterar campos no formulário e cancelar; conferir registro e capacidade interna.

Resultado esperado: Persistência original e saldo85 permanecem; nenhuma contribuição foi alterada.

Origem no requisito: CA9-edicao: CA9: cancelar edição conserva registro e totais anteriores.

#### CT-025 — CA9-exclusao — Exclusão confirmada com efeito único

Contexto: Verificação de valores pela capacidade interna conforme contexto e massa M; evidência reproduzível da integração, sem interface financeira adicional.

Verificação: Em tentativas independentes na massa M em01/12, cancelar exclusão da despesa30 e depois confirmar. Conferir dados e valores internos.

Resultado esperado: Cancelar mantém saldo85 e registro; confirmar produz115 e remove só o escolhido.

Origem no requisito: CA9-exclusao: CA9: cancelar exclusão mantém dados/totais; confirmar remove do histórico/cálculos sem desfazer.

#### CT-026 — CA10-cadastro — Cadastro e conferência de uma transação própria

Verificação: Provocar falha controlada de persistência no cadastro e tentar novamente após restauração.

Resultado esperado: Sem gravação parcial ou falso sucesso; usuário recebe orientação de tentar novamente.

Origem no requisito: CA10-cadastro: CA10: falha ao cadastrar não grava parcialmente nem mostra sucesso; orienta nova tentativa.

#### CT-027 — CA10-edicao — Edição de transação com efeitos financeiros

Contexto: Verificação de valores pela capacidade interna conforme contexto e massa M; evidência reproduzível da integração, sem interface financeira adicional.

Verificação: Provocar falha em edição e editar identificador removido/indisponível.

Resultado esperado: Sem alteração parcial, falso sucesso ou dados alheios; informa indisponibilidade ou nova tentativa conforme caso.

Origem no requisito: CA10-edicao: CA10: falha ao editar não altera parcialmente nem mostra sucesso; registro removido/indisponível não pode ser alterado e não revela dados de terceiros.

#### CT-028 — CA10-consulta — Histórico por período

Verificação: Abrir identificador inexistente ou removido.

Resultado esperado: Informa indisponibilidade sem dados de outra conta.

Origem no requisito: CA10-consulta: CA10: registro indisponível não revela dados de terceiros e a interface informa indisponibilidade.

#### CT-029 — CA12-cadastro — Cadastro e conferência de uma transação própria

Verificação: Cadastrar duas vezes em operações distintas com mesmo tipo/valor/descrição/categoria/data.

Resultado esperado: Cria dois registros independentes.

Origem no requisito: CA12-cadastro: CA12: duas operações distintas com dados iguais podem criar duas transações, sem deduplicação automática.

#### CT-030 — CA12-edicao — Edição de transação com efeitos financeiros

Verificação: Editar só um dos dois registros iguais.

Resultado esperado: Somente o escolhido muda.

Origem no requisito: CA12-edicao: CA12: registros com dados iguais possuem edição independente.

#### CT-031 — CA12-exclusao — Exclusão confirmada com efeito único

Contexto: Verificação de valores pela capacidade interna conforme contexto e massa M; evidência reproduzível da integração, sem interface financeira adicional.

Verificação: Excluir a despesa30 da massa M em01/12 e repetir a confirmação; em cenário separado com dois registros iguais, excluir apenas um.

Resultado esperado: Saldo85→115→115 sem novo efeito na repetição. No cenário de iguais o outro registro e sua contribuição permanecem.

Origem no requisito: CA12-exclusao: CA12: exclusão de registros iguais é independente; repetir exclusão de registro removido não produz novo efeito nos totais.

#### CT-032 — CA11 — Cadastro e conferência de uma transação própria

Verificação: Selecionar categoria, mudar tipo e tentar salvar com categoria anterior incompatível.

Resultado esperado: Exige seleção compatível e não grava combinação inválida.

Origem no requisito: CA11: Categorias disponíveis correspondem exatamente a R3; trocar tipo não mantém categoria incompatível silenciosamente nem permite concluir com ela.

#### CT-033 — F-edicao-validacao — Edição de transação com efeitos financeiros

Verificação: Editar com cada campo ausente, valor inválido/precisão maior, descrição fora do limite, data inválida e tipo/categoria incompatíveis.

Resultado esperado: Recusa, conserva dados para correção e preserva registro anterior.

Origem no requisito: F-edicao-validacao: Fluxos alternativos: edição inválida preserva formulário, mostra erros e não altera dados; limites R1–R3 e troca de tipo/categoria aplicam-se também à edição.

#### CT-034 — F-exclusao-falha — Exclusão confirmada com efeito único

Contexto: Verificação de valores pela capacidade interna conforme contexto e massa M; evidência reproduzível da integração, sem interface financeira adicional.

Verificação: Na massa M em01/12, provocar falha controlada na confirmação de exclusão e conferir persistência e valores internos.

Resultado esperado: Registro permanece e saldo85 é preservado, sem falso sucesso; orienta nova tentativa.

Origem no requisito: F-exclusao-falha: Fluxos alternativos: falha ao persistir exclusão não apresenta sucesso nem aplica alteração parcial; orienta nova tentativa.


## Descrições completas

### 1. [DEV] [WEB] [USUARIO] Gestão de transações - Cadastro e conferência de uma transação própria

#### Entrega

Permitir cadastrar receita ou despesa e conferir imediatamente os campos lidos do registro persistido. O titular pode guardar o endereço dessa consulta individual, sair, entrar novamente e reabrir o mesmo registro para confirmar sua persistência.

#### Escopo e limites

Não entrega a descoberta do conjunto, histórico, filtros nem botões de edição/exclusão. A leitura individual é a mesma que o histórico reutilizará; não criar uma segunda tela de detalhes. Receitas e despesas permanecem juntas por compartilharem campos, validação e leitura.

#### Critérios de aceite

- Tipo receita/despesa, valor positivo em reais, descrição, categoria e data são obrigatórios; tipo determina entrada ou saída.
- Valor entre R$ 0,01 e R$ 999.999.999,99 com até duas casas; não arredondar entrada com precisão maior. Descrição entre 1 e 120 caracteres após aparar extremidades. Data válida de 01/01/1900 a 31/12/9999.
- Oferecer somente receitas: Salário, Freelance, Rendimentos, Outras receitas; despesas: Alimentação, Moradia, Transporte, Saúde, Educação, Lazer, Compras, Outras despesas. Sem manutenção de categorias.
- Vincular cadastro ao usuário autenticado com e-mail confirmado, sem aceitar outro proprietário; persistência permanece após sair e entrar.
- R10 e dados percebidos, consulta individual: conferir descrição, tipo, valor em reais com centavos, categoria e data brasileira do registro persistido, inclusive ao reabrir após novo login.
- Salvar receita/despesa válida cria um registro próprio, mostra sucesso e mantém dados após novo acesso.
- Ausências, categoria incompatível, valores/datas fora de R2 e descrição vazia/longa impedem salvar, mostram erros e preservam o formulário.
- CA7, consulta individual: titular habilitado consulta todos os campos do próprio registro; identificador de outra conta não revela seus dados.
- CA9: cancelar cadastro não modifica registros nem totais.
- CA10: falha ao cadastrar não grava parcialmente nem mostra sucesso; orienta nova tentativa.
- CA10: registro indisponível não revela dados de terceiros e a interface informa indisponibilidade.
- CA12: duas operações distintas com dados iguais podem criar duas transações, sem deduplicação automática.
- Categorias disponíveis correspondem exatamente a R3; trocar tipo não mantém categoria incompatível silenciosamente nem permite concluir com ela.
- Depois de salvar, a consulta individual mostra valores lidos da persistência, não apenas dados retidos no formulário. Ao sair, entrar e reabrir o endereço do registro, os mesmos campos continuam disponíveis ao titular.

#### Dependências

Para iniciar: autenticação e confirmação de e-mail existentes. Para concluir este corte: cadastro válido, consulta individual autorizada e reabertura após novo login, sem depender do histórico completo.

#### Referências

Item pai Redmine `#1015911`; regras/critérios R1, R2, R3, R4, R10-campos, CA1, CA2, CA7-consulta, CA9-cadastro, CA10-cadastro, CA10-consulta, CA12-cadastro, CA11.

### 2. [DEV] [WEB] [USUARIO] Gestão de transações - Histórico por período

#### Entrega

Permitir descobrir e percorrer as próprias transações por período, abrindo a consulta individual já entregue no cadastro. Inclui mês atual, outro mês, histórico integral, ordenação, paginação e contagem.

#### Escopo e limites

Não refaz a leitura individual nem a validação do cadastro. Busca textual e filtros de tipo/categoria pertencem à entrega específica; paginação e seleção de período já funcionam nesta entrega.

#### Critérios de aceite

- CA6: histórico sem registros orienta primeiro cadastro.
- R10 e dados percebidos, histórico: exibir descrição, tipo, valor em reais com centavos, categoria e data brasileira de cada registro, número de resultados e acesso à consulta individual já entregue.
- R9, navegação: ordenar por data da movimentação decrescente e cadastro mais recente em empate; páginas de 50 registros, permitindo percorrer todo o conjunto do período.
- CA5, período: iniciar histórico no mês atual, permitir outro mês ou todo histórico; mudar período retorna à primeira página.
- CA7 e permissões, descoberta: histórico e seus resultados não revelam registros de outra conta e levam somente à consulta individual autorizada.

#### Dependências

Para iniciar: ‘Gestão de transações - Cadastro e conferência de uma transação própria’, que fornece registros e consulta individual. Para concluir: navegação por período/páginas abre essa mesma consulta.

#### Referências

Item pai Redmine `#1015911`; regras/critérios CA6-vazio, R10-historico, R9-navegacao, CA5-periodo, CA7-historico.

### 3. [DEV] [WEB] [USUARIO] Gestão de transações - Busca por descrição, tipo e categoria

#### Entrega

Permitir localizar registros do histórico por trecho da descrição, tipo e categoria, combinados com o período. Reutiliza navegação, paginação e consulta individual já entregues.

#### Escopo e limites

Acrescenta busca e combinação de filtros ao histórico existente; não reconstrói ordenação, consulta individual ou paginação.

#### Critérios de aceite

- R9, busca e filtros: trecho da descrição sem distinguir caixa/acentos; tipo/categoria/período restringem o mesmo conjunto. Limpar filtros mostra todo o histórico; manter filtros entre páginas e retornar à primeira ao alterar um filtro.
- CA5, busca combinada: descrição, tipo e categoria combinados com período retornam apenas registros correspondentes do usuário, preservando ordenação e paginação do histórico.
- CA6: busca sem resultados difere do histórico vazio e permite ajustar/limpar; limpar retorna histórico integral.

#### Dependências

Para iniciar: ‘Gestão de transações - Histórico por período’. Para concluir: filtros combinados preservam sua ordenação e paginação, sem vazar registros de outra conta.

#### Referências

Item pai Redmine `#1015911`; regras/critérios R9, CA5, CA6-busca.

### 4. [DEV] [WEB] [USUARIO] Gestão de transações - Agendamentos e competência financeira

#### Entrega

Identificar agendamentos nas consultas e aplicar a competência financeira em America/Sao_Paulo. Entrega a transição visível de agendada e os resultados de saldo e totais da capacidade interna, verificáveis sem dashboard.

#### Escopo e limites

Não acrescenta dashboard, tela de saldo, endpoint público, API consumível ou comando de produto para inspeção. O histórico/consulta individual mostram agendada; valores são verificados na capacidade interna da aplicação. Não executa pagamentos externos.

#### Critérios de aceite

- Data define competência em America/Sao_Paulo; futura é agendada, aparece no histórico e não afeta saldo/totais até início da data. Inclusão automática, sem confirmação manual nem pagamento externo.
- Saldo é receitas menos despesas de registros não excluídos até hoje; totais mensais usam data dentro do mês e até hoje. Mês futuro não realiza movimentações; saldo negativo permitido, sem saldo inicial separado.
- R10: futuras mostram identificação de agendada, seguem ordenação por data sem fila separada; identificação cessa na data.
- Futura aparece agendada e não afeta saldo nem totais, mesmo na consulta de seu mês futuro.
- Ao chegar a data em America/Sao_Paulo, compõe valores de R6 sem confirmação e perde marcação de agendada.
- Com receita de R$ 100,00 e despesa de R$ 30,00 em 30/11, mais receita de R$ 20,00 e despesa de R$ 5,00 em 01/12, o saldo às 23:59:59 de 30/11 em Brasília é R$ 70,00 e os totais de dezembro são zero. Às 00:00:00 de 01/12, saldo R$ 85,00 e totais de dezembro R$ 20,00/R$ 5,00; novembro permanece R$ 100,00/R$ 30,00. Registros excluídos e de outra conta não entram.

#### Dependências

Para iniciar: ‘Gestão de transações - Cadastro e conferência de uma transação própria’. Para concluir: integrar a indicação de agendada em ‘Gestão de transações - Histórico por período’ e conferir saldo/totais na capacidade interna com dados persistidos e passagem controlada da data.

#### Referências

Item pai Redmine `#1015911`; regras/critérios R5, R6, R10-agendada, CA3, CA4.

### 5. [DEV] [WEB] [USUARIO] Gestão de transações - Edição de transação com efeitos financeiros

#### Entrega

Permitir corrigir todos os campos do mesmo registro próprio, reaproveitando formulário e consulta individual. A entrega inclui integrar e verificar o efeito financeiro real da alteração e atualizar a consulta.

#### Escopo e limites

Não duplica o registro nem reimplementa a regra de saldo. Salvar campos sem integrar e verificar os efeitos financeiros não conclui esta entrega.

#### Critérios de aceite

- Editar todos os campos próprios em qualquer data; tipo, valor, categoria e data atualizam valores aplicáveis. Passada/hoje para futura retira efeito; futura para hoje/passada inclui.
- CA7: detalhes próprios oferecem edição; outra conta não pode alterar por tela ou identificador direto.
- Editar campo válido atualiza o mesmo registro e seus efeitos; mover passada para futura retira contribuição e inverso inclui.
- CA9: cancelar edição conserva registro e totais anteriores.
- CA10: falha ao editar não altera parcialmente nem mostra sucesso; registro removido/indisponível não pode ser alterado e não revela dados de terceiros.
- CA12: registros com dados iguais possuem edição independente.
- Fluxos alternativos: edição inválida preserva formulário, mostra erros e não altera dados; limites R1–R3 e troca de tipo/categoria aplicam-se também à edição.
- Conclusão exige efeitos integrados: na massa de referência com saldo R$ 85,00 em 01/12, mover a receita de R$ 100,00 de 30/11 para 02/12 resulta em saldo -R$ 15,00; trazê-la de volta restaura R$ 85,00. A consulta do mesmo registro e o histórico refletem a alteração.
- Na edição, recusar valor fora de R$ 0,01 a R$ 999.999.999,99 ou mais de duas casas sem arredondar; descrição vazia ou acima de120 caracteres após aparar; data inválida ou fora de01/01/1900 a31/12/9999; campos obrigatórios ausentes e categoria incompatível. Preservar formulário e registro anterior.

#### Dependências

Para iniciar: ‘Gestão de transações - Cadastro e conferência de uma transação própria’, com formulário e consulta individual. Para concluir: integrar ‘Gestão de transações - Agendamentos e competência financeira’ e ‘Gestão de transações - Histórico por período’, verificando valores antes/depois e atualização das consultas. Persistência isolada não basta para encerrar.

#### Referências

Item pai Redmine `#1015911`; regras/critérios R7, CA7-edicao, CA8, CA9-edicao, CA10-edicao, CA12-edicao, F-edicao-validacao.

### 6. [DEV] [WEB] [USUARIO] Gestão de transações - Exclusão confirmada com efeito único

#### Entrega

Permitir confirmar ou cancelar exclusão de registro próprio. A entrega remove sua contribuição financeira uma única vez, atualiza as consultas e preserva registros distintos com dados iguais.

#### Escopo e limites

Não oferece desfazer nem reimplementa os cálculos. Remover dados sem conferir seu efeito financeiro e sua repetição não conclui esta entrega.

#### Critérios de aceite

- Excluir somente após confirmação, removendo do histórico e cálculos, sem desfazer.
- CA7: detalhes próprios oferecem exclusão; outra conta não pode excluir por tela ou identificador direto.
- CA9: cancelar exclusão mantém dados/totais; confirmar remove do histórico/cálculos sem desfazer.
- CA12: exclusão de registros iguais é independente; repetir exclusão de registro removido não produz novo efeito nos totais.
- Fluxos alternativos: falha ao persistir exclusão não apresenta sucesso nem aplica alteração parcial; orienta nova tentativa.
- Conclusão exige efeitos integrados: na massa de referência com saldo R$ 85,00 em 01/12, excluir a despesa de R$ 30,00 produz R$ 115,00. Repetir a mesma exclusão mantém R$ 115,00; cancelar ou falhar antes de concluir mantém R$ 85,00.

#### Dependências

Para iniciar: ‘Gestão de transações - Cadastro e conferência de uma transação própria’, com consulta individual e propriedade. Para concluir: integrar ‘Gestão de transações - Agendamentos e competência financeira’ e ‘Gestão de transações - Histórico por período’, verificando remoção do efeito, repetição sem novo efeito e atualização das consultas.

#### Referências

Item pai Redmine `#1015911`; regras/critérios R8, CA7-exclusao, CA9-exclusao, CA12-exclusao, F-exclusao-falha.

## Publicação proposta

Seis DEV novas e uma QA. Sem filhas existentes para adoção/preservação. Projeto FinAi65224; mãe Feature1015911; DEV Task4; QA Deliverable5; New1; Normal4; Sprint1 (20355) herdada; sem categoria, responsável ou datas. Pai e relações entre Features permanecem preservados. Nenhum bloqueio externo novo.

### Relações nativas propostas

- **[DEV] [WEB] [USUARIO] Gestão de transações - Cadastro e conferência de uma transação própria** bloqueia **[QA] [WEB] [USUARIO] Gestão de transações**.
- **[DEV] [WEB] [USUARIO] Gestão de transações - Cadastro e conferência de uma transação própria** bloqueia **[DEV] [WEB] [USUARIO] Gestão de transações - Histórico por período**.
- **[DEV] [WEB] [USUARIO] Gestão de transações - Histórico por período** bloqueia **[QA] [WEB] [USUARIO] Gestão de transações**.
- **[DEV] [WEB] [USUARIO] Gestão de transações - Histórico por período** bloqueia **[DEV] [WEB] [USUARIO] Gestão de transações - Busca por descrição, tipo e categoria**.
- **[DEV] [WEB] [USUARIO] Gestão de transações - Busca por descrição, tipo e categoria** bloqueia **[QA] [WEB] [USUARIO] Gestão de transações**.
- **[DEV] [WEB] [USUARIO] Gestão de transações - Cadastro e conferência de uma transação própria** bloqueia **[DEV] [WEB] [USUARIO] Gestão de transações - Agendamentos e competência financeira**.
- **[DEV] [WEB] [USUARIO] Gestão de transações - Agendamentos e competência financeira** bloqueia **[QA] [WEB] [USUARIO] Gestão de transações**.
- **[DEV] [WEB] [USUARIO] Gestão de transações - Cadastro e conferência de uma transação própria** bloqueia **[DEV] [WEB] [USUARIO] Gestão de transações - Edição de transação com efeitos financeiros**.
- **[DEV] [WEB] [USUARIO] Gestão de transações - Edição de transação com efeitos financeiros** bloqueia **[QA] [WEB] [USUARIO] Gestão de transações**.
- **[DEV] [WEB] [USUARIO] Gestão de transações - Cadastro e conferência de uma transação própria** bloqueia **[DEV] [WEB] [USUARIO] Gestão de transações - Exclusão confirmada com efeito único**.
- **[DEV] [WEB] [USUARIO] Gestão de transações - Exclusão confirmada com efeito único** bloqueia **[QA] [WEB] [USUARIO] Gestão de transações**.

### Documento de condições

Fonte aprovada nesta revisão: CT-001 a CT-034, com IDs preservados e conteúdo atualizado. DOCX previsto `slices/condicoes-teste-r005.docx`, gerado após aprovação e anexado à nova QA; Markdown complementar `slices/condicoes-teste-r005.md`. Hash da proposta `57ded1e557d2f64d63892edb9d4feecbce1944ffb5f362ebc4e779664fc6bb92`. Tamanho/hash binário serão conferidos antes do upload. Revisão1 permanece preservada.

### [QA] [WEB] [USUARIO] Gestão de transações

Estimativa: **2h**; bloqueada pelas seis DEV.

#### Objetivo

Verificar as jornadas de transações e seus efeitos financeiros integrados, sem depender do dashboard.

#### Jornadas integradas

- CT-001: Cadastrar separadamente receita e despesa válidas e omitir cada campo obrigatório. Resultado esperado: Dados válidos salvam; ausência de qualquer campo impede salvar com erro.
- CT-002: Testar limites monetários, zero/negativo/acima do máximo e três casas; descrição vazia, espaços, 1,120,121 caracteres; datas limites, fora delas e inválidas. Resultado esperado: Limites inclusivos válidos são aceitos; demais entradas são recusadas sem arredondamento silencioso e com formulário preservado.
- CT-003: Conferir as listas para ambos os tipos e procurar ações de criar, renomear ou excluir categoria. Resultado esperado: Listas correspondem exatamente às categorias aprovadas e não permitem manutenção.
- CT-004: Cadastrar como A e tentar escolher B como proprietário; sair e entrar como A para consultar; tentar cadastrar sem sessão e sem e-mail confirmado. Resultado esperado: Registro pertence apenas a A e permanece persistido; proprietário alheio não é aceito e usuários não habilitados não operam.
- CT-005: Na massa M, conferir indicação e cálculos às 23:59:59 de30/11 e às00:00:00 de01/12 em Brasília, quando UTC já está no próximo dia antes da virada local. Resultado esperado: Antes: saldo70, novembro receitas100/despesas30, dezembro0/0; futuras agendadas. Depois: saldo85, novembro100/30, dezembro20/5; registros de01/12 deixam de ser agendados sem confirmação ou pagamento externo.
- CT-006: Comparar a capacidade interna com a massa M antes/depois da virada, excluídos e outra conta presentes. Em cenários separados usar apenas despesa10; e receitas0,10+0,20 com despesa0,01. Resultado esperado: Massa M retorna70 antes e85 depois; excluída7 e contaB900 não entram. Somente despesa10 retorna saldo-10. Centavos retornam saldo0,29 exato. Não existe saldo inicial separado.
- CT-007: Em01/12 na massa M, pela operação real de edição, mover receita100 para02/12 e depois devolver a30/11. Em cenários independentes, mudar despesa30 para40, e mudar despesa30 para receita30 com categoria compatível. Resultado esperado: Datas: saldo85→-15→85, novembro receitas100→0→100. Valor: saldo75 e novembro despesa40. Tipo: saldo145 e novembro receitas130/despesas0. Mesmo registro atualizado, sem duplicação.
- CT-008: Em01/12 na massa M, confirmar pela aplicação a exclusão da despesa30; conferir consulta individual, histórico e capacidade de cálculo. Resultado esperado: Registro indisponível/removido, saldo115, novembro receitas100/despesas0, dezembro20/5; sem desfazer.
- CT-009: Usar mais de 50 registros e descrições acentuadas; buscar trecho com caixa/acentos diferentes, combinar filtros, navegar, mudar filtro e limpar. Resultado esperado: Resultados próprios respeitam combinações e ordem; páginas têm até 50, mantêm filtros, alteração retorna à primeira e limpeza retorna ao histórico integral.
- CT-010: Salvar transação e conferir a leitura individual; depois acessar o mesmo registro pelo histórico. Resultado esperado: Tipo, valor em reais/centavos, descrição, categoria e data brasileira coincidem nas duas entradas; histórico reutiliza a consulta individual.
- CT-011: Consultar histórico misturando datas futuras, atuais e passadas e atravessar a data prevista. Resultado esperado: Futuras se integram à ordem cronológica e deixam de ser agendadas na data, sem fila separada.
- CT-012: Cadastrar receita e despesa; conferir os campos persistidos na consulta individual. Guardar seu endereço, sair, entrar novamente e reabri-lo sem depender da busca ou do histórico. Resultado esperado: Sucesso corresponde à gravação e o titular reencontra os mesmos dados persistidos; não depende de memória do formulário.
- CT-013: Enviar formulário com cada classe de erro e corrigir sem redigitar campos válidos. Resultado esperado: Não cria registro inválido; exibe erros e conserva dados para correção.
- CT-014: Na massa M em30/11 consultar internamente totais de dezembro e conferir registros futuros nas consultas individuais e histórico. Resultado esperado: Receita20/despesa5 de01/12 permanecem agendadas; dezembro0/0 e saldo70, embora o mês futuro seja selecionado.
- CT-015: Reexecutar a consulta na massa M imediatamente antes/depois da virada local, sem editar registros, clicar em confirmação ou esperar a virada real. Resultado esperado: Virada controlada altera saldo70→85 e dezembro0/0→20/5; indicação de agendada desaparece na consulta correspondente.
- CT-016: Usar duas contas e períodos distintos; abrir consulta inicial, trocar mês/todos e combinar filtros. Resultado esperado: Padrão mês atual; resultados somente da conta e correspondentes, com ordenação/paginação correta.
- CT-017: Abrir histórico de conta sem nenhuma movimentação. Resultado esperado: Apresenta estado vazio e caminho para cadastrar.
- CT-018: Em conta com registros, aplicar busca sem correspondência e limpar filtros. Resultado esperado: Informa ausência de correspondência e permite retomar todo histórico.
- CT-019: Como B, tentar o endereço individual de A e percorrer o histórico; como A, reabrir o próprio registro após novo login. Resultado esperado: Consulta individual e descoberta ficam limitadas ao titular; acesso alheio não expõe dados.
- CT-020: Editar registro próprio e tentar alterar o de outra conta por acesso direto. Resultado esperado: Somente proprietário habilitado altera; tentativa alheia não muda dados nem revela conteúdo.
- CT-021: Solicitar exclusão própria e tentar excluir registro alheio. Resultado esperado: Ação disponível ao titular; acesso alheio não remove nem revela dados.
- CT-022: Editar os cinco campos pela aplicação, conferir consulta individual/histórico e resultados internos antes/depois; incluir a massa M e as transições de CT-007. Resultado esperado: Identidade e propriedade preservadas; consultas atualizadas e cálculos coincidem com a nova contribuição. Edição não pode ser concluída apenas com prova de gravação.
- CT-023: Preencher cadastro e cancelar. Resultado esperado: Nenhum registro novo nem alteração financeira.
- CT-024: Na massa M em01/12, alterar campos no formulário e cancelar; conferir registro e capacidade interna. Resultado esperado: Persistência original e saldo85 permanecem; nenhuma contribuição foi alterada.
- CT-025: Em tentativas independentes na massa M em01/12, cancelar exclusão da despesa30 e depois confirmar. Conferir dados e valores internos. Resultado esperado: Cancelar mantém saldo85 e registro; confirmar produz115 e remove só o escolhido.
- CT-026: Provocar falha controlada de persistência no cadastro e tentar novamente após restauração. Resultado esperado: Sem gravação parcial ou falso sucesso; usuário recebe orientação de tentar novamente.
- CT-027: Provocar falha em edição e editar identificador removido/indisponível. Resultado esperado: Sem alteração parcial, falso sucesso ou dados alheios; informa indisponibilidade ou nova tentativa conforme caso.
- CT-028: Abrir identificador inexistente ou removido. Resultado esperado: Informa indisponibilidade sem dados de outra conta.
- CT-029: Cadastrar duas vezes em operações distintas com mesmo tipo/valor/descrição/categoria/data. Resultado esperado: Cria dois registros independentes.
- CT-030: Editar só um dos dois registros iguais. Resultado esperado: Somente o escolhido muda.
- CT-031: Excluir a despesa30 da massa M em01/12 e repetir a confirmação; em cenário separado com dois registros iguais, excluir apenas um. Resultado esperado: Saldo85→115→115 sem novo efeito na repetição. No cenário de iguais o outro registro e sua contribuição permanecem.
- CT-032: Selecionar categoria, mudar tipo e tentar salvar com categoria anterior incompatível. Resultado esperado: Exige seleção compatível e não grava combinação inválida.
- CT-033: Editar com cada campo ausente, valor inválido/precisão maior, descrição fora do limite, data inválida e tipo/categoria incompatíveis. Resultado esperado: Recusa, conserva dados para correção e preserva registro anterior.
- CT-034: Na massa M em01/12, provocar falha controlada na confirmação de exclusão e conferir persistência e valores internos. Resultado esperado: Registro permanece e saldo85 é preservado, sem falso sucesso; orienta nova tentativa.

#### Regras e permissões

- Tipo receita/despesa, valor positivo em reais, descrição, categoria e data são obrigatórios; tipo determina entrada ou saída.
- Valor entre R$ 0,01 e R$ 999.999.999,99 com até duas casas; não arredondar entrada com precisão maior. Descrição entre 1 e 120 caracteres após aparar extremidades. Data válida de 01/01/1900 a 31/12/9999.
- Oferecer somente receitas: Salário, Freelance, Rendimentos, Outras receitas; despesas: Alimentação, Moradia, Transporte, Saúde, Educação, Lazer, Compras, Outras despesas. Sem manutenção de categorias.
- Vincular cadastro ao usuário autenticado com e-mail confirmado, sem aceitar outro proprietário; persistência permanece após sair e entrar.
- Data define competência em America/Sao_Paulo; futura é agendada, aparece no histórico e não afeta saldo/totais até início da data. Inclusão automática, sem confirmação manual nem pagamento externo.
- Saldo é receitas menos despesas de registros não excluídos até hoje; totais mensais usam data dentro do mês e até hoje. Mês futuro não realiza movimentações; saldo negativo permitido, sem saldo inicial separado.
- Editar todos os campos próprios em qualquer data; tipo, valor, categoria e data atualizam valores aplicáveis. Passada/hoje para futura retira efeito; futura para hoje/passada inclui.
- Excluir somente após confirmação, removendo do histórico e cálculos, sem desfazer.
- R9, busca e filtros: trecho da descrição sem distinguir caixa/acentos; tipo/categoria/período restringem o mesmo conjunto. Limpar filtros mostra todo o histórico; manter filtros entre páginas e retornar à primeira ao alterar um filtro.
- R10 e dados percebidos, consulta individual: conferir descrição, tipo, valor em reais com centavos, categoria e data brasileira do registro persistido, inclusive ao reabrir após novo login.
- R10: futuras mostram identificação de agendada, seguem ordenação por data sem fila separada; identificação cessa na data.
- R10 e dados percebidos, histórico: exibir descrição, tipo, valor em reais com centavos, categoria e data brasileira de cada registro, número de resultados e acesso à consulta individual já entregue.
- R9, navegação: ordenar por data da movimentação decrescente e cadastro mais recente em empate; páginas de 50 registros, permitindo percorrer todo o conjunto do período.
- Aplicar a massa M do documento de condições, com cenários reiniciados de forma independente. Valores esperados são definidos antes da execução; não são calculados pelo mesmo código que está sendo verificado.
- Conferir resultados internos por testes de integração sobre registros persistidos e relógio controlado, preservando implementação real de cálculo e consultas. Registrar comando da suíte, revisão testada, instante, massa, esperado e observado. Não criar dashboard, API, endpoint de produto ou script avulso para QA.

#### Impactos relacionados

- A consulta individual nasce no cadastro e é reutilizada pelo histórico, edição e exclusão; verificar reabertura após novo login e isolamento em todos os caminhos.
- Conferir visualmente a transição de agendada nas consultas já previstas e numericamente saldo/totais pela capacidade interna. As duas evidências se complementam.
- Edição e exclusão só podem ser consideradas completas com operações reais integradas ao cálculo e ao histórico, incluindo cancelamento, falha e repetição.

#### Critérios de conclusão

- Executar CT-001 a CT-034 na revisão corrente e registrar as evidências de interface e integração conforme o documento.
- Comprovar a massa M: saldo70→85 na virada; edição de data85→-15→85; exclusão da despesa30 com saldo85→115 e repetição115. Valores em reais.
- Não aceitar apenas atualização no banco ou retorno de sucesso como evidência dos efeitos financeiros de edição/exclusão.
- Registrar divergências e condições não executadas. Sem acesso à suíte reproduzível, ao relógio controlado ou às falhas necessárias, registrar impedimento de execução em vez de aprovação.

#### Referências

Item pai Redmine #1015911; regras/critérios R1, R2, R3, R4, R5, R6, R7, R8, R9, R10-campos, R10-agendada, CA1, CA2, CA3, CA4, CA5, CA6-vazio, CA6-busca, CA7-consulta, CA7-edicao, CA7-exclusao, CA8, CA9-cadastro, CA9-edicao, CA9-exclusao, CA10-cadastro, CA10-edicao, CA10-consulta, CA12-cadastro, CA12-edicao, CA12-exclusao, CA11, F-edicao-validacao, F-exclusao-falha, R10-historico, R9-navegacao, CA5-periodo, CA7-historico.

