# Prévia completa — Dashboard financeiro

Proposta ainda não aprovada para publicação. Um único consentimento cobre o requisito integral e exatamente as três operações abaixo.

## Destino e escolhas de publicação

- Servidor https://redmine.remsoft.com.br; identidade verificada Mário Tinelli (131789).
- Projeto FinAi (65224); Sprint 1 (20355), selecionada pelo usuário e confirmada aberta.
- Feature, tracker 2; estado inicial New (1), sem categoria. Classificação e título herdados do catálogo aprovado; o projeto não disponibiliza categorias de issue na consulta de metadados.
- Título: [WEB] [USUARIO] Dashboard financeiro.
- Sequencing: campo 2, valor 4, pela quarta posição do catálogo. Mantém a sequência própria iniciada em 1, conforme exceção aprovada para desconsiderar todas as tasks antigas. Não usa conteúdo ou sequência das issues antigas e não alega máximo histórico observado.
- Nova demanda deste fluxo, sem reaproveitamento de tasks antigas.
- Pré-requisito direto: #1016105, Gestão de transações, criada neste fluxo; continua New, sem alegação de implementação concluída. Acesso e base visual são pré-requisitos transitivos e não recebem arestas diretas redundantes.

## Operações propostas

1. Criar uma nova Feature com os atributos exatos e o conteúdo funcional integral abaixo.
2. Persistir o ID retornado e atualizar somente a descrição e fixed_version_id dessa mesma issue, acrescentando caminho definitivo e atribuição. {{created_issue_id}} será substituído exclusivamente pelo ID retornado na criação. Preservar estado e textos externos à seção gerenciada.
3. Criar ou reconciliar a relação blocks, chave transacoes-blocks-dashboard, da issue #1016105 para {{created_issue_id}}. Não duplicar relação equivalente nem mudar estados.

Nenhuma outra issue é criada, excluída, encerrada ou alterada. A #1016105 recebe somente o vínculo descrito. Tasks antigas permanecem desconsideradas.

## Requisito canônico integral

# [WEB] [USUARIO] Dashboard financeiro

## Objetivo

Permitir que o titular autenticado e com e-mail confirmado compreenda sua situação financeira pelo saldo geral, totais de receitas e despesas do mês, balanço mensal e movimentações recentes, usando exclusivamente seus registros reais persistidos no sistema.

## Resultado esperado

A Visão geral apresenta números coerentes com as transações do titular, permite consultar outro mês e oferece caminhos para registrar ou consultar movimentações. Valores vazios, negativos e indisponíveis são distinguidos, sem dados fictícios ou de outras contas.

## Atores e permissões

Titular autenticado e confirmado consulta somente os próprios dados. Visitantes e contas sem confirmação seguem as restrições da Feature de acesso. Totais, contagens, gráfico e lista não podem revelar informações de outro titular, inclusive por acesso direto.

## Histórias de usuário

1. Como titular, quero visualizar meu saldo geral para conhecer a diferença acumulada entre receitas e despesas registradas.
2. Como titular, quero consultar receitas, despesas e resultado de um mês para entender aquele período.
3. Como titular, quero ver minhas movimentações mais recentes e abrir seus detalhes ou o histórico completo.
4. Como titular, quero iniciar um registro pelo dashboard e ver meus números atualizados após manter as transações.
5. Como titular sem registros, quero orientação para começar sem confundir ausência de dados com falha de consulta.

## Fluxo principal

1. Abrir Visão geral. Consultar os dados do titular e apresentar saldo geral, receitas do mês e despesas do mês, com suas contagens, iniciando no mês corrente.
2. Apresentar o balanço do mês por duas barras comparativas identificadas como Receitas e Despesas, seus valores, mês de referência e resultado mensal.
3. Selecionar outro mês. Atualizar totais, contagens, gráfico e resultado referentes àquele mês. Manter o saldo geral e as movimentações recentes correspondentes a todo o histórico.
4. Apresentar até cinco movimentações recentes com descrição, categoria, data, valor e identificação de receita/despesa, conforme a composição responsiva do design.
5. Abrir os detalhes de uma movimentação ou Ver todas para acessar o histórico completo do titular. Reutilizar as operações e regras da gestão de transações.
6. Acionar Nova transação, preencher e salvar pela jornada já definida. Após sucesso, atualizar os dados do dashboard. Edição ou exclusão concluída a partir dos detalhes também atualiza os números e a lista.

