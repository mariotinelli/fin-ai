# Fatiamento de [WEB] [USUARIO] Gestão de transações

Revisão: 1  
Hash: `85887de6a7037e9056e83207c7f54b30486c239eb55c4ed6cb024a51d0faa889`

## Prévia numerada

1. **[DEV] [WEB] [USUARIO] Gestão de transações - Cadastro de receitas e despesas próprias** — 6h
   - Entrega: Criar o cadastro de movimentações próprias com persistência, categorias predefinidas e validações. A autenticação e a confirmação de e-mail existentes devem ser preservadas.
   - Bloqueado por: Nenhum
   - Bloqueios externos: Nenhum
2. **[DEV] [WEB] [USUARIO] Gestão de transações - Histórico e detalhes próprios** — 4.5h
   - Entrega: Criar a consulta das movimentações e de seus detalhes, limitada à conta autenticada, com campos legíveis e estado vazio.
   - Bloqueado por: 1
   - Bloqueios externos: Nenhum
3. **[DEV] [WEB] [USUARIO] Gestão de transações - Busca e filtros do histórico** — 5h
   - Entrega: Permitir localizar movimentações por período, descrição, tipo e categoria, com contagem, ordenação e paginação consistentes.
   - Bloqueado por: 2
   - Bloqueios externos: Nenhum
4. **[DEV] [WEB] [USUARIO] Gestão de transações - Vigência das movimentações por data** — 4.5h
   - Entrega: Identificar movimentações futuras como agendadas e aplicar automaticamente sua competência financeira quando chegar a data em Brasília.
   - Bloqueado por: 2
   - Bloqueios externos: Nenhum
5. **[DEV] [WEB] [USUARIO] Gestão de transações - Edição de movimentações próprias** — 4h
   - Entrega: Permitir corrigir todos os campos de uma movimentação própria sem mudar sua identidade, refletindo a alteração no histórico e nos valores aplicáveis.
   - Bloqueado por: 2
   - Bloqueios externos: Nenhum
6. **[DEV] [WEB] [USUARIO] Gestão de transações - Exclusão confirmada de movimentações** — 3h
   - Entrega: Permitir excluir movimentação própria após confirmação, removendo seu efeito uma única vez e permitindo cancelar antes da exclusão.
   - Bloqueado por: 2
   - Bloqueios externos: Nenhum

## Cobertura

