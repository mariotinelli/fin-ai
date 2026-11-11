# Fatiamento de [WEB] [USUARIO] Assistente financeiro com IA

Revisão: 2  
Hash: `08943b208fd4499cd0ba96eb892048ba5da3e55215864f30b8434b4f51afe257`

## Prévia numerada

1. **[DEV] [WEB] [USUARIO] Assistente financeiro com IA - Conversa contínua com histórico salvo** — 4h
   - Entrega: Criar a conversa própria contínua, com envio e histórico de mensagens salvo no sistema, ordem/data e retomada automática em outras sessões/navegadores. Entregar uma capacidade de histórico observável sem simular resposta financeira ou produzir lançamentos.
   - Bloqueado por: Nenhum
   - Bloqueios externos: slice Redmine 1016117 ([QA] [WEB] [USUARIO] Adequação visual do FinAI): Base visual das telas atuais implementada e verificada - Conversa/histórico pode iniciar sem dados financeiros, mas a política visual-first aprovada exige a fundação entregue/verificada; #1016117 publicado em New não representa cumprimento.
2. **[DEV] [WEB] [USUARIO] Assistente financeiro com IA - Consultas financeiras com IA real** — 6h
   - Entrega: Entregar a primeira integração real de IA ao usuário por consultas financeiras em linguagem natural, usando a conversa persistida para contexto e os registros atuais do próprio titular. Este é o único dono da integração real reutilizada pelas próximas entregas, não uma tarefa isolada de SDK/provider.
   - Bloqueado por: 1
   - Bloqueios externos: slice Redmine 1016123 ([DEV] [WEB] [USUARIO] Gestão de transações - Cadastro de receitas e despesas com conferência do registro): Registros próprios reais persistidos, categorias e validações financeiras - Consultas de IA reais precisam da primeira capacidade financeira fornecida por #1016123. Propostas e confirmação consomem essas regras/criação pelo caminho interno, sem duplicar arestas transitivas.
3. **[DEV] [WEB] [USUARIO] Assistente financeiro com IA - Múltiplas propostas para revisão** — 4.5h
   - Entrega: Interpretar várias movimentações de uma mensagem com IA real e apresentar propostas persistidas e distinguíveis com seus cinco campos, data absoluta e estado, permitindo revisar as completas sem criar transações. Manter identidade e lacunas dos itens incompletos para o esclarecimento posterior, sem descartá-los ou inventar dados.
   - Bloqueado por: 2
   - Bloqueios externos: Nenhum
4. **[DEV] [WEB] [USUARIO] Assistente financeiro com IA - Esclarecimento, correção e cancelamento individuais** — 4h
   - Entrega: Completar e revisar o item correto entre várias propostas, com perguntas de esclarecimento, edição de campos e cancelamento individual, preservando os demais itens e os estados/versões salvos. A extração inicial já fornece propostas identificáveis, inclusive incompletas.
   - Bloqueado por: 3
   - Bloqueios externos: Nenhum
5. **[DEV] [WEB] [USUARIO] Assistente financeiro com IA - Confirmação individual sem duplicação** — 5.5h
   - Entrega: Transformar exclusivamente a proposta escolhida e confirmada em uma transação válida do titular, com resultados individuais persistidos e retomada segura. Revalidar dados/estado/versão e impedir repetição, incluindo resultados parciais e falha cujo efeito salvo seja incerto.
   - Bloqueado por: 3
   - Bloqueios externos: Nenhum

## Cobertura

