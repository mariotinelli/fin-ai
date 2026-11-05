# [DEV] [WEB] [USUARIO] Dashboard financeiro - Indicadores e consulta por mês

- Redmine: `#1015937`
- Tipo: `DEV`
- Tracker: Task (`4`)
- Item pai: `#1015912`
- Estimativa: `1.5h`

## Descrição

## Entrega

Substituir os placeholders por saldo geral e totais mensais reais do titular, com seleção do mês, comparação simples e resultado mensal coerentes. Reutilizar os cálculos de Gestão de transações.

## Escopo e limites

Não reimplementa cálculo de competência, não antecipa futuras nem cria projeções/relatórios avançados. Recentes é outra entrega; a preservação do seu conjunto na troca de mês é conferida na integração.

## Critérios de aceite

- Elegíveis são somente transações próprias não excluídas e com data até hoje em America/Sao_Paulo; dashboard exige autenticação e e-mail confirmado.
- Saldo geral soma receitas elegíveis menos despesas de todo histórico, aceita negativo e não muda por selecionar outro mês; sem saldo inicial separado.
- Totais mensais somam receitas/despesas elegíveis por data dentro do mês selecionado; atual só até hoje, passado seus registros, futuro sem antecipação.
- Comparação simples de receitas/despesas e resultado mensal usam exatamente os totais dos indicadores; resultado=receitas−despesas. Sem projeções, tendências ou relatórios avançados.
- Ao abrir o dashboard consultar valores atuais; mês inicial é o atual em Brasília, sem usar o calendário UTC incorretamente.
- Exibir valores em reais com duas casas, identificando saldo geral e mês selecionado.
- Abrir no mês atual de Brasília e mostrar só números/registros do titular autenticado e confirmado.
- Saldo, totais e resultado mensal correspondem a R2/R3/R6, inclusive negativo.
- Trocar mês altera somente totais/comparativo do período, não saldo geral nem conjunto de recentes.
- Sem movimentações mostrar R$0,00 e orientação de primeiro cadastro; só futuras mostrar zeros reais e orientação de agendamentos no histórico; mês vazio zera só totais, preservando saldo e recentes globais.
- Indicadores mostram carregamento durante consulta; falha mostra indisponibilidade e tentar novamente, sem substituir por zeros aparentando dados reais; sucesso posterior mostra valores reais.
- Nenhum usuário acessa indicadores de outra conta, inclusive tentativa direta de trocar identificador.

## Dependências

Para iniciar: layout e autenticação existentes e requisitos funcionais aprovados permitem preparar apresentação e casos de teste. Para concluir: consumir dados/cálculos reais de ‘[DEV] [WEB] [USUARIO] Gestão de transações - Agendamentos e competência financeira (#1015933)’, alimentados por ‘[DEV] [WEB] [USUARIO] Gestão de transações - Cadastro e conferência de uma transação própria (#1015930)’; integração com ‘Dashboard financeiro - Movimentações recentes e detalhes’ verifica que trocar mês não muda recentes. Não concluir com dados simulados.

## Referências

Item pai Redmine #1015912; regras/critérios R1, R2, R3, R6, R7-abertura, R8-valores, CA1, CA2, CA3, CA6-indicadores, CA9-indicadores, CA10-indicadores.

<!-- project-slices-child:1ba44f48352382b8269a32a367c27279a9eb94b263cd596ed7920a5779769918 -->

## Relações

- `#1015937` blocks `#1015939`
- `#1015937` blocks `#1015940`
