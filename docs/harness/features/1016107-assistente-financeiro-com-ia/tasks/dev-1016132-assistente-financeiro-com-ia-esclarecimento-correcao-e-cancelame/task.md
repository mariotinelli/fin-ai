# [DEV] [WEB] [USUARIO] Assistente financeiro com IA - Esclarecimento, correção e cancelamento individuais

- Redmine: `#1016132`
- Tipo: `DEV`
- Tracker: Task (`4`)
- Item pai: `#1016107`
- Estimativa: `4h`

## Descrição

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

<!-- project-slices-child:97d8723bccccdf987f4fba28d53f2f7535a5851583474b2e87f0841a46eb98e1 -->

## Relações

- `#1016131` blocks `#1016132`
- `#1016132` blocks `#1016134`