| Regra ou critério | Destino | Evidência |
| --- | --- | --- |
| R1: A integração usa IA real para interpretar e responder; o assistente simulado por regras do protótipo não atende a esta entrega. Escolha de provedor, modelo e mecanismo de integração pertence à implementação, sem alterar os resultados e limites definidos aqui. | Slice 2 | design-input-001: query; requisito R7–R10. Capacidade do assistente ausente; o proprietário cria o comportamento de seu domínio. Condições transversais de histórico,versões e titularidade são também aplicadas pelas consumidoras explícitas,sem duplicar a mesma persistência/integração. |
| R2: Uma mensagem pode gerar várias propostas de transação. Cada proposta tem revisão, confirmação, correção, cancelamento e resultado próprios. Nenhuma é persistida sem confirmação explícita do titular no controle correspondente. Uma confirmação não autoriza outras propostas. | Slice 3 | design-input-001: showProposal,completePending,cancelProposal,handle. Capacidade do assistente ausente; o proprietário cria o comportamento de seu domínio. Condições transversais de histórico,versões e titularidade são também aplicadas pelas consumidoras explícitas,sem duplicar a mesma persistência/integração. |
| R3: Tipo, valor, descrição, categoria e data seguem integralmente as regras de Gestão de transações #1016105: valores em reais positivos até R$ 999.999.999,99 com até duas casas; descrição obrigatória até 120 caracteres; categorias predefinidas compatíveis com o tipo; data válida entre 01/01/1900 e hoje; somente movimentações realizadas. A classificação automática é uma proposta visível, sujeita a correção e confirmação. | Slice 3 | design-input-001: showProposal,completePending,cancelProposal,handle. Capacidade do assistente ausente; o proprietário cria o comportamento de seu domínio. Condições transversais de histórico,versões e titularidade são também aplicadas pelas consumidoras explícitas,sem duplicar a mesma persistência/integração. |
| R4: A falta de data assume hoje como proposta; referências explícitas devem ser interpretadas ou esclarecidas, sem substituir silenciosamente uma data informada por hoje. Propostas salvas retêm sua data absoluta ao reabrir a conversa, sem reinterpretar hoje/ontem com o novo dia. Campos são revalidados ao confirmar. | Slice 3 | design-input-001: showProposal,completePending,cancelProposal,handle. Capacidade do assistente ausente; o proprietário cria o comportamento de seu domínio. Condições transversais de histórico,versões e titularidade são também aplicadas pelas consumidoras explícitas,sem duplicar a mesma persistência/integração. |
| R5: Propostas corrigidas invalidam a possibilidade de confirmar versões anteriores. Propostas confirmadas ou canceladas mantêm seu estado no histórico. Uma transação já confirmada e posteriormente editada ou excluída manualmente não pode ser recriada pelo botão antigo da conversa. | Slice 4 | design-input-001: showProposal,completePending,cancelProposal,handle. Capacidade do assistente ausente; o proprietário cria o comportamento de seu domínio. Condições transversais de histórico,versões e titularidade são também aplicadas pelas consumidoras explícitas,sem duplicar a mesma persistência/integração. |
| R6: Manter uma única conversa contínua por usuário, sem lista de conversas nem ação de iniciar outra conversa. Persistir mensagens, respostas, propostas e seus estados para retomada em sessões e navegadores posteriores da mesma conta. Não incluir edição ou exclusão do histórico nesta entrega. | Slice 1 | docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md: #assistant,#messages,#chat-form,send,addMessage. Capacidade do assistente ausente; o proprietário cria o comportamento de seu domínio. Condições transversais de histórico,versões e titularidade são também aplicadas pelas consumidoras explícitas,sem duplicar a mesma persistência/integração. |
| R7: Consultas suportam saldo geral acumulado, somas e contagens de receitas/despesas por período e categoria e movimentações recentes correspondentes. O saldo geral considera todo o histórico; consultas com este mês ou mês passado usam esses meses de calendário; datas e intervalos explícitos são usados quando compreensíveis, e ambiguidades são esclarecidas. Para listagens recentes, mostrar até cinco registros e indicar quando houver mais correspondências consultáveis no histórico manual. | Slice 2 | design-input-001: query; requisito R7–R10. Capacidade do assistente ausente; o proprietário cria o comportamento de seu domínio. Condições transversais de histórico,versões e titularidade são também aplicadas pelas consumidoras explícitas,sem duplicar a mesma persistência/integração. |
| R8: Perguntas de despesa/receita sem período informado usam o mês corrente como recorte declarado, conforme a referência. Saldo geral e últimas movimentações sem outro recorte consideram todo o histórico. Respostas indicam período, categoria e tipo usados quando aplicáveis, para o usuário compreender o que foi consultado. Valores e contagens vêm de registros persistidos, nunca de exemplos ou apenas das mensagens da conversa. | Slice 2 | design-input-001: query; requisito R7–R10. Capacidade do assistente ausente; o proprietário cria o comportamento de seu domínio. Condições transversais de histórico,versões e titularidade são também aplicadas pelas consumidoras explícitas,sem duplicar a mesma persistência/integração. |
| R9: Novas consultas podem usar a conversa para compreender referências como “e no mês passado?”, mas precisam consultar os dados financeiros atuais. Respostas antigas permanecem no histórico como foram dadas e não são recalculadas ao reabrir; a posição/data da mensagem permite reconhecê-las como históricas. Solicitar novamente produz resposta baseada nos dados atuais. | Slice 2 | design-input-001: query; requisito R7–R10. Capacidade do assistente ausente; o proprietário cria o comportamento de seu domínio. Condições transversais de histórico,versões e titularidade são também aplicadas pelas consumidoras explícitas,sem duplicar a mesma persistência/integração. |
| R10: Consultar dados não cria nem altera transações. Texto de mensagens, respostas da IA ou pedidos para ignorar regras não dispensam confirmação, validação ou titularidade. Mensagens e propostas de outro titular não podem ser expostas ou utilizadas na resposta. | Slice 2 | design-input-001: query; requisito R7–R10. Capacidade do assistente ausente; o proprietário cria o comportamento de seu domínio. Condições transversais de histórico,versões e titularidade são também aplicadas pelas consumidoras explícitas,sem duplicar a mesma persistência/integração. |
| R11: A tela segue #assistant do design, com mensagens diferenciadas por autor, campo de composição, processamento, sugestões e guia de uso. Adaptar os cartões de proposta para vários itens e manter histórico salvo sem substituir a linguagem visual. Remover rótulos de assistente simulado e armazenamento apenas local. Conservar claro, escuro e acompanhar o sistema, com composição adaptada a celular, tablet e computador. | Slice 1 | docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md: #assistant,#messages,#chat-form,send,addMessage. Capacidade do assistente ausente; o proprietário cria o comportamento de seu domínio. Condições transversais de histórico,versões e titularidade são também aplicadas pelas consumidoras explícitas,sem duplicar a mesma persistência/integração. |
| CA1: Enviar uma mensagem com duas ou mais movimentações identificáveis; receber propostas distintas, com tipo, valor, descrição, categoria e data próprios, sem transações persistidas antes de confirmar. | Slice 3 | design-input-001: showProposal,completePending,cancelProposal,handle. Capacidade do assistente ausente; o proprietário cria o comportamento de seu domínio. Condições transversais de histórico,versões e titularidade são também aplicadas pelas consumidoras explícitas,sem duplicar a mesma persistência/integração. |
| CA2: Confirmar somente uma proposta entre várias; criar exatamente sua transação e manter as outras sem efeito financeiro. Confirmar as demais individualmente cria somente os registros correspondentes. | Slice 5 | app/Models; app/Actions; app/Http/Controllers; database/migrations; resources/js/pages. Capacidade do assistente ausente; o proprietário cria o comportamento de seu domínio. Condições transversais de histórico,versões e titularidade são também aplicadas pelas consumidoras explícitas,sem duplicar a mesma persistência/integração. |
| CA3: Enviar uma movimentação incompleta ou ambígua junto de outra completa; o assistente identifica a qual item se refere a pergunta, atualiza somente esse item e permite revisar a proposta completa sem exigir o preenchimento das demais. | Slice 4 | design-input-001: showProposal,completePending,cancelProposal,handle. Capacidade do assistente ausente; o proprietário cria o comportamento de seu domínio. Condições transversais de histórico,versões e titularidade são também aplicadas pelas consumidoras explícitas,sem duplicar a mesma persistência/integração. |
| CA4: Corrigir uma proposta e depois confirmar; persistir os campos revisados, com a versão anterior indisponível para confirmação. Cancelar uma proposta não registra nem cancela as outras. | Slice 4 | design-input-001: showProposal,completePending,cancelProposal,handle. Capacidade do assistente ausente; o proprietário cria o comportamento de seu domínio. Condições transversais de histórico,versões e titularidade são também aplicadas pelas consumidoras explícitas,sem duplicar a mesma persistência/integração. |
| CA5: Informar valores, descrições, tipos, categorias ou datas fora de R3; impedir registro e solicitar correção. Mensagem sem data propõe hoje explicitamente; mensagem com data futura pede correção. Reabrir em outro dia conserva a data absoluta previamente proposta. | Slice 3 | design-input-001: showProposal,completePending,cancelProposal,handle. Capacidade do assistente ausente; o proprietário cria o comportamento de seu domínio. Condições transversais de histórico,versões e titularidade são também aplicadas pelas consumidoras explícitas,sem duplicar a mesma persistência/integração. |
| CA6: Repetir a confirmação, reabrir o histórico ou usar controle antigo de proposta confirmada/cancelada; não criar nova transação. Isso também vale se o registro original tiver sido editado ou excluído manualmente depois. | Slice 5 | app/Models; app/Actions; app/Http/Controllers; database/migrations; resources/js/pages. Capacidade do assistente ausente; o proprietário cria o comportamento de seu domínio. Condições transversais de histórico,versões e titularidade são também aplicadas pelas consumidoras explícitas,sem duplicar a mesma persistência/integração. |
| CA7: Confirmar várias propostas individualmente e provocar falha em uma; manter os resultados já concluídos, informar qual item falhou e permitir retomar somente o que não foi registrado. Se houver incerteza sobre o efeito salvo, reconciliar a mesma proposta antes de uma nova tentativa que possa duplicá-la. | Slice 5 | app/Models; app/Actions; app/Http/Controllers; database/migrations; resources/js/pages. Capacidade do assistente ausente; o proprietário cria o comportamento de seu domínio. Condições transversais de histórico,versões e titularidade são também aplicadas pelas consumidoras explícitas,sem duplicar a mesma persistência/integração. |
| CA8: Sair, recarregar e acessar por outro navegador na mesma conta; recuperar a mesma conversa contínua, mensagens e propostas com seus estados. Propostas pendentes continuam sem persistência financeira e não há criação/seleção de conversas separadas. | Slice 1 | docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md: #assistant,#messages,#chat-form,send,addMessage. Capacidade do assistente ausente; o proprietário cria o comportamento de seu domínio. Condições transversais de histórico,versões e titularidade são também aplicadas pelas consumidoras explícitas,sem duplicar a mesma persistência/integração. |
| CA9: Consultar saldo geral, receitas/despesas por mês, dia ou intervalo compreensível, categoria e recentes; valores, contagens e registros correspondem ao sistema, com recortes declarados. Sem período para totais, usar mês corrente declarado; sem recorte para saldo/recentes, usar todo o histórico. | Slice 2 | design-input-001: query; requisito R7–R10. Capacidade do assistente ausente; o proprietário cria o comportamento de seu domínio. Condições transversais de histórico,versões e titularidade são também aplicadas pelas consumidoras explícitas,sem duplicar a mesma persistência/integração. |
| CA10: Fazer referência ao período de uma pergunta anterior; interpretar o contexto quando claro e consultar os dados atuais. Alterar transações manualmente e perguntar novamente produz números atualizados; respostas antigas no histórico permanecem como foram dadas. | Slice 2 | design-input-001: query; requisito R7–R10. Capacidade do assistente ausente; o proprietário cria o comportamento de seu domínio. Condições transversais de histórico,versões e titularidade são também aplicadas pelas consumidoras explícitas,sem duplicar a mesma persistência/integração. |
| CA11: Consultar recorte sem registros; informar ausência real de dados. Provocar falha na IA, consulta ou histórico; apresentar o erro correspondente e nova tentativa sem fabricar valores, alegar histórico vazio/salvo indevidamente ou criar transações. | Slice 2 | design-input-001: query; requisito R7–R10. Capacidade do assistente ausente; o proprietário cria o comportamento de seu domínio. Condições transversais de histórico,versões e titularidade são também aplicadas pelas consumidoras explícitas,sem duplicar a mesma persistência/integração. |
| CA12: Tentar consultar ou confirmar propostas/transações de outra conta, inclusive por acesso direto, ou pedir para ignorar confirmação e titularidade; não expor dados nem registrar indevidamente. Visitantes e contas não confirmadas não acessam o assistente. | Slice 2 | design-input-001: query; requisito R7–R10. Capacidade do assistente ausente; o proprietário cria o comportamento de seu domínio. Condições transversais de histórico,versões e titularidade são também aplicadas pelas consumidoras explícitas,sem duplicar a mesma persistência/integração. |
| CA13: Pedir edição/exclusão de registros ou ação fora do escopo; orientar os limites e a jornada manual aplicável, sem executar a operação pelo chat. | Slice 2 | design-input-001: query; requisito R7–R10. Capacidade do assistente ausente; o proprietário cria o comportamento de seu domínio. Condições transversais de histórico,versões e titularidade são também aplicadas pelas consumidoras explícitas,sem duplicar a mesma persistência/integração. |
| CA14: Utilizar chat, sugestões, composição, esclarecimentos e múltiplos cartões em computador, tablet e celular, nos temas claro, escuro e acompanhar o sistema; preservar a identidade e hierarquia do design, estados distinguíveis e controles correspondentes ao item correto, sem rótulos de simulação. | Slice 1 | docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md: #assistant,#messages,#chat-form,send,addMessage. Capacidade do assistente ausente; o proprietário cria o comportamento de seu domínio. Condições transversais de histórico,versões e titularidade são também aplicadas pelas consumidoras explícitas,sem duplicar a mesma persistência/integração. |
| R5-Confirmacao: Desdobramento de R5: confirmar observa versão/estado atual e não recria transação já confirmada depois de manutenção manual. | Slice 5 | app/Models; app/Actions; app/Http/Controllers; database/migrations; resources/js/pages. Capacidade do assistente ausente; o proprietário cria o comportamento de seu domínio. Condições transversais de histórico,versões e titularidade são também aplicadas pelas consumidoras explícitas,sem duplicar a mesma persistência/integração. |
| CA5-Confirmacao: Desdobramento de CA5/R3/R4: revalidar todos os campos e data absoluta no ato de confirmar. | Slice 5 | app/Models; app/Actions; app/Http/Controllers; database/migrations; resources/js/pages. Capacidade do assistente ausente; o proprietário cria o comportamento de seu domínio. Condições transversais de histórico,versões e titularidade são também aplicadas pelas consumidoras explícitas,sem duplicar a mesma persistência/integração. |
| CA11-Historico: Desdobramento de CA11: falha de gravação/carga de histórico não equivale a conversa salva/vazia. | Slice 1 | docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md: #assistant,#messages,#chat-form,send,addMessage. Capacidade do assistente ausente; o proprietário cria o comportamento de seu domínio. Condições transversais de histórico,versões e titularidade são também aplicadas pelas consumidoras explícitas,sem duplicar a mesma persistência/integração. |
| CA12-Historico: Desdobramento de CA12: somente o próprio titular acessa sua conversa e mensagens. | Slice 1 | docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md: #assistant,#messages,#chat-form,send,addMessage. Capacidade do assistente ausente; o proprietário cria o comportamento de seu domínio. Condições transversais de histórico,versões e titularidade são também aplicadas pelas consumidoras explícitas,sem duplicar a mesma persistência/integração. |
| CA12-Propostas: Desdobramento de CA12/R10: titularidade e confirmação obrigatórias também por acesso direto às propostas/ações. | Slice 5 | app/Models; app/Actions; app/Http/Controllers; database/migrations; resources/js/pages. Capacidade do assistente ausente; o proprietário cria o comportamento de seu domínio. Condições transversais de histórico,versões e titularidade são também aplicadas pelas consumidoras explícitas,sem duplicar a mesma persistência/integração. |