| Regra ou critério | Destino | Evidência |
| --- | --- | --- |
| R1: Tipo receita/despesa, valor positivo em reais, descrição, categoria e data são obrigatórios; tipo determina entrada ou saída. | Slice 1 | Capacidade financeira ausente em app/Models, routes/web.php, database/migrations e resources/js/pages. Cadastro de receitas e despesas próprias entrega este comportamento; autenticação existente é preservada. |
| R2: Valor entre R$ 0,01 e R$ 999.999.999,99 com até duas casas; não arredondar entrada com precisão maior. Descrição entre 1 e 120 caracteres após aparar extremidades. Data válida de 01/01/1900 a 31/12/9999. | Slice 1 | Capacidade financeira ausente em app/Models, routes/web.php, database/migrations e resources/js/pages. Cadastro de receitas e despesas próprias entrega este comportamento; autenticação existente é preservada. |
| R3: Oferecer somente receitas: Salário, Freelance, Rendimentos, Outras receitas; despesas: Alimentação, Moradia, Transporte, Saúde, Educação, Lazer, Compras, Outras despesas. Sem manutenção de categorias. | Slice 1 | Capacidade financeira ausente em app/Models, routes/web.php, database/migrations e resources/js/pages. Cadastro de receitas e despesas próprias entrega este comportamento; autenticação existente é preservada. |
| R4: Vincular cadastro ao usuário autenticado com e-mail confirmado, sem aceitar outro proprietário; persistência permanece após sair e entrar. | Slice 1 | Capacidade financeira ausente em app/Models, routes/web.php, database/migrations e resources/js/pages. Cadastro de receitas e despesas próprias entrega este comportamento; autenticação existente é preservada. |
| R5: Data define competência em America/Sao_Paulo; futura é agendada, aparece no histórico e não afeta saldo/totais até início da data. Inclusão automática, sem confirmação manual nem pagamento externo. | Slice 4 | Capacidade financeira ausente em app/Models, routes/web.php, database/migrations e resources/js/pages. Vigência das movimentações por data entrega este comportamento; autenticação existente é preservada. |
| R6: Saldo é receitas menos despesas de registros não excluídos até hoje; totais mensais usam data dentro do mês e até hoje. Mês futuro não realiza movimentações; saldo negativo permitido, sem saldo inicial separado. | Slice 4 | Capacidade financeira ausente em app/Models, routes/web.php, database/migrations e resources/js/pages. Vigência das movimentações por data entrega este comportamento; autenticação existente é preservada. |
| R7: Editar todos os campos próprios em qualquer data; tipo, valor, categoria e data atualizam valores aplicáveis. Passada/hoje para futura retira efeito; futura para hoje/passada inclui. | Slice 5 | Capacidade financeira ausente em app/Models, routes/web.php, database/migrations e resources/js/pages. Edição de movimentações próprias entrega este comportamento; autenticação existente é preservada. |
| R8: Excluir somente após confirmação, removendo do histórico e cálculos, sem desfazer. | Slice 6 | Capacidade financeira ausente em app/Models, routes/web.php, database/migrations e resources/js/pages. Exclusão confirmada de movimentações entrega este comportamento; autenticação existente é preservada. |
| R9: Busca por trecho sem distinguir caixa/acentos; período, tipo e categoria combinados no mesmo conjunto; limpar filtros mostra todo histórico. Ordenar data decrescente e cadastro mais recente em empate; páginas de 50, filtros mantidos, mudança retorna à primeira. | Slice 3 | Capacidade financeira ausente em app/Models, routes/web.php, database/migrations e resources/js/pages. Busca e filtros do histórico entrega este comportamento; autenticação existente é preservada. |
| R10-campos: R10 e dados percebidos: histórico/detalhes mostram descrição, tipo, valor em reais com centavos, categoria e data brasileira. | Slice 2 | Capacidade financeira ausente em app/Models, routes/web.php, database/migrations e resources/js/pages. Histórico e detalhes próprios entrega este comportamento; autenticação existente é preservada. |
| R10-agendada: R10: futuras mostram identificação de agendada, seguem ordenação por data sem fila separada; identificação cessa na data. | Slice 4 | Capacidade financeira ausente em app/Models, routes/web.php, database/migrations e resources/js/pages. Vigência das movimentações por data entrega este comportamento; autenticação existente é preservada. |
| CA1: Salvar receita/despesa válida cria um registro próprio, mostra sucesso e mantém dados após novo acesso. | Slice 1 | Capacidade financeira ausente em app/Models, routes/web.php, database/migrations e resources/js/pages. Cadastro de receitas e despesas próprias entrega este comportamento; autenticação existente é preservada. |
| CA2: Ausências, categoria incompatível, valores/datas fora de R2 e descrição vazia/longa impedem salvar, mostram erros e preservam o formulário. | Slice 1 | Capacidade financeira ausente em app/Models, routes/web.php, database/migrations e resources/js/pages. Cadastro de receitas e despesas próprias entrega este comportamento; autenticação existente é preservada. |
| CA3: Futura aparece agendada e não afeta saldo nem totais, mesmo na consulta de seu mês futuro. | Slice 4 | Capacidade financeira ausente em app/Models, routes/web.php, database/migrations e resources/js/pages. Vigência das movimentações por data entrega este comportamento; autenticação existente é preservada. |
| CA4: Ao chegar a data em America/Sao_Paulo, compõe valores de R6 sem confirmação e perde marcação de agendada. | Slice 4 | Capacidade financeira ausente em app/Models, routes/web.php, database/migrations e resources/js/pages. Vigência das movimentações por data entrega este comportamento; autenticação existente é preservada. |
| CA5: Histórico inicia no mês atual; escolher mês ou todo histórico e combinar descrição/tipo/categoria retorna apenas registros próprios com ordem/paginação de R9. | Slice 3 | Capacidade financeira ausente em app/Models, routes/web.php, database/migrations e resources/js/pages. Busca e filtros do histórico entrega este comportamento; autenticação existente é preservada. |
| CA6-vazio: CA6: histórico sem registros orienta primeiro cadastro. | Slice 2 | Capacidade financeira ausente em app/Models, routes/web.php, database/migrations e resources/js/pages. Histórico e detalhes próprios entrega este comportamento; autenticação existente é preservada. |
| CA6-busca: CA6: busca sem resultados difere do histórico vazio e permite ajustar/limpar; limpar retorna histórico integral. | Slice 3 | Capacidade financeira ausente em app/Models, routes/web.php, database/migrations e resources/js/pages. Busca e filtros do histórico entrega este comportamento; autenticação existente é preservada. |
| CA7-consulta: CA7: abrir registro próprio mostra todos os campos; listas, busca e detalhes não revelam registros de outra pessoa, inclusive por identificador direto. | Slice 2 | Capacidade financeira ausente em app/Models, routes/web.php, database/migrations e resources/js/pages. Histórico e detalhes próprios entrega este comportamento; autenticação existente é preservada. |
| CA7-edicao: CA7: detalhes próprios oferecem edição; outra conta não pode alterar por tela ou identificador direto. | Slice 5 | Capacidade financeira ausente em app/Models, routes/web.php, database/migrations e resources/js/pages. Edição de movimentações próprias entrega este comportamento; autenticação existente é preservada. |
| CA7-exclusao: CA7: detalhes próprios oferecem exclusão; outra conta não pode excluir por tela ou identificador direto. | Slice 6 | Capacidade financeira ausente em app/Models, routes/web.php, database/migrations e resources/js/pages. Exclusão confirmada de movimentações entrega este comportamento; autenticação existente é preservada. |
| CA8: Editar campo válido atualiza o mesmo registro e seus efeitos; mover passada para futura retira contribuição e inverso inclui. | Slice 5 | Capacidade financeira ausente em app/Models, routes/web.php, database/migrations e resources/js/pages. Edição de movimentações próprias entrega este comportamento; autenticação existente é preservada. |
| CA9-cadastro: CA9: cancelar cadastro não modifica registros nem totais. | Slice 1 | Capacidade financeira ausente em app/Models, routes/web.php, database/migrations e resources/js/pages. Cadastro de receitas e despesas próprias entrega este comportamento; autenticação existente é preservada. |
| CA9-edicao: CA9: cancelar edição conserva registro e totais anteriores. | Slice 5 | Capacidade financeira ausente em app/Models, routes/web.php, database/migrations e resources/js/pages. Edição de movimentações próprias entrega este comportamento; autenticação existente é preservada. |
| CA9-exclusao: CA9: cancelar exclusão mantém dados/totais; confirmar remove do histórico/cálculos sem desfazer. | Slice 6 | Capacidade financeira ausente em app/Models, routes/web.php, database/migrations e resources/js/pages. Exclusão confirmada de movimentações entrega este comportamento; autenticação existente é preservada. |
| CA10-cadastro: CA10: falha ao cadastrar não grava parcialmente nem mostra sucesso; orienta nova tentativa. | Slice 1 | Capacidade financeira ausente em app/Models, routes/web.php, database/migrations e resources/js/pages. Cadastro de receitas e despesas próprias entrega este comportamento; autenticação existente é preservada. |
| CA10-edicao: CA10: falha ao editar não altera parcialmente nem mostra sucesso; registro removido/indisponível não pode ser alterado e não revela dados de terceiros. | Slice 5 | Capacidade financeira ausente em app/Models, routes/web.php, database/migrations e resources/js/pages. Edição de movimentações próprias entrega este comportamento; autenticação existente é preservada. |
| CA10-consulta: CA10: registro indisponível não revela dados de terceiros e a interface informa indisponibilidade. | Slice 2 | Capacidade financeira ausente em app/Models, routes/web.php, database/migrations e resources/js/pages. Histórico e detalhes próprios entrega este comportamento; autenticação existente é preservada. |
| CA12-cadastro: CA12: duas operações distintas com dados iguais podem criar duas transações, sem deduplicação automática. | Slice 1 | Capacidade financeira ausente em app/Models, routes/web.php, database/migrations e resources/js/pages. Cadastro de receitas e despesas próprias entrega este comportamento; autenticação existente é preservada. |
| CA12-edicao: CA12: registros com dados iguais possuem edição independente. | Slice 5 | Capacidade financeira ausente em app/Models, routes/web.php, database/migrations e resources/js/pages. Edição de movimentações próprias entrega este comportamento; autenticação existente é preservada. |
| CA12-exclusao: CA12: exclusão de registros iguais é independente; repetir exclusão de registro removido não produz novo efeito nos totais. | Slice 6 | Capacidade financeira ausente em app/Models, routes/web.php, database/migrations e resources/js/pages. Exclusão confirmada de movimentações entrega este comportamento; autenticação existente é preservada. |
| CA11: Categorias disponíveis correspondem exatamente a R3; trocar tipo não mantém categoria incompatível silenciosamente nem permite concluir com ela. | Slice 1 | Capacidade financeira ausente em app/Models, routes/web.php, database/migrations e resources/js/pages. Cadastro de receitas e despesas próprias entrega este comportamento; autenticação existente é preservada. |
| F-edicao-validacao: Fluxos alternativos: edição inválida preserva formulário, mostra erros e não altera dados; limites R1–R3 e troca de tipo/categoria aplicam-se também à edição. | Slice 5 | Capacidade financeira ausente em app/Models, routes/web.php, database/migrations e resources/js/pages. Edição de movimentações próprias entrega este comportamento; autenticação existente é preservada. |
| F-exclusao-falha: Fluxos alternativos: falha ao persistir exclusão não apresenta sucesso nem aplica alteração parcial; orienta nova tentativa. | Slice 6 | Capacidade financeira ausente em app/Models, routes/web.php, database/migrations e resources/js/pages. Exclusão confirmada de movimentações entrega este comportamento; autenticação existente é preservada. |

