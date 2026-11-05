# Condições de teste

## Contexto

Usuário autenticado com e-mail confirmado. Preparar duas contas, todas as categorias, valores/descrições/datas de limite, mais de50 registros, datas passadas/atuais/futuras, virada controlada em America/Sao_Paulo e falhas de persistência controladas. Condições futuras de QA, sem alegação de execução. Verificar na interface a indicação de agendada e usar testes de integração reproduzíveis da capacidade interna de cálculo, com banco de teste real, relógio controlado e sem substituir cálculo ou consulta por respostas simuladas. Não usar dashboard, endpoint novo ou script avulso. Registrar comando da suíte, revisão testada, massa, instante, esperado e observado. Massa M: usuário A com receita R$ 100,00 e despesa R$ 30,00 em 30/11/2026; receita R$ 20,00 e despesa R$ 5,00 em 01/12/2026; receita R$ 7,00 excluída em 30/11. Usuário B com receita R$ 900,00 em 30/11. Relógio em America/Sao_Paulo. Cada cenário recomeça da massa, sem depender do resultado de outro. Para efeitos de edição/exclusão, executar a operação real da aplicação antes de consultar os cálculos; alteração direta da massa não comprova integração da mutação.

### CT-001 — R1 — Cadastro e conferência de uma transação própria

Verificação: Cadastrar separadamente receita e despesa válidas e omitir cada campo obrigatório.

Resultado esperado: Dados válidos salvam; ausência de qualquer campo impede salvar com erro.

Origem no requisito: R1: Tipo receita/despesa, valor positivo em reais, descrição, categoria e data são obrigatórios; tipo determina entrada ou saída.

### CT-002 — R2 — Cadastro e conferência de uma transação própria

Verificação: Testar limites monetários, zero/negativo/acima do máximo e três casas; descrição vazia, espaços, 1,120,121 caracteres; datas limites, fora delas e inválidas.

Resultado esperado: Limites inclusivos válidos são aceitos; demais entradas são recusadas sem arredondamento silencioso e com formulário preservado.

Origem no requisito: R2: Valor entre R$ 0,01 e R$ 999.999.999,99 com até duas casas; não arredondar entrada com precisão maior. Descrição entre 1 e 120 caracteres após aparar extremidades. Data válida de 01/01/1900 a 31/12/9999.

### CT-003 — R3 — Cadastro e conferência de uma transação própria

Verificação: Conferir as listas para ambos os tipos e procurar ações de criar, renomear ou excluir categoria.

Resultado esperado: Listas correspondem exatamente às categorias aprovadas e não permitem manutenção.

Origem no requisito: R3: Oferecer somente receitas: Salário, Freelance, Rendimentos, Outras receitas; despesas: Alimentação, Moradia, Transporte, Saúde, Educação, Lazer, Compras, Outras despesas. Sem manutenção de categorias.

### CT-004 — R4 — Cadastro e conferência de uma transação própria

Verificação: Cadastrar como A e tentar escolher B como proprietário; sair e entrar como A para consultar; tentar cadastrar sem sessão e sem e-mail confirmado.

Resultado esperado: Registro pertence apenas a A e permanece persistido; proprietário alheio não é aceito e usuários não habilitados não operam.

Origem no requisito: R4: Vincular cadastro ao usuário autenticado com e-mail confirmado, sem aceitar outro proprietário; persistência permanece após sair e entrar.

### CT-005 — R5 — Agendamentos e competência financeira

Contexto: Verificação de valores pela capacidade interna conforme contexto e massa M; evidência reproduzível da integração, sem interface financeira adicional.

Verificação: Na massa M, conferir indicação e cálculos às 23:59:59 de30/11 e às00:00:00 de01/12 em Brasília, quando UTC já está no próximo dia antes da virada local.

Resultado esperado: Antes: saldo70, novembro receitas100/despesas30, dezembro0/0; futuras agendadas. Depois: saldo85, novembro100/30, dezembro20/5; registros de01/12 deixam de ser agendados sem confirmação ou pagamento externo.