Formato das condições: Markdown e DOCX.

## Condições de teste

Estas condições integram a aprovação da decomposição. A validação estrutural não substitui a revisão semântica do tech lead.

### Contexto

Titulares A/B confirmados,visitante e conta não confirmada; duas sessões/navegadores; serviço de IA real acessível e respostas/falhas controláveis onde necessário. Preparar dados financeiros conhecidos em períodos/categorias distintos, lotes completos/incompletos/inválidos, datas locais e relógio controlável, proposta corrigida/cancelada/confirmada e falhas com resultado conhecido/incerto. Fornecedores financeiros e visual devem estar disponíveis para o aceite. Não há suíte de assistente pronta presumida; resultados/evidências serão produzidos na execução posterior, com impedimentos explícitos.

### Histórico

#### CT-001 — Conversa contínua própria

Verificação: Enviar mensagens,sair,recarregar e abrir outro navegador na mesma conta.

Resultado esperado: Retomar a mesma conversa,ordem/data/autoria e mensagens salvas;sem várias conversas ou gestão de threads.

Origem no requisito: R6: Manter uma única conversa contínua por usuário, sem lista de conversas nem ação de iniciar outra conversa. Persistir mensagens, respostas, propostas e seus estados para retomada em sessões e navegadores posteriores da mesma conta. Não incluir edição ou exclusão do histórico nesta entrega.; CA8: Sair, recarregar e acessar por outro navegador na mesma conta; recuperar a mesma conversa contínua, mensagens e propostas com seus estados. Propostas pendentes continuam sem persistência financeira e não há criação/seleção de conversas separadas.

#### CT-002 — Composição e limite

Verificação: Usar mensagem válida até500caracteres e observar envio/processamento;conferir campo,sugestões e estados sem atividade falsa de IA.

Resultado esperado: Limite aprovado,estado real e controle de envio protegido enquanto processa;sem resposta simulada ou lançamento por salvar mensagem.

Origem no requisito: R6: Manter uma única conversa contínua por usuário, sem lista de conversas nem ação de iniciar outra conversa. Persistir mensagens, respostas, propostas e seus estados para retomada em sessões e navegadores posteriores da mesma conta. Não incluir edição ou exclusão do histórico nesta entrega.; R11: A tela segue #assistant do design, com mensagens diferenciadas por autor, campo de composição, processamento, sugestões e guia de uso. Adaptar os cartões de proposta para vários itens e manter histórico salvo sem substituir a linguagem visual. Remover rótulos de assistente simulado e armazenamento apenas local. Conservar claro, escuro e acompanhar o sistema, com composição adaptada a celular, tablet e computador.; CA14: Utilizar chat, sugestões, composição, esclarecimentos e múltiplos cartões em computador, tablet e celular, nos temas claro, escuro e acompanhar o sistema; preservar a identidade e hierarquia do design, estados distinguíveis e controles correspondentes ao item correto, sem rótulos de simulação.

#### CT-003 — Falha ao salvar mensagem

Verificação: Provocar falha de gravação e retomar.

Resultado esperado: Não alegar salva;conservar mensagem ainda não enviada quando aplicável,com erro/nova tentativa.

Origem no requisito: CA11-Historico: Desdobramento de CA11: falha de gravação/carga de histórico não equivale a conversa salva/vazia.

#### CT-004 — Falha ao carregar histórico

Verificação: Provocar falha de leitura e restaurar.

Resultado esperado: Indisponibilidade não é conversa vazia;retomada recupera histórico real.

Origem no requisito: CA11-Historico: Desdobramento de CA11: falha de gravação/carga de histórico não equivale a conversa salva/vazia.; CA8: Sair, recarregar e acessar por outro navegador na mesma conta; recuperar a mesma conversa contínua, mensagens e propostas com seus estados. Propostas pendentes continuam sem persistência financeira e não há criação/seleção de conversas separadas.

#### CT-005 — Autoria e data históricas

Verificação: Retomar mensagens próprias/do assistente e comparar ordem e data.

Resultado esperado: Autoria distinguível,ordem cronológica e contexto histórico reconhecível,sem recalcular respostas antigas.

Origem no requisito: R6: Manter uma única conversa contínua por usuário, sem lista de conversas nem ação de iniciar outra conversa. Persistir mensagens, respostas, propostas e seus estados para retomada em sessões e navegadores posteriores da mesma conta. Não incluir edição ou exclusão do histórico nesta entrega.; R9: Novas consultas podem usar a conversa para compreender referências como “e no mês passado?”, mas precisam consultar os dados financeiros atuais. Respostas antigas permanecem no histórico como foram dadas e não são recalculadas ao reabrir; a posição/data da mensagem permite reconhecê-las como históricas. Solicitar novamente produz resposta baseada nos dados atuais.; R11: A tela segue #assistant do design, com mensagens diferenciadas por autor, campo de composição, processamento, sugestões e guia de uso. Adaptar os cartões de proposta para vários itens e manter histórico salvo sem substituir a linguagem visual. Remover rótulos de assistente simulado e armazenamento apenas local. Conservar claro, escuro e acompanhar o sistema, com composição adaptada a celular, tablet e computador.; CA8: Sair, recarregar e acessar por outro navegador na mesma conta; recuperar a mesma conversa contínua, mensagens e propostas com seus estados. Propostas pendentes continuam sem persistência financeira e não há criação/seleção de conversas separadas.

### Consultas reais

#### CT-006 — Integração real de IA

Verificação: Com serviço real configurado,fazer consulta compreensível e enviar movimentações;conferir as respostas/propostas resultantes e evidência da integração.

Resultado esperado: Interpretação usa IA real;protótipo por regras não é entregue como integração;falhas não geram resultados fictícios.

Origem no requisito: R1: A integração usa IA real para interpretar e responder; o assistente simulado por regras do protótipo não atende a esta entrega. Escolha de provedor, modelo e mecanismo de integração pertence à implementação, sem alterar os resultados e limites definidos aqui.; CA9: Consultar saldo geral, receitas/despesas por mês, dia ou intervalo compreensível, categoria e recentes; valores, contagens e registros correspondem ao sistema, com recortes declarados. Sem período para totais, usar mês corrente declarado; sem recorte para saldo/recentes, usar todo o histórico.; CA1: Enviar uma mensagem com duas ou mais movimentações identificáveis; receber propostas distintas, com tipo, valor, descrição, categoria e data próprios, sem transações persistidas antes de confirmar.

