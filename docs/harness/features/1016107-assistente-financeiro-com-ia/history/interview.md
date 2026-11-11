# Histórico da entrevista — Assistente financeiro com IA

## Contexto herdado e passagem de contexto

Item 5: [WEB] [USUARIO] Assistente financeiro com IA. Titular confirmado usa chat com IA real para registrar receitas/despesas e consultar dados reais, somente da própria conta. Sempre revisar e confirmar antes de persistir; corrigir, cancelar e completar informações. Não incluir edição/exclusão por IA, aconselhamento, automações ou múltiplos agentes, conforme o catálogo aprovado.

Dependência direta: transações #1016105. Base visual #1016101 e acesso #1016104 são transitivos. Dashboard #1016106 é consumidor independente; não bloqueia o assistente. Os requisitos estão publicados, sem presumir implementação. Ignorar todas as tasks antigas.

Reutilizar respostas: persistência no sistema e IA real; contas individuais; confirmação obrigatória do e-mail; categorias fixas aprovadas; registros somente realizados, sem data futura; validações financeiras da Feature de transações; claro/escuro/sistema. O chat do design fornece composição, sugestões, processamento, confirmação/correção/cancelamento e consultas exemplificadas, mas usa regras simuladas e mensagens não persistidas. A IA real substitui essa simulação, conforme decisão do usuário.

### Q10 — Quantidade de transações por mensagem

Contexto: o escopo prevê registro por conversa; o design apresenta uma proposta por vez, mas não define a resposta para uma mensagem que descreva vários gastos.
Por que importa: define se há revisão individual simples ou lote com múltiplas confirmações e estados.
Pergunta: no MVP, trabalhar com uma transação por vez e solicitar que separe mensagens com vários registros, ou interpretar vários registros na mesma mensagem?
Opções: A — uma por vez, com orientação para separar; B — várias na mesma mensagem, com revisão e confirmação individual de cada uma.
Recomendação: A, por corresponder à proposta única do design e manter a primeira integração básica de IA.
Resposta: aguardando usuário.
Estado: bloqueante.

### Q11 — Histórico das conversas

Contexto: todas as transações devem ser persistidas, mas o escopo não diz se mensagens do chat também devem ser guardadas. O protótipo não retém as mensagens após recarregar a página.
Por que importa: define se o usuário pode reabrir a conversa ao voltar ao sistema; não muda a persistência obrigatória das transações confirmadas.
Pergunta: salvar o histórico de mensagens para retomar depois ou manter a conversa apenas enquanto a tela estiver aberta?
Opções: A — conversa temporária, como no protótipo; B — histórico salvo e retomável pelo próprio titular.
Recomendação: A, para manter o limite do protótipo e não ampliar persistência de conversas sem demanda. Transações confirmadas continuam sempre salvas no sistema.
Resposta: aguardando usuário.
Estado: bloqueante.

## Pontos a reconciliar após esta rodada

Consultas por saldo, receitas/despesas, categoria, período e últimas movimentações; períodos ambíguos e ausência de dados; data omitida e interpretação de hoje/ontem; categoria desconhecida ou ambígua; invalidação de propostas anteriores, repetição de confirmação e falhas do serviço/consulta/persistência. Reutilizar a proposta do design onde clara, pedir decisões somente quando necessárias. Escolha de modelo/provedor e mecanismo de integração ficam para implementação.


## Resolução de Q10 e Q11

Resposta exata do usuário: “q10. aceitar varias e confirmar q11. salvar historico”.

Q10 resolvida: aceitar várias transações por mensagem com revisão e confirmação individual, como na alternativa B apresentada. Cada proposta é identificável, revisável e confirmável; nenhuma é persistida apenas pelo recebimento da mensagem. Q11 resolvida: manter histórico de mensagens salvo para o próprio titular retomar depois, como na alternativa B. Recomendações iniciais de proposta única e conversa temporária não foram adotadas.

