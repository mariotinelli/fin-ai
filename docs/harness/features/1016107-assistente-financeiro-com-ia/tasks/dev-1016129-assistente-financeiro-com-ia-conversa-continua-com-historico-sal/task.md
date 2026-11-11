# [DEV] [WEB] [USUARIO] Assistente financeiro com IA - Conversa contínua com histórico salvo

- Redmine: `#1016129`
- Tipo: `DEV`
- Tracker: Task (`4`)
- Item pai: `#1016107`
- Estimativa: `4h`

## Descrição

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

<!-- project-slices-child:84026106c66b9e502ad98b072331b2a4a0e5fd4c254f1d490aa267e96c4717bf -->

## Relações

- `#1016129` blocks `#1016130`
- `#1016129` blocks `#1016134`