## Fluxos alternativos e exceções

- Sem registros no histórico, apresentar saldo e totais em R$ 0,00, contagens vazias, orientações e ação para o primeiro cadastro; o gráfico apresenta o estado inicial da referência.
- Com registros no histórico, mas nenhum no mês selecionado, apresentar totais mensais e resultado em zero, contagens vazias e gráfico sem movimento; saldo geral e recentes continuam usando o histórico completo.
- Saldo geral ou resultado mensal negativo é apresentado com valor e sinal corretos, sem limitar o resultado a zero.
- Receitas e despesas positivas de mesmo valor produzem resultado zero, mantendo o gráfico e as contagens de registros existentes; não confundir com mês sem movimentação.
- Falha de consulta apresenta indisponibilidade e caminho de nova tentativa. Não apresentar erro de carregamento como zero, histórico vazio ou números recuperados com sucesso.
- Cancelar ou falhar no cadastro, edição ou exclusão não apresenta novos valores como se a alteração tivesse sido persistida. Após uma alteração concluída, refletir o estado salvo.
- O convite visual para o assistente segue a referência; sua ação só abre o assistente quando essa Feature estiver disponível. Até lá, mantê-la indisponível, sem simular conversa ou criar uma tela futura. Isso não bloqueia o aceite do dashboard.

## Regras de negócio

R1. Saldo geral = soma de todas as receitas do titular menos soma de todas as despesas do titular em todo o histórico persistido. Não há saldo inicial manual, conciliação bancária ou saldo por múltiplas contas nesta entrega. O seletor de mês não altera o saldo geral.

R2. Receitas e despesas do mês são as somas por tipo das transações cuja data pertence ao mês e ano selecionados. Contagens correspondem à quantidade de transações de cada tipo no período. Resultado do mês = receitas do mês menos despesas do mês.

R3. Iniciar no mês corrente e permitir escolher outro mês e ano. As datas e o mês corrente seguem o mesmo calendário local da gestão de transações. O dashboard não altera datas nem cria registros; somente movimentações realizadas são persistidas conforme a Feature responsável.

R4. O balanço compara receitas e despesas do mês em duas barras, com legenda e valores. A maior soma positiva ocupa a extensão de referência e a outra é proporcional; total zero não causa cálculo inválido. Sem transações no mês, apresentar estado vazio próprio em vez de barras fictícias.

R5. Recentes apresenta os cinco registros mais recentes de todo o histórico, ordenados por data decrescente e depois pelo cadastro mais recente, como na gestão de transações. Com menos de cinco, mostrar somente os existentes. Trocar o mês não filtra essa lista.

R6. Consultas, contagens e totais usam somente transações persistidas do titular. Ao acessar ou atualizar a Visão geral, buscar o estado salvo no sistema. Após concluir operações financeiras iniciadas no dashboard, atualizar seus valores e lista. Esta entrega não define atualização automática contínua entre sessões.

R7. Apresentar valores em reais e datas em formato brasileiro. Distinguir receitas e despesas por identificação, sinal e aparência, mantendo a linguagem visual FinAI. Não usar números de demonstração ou resultados derivados de outro titular.

R8. Preservar a composição #overview do design: cabeçalho, mês, ação Nova transação, três cartões de resumo com destaque no saldo geral, balanço do mês, convite do assistente e últimas movimentações com Ver todas. Usar a base visual aprovada, incluindo claro, escuro e acompanhar o sistema; no celular, adaptar grade, navegação e lista compacta sem perder acesso aos detalhes.

## Dados percebidos pelo usuário

Saldo geral; receitas e despesas do mês com contagens; mês/ano selecionados; barras e legenda; resultado mensal; últimas movimentações com seus campos e sinais; ações para cadastro, detalhes, histórico e assistente quando disponível; estados de carregamento, ausência de registros e falha.

## Critérios de aceite