Origem no requisito: R5: Data define competência em America/Sao_Paulo; futura é agendada, aparece no histórico e não afeta saldo/totais até início da data. Inclusão automática, sem confirmação manual nem pagamento externo.

### CT-006 — R6 — Agendamentos e competência financeira

Contexto: Verificação de valores pela capacidade interna conforme contexto e massa M; evidência reproduzível da integração, sem interface financeira adicional.

Verificação: Comparar a capacidade interna com a massa M antes/depois da virada, excluídos e outra conta presentes. Em cenários separados usar apenas despesa10; e receitas0,10+0,20 com despesa0,01.

Resultado esperado: Massa M retorna70 antes e85 depois; excluída7 e contaB900 não entram. Somente despesa10 retorna saldo-10. Centavos retornam saldo0,29 exato. Não existe saldo inicial separado.

Origem no requisito: R6: Saldo é receitas menos despesas de registros não excluídos até hoje; totais mensais usam data dentro do mês e até hoje. Mês futuro não realiza movimentações; saldo negativo permitido, sem saldo inicial separado.

### CT-007 — R7 — Edição de transação com efeitos financeiros

Contexto: Verificação de valores pela capacidade interna conforme contexto e massa M; evidência reproduzível da integração, sem interface financeira adicional.

Verificação: Em01/12 na massa M, pela operação real de edição, mover receita100 para02/12 e depois devolver a30/11. Em cenários independentes, mudar despesa30 para40, e mudar despesa30 para receita30 com categoria compatível.

Resultado esperado: Datas: saldo85→-15→85, novembro receitas100→0→100. Valor: saldo75 e novembro despesa40. Tipo: saldo145 e novembro receitas130/despesas0. Mesmo registro atualizado, sem duplicação.

Origem no requisito: R7: Editar todos os campos próprios em qualquer data; tipo, valor, categoria e data atualizam valores aplicáveis. Passada/hoje para futura retira efeito; futura para hoje/passada inclui.

### CT-008 — R8 — Exclusão confirmada com efeito único

Contexto: Verificação de valores pela capacidade interna conforme contexto e massa M; evidência reproduzível da integração, sem interface financeira adicional.

Verificação: Em01/12 na massa M, confirmar pela aplicação a exclusão da despesa30; conferir consulta individual, histórico e capacidade de cálculo.

Resultado esperado: Registro indisponível/removido, saldo115, novembro receitas100/despesas0, dezembro20/5; sem desfazer.

Origem no requisito: R8: Excluir somente após confirmação, removendo do histórico e cálculos, sem desfazer.

### CT-009 — R9 — Busca por descrição, tipo e categoria

Verificação: Usar mais de 50 registros e descrições acentuadas; buscar trecho com caixa/acentos diferentes, combinar filtros, navegar, mudar filtro e limpar.

Resultado esperado: Resultados próprios respeitam combinações e ordem; páginas têm até 50, mantêm filtros, alteração retorna à primeira e limpeza retorna ao histórico integral.

Origem no requisito: R9: R9, busca e filtros: trecho da descrição sem distinguir caixa/acentos; tipo/categoria/período restringem o mesmo conjunto. Limpar filtros mostra todo o histórico; manter filtros entre páginas e retornar à primeira ao alterar um filtro.; R9-navegacao: R9, navegação: ordenar por data da movimentação decrescente e cadastro mais recente em empate; páginas de 50 registros, permitindo percorrer todo o conjunto do período.

### CT-010 — Campos na consulta individual e no histórico

Verificação: Salvar transação e conferir a leitura individual; depois acessar o mesmo registro pelo histórico.

Resultado esperado: Tipo, valor em reais/centavos, descrição, categoria e data brasileira coincidem nas duas entradas; histórico reutiliza a consulta individual.

Origem no requisito: R10-campos: R10 e dados percebidos, consulta individual: conferir descrição, tipo, valor em reais com centavos, categoria e data brasileira do registro persistido, inclusive ao reabrir após novo login.; R10-historico: R10 e dados percebidos, histórico: exibir descrição, tipo, valor em reais com centavos, categoria e data brasileira de cada registro, número de resultados e acesso à consulta individual já entregue.