Formato das condições: Markdown e DOCX.

## Condições de teste

Estas condições integram a aprovação da decomposição. A validação estrutural não substitui a revisão semântica do tech lead.

### Contexto

Usuário autenticado com e-mail confirmado. Preparar duas contas, todas as categorias, valores/descrições/datas de limite, mais de50 registros, datas passadas/atuais/futuras, virada controlada em America/Sao_Paulo e falhas de persistência controladas. Condições futuras de QA, sem alegação de execução.

#### CT-001 — R1 — Cadastro de receitas e despesas próprias

Verificação: Cadastrar separadamente receita e despesa válidas e omitir cada campo obrigatório.

Resultado esperado: Dados válidos salvam; ausência de qualquer campo impede salvar com erro.

Origem no requisito: R1: Tipo receita/despesa, valor positivo em reais, descrição, categoria e data são obrigatórios; tipo determina entrada ou saída.

#### CT-002 — R2 — Cadastro de receitas e despesas próprias

Verificação: Testar limites monetários, zero/negativo/acima do máximo e três casas; descrição vazia, espaços, 1,120,121 caracteres; datas limites, fora delas e inválidas.

Resultado esperado: Limites inclusivos válidos são aceitos; demais entradas são recusadas sem arredondamento silencioso e com formulário preservado.

Origem no requisito: R2: Valor entre R$ 0,01 e R$ 999.999.999,99 com até duas casas; não arredondar entrada com precisão maior. Descrição entre 1 e 120 caracteres após aparar extremidades. Data válida de 01/01/1900 a 31/12/9999.

#### CT-003 — R3 — Cadastro de receitas e despesas próprias

Verificação: Conferir as listas para ambos os tipos e procurar ações de criar, renomear ou excluir categoria.

Resultado esperado: Listas correspondem exatamente às categorias aprovadas e não permitem manutenção.

Origem no requisito: R3: Oferecer somente receitas: Salário, Freelance, Rendimentos, Outras receitas; despesas: Alimentação, Moradia, Transporte, Saúde, Educação, Lazer, Compras, Outras despesas. Sem manutenção de categorias.

#### CT-004 — R4 — Cadastro de receitas e despesas próprias

Verificação: Cadastrar como A e tentar escolher B como proprietário; sair e entrar como A para consultar; tentar cadastrar sem sessão e sem e-mail confirmado.

Resultado esperado: Registro pertence apenas a A e permanece persistido; proprietário alheio não é aceito e usuários não habilitados não operam.

Origem no requisito: R4: Vincular cadastro ao usuário autenticado com e-mail confirmado, sem aceitar outro proprietário; persistência permanece após sair e entrar.

#### CT-005 — R5 — Vigência das movimentações por data

Verificação: Criar transação de amanhã; observar antes e depois da meia-noite de Brasília, inclusive quando UTC já está no dia seguinte.

Resultado esperado: Antes fica agendada e fora dos valores; na data deixa de ser agendada e entra automaticamente, sem pagamento externo.

Origem no requisito: R5: Data define competência em America/Sao_Paulo; futura é agendada, aparece no histórico e não afeta saldo/totais até início da data. Inclusão automática, sem confirmação manual nem pagamento externo.

#### CT-006 — R6 — Vigência das movimentações por data

Verificação: Preparar receitas/despesas passadas, atuais, futuras e excluídas em dois meses; calcular saldo e totais, selecionar mês futuro e um conjunto negativo.

Resultado esperado: Valores exatos em centavos seguem o conjunto aprovado, excluem futuras/excluídas e permitem saldo negativo sem saldo inicial.

Origem no requisito: R6: Saldo é receitas menos despesas de registros não excluídos até hoje; totais mensais usam data dentro do mês e até hoje. Mês futuro não realiza movimentações; saldo negativo permitido, sem saldo inicial separado.

#### CT-007 — R7 — Edição de movimentações próprias

Verificação: Editar cada campo de uma transação própria passada e futura; realizar ambas as transições de data e alterar tipo/valor.

Resultado esperado: Atualiza o mesmo registro e recalcula os efeitos sem duplicar nem manter contribuição anterior indevida.

Origem no requisito: R7: Editar todos os campos próprios em qualquer data; tipo, valor, categoria e data atualizam valores aplicáveis. Passada/hoje para futura retira efeito; futura para hoje/passada inclui.

#### CT-008 — R8 — Exclusão confirmada de movimentações

Verificação: Solicitar exclusão de registro próprio e confirmar; consultar histórico e valores.

Resultado esperado: Registro deixa de aparecer e de contribuir; não há ação de desfazer.

Origem no requisito: R8: Excluir somente após confirmação, removendo do histórico e cálculos, sem desfazer.

#### CT-009 — R9 — Busca e filtros do histórico

Verificação: Usar mais de 50 registros e descrições acentuadas; buscar trecho com caixa/acentos diferentes, combinar filtros, navegar, mudar filtro e limpar.

Resultado esperado: Resultados próprios respeitam combinações e ordem; páginas têm até 50, mantêm filtros, alteração retorna à primeira e limpeza retorna ao histórico integral.

Origem no requisito: R9: Busca por trecho sem distinguir caixa/acentos; período, tipo e categoria combinados no mesmo conjunto; limpar filtros mostra todo histórico. Ordenar data decrescente e cadastro mais recente em empate; páginas de 50, filtros mantidos, mudança retorna à primeira.

#### CT-010 — R10-campos — Histórico e detalhes próprios

Verificação: Abrir histórico e detalhes de receitas/despesas próprias.

Resultado esperado: Todos os campos aparecem com valores e datas legíveis nos formatos aprovados.

Origem no requisito: R10-campos: R10 e dados percebidos: histórico/detalhes mostram descrição, tipo, valor em reais com centavos, categoria e data brasileira.

#### CT-011 — R10-agendada — Vigência das movimentações por data