CA1. Com receitas e despesas em meses diferentes, abrir Visão geral; o saldo geral corresponde à diferença de todo o histórico e os totais/contagens mensais correspondem somente ao mês corrente.

CA2. Selecionar outro mês e ano; atualizar receitas, despesas, contagens, barras e resultado do período, mantendo saldo geral e recentes independentes do filtro mensal.

CA3. Consultar cenário com despesas superiores às receitas; apresentar saldo geral e/ou resultado mensal negativos corretamente. Com valores iguais e positivos, mostrar resultado zero com os registros e barras correspondentes.

CA4. Sem registros, apresentar zeros e orientação de início, sem valores fictícios. Em um mês sem movimento, mas com histórico em outros meses, apresentar somente os indicadores mensais vazios, preservando saldo e recentes do histórico.

CA5. Comparar o gráfico com os totais mensais; legenda, valores e proporções das duas barras correspondem às somas. Um tipo com soma zero e outro positivo continua apresentável; ausência completa de movimentos usa o estado vazio.

CA6. Com mais de cinco registros e datas empatadas, conferir os cinco recentes conforme R5. Com menos registros, não completar a lista com exemplos. Abrir detalhes e Ver todas leva aos dados próprios usando a gestão de transações.

CA7. Cadastrar, editar e excluir uma transação pelas ações disponíveis no dashboard; após cada sucesso, saldo, totais, contagens, barras, resultado e recentes refletem os registros salvos segundo seus respectivos recortes. Cancelamento ou falha não aplica alteração fictícia.

CA8. Provocar falha de consulta; apresentar indisponibilidade e nova tentativa sem afirmar saldo zero ou ausência de registros. Restabelecer a consulta e tentar novamente recupera os valores reais.

CA9. Usar contas com dados distintos; cada uma visualiza somente seus próprios totais, contagens, gráfico e recentes. Visitantes e contas sem confirmação não acessam o dashboard conforme a Feature de acesso.

CA10. Conferir a composição da Visão geral em computador, tablet e celular nos temas claro, escuro e acompanhar o sistema; manter hierarquia, destaque do saldo, cartões, balanço e lista do design. O convite do assistente não simula uma funcionalidade antes da entrega responsável.

## Dependências

Gestão de transações, issue #1016105: fornece os registros pessoais persistidos, suas categorias e as operações de manutenção reutilizadas. Acesso #1016104 e base visual #1016101 são pré-requisitos transitivos, sem relações diretas redundantes. Requisitos publicados não comprovam implementação concluída.

Assistente financeiro é entrega independente após transações. O dashboard conserva seu ponto de entrada visual e habilita a ação quando o assistente estiver disponível; não exige implementar chat ou IA para concluir esta Feature.

## Designs e evidências

Referência principal design-input-001, ../../scopes/2026-11-11-finai-mvp/sources/design-input-001.md; ZIP original C:/Users/maari/Downloads/FinAI-Controle-Financeiro.zip. Localizadores: #overview, #balance, #income, #expense, #graph, #month-result, #recent, #month e #open-chat; funções render, sorted e list; estilos .stats, .overview-grid, .assistant-teaser e media queries. Cálculos e recortes de R1 a R5 reproduzem os demonstrados no protótipo.

Base visual conforme docs/harness/features/1016101-adequacao-visual-do-finai/feature.md; dados e manutenção conforme docs/harness/features/1016105-gestao-de-transacoes/feature.md. Escopo §§3.1 e 4 em conversation-input-001. Adaptar persistência local para dados do sistema e remover referências a assistente simulado conforme decisões anteriores. Aceitação visual em R8 e CA10. Nenhuma task antiga do Redmine é fonte.

## Dentro do escopo

Saldo geral acumulado, receitas/despesas e contagens mensais, seleção de mês, balanço simples e resultado, cinco movimentações recentes, reaproveitamento de cadastro/detalhes/histórico, atualização dos indicadores após manutenção concluída, isolamento por titular e estados descritos, conforme o design.

## Fora do escopo

Saldo inicial manual, integração ou conciliação bancária, múltiplas contas financeiras, gráficos de evolução temporal, relatórios avançados, exportação e filtros analíticos adicionais. Chat, registro por linguagem natural e consultas à IA pertencem à Feature Assistente financeiro. Esta etapa não implementa código nem decompõe tarefas técnicas.

