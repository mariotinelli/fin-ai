# [WEB] [USUARIO] Dashboard financeiro

## Objetivo

Permitir ao usuário compreender sua situação financeira por meio do saldo geral, receitas e despesas mensais e movimentações recentes, calculados exclusivamente a partir dos seus registros reais.

## Resultado esperado

O usuário acessa uma visão geral coerente com Gestão de transações, escolhe o mês dos totais e consulta os cinco registros mais recentes até hoje. Movimentações futuras não antecipam valores no dashboard.

## Atores e permissões

Usuário autenticado com e-mail confirmado acessa somente seus próprios números e registros. Usuário não autenticado ou sem e-mail confirmado segue as restrições de Acesso à conta. Dados de outra conta não aparecem em indicadores, recentes ou detalhes.

## Histórias de usuário

1. Como usuário, quero visualizar meu saldo geral para conhecer o resultado acumulado das minhas movimentações.
2. Como usuário, quero consultar receitas e despesas de um mês para acompanhar esse período.
3. Como usuário, quero ver movimentações recentes e acessar seus detalhes ou o histórico.
4. Como usuário, quero que alterações nas minhas transações e a chegada de datas agendadas sejam refletidas nos números apresentados.

## Fluxo principal

1. Abrir o dashboard com o mês atual de America/Sao_Paulo selecionado.
2. Consultar saldo geral acumulado até hoje, receitas e despesas do mês selecionado.
3. Alterar o mês para consultar outro período. Somente indicadores mensais e seu comparativo mudam; saldo geral e recentes mantêm seus critérios globais.
4. Consultar até cinco movimentações com data mais recente até hoje, de todo o histórico; abrir seus detalhes reutiliza a entrega de Gestão de transações.
5. Usar Ver todas para abrir o histórico integral. Usar Nova transação para iniciar o cadastro já definido em Gestão de transações.
6. Ao concluir cadastro, edição ou exclusão a partir do dashboard, atualizar os indicadores e a lista sem exigir recarregamento manual. Ao voltar de outras áreas, consultar novamente os dados reais.

## Fluxos alternativos e exceções

- Conta sem movimentações apresenta valores R$ 0,00 e orientação para registrar a primeira transação.
- Mês sem movimentações elegíveis apresenta receitas e despesas zeradas e mensagem de ausência naquele período; saldo e recentes de outros meses continuam visíveis.
- Conta com apenas registros futuros apresenta saldo e totais zerados e nenhuma movimentação recente; informa que os agendamentos podem ser consultados no histórico.
- Mês futuro pode ser selecionado, mas não apresenta previsões como valores realizados: seus totais permanecem zerados até existirem registros elegíveis.
- Durante a consulta, apresentar estado de carregamento. Se a leitura falhar, mostrar indisponibilidade e opção de tentar novamente; não substituir falha por zeros que pareçam valores reais.
- Se uma transação deixar de existir antes de abrir detalhes, informar indisponibilidade e permitir atualizar a lista.
- Ao cancelar cadastro, edição ou exclusão, manter os valores anteriores. Só refletir alterações efetivamente persistidas.

## Regras de negócio

R1. Elegíveis são as transações do próprio usuário, não excluídas e com data menor ou igual a hoje em America/Sao_Paulo.

R2. Saldo geral é a soma de receitas elegíveis menos a soma de despesas elegíveis de todo o histórico. Pode ser negativo e não muda apenas porque o usuário selecionou outro mês. Não há saldo inicial separado.

R3. Receitas e despesas mensais somam separadamente os registros elegíveis cuja data pertence ao mês selecionado. O mês atual inclui somente datas até hoje; um mês passado inclui seus registros elegíveis; um mês futuro não antecipa movimentações.

R4. Recentes usa todo o histórico elegível, independente do mês selecionado, em ordem decrescente de data da movimentação, com desempate pelo cadastro mais recente, limitado a cinco registros. Agendadas somente entram quando sua data chega. Com menos de cinco registros elegíveis, exibir todos os existentes.

R5. Registros duplicados permitidos pela Gestão de transações contam individualmente. Edição e exclusão recalculam os indicadores e podem mudar a lista de recentes.