Verificação: Consultar histórico misturando datas futuras, atuais e passadas e atravessar a data prevista.

Resultado esperado: Futuras se integram à ordem cronológica e deixam de ser agendadas na data, sem fila separada.

Origem no requisito: R10-agendada: R10: futuras mostram identificação de agendada, seguem ordenação por data sem fila separada; identificação cessa na data.

#### CT-012 — CA1 — Cadastro de receitas e despesas próprias

Verificação: Cadastrar cada tipo, sair e entrar novamente e conferir registros.

Resultado esperado: Registros próprios persistem e sucesso corresponde à gravação concluída.

Origem no requisito: CA1: Salvar receita/despesa válida cria um registro próprio, mostra sucesso e mantém dados após novo acesso.

#### CT-013 — CA2 — Cadastro de receitas e despesas próprias

Verificação: Enviar formulário com cada classe de erro e corrigir sem redigitar campos válidos.

Resultado esperado: Não cria registro inválido; exibe erros e conserva dados para correção.

Origem no requisito: CA2: Ausências, categoria incompatível, valores/datas fora de R2 e descrição vazia/longa impedem salvar, mostram erros e preservam o formulário.

#### CT-014 — CA3 — Vigência das movimentações por data

Verificação: Cadastrar futura e consultar seu mês e os valores gerais.

Resultado esperado: Continua agendada e fora do saldo/totais.

Origem no requisito: CA3: Futura aparece agendada e não afeta saldo nem totais, mesmo na consulta de seu mês futuro.

#### CT-015 — CA4 — Vigência das movimentações por data

Verificação: Comparar consultas imediatamente antes e após início da data em Brasília sem confirmar recebimento/pagamento.

Resultado esperado: Passa automaticamente aos valores e perde indicação.

Origem no requisito: CA4: Ao chegar a data em America/Sao_Paulo, compõe valores de R6 sem confirmação e perde marcação de agendada.

#### CT-016 — CA5 — Busca e filtros do histórico

Verificação: Usar duas contas e períodos distintos; abrir consulta inicial, trocar mês/todos e combinar filtros.

Resultado esperado: Padrão mês atual; resultados somente da conta e correspondentes, com ordenação/paginação correta.

Origem no requisito: CA5: Histórico inicia no mês atual; escolher mês ou todo histórico e combinar descrição/tipo/categoria retorna apenas registros próprios com ordem/paginação de R9.

#### CT-017 — CA6-vazio — Histórico e detalhes próprios

Verificação: Abrir histórico de conta sem nenhuma movimentação.

Resultado esperado: Apresenta estado vazio e caminho para cadastrar.

Origem no requisito: CA6-vazio: CA6: histórico sem registros orienta primeiro cadastro.

#### CT-018 — CA6-busca — Busca e filtros do histórico

Verificação: Em conta com registros, aplicar busca sem correspondência e limpar filtros.

Resultado esperado: Informa ausência de correspondência e permite retomar todo histórico.

Origem no requisito: CA6-busca: CA6: busca sem resultados difere do histórico vazio e permite ajustar/limpar; limpar retorna histórico integral.

#### CT-019 — CA7-consulta — Histórico e detalhes próprios

Verificação: Como B, tentar abrir identificador de A; como A, abrir próprio registro e conferir campos.

Resultado esperado: A consulta própria funciona; a alheia informa indisponibilidade sem revelar dados.

Origem no requisito: CA7-consulta: CA7: abrir registro próprio mostra todos os campos; listas, busca e detalhes não revelam registros de outra pessoa, inclusive por identificador direto.

#### CT-020 — CA7-edicao — Edição de movimentações próprias

Verificação: Editar registro próprio e tentar alterar o de outra conta por acesso direto.

Resultado esperado: Somente proprietário habilitado altera; tentativa alheia não muda dados nem revela conteúdo.

Origem no requisito: CA7-edicao: CA7: detalhes próprios oferecem edição; outra conta não pode alterar por tela ou identificador direto.

#### CT-021 — CA7-exclusao — Exclusão confirmada de movimentações

Verificação: Solicitar exclusão própria e tentar excluir registro alheio.

Resultado esperado: Ação disponível ao titular; acesso alheio não remove nem revela dados.

Origem no requisito: CA7-exclusao: CA7: detalhes próprios oferecem exclusão; outra conta não pode excluir por tela ou identificador direto.

#### CT-022 — CA8 — Edição de movimentações próprias

Verificação: Conferir identidade e cálculos antes/depois de edição dos cinco campos e transições temporais.

Resultado esperado: Identidade permanece, histórico atualiza e valores seguem nova configuração.

Origem no requisito: CA8: Editar campo válido atualiza o mesmo registro e seus efeitos; mover passada para futura retira contribuição e inverso inclui.

#### CT-023 — CA9-cadastro — Cadastro de receitas e despesas próprias

Verificação: Preencher cadastro e cancelar.

Resultado esperado: Nenhum registro novo nem alteração financeira.

Origem no requisito: CA9-cadastro: CA9: cancelar cadastro não modifica registros nem totais.

#### CT-024 — CA9-edicao — Edição de movimentações próprias

Verificação: Alterar campos no formulário e cancelar.

Resultado esperado: Persistência e efeitos permanecem iguais aos anteriores.

Origem no requisito: CA9-edicao: CA9: cancelar edição conserva registro e totais anteriores.

#### CT-025 — CA9-exclusao — Exclusão confirmada de movimentações

Verificação: Cancelar uma confirmação e, em outra tentativa, confirmar.

Resultado esperado: Cancelamento não altera; confirmação remove somente o registro escolhido e seu efeito.

Origem no requisito: CA9-exclusao: CA9: cancelar exclusão mantém dados/totais; confirmar remove do histórico/cálculos sem desfazer.

#### CT-026 — CA10-cadastro — Cadastro de receitas e despesas próprias

Verificação: Provocar falha controlada de persistência no cadastro e tentar novamente após restauração.

Resultado esperado: Sem gravação parcial ou falso sucesso; usuário recebe orientação de tentar novamente.

Origem no requisito: CA10-cadastro: CA10: falha ao cadastrar não grava parcialmente nem mostra sucesso; orienta nova tentativa.

#### CT-027 — CA10-edicao — Edição de movimentações próprias

Verificação: Provocar falha em edição e editar identificador removido/indisponível.

Resultado esperado: Sem alteração parcial, falso sucesso ou dados alheios; informa indisponibilidade ou nova tentativa conforme caso.

Origem no requisito: CA10-edicao: CA10: falha ao editar não altera parcialmente nem mostra sucesso; registro removido/indisponível não pode ser alterado e não revela dados de terceiros.

#### CT-028 — CA10-consulta — Histórico e detalhes próprios