## Atributos exatos da criação

```json
{
  "project_id": 65224,
  "tracker_id": 2,
  "status_id": 1,
  "category_id": null,
  "fixed_version_id": 20355,
  "custom_fields": [
    {
      "id": 2,
      "value": "4"
    }
  ],
  "subject": "[WEB] [USUARIO] Dashboard financeiro"
}
```

## Descrição integral da criação

````markdown
<!-- project-flow:run d346be46-ce4c-418a-a37e-bd652d5d7049 -->
<!-- project-flow:start -->
## Objetivo

Permitir que o titular autenticado e com e-mail confirmado compreenda sua situação financeira pelo saldo geral, totais de receitas e despesas do mês, balanço mensal e movimentações recentes, usando exclusivamente seus registros reais persistidos no sistema.

## Resultado esperado

A Visão geral apresenta números coerentes com as transações do titular, permite consultar outro mês e oferece caminhos para registrar ou consultar movimentações. Valores vazios, negativos e indisponíveis são distinguidos, sem dados fictícios ou de outras contas.

## Atores e permissões

Titular autenticado e confirmado consulta somente os próprios dados. Visitantes e contas sem confirmação seguem as restrições da Feature de acesso. Totais, contagens, gráfico e lista não podem revelar informações de outro titular, inclusive por acesso direto.

## Histórias de usuário

1. Como titular, quero visualizar meu saldo geral para conhecer a diferença acumulada entre receitas e despesas registradas.
2. Como titular, quero consultar receitas, despesas e resultado de um mês para entender aquele período.
3. Como titular, quero ver minhas movimentações mais recentes e abrir seus detalhes ou o histórico completo.
4. Como titular, quero iniciar um registro pelo dashboard e ver meus números atualizados após manter as transações.
5. Como titular sem registros, quero orientação para começar sem confundir ausência de dados com falha de consulta.

## Fluxo principal

1. Abrir Visão geral. Consultar os dados do titular e apresentar saldo geral, receitas do mês e despesas do mês, com suas contagens, iniciando no mês corrente.
2. Apresentar o balanço do mês por duas barras comparativas identificadas como Receitas e Despesas, seus valores, mês de referência e resultado mensal.
3. Selecionar outro mês. Atualizar totais, contagens, gráfico e resultado referentes àquele mês. Manter o saldo geral e as movimentações recentes correspondentes a todo o histórico.
4. Apresentar até cinco movimentações recentes com descrição, categoria, data, valor e identificação de receita/despesa, conforme a composição responsiva do design.
5. Abrir os detalhes de uma movimentação ou Ver todas para acessar o histórico completo do titular. Reutilizar as operações e regras da gestão de transações.
6. Acionar Nova transação, preencher e salvar pela jornada já definida. Após sucesso, atualizar os dados do dashboard. Edição ou exclusão concluída a partir dos detalhes também atualiza os números e a lista.

## Fluxos alternativos e exceções

- Sem registros no histórico, apresentar saldo e totais em R$ 0,00, contagens vazias, orientações e ação para o primeiro cadastro; o gráfico apresenta o estado inicial da referência.
- Com registros no histórico, mas nenhum no mês selecionado, apresentar totais mensais e resultado em zero, contagens vazias e gráfico sem movimento; saldo geral e recentes continuam usando o histórico completo.
- Saldo geral ou resultado mensal negativo é apresentado com valor e sinal corretos, sem limitar o resultado a zero.
- Receitas e despesas positivas de mesmo valor produzem resultado zero, mantendo o gráfico e as contagens de registros existentes; não confundir com mês sem movimentação.
- Falha de consulta apresenta indisponibilidade e caminho de nova tentativa. Não apresentar erro de carregamento como zero, histórico vazio ou números recuperados com sucesso.
- Cancelar ou falhar no cadastro, edição ou exclusão não apresenta novos valores como se a alteração tivesse sido persistida. Após uma alteração concluída, refletir o estado salvo.
- O convite visual para o assistente segue a referência; sua ação só abre o assistente quando essa Feature estiver disponível. Até lá, mantê-la indisponível, sem simular conversa ou criar uma tela futura. Isso não bloqueia o aceite do dashboard.