Adaptações do protótipo: múltiplas propostas e persistência das mensagens devem preservar a linguagem visual do chat. Não mudam título, público, dependências ou limite da capacidade do catálogo; detalham o registro e a conversa já previstos. Uma proposta completa pode ser confirmada sem aguardar completar as demais, pois as confirmações são individuais. Propostas confirmadas não podem registrar novamente ao reabrir o histórico; as ainda não confirmadas permanecem sem efeito financeiro.

### Q12 — Organização do histórico salvo

Contexto: Q11 confirmou salvar as mensagens; o design tem uma única tela de conversa e não mostra uma lista de conversas separadas.
Por que importa: define o que a pessoa encontra ao voltar ao assistente e se pode iniciar ou alternar entre conversas distintas.
Pergunta: manter uma conversa contínua por usuário, retomada automaticamente, ou oferecer várias conversas separadas com escolha de qual abrir?
Opções: A — histórico único contínuo, sem seleção de conversas; B — várias conversas, com iniciar nova e escolher uma anterior.
Recomendação: A, pois permite retomar o histórico com a mesma composição do design, sem acrescentar uma gestão de conversas ao MVP.
Resposta: aguardando usuário.
Estado: bloqueante.

## Regras a consolidar na prévia após Q12

Preservar propostas e seu estado no histórico; mostrar as datas absolutas interpretadas, sem reinterpretar hoje/ontem ao reabrir; validar novamente os campos ao confirmar; não duplicar propostas já confirmadas nem transformar reenvio/reabertura em autorização. Tratar confirmações e falhas por proposta com resultados visíveis. Proposta incompleta pede informações referentes ao item correto. Persistência de mensagens e transações são distintas: uma mensagem salva nunca equivale a transação criada. Consultas usam os dados atuais do sistema; respostas antigas preservadas são histórico, não consulta atualizada automaticamente. Não solicitar escolhas técnicas de modelo, provedor ou armazenamento.


## Resolução de Q12 e fechamento da entrevista

Resposta exata do usuário: “conversar continua”. Q12 resolvida: uma única conversa contínua por usuário, retomada automaticamente, sem criar ou escolher conversas separadas.

Q10, Q11 e Q12 resolvidas. Não restam perguntas materiais abertas. A proposta integral consolida confirmações individuais de várias transações, propostas incompletas e resultados parciais, correção/cancelamento, retomada de estados sem duplicação, consultas atuais e respostas históricas preservadas, falhas e titularidade. Data ausente assume hoje como na referência, mas deve ser exibida como data absoluta para confirmação; datas futuras seguem recusadas. Categoria deve ser válida e apresentada, pedindo esclarecimento se não houver classificação segura. Essas regras constarão na prévia para aprovação, sem atribuí-las a respostas inexistentes.

Adaptações de múltiplas propostas e histórico salvo cabem na capacidade conversacional aprovada, sem nova Feature, mudança de público, título ou dependência. Proposta de publicação: Sequencing 5 pela posição do catálogo, respeitando a exceção já aprovada de desconsiderar tasks antigas. Relação direta transacoes-blocks-assistente, partindo da #1016105; dashboard não é dependência.


## Prévia pronta para revisão

Q10, Q11 e Q12 resolvidas. Requisito, plano e todas as seções funcionais da criação/publicação comparados integralmente. Prévia inclui histórico contínuo salvo, múltiplas propostas e estados, confirmação individual, consultas reais, falhas e a relação transacoes-blocks-assistente. Estado validado; aguardando aprovação única. Nenhuma mutação remota executada neste item.


## Aprovação e publicação concluídas

O usuário aprovou a prévia integral. Consentimento único registrado para requisito e plano, com criação, publicação e relação transacoes-blocks-assistente. Criada #1016107, Sprint 1, Sequencing 5, estado New preservado. Conteúdo integral conferido pelo checker funcional; relação 838 (#1016105 blocks #1016107) confirmada em ambos os extremos. Requisito concluído não significa implementação concluída. Baseline de comparação normaliza apenas CRLF/LF no conteúdo funcional, preservando a resposta original.
