# [QA] [WEB] [USUARIO] Gestão de transações

- Redmine: `#1015936`
- Tipo: `QA`
- Tracker: Deliverable (`5`)
- Item pai: `#1015911`
- Estimativa: `2h`

## Descrição

## Objetivo

Verificar as jornadas de transações e seus efeitos financeiros integrados, sem depender do dashboard.

## Jornadas integradas

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

## Regras e permissões

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

## Impactos relacionados

- A consulta individual nasce no cadastro e é reutilizada pelo histórico, edição e exclusão; verificar reabertura após novo login e isolamento em todos os caminhos.
- Conferir visualmente a transição de agendada nas consultas já previstas e numericamente saldo/totais pela capacidade interna. As duas evidências se complementam.
- Edição e exclusão só podem ser consideradas completas com operações reais integradas ao cálculo e ao histórico, incluindo cancelamento, falha e repetição.

## Critérios de conclusão

- Executar CT-001 a CT-034 na revisão corrente e registrar as evidências de interface e integração conforme o documento.
- Comprovar a massa M: saldo70→85 na virada; edição de data85→-15→85; exclusão da despesa30 com saldo85→115 e repetição115. Valores em reais.
- Não aceitar apenas atualização no banco ou retorno de sucesso como evidência dos efeitos financeiros de edição/exclusão.
- Registrar divergências e condições não executadas. Sem acesso à suíte reproduzível, ao relógio controlado ou às falhas necessárias, registrar impedimento de execução em vez de aprovação.

## Referências

Item pai Redmine #1015911; regras/critérios R1, R2, R3, R4, R5, R6, R7, R8, R9, R10-campos, R10-agendada, CA1, CA2, CA3, CA4, CA5, CA6-vazio, CA6-busca, CA7-consulta, CA7-edicao, CA7-exclusao, CA8, CA9-cadastro, CA9-edicao, CA9-exclusao, CA10-cadastro, CA10-edicao, CA10-consulta, CA12-cadastro, CA12-edicao, CA12-exclusao, CA11, F-edicao-validacao, F-exclusao-falha, R10-historico, R9-navegacao, CA5-periodo, CA7-historico.

<!-- project-slices-child:ecc3236abdb0db6f80a3dfe7cb47b1fd92c6091a52ac594623330159e6d16ea1 -->

## Relações

- `#1015930` blocks `#1015936`
- `#1015931` blocks `#1015936`
- `#1015932` blocks `#1015936`
- `#1015933` blocks `#1015936`
- `#1015934` blocks `#1015936`
- `#1015935` blocks `#1015936`
