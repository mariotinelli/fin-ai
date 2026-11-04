# Revisão de Assistente financeiro com IA

Projeto FinAi #65224; Sprint 1 #20355; Feature #2; estado inicial New #1; sem categoria; Sequencing #2 = 4 (baseline 0 + posição 4). Sem demanda semelhante na versão.

Operações: criar com requisito integral; atualizar descrição e versão acrescentando caminho canônico com ID retornado, preservando status e texto humano externo; criar relação blocks de #1015911 (Gestão de transações) para {{created_issue_id}} (Assistente financeiro com IA), reconciliando se já existir. Sem outras relações ou alterações de status.

## Requisito completo

# [WEB] [USUARIO] Assistente financeiro com IA

## Objetivo

Permitir ao usuário registrar receitas e despesas e consultar suas finanças por linguagem natural, com IA real, confirmação explícita antes de gravar e respostas fundamentadas exclusivamente nos registros da própria conta.

## Resultado esperado

O usuário conversa, complementa dados faltantes, revisa uma proposta e confirma um único registro. Consulta saldo, totais e listas reais, incluindo agendadas quando solicitadas. Mensagens e registro em preparação são preservados ao sair e voltar.

## Atores e permissões

Somente o usuário autenticado com e-mail confirmado acessa sua conversa, propostas e dados financeiros. Pedidos no chat não alteram o proprietário de uma transação, dispensam confirmação ou permitem consultar outra conta. O assistente não executa pagamentos nem operações bancárias.

## Histórias de usuário

1. Como usuário, quero descrever uma receita ou despesa para preparar seu registro.
2. Como usuário, quero complementar ou corrigir os dados e confirmar antes de gravar.
3. Como usuário, quero cancelar uma proposta sem criar transação.
4. Como usuário, quero consultar números e movimentações reais com períodos e filtros claros.
5. Como usuário, quero retomar minha conversa e proposta pendente depois de sair.
6. Como usuário, quero consultar dados enquanto preparo um registro, sem perder a proposta.

## Fluxo principal

1. Abrir a conversa contínua da própria conta; na primeira utilização, mostrar orientação sobre registro confirmado e consultas disponíveis.
2. Enviar uma mensagem sobre uma movimentação. A IA identifica tipo, valor, descrição, categoria e data; solicita os dados faltantes ou ambíguos.
3. Sem data informada, propor hoje em America/Sao_Paulo. Fixar datas relativas na data concreta interpretada, exibindo-a para revisão.
4. Com os cinco campos completos e válidos, apresentar proposta com Confirmar, Corrigir e Cancelar.
5. Corrigir permite revisar todos os campos em formulário; salvar a correção atualiza a proposta e exige nova confirmação, sem criar a transação.
6. Confirmar grava a versão atual da proposta uma única vez. Mostrar sucesso somente após persistência confirmada. O registro aparece no histórico e compõe o dashboard conforme sua data; se futuro, informar que está agendado.
7. Cancelar descarta o registro em preparação sem gravar. A conversa mantém o resultado do cancelamento.
8. Para consultas, identificar intenção, período e filtros; consultar os dados atuais e apresentar resultado com esses critérios explícitos.
9. Ao sair e voltar, restaurar mensagens e eventual preparação incompleta ou proposta pendente. Nenhuma retomada confirma ou altera a data automaticamente.

## Fluxos alternativos e exceções

- Mensagem com várias movimentações pede envio de uma por vez. Não grava parcialmente nem escolhe silenciosamente uma delas.
- Tipo, valor, descrição ou data ambíguos exigem esclarecimento. Não inventar valores nem usar hoje para substituir uma data explicitamente informada, mas inválida.
- Inferir categoria somente entre as predefinidas e compatíveis com o tipo. Sem correspondência segura, pedir escolha; não criar categoria nem selecionar Outras silenciosamente.
- Sem campos válidos, não liberar confirmação. Confirmação escrita, como “sim”, orienta usar o botão da proposta atual e não grava.
- Versão corrigida invalida a confirmação de versões anteriores. Propostas canceladas ou já confirmadas não podem gravar novamente, inclusive após recarregar a página.
- Consultas são permitidas enquanto houver registro em preparação. Outro pedido de registro orienta confirmar ou cancelar o anterior; mensagem ambígua pede esclarecimento, sem sobrescrever a proposta.
- Falha de interpretação ou indisponibilidade da IA mostra aviso e permite nova tentativa ou cadastro manual, preservando a proposta já existente. A operação manual não confirma automaticamente a proposta do chat.
- Falha conhecida de gravação mantém a proposta para nova tentativa, sem anunciar sucesso. Se o resultado da gravação for incerto, conferir se ela ocorreu antes de repetir; não criar outra transação por uma repetição da confirmação.
- Consulta sem registros informa a ausência; consulta que falhou informa indisponibilidade, sem fabricar números nem substituir falha por zero.
- Pedidos de edição ou exclusão de transações já salvas orientam usar Gestão de transações. Cancelar uma proposta não exclui transações.
- Consultas fora das capacidades previstas pedem reformulação ou explicam o limite, sem inventar respostas financeiras.