#### CT-007 — Saldo real

Verificação: Com valores conhecidos no sistema e números conflitantes apenas em mensagens,perguntar saldo geral.

Resultado esperado: Usar todo histórico real do titular,não números ditos na conversa ou exemplos.

Origem no requisito: R7: Consultas suportam saldo geral acumulado, somas e contagens de receitas/despesas por período e categoria e movimentações recentes correspondentes. O saldo geral considera todo o histórico; consultas com este mês ou mês passado usam esses meses de calendário; datas e intervalos explícitos são usados quando compreensíveis, e ambiguidades são esclarecidas. Para listagens recentes, mostrar até cinco registros e indicar quando houver mais correspondências consultáveis no histórico manual.; R8: Perguntas de despesa/receita sem período informado usam o mês corrente como recorte declarado, conforme a referência. Saldo geral e últimas movimentações sem outro recorte consideram todo o histórico. Respostas indicam período, categoria e tipo usados quando aplicáveis, para o usuário compreender o que foi consultado. Valores e contagens vêm de registros persistidos, nunca de exemplos ou apenas das mensagens da conversa.; CA9: Consultar saldo geral, receitas/despesas por mês, dia ou intervalo compreensível, categoria e recentes; valores, contagens e registros correspondem ao sistema, com recortes declarados. Sem período para totais, usar mês corrente declarado; sem recorte para saldo/recentes, usar todo o histórico.

#### CT-008 — Período,categoria e contagens

Verificação: Consultar receitas/despesas por este mês,mês passado,dia/intervalo explícito compreensível e categoria com massa conhecida.

Resultado esperado: Somas,contagens e registros corretos;recorte/tipo/categoria declarados quando aplicáveis.

Origem no requisito: R7: Consultas suportam saldo geral acumulado, somas e contagens de receitas/despesas por período e categoria e movimentações recentes correspondentes. O saldo geral considera todo o histórico; consultas com este mês ou mês passado usam esses meses de calendário; datas e intervalos explícitos são usados quando compreensíveis, e ambiguidades são esclarecidas. Para listagens recentes, mostrar até cinco registros e indicar quando houver mais correspondências consultáveis no histórico manual.; R8: Perguntas de despesa/receita sem período informado usam o mês corrente como recorte declarado, conforme a referência. Saldo geral e últimas movimentações sem outro recorte consideram todo o histórico. Respostas indicam período, categoria e tipo usados quando aplicáveis, para o usuário compreender o que foi consultado. Valores e contagens vêm de registros persistidos, nunca de exemplos ou apenas das mensagens da conversa.; CA9: Consultar saldo geral, receitas/despesas por mês, dia ou intervalo compreensível, categoria e recentes; valores, contagens e registros correspondem ao sistema, com recortes declarados. Sem período para totais, usar mês corrente declarado; sem recorte para saldo/recentes, usar todo o histórico.

#### CT-009 — Recortes padrão

Verificação: Pedir totais sem período e saldo/recentes sem outro recorte.

Resultado esperado: Totais usam mês corrente declarado;saldo/recentes usam todo histórico.

Origem no requisito: R8: Perguntas de despesa/receita sem período informado usam o mês corrente como recorte declarado, conforme a referência. Saldo geral e últimas movimentações sem outro recorte consideram todo o histórico. Respostas indicam período, categoria e tipo usados quando aplicáveis, para o usuário compreender o que foi consultado. Valores e contagens vêm de registros persistidos, nunca de exemplos ou apenas das mensagens da conversa.; CA9: Consultar saldo geral, receitas/despesas por mês, dia ou intervalo compreensível, categoria e recentes; valores, contagens e registros correspondem ao sistema, com recortes declarados. Sem período para totais, usar mês corrente declarado; sem recorte para saldo/recentes, usar todo o histórico.

#### CT-010 — Ambiguidade de consulta

Verificação: Pedir recorte ou referência sem interpretação segura.

Resultado esperado: Solicitar esclarecimento em vez de inventar período/valores.

Origem no requisito: R7: Consultas suportam saldo geral acumulado, somas e contagens de receitas/despesas por período e categoria e movimentações recentes correspondentes. O saldo geral considera todo o histórico; consultas com este mês ou mês passado usam esses meses de calendário; datas e intervalos explícitos são usados quando compreensíveis, e ambiguidades são esclarecidas. Para listagens recentes, mostrar até cinco registros e indicar quando houver mais correspondências consultáveis no histórico manual.; CA9: Consultar saldo geral, receitas/despesas por mês, dia ou intervalo compreensível, categoria e recentes; valores, contagens e registros correspondem ao sistema, com recortes declarados. Sem período para totais, usar mês corrente declarado; sem recorte para saldo/recentes, usar todo o histórico.

#### CT-011 — Recentes e histórico manual

Verificação: Com mais de cinco correspondências,pedir últimas movimentações.

Resultado esperado: Até cinco registros reais e indicação dos demais consultáveis no histórico manual.

Origem no requisito: R7: Consultas suportam saldo geral acumulado, somas e contagens de receitas/despesas por período e categoria e movimentações recentes correspondentes. O saldo geral considera todo o histórico; consultas com este mês ou mês passado usam esses meses de calendário; datas e intervalos explícitos são usados quando compreensíveis, e ambiguidades são esclarecidas. Para listagens recentes, mostrar até cinco registros e indicar quando houver mais correspondências consultáveis no histórico manual.; CA9: Consultar saldo geral, receitas/despesas por mês, dia ou intervalo compreensível, categoria e recentes; valores, contagens e registros correspondem ao sistema, com recortes declarados. Sem período para totais, usar mês corrente declarado; sem recorte para saldo/recentes, usar todo o histórico.

#### CT-012 — Contexto e dados atualizados

Verificação: Consultar,usar “e no mês passado?”,alterar dados manualmente e consultar de novo;reabrir conversa.

Resultado esperado: Contexto claro é entendido;consulta nova usa dados atuais;respostas antigas permanecem como dadas e reconhecíveis por posição/data.

Origem no requisito: R9: Novas consultas podem usar a conversa para compreender referências como “e no mês passado?”, mas precisam consultar os dados financeiros atuais. Respostas antigas permanecem no histórico como foram dadas e não são recalculadas ao reabrir; a posição/data da mensagem permite reconhecê-las como históricas. Solicitar novamente produz resposta baseada nos dados atuais.; CA10: Fazer referência ao período de uma pergunta anterior; interpretar o contexto quando claro e consultar os dados atuais. Alterar transações manualmente e perguntar novamente produz números atualizados; respostas antigas no histórico permanecem como foram dadas.

#### CT-013 — Sem dados e falha de consulta

Verificação: Consultar recorte sem registros e depois provocar falha de consulta.

Resultado esperado: Ausência real distinguida de indisponibilidade;falha nunca vira saldo zero ou dado inexistente fabricado.

Origem no requisito: R7: Consultas suportam saldo geral acumulado, somas e contagens de receitas/despesas por período e categoria e movimentações recentes correspondentes. O saldo geral considera todo o histórico; consultas com este mês ou mês passado usam esses meses de calendário; datas e intervalos explícitos são usados quando compreensíveis, e ambiguidades são esclarecidas. Para listagens recentes, mostrar até cinco registros e indicar quando houver mais correspondências consultáveis no histórico manual.; CA11: Consultar recorte sem registros; informar ausência real de dados. Provocar falha na IA, consulta ou histórico; apresentar o erro correspondente e nova tentativa sem fabricar valores, alegar histórico vazio/salvo indevidamente ou criar transações.

#### CT-014 — Falha de IA/interpretação

Verificação: Indisponibilizar o serviço ou fornecer resposta não interpretável e restaurar.

Resultado esperado: Orientar nova tentativa/cadastro manual,sem inventar resposta ou criar finança.

Origem no requisito: R1: A integração usa IA real para interpretar e responder; o assistente simulado por regras do protótipo não atende a esta entrega. Escolha de provedor, modelo e mecanismo de integração pertence à implementação, sem alterar os resultados e limites definidos aqui.; CA11: Consultar recorte sem registros; informar ausência real de dados. Provocar falha na IA, consulta ou histórico; apresentar o erro correspondente e nova tentativa sem fabricar valores, alegar histórico vazio/salvo indevidamente ou criar transações.

#### CT-015 — Limites de ação

Verificação: Pedir edição/exclusão de transações,aconselhamento ou outra ação fora da Feature.

Resultado esperado: Explicar limite e jornada manual aplicável,sem executar a ação no chat.

Origem no requisito: R10: Consultar dados não cria nem altera transações. Texto de mensagens, respostas da IA ou pedidos para ignorar regras não dispensam confirmação, validação ou titularidade. Mensagens e propostas de outro titular não podem ser expostas ou utilizadas na resposta.; CA13: Pedir edição/exclusão de registros ou ação fora do escopo; orientar os limites e a jornada manual aplicável, sem executar a operação pelo chat.

