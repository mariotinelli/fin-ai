# [QA] [WEB] [USUARIO] Assistente financeiro com IA

- Redmine: `#1016134`
- Tipo: `QA`
- Tracker: Deliverable (`5`)
- Item pai: `#1016107`
- Estimativa: `3h`

## Descrição

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

<!-- project-slices-child:c4d232c7047fda97838d782efc9ff0e34d30279357a5bce9df59012c25b3b61d -->

## Relações

- `#1016129` blocks `#1016134`
- `#1016130` blocks `#1016134`
- `#1016131` blocks `#1016134`
- `#1016132` blocks `#1016134`
- `#1016133` blocks `#1016134`