Verificação: Abrir identificador inexistente ou removido.

Resultado esperado: Informa indisponibilidade sem dados de outra conta.

Origem no requisito: CA10-consulta: CA10: registro indisponível não revela dados de terceiros e a interface informa indisponibilidade.

#### CT-029 — CA12-cadastro — Cadastro de receitas e despesas próprias

Verificação: Cadastrar duas vezes em operações distintas com mesmo tipo/valor/descrição/categoria/data.

Resultado esperado: Cria dois registros independentes.

Origem no requisito: CA12-cadastro: CA12: duas operações distintas com dados iguais podem criar duas transações, sem deduplicação automática.

#### CT-030 — CA12-edicao — Edição de movimentações próprias

Verificação: Editar só um dos dois registros iguais.

Resultado esperado: Somente o escolhido muda.

Origem no requisito: CA12-edicao: CA12: registros com dados iguais possuem edição independente.

#### CT-031 — CA12-exclusao — Exclusão confirmada de movimentações

Verificação: Excluir um dos registros iguais, repetir a mesma confirmação e consultar o outro e os valores.

Resultado esperado: Outro registro permanece; segunda exclusão não altera novamente totais.

Origem no requisito: CA12-exclusao: CA12: exclusão de registros iguais é independente; repetir exclusão de registro removido não produz novo efeito nos totais.

#### CT-032 — CA11 — Cadastro de receitas e despesas próprias

Verificação: Selecionar categoria, mudar tipo e tentar salvar com categoria anterior incompatível.

Resultado esperado: Exige seleção compatível e não grava combinação inválida.

Origem no requisito: CA11: Categorias disponíveis correspondem exatamente a R3; trocar tipo não mantém categoria incompatível silenciosamente nem permite concluir com ela.

#### CT-033 — F-edicao-validacao — Edição de movimentações próprias

Verificação: Editar com cada campo ausente, valor inválido/precisão maior, descrição fora do limite, data inválida e tipo/categoria incompatíveis.

Resultado esperado: Recusa, conserva dados para correção e preserva registro anterior.

Origem no requisito: F-edicao-validacao: Fluxos alternativos: edição inválida preserva formulário, mostra erros e não altera dados; limites R1–R3 e troca de tipo/categoria aplicam-se também à edição.

#### CT-034 — F-exclusao-falha — Exclusão confirmada de movimentações

Verificação: Provocar falha controlada ao confirmar exclusão e consultar dados/valores.

Resultado esperado: Registro e efeito permanecem coerentes, sem falso sucesso; orienta nova tentativa.

Origem no requisito: F-exclusao-falha: Fluxos alternativos: falha ao persistir exclusão não apresenta sucesso nem aplica alteração parcial; orienta nova tentativa.


## Descrições completas

### 1. [DEV] [WEB] [USUARIO] Gestão de transações - Cadastro de receitas e despesas próprias

#### Entrega

Criar o cadastro de movimentações próprias com persistência, categorias predefinidas e validações. A autenticação e a confirmação de e-mail existentes devem ser preservadas.

#### Escopo e limites

Inclui o formulário e seu resultado de sucesso. Consulta do registro fica em ‘Gestão de transações - Histórico e detalhes próprios’; classificação de agendada e cálculos ficam em ‘Gestão de transações - Vigência das movimentações por data’.

#### Critérios de aceite

- Tipo receita/despesa, valor positivo em reais, descrição, categoria e data são obrigatórios; tipo determina entrada ou saída.
- Valor entre R$ 0,01 e R$ 999.999.999,99 com até duas casas; não arredondar entrada com precisão maior. Descrição entre 1 e 120 caracteres após aparar extremidades. Data válida de 01/01/1900 a 31/12/9999.
- Oferecer somente receitas: Salário, Freelance, Rendimentos, Outras receitas; despesas: Alimentação, Moradia, Transporte, Saúde, Educação, Lazer, Compras, Outras despesas. Sem manutenção de categorias.
- Vincular cadastro ao usuário autenticado com e-mail confirmado, sem aceitar outro proprietário; persistência permanece após sair e entrar.
- Salvar receita/despesa válida cria um registro próprio, mostra sucesso e mantém dados após novo acesso.
- Ausências, categoria incompatível, valores/datas fora de R2 e descrição vazia/longa impedem salvar, mostram erros e preservam o formulário.
- CA9: cancelar cadastro não modifica registros nem totais.
- CA10: falha ao cadastrar não grava parcialmente nem mostra sucesso; orienta nova tentativa.
- CA12: duas operações distintas com dados iguais podem criar duas transações, sem deduplicação automática.
- Categorias disponíveis correspondem exatamente a R3; trocar tipo não mantém categoria incompatível silenciosamente nem permite concluir com ela.

#### Dependências

Pode iniciar com a autenticação existente. A jornada completa de consulta integra ‘Gestão de transações - Histórico e detalhes próprios’.

#### Referências

Item pai Redmine `#1015911`; regras/critérios R1, R2, R3, R4, CA1, CA2, CA9-cadastro, CA10-cadastro, CA12-cadastro, CA11.

### 2. [DEV] [WEB] [USUARIO] Gestão de transações - Histórico e detalhes próprios

#### Entrega

Criar a consulta das movimentações e de seus detalhes, limitada à conta autenticada, com campos legíveis e estado vazio.

#### Escopo e limites

Busca, período, filtros e paginação ficam em ‘Gestão de transações - Busca e filtros do histórico’. As ações de editar e excluir integram as respectivas entregas.

#### Critérios de aceite

- R10 e dados percebidos: histórico/detalhes mostram descrição, tipo, valor em reais com centavos, categoria e data brasileira.
- CA6: histórico sem registros orienta primeiro cadastro.
- CA7: abrir registro próprio mostra todos os campos; listas, busca e detalhes não revelam registros de outra pessoa, inclusive por identificador direto.
- CA10: registro indisponível não revela dados de terceiros e a interface informa indisponibilidade.

#### Dependências

Depende de ‘Gestão de transações - Cadastro de receitas e despesas próprias’, que fornece registros persistidos. Para a jornada completa, integrar ‘Gestão de transações - Edição de movimentações próprias’ e ‘Gestão de transações - Exclusão confirmada de movimentações’.

#### Referências

Item pai Redmine `#1015911`; regras/critérios R10-campos, CA6-vazio, CA7-consulta, CA10-consulta.

### 3. [DEV] [WEB] [USUARIO] Gestão de transações - Busca e filtros do histórico

#### Entrega

Permitir localizar movimentações por período, descrição, tipo e categoria, com contagem, ordenação e paginação consistentes.

#### Escopo e limites

Opera sobre o histórico próprio; não cria consultas de outros usuários nem relatórios avançados.