## Regras de negócio

R1. Saldo geral = soma de todas as receitas do titular menos soma de todas as despesas do titular em todo o histórico persistido. Não há saldo inicial manual, conciliação bancária ou saldo por múltiplas contas nesta entrega. O seletor de mês não altera o saldo geral.

R2. Receitas e despesas do mês são as somas por tipo das transações cuja data pertence ao mês e ano selecionados. Contagens correspondem à quantidade de transações de cada tipo no período. Resultado do mês = receitas do mês menos despesas do mês.

R3. Iniciar no mês corrente e permitir escolher outro mês e ano. As datas e o mês corrente seguem o mesmo calendário local da gestão de transações. O dashboard não altera datas nem cria registros; somente movimentações realizadas são persistidas conforme a Feature responsável.

R4. O balanço compara receitas e despesas do mês em duas barras, com legenda e valores. A maior soma positiva ocupa a extensão de referência e a outra é proporcional; total zero não causa cálculo inválido. Sem transações no mês, apresentar estado vazio próprio em vez de barras fictícias.

R5. Recentes apresenta os cinco registros mais recentes de todo o histórico, ordenados por data decrescente e depois pelo cadastro mais recente, como na gestão de transações. Com menos de cinco, mostrar somente os existentes. Trocar o mês não filtra essa lista.

R6. Consultas, contagens e totais usam somente transações persistidas do titular. Ao acessar ou atualizar a Visão geral, buscar o estado salvo no sistema. Após concluir operações financeiras iniciadas no dashboard, atualizar seus valores e lista. Esta entrega não define atualização automática contínua entre sessões.

R7. Apresentar valores em reais e datas em formato brasileiro. Distinguir receitas e despesas por identificação, sinal e aparência, mantendo a linguagem visual FinAI. Não usar números de demonstração ou resultados derivados de outro titular.

R8. Preservar a composição #overview do design: cabeçalho, mês, ação Nova transação, três cartões de resumo com destaque no saldo geral, balanço do mês, convite do assistente e últimas movimentações com Ver todas. Usar a base visual aprovada, incluindo claro, escuro e acompanhar o sistema; no celular, adaptar grade, navegação e lista compacta sem perder acesso aos detalhes.

## Dados percebidos pelo usuário

Saldo geral; receitas e despesas do mês com contagens; mês/ano selecionados; barras e legenda; resultado mensal; últimas movimentações com seus campos e sinais; ações para cadastro, detalhes, histórico e assistente quando disponível; estados de carregamento, ausência de registros e falha.

## Critérios de aceite

CA1. Com receitas e despesas em meses diferentes, abrir Visão geral; o saldo geral corresponde à diferença de todo o histórico e os totais/contagens mensais correspondem somente ao mês corrente.

CA2. Selecionar outro mês e ano; atualizar receitas, despesas, contagens, barras e resultado do período, mantendo saldo geral e recentes independentes do filtro mensal.

CA3. Consultar cenário com despesas superiores às receitas; apresentar saldo geral e/ou resultado mensal negativos corretamente. Com valores iguais e positivos, mostrar resultado zero com os registros e barras correspondentes.

CA4. Sem registros, apresentar zeros e orientação de início, sem valores fictícios. Em um mês sem movimento, mas com histórico em outros meses, apresentar somente os indicadores mensais vazios, preservando saldo e recentes do histórico.

CA5. Comparar o gráfico com os totais mensais; legenda, valores e proporções das duas barras correspondem às somas. Um tipo com soma zero e outro positivo continua apresentável; ausência completa de movimentos usa o estado vazio.

CA6. Com mais de cinco registros e datas empatadas, conferir os cinco recentes conforme R5. Com menos registros, não completar a lista com exemplos. Abrir detalhes e Ver todas leva aos dados próprios usando a gestão de transações.

CA7. Cadastrar, editar e excluir uma transação pelas ações disponíveis no dashboard; após cada sucesso, saldo, totais, contagens, barras, resultado e recentes refletem os registros salvos segundo seus respectivos recortes. Cancelamento ou falha não aplica alteração fictícia.

