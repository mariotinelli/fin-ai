# [DEV] [WEB] [USUARIO] Gestão de transações - Cadastro de receitas e despesas com conferência do registro

- Redmine: `#1016123`
- Tipo: `DEV`
- Tracker: Task (`4`)
- Item pai: `#1016105`
- Estimativa: `2h`

## Descrição

## Entrega

Criar a primeira capacidade financeira real: cadastrar Receita/Despesa com categorias predefinidas, salvar no sistema para o próprio titular e consultar os cinco campos do registro salvo. Integrar entrada de Transações, formulário, processamento, validações e conferência mínima, para que a entrega seja verificável sem o histórico completo.

## Escopo e limites

Responsável pela primeira persistência, categorias, regras e detalhes do registro. Histórico completo/filtros/paginação pertencem à outra entrega; edição/exclusão à manutenção. Não criar tarefa isolada por camada nem implementar dashboard/IA.

## Critérios de aceite

- Titular autenticado e confirmado abre Nova transação com Despesa e data local de hoje; tipo, valor, descrição, categoria e data são obrigatórios. Categorias Receita: Salário,Freelance,Rendimentos,Outras receitas; Despesa: Alimentação,Moradia,Transporte,Saúde,Educação,Lazer,Compras,Outras despesas.
- Aceitar reais maiores que zero até R$999.999.999,99, com até duas casas; descrição até120caracteres e não apenas espaços; data válida entre01/01/1900 e hoje no calendário local percebido pelo usuário. Recusar ausências, valores inválidos/zero/negativos/excessivos ou mais de duas casas, descrição inválida e data inválida/futura com erros, sem salvar.
- Ao alternar o tipo, apresentar somente suas categorias e não persistir categoria anterior incompatível ou item fora da lista. O formulário apresenta a classificação que será salva.
- Salvar cria uma transação do titular por envio concluído, indica processamento e impede novo envio pelo mesmo botão enquanto processa; após sucesso, fecha formulário e confirma. Detalhes permitem conferir tipo,valor,descrição,categoria e data reais salvos,com apresentação brasileira.
- Fechar/cancelar não salva; falha informa o problema sem sucesso fictício, conserva os dados digitados e permite tentar novamente. Transação permanece acessível à mesma conta após sair/voltar ou usar outro navegador.
- Visitante e conta não confirmada não usam a operação; outro titular não lê o detalhe nem cria registro em conta alheia por acesso direto ou parâmetros. O proprietário não é selecionável pelo usuário.
- Nas novas superfícies, preservar a composição aplicável do design e consumir a identidade FinAI fornecida, em computador/tablet/celular, claro/escuro/sistema, sem reconstruir marca, temas ou navegação compartilhada.

## Dependências

Início bloqueado por [QA] [WEB] [USUARIO] Adequação visual do FinAI (#1016117), marco da fundação visual implementada/verificada. Reutilizar a autenticação e auth+verified já existentes; integrar com a Feature Acesso à conta pessoal no aceite final sem refazer suas correções. Fornece registros e detalhes para Histórico, filtros e paginação e Edição e exclusão confirmada.

## Referências

Item pai Redmine #1016105; regras/critérios R1, R2, R3, R4, R8, R9, CA1, CA2, CA3, CA4, CA8, CA10, CA11, CA12.

- design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; #transaction-dialog,#detail-dialog,#new-transaction; campos,cats,categoryOptions,fieldError e aparência dos diálogos
- Adaptações aprovadas: persistência no sistema e por titular, somente datas até hoje, categorias do design mantidas e variante escura da base visual.

<!-- project-slices-child:7c695bc9365c6fb2eb16b3430f06194e780bf35c092218dfe38ad8dcaaa8aae5 -->

## Relações

- `#1016123` blocks `#1016124`
- `#1016123` blocks `#1016125`
- `#1016123` blocks `#1016126`