## Regras de negócio

R1. IA real interpreta linguagem natural. Provedor, modelo e mecanismo de integração são decisões posteriores de implementação; uma simulação por regras não satisfaz esta entrega.

R2. Campos, limites e categorias são os mesmos de Gestão de transações #1015911: tipo receita/despesa, valor em reais entre R$ 0,01 e R$ 999.999.999,99 com até duas casas decimais, descrição de 1 a 120 caracteres após remover espaços nas extremidades, categoria compatível e data válida entre 01/01/1900 e 31/12/9999. Não arredondar silenciosamente precisão excedente.

R3. Receitas: Salário, Freelance, Rendimentos e Outras receitas. Despesas: Alimentação, Moradia, Transporte, Saúde, Educação, Lazer, Compras e Outras despesas. O usuário revisa a categoria inferida antes de confirmar.

R4. Há no máximo um registro em preparação por usuário. Ele pode estar incompleto ou pronto para confirmação. Mensagens e propostas não são transações e não entram nos cálculos antes de confirmação e persistência.

R5. Somente Confirmar na versão atual grava. Repetir a confirmação da mesma proposta produz no máximo uma transação; iniciar e confirmar uma nova proposta com dados iguais pode criar outro registro, conforme a regra de transações distintas.

R6. Uma conversa contínua é persistida por usuário. A proposta e dados já coletados são retomados sem gravação; uma data já fixada não muda porque o dia mudou. Mensagens antigas permanecem como histórico, não como prova de saldo atual. Nova consulta busca dados atuais, refletindo alterações e exclusões feitas na interface.

R7. Datas relativas usam America/Sao_Paulo. Sem data no registro, propor hoje. Quando uma expressão de data não puder ser determinada com segurança, perguntar. Futuras são permitidas e só afetam saldo e totais ao chegar sua data.

R8. Consultas disponíveis: saldo geral; totais de receitas e despesas por período e categoria; listagem por período, tipo e categoria; listagem de agendadas. Períodos reconhecidos incluem hoje, ontem, este mês, mês passado e datas ou intervalos explícitos, incluindo pedido expresso de todo o histórico.

R9. Consulta independente sem período usa este mês para totais e listas, declarando isso na resposta. Saldo geral sempre considera todo o histórico até hoje. Agendadas sem período considera todas as futuras. Continuação explícita de uma consulta pode reaproveitar seus filtros; se houver dúvida, esclarecer e apresentar os critérios efetivamente utilizados.

R10. Totais e saldo seguem Gestão de transações: somente registros próprios não excluídos até hoje. Intervalos incluem as datas inicial e final; intervalo invertido ou ambíguo pede correção. Listas comuns excluem agendadas, salvo pedido explícito para incluí-las ou consultá-las; quando incluídas, identificá-las separadamente e não somá-las aos valores já contabilizados.

R11. Proposta de apresentação das listas: até dez registros por resposta, por data decrescente e cadastro mais recente no desempate, com quantidade total encontrada e opção Ver mais. Ver mais mantém período e filtros e consulta dados reais; ao alterar os critérios, iniciar nova lista. Os totais solicitados correspondem a todos os registros elegíveis do filtro, não só à página exibida.

R12. Cada resposta financeira identifica período e filtros, distingue dados contabilizados de agendados e usa reais com centavos. Não inventa transações, categorias, valores ou resultado de uma gravação. Registrar uma futura não significa realizar o pagamento ou recebimento.

## Dados percebidos pelo usuário

Mensagens salvas, indicação de processamento e erro, perguntas de complementação, proposta com tipo/valor/descrição/categoria/data, botões Confirmar/Corrigir/Cancelar, estado pendente/confirmado/cancelado, confirmação de persistência, resultados com período e filtros, listas com indicação de agendamento e opção de continuidade.

## Critérios de aceite

CA1. “Gastei R$ 35 no almoço”, sem data, prepara despesa de R$ 35, descrição coerente, categoria sugerida e data de hoje em Brasília, permitindo revisão; não cria transação antes de Confirmar.