#### Critérios de aceite

- Busca por trecho sem distinguir caixa/acentos; período, tipo e categoria combinados no mesmo conjunto; limpar filtros mostra todo histórico. Ordenar data decrescente e cadastro mais recente em empate; páginas de 50, filtros mantidos, mudança retorna à primeira.
- Histórico inicia no mês atual; escolher mês ou todo histórico e combinar descrição/tipo/categoria retorna apenas registros próprios com ordem/paginação de R9.
- CA6: busca sem resultados difere do histórico vazio e permite ajustar/limpar; limpar retorna histórico integral.

#### Dependências

Depende de ‘Gestão de transações - Histórico e detalhes próprios’, que fornece a consulta navegável.

#### Referências

Item pai Redmine `#1015911`; regras/critérios R9, CA5, CA6-busca.

### 4. [DEV] [WEB] [USUARIO] Gestão de transações - Vigência das movimentações por data

#### Entrega

Identificar movimentações futuras como agendadas e aplicar automaticamente sua competência financeira quando chegar a data em Brasília.

#### Escopo e limites

Entrega a indicação no histórico e as regras de saldo e totais previstas no requisito. Telas do dashboard e conversa com IA pertencem às Features seguintes; não cria API consumível nem executa pagamentos.

#### Critérios de aceite

- Data define competência em America/Sao_Paulo; futura é agendada, aparece no histórico e não afeta saldo/totais até início da data. Inclusão automática, sem confirmação manual nem pagamento externo.
- Saldo é receitas menos despesas de registros não excluídos até hoje; totais mensais usam data dentro do mês e até hoje. Mês futuro não realiza movimentações; saldo negativo permitido, sem saldo inicial separado.
- R10: futuras mostram identificação de agendada, seguem ordenação por data sem fila separada; identificação cessa na data.
- Futura aparece agendada e não afeta saldo nem totais, mesmo na consulta de seu mês futuro.
- Ao chegar a data em America/Sao_Paulo, compõe valores de R6 sem confirmação e perde marcação de agendada.

#### Dependências

Depende de ‘Gestão de transações - Histórico e detalhes próprios’. Os efeitos após alterações integram ‘Gestão de transações - Edição de movimentações próprias’ e ‘Gestão de transações - Exclusão confirmada de movimentações’.

#### Referências

Item pai Redmine `#1015911`; regras/critérios R5, R6, R10-agendada, CA3, CA4.

### 5. [DEV] [WEB] [USUARIO] Gestão de transações - Edição de movimentações próprias

#### Entrega

Permitir corrigir todos os campos de uma movimentação própria sem mudar sua identidade, refletindo a alteração no histórico e nos valores aplicáveis.

#### Escopo e limites

Reutiliza limites e categorias do cadastro; não cria uma segunda movimentação ao editar.

#### Critérios de aceite

- Editar todos os campos próprios em qualquer data; tipo, valor, categoria e data atualizam valores aplicáveis. Passada/hoje para futura retira efeito; futura para hoje/passada inclui.
- CA7: detalhes próprios oferecem edição; outra conta não pode alterar por tela ou identificador direto.
- Editar campo válido atualiza o mesmo registro e seus efeitos; mover passada para futura retira contribuição e inverso inclui.
- CA9: cancelar edição conserva registro e totais anteriores.
- CA10: falha ao editar não altera parcialmente nem mostra sucesso; registro removido/indisponível não pode ser alterado e não revela dados de terceiros.
- CA12: registros com dados iguais possuem edição independente.
- Fluxos alternativos: edição inválida preserva formulário, mostra erros e não altera dados; limites R1–R3 e troca de tipo/categoria aplicam-se também à edição.

#### Dependências

Depende de ‘Gestão de transações - Histórico e detalhes próprios’. Pode iniciar com os registros existentes; para concluir os efeitos financeiros, integrar ‘Gestão de transações - Vigência das movimentações por data’.

#### Referências

Item pai Redmine `#1015911`; regras/critérios R7, CA7-edicao, CA8, CA9-edicao, CA10-edicao, CA12-edicao, F-edicao-validacao.

### 6. [DEV] [WEB] [USUARIO] Gestão de transações - Exclusão confirmada de movimentações

#### Entrega

Permitir excluir movimentação própria após confirmação, removendo seu efeito uma única vez e permitindo cancelar antes da exclusão.

#### Escopo e limites

Não oferece desfazer nem altera outras movimentações, mesmo quando seus dados são iguais.

#### Critérios de aceite

- Excluir somente após confirmação, removendo do histórico e cálculos, sem desfazer.
- CA7: detalhes próprios oferecem exclusão; outra conta não pode excluir por tela ou identificador direto.
- CA9: cancelar exclusão mantém dados/totais; confirmar remove do histórico/cálculos sem desfazer.
- CA12: exclusão de registros iguais é independente; repetir exclusão de registro removido não produz novo efeito nos totais.
- Fluxos alternativos: falha ao persistir exclusão não apresenta sucesso nem aplica alteração parcial; orienta nova tentativa.

#### Dependências

Depende de ‘Gestão de transações - Histórico e detalhes próprios’. Para concluir os efeitos financeiros, integrar ‘Gestão de transações - Vigência das movimentações por data’.

#### Referências

Item pai Redmine `#1015911`; regras/critérios R8, CA7-exclusao, CA9-exclusao, CA12-exclusao, F-exclusao-falha.

## Publicação proposta — revisão 1

Criar seis DEV e uma QA, conforme as descrições integrais desta prévia. Não foram encontradas filhas existentes em busca com status abertos e fechados.

| Campo | DEV | QA |
| --- | --- | --- |
| Projeto / mãe | FinAi 65224 / Feature 1015911 | FinAi 65224 / Feature 1015911 |
| Tracker | Task (4) | Deliverable (5) |
| Status / prioridade | New (1) / Normal (4) | New (1) / Normal (4) |
| Versão | Sprint 1 (20355) | Sprint 1 (20355) |
| Categoria | Sem categoria | Sem categoria |
| Responsável / início / vencimento | Vazios | Vazios |
| Horas | 6; 4,5; 5; 4,5; 4; 3 | 6 |

### Relações propostas

