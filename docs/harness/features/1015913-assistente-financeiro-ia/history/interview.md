# Entrevista — Assistente financeiro com IA

Item 4/4 do catálogo aprovado: chat com IA real, identificação de informações, complementação de campos faltantes, registro com confirmação e consultas reais por usuário. Dependência direta Gestão de transações #1015911; dashboard #1015912 já publicado, sem novo bloqueio de catálogo. Design somente visual, não autoriza assistente simulado.

## Rodada 1

Q13 — Quando a mensagem não informar data, propor hoje (Brasília), mostrando a data para revisão antes da confirmação, ou sempre perguntar? Recomenda-se propor hoje para reduzir uma etapa, mantendo correção e confirmação explícitas. Exemplo: Gastei 35 no almoço.

Q14 — Mensagem com várias movimentações: permitir interpretar e revisar cada uma separadamente ou pedir ao usuário que envie uma por vez? Recomenda-se uma por vez no MVP para manter complementação e confirmação inequívocas. Exemplo: Gastei 35 no almoço e 20 no transporte. Nenhuma gravação ocorre enquanto não houver uma proposta válida confirmada.

Próximas decisões materiais: escopo de consultas e períodos, proposta/correção/cancelamento, persistência da conversa e tratamento de ambiguidades/indisponibilidade. Não antecipar respostas. Provedor, modelo e mecanismos de integração pertencem à implementação.


## Resposta à rodada 1

Usuário: “pode ser”. Q13 e Q14 resolvidas conforme recomendações apresentadas: hoje em Brasília quando não houver data, com revisão antes de confirmar; uma movimentação por vez, pedindo envio separado ao identificar várias. Não se presume gravação parcial de uma mensagem com várias movimentações.

## Rodada 2 — consultas e conversa

Q15 — Proposta de consultas: saldo geral; receitas e despesas por período e categoria; lista de movimentações por período, tipo e categoria; lista de agendadas quando solicitada. Períodos: hoje, ontem, este mês, mês passado e datas/intervalos explícitos. Respostas identificam período e filtros; agendadas não entram como realizadas. Confirmar conjunto ou indicar outra consulta necessária. Recomendação cobre os critérios de sucesso sem análises ou recomendações financeiras avançadas.

Q16 — Histórico do chat: salvar uma conversa contínua por usuário para reaparecer após sair e voltar, ou iniciar conversa vazia a cada acesso? Recomenda-se salvar para permitir consultar o que foi conversado. Transações persistem em qualquer opção. Salvar não implica múltiplas conversas ou retomada automática de proposta pendente; esse comportamento será definido após a escolha.

Pendências posteriores: confirmação, correção/cancelamento, ambiguidades, consulta sem período, proposta pendente, falhas e retomada conforme Q16. Recomendações não substituem respostas.


## Resposta à rodada 2

Usuário: “pode ser”. Q15 e Q16 resolvidas conforme recomendações: conjunto de consultas e períodos propostos; conversa contínua salva por usuário. Não pressupõe múltiplas conversas nem confirmação automática ao retomar.

## Rodada 3 — confirmação e retomada

Q17 — Proposta completa mostra tipo, valor, descrição, categoria e data, com ações Confirmar, Corrigir e Cancelar. Recomenda-se confirmar somente pelo botão da proposta atual; mensagem “sim” orienta usar o botão, sem gravar. Correção altera os campos e exige nova revisão/confirmar; confirmação repetida não duplica o registro. Alternativa: aceitar confirmação textual inequívoca, exigindo definir como vinculá-la à proposta atual.

Q18 — Recomenda-se manter a proposta pendente ao sair, sem gravar. Ao voltar, mostrar novamente os dados e exigir confirmação; uma data já proposta fica fixa (não muda para o novo hoje). Se a coleta estiver incompleta, continuar pedindo os campos faltantes. Alternativa: cancelar o registro em preparação ao sair, mantendo apenas as mensagens e exigindo um novo pedido.

Pendências para próxima rodada ou proposta final: consultas sem período, categoria ambígua e interpretação insegura, ações enquanto há proposta pendente, indisponibilidade e correção de transações já registradas. Não inventar confirmação para essas escolhas.


## Resposta à rodada 3

Usuário: “pode ser”. Q17 e Q18 resolvidas conforme recomendações: confirmar apenas pelo botão da proposta atual, corrigir e revisar novamente, cancelar sem gravar, não duplicar confirmação repetida; preservar registro em preparação e data fixada ao sair, retomando sem gravação automática.

## Rodada 4 — consultas e proposta pendente

Q19 — Para consulta sem período, recomendar este mês para totais e listagens, declarando o período na resposta; saldo geral continua todo o histórico até hoje, e pedido explícito de todo o histórico é respeitado. Listagem de agendadas sem período considera todas as futuras. Alternativa: perguntar o período antes de responder a totais/listagens sem período.

Q20 — Com registro em preparação, recomendar permitir consultas financeiras sem perder a proposta, mas pedir que confirme ou cancele antes de iniciar outro registro. Mensagens ambíguas pedem esclarecimento e não sobrescrevem a proposta. Alternativa: exigir concluir ou cancelar antes de qualquer consulta. A capacidade de uma movimentação por vez permanece.

As propostas de tratamento de interpretação insegura, falhas e dados reais serão apresentadas com os critérios de aceite na revisão final. Nenhuma decisão desta rodada foi presumida.


## Resposta à rodada 4 e revisão

Usuário: “concordo”. Q19 e Q20 resolvidas conforme recomendações. Requisito completo preparado. Detalhes de correção em formulário, listas de dez registros, ambiguidades, falhas e limites são propostas explícitas na revisão, não respostas inventadas. Busca completa na Sprint 1: #1015909, #1015911 e #1015912, sem demanda equivalente ao assistente. Sem categorias. Sequencing 4 = baseline 0 + posição 4. Plano inclui #1015911 blocks nova issue. Nenhuma mutação remota.


Requisito e operações aprovados pelo usuário: “aprovado”. Consentimento registrado em 2026-11-04T20:18:37.834848+00:00.


Publicacao concluida: #1015913, Sprint 1, Sequencing 4, status New. Conteudo integral e relacao blocks #1015911 -> #1015913 (765) validados.
