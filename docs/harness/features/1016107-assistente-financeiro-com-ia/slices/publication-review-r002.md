# Prévia completa — Assistente financeiro com IA

Revisão002, aprovada com correção exclusiva da estimativa de QA. Uma decisão do tech lead cobre o fatiamento, condições e exatamente as operações/vínculos abaixo. Nenhuma filha do Assistente foi criada.

## Entregas e estimativas

Os títulos DEV preservam [DEV] [WEB] [USUARIO] Assistente financeiro com IA - seguido do nome da entrega.

| # | Entrega | Esforço | Bloqueio de início |
| --- | --- | --- | --- |
| 1 | Conversa contínua com histórico salvo | 4h | Nenhum interno; fornecedor #1016117 |
| 2 | Consultas financeiras com IA real | 6h | 1; fornecedor #1016123 |
| 3 | Múltiplas propostas para revisão | 4.5h | 2 |
| 4 | Esclarecimento, correção e cancelamento individuais | 4h | 3 |
| 5 | Confirmação individual sem duplicação | 5.5h | 3 |
| QA | [QA] [WEB] [USUARIO] Assistente financeiro com IA | 3h | Os cinco DEV completos |

Total: **24h DEV + 3h QA = 27h** de esforço, não prazo de calendário.

As capacidades de conversa, IA real e propostas duráveis ainda não existem no código. Os cortes são resultados verificáveis: salvar/retomar mensagens; consultar dados reais com IA; revisar várias propostas; completar/corrigir/cancelar o item correto; confirmar sem duplicação. Não criar tarefas isoladas de SDK,banco ou prompt.

A interpretação de várias propostas foi refinada em duas entregas coerentes para manter a cobertura e o teto6h: revisão inicial das completas com identidade/lacunas das incompletas,e evolução posterior desses itens. As estimativas independentes e a conciliação estão nas decisões,sem copiar durações humanas de outros itens como padrão.

## Dependências e vínculos exatos