### CT-011 — R10-agendada — Agendamentos e competência financeira

Verificação: Consultar histórico misturando datas futuras, atuais e passadas e atravessar a data prevista.

Resultado esperado: Futuras se integram à ordem cronológica e deixam de ser agendadas na data, sem fila separada.

Origem no requisito: R10-agendada: R10: futuras mostram identificação de agendada, seguem ordenação por data sem fila separada; identificação cessa na data.

### CT-012 — CA1 — Cadastro e conferência de uma transação própria

Verificação: Cadastrar receita e despesa; conferir os campos persistidos na consulta individual. Guardar seu endereço, sair, entrar novamente e reabri-lo sem depender da busca ou do histórico.

Resultado esperado: Sucesso corresponde à gravação e o titular reencontra os mesmos dados persistidos; não depende de memória do formulário.

Origem no requisito: CA1: Salvar receita/despesa válida cria um registro próprio, mostra sucesso e mantém dados após novo acesso.

### CT-013 — CA2 — Cadastro e conferência de uma transação própria

Verificação: Enviar formulário com cada classe de erro e corrigir sem redigitar campos válidos.

Resultado esperado: Não cria registro inválido; exibe erros e conserva dados para correção.

Origem no requisito: CA2: Ausências, categoria incompatível, valores/datas fora de R2 e descrição vazia/longa impedem salvar, mostram erros e preservam o formulário.

### CT-014 — CA3 — Agendamentos e competência financeira

Contexto: Verificação de valores pela capacidade interna conforme contexto e massa M; evidência reproduzível da integração, sem interface financeira adicional.

Verificação: Na massa M em30/11 consultar internamente totais de dezembro e conferir registros futuros nas consultas individuais e histórico.

Resultado esperado: Receita20/despesa5 de01/12 permanecem agendadas; dezembro0/0 e saldo70, embora o mês futuro seja selecionado.

Origem no requisito: CA3: Futura aparece agendada e não afeta saldo nem totais, mesmo na consulta de seu mês futuro.

### CT-015 — CA4 — Agendamentos e competência financeira

Contexto: Verificação de valores pela capacidade interna conforme contexto e massa M; evidência reproduzível da integração, sem interface financeira adicional.

Verificação: Reexecutar a consulta na massa M imediatamente antes/depois da virada local, sem editar registros, clicar em confirmação ou esperar a virada real.

Resultado esperado: Virada controlada altera saldo70→85 e dezembro0/0→20/5; indicação de agendada desaparece na consulta correspondente.

Origem no requisito: CA4: Ao chegar a data em America/Sao_Paulo, compõe valores de R6 sem confirmação e perde marcação de agendada.

### CT-016 — CA5 — Busca por descrição, tipo e categoria

Verificação: Usar duas contas e períodos distintos; abrir consulta inicial, trocar mês/todos e combinar filtros.

Resultado esperado: Padrão mês atual; resultados somente da conta e correspondentes, com ordenação/paginação correta.

Origem no requisito: CA5: CA5, busca combinada: descrição, tipo e categoria combinados com período retornam apenas registros correspondentes do usuário, preservando ordenação e paginação do histórico.; CA5-periodo: CA5, período: iniciar histórico no mês atual, permitir outro mês ou todo histórico; mudar período retorna à primeira página.

### CT-017 — CA6-vazio — Histórico por período

Verificação: Abrir histórico de conta sem nenhuma movimentação.

Resultado esperado: Apresenta estado vazio e caminho para cadastrar.

Origem no requisito: CA6-vazio: CA6: histórico sem registros orienta primeiro cadastro.

### CT-018 — CA6-busca — Busca por descrição, tipo e categoria

Verificação: Em conta com registros, aplicar busca sem correspondência e limpar filtros.

Resultado esperado: Informa ausência de correspondência e permite retomar todo histórico.