- **[DEV] [WEB] [USUARIO] Gestão de transações - Cadastro de receitas e despesas próprias** bloqueia **[QA] [WEB] [USUARIO] Gestão de transações**.
- **[DEV] [WEB] [USUARIO] Gestão de transações - Cadastro de receitas e despesas próprias** bloqueia **[DEV] [WEB] [USUARIO] Gestão de transações - Histórico e detalhes próprios**.
- **[DEV] [WEB] [USUARIO] Gestão de transações - Histórico e detalhes próprios** bloqueia **[QA] [WEB] [USUARIO] Gestão de transações**.
- **[DEV] [WEB] [USUARIO] Gestão de transações - Histórico e detalhes próprios** bloqueia **[DEV] [WEB] [USUARIO] Gestão de transações - Busca e filtros do histórico**.
- **[DEV] [WEB] [USUARIO] Gestão de transações - Busca e filtros do histórico** bloqueia **[QA] [WEB] [USUARIO] Gestão de transações**.
- **[DEV] [WEB] [USUARIO] Gestão de transações - Histórico e detalhes próprios** bloqueia **[DEV] [WEB] [USUARIO] Gestão de transações - Vigência das movimentações por data**.
- **[DEV] [WEB] [USUARIO] Gestão de transações - Vigência das movimentações por data** bloqueia **[QA] [WEB] [USUARIO] Gestão de transações**.
- **[DEV] [WEB] [USUARIO] Gestão de transações - Histórico e detalhes próprios** bloqueia **[DEV] [WEB] [USUARIO] Gestão de transações - Edição de movimentações próprias**.
- **[DEV] [WEB] [USUARIO] Gestão de transações - Edição de movimentações próprias** bloqueia **[QA] [WEB] [USUARIO] Gestão de transações**.
- **[DEV] [WEB] [USUARIO] Gestão de transações - Histórico e detalhes próprios** bloqueia **[DEV] [WEB] [USUARIO] Gestão de transações - Exclusão confirmada de movimentações**.
- **[DEV] [WEB] [USUARIO] Gestão de transações - Exclusão confirmada de movimentações** bloqueia **[QA] [WEB] [USUARIO] Gestão de transações**.

Não há bloqueios externos de filhas. Autenticação e verificação de e-mail já existem. Preservar as relações atuais entre as Features e o status New da mãe. Integração com vigência é necessária para concluir efeitos da edição/exclusão, sem bloquear seu início.

### Documento de teste

DOCX obrigatório: `slices/condicoes-teste-r001.docx`, gerado após aprovação da fonte de 34 condições CT-001 a CT-034 e anexado à nova QA. Markdown complementar em `slices/condicoes-teste-r001.md`. Fonte: proposta `85887de6a7037e9056e83207c7f54b30486c239eb55c4ed6cb024a51d0faa889`. O tamanho e hash binário serão conferidos na preparação antes do upload; mudança material exige nova prévia.

### Estimativas e cobertura

Total DEV: **27h**. QA: **6h**. Total: **33h**. Dois avaliadores independentes estimaram o trabalho sem usar estimativas herdadas. A primeira avaliação reuniu cadastro e histórico básico em6h; a segunda identificou risco de exceder o teto ao incluir consulta/detalhes e propôs separá-los. A decomposição escolhida separa cadastro e consulta e mantém todas as tarefas em até6h. QA pressupõe massa pronta, duas contas, datas e falhas controláveis.

A tabela de cobertura contempla R1–R10, CA1–CA12 e exceções. Subdivisões por operação evitam atribuir uma regra a duas entregas. A inspeção não encontrou capacidades financeiras, apenas acesso e componentes reutilizáveis. Nenhum teste financeiro foi executado. Banco efetivo SQLite e timezone geral UTC foram conferidos; a competência deve seguir America/Sao_Paulo e a busca deve ignorar acentos. Não há ampliação de escopo, API consumível ou Study.

### 7. [QA] [WEB] [USUARIO] Gestão de transações

Estimativa: **6h**. Bloqueada por todas as seis DEV.

#### Objetivo

Verificar o ciclo completo de transações próprias, incluindo cadastro, consulta, datas agendadas, correção e exclusão.

#### Jornadas integradas