- Criar quatro vínculos internos `blocks`: Conversa→Consultas; Consultas→Propostas; Propostas→Esclarecimento/correção/cancelamento; Propostas→Confirmação.
- Confirmação pode iniciar com identidade/estado/versão mínimos fornecidos por Propostas; integra as mudanças de Esclarecimento/correção/cancelamento para concluir seus critérios,sem bloquear artificialmente seu início nessa outra consumidora.
- Criar cinco vínculos dos cinco DEV para a nova QA integrada.
- Criar `blocks` de [QA] [WEB] [USUARIO] Adequação visual do FinAI (#1016117) para o novo DEV Conversa,que pode iniciar sem domínio financeiro depois da fundação verificada.
- Criar `blocks` de [DEV] [WEB] [USUARIO] Gestão de transações - Cadastro de receitas e despesas com conferência do registro (#1016123) para o novo DEV Consultas. Os demais herdam os fornecedores por dependências transitivas,sem arestas duplicadas.
- Os extremos novos são exclusivamente os IDs retornados para estas seis filhas,com os títulos/conteúdo da prévia. Preservar relações Feature→Feature e vínculos alheios.
- Histórico financeiro #1016124 é integração de conclusão do encaminhamento manual; manutenção #1016125 é integração de conclusão do cenário de proposta confirmada após edição/exclusão manual. Não bloqueiam o primeiro histórico ou a integração inicial de consultas. Dashboard não é bloqueador.
- Grafo relevante completo reutilizado da leitura final21issues/23relações; os11vínculos novos não criam ciclos. Após criação,reler grafo antes dos externos. Diferença material exige delta; vincular somente aos IDs retornados já está coberto pela decisão.

## Condições de execução e limites de inspeção

O requisito reserva provedor/modelo/mecanismo à implementação. Não há SDK de IA direto instalado e nenhum teste/serviço real foi chamado nesta preparação; a proposta inclui a primeira integração e não instala dependências agora. Execução e QA exigem serviço de IA real acessível/configurável e condições controladas de falha. Indisponibilidade operacional deve ser registrada,nunca substituída por simulação. As avaliações não identificaram questão técnica concreta que imponha Study antes de definir as entregas; incompatibilidade material futura deve ser avaliada pelo seu impacto.

## Sequencing — regra já autorizada

Campo nativo Sequencing2. Assistente sem filhas permanece vazio até publicar. Depois:mãe#1016107=17;DEV1–DEV5=17,18,19,20,21;QA=22;próximo23. Primeira filha repete a mãe e QA também incrementa.

Aplicar em operação separada somente nesse campo,conferindo o mapa e preservando todos os demais campos e históricos; diferenças materiais por concorrência interrompem para revisão.

## Campos e operações autorizáveis

- Pai nativo#1016107,[WEB] [USUARIO] Assistente financeiro com IA,New preservado.
- Criar cinco TaskDEV(4) e uma DeliverableQA(5),FinAi65224,Sprint120355,sem categoria,responsável ou datas.
- Filhas em New1,prioridade Normal4,com estimated_hours desta prévia.
- Criar/reconciliar nove vínculos internos e dois externos descritos,sem duplicar nem alterar estados de pais/fornecedores.
- Gerar DOCX da fonte aprovada,fazer upload e associá-lo somente à nova QA,preservando demais campos/anexos.
- Aplicar o Sequencing conforme a política já solicitada,sem alteração de conteúdo funcional.
- Pai consultado com children:sem filhas a adotar/excluir. Nenhuma task antiga é contexto/alvo.
- Descrições funcionais abaixo são a autoridade. Após consentimento,helpers vinculam aprovação/documento/IDs e acrescentam seus marcadores técnicos de recuperação,sem nova confirmação equivalente. Mudança material exige outra prévia.

## Documento de condições incluído nesta decisão

DOCX obrigatório e complemento Markdown: slices/condicoes-teste-r002.docx e slices/condicoes-teste-r002.md. Destino [QA] [WEB] [USUARIO] Assistente financeiro com IA,nova filha desta publicação.

Fonte: as40condições integrais desta revisão e seus vínculos ao requisito. O arquivo oficial é gerado após consentimento,o hash dos bytes vinculado ao plano e a associação verificada no readback. A decisão autoriza geração/upload/anexo da mesma fonte,sem editar conteúdo; diferença material pede nova prévia.

## Descrições completas e campos por filha

### [DEV] [WEB] [USUARIO] Assistente financeiro com IA - Conversa contínua com histórico salvo

```json
{
  "project_id": 65224,
  "parent_issue_id": 1016107,
  "tracker_id": 4,
  "status_id": 1,
  "subject": "[DEV] [WEB] [USUARIO] Assistente financeiro com IA - Conversa contínua com histórico salvo",
  "assigned_to_id": null,
  "start_date": null,
  "due_date": null,
  "estimated_hours": 4,
  "priority_id": 4,
  "fixed_version_id": 20355
}
```

## Entrega

Criar a conversa própria contínua, com envio e histórico de mensagens salvo no sistema, ordem/data e retomada automática em outras sessões/navegadores. Entregar uma capacidade de histórico observável sem simular resposta financeira ou produzir lançamentos.

## Escopo e limites

Responsável pela conversa, mensagens, composição e estados de carga/gravação. Respostas reais de IA, cartões/estados específicos de propostas e persistência financeira têm donos nas próximas entregas; histórico salvo não deve ser apresentado como assistente completo ou processamento de IA que nunca termina.

## Critérios de aceite

- Abrir/retomar uma única conversa por usuário, com mensagens diferenciadas por autor em ordem cronológica e data reconhecível; sem seleção de conversas, edição ou exclusão do histórico. Sem mensagens, apresentar acolhimento e sugestões da referência.
- Aceitar envio de mensagem até500caracteres, salvar a mensagem própria e indicar seu processamento real, impedindo novo envio pelo controle enquanto esse processamento ocorre; não inventar resposta nem afirmar que IA atuou quando ainda não há integração disponível.
- Sair,recarregar e abrir outro navegador na mesma conta recupera as mensagens salvas. Propostas e estados produzidos pelos consumidores posteriores devem integrar esse histórico, sem confundir salvamento de mensagem com transação criada.
- Falha ao carregar histórico informa indisponibilidade e nova tentativa, não conversa vazia como sucesso. Falha ao salvar não alega mensagem salva; conservar a ainda não enviada quando aplicável e permitir retomar.
- Somente o titular confirmado acessa a própria conversa/mensagens, inclusive por acesso direto. Visitante e conta não confirmada permanecem restritos.
- Na superfície desta entrega, consumir a base FinAI e a composição #assistant nos temas claro/escuro/sistema e em computador/tablet/celular. Manter autoria das mensagens, campo/guia/sugestões/feedback e controles identificáveis; múltiplos cartões preservam a hierarquia da referência. Não mostrar rótulos de simulação ou armazenamento apenas local.

## Dependências

Início bloqueado por [QA] [WEB] [USUARIO] Adequação visual do FinAI (#1016117), marco da base implementada/verificada. Não depende de persistência financeira para começar. Fornece a conversa usada por Consultas financeiras com IA real e pelas entregas de propostas/estados; integração dessas saídas é necessária ao aceite final do item inteiro.

## Referências

Item pai Redmine #1016107; regras/critérios R6, R11, CA8, CA11-Historico, CA12-Historico, CA14.

- design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; #assistant,#messages,#chat-form,.chat-layout,.message,.chat-compose,sugestões e media queries
- Adaptações aprovadas: IA real, histórico salvo em conversa contínua, múltiplas propostas e confirmação individual; a linguagem visual é preservada.


### [DEV] [WEB] [USUARIO] Assistente financeiro com IA - Consultas financeiras com IA real

```json
{
  "project_id": 65224,
  "parent_issue_id": 1016107,
  "tracker_id": 4,
  "status_id": 1,
  "subject": "[DEV] [WEB] [USUARIO] Assistente financeiro com IA - Consultas financeiras com IA real",
  "assigned_to_id": null,
  "start_date": null,
  "due_date": null,
  "estimated_hours": 6,
  "priority_id": 4,
  "fixed_version_id": 20355
}
```

## Entrega

Entregar a primeira integração real de IA ao usuário por consultas financeiras em linguagem natural, usando a conversa persistida para contexto e os registros atuais do próprio titular. Este é o único dono da integração real reutilizada pelas próximas entregas, não uma tarefa isolada de SDK/provider.

## Escopo e limites

Responsável por interpretar consultas, declarar recortes, obter dados atuais e responder com eles, além de falhas/limites. Não cria ou altera transações, não produz aconselhamento e não substitui IA por respostas simuladas por regras. Provedor/modelo/mecanismo são escolhas de implementação previstas em R1.

## Critérios de aceite

- Consultar saldo geral de todo o histórico e somas/contagens de receitas/despesas por mês,dia,intervalo compreensível e categoria; apresentar período,tipo e categoria usados quando aplicáveis. Listar até cinco recentes e indicar mais correspondências consultáveis no histórico manual.
- Sem período para totais, usar mês corrente declarado; para saldo/recentes sem recorte, usar todo o histórico. Este mês/mês passado seguem calendário local; referências ambíguas pedem esclarecimento, sem inventar valores ou períodos.
- Usar a conversa quando referências forem claras, como “e no mês passado?”, mas buscar valores atuais no sistema. Respostas antigas ficam históricas como foram dadas, com data/posição reconhecível, e não são recalculadas ao reabrir.
- Ausência real de registros é distinta de indisponibilidade. Falha da IA/interpretação orienta tentar novamente ou cadastro manual, sem fabricar resposta ou lançamento; falha de consulta não vira saldo zero ou ausência de dados.
- Consultar não escreve finanças; dados de outro titular e pedidos para ignorar titularidade/confirmação não liberam operação. Pedidos de editar/excluir registros, aconselhamento ou ações fora do escopo recebem orientação e caminho manual aplicável, sem execução pelo chat.
- Mensagens e respostas próprias ficam no histórico contínuo; não usar números somente do texto da conversa como fatos persistidos do sistema.
- Na superfície desta entrega, consumir a base FinAI e a composição #assistant nos temas claro/escuro/sistema e em computador/tablet/celular. Manter autoria das mensagens, campo/guia/sugestões/feedback e controles identificáveis; múltiplos cartões preservam a hierarquia da referência. Não mostrar rótulos de simulação ou armazenamento apenas local.

## Dependências

Início bloqueado por Conversa contínua com histórico salvo e pelo cadastro/persistência de Transações (#1016123). A base visual é transitiva. Para concluir o encaminhamento ao histórico manual, integrar Histórico, filtros e paginação (#1016124), sem bloquear o início dos agregados por essa integração. Fornece a integração real às propostas; Dashboard não é bloqueador.

## Referências

Item pai Redmine #1016107; regras/critérios R1, R7, R8, R9, R10, CA9, CA10, CA11, CA12, CA13, CA14.

- design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; #assistant,query,sugestões,guia,composição,mensagens e estados de processamento/erro
- Adaptações aprovadas: IA real, histórico salvo em conversa contínua, múltiplas propostas e confirmação individual; a linguagem visual é preservada.


### [DEV] [WEB] [USUARIO] Assistente financeiro com IA - Múltiplas propostas para revisão

```json
{
  "project_id": 65224,
  "parent_issue_id": 1016107,
  "tracker_id": 4,
  "status_id": 1,
  "subject": "[DEV] [WEB] [USUARIO] Assistente financeiro com IA - Múltiplas propostas para revisão",
  "assigned_to_id": null,
  "start_date": null,
  "due_date": null,
  "estimated_hours": 4.5,
  "priority_id": 4,
  "fixed_version_id": 20355
}
```

## Entrega

Interpretar várias movimentações de uma mensagem com IA real e apresentar propostas persistidas e distinguíveis com seus cinco campos, data absoluta e estado, permitindo revisar as completas sem criar transações. Manter identidade e lacunas dos itens incompletos para o esclarecimento posterior, sem descartá-los ou inventar dados.

## Escopo e limites

Responsável pela extração inicial, identidade/estado/versão mínimos confiáveis e apresentação das propostas. Esclarecimento, correção e cancelamento pertencem à entrega específica; a criação financeira somente à confirmação individual. Não reconstruir integração de IA nem validações financeiras fornecidas.

## Critérios de aceite

- Mensagem com duas ou mais movimentações identificáveis gera propostas distintas para todos os itens reconhecidos, com tipo,valor,descrição,categoria e data próprios. Nenhum lançamento é criado apenas pelo recebimento/salvamento da mensagem.
- Itens completos são revisáveis e itens incompletos/ambíguos conservam identidade/lacunas sem inventar campos; uma proposta completa não depende de preencher as demais para chegar à confirmação fornecida pela entrega responsável.
- Aplicar regras de Transações: BRL positivo atéR$999.999.999,99 com até duas casas,descrição obrigatória até120,categorias fixas compatíveis e data válida1900atéhoje. Classificação automática é proposta visível e corrigível, não fato incontestável.
- Sem data, propor hoje explicitamente; datas informadas são interpretadas ou marcadas para esclarecimento, sem trocar silenciosamente por hoje. Hoje/ontem tornam-se datas absolutas e permanecem iguais ao reabrir em outro dia.
- Propostas e seus estados ficam vinculados à mensagem/conversa própria e retomam depois. Falha de extração/gravação não fabrica proposta salva ou transação; titular alheio não pode ler os cartões ou seus dados.
- Na superfície desta entrega, consumir a base FinAI e a composição #assistant nos temas claro/escuro/sistema e em computador/tablet/celular. Manter autoria das mensagens, campo/guia/sugestões/feedback e controles identificáveis; múltiplos cartões preservam a hierarquia da referência. Não mostrar rótulos de simulação ou armazenamento apenas local.

## Dependências

Início bloqueado por Consultas financeiras com IA real, que já fornece conversa,integração e dados financeiros necessários por suas dependências. Fornece identidade,estado e versão mínimos para Esclarecimento, correção e cancelamento individuais e Confirmação individual sem duplicação. Não repetir arestas transitivas de conversa/visual/Transações.

## Referências

Item pai Redmine #1016107; regras/critérios R1, R2, R3, R4, R6, CA1, CA3, CA5, CA8, CA12, CA14.

- design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; #assistant,showProposal,completePending,#transaction-dialog e cartões de revisão adaptados para vários itens
- Adaptações aprovadas: IA real, histórico salvo em conversa contínua, múltiplas propostas e confirmação individual; a linguagem visual é preservada.


### [DEV] [WEB] [USUARIO] Assistente financeiro com IA - Esclarecimento, correção e cancelamento individuais

```json
{
  "project_id": 65224,
  "parent_issue_id": 1016107,
  "tracker_id": 4,
  "status_id": 1,
  "subject": "[DEV] [WEB] [USUARIO] Assistente financeiro com IA - Esclarecimento, correção e cancelamento individuais",
  "assigned_to_id": null,
  "start_date": null,
  "due_date": null,
  "estimated_hours": 4,
  "priority_id": 4,
  "fixed_version_id": 20355
}
```

## Entrega

Completar e revisar o item correto entre várias propostas, com perguntas de esclarecimento, edição de campos e cancelamento individual, preservando os demais itens e os estados/versões salvos. A extração inicial já fornece propostas identificáveis, inclusive incompletas.

## Escopo e limites

Responsável pela evolução e invalidação dos estados/versões das propostas, sem criar finanças. Confirmação consome o estado atual; não manter interpretação independente de qual versão está vigente. Não transformar correção de proposta em edição de transação já registrada.

## Critérios de aceite

- Pedir os dados ausentes/ambíguos identificando a proposta; complemento altera somente o item referido e não descarta ou muda os demais. Referências a confirmar/cancelar sem item claro pedem identificação.
- Proposta completa pode seguir independentemente das incompletas. Tipo,valor,descrição,categoria e data sem interpretação segura não são preenchidos como fatos conhecidos.
- Corrigir permite revisar campos na linguagem visual do formulário financeiro e voltar com proposta atualizada ainda sem lançamento. Versão anterior fica não confirmável, inclusive por controles antigos em outra sessão.
- Cancelar somente o item selecionado conserva seu estado cancelado no histórico, sem registro nem cancelamento automático dos demais. Dados inválidos/futuros pedem correção segundo as regras fornecidas.
- Retomar a conversa conserva estado/versão atual e a data absoluta já proposta; não reinterpretar hoje/ontem no novo dia. Falha de mudança não é apresentada como revisão/cancelamento concluído.
- Na superfície desta entrega, consumir a base FinAI e a composição #assistant nos temas claro/escuro/sistema e em computador/tablet/celular. Manter autoria das mensagens, campo/guia/sugestões/feedback e controles identificáveis; múltiplos cartões preservam a hierarquia da referência. Não mostrar rótulos de simulação ou armazenamento apenas local.

## Dependências

Início bloqueado por Múltiplas propostas para revisão. Para concluir o aceite integrado de correção/cancelamento, integrar Confirmação individual sem duplicação, que deve consultar o mesmo estado/versão atual antes de criar finanças. Essa integração de conclusão não gera bloqueio nativo de início entre as duas consumidoras.

## Referências

Item pai Redmine #1016107; regras/critérios R2, R3, R4, R5, R6, CA3, CA4, CA5, CA8, CA14.

- design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; #assistant,completePending,showProposal,cancelProposal,#transaction-dialog e ações dos cartões
- Adaptações aprovadas: IA real, histórico salvo em conversa contínua, múltiplas propostas e confirmação individual; a linguagem visual é preservada.


### [DEV] [WEB] [USUARIO] Assistente financeiro com IA - Confirmação individual sem duplicação

```json
{
  "project_id": 65224,
  "parent_issue_id": 1016107,
  "tracker_id": 4,
  "status_id": 1,
  "subject": "[DEV] [WEB] [USUARIO] Assistente financeiro com IA - Confirmação individual sem duplicação",
  "assigned_to_id": null,
  "start_date": null,
  "due_date": null,
  "estimated_hours": 5.5,
  "priority_id": 4,
  "fixed_version_id": 20355
}
```

## Entrega

Transformar exclusivamente a proposta escolhida e confirmada em uma transação válida do titular, com resultados individuais persistidos e retomada segura. Revalidar dados/estado/versão e impedir repetição, incluindo resultados parciais e falha cujo efeito salvo seja incerto.

## Escopo e limites

Único dono da passagem de proposta confirmada para transação, reutilizando criação e regras de Transações. Não usar salvamento de mensagens, resposta da IA ou confirmação de outro item como autorização. Preservar confirmação histórica mesmo após edição/exclusão manual do registro financeiro.

## Critérios de aceite

- Somente confirmação explícita do titular no controle correspondente pode criar uma transação válida da proposta selecionada. Uma confirmação não autoriza as outras; completas podem ser confirmadas sem completar os demais itens.
- Revalidar os cinco campos,restrições financeiras,data absoluta,estado e versão atuais. Incompleta,inválida,versão substituída,cancelada ou de outro titular não registra e recebe orientação adequada.
- Repetir confirmação,recarregar,reabrir ou usar controle antigo, inclusive em duas sessões, não cria duplicata. A proposta confirmada permanece não registrável mesmo após manutenção manual editar/excluir a transação original.
- Nova mensagem repetindo um gasto só pode criar outro lançamento após nova proposta e confirmação próprias; não registrar automaticamente por igualdade de texto ou pelo contexto de conversa.
- Em várias confirmações individuais, falha de um item conserva sucessos e não confirma os outros. Mostrar resultado de cada um,permitindo retomar somente o que não foi registrado.
- Se o efeito salvo for incerto, informar necessidade de verificação e reconciliar a mesma proposta antes de permitir tentativa que possa duplicar. Falha de leitura não prova ausência de lançamento; não afirmar sucesso ou falha definitiva sem saber o resultado.
- Guardar resultados e estados no histórico contínuo. Consultas/textos pedindo para dispensar confirmação não escrevem finanças e não ultrapassam titularidade. Transações reais ficam disponíveis às consultas do sistema, sem fonte financeira paralela no chat.
- Na superfície desta entrega, consumir a base FinAI e a composição #assistant nos temas claro/escuro/sistema e em computador/tablet/celular. Manter autoria das mensagens, campo/guia/sugestões/feedback e controles identificáveis; múltiplos cartões preservam a hierarquia da referência. Não mostrar rótulos de simulação ou armazenamento apenas local.

## Dependências

Início bloqueado por Múltiplas propostas para revisão, que fornece identidade/estado/versão mínimos e herda conversa,integração e criação financeira #1016123. Para concluir, integrar os estados alterados por Esclarecimento, correção e cancelamento individuais. Edição e exclusão confirmada de Transações (#1016125) é necessária à verificação de manutenção manual posterior; não bloqueia iniciar a confirmação. Dashboard não é necessário.

## Referências

Item pai Redmine #1016107; regras/critérios R2, R3, R4, R5, R5-Confirmacao, R6, R10, CA2, CA4, CA5-Confirmacao, CA6, CA7, CA8, CA12-Propostas, CA14.

- design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; #assistant,showProposal,controles Confirmar/Corrigir/Cancelar e estados individuais persistidos
- Adaptações aprovadas: IA real, histórico salvo em conversa contínua, múltiplas propostas e confirmação individual; a linguagem visual é preservada.


### [QA] [WEB] [USUARIO] Assistente financeiro com IA

```json
{
  "project_id": 65224,
  "parent_issue_id": 1016107,
  "tracker_id": 5,
  "status_id": 1,
  "subject": "[QA] [WEB] [USUARIO] Assistente financeiro com IA",
  "assigned_to_id": null,
  "start_date": null,
  "due_date": null,
  "estimated_hours": 3,
  "priority_id": 4,
  "fixed_version_id": 20355
}
```

## Objetivo

Verificar a conversa contínua com IA real,consultas atuais,múltiplas propostas e confirmação individual segura,com histórico/estados persistidos e titularidade.

## Jornadas integradas

- Conversa contínua própria: Enviar mensagens,sair,recarregar e abrir outro navegador na mesma conta. Resultado esperado: Retomar a mesma conversa,ordem/data/autoria e mensagens salvas;sem várias conversas ou gestão de threads.
- Composição e limite: Usar mensagem válida até500caracteres e observar envio/processamento;conferir campo,sugestões e estados sem atividade falsa de IA. Resultado esperado: Limite aprovado,estado real e controle de envio protegido enquanto processa;sem resposta simulada ou lançamento por salvar mensagem.
- Falha ao salvar mensagem: Provocar falha de gravação e retomar. Resultado esperado: Não alegar salva;conservar mensagem ainda não enviada quando aplicável,com erro/nova tentativa.
- Falha ao carregar histórico: Provocar falha de leitura e restaurar. Resultado esperado: Indisponibilidade não é conversa vazia;retomada recupera histórico real.
- Autoria e data históricas: Retomar mensagens próprias/do assistente e comparar ordem e data. Resultado esperado: Autoria distinguível,ordem cronológica e contexto histórico reconhecível,sem recalcular respostas antigas.
- Integração real de IA: Com serviço real configurado,fazer consulta compreensível e enviar movimentações;conferir as respostas/propostas resultantes e evidência da integração. Resultado esperado: Interpretação usa IA real;protótipo por regras não é entregue como integração;falhas não geram resultados fictícios.
- Saldo real: Com valores conhecidos no sistema e números conflitantes apenas em mensagens,perguntar saldo geral. Resultado esperado: Usar todo histórico real do titular,não números ditos na conversa ou exemplos.
- Período,categoria e contagens: Consultar receitas/despesas por este mês,mês passado,dia/intervalo explícito compreensível e categoria com massa conhecida. Resultado esperado: Somas,contagens e registros corretos;recorte/tipo/categoria declarados quando aplicáveis.
- Recortes padrão: Pedir totais sem período e saldo/recentes sem outro recorte. Resultado esperado: Totais usam mês corrente declarado;saldo/recentes usam todo histórico.
- Ambiguidade de consulta: Pedir recorte ou referência sem interpretação segura. Resultado esperado: Solicitar esclarecimento em vez de inventar período/valores.
- Recentes e histórico manual: Com mais de cinco correspondências,pedir últimas movimentações. Resultado esperado: Até cinco registros reais e indicação dos demais consultáveis no histórico manual.
- Contexto e dados atualizados: Consultar,usar “e no mês passado?”,alterar dados manualmente e consultar de novo;reabrir conversa. Resultado esperado: Contexto claro é entendido;consulta nova usa dados atuais;respostas antigas permanecem como dadas e reconhecíveis por posição/data.
- Sem dados e falha de consulta: Consultar recorte sem registros e depois provocar falha de consulta. Resultado esperado: Ausência real distinguida de indisponibilidade;falha nunca vira saldo zero ou dado inexistente fabricado.
- Falha de IA/interpretação: Indisponibilizar o serviço ou fornecer resposta não interpretável e restaurar. Resultado esperado: Orientar nova tentativa/cadastro manual,sem inventar resposta ou criar finança.
- Limites de ação: Pedir edição/exclusão de transações,aconselhamento ou outra ação fora da Feature. Resultado esperado: Explicar limite e jornada manual aplicável,sem executar a ação no chat.
- Várias propostas completas: Enviar mensagem com duas ou mais movimentações identificáveis. Resultado esperado: Propostas distintas,cinco campos e estados próprios,sem transações antes de confirmar.
- Lote completo/incompleto: Enviar um item completo e outro incompleto/ambíguo. Resultado esperado: Conservar todos os itens identificáveis;pergunta aponta o item certo e o completo pode seguir independentemente.
- Validações dos campos: Usar tipo/valor/descrição/categoria/data fora das regras financeiras,com fronteiras de valor/duas casas/120caracteres/1900atéhoje. Resultado esperado: Não registrar inválido;apresentar lacuna/correção sem inventar campos e reutilizar regras/categorias compatíveis.
- Data ausente e explícita: Enviar sem data e com uma data explícita válida ou inválida. Resultado esperado: Ausente propõe hoje declarado;informada é interpretada ou esclarecida,nunca trocada silenciosamente por hoje.
- Hoje/ontem e retomada: Criar propostas com hoje/ontem e reabrir em outro dia. Resultado esperado: Exibir e manter datas absolutas já propostas;revalidar no confirmar sem reinterpretar o texto pelo novo dia.
- Completar o item correto: Responder aos dados faltantes de um item entre vários. Resultado esperado: Alterar somente aquele,sem descartar/modificar demais;dados sem certeza pedem esclarecimento.
- Corrigir campos e versão: Corrigir proposta e tentar seus controles antigos em outra sessão. Resultado esperado: Proposta nova ainda não é transação;versão anterior não confirmável,e confirmar depois usa os campos revisados.
- Cancelar individualmente: Cancelar um item entre vários e reabrir o histórico. Resultado esperado: Apenas ele cancelado e sem lançamento;demais mantidos,e estado cancelado persiste.
- Referência ambígua a ação: Pedir confirmar/cancelar sem identificar o item quando houver várias propostas. Resultado esperado: Pedir identificação;nenhum cancelamento/registro indevido ou confirmação automática de lote.
- Retomar todos os estados: Salvar mensagens/propostas pendentes,corrigidas,canceladas/confirmadas e retomar em outro navegador. Resultado esperado: Mesma conversa e estados atuais;pendentes sem efeito financeiro,sem reativar antigos ou reinterpretar datas.
- Confirmar somente uma: Entre propostas completas/incompletas,confirmar uma completa. Resultado esperado: Exatamente sua transação;demais continuam sem efeito financeiro,e confirmar outras depois cria somente as correspondentes.
- Revalidar no confirmar: Tentar confirmar proposta incompleta/inválida ou alterada antes da confirmação. Resultado esperado: Impedir e orientar correção;verificar campos,data,estado/versão atuais sem efeito indevido.
- Repetição e sessões: Confirmar,repetir,recaregar/reabrir e usar controles antigos, inclusive por duas sessões. Resultado esperado: Uma transação por proposta,sem duplicar por repetição ou reabertura.
- Versão antiga ou cancelada: Confirmar depois de corrigir/cancelar a proposta,usando versão anterior. Resultado esperado: Recusar estado/versão inválidos;somente proposta vigente e explicitamente confirmada pode criar.
- Manutenção manual posterior: Confirmar,depois editar/excluir manualmente sua transação,e usar botão antigo no histórico. Resultado esperado: Estado confirmado permanece;não recriar o registro pelo controle histórico.
- Nova mensagem igual: Enviar novamente o mesmo texto de gasto após uma confirmação. Resultado esperado: Novo registro somente por nova proposta e confirmação próprias,sem criação automática por igualdade de texto.
- Resultados parciais: Confirmar itens individualmente e provocar falha em um deles. Resultado esperado: Sucessos mantidos,resultado por item claro,demais não confirmados automaticamente;retomar apenas o não registrado.
- Falha conhecida ao persistir: Falhar confirmação sem registro e restaurar para nova tentativa válida. Resultado esperado: Sem sucesso fictício;erro do item identificável e uma transação após concluir a retomada.
- Efeito incerto com registro salvo: Após persistir,perder resposta de confirmação e tentar retomar. Resultado esperado: Verificar/reconciliar a mesma proposta antes de nova tentativa,não duplicar e reconhecer confirmação existente.
- Efeito incerto sem registro: Interromper operação antes de salvar e recuperar seu resultado de forma verificável antes de retentar. Resultado esperado: Não alegar resultado definitivo sem saber;somente após reconciliação permitir retomar sem duplicação.Falha de leitura não prova ausência.
- Histórico alheio: Como B,tentar conversa/mensagens de A por acesso direto. Resultado esperado: Não ler ou usar dados/mensagens alheias na resposta.
- Consulta alheia ou dispensa de regras: Pedir dados de outra conta ou mandar ignorar validação/confirmação/titularidade. Resultado esperado: Não revelar nem alterar dados;consulta não cria finanças e texto do usuário/IA não dispensa as regras.
- Ações em proposta alheia: Como B,tentar consultar,corrigir,cancelar/confirmar proposta de A por acesso direto. Resultado esperado: Não expor nem modificar indevidamente;nenhuma transação alheia criada.
- Visitante e não-confirmado: Abrir chat,consultas,propostas e confirmações sem sessão ou e-mail confirmado. Resultado esperado: Restringir acesso conforme a jornada de conta,sem dados expostos ou registros.
- Chat e cartões responsivos: Comparar com design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md (#assistant,.chat-layout,.message,composer,sugestões,guia e cartões adaptados),em computador/tablet/celular,claro/escuro/sistema,com estados variados. Resultado esperado: Autoria/hierarquia/identidade preservadas,controles distinguem o item correto,composição utilizável sem rótulos de simulação/armazenamento local.

## Regras e permissões

- Mensagem salva não é transação;cada proposta precisa de sua confirmação explícita,campos válidos e estado/versão atuais.
- Conversa e dados são só do titular confirmado;consultas/textos da IA ou do usuário não dispensam validação ou permitem escrever finanças indevidas.
- Retomada preserva histórico,data absoluta e estados;repetição,correção/cancelamento e manutenção manual posterior não reativam registros já concluídos.
- Respostas novas consultam dados atuais;antigas ficam históricas;falha/ausência e resultado incerto são distinguidos,sem fabricar valores ou provas de ausência.

## Impactos relacionados

- Consumir criação/validações e histórico/manutenção de Transações nos pontos de integração,sem refazer toda a QA dos fornecedores.
- Conferir efeitos entre várias propostas e entre sessões,não apenas o botão visível no navegador.
- Usar a base visual e testar a composição nova do chat e cartões;Dashboard não é pré-requisito.

## Critérios de conclusão

- Executar CT-001 aCT-040 da revisão aprovada,registrando dados/contexto,resultado observado e evidência por condição.
- Confirmar jornadas integradas,reais e de falha,inclusive reconciliação e titularidade;reportar desvios/impedimentos sem declarar aprovação de condição não executada.
- Manter o DOCX da revisão associado à QA e registrar preparação,resultados e reteste delimitado conforme execução.

## Referências

Item pai Redmine #1016107; regras/critérios R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, CA1, CA2, CA3, CA4, CA5, CA6, CA7, CA8, CA9, CA10, CA11, CA12, CA13, CA14, R5-Confirmacao, CA5-Confirmacao, CA11-Historico, CA12-Historico, CA12-Propostas.


## Condições de teste integrais

# Condições de teste

## Contexto

Titulares A/B confirmados,visitante e conta não confirmada; duas sessões/navegadores; serviço de IA real acessível e respostas/falhas controláveis onde necessário. Preparar dados financeiros conhecidos em períodos/categorias distintos, lotes completos/incompletos/inválidos, datas locais e relógio controlável, proposta corrigida/cancelada/confirmada e falhas com resultado conhecido/incerto. Fornecedores financeiros e visual devem estar disponíveis para o aceite. Não há suíte de assistente pronta presumida; resultados/evidências serão produzidos na execução posterior, com impedimentos explícitos.

## Histórico

### CT-001 — Conversa contínua própria

Verificação: Enviar mensagens,sair,recarregar e abrir outro navegador na mesma conta.

Resultado esperado: Retomar a mesma conversa,ordem/data/autoria e mensagens salvas;sem várias conversas ou gestão de threads.

Origem no requisito: R6: Manter uma única conversa contínua por usuário, sem lista de conversas nem ação de iniciar outra conversa. Persistir mensagens, respostas, propostas e seus estados para retomada em sessões e navegadores posteriores da mesma conta. Não incluir edição ou exclusão do histórico nesta entrega.; CA8: Sair, recarregar e acessar por outro navegador na mesma conta; recuperar a mesma conversa contínua, mensagens e propostas com seus estados. Propostas pendentes continuam sem persistência financeira e não há criação/seleção de conversas separadas.

### CT-002 — Composição e limite

Verificação: Usar mensagem válida até500caracteres e observar envio/processamento;conferir campo,sugestões e estados sem atividade falsa de IA.

Resultado esperado: Limite aprovado,estado real e controle de envio protegido enquanto processa;sem resposta simulada ou lançamento por salvar mensagem.

Origem no requisito: R6: Manter uma única conversa contínua por usuário, sem lista de conversas nem ação de iniciar outra conversa. Persistir mensagens, respostas, propostas e seus estados para retomada em sessões e navegadores posteriores da mesma conta. Não incluir edição ou exclusão do histórico nesta entrega.; R11: A tela segue #assistant do design, com mensagens diferenciadas por autor, campo de composição, processamento, sugestões e guia de uso. Adaptar os cartões de proposta para vários itens e manter histórico salvo sem substituir a linguagem visual. Remover rótulos de assistente simulado e armazenamento apenas local. Conservar claro, escuro e acompanhar o sistema, com composição adaptada a celular, tablet e computador.; CA14: Utilizar chat, sugestões, composição, esclarecimentos e múltiplos cartões em computador, tablet e celular, nos temas claro, escuro e acompanhar o sistema; preservar a identidade e hierarquia do design, estados distinguíveis e controles correspondentes ao item correto, sem rótulos de simulação.

### CT-003 — Falha ao salvar mensagem

Verificação: Provocar falha de gravação e retomar.

Resultado esperado: Não alegar salva;conservar mensagem ainda não enviada quando aplicável,com erro/nova tentativa.

Origem no requisito: CA11-Historico: Desdobramento de CA11: falha de gravação/carga de histórico não equivale a conversa salva/vazia.

### CT-004 — Falha ao carregar histórico

Verificação: Provocar falha de leitura e restaurar.

Resultado esperado: Indisponibilidade não é conversa vazia;retomada recupera histórico real.

Origem no requisito: CA11-Historico: Desdobramento de CA11: falha de gravação/carga de histórico não equivale a conversa salva/vazia.; CA8: Sair, recarregar e acessar por outro navegador na mesma conta; recuperar a mesma conversa contínua, mensagens e propostas com seus estados. Propostas pendentes continuam sem persistência financeira e não há criação/seleção de conversas separadas.

### CT-005 — Autoria e data históricas

Verificação: Retomar mensagens próprias/do assistente e comparar ordem e data.

Resultado esperado: Autoria distinguível,ordem cronológica e contexto histórico reconhecível,sem recalcular respostas antigas.

Origem no requisito: R6: Manter uma única conversa contínua por usuário, sem lista de conversas nem ação de iniciar outra conversa. Persistir mensagens, respostas, propostas e seus estados para retomada em sessões e navegadores posteriores da mesma conta. Não incluir edição ou exclusão do histórico nesta entrega.; R9: Novas consultas podem usar a conversa para compreender referências como “e no mês passado?”, mas precisam consultar os dados financeiros atuais. Respostas antigas permanecem no histórico como foram dadas e não são recalculadas ao reabrir; a posição/data da mensagem permite reconhecê-las como históricas. Solicitar novamente produz resposta baseada nos dados atuais.; R11: A tela segue #assistant do design, com mensagens diferenciadas por autor, campo de composição, processamento, sugestões e guia de uso. Adaptar os cartões de proposta para vários itens e manter histórico salvo sem substituir a linguagem visual. Remover rótulos de assistente simulado e armazenamento apenas local. Conservar claro, escuro e acompanhar o sistema, com composição adaptada a celular, tablet e computador.; CA8: Sair, recarregar e acessar por outro navegador na mesma conta; recuperar a mesma conversa contínua, mensagens e propostas com seus estados. Propostas pendentes continuam sem persistência financeira e não há criação/seleção de conversas separadas.

## Consultas reais

### CT-006 — Integração real de IA

Verificação: Com serviço real configurado,fazer consulta compreensível e enviar movimentações;conferir as respostas/propostas resultantes e evidência da integração.

Resultado esperado: Interpretação usa IA real;protótipo por regras não é entregue como integração;falhas não geram resultados fictícios.

Origem no requisito: R1: A integração usa IA real para interpretar e responder; o assistente simulado por regras do protótipo não atende a esta entrega. Escolha de provedor, modelo e mecanismo de integração pertence à implementação, sem alterar os resultados e limites definidos aqui.; CA9: Consultar saldo geral, receitas/despesas por mês, dia ou intervalo compreensível, categoria e recentes; valores, contagens e registros correspondem ao sistema, com recortes declarados. Sem período para totais, usar mês corrente declarado; sem recorte para saldo/recentes, usar todo o histórico.; CA1: Enviar uma mensagem com duas ou mais movimentações identificáveis; receber propostas distintas, com tipo, valor, descrição, categoria e data próprios, sem transações persistidas antes de confirmar.

### CT-007 — Saldo real

Verificação: Com valores conhecidos no sistema e números conflitantes apenas em mensagens,perguntar saldo geral.

Resultado esperado: Usar todo histórico real do titular,não números ditos na conversa ou exemplos.

Origem no requisito: R7: Consultas suportam saldo geral acumulado, somas e contagens de receitas/despesas por período e categoria e movimentações recentes correspondentes. O saldo geral considera todo o histórico; consultas com este mês ou mês passado usam esses meses de calendário; datas e intervalos explícitos são usados quando compreensíveis, e ambiguidades são esclarecidas. Para listagens recentes, mostrar até cinco registros e indicar quando houver mais correspondências consultáveis no histórico manual.; R8: Perguntas de despesa/receita sem período informado usam o mês corrente como recorte declarado, conforme a referência. Saldo geral e últimas movimentações sem outro recorte consideram todo o histórico. Respostas indicam período, categoria e tipo usados quando aplicáveis, para o usuário compreender o que foi consultado. Valores e contagens vêm de registros persistidos, nunca de exemplos ou apenas das mensagens da conversa.; CA9: Consultar saldo geral, receitas/despesas por mês, dia ou intervalo compreensível, categoria e recentes; valores, contagens e registros correspondem ao sistema, com recortes declarados. Sem período para totais, usar mês corrente declarado; sem recorte para saldo/recentes, usar todo o histórico.

### CT-008 — Período,categoria e contagens

Verificação: Consultar receitas/despesas por este mês,mês passado,dia/intervalo explícito compreensível e categoria com massa conhecida.

Resultado esperado: Somas,contagens e registros corretos;recorte/tipo/categoria declarados quando aplicáveis.

Origem no requisito: R7: Consultas suportam saldo geral acumulado, somas e contagens de receitas/despesas por período e categoria e movimentações recentes correspondentes. O saldo geral considera todo o histórico; consultas com este mês ou mês passado usam esses meses de calendário; datas e intervalos explícitos são usados quando compreensíveis, e ambiguidades são esclarecidas. Para listagens recentes, mostrar até cinco registros e indicar quando houver mais correspondências consultáveis no histórico manual.; R8: Perguntas de despesa/receita sem período informado usam o mês corrente como recorte declarado, conforme a referência. Saldo geral e últimas movimentações sem outro recorte consideram todo o histórico. Respostas indicam período, categoria e tipo usados quando aplicáveis, para o usuário compreender o que foi consultado. Valores e contagens vêm de registros persistidos, nunca de exemplos ou apenas das mensagens da conversa.; CA9: Consultar saldo geral, receitas/despesas por mês, dia ou intervalo compreensível, categoria e recentes; valores, contagens e registros correspondem ao sistema, com recortes declarados. Sem período para totais, usar mês corrente declarado; sem recorte para saldo/recentes, usar todo o histórico.

### CT-009 — Recortes padrão

Verificação: Pedir totais sem período e saldo/recentes sem outro recorte.

Resultado esperado: Totais usam mês corrente declarado;saldo/recentes usam todo histórico.

Origem no requisito: R8: Perguntas de despesa/receita sem período informado usam o mês corrente como recorte declarado, conforme a referência. Saldo geral e últimas movimentações sem outro recorte consideram todo o histórico. Respostas indicam período, categoria e tipo usados quando aplicáveis, para o usuário compreender o que foi consultado. Valores e contagens vêm de registros persistidos, nunca de exemplos ou apenas das mensagens da conversa.; CA9: Consultar saldo geral, receitas/despesas por mês, dia ou intervalo compreensível, categoria e recentes; valores, contagens e registros correspondem ao sistema, com recortes declarados. Sem período para totais, usar mês corrente declarado; sem recorte para saldo/recentes, usar todo o histórico.

### CT-010 — Ambiguidade de consulta

Verificação: Pedir recorte ou referência sem interpretação segura.

Resultado esperado: Solicitar esclarecimento em vez de inventar período/valores.

Origem no requisito: R7: Consultas suportam saldo geral acumulado, somas e contagens de receitas/despesas por período e categoria e movimentações recentes correspondentes. O saldo geral considera todo o histórico; consultas com este mês ou mês passado usam esses meses de calendário; datas e intervalos explícitos são usados quando compreensíveis, e ambiguidades são esclarecidas. Para listagens recentes, mostrar até cinco registros e indicar quando houver mais correspondências consultáveis no histórico manual.; CA9: Consultar saldo geral, receitas/despesas por mês, dia ou intervalo compreensível, categoria e recentes; valores, contagens e registros correspondem ao sistema, com recortes declarados. Sem período para totais, usar mês corrente declarado; sem recorte para saldo/recentes, usar todo o histórico.

### CT-011 — Recentes e histórico manual

Verificação: Com mais de cinco correspondências,pedir últimas movimentações.

Resultado esperado: Até cinco registros reais e indicação dos demais consultáveis no histórico manual.

Origem no requisito: R7: Consultas suportam saldo geral acumulado, somas e contagens de receitas/despesas por período e categoria e movimentações recentes correspondentes. O saldo geral considera todo o histórico; consultas com este mês ou mês passado usam esses meses de calendário; datas e intervalos explícitos são usados quando compreensíveis, e ambiguidades são esclarecidas. Para listagens recentes, mostrar até cinco registros e indicar quando houver mais correspondências consultáveis no histórico manual.; CA9: Consultar saldo geral, receitas/despesas por mês, dia ou intervalo compreensível, categoria e recentes; valores, contagens e registros correspondem ao sistema, com recortes declarados. Sem período para totais, usar mês corrente declarado; sem recorte para saldo/recentes, usar todo o histórico.

### CT-012 — Contexto e dados atualizados

Verificação: Consultar,usar “e no mês passado?”,alterar dados manualmente e consultar de novo;reabrir conversa.

Resultado esperado: Contexto claro é entendido;consulta nova usa dados atuais;respostas antigas permanecem como dadas e reconhecíveis por posição/data.

Origem no requisito: R9: Novas consultas podem usar a conversa para compreender referências como “e no mês passado?”, mas precisam consultar os dados financeiros atuais. Respostas antigas permanecem no histórico como foram dadas e não são recalculadas ao reabrir; a posição/data da mensagem permite reconhecê-las como históricas. Solicitar novamente produz resposta baseada nos dados atuais.; CA10: Fazer referência ao período de uma pergunta anterior; interpretar o contexto quando claro e consultar os dados atuais. Alterar transações manualmente e perguntar novamente produz números atualizados; respostas antigas no histórico permanecem como foram dadas.

### CT-013 — Sem dados e falha de consulta

Verificação: Consultar recorte sem registros e depois provocar falha de consulta.

Resultado esperado: Ausência real distinguida de indisponibilidade;falha nunca vira saldo zero ou dado inexistente fabricado.

Origem no requisito: R7: Consultas suportam saldo geral acumulado, somas e contagens de receitas/despesas por período e categoria e movimentações recentes correspondentes. O saldo geral considera todo o histórico; consultas com este mês ou mês passado usam esses meses de calendário; datas e intervalos explícitos são usados quando compreensíveis, e ambiguidades são esclarecidas. Para listagens recentes, mostrar até cinco registros e indicar quando houver mais correspondências consultáveis no histórico manual.; CA11: Consultar recorte sem registros; informar ausência real de dados. Provocar falha na IA, consulta ou histórico; apresentar o erro correspondente e nova tentativa sem fabricar valores, alegar histórico vazio/salvo indevidamente ou criar transações.

### CT-014 — Falha de IA/interpretação

Verificação: Indisponibilizar o serviço ou fornecer resposta não interpretável e restaurar.

Resultado esperado: Orientar nova tentativa/cadastro manual,sem inventar resposta ou criar finança.

Origem no requisito: R1: A integração usa IA real para interpretar e responder; o assistente simulado por regras do protótipo não atende a esta entrega. Escolha de provedor, modelo e mecanismo de integração pertence à implementação, sem alterar os resultados e limites definidos aqui.; CA11: Consultar recorte sem registros; informar ausência real de dados. Provocar falha na IA, consulta ou histórico; apresentar o erro correspondente e nova tentativa sem fabricar valores, alegar histórico vazio/salvo indevidamente ou criar transações.

### CT-015 — Limites de ação

Verificação: Pedir edição/exclusão de transações,aconselhamento ou outra ação fora da Feature.

Resultado esperado: Explicar limite e jornada manual aplicável,sem executar a ação no chat.

Origem no requisito: R10: Consultar dados não cria nem altera transações. Texto de mensagens, respostas da IA ou pedidos para ignorar regras não dispensam confirmação, validação ou titularidade. Mensagens e propostas de outro titular não podem ser expostas ou utilizadas na resposta.; CA13: Pedir edição/exclusão de registros ou ação fora do escopo; orientar os limites e a jornada manual aplicável, sem executar a operação pelo chat.

## Propostas e revisão

### CT-016 — Várias propostas completas

Verificação: Enviar mensagem com duas ou mais movimentações identificáveis.

Resultado esperado: Propostas distintas,cinco campos e estados próprios,sem transações antes de confirmar.

Origem no requisito: R2: Uma mensagem pode gerar várias propostas de transação. Cada proposta tem revisão, confirmação, correção, cancelamento e resultado próprios. Nenhuma é persistida sem confirmação explícita do titular no controle correspondente. Uma confirmação não autoriza outras propostas.; CA1: Enviar uma mensagem com duas ou mais movimentações identificáveis; receber propostas distintas, com tipo, valor, descrição, categoria e data próprios, sem transações persistidas antes de confirmar.

### CT-017 — Lote completo/incompleto

Verificação: Enviar um item completo e outro incompleto/ambíguo.

Resultado esperado: Conservar todos os itens identificáveis;pergunta aponta o item certo e o completo pode seguir independentemente.

Origem no requisito: R2: Uma mensagem pode gerar várias propostas de transação. Cada proposta tem revisão, confirmação, correção, cancelamento e resultado próprios. Nenhuma é persistida sem confirmação explícita do titular no controle correspondente. Uma confirmação não autoriza outras propostas.; CA3: Enviar uma movimentação incompleta ou ambígua junto de outra completa; o assistente identifica a qual item se refere a pergunta, atualiza somente esse item e permite revisar a proposta completa sem exigir o preenchimento das demais.

### CT-018 — Validações dos campos

Verificação: Usar tipo/valor/descrição/categoria/data fora das regras financeiras,com fronteiras de valor/duas casas/120caracteres/1900atéhoje.

Resultado esperado: Não registrar inválido;apresentar lacuna/correção sem inventar campos e reutilizar regras/categorias compatíveis.

Origem no requisito: R3: Tipo, valor, descrição, categoria e data seguem integralmente as regras de Gestão de transações #1016105: valores em reais positivos até R$ 999.999.999,99 com até duas casas; descrição obrigatória até 120 caracteres; categorias predefinidas compatíveis com o tipo; data válida entre 01/01/1900 e hoje; somente movimentações realizadas. A classificação automática é uma proposta visível, sujeita a correção e confirmação.; CA5: Informar valores, descrições, tipos, categorias ou datas fora de R3; impedir registro e solicitar correção. Mensagem sem data propõe hoje explicitamente; mensagem com data futura pede correção. Reabrir em outro dia conserva a data absoluta previamente proposta.

### CT-019 — Data ausente e explícita

Verificação: Enviar sem data e com uma data explícita válida ou inválida.

Resultado esperado: Ausente propõe hoje declarado;informada é interpretada ou esclarecida,nunca trocada silenciosamente por hoje.

Origem no requisito: R4: A falta de data assume hoje como proposta; referências explícitas devem ser interpretadas ou esclarecidas, sem substituir silenciosamente uma data informada por hoje. Propostas salvas retêm sua data absoluta ao reabrir a conversa, sem reinterpretar hoje/ontem com o novo dia. Campos são revalidados ao confirmar.; CA5: Informar valores, descrições, tipos, categorias ou datas fora de R3; impedir registro e solicitar correção. Mensagem sem data propõe hoje explicitamente; mensagem com data futura pede correção. Reabrir em outro dia conserva a data absoluta previamente proposta.

### CT-020 — Hoje/ontem e retomada

Verificação: Criar propostas com hoje/ontem e reabrir em outro dia.

Resultado esperado: Exibir e manter datas absolutas já propostas;revalidar no confirmar sem reinterpretar o texto pelo novo dia.

Origem no requisito: R4: A falta de data assume hoje como proposta; referências explícitas devem ser interpretadas ou esclarecidas, sem substituir silenciosamente uma data informada por hoje. Propostas salvas retêm sua data absoluta ao reabrir a conversa, sem reinterpretar hoje/ontem com o novo dia. Campos são revalidados ao confirmar.; CA5: Informar valores, descrições, tipos, categorias ou datas fora de R3; impedir registro e solicitar correção. Mensagem sem data propõe hoje explicitamente; mensagem com data futura pede correção. Reabrir em outro dia conserva a data absoluta previamente proposta.; CA5-Confirmacao: Desdobramento de CA5/R3/R4: revalidar todos os campos e data absoluta no ato de confirmar.

### CT-021 — Completar o item correto

Verificação: Responder aos dados faltantes de um item entre vários.

Resultado esperado: Alterar somente aquele,sem descartar/modificar demais;dados sem certeza pedem esclarecimento.

Origem no requisito: CA3: Enviar uma movimentação incompleta ou ambígua junto de outra completa; o assistente identifica a qual item se refere a pergunta, atualiza somente esse item e permite revisar a proposta completa sem exigir o preenchimento das demais.; R2: Uma mensagem pode gerar várias propostas de transação. Cada proposta tem revisão, confirmação, correção, cancelamento e resultado próprios. Nenhuma é persistida sem confirmação explícita do titular no controle correspondente. Uma confirmação não autoriza outras propostas.

### CT-022 — Corrigir campos e versão

Verificação: Corrigir proposta e tentar seus controles antigos em outra sessão.

Resultado esperado: Proposta nova ainda não é transação;versão anterior não confirmável,e confirmar depois usa os campos revisados.

Origem no requisito: R5: Propostas corrigidas invalidam a possibilidade de confirmar versões anteriores. Propostas confirmadas ou canceladas mantêm seu estado no histórico. Uma transação já confirmada e posteriormente editada ou excluída manualmente não pode ser recriada pelo botão antigo da conversa.; CA4: Corrigir uma proposta e depois confirmar; persistir os campos revisados, com a versão anterior indisponível para confirmação. Cancelar uma proposta não registra nem cancela as outras.

### CT-023 — Cancelar individualmente

Verificação: Cancelar um item entre vários e reabrir o histórico.

Resultado esperado: Apenas ele cancelado e sem lançamento;demais mantidos,e estado cancelado persiste.

Origem no requisito: R2: Uma mensagem pode gerar várias propostas de transação. Cada proposta tem revisão, confirmação, correção, cancelamento e resultado próprios. Nenhuma é persistida sem confirmação explícita do titular no controle correspondente. Uma confirmação não autoriza outras propostas.; R5: Propostas corrigidas invalidam a possibilidade de confirmar versões anteriores. Propostas confirmadas ou canceladas mantêm seu estado no histórico. Uma transação já confirmada e posteriormente editada ou excluída manualmente não pode ser recriada pelo botão antigo da conversa.; CA4: Corrigir uma proposta e depois confirmar; persistir os campos revisados, com a versão anterior indisponível para confirmação. Cancelar uma proposta não registra nem cancela as outras.

### CT-024 — Referência ambígua a ação

Verificação: Pedir confirmar/cancelar sem identificar o item quando houver várias propostas.

Resultado esperado: Pedir identificação;nenhum cancelamento/registro indevido ou confirmação automática de lote.

Origem no requisito: R2: Uma mensagem pode gerar várias propostas de transação. Cada proposta tem revisão, confirmação, correção, cancelamento e resultado próprios. Nenhuma é persistida sem confirmação explícita do titular no controle correspondente. Uma confirmação não autoriza outras propostas.; CA3: Enviar uma movimentação incompleta ou ambígua junto de outra completa; o assistente identifica a qual item se refere a pergunta, atualiza somente esse item e permite revisar a proposta completa sem exigir o preenchimento das demais.; CA4: Corrigir uma proposta e depois confirmar; persistir os campos revisados, com a versão anterior indisponível para confirmação. Cancelar uma proposta não registra nem cancela as outras.

## Confirmação e retomada

### CT-025 — Retomar todos os estados

Verificação: Salvar mensagens/propostas pendentes,corrigidas,canceladas/confirmadas e retomar em outro navegador.

Resultado esperado: Mesma conversa e estados atuais;pendentes sem efeito financeiro,sem reativar antigos ou reinterpretar datas.

Origem no requisito: R6: Manter uma única conversa contínua por usuário, sem lista de conversas nem ação de iniciar outra conversa. Persistir mensagens, respostas, propostas e seus estados para retomada em sessões e navegadores posteriores da mesma conta. Não incluir edição ou exclusão do histórico nesta entrega.; CA8: Sair, recarregar e acessar por outro navegador na mesma conta; recuperar a mesma conversa contínua, mensagens e propostas com seus estados. Propostas pendentes continuam sem persistência financeira e não há criação/seleção de conversas separadas.

### CT-026 — Confirmar somente uma

Verificação: Entre propostas completas/incompletas,confirmar uma completa.

Resultado esperado: Exatamente sua transação;demais continuam sem efeito financeiro,e confirmar outras depois cria somente as correspondentes.

Origem no requisito: R2: Uma mensagem pode gerar várias propostas de transação. Cada proposta tem revisão, confirmação, correção, cancelamento e resultado próprios. Nenhuma é persistida sem confirmação explícita do titular no controle correspondente. Uma confirmação não autoriza outras propostas.; CA2: Confirmar somente uma proposta entre várias; criar exatamente sua transação e manter as outras sem efeito financeiro. Confirmar as demais individualmente cria somente os registros correspondentes.

### CT-027 — Revalidar no confirmar

Verificação: Tentar confirmar proposta incompleta/inválida ou alterada antes da confirmação.

Resultado esperado: Impedir e orientar correção;verificar campos,data,estado/versão atuais sem efeito indevido.

Origem no requisito: R3: Tipo, valor, descrição, categoria e data seguem integralmente as regras de Gestão de transações #1016105: valores em reais positivos até R$ 999.999.999,99 com até duas casas; descrição obrigatória até 120 caracteres; categorias predefinidas compatíveis com o tipo; data válida entre 01/01/1900 e hoje; somente movimentações realizadas. A classificação automática é uma proposta visível, sujeita a correção e confirmação.; R4: A falta de data assume hoje como proposta; referências explícitas devem ser interpretadas ou esclarecidas, sem substituir silenciosamente uma data informada por hoje. Propostas salvas retêm sua data absoluta ao reabrir a conversa, sem reinterpretar hoje/ontem com o novo dia. Campos são revalidados ao confirmar.; CA5-Confirmacao: Desdobramento de CA5/R3/R4: revalidar todos os campos e data absoluta no ato de confirmar.

### CT-028 — Repetição e sessões

Verificação: Confirmar,repetir,recaregar/reabrir e usar controles antigos, inclusive por duas sessões.

Resultado esperado: Uma transação por proposta,sem duplicar por repetição ou reabertura.

Origem no requisito: R5-Confirmacao: Desdobramento de R5: confirmar observa versão/estado atual e não recria transação já confirmada depois de manutenção manual.; CA6: Repetir a confirmação, reabrir o histórico ou usar controle antigo de proposta confirmada/cancelada; não criar nova transação. Isso também vale se o registro original tiver sido editado ou excluído manualmente depois.

### CT-029 — Versão antiga ou cancelada

Verificação: Confirmar depois de corrigir/cancelar a proposta,usando versão anterior.

Resultado esperado: Recusar estado/versão inválidos;somente proposta vigente e explicitamente confirmada pode criar.

Origem no requisito: R5: Propostas corrigidas invalidam a possibilidade de confirmar versões anteriores. Propostas confirmadas ou canceladas mantêm seu estado no histórico. Uma transação já confirmada e posteriormente editada ou excluída manualmente não pode ser recriada pelo botão antigo da conversa.; R5-Confirmacao: Desdobramento de R5: confirmar observa versão/estado atual e não recria transação já confirmada depois de manutenção manual.; CA6: Repetir a confirmação, reabrir o histórico ou usar controle antigo de proposta confirmada/cancelada; não criar nova transação. Isso também vale se o registro original tiver sido editado ou excluído manualmente depois.

### CT-030 — Manutenção manual posterior

Verificação: Confirmar,depois editar/excluir manualmente sua transação,e usar botão antigo no histórico.

Resultado esperado: Estado confirmado permanece;não recriar o registro pelo controle histórico.

Origem no requisito: R5-Confirmacao: Desdobramento de R5: confirmar observa versão/estado atual e não recria transação já confirmada depois de manutenção manual.; CA6: Repetir a confirmação, reabrir o histórico ou usar controle antigo de proposta confirmada/cancelada; não criar nova transação. Isso também vale se o registro original tiver sido editado ou excluído manualmente depois.

### CT-031 — Nova mensagem igual

Verificação: Enviar novamente o mesmo texto de gasto após uma confirmação.

Resultado esperado: Novo registro somente por nova proposta e confirmação próprias,sem criação automática por igualdade de texto.

Origem no requisito: R2: Uma mensagem pode gerar várias propostas de transação. Cada proposta tem revisão, confirmação, correção, cancelamento e resultado próprios. Nenhuma é persistida sem confirmação explícita do titular no controle correspondente. Uma confirmação não autoriza outras propostas.; CA2: Confirmar somente uma proposta entre várias; criar exatamente sua transação e manter as outras sem efeito financeiro. Confirmar as demais individualmente cria somente os registros correspondentes.; CA6: Repetir a confirmação, reabrir o histórico ou usar controle antigo de proposta confirmada/cancelada; não criar nova transação. Isso também vale se o registro original tiver sido editado ou excluído manualmente depois.

### CT-032 — Resultados parciais

Verificação: Confirmar itens individualmente e provocar falha em um deles.

Resultado esperado: Sucessos mantidos,resultado por item claro,demais não confirmados automaticamente;retomar apenas o não registrado.

Origem no requisito: CA7: Confirmar várias propostas individualmente e provocar falha em uma; manter os resultados já concluídos, informar qual item falhou e permitir retomar somente o que não foi registrado. Se houver incerteza sobre o efeito salvo, reconciliar a mesma proposta antes de uma nova tentativa que possa duplicá-la.

### CT-033 — Falha conhecida ao persistir

Verificação: Falhar confirmação sem registro e restaurar para nova tentativa válida.

Resultado esperado: Sem sucesso fictício;erro do item identificável e uma transação após concluir a retomada.

Origem no requisito: CA7: Confirmar várias propostas individualmente e provocar falha em uma; manter os resultados já concluídos, informar qual item falhou e permitir retomar somente o que não foi registrado. Se houver incerteza sobre o efeito salvo, reconciliar a mesma proposta antes de uma nova tentativa que possa duplicá-la.

### CT-034 — Efeito incerto com registro salvo

Verificação: Após persistir,perder resposta de confirmação e tentar retomar.

Resultado esperado: Verificar/reconciliar a mesma proposta antes de nova tentativa,não duplicar e reconhecer confirmação existente.

Origem no requisito: CA7: Confirmar várias propostas individualmente e provocar falha em uma; manter os resultados já concluídos, informar qual item falhou e permitir retomar somente o que não foi registrado. Se houver incerteza sobre o efeito salvo, reconciliar a mesma proposta antes de uma nova tentativa que possa duplicá-la.; CA6: Repetir a confirmação, reabrir o histórico ou usar controle antigo de proposta confirmada/cancelada; não criar nova transação. Isso também vale se o registro original tiver sido editado ou excluído manualmente depois.

### CT-035 — Efeito incerto sem registro

Verificação: Interromper operação antes de salvar e recuperar seu resultado de forma verificável antes de retentar.

Resultado esperado: Não alegar resultado definitivo sem saber;somente após reconciliação permitir retomar sem duplicação.Falha de leitura não prova ausência.

Origem no requisito: CA7: Confirmar várias propostas individualmente e provocar falha em uma; manter os resultados já concluídos, informar qual item falhou e permitir retomar somente o que não foi registrado. Se houver incerteza sobre o efeito salvo, reconciliar a mesma proposta antes de uma nova tentativa que possa duplicá-la.

## Permissões e visual

### CT-036 — Histórico alheio

Verificação: Como B,tentar conversa/mensagens de A por acesso direto.

Resultado esperado: Não ler ou usar dados/mensagens alheias na resposta.

Origem no requisito: CA12-Historico: Desdobramento de CA12: somente o próprio titular acessa sua conversa e mensagens.; R10: Consultar dados não cria nem altera transações. Texto de mensagens, respostas da IA ou pedidos para ignorar regras não dispensam confirmação, validação ou titularidade. Mensagens e propostas de outro titular não podem ser expostas ou utilizadas na resposta.

### CT-037 — Consulta alheia ou dispensa de regras

Verificação: Pedir dados de outra conta ou mandar ignorar validação/confirmação/titularidade.

Resultado esperado: Não revelar nem alterar dados;consulta não cria finanças e texto do usuário/IA não dispensa as regras.

Origem no requisito: R10: Consultar dados não cria nem altera transações. Texto de mensagens, respostas da IA ou pedidos para ignorar regras não dispensam confirmação, validação ou titularidade. Mensagens e propostas de outro titular não podem ser expostas ou utilizadas na resposta.; CA12: Tentar consultar ou confirmar propostas/transações de outra conta, inclusive por acesso direto, ou pedir para ignorar confirmação e titularidade; não expor dados nem registrar indevidamente. Visitantes e contas não confirmadas não acessam o assistente.

### CT-038 — Ações em proposta alheia

Verificação: Como B,tentar consultar,corrigir,cancelar/confirmar proposta de A por acesso direto.

Resultado esperado: Não expor nem modificar indevidamente;nenhuma transação alheia criada.

Origem no requisito: CA12-Propostas: Desdobramento de CA12/R10: titularidade e confirmação obrigatórias também por acesso direto às propostas/ações.; R10: Consultar dados não cria nem altera transações. Texto de mensagens, respostas da IA ou pedidos para ignorar regras não dispensam confirmação, validação ou titularidade. Mensagens e propostas de outro titular não podem ser expostas ou utilizadas na resposta.

### CT-039 — Visitante e não-confirmado

Verificação: Abrir chat,consultas,propostas e confirmações sem sessão ou e-mail confirmado.

Resultado esperado: Restringir acesso conforme a jornada de conta,sem dados expostos ou registros.

Origem no requisito: CA12: Tentar consultar ou confirmar propostas/transações de outra conta, inclusive por acesso direto, ou pedir para ignorar confirmação e titularidade; não expor dados nem registrar indevidamente. Visitantes e contas não confirmadas não acessam o assistente.; CA12-Historico: Desdobramento de CA12: somente o próprio titular acessa sua conversa e mensagens.; CA12-Propostas: Desdobramento de CA12/R10: titularidade e confirmação obrigatórias também por acesso direto às propostas/ações.

### CT-040 — Chat e cartões responsivos

Verificação: Comparar com design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md (#assistant,.chat-layout,.message,composer,sugestões,guia e cartões adaptados),em computador/tablet/celular,claro/escuro/sistema,com estados variados.

Resultado esperado: Autoria/hierarquia/identidade preservadas,controles distinguem o item correto,composição utilizável sem rótulos de simulação/armazenamento local.

Origem no requisito: R11: A tela segue #assistant do design, com mensagens diferenciadas por autor, campo de composição, processamento, sugestões e guia de uso. Adaptar os cartões de proposta para vários itens e manter histórico salvo sem substituir a linguagem visual. Remover rótulos de assistente simulado e armazenamento apenas local. Conservar claro, escuro e acompanhar o sistema, com composição adaptada a celular, tablet e computador.; CA14: Utilizar chat, sugestões, composição, esclarecimentos e múltiplos cartões em computador, tablet e celular, nos temas claro, escuro e acompanhar o sistema; preservar a identidade e hierarquia do design, estados distinguíveis e controles correspondentes ao item correto, sem rótulos de simulação.

## Cobertura, inspeção e estimativas

A tabela completa está em [slices.md](slices.md). Desdobramentos de R5/CA5/CA11/CA12 explicitam os mesmos critérios entre histórico,consulta e confirmação,sem requisito novo. A integração real e a persistência da conversa têm donos únicos; consumidoras compartilham estados e regras em vez de duplicá-los.

- Escopo vem do requisito aprovado #1016107 e decisões Q10–Q12: várias propostas,confirmação individual,histórico salvo e conversa contínua. Nenhuma task antiga é contexto ou capacidade pronta.
- Inspeção de código,dependências diretas e protótipo confirma ausência de assistente real. Existem autenticação,componentes e fornecedores financeiros com dono,mas New não significa implementado. Nenhum teste ou chamada a serviço de IA foi executado nesta preparação; nenhuma dependência foi instalada.
- Avaliação independente A, estimate_visual_delivery: história3h,consultas5,5h,propostas/revisão agregadas5,5h,confirmação4,5h,QA5,5h. No refinamento de propostas:extração/revisão inicial3h e esclarecimento/correção/cancelamento3h,nova análise de escopos em lugar de divisão aritmética.
- Avaliação independente B, estimate_visual_reuse: história4h,consultas6h,propostas agregadas8,5h refinadas em4,5h+4h,confirmação5,5h,QA6h. Cada avaliação recebeu requisito/evidência sem estimativa candidata ou números da outra.
- Histórico da primeira proposta — estimativas do agente principal: história4h (primeira conversa persistida/UI/retomada/erros),consultas6h (primeira integração real,contexto,dados atuais e falhas),propostas4,5h (extração múltipla,estado inicial confiável e cartões),esclarecimento/correção/cancelamento4h (associação ao item,versões e retomada),confirmação5,5h (revalidação,efeitos individuais,antirrepetição e resultado incerto),QA6h (serviço/dados/falhas,contexto,lotes/estados,sessões,titularidade e visual). Total24h DEV+6h QA=30h. Não é média automática,desconto por IA ou tempo executado.
- Calibrações humanas anteriores são referências específicas,não medidas: visualDEV2h/QA1,5h;acesso1,5/2/2h eQA1h;transaçõesDEV2h eQA1,5h. Dashboardaceito4,5h/QA2,5h também não inclui a primeira integração real ou propostas duráveis. Nenhuma dessas horas foi copiada automaticamente como padrão.
- Refinar propostas em duas entregas de resultado observável conserva a experiência e o teto6h: revisão das completas com identidade/lacunas;depois complemento/correção/cancelamento. Não descartar incompletas na extração inicial. Não criar tarefa isolada de banco,SDK,provider ou prompt.
- Bloqueios internos reais:1→2→3;3→4 e3→5. Confirmação pode iniciar com identidade/estado/versão mínimos de3 e integra4 para concluir. QAaguarda os cincoDEV. Externos específicos:QAvisual#1016117→conversa1 eTxcadastro#1016123→consultas2. Demais fornecedores transitivos não recebem arestas redundantes.
- Histórico financeiro#1016124 é integração de conclusão das consultas/encaminhamento manual;manutenção#1016125 é integração de conclusão do cenário proposta confirmada seguida de edição/exclusão manual. Dashboardnão é bloqueador e seus agregados não são dados prontos presumidos.
- Sem pergunta técnica demonstrada que impeça cortes completos,não abrir Study só por ausência de SDK/provedor escolhido. R1 reserva escolha à implementação. A execução exige acesso configurável a IA real e ambiente de teste; indisponibilidade impede aquela integração/verificação,não autoriza simulação. Incompatibilidade concreta futura deve ser avaliada com seu impacto,se surgir.
- IDs R1–R11/CA1–CA14 preservados. Desdobramentos R5/CA5/CA11/CA12 explicitam confirmação,histórico e titularidade por domínio,sem requisito novo. Todas as capacidades do assistente são create; reuso de base não muda essa classificação.
- Sequencing já autorizado: próximo17; após publicar,mãeAssistente17,DEV1–DEV5 em17–21 eQA22,próximo23. Até ter filhas,o pai permanece vazio. Reaplicar a regra ao conjunto sem reescrever históricos,alterando somente custom field2 e verificando demais campos.
- Publicação proposta: cincoTaskDEV e umaDeliverableQA,New/Normal,pai1016107,versãoSprint1,sem responsável/datas; nove vínculos internos e dois externos conforme a prévia e IDs retornados. Gerar/upload/anexar DOCX à novaQA. Não alterar estado de pais/fornecedores ou relações anteriores.
- Decisão explícita de Mário Tinelli nesta conversa: aceita as estimativas DEV por ser algo realmente novo e exigir bastante teste;corrige somente QA de6h para3h e autoriza publicar. DEV permanece24h,QA3h,total27h. É calibração humana e consentimento de publicação da prévia completa com essa correção,sem reduzir conteúdo,cobertura,40condições ou dependências.