### Propostas e revisão

#### CT-016 — Várias propostas completas

Verificação: Enviar mensagem com duas ou mais movimentações identificáveis.

Resultado esperado: Propostas distintas,cinco campos e estados próprios,sem transações antes de confirmar.

Origem no requisito: R2: Uma mensagem pode gerar várias propostas de transação. Cada proposta tem revisão, confirmação, correção, cancelamento e resultado próprios. Nenhuma é persistida sem confirmação explícita do titular no controle correspondente. Uma confirmação não autoriza outras propostas.; CA1: Enviar uma mensagem com duas ou mais movimentações identificáveis; receber propostas distintas, com tipo, valor, descrição, categoria e data próprios, sem transações persistidas antes de confirmar.

#### CT-017 — Lote completo/incompleto

Verificação: Enviar um item completo e outro incompleto/ambíguo.

Resultado esperado: Conservar todos os itens identificáveis;pergunta aponta o item certo e o completo pode seguir independentemente.

Origem no requisito: R2: Uma mensagem pode gerar várias propostas de transação. Cada proposta tem revisão, confirmação, correção, cancelamento e resultado próprios. Nenhuma é persistida sem confirmação explícita do titular no controle correspondente. Uma confirmação não autoriza outras propostas.; CA3: Enviar uma movimentação incompleta ou ambígua junto de outra completa; o assistente identifica a qual item se refere a pergunta, atualiza somente esse item e permite revisar a proposta completa sem exigir o preenchimento das demais.

#### CT-018 — Validações dos campos

Verificação: Usar tipo/valor/descrição/categoria/data fora das regras financeiras,com fronteiras de valor/duas casas/120caracteres/1900atéhoje.

Resultado esperado: Não registrar inválido;apresentar lacuna/correção sem inventar campos e reutilizar regras/categorias compatíveis.

Origem no requisito: R3: Tipo, valor, descrição, categoria e data seguem integralmente as regras de Gestão de transações #1016105: valores em reais positivos até R$ 999.999.999,99 com até duas casas; descrição obrigatória até 120 caracteres; categorias predefinidas compatíveis com o tipo; data válida entre 01/01/1900 e hoje; somente movimentações realizadas. A classificação automática é uma proposta visível, sujeita a correção e confirmação.; CA5: Informar valores, descrições, tipos, categorias ou datas fora de R3; impedir registro e solicitar correção. Mensagem sem data propõe hoje explicitamente; mensagem com data futura pede correção. Reabrir em outro dia conserva a data absoluta previamente proposta.

#### CT-019 — Data ausente e explícita

Verificação: Enviar sem data e com uma data explícita válida ou inválida.

Resultado esperado: Ausente propõe hoje declarado;informada é interpretada ou esclarecida,nunca trocada silenciosamente por hoje.

Origem no requisito: R4: A falta de data assume hoje como proposta; referências explícitas devem ser interpretadas ou esclarecidas, sem substituir silenciosamente uma data informada por hoje. Propostas salvas retêm sua data absoluta ao reabrir a conversa, sem reinterpretar hoje/ontem com o novo dia. Campos são revalidados ao confirmar.; CA5: Informar valores, descrições, tipos, categorias ou datas fora de R3; impedir registro e solicitar correção. Mensagem sem data propõe hoje explicitamente; mensagem com data futura pede correção. Reabrir em outro dia conserva a data absoluta previamente proposta.

#### CT-020 — Hoje/ontem e retomada

Verificação: Criar propostas com hoje/ontem e reabrir em outro dia.

Resultado esperado: Exibir e manter datas absolutas já propostas;revalidar no confirmar sem reinterpretar o texto pelo novo dia.

Origem no requisito: R4: A falta de data assume hoje como proposta; referências explícitas devem ser interpretadas ou esclarecidas, sem substituir silenciosamente uma data informada por hoje. Propostas salvas retêm sua data absoluta ao reabrir a conversa, sem reinterpretar hoje/ontem com o novo dia. Campos são revalidados ao confirmar.; CA5: Informar valores, descrições, tipos, categorias ou datas fora de R3; impedir registro e solicitar correção. Mensagem sem data propõe hoje explicitamente; mensagem com data futura pede correção. Reabrir em outro dia conserva a data absoluta previamente proposta.; CA5-Confirmacao: Desdobramento de CA5/R3/R4: revalidar todos os campos e data absoluta no ato de confirmar.

#### CT-021 — Completar o item correto

Verificação: Responder aos dados faltantes de um item entre vários.

Resultado esperado: Alterar somente aquele,sem descartar/modificar demais;dados sem certeza pedem esclarecimento.

Origem no requisito: CA3: Enviar uma movimentação incompleta ou ambígua junto de outra completa; o assistente identifica a qual item se refere a pergunta, atualiza somente esse item e permite revisar a proposta completa sem exigir o preenchimento das demais.; R2: Uma mensagem pode gerar várias propostas de transação. Cada proposta tem revisão, confirmação, correção, cancelamento e resultado próprios. Nenhuma é persistida sem confirmação explícita do titular no controle correspondente. Uma confirmação não autoriza outras propostas.

#### CT-022 — Corrigir campos e versão

Verificação: Corrigir proposta e tentar seus controles antigos em outra sessão.

Resultado esperado: Proposta nova ainda não é transação;versão anterior não confirmável,e confirmar depois usa os campos revisados.

Origem no requisito: R5: Propostas corrigidas invalidam a possibilidade de confirmar versões anteriores. Propostas confirmadas ou canceladas mantêm seu estado no histórico. Uma transação já confirmada e posteriormente editada ou excluída manualmente não pode ser recriada pelo botão antigo da conversa.; CA4: Corrigir uma proposta e depois confirmar; persistir os campos revisados, com a versão anterior indisponível para confirmação. Cancelar uma proposta não registra nem cancela as outras.

#### CT-023 — Cancelar individualmente

Verificação: Cancelar um item entre vários e reabrir o histórico.

Resultado esperado: Apenas ele cancelado e sem lançamento;demais mantidos,e estado cancelado persiste.

Origem no requisito: R2: Uma mensagem pode gerar várias propostas de transação. Cada proposta tem revisão, confirmação, correção, cancelamento e resultado próprios. Nenhuma é persistida sem confirmação explícita do titular no controle correspondente. Uma confirmação não autoriza outras propostas.; R5: Propostas corrigidas invalidam a possibilidade de confirmar versões anteriores. Propostas confirmadas ou canceladas mantêm seu estado no histórico. Uma transação já confirmada e posteriormente editada ou excluída manualmente não pode ser recriada pelo botão antigo da conversa.; CA4: Corrigir uma proposta e depois confirmar; persistir os campos revisados, com a versão anterior indisponível para confirmação. Cancelar uma proposta não registra nem cancela as outras.

#### CT-024 — Referência ambígua a ação

Verificação: Pedir confirmar/cancelar sem identificar o item quando houver várias propostas.

Resultado esperado: Pedir identificação;nenhum cancelamento/registro indevido ou confirmação automática de lote.

Origem no requisito: R2: Uma mensagem pode gerar várias propostas de transação. Cada proposta tem revisão, confirmação, correção, cancelamento e resultado próprios. Nenhuma é persistida sem confirmação explícita do titular no controle correspondente. Uma confirmação não autoriza outras propostas.; CA3: Enviar uma movimentação incompleta ou ambígua junto de outra completa; o assistente identifica a qual item se refere a pergunta, atualiza somente esse item e permite revisar a proposta completa sem exigir o preenchimento das demais.; CA4: Corrigir uma proposta e depois confirmar; persistir os campos revisados, com a versão anterior indisponível para confirmação. Cancelar uma proposta não registra nem cancela as outras.

### Confirmação e retomada

#### CT-025 — Retomar todos os estados

Verificação: Salvar mensagens/propostas pendentes,corrigidas,canceladas/confirmadas e retomar em outro navegador.

Resultado esperado: Mesma conversa e estados atuais;pendentes sem efeito financeiro,sem reativar antigos ou reinterpretar datas.

Origem no requisito: R6: Manter uma única conversa contínua por usuário, sem lista de conversas nem ação de iniciar outra conversa. Persistir mensagens, respostas, propostas e seus estados para retomada em sessões e navegadores posteriores da mesma conta. Não incluir edição ou exclusão do histórico nesta entrega.; CA8: Sair, recarregar e acessar por outro navegador na mesma conta; recuperar a mesma conversa contínua, mensagens e propostas com seus estados. Propostas pendentes continuam sem persistência financeira e não há criação/seleção de conversas separadas.

#### CT-026 — Confirmar somente uma