- Cadastrar separadamente receita e despesa válidas e omitir cada campo obrigatório. Resultado esperado: Dados válidos salvam; ausência de qualquer campo impede salvar com erro.
- Testar limites monetários, zero/negativo/acima do máximo e três casas; descrição vazia, espaços, 1,120,121 caracteres; datas limites, fora delas e inválidas. Resultado esperado: Limites inclusivos válidos são aceitos; demais entradas são recusadas sem arredondamento silencioso e com formulário preservado.
- Conferir as listas para ambos os tipos e procurar ações de criar, renomear ou excluir categoria. Resultado esperado: Listas correspondem exatamente às categorias aprovadas e não permitem manutenção.
- Cadastrar como A e tentar escolher B como proprietário; sair e entrar como A para consultar; tentar cadastrar sem sessão e sem e-mail confirmado. Resultado esperado: Registro pertence apenas a A e permanece persistido; proprietário alheio não é aceito e usuários não habilitados não operam.
- Criar transação de amanhã; observar antes e depois da meia-noite de Brasília, inclusive quando UTC já está no dia seguinte. Resultado esperado: Antes fica agendada e fora dos valores; na data deixa de ser agendada e entra automaticamente, sem pagamento externo.
- Preparar receitas/despesas passadas, atuais, futuras e excluídas em dois meses; calcular saldo e totais, selecionar mês futuro e um conjunto negativo. Resultado esperado: Valores exatos em centavos seguem o conjunto aprovado, excluem futuras/excluídas e permitem saldo negativo sem saldo inicial.
- Editar cada campo de uma transação própria passada e futura; realizar ambas as transições de data e alterar tipo/valor. Resultado esperado: Atualiza o mesmo registro e recalcula os efeitos sem duplicar nem manter contribuição anterior indevida.
- Solicitar exclusão de registro próprio e confirmar; consultar histórico e valores. Resultado esperado: Registro deixa de aparecer e de contribuir; não há ação de desfazer.
- Usar mais de 50 registros e descrições acentuadas; buscar trecho com caixa/acentos diferentes, combinar filtros, navegar, mudar filtro e limpar. Resultado esperado: Resultados próprios respeitam combinações e ordem; páginas têm até 50, mantêm filtros, alteração retorna à primeira e limpeza retorna ao histórico integral.
- Abrir histórico e detalhes de receitas/despesas próprias. Resultado esperado: Todos os campos aparecem com valores e datas legíveis nos formatos aprovados.
- Consultar histórico misturando datas futuras, atuais e passadas e atravessar a data prevista. Resultado esperado: Futuras se integram à ordem cronológica e deixam de ser agendadas na data, sem fila separada.
- Cadastrar cada tipo, sair e entrar novamente e conferir registros. Resultado esperado: Registros próprios persistem e sucesso corresponde à gravação concluída.
- Enviar formulário com cada classe de erro e corrigir sem redigitar campos válidos. Resultado esperado: Não cria registro inválido; exibe erros e conserva dados para correção.
- Cadastrar futura e consultar seu mês e os valores gerais. Resultado esperado: Continua agendada e fora do saldo/totais.
- Comparar consultas imediatamente antes e após início da data em Brasília sem confirmar recebimento/pagamento. Resultado esperado: Passa automaticamente aos valores e perde indicação.
- Usar duas contas e períodos distintos; abrir consulta inicial, trocar mês/todos e combinar filtros. Resultado esperado: Padrão mês atual; resultados somente da conta e correspondentes, com ordenação/paginação correta.
- Abrir histórico de conta sem nenhuma movimentação. Resultado esperado: Apresenta estado vazio e caminho para cadastrar.
- Em conta com registros, aplicar busca sem correspondência e limpar filtros. Resultado esperado: Informa ausência de correspondência e permite retomar todo histórico.
- Como B, tentar abrir identificador de A; como A, abrir próprio registro e conferir campos. Resultado esperado: A consulta própria funciona; a alheia informa indisponibilidade sem revelar dados.
- Editar registro próprio e tentar alterar o de outra conta por acesso direto. Resultado esperado: Somente proprietário habilitado altera; tentativa alheia não muda dados nem revela conteúdo.
- Solicitar exclusão própria e tentar excluir registro alheio. Resultado esperado: Ação disponível ao titular; acesso alheio não remove nem revela dados.
- Conferir identidade e cálculos antes/depois de edição dos cinco campos e transições temporais. Resultado esperado: Identidade permanece, histórico atualiza e valores seguem nova configuração.
- Preencher cadastro e cancelar. Resultado esperado: Nenhum registro novo nem alteração financeira.
- Alterar campos no formulário e cancelar. Resultado esperado: Persistência e efeitos permanecem iguais aos anteriores.
- Cancelar uma confirmação e, em outra tentativa, confirmar. Resultado esperado: Cancelamento não altera; confirmação remove somente o registro escolhido e seu efeito.
- Provocar falha controlada de persistência no cadastro e tentar novamente após restauração. Resultado esperado: Sem gravação parcial ou falso sucesso; usuário recebe orientação de tentar novamente.
- Provocar falha em edição e editar identificador removido/indisponível. Resultado esperado: Sem alteração parcial, falso sucesso ou dados alheios; informa indisponibilidade ou nova tentativa conforme caso.
- Abrir identificador inexistente ou removido. Resultado esperado: Informa indisponibilidade sem dados de outra conta.
- Cadastrar duas vezes em operações distintas com mesmo tipo/valor/descrição/categoria/data. Resultado esperado: Cria dois registros independentes.
- Editar só um dos dois registros iguais. Resultado esperado: Somente o escolhido muda.
- Excluir um dos registros iguais, repetir a mesma confirmação e consultar o outro e os valores. Resultado esperado: Outro registro permanece; segunda exclusão não altera novamente totais.
- Selecionar categoria, mudar tipo e tentar salvar com categoria anterior incompatível. Resultado esperado: Exige seleção compatível e não grava combinação inválida.
- Editar com cada campo ausente, valor inválido/precisão maior, descrição fora do limite, data inválida e tipo/categoria incompatíveis. Resultado esperado: Recusa, conserva dados para correção e preserva registro anterior.
- Provocar falha controlada ao confirmar exclusão e consultar dados/valores. Resultado esperado: Registro e efeito permanecem coerentes, sem falso sucesso; orienta nova tentativa.

#### Regras e permissões

- Tipo receita/despesa, valor positivo em reais, descrição, categoria e data são obrigatórios; tipo determina entrada ou saída.
- Valor entre R$ 0,01 e R$ 999.999.999,99 com até duas casas; não arredondar entrada com precisão maior. Descrição entre 1 e 120 caracteres após aparar extremidades. Data válida de 01/01/1900 a 31/12/9999.
- Oferecer somente receitas: Salário, Freelance, Rendimentos, Outras receitas; despesas: Alimentação, Moradia, Transporte, Saúde, Educação, Lazer, Compras, Outras despesas. Sem manutenção de categorias.
- Vincular cadastro ao usuário autenticado com e-mail confirmado, sem aceitar outro proprietário; persistência permanece após sair e entrar.
- Data define competência em America/Sao_Paulo; futura é agendada, aparece no histórico e não afeta saldo/totais até início da data. Inclusão automática, sem confirmação manual nem pagamento externo.
- Saldo é receitas menos despesas de registros não excluídos até hoje; totais mensais usam data dentro do mês e até hoje. Mês futuro não realiza movimentações; saldo negativo permitido, sem saldo inicial separado.
- Editar todos os campos próprios em qualquer data; tipo, valor, categoria e data atualizam valores aplicáveis. Passada/hoje para futura retira efeito; futura para hoje/passada inclui.
- Excluir somente após confirmação, removendo do histórico e cálculos, sem desfazer.
- Busca por trecho sem distinguir caixa/acentos; período, tipo e categoria combinados no mesmo conjunto; limpar filtros mostra todo histórico. Ordenar data decrescente e cadastro mais recente em empate; páginas de 50, filtros mantidos, mudança retorna à primeira.
- R10 e dados percebidos: histórico/detalhes mostram descrição, tipo, valor em reais com centavos, categoria e data brasileira.
- R10: futuras mostram identificação de agendada, seguem ordenação por data sem fila separada; identificação cessa na data.

#### Impactos relacionados

- Preservar autenticação e e-mail confirmado em todos os caminhos; usar duas contas para verificar que nenhuma consulta ou mutação revela ou opera registros alheios.
- Verificar efeitos financeiros após cadastro, passagem de data, edição e exclusão com a mesma regra de competência; telas do dashboard e chat não integram esta QA.
- Verificar independência de movimentações com dados iguais e inexistência de novo efeito ao repetir exclusão já concluída.

#### Critérios de conclusão

- Executar CT-001 a CT-034 do documento de condições desta revisão, registrando contexto, resultado observado e evidência de cada cenário.
- Conferir os limites exatos de valor, descrição e data, categorias por tipo, isolamento, busca sem acentos, ordem/paginação e cálculos por data de Brasília.
- Registrar desvios reproduzíveis com esperado/observado e condições impedidas; falta de massa, controle de data ou falha reproduzível não equivale a aprovação.

#### Referências

Item pai Redmine #1015911; regras/critérios R1, R2, R3, R4, R5, R6, R7, R8, R9, R10-campos, R10-agendada, CA1, CA2, CA3, CA4, CA5, CA6-vazio, CA6-busca, CA7-consulta, CA7-edicao, CA7-exclusao, CA8, CA9-cadastro, CA9-edicao, CA9-exclusao, CA10-cadastro, CA10-edicao, CA10-consulta, CA12-cadastro, CA12-edicao, CA12-exclusao, CA11, F-edicao-validacao, F-exclusao-falha.