CA2. Dados ausentes ou interpretação ambígua geram pergunta de esclarecimento. Campo inválido ou categoria incompatível impede confirmação; nenhuma informação financeira é inventada para completar a proposta.

CA3. Mensagem com duas movimentações pede envio separado e não grava nenhuma parcialmente.

CA4. Corrigir altera a proposta, exige nova revisão e invalida confirmações antigas. Cancelar não cria transação; escrever “sim” não grava e orienta usar Confirmar.

CA5. Confirmar proposta válida cria um único registro próprio e mostra sucesso após persistência. Repetir a mesma confirmação, inclusive depois de voltar ao chat, não duplica.

CA6. Confirmar movimentação futura a registra como agendada; ela fica fora dos totais até sua data e entra automaticamente conforme as regras de Gestão de transações.

CA7. Sair e voltar restaura mensagens e preparação pendente ou incompleta; não grava, não perde os dados coletados e não troca a data fixada por um novo hoje.

CA8. Uma consulta durante preparação responde com dados reais sem perder a proposta. Pedido de outro registro orienta concluir ou cancelar o anterior; ambiguidade não sobrescreve dados.

CA9. Consultas retornam saldo, totais e listas conforme R8 a R12. Sem período, usam os padrões de R9; pedido explícito de outro período ou todo o histórico é respeitado e identificado.

CA10. Dados inexistentes produzem ausência de registros e zero quando o cálculo realmente for zero; falha de leitura produz indisponibilidade, nunca um resultado financeiro inventado.

CA11. Após editar ou excluir uma transação pela interface, uma nova consulta reflete o estado atual; respostas antigas continuam apenas como histórico.

CA12. Mais de dez registros permitem Ver mais com os mesmos filtros; a resposta informa a quantidade total e não apresenta uma página como se fosse toda a listagem. Totais usam o conjunto completo elegível.

CA13. Falha de gravação não anuncia sucesso; nova tentativa ou confirmação repetida não duplica uma gravação já efetivada. Falha da IA permite tentar novamente ou usar cadastro manual.

CA14. Usuário não consulta nem modifica conversa, proposta ou dados de outra conta, mesmo pedindo isso em linguagem natural. Pedido de editar/excluir transação salva orienta usar Gestão de transações.

## Dependências

Gestão de transações — #1015911 — fornece persistência, categorias, validações, isolamento e regras de cálculo. Acesso à conta está incluído por essa dependência. Os registros confirmados são os mesmos consumidos pelo Dashboard financeiro #1015912; não há dependência direta adicional no catálogo. Uma integração funcional com IA é necessária para atender R1.

## Designs e evidências

Catálogo, escopo inicial, respostas Q13 a Q20 e requisito aprovado de Gestão de transações. O design é exclusivamente visual; não autoriza assistente simulado nem armazenamento apenas no navegador. R11, correção em formulário e detalhes de falhas, ambiguidades e consulta são propostas explícitas nesta revisão. Modelos e provedores de IA não foram escolhidos no levantamento funcional.

## Dentro do escopo

Chat com IA real, conversa contínua salva, um registro em preparação, extração e complementação, revisão/correção/cancelamento, confirmação por botão, retomada, persistência sem duplicação da mesma proposta e consultas reais com os filtros e períodos definidos.

## Fora do escopo

Múltiplos agentes ou múltiplas conversas por usuário, lotes de transações, edição/exclusão de registros salvos pelo chat, gestão de categorias, pagamentos externos, bancos, importações, arquivos/áudio/imagens no chat, recorrência, análises avançadas e recomendações financeiras personalizadas. Não inclui gerenciamento de exclusão/edição de mensagens ou garantia de atualização automática de respostas históricas.


## Descrição exata na criação

<!-- project-flow:run 1a34fdd3-9440-446c-8725-76246ece59ff -->
<!-- project-flow:start -->
## Objetivo

Permitir ao usuário registrar receitas e despesas e consultar suas finanças por linguagem natural, com IA real, confirmação explícita antes de gravar e respostas fundamentadas exclusivamente nos registros da própria conta.

## Resultado esperado

O usuário conversa, complementa dados faltantes, revisa uma proposta e confirma um único registro. Consulta saldo, totais e listas reais, incluindo agendadas quando solicitadas. Mensagens e registro em preparação são preservados ao sair e voltar.

## Atores e permissões

Somente o usuário autenticado com e-mail confirmado acessa sua conversa, propostas e dados financeiros. Pedidos no chat não alteram o proprietário de uma transação, dispensam confirmação ou permitem consultar outra conta. O assistente não executa pagamentos nem operações bancárias.

## Histórias de usuário

