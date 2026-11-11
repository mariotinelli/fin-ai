# [DEV] [WEB] [USUARIO] Assistente financeiro com IA - Consultas financeiras com IA real

- Redmine: `#1016130`
- Tipo: `DEV`
- Tracker: Task (`4`)
- Item pai: `#1016107`
- Estimativa: `6h`

## Descrição

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

<!-- project-slices-child:a091864d75cb2a1c832088b2f1316ad0c7cb8b777433fba17fd99b5d927d322a -->

## Relações

- `#1016129` blocks `#1016130`
- `#1016130` blocks `#1016131`
- `#1016130` blocks `#1016134`