Verificação: Entre propostas completas/incompletas,confirmar uma completa.

Resultado esperado: Exatamente sua transação;demais continuam sem efeito financeiro,e confirmar outras depois cria somente as correspondentes.

Origem no requisito: R2: Uma mensagem pode gerar várias propostas de transação. Cada proposta tem revisão, confirmação, correção, cancelamento e resultado próprios. Nenhuma é persistida sem confirmação explícita do titular no controle correspondente. Uma confirmação não autoriza outras propostas.; CA2: Confirmar somente uma proposta entre várias; criar exatamente sua transação e manter as outras sem efeito financeiro. Confirmar as demais individualmente cria somente os registros correspondentes.

#### CT-027 — Revalidar no confirmar

Verificação: Tentar confirmar proposta incompleta/inválida ou alterada antes da confirmação.

Resultado esperado: Impedir e orientar correção;verificar campos,data,estado/versão atuais sem efeito indevido.

Origem no requisito: R3: Tipo, valor, descrição, categoria e data seguem integralmente as regras de Gestão de transações #1016105: valores em reais positivos até R$ 999.999.999,99 com até duas casas; descrição obrigatória até 120 caracteres; categorias predefinidas compatíveis com o tipo; data válida entre 01/01/1900 e hoje; somente movimentações realizadas. A classificação automática é uma proposta visível, sujeita a correção e confirmação.; R4: A falta de data assume hoje como proposta; referências explícitas devem ser interpretadas ou esclarecidas, sem substituir silenciosamente uma data informada por hoje. Propostas salvas retêm sua data absoluta ao reabrir a conversa, sem reinterpretar hoje/ontem com o novo dia. Campos são revalidados ao confirmar.; CA5-Confirmacao: Desdobramento de CA5/R3/R4: revalidar todos os campos e data absoluta no ato de confirmar.

#### CT-028 — Repetição e sessões

Verificação: Confirmar,repetir,recaregar/reabrir e usar controles antigos, inclusive por duas sessões.

Resultado esperado: Uma transação por proposta,sem duplicar por repetição ou reabertura.

Origem no requisito: R5-Confirmacao: Desdobramento de R5: confirmar observa versão/estado atual e não recria transação já confirmada depois de manutenção manual.; CA6: Repetir a confirmação, reabrir o histórico ou usar controle antigo de proposta confirmada/cancelada; não criar nova transação. Isso também vale se o registro original tiver sido editado ou excluído manualmente depois.

#### CT-029 — Versão antiga ou cancelada

Verificação: Confirmar depois de corrigir/cancelar a proposta,usando versão anterior.

Resultado esperado: Recusar estado/versão inválidos;somente proposta vigente e explicitamente confirmada pode criar.

Origem no requisito: R5: Propostas corrigidas invalidam a possibilidade de confirmar versões anteriores. Propostas confirmadas ou canceladas mantêm seu estado no histórico. Uma transação já confirmada e posteriormente editada ou excluída manualmente não pode ser recriada pelo botão antigo da conversa.; R5-Confirmacao: Desdobramento de R5: confirmar observa versão/estado atual e não recria transação já confirmada depois de manutenção manual.; CA6: Repetir a confirmação, reabrir o histórico ou usar controle antigo de proposta confirmada/cancelada; não criar nova transação. Isso também vale se o registro original tiver sido editado ou excluído manualmente depois.

#### CT-030 — Manutenção manual posterior

Verificação: Confirmar,depois editar/excluir manualmente sua transação,e usar botão antigo no histórico.

Resultado esperado: Estado confirmado permanece;não recriar o registro pelo controle histórico.

Origem no requisito: R5-Confirmacao: Desdobramento de R5: confirmar observa versão/estado atual e não recria transação já confirmada depois de manutenção manual.; CA6: Repetir a confirmação, reabrir o histórico ou usar controle antigo de proposta confirmada/cancelada; não criar nova transação. Isso também vale se o registro original tiver sido editado ou excluído manualmente depois.

#### CT-031 — Nova mensagem igual

Verificação: Enviar novamente o mesmo texto de gasto após uma confirmação.

Resultado esperado: Novo registro somente por nova proposta e confirmação próprias,sem criação automática por igualdade de texto.

Origem no requisito: R2: Uma mensagem pode gerar várias propostas de transação. Cada proposta tem revisão, confirmação, correção, cancelamento e resultado próprios. Nenhuma é persistida sem confirmação explícita do titular no controle correspondente. Uma confirmação não autoriza outras propostas.; CA2: Confirmar somente uma proposta entre várias; criar exatamente sua transação e manter as outras sem efeito financeiro. Confirmar as demais individualmente cria somente os registros correspondentes.; CA6: Repetir a confirmação, reabrir o histórico ou usar controle antigo de proposta confirmada/cancelada; não criar nova transação. Isso também vale se o registro original tiver sido editado ou excluído manualmente depois.

#### CT-032 — Resultados parciais

Verificação: Confirmar itens individualmente e provocar falha em um deles.

Resultado esperado: Sucessos mantidos,resultado por item claro,demais não confirmados automaticamente;retomar apenas o não registrado.

Origem no requisito: CA7: Confirmar várias propostas individualmente e provocar falha em uma; manter os resultados já concluídos, informar qual item falhou e permitir retomar somente o que não foi registrado. Se houver incerteza sobre o efeito salvo, reconciliar a mesma proposta antes de uma nova tentativa que possa duplicá-la.

#### CT-033 — Falha conhecida ao persistir

Verificação: Falhar confirmação sem registro e restaurar para nova tentativa válida.

Resultado esperado: Sem sucesso fictício;erro do item identificável e uma transação após concluir a retomada.

Origem no requisito: CA7: Confirmar várias propostas individualmente e provocar falha em uma; manter os resultados já concluídos, informar qual item falhou e permitir retomar somente o que não foi registrado. Se houver incerteza sobre o efeito salvo, reconciliar a mesma proposta antes de uma nova tentativa que possa duplicá-la.

#### CT-034 — Efeito incerto com registro salvo

Verificação: Após persistir,perder resposta de confirmação e tentar retomar.

Resultado esperado: Verificar/reconciliar a mesma proposta antes de nova tentativa,não duplicar e reconhecer confirmação existente.

Origem no requisito: CA7: Confirmar várias propostas individualmente e provocar falha em uma; manter os resultados já concluídos, informar qual item falhou e permitir retomar somente o que não foi registrado. Se houver incerteza sobre o efeito salvo, reconciliar a mesma proposta antes de uma nova tentativa que possa duplicá-la.; CA6: Repetir a confirmação, reabrir o histórico ou usar controle antigo de proposta confirmada/cancelada; não criar nova transação. Isso também vale se o registro original tiver sido editado ou excluído manualmente depois.

#### CT-035 — Efeito incerto sem registro

Verificação: Interromper operação antes de salvar e recuperar seu resultado de forma verificável antes de retentar.

Resultado esperado: Não alegar resultado definitivo sem saber;somente após reconciliação permitir retomar sem duplicação.Falha de leitura não prova ausência.

Origem no requisito: CA7: Confirmar várias propostas individualmente e provocar falha em uma; manter os resultados já concluídos, informar qual item falhou e permitir retomar somente o que não foi registrado. Se houver incerteza sobre o efeito salvo, reconciliar a mesma proposta antes de uma nova tentativa que possa duplicá-la.

### Permissões e visual

#### CT-036 — Histórico alheio

Verificação: Como B,tentar conversa/mensagens de A por acesso direto.

Resultado esperado: Não ler ou usar dados/mensagens alheias na resposta.

Origem no requisito: CA12-Historico: Desdobramento de CA12: somente o próprio titular acessa sua conversa e mensagens.; R10: Consultar dados não cria nem altera transações. Texto de mensagens, respostas da IA ou pedidos para ignorar regras não dispensam confirmação, validação ou titularidade. Mensagens e propostas de outro titular não podem ser expostas ou utilizadas na resposta.

#### CT-037 — Consulta alheia ou dispensa de regras

Verificação: Pedir dados de outra conta ou mandar ignorar validação/confirmação/titularidade.

Resultado esperado: Não revelar nem alterar dados;consulta não cria finanças e texto do usuário/IA não dispensa as regras.

Origem no requisito: R10: Consultar dados não cria nem altera transações. Texto de mensagens, respostas da IA ou pedidos para ignorar regras não dispensam confirmação, validação ou titularidade. Mensagens e propostas de outro titular não podem ser expostas ou utilizadas na resposta.; CA12: Tentar consultar ou confirmar propostas/transações de outra conta, inclusive por acesso direto, ou pedir para ignorar confirmação e titularidade; não expor dados nem registrar indevidamente. Visitantes e contas não confirmadas não acessam o assistente.

#### CT-038 — Ações em proposta alheia