CA8. Provocar falha de consulta; apresentar indisponibilidade e nova tentativa sem afirmar saldo zero ou ausência de registros. Restabelecer a consulta e tentar novamente recupera os valores reais.

CA9. Usar contas com dados distintos; cada uma visualiza somente seus próprios totais, contagens, gráfico e recentes. Visitantes e contas sem confirmação não acessam o dashboard conforme a Feature de acesso.

CA10. Conferir a composição da Visão geral em computador, tablet e celular nos temas claro, escuro e acompanhar o sistema; manter hierarquia, destaque do saldo, cartões, balanço e lista do design. O convite do assistente não simula uma funcionalidade antes da entrega responsável.

## Dependências

Gestão de transações, issue #1016105: fornece os registros pessoais persistidos, suas categorias e as operações de manutenção reutilizadas. Acesso #1016104 e base visual #1016101 são pré-requisitos transitivos, sem relações diretas redundantes. Requisitos publicados não comprovam implementação concluída.

Assistente financeiro é entrega independente após transações. O dashboard conserva seu ponto de entrada visual e habilita a ação quando o assistente estiver disponível; não exige implementar chat ou IA para concluir esta Feature.

## Dentro do escopo

Saldo geral acumulado, receitas/despesas e contagens mensais, seleção de mês, balanço simples e resultado, cinco movimentações recentes, reaproveitamento de cadastro/detalhes/histórico, atualização dos indicadores após manutenção concluída, isolamento por titular e estados descritos, conforme o design.

## Fora do escopo

Saldo inicial manual, integração ou conciliação bancária, múltiplas contas financeiras, gráficos de evolução temporal, relatórios avançados, exportação e filtros analíticos adicionais. Chat, registro por linguagem natural e consultas à IA pertencem à Feature Assistente financeiro. Esta etapa não implementa código nem decompõe tarefas técnicas.
<!-- project-flow:end -->
````

## Atualização posterior — destino e campos

```json
{
  "issue_id": "{{created_issue_id}}",
  "changes": {
    "fixed_version_id": 20355,
    "description": "Descrição integral apresentada a seguir"
  }
}
```

## Descrição integral da publicação final

````markdown
<!-- project-flow:run d346be46-ce4c-418a-a37e-bd652d5d7049 -->
<!-- project-flow:start -->
## Objetivo

Permitir que o titular autenticado e com e-mail confirmado compreenda sua situação financeira pelo saldo geral, totais de receitas e despesas do mês, balanço mensal e movimentações recentes, usando exclusivamente seus registros reais persistidos no sistema.

## Resultado esperado

A Visão geral apresenta números coerentes com as transações do titular, permite consultar outro mês e oferece caminhos para registrar ou consultar movimentações. Valores vazios, negativos e indisponíveis são distinguidos, sem dados fictícios ou de outras contas.

## Atores e permissões

Titular autenticado e confirmado consulta somente os próprios dados. Visitantes e contas sem confirmação seguem as restrições da Feature de acesso. Totais, contagens, gráfico e lista não podem revelar informações de outro titular, inclusive por acesso direto.

## Histórias de usuário

1. Como titular, quero visualizar meu saldo geral para conhecer a diferença acumulada entre receitas e despesas registradas.
2. Como titular, quero consultar receitas, despesas e resultado de um mês para entender aquele período.
3. Como titular, quero ver minhas movimentações mais recentes e abrir seus detalhes ou o histórico completo.
4. Como titular, quero iniciar um registro pelo dashboard e ver meus números atualizados após manter as transações.
5. Como titular sem registros, quero orientação para começar sem confundir ausência de dados com falha de consulta.

## Fluxo principal