Origem no requisito: CA6-busca: CA6: busca sem resultados difere do histórico vazio e permite ajustar/limpar; limpar retorna histórico integral.

### CT-019 — CA7-consulta — Histórico por período

Verificação: Como B, tentar o endereço individual de A e percorrer o histórico; como A, reabrir o próprio registro após novo login.

Resultado esperado: Consulta individual e descoberta ficam limitadas ao titular; acesso alheio não expõe dados.

Origem no requisito: CA7-consulta: CA7, consulta individual: titular habilitado consulta todos os campos do próprio registro; identificador de outra conta não revela seus dados.; CA7-historico: CA7 e permissões, descoberta: histórico e seus resultados não revelam registros de outra conta e levam somente à consulta individual autorizada.

### CT-020 — CA7-edicao — Edição de transação com efeitos financeiros

Verificação: Editar registro próprio e tentar alterar o de outra conta por acesso direto.

Resultado esperado: Somente proprietário habilitado altera; tentativa alheia não muda dados nem revela conteúdo.

Origem no requisito: CA7-edicao: CA7: detalhes próprios oferecem edição; outra conta não pode alterar por tela ou identificador direto.

### CT-021 — CA7-exclusao — Exclusão confirmada com efeito único

Verificação: Solicitar exclusão própria e tentar excluir registro alheio.

Resultado esperado: Ação disponível ao titular; acesso alheio não remove nem revela dados.

Origem no requisito: CA7-exclusao: CA7: detalhes próprios oferecem exclusão; outra conta não pode excluir por tela ou identificador direto.

### CT-022 — CA8 — Edição de transação com efeitos financeiros

Contexto: Verificação de valores pela capacidade interna conforme contexto e massa M; evidência reproduzível da integração, sem interface financeira adicional.

Verificação: Editar os cinco campos pela aplicação, conferir consulta individual/histórico e resultados internos antes/depois; incluir a massa M e as transições de CT-007.

Resultado esperado: Identidade e propriedade preservadas; consultas atualizadas e cálculos coincidem com a nova contribuição. Edição não pode ser concluída apenas com prova de gravação.

Origem no requisito: CA8: Editar campo válido atualiza o mesmo registro e seus efeitos; mover passada para futura retira contribuição e inverso inclui.

### CT-023 — CA9-cadastro — Cadastro e conferência de uma transação própria

Contexto: Verificação de valores pela capacidade interna conforme contexto e massa M; evidência reproduzível da integração, sem interface financeira adicional.

Verificação: Preencher cadastro e cancelar.

Resultado esperado: Nenhum registro novo nem alteração financeira.

Origem no requisito: CA9-cadastro: CA9: cancelar cadastro não modifica registros nem totais.

### CT-024 — CA9-edicao — Edição de transação com efeitos financeiros

Contexto: Verificação de valores pela capacidade interna conforme contexto e massa M; evidência reproduzível da integração, sem interface financeira adicional.

Verificação: Na massa M em01/12, alterar campos no formulário e cancelar; conferir registro e capacidade interna.

Resultado esperado: Persistência original e saldo85 permanecem; nenhuma contribuição foi alterada.

Origem no requisito: CA9-edicao: CA9: cancelar edição conserva registro e totais anteriores.

### CT-025 — CA9-exclusao — Exclusão confirmada com efeito único

Contexto: Verificação de valores pela capacidade interna conforme contexto e massa M; evidência reproduzível da integração, sem interface financeira adicional.

Verificação: Em tentativas independentes na massa M em01/12, cancelar exclusão da despesa30 e depois confirmar. Conferir dados e valores internos.

Resultado esperado: Cancelar mantém saldo85 e registro; confirmar produz115 e remove só o escolhido.

Origem no requisito: CA9-exclusao: CA9: cancelar exclusão mantém dados/totais; confirmar remove do histórico/cálculos sem desfazer.

### CT-026 — CA10-cadastro — Cadastro e conferência de uma transação própria

Verificação: Provocar falha controlada de persistência no cadastro e tentar novamente após restauração.