1. Como usuário, quero descrever uma receita ou despesa para preparar seu registro.
2. Como usuário, quero complementar ou corrigir os dados e confirmar antes de gravar.
3. Como usuário, quero cancelar uma proposta sem criar transação.
4. Como usuário, quero consultar números e movimentações reais com períodos e filtros claros.
5. Como usuário, quero retomar minha conversa e proposta pendente depois de sair.
6. Como usuário, quero consultar dados enquanto preparo um registro, sem perder a proposta.

## Fluxo principal

1. Abrir a conversa contínua da própria conta; na primeira utilização, mostrar orientação sobre registro confirmado e consultas disponíveis.
2. Enviar uma mensagem sobre uma movimentação. A IA identifica tipo, valor, descrição, categoria e data; solicita os dados faltantes ou ambíguos.
3. Sem data informada, propor hoje em America/Sao_Paulo. Fixar datas relativas na data concreta interpretada, exibindo-a para revisão.
4. Com os cinco campos completos e válidos, apresentar proposta com Confirmar, Corrigir e Cancelar.
5. Corrigir permite revisar todos os campos em formulário; salvar a correção atualiza a proposta e exige nova confirmação, sem criar a transação.
6. Confirmar grava a versão atual da proposta uma única vez. Mostrar sucesso somente após persistência confirmada. O registro aparece no histórico e compõe o dashboard conforme sua data; se futuro, informar que está agendado.
7. Cancelar descarta o registro em preparação sem gravar. A conversa mantém o resultado do cancelamento.
8. Para consultas, identificar intenção, período e filtros; consultar os dados atuais e apresentar resultado com esses critérios explícitos.
9. Ao sair e voltar, restaurar mensagens e eventual preparação incompleta ou proposta pendente. Nenhuma retomada confirma ou altera a data automaticamente.

## Fluxos alternativos e exceções

- Mensagem com várias movimentações pede envio de uma por vez. Não grava parcialmente nem escolhe silenciosamente uma delas.
- Tipo, valor, descrição ou data ambíguos exigem esclarecimento. Não inventar valores nem usar hoje para substituir uma data explicitamente informada, mas inválida.
- Inferir categoria somente entre as predefinidas e compatíveis com o tipo. Sem correspondência segura, pedir escolha; não criar categoria nem selecionar Outras silenciosamente.
- Sem campos válidos, não liberar confirmação. Confirmação escrita, como “sim”, orienta usar o botão da proposta atual e não grava.
- Versão corrigida invalida a confirmação de versões anteriores. Propostas canceladas ou já confirmadas não podem gravar novamente, inclusive após recarregar a página.
- Consultas são permitidas enquanto houver registro em preparação. Outro pedido de registro orienta confirmar ou cancelar o anterior; mensagem ambígua pede esclarecimento, sem sobrescrever a proposta.
- Falha de interpretação ou indisponibilidade da IA mostra aviso e permite nova tentativa ou cadastro manual, preservando a proposta já existente. A operação manual não confirma automaticamente a proposta do chat.
- Falha conhecida de gravação mantém a proposta para nova tentativa, sem anunciar sucesso. Se o resultado da gravação for incerto, conferir se ela ocorreu antes de repetir; não criar outra transação por uma repetição da confirmação.
- Consulta sem registros informa a ausência; consulta que falhou informa indisponibilidade, sem fabricar números nem substituir falha por zero.
- Pedidos de edição ou exclusão de transações já salvas orientam usar Gestão de transações. Cancelar uma proposta não exclui transações.
- Consultas fora das capacidades previstas pedem reformulação ou explicam o limite, sem inventar respostas financeiras.

## Regras de negócio

R1. IA real interpreta linguagem natural. Provedor, modelo e mecanismo de integração são decisões posteriores de implementação; uma simulação por regras não satisfaz esta entrega.

R2. Campos, limites e categorias são os mesmos de Gestão de transações #1015911: tipo receita/despesa, valor em reais entre R$ 0,01 e R$ 999.999.999,99 com até duas casas decimais, descrição de 1 a 120 caracteres após remover espaços nas extremidades, categoria compatível e data válida entre 01/01/1900 e 31/12/9999. Não arredondar silenciosamente precisão excedente.

R3. Receitas: Salário, Freelance, Rendimentos e Outras receitas. Despesas: Alimentação, Moradia, Transporte, Saúde, Educação, Lazer, Compras e Outras despesas. O usuário revisa a categoria inferida antes de confirmar.

R4. Há no máximo um registro em preparação por usuário. Ele pode estar incompleto ou pronto para confirmação. Mensagens e propostas não são transações e não entram nos cálculos antes de confirmação e persistência.