1. Abrir Visão geral. Consultar os dados do titular e apresentar saldo geral, receitas do mês e despesas do mês, com suas contagens, iniciando no mês corrente.
2. Apresentar o balanço do mês por duas barras comparativas identificadas como Receitas e Despesas, seus valores, mês de referência e resultado mensal.
3. Selecionar outro mês. Atualizar totais, contagens, gráfico e resultado referentes àquele mês. Manter o saldo geral e as movimentações recentes correspondentes a todo o histórico.
4. Apresentar até cinco movimentações recentes com descrição, categoria, data, valor e identificação de receita/despesa, conforme a composição responsiva do design.
5. Abrir os detalhes de uma movimentação ou Ver todas para acessar o histórico completo do titular. Reutilizar as operações e regras da gestão de transações.
6. Acionar Nova transação, preencher e salvar pela jornada já definida. Após sucesso, atualizar os dados do dashboard. Edição ou exclusão concluída a partir dos detalhes também atualiza os números e a lista.

## Fluxos alternativos e exceções

- Sem registros no histórico, apresentar saldo e totais em R$ 0,00, contagens vazias, orientações e ação para o primeiro cadastro; o gráfico apresenta o estado inicial da referência.
- Com registros no histórico, mas nenhum no mês selecionado, apresentar totais mensais e resultado em zero, contagens vazias e gráfico sem movimento; saldo geral e recentes continuam usando o histórico completo.
- Saldo geral ou resultado mensal negativo é apresentado com valor e sinal corretos, sem limitar o resultado a zero.
- Receitas e despesas positivas de mesmo valor produzem resultado zero, mantendo o gráfico e as contagens de registros existentes; não confundir com mês sem movimentação.
- Falha de consulta apresenta indisponibilidade e caminho de nova tentativa. Não apresentar erro de carregamento como zero, histórico vazio ou números recuperados com sucesso.
- Cancelar ou falhar no cadastro, edição ou exclusão não apresenta novos valores como se a alteração tivesse sido persistida. Após uma alteração concluída, refletir o estado salvo.
- O convite visual para o assistente segue a referência; sua ação só abre o assistente quando essa Feature estiver disponível. Até lá, mantê-la indisponível, sem simular conversa ou criar uma tela futura. Isso não bloqueia o aceite do dashboard.

## Regras de negócio

R1. Saldo geral = soma de todas as receitas do titular menos soma de todas as despesas do titular em todo o histórico persistido. Não há saldo inicial manual, conciliação bancária ou saldo por múltiplas contas nesta entrega. O seletor de mês não altera o saldo geral.

R2. Receitas e despesas do mês são as somas por tipo das transações cuja data pertence ao mês e ano selecionados. Contagens correspondem à quantidade de transações de cada tipo no período. Resultado do mês = receitas do mês menos despesas do mês.

R3. Iniciar no mês corrente e permitir escolher outro mês e ano. As datas e o mês corrente seguem o mesmo calendário local da gestão de transações. O dashboard não altera datas nem cria registros; somente movimentações realizadas são persistidas conforme a Feature responsável.

R4. O balanço compara receitas e despesas do mês em duas barras, com legenda e valores. A maior soma positiva ocupa a extensão de referência e a outra é proporcional; total zero não causa cálculo inválido. Sem transações no mês, apresentar estado vazio próprio em vez de barras fictícias.

R5. Recentes apresenta os cinco registros mais recentes de todo o histórico, ordenados por data decrescente e depois pelo cadastro mais recente, como na gestão de transações. Com menos de cinco, mostrar somente os existentes. Trocar o mês não filtra essa lista.

R6. Consultas, contagens e totais usam somente transações persistidas do titular. Ao acessar ou atualizar a Visão geral, buscar o estado salvo no sistema. Após concluir operações financeiras iniciadas no dashboard, atualizar seus valores e lista. Esta entrega não define atualização automática contínua entre sessões.

R7. Apresentar valores em reais e datas em formato brasileiro. Distinguir receitas e despesas por identificação, sinal e aparência, mantendo a linguagem visual FinAI. Não usar números de demonstração ou resultados derivados de outro titular.

R8. Preservar a composição #overview do design: cabeçalho, mês, ação Nova transação, três cartões de resumo com destaque no saldo geral, balanço do mês, convite do assistente e últimas movimentações com Ver todas. Usar a base visual aprovada, incluindo claro, escuro e acompanhar o sistema; no celular, adaptar grade, navegação e lista compacta sem perder acesso aos detalhes.

## Dados percebidos pelo usuário