Resultado esperado: Sem gravação parcial ou falso sucesso; usuário recebe orientação de tentar novamente.

Origem no requisito: CA10-cadastro: CA10: falha ao cadastrar não grava parcialmente nem mostra sucesso; orienta nova tentativa.

### CT-027 — CA10-edicao — Edição de transação com efeitos financeiros

Contexto: Verificação de valores pela capacidade interna conforme contexto e massa M; evidência reproduzível da integração, sem interface financeira adicional.

Verificação: Provocar falha em edição e editar identificador removido/indisponível.

Resultado esperado: Sem alteração parcial, falso sucesso ou dados alheios; informa indisponibilidade ou nova tentativa conforme caso.

Origem no requisito: CA10-edicao: CA10: falha ao editar não altera parcialmente nem mostra sucesso; registro removido/indisponível não pode ser alterado e não revela dados de terceiros.

### CT-028 — CA10-consulta — Histórico por período

Verificação: Abrir identificador inexistente ou removido.

Resultado esperado: Informa indisponibilidade sem dados de outra conta.

Origem no requisito: CA10-consulta: CA10: registro indisponível não revela dados de terceiros e a interface informa indisponibilidade.

### CT-029 — CA12-cadastro — Cadastro e conferência de uma transação própria

Verificação: Cadastrar duas vezes em operações distintas com mesmo tipo/valor/descrição/categoria/data.

Resultado esperado: Cria dois registros independentes.

Origem no requisito: CA12-cadastro: CA12: duas operações distintas com dados iguais podem criar duas transações, sem deduplicação automática.

### CT-030 — CA12-edicao — Edição de transação com efeitos financeiros

Verificação: Editar só um dos dois registros iguais.

Resultado esperado: Somente o escolhido muda.

Origem no requisito: CA12-edicao: CA12: registros com dados iguais possuem edição independente.

### CT-031 — CA12-exclusao — Exclusão confirmada com efeito único

Contexto: Verificação de valores pela capacidade interna conforme contexto e massa M; evidência reproduzível da integração, sem interface financeira adicional.

Verificação: Excluir a despesa30 da massa M em01/12 e repetir a confirmação; em cenário separado com dois registros iguais, excluir apenas um.

Resultado esperado: Saldo85→115→115 sem novo efeito na repetição. No cenário de iguais o outro registro e sua contribuição permanecem.

Origem no requisito: CA12-exclusao: CA12: exclusão de registros iguais é independente; repetir exclusão de registro removido não produz novo efeito nos totais.

### CT-032 — CA11 — Cadastro e conferência de uma transação própria

Verificação: Selecionar categoria, mudar tipo e tentar salvar com categoria anterior incompatível.

Resultado esperado: Exige seleção compatível e não grava combinação inválida.

Origem no requisito: CA11: Categorias disponíveis correspondem exatamente a R3; trocar tipo não mantém categoria incompatível silenciosamente nem permite concluir com ela.

### CT-033 — F-edicao-validacao — Edição de transação com efeitos financeiros

Verificação: Editar com cada campo ausente, valor inválido/precisão maior, descrição fora do limite, data inválida e tipo/categoria incompatíveis.

Resultado esperado: Recusa, conserva dados para correção e preserva registro anterior.

Origem no requisito: F-edicao-validacao: Fluxos alternativos: edição inválida preserva formulário, mostra erros e não altera dados; limites R1–R3 e troca de tipo/categoria aplicam-se também à edição.

### CT-034 — F-exclusao-falha — Exclusão confirmada com efeito único

Contexto: Verificação de valores pela capacidade interna conforme contexto e massa M; evidência reproduzível da integração, sem interface financeira adicional.

Verificação: Na massa M em01/12, provocar falha controlada na confirmação de exclusão e conferir persistência e valores internos.

Resultado esperado: Registro permanece e saldo85 é preservado, sem falso sucesso; orienta nova tentativa.

Origem no requisito: F-exclusao-falha: Fluxos alternativos: falha ao persistir exclusão não apresenta sucesso nem aplica alteração parcial; orienta nova tentativa.