R5. Somente Confirmar na versão atual grava. Repetir a confirmação da mesma proposta produz no máximo uma transação; iniciar e confirmar uma nova proposta com dados iguais pode criar outro registro, conforme a regra de transações distintas.

R6. Uma conversa contínua é persistida por usuário. A proposta e dados já coletados são retomados sem gravação; uma data já fixada não muda porque o dia mudou. Mensagens antigas permanecem como histórico, não como prova de saldo atual. Nova consulta busca dados atuais, refletindo alterações e exclusões feitas na interface.

R7. Datas relativas usam America/Sao_Paulo. Sem data no registro, propor hoje. Quando uma expressão de data não puder ser determinada com segurança, perguntar. Futuras são permitidas e só afetam saldo e totais ao chegar sua data.

R8. Consultas disponíveis: saldo geral; totais de receitas e despesas por período e categoria; listagem por período, tipo e categoria; listagem de agendadas. Períodos reconhecidos incluem hoje, ontem, este mês, mês passado e datas ou intervalos explícitos, incluindo pedido expresso de todo o histórico.

R9. Consulta independente sem período usa este mês para totais e listas, declarando isso na resposta. Saldo geral sempre considera todo o histórico até hoje. Agendadas sem período considera todas as futuras. Continuação explícita de uma consulta pode reaproveitar seus filtros; se houver dúvida, esclarecer e apresentar os critérios efetivamente utilizados.

R10. Totais e saldo seguem Gestão de transações: somente registros próprios não excluídos até hoje. Intervalos incluem as datas inicial e final; intervalo invertido ou ambíguo pede correção. Listas comuns excluem agendadas, salvo pedido explícito para incluí-las ou consultá-las; quando incluídas, identificá-las separadamente e não somá-las aos valores já contabilizados.

R11. Proposta de apresentação das listas: até dez registros por resposta, por data decrescente e cadastro mais recente no desempate, com quantidade total encontrada e opção Ver mais. Ver mais mantém período e filtros e consulta dados reais; ao alterar os critérios, iniciar nova lista. Os totais solicitados correspondem a todos os registros elegíveis do filtro, não só à página exibida.

R12. Cada resposta financeira identifica período e filtros, distingue dados contabilizados de agendados e usa reais com centavos. Não inventa transações, categorias, valores ou resultado de uma gravação. Registrar uma futura não significa realizar o pagamento ou recebimento.

## Dados percebidos pelo usuário

Mensagens salvas, indicação de processamento e erro, perguntas de complementação, proposta com tipo/valor/descrição/categoria/data, botões Confirmar/Corrigir/Cancelar, estado pendente/confirmado/cancelado, confirmação de persistência, resultados com período e filtros, listas com indicação de agendamento e opção de continuidade.

## Critérios de aceite

CA1. “Gastei R$ 35 no almoço”, sem data, prepara despesa de R$ 35, descrição coerente, categoria sugerida e data de hoje em Brasília, permitindo revisão; não cria transação antes de Confirmar.

CA2. Dados ausentes ou interpretação ambígua geram pergunta de esclarecimento. Campo inválido ou categoria incompatível impede confirmação; nenhuma informação financeira é inventada para completar a proposta.

CA3. Mensagem com duas movimentações pede envio separado e não grava nenhuma parcialmente.

CA4. Corrigir altera a proposta, exige nova revisão e invalida confirmações antigas. Cancelar não cria transação; escrever “sim” não grava e orienta usar Confirmar.

CA5. Confirmar proposta válida cria um único registro próprio e mostra sucesso após persistência. Repetir a mesma confirmação, inclusive depois de voltar ao chat, não duplica.

CA6. Confirmar movimentação futura a registra como agendada; ela fica fora dos totais até sua data e entra automaticamente conforme as regras de Gestão de transações.

CA7. Sair e voltar restaura mensagens e preparação pendente ou incompleta; não grava, não perde os dados coletados e não troca a data fixada por um novo hoje.

CA8. Uma consulta durante preparação responde com dados reais sem perder a proposta. Pedido de outro registro orienta concluir ou cancelar o anterior; ambiguidade não sobrescreve dados.

CA9. Consultas retornam saldo, totais e listas conforme R8 a R12. Sem período, usam os padrões de R9; pedido explícito de outro período ou todo o histórico é respeitado e identificado.

CA10. Dados inexistentes produzem ausência de registros e zero quando o cálculo realmente for zero; falha de leitura produz indisponibilidade, nunca um resultado financeiro inventado.