R6. Proposta visual de resumo: apresentar comparação simples de receitas e despesas do mês e resultado mensal (receitas menos despesas), usando exatamente os mesmos totais dos indicadores. É uma representação dos dados já calculados, sem projeções, tendências ou relatórios avançados.

R7. Ao abrir ou retornar ao dashboard e após uma alteração concluída nele, consultar valores atuais. Uma tela mantida aberta durante a virada da data deve atualizar o conjunto elegível quando voltar a ser consultada; atualização contínua de uma tela ociosa ou sincronização instantânea entre dispositivos não são critérios desta entrega.

R8. Cada valor é apresentado em reais com duas casas decimais. A tela identifica claramente saldo geral, mês selecionado e que os recentes consideram todo o histórico até hoje.

## Dados percebidos pelo usuário

Saldo geral, mês de referência, total de receitas, total de despesas, comparativo e resultado mensal propostos em R6. Nos recentes: descrição, tipo, valor, categoria e data; todos os campos ficam disponíveis nos detalhes, mesmo quando o layout compacto reduz a lista. Estados de carregamento, ausência de dados e erro, e acessos a detalhes, histórico e cadastro.

## Critérios de aceite

CA1. Ao abrir o dashboard, selecionar o mês atual pelo calendário de Brasília e exibir somente números e registros do usuário autenticado e confirmado.

CA2. Com receitas e despesas elegíveis, o saldo geral corresponde a R2, inclusive quando negativo; totais e resultado mensal correspondem a R3 e R6.

CA3. Ao trocar o mês, atualizar os totais e comparativo daquele mês sem alterar o saldo geral nem o conjunto de recentes apenas pela troca.

CA4. Registros futuros não entram em nenhum indicador ou nos recentes antes da data. Ao chegar a data, a próxima consulta os considera automaticamente, sem confirmar pagamento ou recebimento.

CA5. Exibir os cinco registros de data mais recente até hoje, com desempate pelo cadastro, ou todos quando houver menos de cinco; registros de outros meses podem aparecer.

CA6. Sem registros elegíveis, mostrar zeros e estado vazio coerente; com apenas futuras, permitir localizar os agendamentos pelo histórico; mês vazio não apaga saldo e recentes de outros meses.

CA7. Abrir detalhes e Nova transação reutiliza as operações de Gestão de transações. Ver todas abre o histórico integral, sem transportar um filtro mensal que contradiga a lista global de recentes.

CA8. Cadastro, edição ou exclusão concluídos a partir do dashboard atualizam números e recentes sem recarregamento manual; cancelar não altera os valores. Retornar de outras áreas consulta os dados atualizados.

CA9. Falha de consulta apresenta erro e nova tentativa, sem exibir zeros como se fossem dados recuperados; sucesso posterior apresenta os valores reais.

CA10. Um usuário não acessa indicadores, registros ou detalhes de outro usuário; transação indisponível não revela informações de outra conta.

## Dependências

Gestão de transações — #1015911 — fornece registros, categorias, isolamento, operações e regras temporais. O requisito de Acesso à conta é atendido por essa dependência. O dashboard não depende da entrega do assistente para apresentar números e movimentações.

## Designs e evidências

Catálogo aprovado; respostas Q11 e Q12; decisões e requisito de Gestão de transações #1015911. O pacote FinAI-Controle-Financeiro.zip orienta apenas o visual da Visão geral. O comparativo e resultado mensal de R6, os estados e atalhos são propostas explícitas nesta revisão, sem adotar o armazenamento local ou o assistente simulado do protótipo.

## Dentro do escopo

Indicadores reais por usuário, seleção de mês, saldo geral, comparação simples e resultado do mês, cinco movimentações recentes, acesso às operações existentes, estados sem dados e erro e atualização nos momentos descritos.

## Fora do escopo

Projeções de valores futuros, relatórios avançados, exportações, metas, saldo inicial separado, integração bancária, implementação do chat e atualização contínua de uma tela ociosa ou sincronização instantânea entre dispositivos. A funcionalidade do assistente pertence ao próximo item; eventual chamada visual não deve anunciar atendimento funcional antes de sua entrega.