Verificação: Como B,tentar consultar,corrigir,cancelar/confirmar proposta de A por acesso direto.

Resultado esperado: Não expor nem modificar indevidamente;nenhuma transação alheia criada.

Origem no requisito: CA12-Propostas: Desdobramento de CA12/R10: titularidade e confirmação obrigatórias também por acesso direto às propostas/ações.; R10: Consultar dados não cria nem altera transações. Texto de mensagens, respostas da IA ou pedidos para ignorar regras não dispensam confirmação, validação ou titularidade. Mensagens e propostas de outro titular não podem ser expostas ou utilizadas na resposta.

#### CT-039 — Visitante e não-confirmado

Verificação: Abrir chat,consultas,propostas e confirmações sem sessão ou e-mail confirmado.

Resultado esperado: Restringir acesso conforme a jornada de conta,sem dados expostos ou registros.

Origem no requisito: CA12: Tentar consultar ou confirmar propostas/transações de outra conta, inclusive por acesso direto, ou pedir para ignorar confirmação e titularidade; não expor dados nem registrar indevidamente. Visitantes e contas não confirmadas não acessam o assistente.; CA12-Historico: Desdobramento de CA12: somente o próprio titular acessa sua conversa e mensagens.; CA12-Propostas: Desdobramento de CA12/R10: titularidade e confirmação obrigatórias também por acesso direto às propostas/ações.

#### CT-040 — Chat e cartões responsivos