CA11. Após editar ou excluir uma transação pela interface, uma nova consulta reflete o estado atual; respostas antigas continuam apenas como histórico.

CA12. Mais de dez registros permitem Ver mais com os mesmos filtros; a resposta informa a quantidade total e não apresenta uma página como se fosse toda a listagem. Totais usam o conjunto completo elegível.

CA13. Falha de gravação não anuncia sucesso; nova tentativa ou confirmação repetida não duplica uma gravação já efetivada. Falha da IA permite tentar novamente ou usar cadastro manual.

CA14. Usuário não consulta nem modifica conversa, proposta ou dados de outra conta, mesmo pedindo isso em linguagem natural. Pedido de editar/excluir transação salva orienta usar Gestão de transações.

## Dependências

Gestão de transações — #1015911 — fornece persistência, categorias, validações, isolamento e regras de cálculo. Acesso à conta está incluído por essa dependência. Os registros confirmados são os mesmos consumidos pelo Dashboard financeiro #1015912; não há dependência direta adicional no catálogo. Uma integração funcional com IA é necessária para atender R1.

## Dentro do escopo

Chat com IA real, conversa contínua salva, um registro em preparação, extração e complementação, revisão/correção/cancelamento, confirmação por botão, retomada, persistência sem duplicação da mesma proposta e consultas reais com os filtros e períodos definidos.

## Fora do escopo

Múltiplos agentes ou múltiplas conversas por usuário, lotes de transações, edição/exclusão de registros salvos pelo chat, gestão de categorias, pagamentos externos, bancos, importações, arquivos/áudio/imagens no chat, recorrência, análises avançadas e recomendações financeiras personalizadas. Não inclui gerenciamento de exclusão/edição de mensagens ou garantia de atualização automática de respostas históricas.
<!-- project-flow:end -->

## Descrição exata após publicação

<!-- project-flow:run 1a34fdd3-9440-446c-8725-76246ece59ff -->
<!-- project-flow:start -->
## Objetivo

Permitir ao usuário registrar receitas e despesas e consultar suas finanças por linguagem natural, com IA real, confirmação explícita antes de gravar e respostas fundamentadas exclusivamente nos registros da própria conta.

## Resultado esperado

O usuário conversa, complementa dados faltantes, revisa uma proposta e confirma um único registro. Consulta saldo, totais e listas reais, incluindo agendadas quando solicitadas. Mensagens e registro em preparação são preservados ao sair e voltar.

## Atores e permissões

Somente o usuário autenticado com e-mail confirmado acessa sua conversa, propostas e dados financeiros. Pedidos no chat não alteram o proprietário de uma transação, dispensam confirmação ou permitem consultar outra conta. O assistente não executa pagamentos nem operações bancárias.

## Histórias de usuário

1. Como usuário, quero descrever uma receita ou despesa para preparar seu registro.
2. Como usuário, quero complementar ou corrigir os dados e confirmar antes de gravar.
3. Como usuário, quero cancelar uma proposta sem criar transação.
4. Como usuário, quero consultar números e movimentações reais com períodos e filtros claros.
5. Como usuário, quero retomar minha conversa e proposta pendente depois de sair.
6. Como usuário, quero consultar dados enquanto preparo um registro, sem perder a proposta.

## Fluxo principal

1. Abrir a conversa contínua da própria conta; na primeira utilização, mostrar orientação sobre registro confirmado e consultas disponíveis.
2. Enviar uma mensagem sobre uma movimentação. A IA identifica tipo, valor, descrição, categoria e data; solicita os dados faltantes ou ambíguos.
3. Sem data informada, propor hoje em America/Sao_Paulo. Fixar datas relativas na data concreta interpretada, exibindo-a para revisão.
4. Com os cinco campos completos e válidos, apresentar proposta com Confirmar, Corrigir e Cancelar.
5. Corrigir permite revisar todos os campos em formulário; salvar a correção atualiza a proposta e exige nova confirmação, sem criar a transação.
6. Confirmar grava a versão atual da proposta uma única vez. Mostrar sucesso somente após persistência confirmada. O registro aparece no histórico e compõe o dashboard conforme sua data; se futuro, informar que está agendado.
7. Cancelar descarta o registro em preparação sem gravar. A conversa mantém o resultado do cancelamento.
8. Para consultas, identificar intenção, período e filtros; consultar os dados atuais e apresentar resultado com esses critérios explícitos.
9. Ao sair e voltar, restaurar mensagens e eventual preparação incompleta ou proposta pendente. Nenhuma retomada confirma ou altera a data automaticamente.

## Fluxos alternativos e exceções

