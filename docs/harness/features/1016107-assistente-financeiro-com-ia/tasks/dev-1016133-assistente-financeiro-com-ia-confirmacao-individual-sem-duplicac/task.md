# [DEV] [WEB] [USUARIO] Assistente financeiro com IA - Confirmação individual sem duplicação

- Redmine: `#1016133`
- Tipo: `DEV`
- Tracker: Task (`4`)
- Item pai: `#1016107`
- Estimativa: `5.5h`

## Descrição

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

<!-- project-slices-child:1b22c0ba55601fe82805e8b873b7dcd5aec22692e568ba8d8d23f503927502b5 -->

## Relações

- `#1016131` blocks `#1016133`
- `#1016133` blocks `#1016134`