Verificação: Comparar com design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md (#assistant,.chat-layout,.message,composer,sugestões,guia e cartões adaptados),em computador/tablet/celular,claro/escuro/sistema,com estados variados.

Resultado esperado: Autoria/hierarquia/identidade preservadas,controles distinguem o item correto,composição utilizável sem rótulos de simulação/armazenamento local.

Origem no requisito: R11: A tela segue #assistant do design, com mensagens diferenciadas por autor, campo de composição, processamento, sugestões e guia de uso. Adaptar os cartões de proposta para vários itens e manter histórico salvo sem substituir a linguagem visual. Remover rótulos de assistente simulado e armazenamento apenas local. Conservar claro, escuro e acompanhar o sistema, com composição adaptada a celular, tablet e computador.; CA14: Utilizar chat, sugestões, composição, esclarecimentos e múltiplos cartões em computador, tablet e celular, nos temas claro, escuro e acompanhar o sistema; preservar a identidade e hierarquia do design, estados distinguíveis e controles correspondentes ao item correto, sem rótulos de simulação.


## Descrições completas

### 1. [DEV] [WEB] [USUARIO] Assistente financeiro com IA - Conversa contínua com histórico salvo

#### Entrega

Criar a conversa própria contínua, com envio e histórico de mensagens salvo no sistema, ordem/data e retomada automática em outras sessões/navegadores. Entregar uma capacidade de histórico observável sem simular resposta financeira ou produzir lançamentos.

#### Escopo e limites

Responsável pela conversa, mensagens, composição e estados de carga/gravação. Respostas reais de IA, cartões/estados específicos de propostas e persistência financeira têm donos nas próximas entregas; histórico salvo não deve ser apresentado como assistente completo ou processamento de IA que nunca termina.

#### Critérios de aceite

- Abrir/retomar uma única conversa por usuário, com mensagens diferenciadas por autor em ordem cronológica e data reconhecível; sem seleção de conversas, edição ou exclusão do histórico. Sem mensagens, apresentar acolhimento e sugestões da referência.
- Aceitar envio de mensagem até500caracteres, salvar a mensagem própria e indicar seu processamento real, impedindo novo envio pelo controle enquanto esse processamento ocorre; não inventar resposta nem afirmar que IA atuou quando ainda não há integração disponível.
- Sair,recarregar e abrir outro navegador na mesma conta recupera as mensagens salvas. Propostas e estados produzidos pelos consumidores posteriores devem integrar esse histórico, sem confundir salvamento de mensagem com transação criada.
- Falha ao carregar histórico informa indisponibilidade e nova tentativa, não conversa vazia como sucesso. Falha ao salvar não alega mensagem salva; conservar a ainda não enviada quando aplicável e permitir retomar.
- Somente o titular confirmado acessa a própria conversa/mensagens, inclusive por acesso direto. Visitante e conta não confirmada permanecem restritos.
- Na superfície desta entrega, consumir a base FinAI e a composição #assistant nos temas claro/escuro/sistema e em computador/tablet/celular. Manter autoria das mensagens, campo/guia/sugestões/feedback e controles identificáveis; múltiplos cartões preservam a hierarquia da referência. Não mostrar rótulos de simulação ou armazenamento apenas local.

#### Dependências

Início bloqueado por [QA] [WEB] [USUARIO] Adequação visual do FinAI (#1016117), marco da base implementada/verificada. Não depende de persistência financeira para começar. Fornece a conversa usada por Consultas financeiras com IA real e pelas entregas de propostas/estados; integração dessas saídas é necessária ao aceite final do item inteiro.

#### Referências

Item pai Redmine `#1016107`; regras/critérios R6, R11, CA8, CA11-Historico, CA12-Historico, CA14.

- design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; #assistant,#messages,#chat-form,.chat-layout,.message,.chat-compose,sugestões e media queries
- Adaptações aprovadas: IA real, histórico salvo em conversa contínua, múltiplas propostas e confirmação individual; a linguagem visual é preservada.

### 2. [DEV] [WEB] [USUARIO] Assistente financeiro com IA - Consultas financeiras com IA real

#### Entrega

Entregar a primeira integração real de IA ao usuário por consultas financeiras em linguagem natural, usando a conversa persistida para contexto e os registros atuais do próprio titular. Este é o único dono da integração real reutilizada pelas próximas entregas, não uma tarefa isolada de SDK/provider.

#### Escopo e limites

Responsável por interpretar consultas, declarar recortes, obter dados atuais e responder com eles, além de falhas/limites. Não cria ou altera transações, não produz aconselhamento e não substitui IA por respostas simuladas por regras. Provedor/modelo/mecanismo são escolhas de implementação previstas em R1.

#### Critérios de aceite

- Consultar saldo geral de todo o histórico e somas/contagens de receitas/despesas por mês,dia,intervalo compreensível e categoria; apresentar período,tipo e categoria usados quando aplicáveis. Listar até cinco recentes e indicar mais correspondências consultáveis no histórico manual.
- Sem período para totais, usar mês corrente declarado; para saldo/recentes sem recorte, usar todo o histórico. Este mês/mês passado seguem calendário local; referências ambíguas pedem esclarecimento, sem inventar valores ou períodos.
- Usar a conversa quando referências forem claras, como “e no mês passado?”, mas buscar valores atuais no sistema. Respostas antigas ficam históricas como foram dadas, com data/posição reconhecível, e não são recalculadas ao reabrir.
- Ausência real de registros é distinta de indisponibilidade. Falha da IA/interpretação orienta tentar novamente ou cadastro manual, sem fabricar resposta ou lançamento; falha de consulta não vira saldo zero ou ausência de dados.
- Consultar não escreve finanças; dados de outro titular e pedidos para ignorar titularidade/confirmação não liberam operação. Pedidos de editar/excluir registros, aconselhamento ou ações fora do escopo recebem orientação e caminho manual aplicável, sem execução pelo chat.
- Mensagens e respostas próprias ficam no histórico contínuo; não usar números somente do texto da conversa como fatos persistidos do sistema.
- Na superfície desta entrega, consumir a base FinAI e a composição #assistant nos temas claro/escuro/sistema e em computador/tablet/celular. Manter autoria das mensagens, campo/guia/sugestões/feedback e controles identificáveis; múltiplos cartões preservam a hierarquia da referência. Não mostrar rótulos de simulação ou armazenamento apenas local.

#### Dependências

Início bloqueado por Conversa contínua com histórico salvo e pelo cadastro/persistência de Transações (#1016123). A base visual é transitiva. Para concluir o encaminhamento ao histórico manual, integrar Histórico, filtros e paginação (#1016124), sem bloquear o início dos agregados por essa integração. Fornece a integração real às propostas; Dashboard não é bloqueador.

#### Referências

Item pai Redmine `#1016107`; regras/critérios R1, R7, R8, R9, R10, CA9, CA10, CA11, CA12, CA13, CA14.

- design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; #assistant,query,sugestões,guia,composição,mensagens e estados de processamento/erro
- Adaptações aprovadas: IA real, histórico salvo em conversa contínua, múltiplas propostas e confirmação individual; a linguagem visual é preservada.

### 3. [DEV] [WEB] [USUARIO] Assistente financeiro com IA - Múltiplas propostas para revisão

#### Entrega

Interpretar várias movimentações de uma mensagem com IA real e apresentar propostas persistidas e distinguíveis com seus cinco campos, data absoluta e estado, permitindo revisar as completas sem criar transações. Manter identidade e lacunas dos itens incompletos para o esclarecimento posterior, sem descartá-los ou inventar dados.

#### Escopo e limites

Responsável pela extração inicial, identidade/estado/versão mínimos confiáveis e apresentação das propostas. Esclarecimento, correção e cancelamento pertencem à entrega específica; a criação financeira somente à confirmação individual. Não reconstruir integração de IA nem validações financeiras fornecidas.

#### Critérios de aceite

- Mensagem com duas ou mais movimentações identificáveis gera propostas distintas para todos os itens reconhecidos, com tipo,valor,descrição,categoria e data próprios. Nenhum lançamento é criado apenas pelo recebimento/salvamento da mensagem.
- Itens completos são revisáveis e itens incompletos/ambíguos conservam identidade/lacunas sem inventar campos; uma proposta completa não depende de preencher as demais para chegar à confirmação fornecida pela entrega responsável.
- Aplicar regras de Transações: BRL positivo atéR$999.999.999,99 com até duas casas,descrição obrigatória até120,categorias fixas compatíveis e data válida1900atéhoje. Classificação automática é proposta visível e corrigível, não fato incontestável.
- Sem data, propor hoje explicitamente; datas informadas são interpretadas ou marcadas para esclarecimento, sem trocar silenciosamente por hoje. Hoje/ontem tornam-se datas absolutas e permanecem iguais ao reabrir em outro dia.
- Propostas e seus estados ficam vinculados à mensagem/conversa própria e retomam depois. Falha de extração/gravação não fabrica proposta salva ou transação; titular alheio não pode ler os cartões ou seus dados.
- Na superfície desta entrega, consumir a base FinAI e a composição #assistant nos temas claro/escuro/sistema e em computador/tablet/celular. Manter autoria das mensagens, campo/guia/sugestões/feedback e controles identificáveis; múltiplos cartões preservam a hierarquia da referência. Não mostrar rótulos de simulação ou armazenamento apenas local.

#### Dependências

Início bloqueado por Consultas financeiras com IA real, que já fornece conversa,integração e dados financeiros necessários por suas dependências. Fornece identidade,estado e versão mínimos para Esclarecimento, correção e cancelamento individuais e Confirmação individual sem duplicação. Não repetir arestas transitivas de conversa/visual/Transações.

#### Referências

Item pai Redmine `#1016107`; regras/critérios R1, R2, R3, R4, R6, CA1, CA3, CA5, CA8, CA12, CA14.

- design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; #assistant,showProposal,completePending,#transaction-dialog e cartões de revisão adaptados para vários itens
- Adaptações aprovadas: IA real, histórico salvo em conversa contínua, múltiplas propostas e confirmação individual; a linguagem visual é preservada.

### 4. [DEV] [WEB] [USUARIO] Assistente financeiro com IA - Esclarecimento, correção e cancelamento individuais

#### Entrega

Completar e revisar o item correto entre várias propostas, com perguntas de esclarecimento, edição de campos e cancelamento individual, preservando os demais itens e os estados/versões salvos. A extração inicial já fornece propostas identificáveis, inclusive incompletas.

#### Escopo e limites

Responsável pela evolução e invalidação dos estados/versões das propostas, sem criar finanças. Confirmação consome o estado atual; não manter interpretação independente de qual versão está vigente. Não transformar correção de proposta em edição de transação já registrada.

#### Critérios de aceite

- Pedir os dados ausentes/ambíguos identificando a proposta; complemento altera somente o item referido e não descarta ou muda os demais. Referências a confirmar/cancelar sem item claro pedem identificação.
- Proposta completa pode seguir independentemente das incompletas. Tipo,valor,descrição,categoria e data sem interpretação segura não são preenchidos como fatos conhecidos.
- Corrigir permite revisar campos na linguagem visual do formulário financeiro e voltar com proposta atualizada ainda sem lançamento. Versão anterior fica não confirmável, inclusive por controles antigos em outra sessão.
- Cancelar somente o item selecionado conserva seu estado cancelado no histórico, sem registro nem cancelamento automático dos demais. Dados inválidos/futuros pedem correção segundo as regras fornecidas.
- Retomar a conversa conserva estado/versão atual e a data absoluta já proposta; não reinterpretar hoje/ontem no novo dia. Falha de mudança não é apresentada como revisão/cancelamento concluído.
- Na superfície desta entrega, consumir a base FinAI e a composição #assistant nos temas claro/escuro/sistema e em computador/tablet/celular. Manter autoria das mensagens, campo/guia/sugestões/feedback e controles identificáveis; múltiplos cartões preservam a hierarquia da referência. Não mostrar rótulos de simulação ou armazenamento apenas local.

#### Dependências

Início bloqueado por Múltiplas propostas para revisão. Para concluir o aceite integrado de correção/cancelamento, integrar Confirmação individual sem duplicação, que deve consultar o mesmo estado/versão atual antes de criar finanças. Essa integração de conclusão não gera bloqueio nativo de início entre as duas consumidoras.

#### Referências

Item pai Redmine `#1016107`; regras/critérios R2, R3, R4, R5, R6, CA3, CA4, CA5, CA8, CA14.

- design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; #assistant,completePending,showProposal,cancelProposal,#transaction-dialog e ações dos cartões
- Adaptações aprovadas: IA real, histórico salvo em conversa contínua, múltiplas propostas e confirmação individual; a linguagem visual é preservada.

### 5. [DEV] [WEB] [USUARIO] Assistente financeiro com IA - Confirmação individual sem duplicação

#### Entrega

Transformar exclusivamente a proposta escolhida e confirmada em uma transação válida do titular, com resultados individuais persistidos e retomada segura. Revalidar dados/estado/versão e impedir repetição, incluindo resultados parciais e falha cujo efeito salvo seja incerto.

#### Escopo e limites

Único dono da passagem de proposta confirmada para transação, reutilizando criação e regras de Transações. Não usar salvamento de mensagens, resposta da IA ou confirmação de outro item como autorização. Preservar confirmação histórica mesmo após edição/exclusão manual do registro financeiro.

#### Critérios de aceite

- Somente confirmação explícita do titular no controle correspondente pode criar uma transação válida da proposta selecionada. Uma confirmação não autoriza as outras; completas podem ser confirmadas sem completar os demais itens.
- Revalidar os cinco campos,restrições financeiras,data absoluta,estado e versão atuais. Incompleta,inválida,versão substituída,cancelada ou de outro titular não registra e recebe orientação adequada.
- Repetir confirmação,recarregar,reabrir ou usar controle antigo, inclusive em duas sessões, não cria duplicata. A proposta confirmada permanece não registrável mesmo após manutenção manual editar/excluir a transação original.
- Nova mensagem repetindo um gasto só pode criar outro lançamento após nova proposta e confirmação próprias; não registrar automaticamente por igualdade de texto ou pelo contexto de conversa.
- Em várias confirmações individuais, falha de um item conserva sucessos e não confirma os outros. Mostrar resultado de cada um,permitindo retomar somente o que não foi registrado.
- Se o efeito salvo for incerto, informar necessidade de verificação e reconciliar a mesma proposta antes de permitir tentativa que possa duplicar. Falha de leitura não prova ausência de lançamento; não afirmar sucesso ou falha definitiva sem saber o resultado.
- Guardar resultados e estados no histórico contínuo. Consultas/textos pedindo para dispensar confirmação não escrevem finanças e não ultrapassam titularidade. Transações reais ficam disponíveis às consultas do sistema, sem fonte financeira paralela no chat.
- Na superfície desta entrega, consumir a base FinAI e a composição #assistant nos temas claro/escuro/sistema e em computador/tablet/celular. Manter autoria das mensagens, campo/guia/sugestões/feedback e controles identificáveis; múltiplos cartões preservam a hierarquia da referência. Não mostrar rótulos de simulação ou armazenamento apenas local.

#### Dependências

Início bloqueado por Múltiplas propostas para revisão, que fornece identidade/estado/versão mínimos e herda conversa,integração e criação financeira #1016123. Para concluir, integrar os estados alterados por Esclarecimento, correção e cancelamento individuais. Edição e exclusão confirmada de Transações (#1016125) é necessária à verificação de manutenção manual posterior; não bloqueia iniciar a confirmação. Dashboard não é necessário.

#### Referências

Item pai Redmine `#1016107`; regras/critérios R2, R3, R4, R5, R5-Confirmacao, R6, R10, CA2, CA4, CA5-Confirmacao, CA6, CA7, CA8, CA12-Propostas, CA14.

- design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; #assistant,showProposal,controles Confirmar/Corrigir/Cancelar e estados individuais persistidos
- Adaptações aprovadas: IA real, histórico salvo em conversa contínua, múltiplas propostas e confirmação individual; a linguagem visual é preservada.