- Mensagem com várias movimentações pede envio de uma por vez. Não grava parcialmente nem escolhe silenciosamente uma delas.
- Tipo, valor, descrição ou data ambíguos exigem esclarecimento. Não inventar valores nem usar hoje para substituir uma data explicitamente informada, mas inválida.
- Inferir categoria somente entre as predefinidas e compatíveis com o tipo. Sem correspondência segura, pedir escolha; não criar categoria nem selecionar Outras silenciosamente.
- Sem campos válidos, não liberar confirmação. Confirmação escrita, como “sim”, orienta usar o botão da proposta atual e não grava.
- Versão corrigida invalida a confirmação de versões anteriores. Propostas canceladas ou já confirmadas não podem gravar novamente, inclusive após recarregar a página.
- Consultas são permitidas enquanto houver registro em preparação. Outro pedido de registro orienta confirmar ou cancelar o anterior; mensagem ambígua pede esclarecimento, sem sobrescrever a proposta.
- Falha de interpretação ou indisponibilidade da IA mostra aviso e permite nova tentativa ou cadastro manual, preservando a proposta já existente. A operação manual não confirma automaticamente a proposta do chat.
- Falha conhecida de gravação mantém a proposta para nova tentativa, sem anunciar sucesso. Se o resultado da gravação for incerto, conferir se ela ocorreu antes de repetir; não criar outra transação por uma repetição da confirmação.
- Consulta sem registros informa a ausência; consulta que falhou informa indisponibilidade, sem fabricar números nem substituir falha por zero.
- Pedidos de edição ou exclusão de transações já salvas orientam usar Gestão de transações. Cancelar uma proposta não exclui transações.
- Consultas fora das capacidades previstas pedem reformulação ou explicam o limite, sem inventar respostas financeiras.

## Regras de negócio

R1. IA real interpreta linguagem natural. Provedor, modelo e mecanismo de integração são decisões posteriores de implementação; uma simulação por regras não satisfaz esta entrega.

R2. Campos, limites e categorias são os mesmos de Gestão de transações #1015911: tipo receita/despesa, valor em reais entre R$ 0,01 e R$ 999.999.999,99 com até duas casas decimais, descrição de 1 a 120 caracteres após remover espaços nas extremidades, categoria compatível e data válida entre 01/01/1900 e 31/12/9999. Não arredondar silenciosamente precisão excedente.

R3. Receitas: Salário, Freelance, Rendimentos e Outras receitas. Despesas: Alimentação, Moradia, Transporte, Saúde, Educação, Lazer, Compras e Outras despesas. O usuário revisa a categoria inferida antes de confirmar.

R4. Há no máximo um registro em preparação por usuário. Ele pode estar incompleto ou pronto para confirmação. Mensagens e propostas não são transações e não entram nos cálculos antes de confirmação e persistência.

R5. Somente Confirmar na versão atual grava. Repetir a confirmação da mesma proposta produz no máximo uma transação; iniciar e confirmar uma nova proposta com dados iguais pode criar outro registro, conforme a regra de transações distintas.

R6. Uma conversa contínua é persistida por usuário. A proposta e dados já coletados são retomados sem gravação; uma data já fixada não muda porque o dia mudou. Mensagens antigas permanecem como histórico, não como prova de saldo atual. Nova consulta busca dados atuais, refletindo alterações e exclusões feitas na interface.

R7. Datas relativas usam America/Sao_Paulo. Sem data no registro, propor hoje. Quando uma expressão de data não puder ser determinada com segurança, perguntar. Futuras são permitidas e só afetam saldo e totais ao chegar sua data.

R8. Consultas disponíveis: saldo geral; totais de receitas e despesas por período e categoria; listagem por período, tipo e categoria; listagem de agendadas. Períodos reconhecidos incluem hoje, ontem, este mês, mês passado e datas ou intervalos explícitos, incluindo pedido expresso de todo o histórico.

R9. Consulta independente sem período usa este mês para totais e listas, declarando isso na resposta. Saldo geral sempre considera todo o histórico até hoje. Agendadas sem período considera todas as futuras. Continuação explícita de uma consulta pode reaproveitar seus filtros; se houver dúvida, esclarecer e apresentar os critérios efetivamente utilizados.

R10. Totais e saldo seguem Gestão de transações: somente registros próprios não excluídos até hoje. Intervalos incluem as datas inicial e final; intervalo invertido ou ambíguo pede correção. Listas comuns excluem agendadas, salvo pedido explícito para incluí-las ou consultá-las; quando incluídas, identificá-las separadamente e não somá-las aos valores já contabilizados.

