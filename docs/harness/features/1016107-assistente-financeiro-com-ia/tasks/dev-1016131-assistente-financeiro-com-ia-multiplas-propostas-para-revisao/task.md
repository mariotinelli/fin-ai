# [DEV] [WEB] [USUARIO] Assistente financeiro com IA - Múltiplas propostas para revisão

- Redmine: `#1016131`
- Tipo: `DEV`
- Tracker: Task (`4`)
- Item pai: `#1016107`
- Estimativa: `4.5h`

## Descrição

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

<!-- project-slices-child:73fdde6db6e2d9e07b763ac9df3384ebc48ffff4aae243ecc8354be27ba03d89 -->

## Relações

- `#1016130` blocks `#1016131`
- `#1016131` blocks `#1016132`
- `#1016131` blocks `#1016133`
- `#1016131` blocks `#1016134`