Saldo geral; receitas e despesas do mês com contagens; mês/ano selecionados; barras e legenda; resultado mensal; últimas movimentações com seus campos e sinais; ações para cadastro, detalhes, histórico e assistente quando disponível; estados de carregamento, ausência de registros e falha.

## Critérios de aceite

CA1. Com receitas e despesas em meses diferentes, abrir Visão geral; o saldo geral corresponde à diferença de todo o histórico e os totais/contagens mensais correspondem somente ao mês corrente.

CA2. Selecionar outro mês e ano; atualizar receitas, despesas, contagens, barras e resultado do período, mantendo saldo geral e recentes independentes do filtro mensal.

CA3. Consultar cenário com despesas superiores às receitas; apresentar saldo geral e/ou resultado mensal negativos corretamente. Com valores iguais e positivos, mostrar resultado zero com os registros e barras correspondentes.

CA4. Sem registros, apresentar zeros e orientação de início, sem valores fictícios. Em um mês sem movimento, mas com histórico em outros meses, apresentar somente os indicadores mensais vazios, preservando saldo e recentes do histórico.

CA5. Comparar o gráfico com os totais mensais; legenda, valores e proporções das duas barras correspondem às somas. Um tipo com soma zero e outro positivo continua apresentável; ausência completa de movimentos usa o estado vazio.

CA6. Com mais de cinco registros e datas empatadas, conferir os cinco recentes conforme R5. Com menos registros, não completar a lista com exemplos. Abrir detalhes e Ver todas leva aos dados próprios usando a gestão de transações.

CA7. Cadastrar, editar e excluir uma transação pelas ações disponíveis no dashboard; após cada sucesso, saldo, totais, contagens, barras, resultado e recentes refletem os registros salvos segundo seus respectivos recortes. Cancelamento ou falha não aplica alteração fictícia.

CA8. Provocar falha de consulta; apresentar indisponibilidade e nova tentativa sem afirmar saldo zero ou ausência de registros. Restabelecer a consulta e tentar novamente recupera os valores reais.

CA9. Usar contas com dados distintos; cada uma visualiza somente seus próprios totais, contagens, gráfico e recentes. Visitantes e contas sem confirmação não acessam o dashboard conforme a Feature de acesso.

CA10. Conferir a composição da Visão geral em computador, tablet e celular nos temas claro, escuro e acompanhar o sistema; manter hierarquia, destaque do saldo, cartões, balanço e lista do design. O convite do assistente não simula uma funcionalidade antes da entrega responsável.

## Dependências

Gestão de transações, issue #1016105: fornece os registros pessoais persistidos, suas categorias e as operações de manutenção reutilizadas. Acesso #1016104 e base visual #1016101 são pré-requisitos transitivos, sem relações diretas redundantes. Requisitos publicados não comprovam implementação concluída.

Assistente financeiro é entrega independente após transações. O dashboard conserva seu ponto de entrada visual e habilita a ação quando o assistente estiver disponível; não exige implementar chat ou IA para concluir esta Feature.

## Dentro do escopo

Saldo geral acumulado, receitas/despesas e contagens mensais, seleção de mês, balanço simples e resultado, cinco movimentações recentes, reaproveitamento de cadastro/detalhes/histórico, atualização dos indicadores após manutenção concluída, isolamento por titular e estados descritos, conforme o design.

## Fora do escopo

Saldo inicial manual, integração ou conciliação bancária, múltiplas contas financeiras, gráficos de evolução temporal, relatórios avançados, exportação e filtros analíticos adicionais. Chat, registro por linguagem natural e consultas à IA pertencem à Feature Assistente financeiro. Esta etapa não implementa código nem decompõe tarefas técnicas.

## Requisito canônico

Documento aprovado por Mário Tinelli: docs/harness/features/{{created_issue_id}}-dashboard-financeiro/feature.md
<!-- project-flow:end -->
````

## Relação nativa exata e vinculação do ID

```json
[
  {
    "key": "transacoes-blocks-dashboard",
    "payload": {
      "issue_id": 1016105,
      "issue_to_id": "{{created_issue_id}}",
      "relation_type": "blocks"
    }
  }
]
```