R11. Proposta de apresentação das listas: até dez registros por resposta, por data decrescente e cadastro mais recente no desempate, com quantidade total encontrada e opção Ver mais. Ver mais mantém período e filtros e consulta dados reais; ao alterar os critérios, iniciar nova lista. Os totais solicitados correspondem a todos os registros elegíveis do filtro, não só à página exibida.

R12. Cada resposta financeira identifica período e filtros, distingue dados contabilizados de agendados e usa reais com centavos. Não inventa transações, categorias, valores ou resultado de uma gravação. Registrar uma futura não significa realizar o pagamento ou recebimento.

## Dados percebidos pelo usuário

Mensagens salvas, indicação de processamento e erro, perguntas de complementação, proposta com tipo/valor/descrição/categoria/data, botões Confirmar/Corrigir/Cancelar, estado pendente/confirmado/cancelado, confirmação de persistência, resultados com período e filtros, listas com indicação de agendamento e opção de continuidade.

## Critérios de aceite

CA1. “Gastei R$ 35 no almoço”, sem data, prepara despesa de R$ 35, descrição coerente, categoria sugerida e data de hoje em Brasília, permitindo revisão; não cria transação antes de Confirmar.

CA2. Dados ausentes ou interpretação ambígua geram pergunta de esclarecimento. Campo inválido ou categoria incompatível impede confirmação; nenhuma informação financeira é inventada para completar a proposta.

CA3. Mensagem com duas movimentações pede envio separado e não grava nenhuma parcialmente.

CA4. Corrigir altera a proposta, exige nova revisão e invalida confirmações antigas. Cancelar não cria transação; escrever “sim” não grava e orienta usar Confirmar.

CA5. Confirmar proposta válida cria um único registro próprio e mostra sucesso após persistência. Repetir a mesma confirmação, inclusive depois de voltar ao chat, não duplica.

CA6. Confirmar movimentação futura a registra como agendada; ela fica fora dos totais até sua data e entra automaticamente conforme as regras de Gestão de transações.

CA7. Sair e voltar restaura mensagens e preparação pendente ou incompleta; não grava, não perde os dados coletados e não troca a data fixada por um novo hoje.

CA8. Uma consulta durante preparação responde com dados reais sem perder a proposta. Pedido de outro registro orienta concluir ou cancelar o anterior; ambiguidade não sobrescreve dados.

CA9. Consultas retornam saldo, totais e listas conforme R8 a R12. Sem período, usam os padrões de R9; pedido explícito de outro período ou todo o histórico é respeitado e identificado.

CA10. Dados inexistentes produzem ausência de registros e zero quando o cálculo realmente for zero; falha de leitura produz indisponibilidade, nunca um resultado financeiro inventado.

CA11. Após editar ou excluir uma transação pela interface, uma nova consulta reflete o estado atual; respostas antigas continuam apenas como histórico.

CA12. Mais de dez registros permitem Ver mais com os mesmos filtros; a resposta informa a quantidade total e não apresenta uma página como se fosse toda a listagem. Totais usam o conjunto completo elegível.

CA13. Falha de gravação não anuncia sucesso; nova tentativa ou confirmação repetida não duplica uma gravação já efetivada. Falha da IA permite tentar novamente ou usar cadastro manual.

CA14. Usuário não consulta nem modifica conversa, proposta ou dados de outra conta, mesmo pedindo isso em linguagem natural. Pedido de editar/excluir transação salva orienta usar Gestão de transações.

## Dependências

Gestão de transações — #1015911 — fornece persistência, categorias, validações, isolamento e regras de cálculo. Acesso à conta está incluído por essa dependência. Os registros confirmados são os mesmos consumidos pelo Dashboard financeiro #1015912; não há dependência direta adicional no catálogo. Uma integração funcional com IA é necessária para atender R1.

## Dentro do escopo

Chat com IA real, conversa contínua salva, um registro em preparação, extração e complementação, revisão/correção/cancelamento, confirmação por botão, retomada, persistência sem duplicação da mesma proposta e consultas reais com os filtros e períodos definidos.

## Fora do escopo

Múltiplos agentes ou múltiplas conversas por usuário, lotes de transações, edição/exclusão de registros salvos pelo chat, gestão de categorias, pagamentos externos, bancos, importações, arquivos/áudio/imagens no chat, recorrência, análises avançadas e recomendações financeiras personalizadas. Não inclui gerenciamento de exclusão/edição de mensagens ou garantia de atualização automática de respostas históricas.

## Requisito canônico

Documento aprovado por Mário Tinelli: docs/harness/features/{{created_issue_id}}-assistente-financeiro-ia/feature.md
<!-- project-flow:end -->
