# Fatiamento de [WEB] [USUARIO] Assistente financeiro com IA

Revisão: 3  
Hash: `b81b8e22e6ec1aecadd1ae24bee59c23c173927d87aa84a1a255d5c267635b84`

## Prévia numerada

1. **[DEV] [WEB] [USUARIO] Assistente financeiro com IA - Conversa persistida e saldo real** — 5.5h
   - Entrega: Criar a conversa contínua da conta e a primeira jornada útil com IA real: consultar saldo atual fundamentado nos registros próprios, preservando mensagens, processamento, erros e retomada. Consolidar nessa jornada os guardrails aprovados para que nenhuma mensagem altere permissões, confirmação, titularidade ou limites do assistente.
   - Bloqueado por: Nenhum
   - Bloqueios externos: Nenhum
2. **[DEV] [WEB] [USUARIO] Assistente financeiro com IA - Totais por período e categoria** — 4h
   - Entrega: Ampliar a conversa para totais de receitas e despesas por período/categoria, declarando os critérios e esclarecendo ambiguidades. Reutilizar a competência e os dados de Gestão de transações.
   - Bloqueado por: 1
   - Bloqueios externos: Nenhum
3. **[DEV] [WEB] [USUARIO] Assistente financeiro com IA - Listas e agendadas com continuidade** — 4.5h
   - Entrega: Permitir consultar movimentações realizadas e agendadas com filtros, quantidade total e continuidade de dez registros por resposta, sempre sobre dados atuais.
   - Bloqueado por: 1
   - Bloqueios externos: Nenhum
4. **[DEV] [WEB] [USUARIO] Assistente financeiro com IA - Preparação e retomada de proposta** — 5.5h
   - Entrega: Permitir descrever uma movimentação, complementar campos e retomar uma preparação própria incompleta ou pronta. Apresentar cinco campos válidos para revisão sem criar transação.
   - Bloqueado por: 1
   - Bloqueios externos: Nenhum
5. **[DEV] [WEB] [USUARIO] Assistente financeiro com IA - Correção e cancelamento de proposta** — 3h
   - Entrega: Permitir corrigir todos os campos ou cancelar a preparação atual, preservando o histórico e tornando confirmações anteriores inválidas.
   - Bloqueado por: 4
   - Bloqueios externos: Nenhum
6. **[DEV] [WEB] [USUARIO] Assistente financeiro com IA - Confirmação única e reconciliação** — 5h
   - Entrega: Converter a versão atual confirmada por botão em uma única transação própria, reconhecendo repetições e reconciliando resultados incertos antes de qualquer nova gravação.
   - Bloqueado por: 4
   - Bloqueios externos: Nenhum

## Cobertura

| Regra ou critério | Destino | Evidência |
| --- | --- | --- |
| R1: Interpretar linguagem natural com IA real; provedor/modelo/mecanismo ficam para implementação. Simulação por regras não satisfaz a entrega. | Slice 1 | Chat/estado de proposta/integração IA ausentes no inventário. Conversa persistida e saldo real é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| R2: Proposta usa tipo receita/despesa, valor R$0,01..999.999.999,99 com até2 casas sem arredondamento silencioso, descrição1..120 após aparar, categoria compatível e data válida01/01/1900..31/12/9999. | Slice 4 | Chat/estado de proposta/integração IA ausentes no inventário. Preparação e retomada de proposta é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| R3: Categorias: receita Salário/Freelance/Rendimentos/Outras receitas; despesa Alimentação/Moradia/Transporte/Saúde/Educação/Lazer/Compras/Outras despesas. Inferir só categoria compatível e segura; sem segurança pedir escolha, sem criar categoria nem escolher Outras silenciosamente. | Slice 4 | Chat/estado de proposta/integração IA ausentes no inventário. Preparação e retomada de proposta é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| R4: No máximo um registro em preparação por usuário, incompleto ou pronto. Mensagens/propostas não são transações e não entram nos cálculos. | Slice 4 | Chat/estado de proposta/integração IA ausentes no inventário. Preparação e retomada de proposta é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| R5: Somente botão Confirmar da versão atual grava. Repetir mesma proposta cria no máximo uma transação; nova proposta distinta com dados iguais pode criar outro registro. | Slice 6 | Chat/estado de proposta/integração IA ausentes no inventário. Confirmação única e reconciliação é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| R6-mensagens: Uma conversa contínua persistida por usuário; mensagens antigas permanecem histórico, não prova de saldo atual. Nova consulta usa dados atuais. | Slice 1 | Chat/estado de proposta/integração IA ausentes no inventário. Conversa persistida e saldo real é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| R6-proposta: Preparação incompleta/pronta retoma dados já coletados sem gravar; data fixada não muda porque o dia mudou. | Slice 4 | Chat/estado de proposta/integração IA ausentes no inventário. Preparação e retomada de proposta é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| R7: Datas relativas usam Brasília. Sem data propor hoje; relativa interpretada vira data concreta revisável. Dúvida pergunta; data explicitamente inválida não vira hoje. Futuras permitidas, sem antecipar efeitos. | Slice 4 | Chat/estado de proposta/integração IA ausentes no inventário. Preparação e retomada de proposta é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| R8-saldo: Consulta de saldo geral considera todo histórico próprio elegível até hoje, independentemente de período usado em perguntas anteriores. | Slice 1 | Chat/estado de proposta/integração IA ausentes no inventário. Conversa persistida e saldo real é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| R8-totais: Consultar totais de receitas/despesas por período e categoria. Reconhecer hoje, ontem, este mês, mês passado, datas/intervalos explícitos e todo histórico. | Slice 2 | Chat/estado de proposta/integração IA ausentes no inventário. Totais por período e categoria é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| R8-listas: Listar por período, tipo e categoria e listar agendadas, usando hoje/ontem/este mês/mês passado/datas/intervalos/todo histórico quando solicitados. | Slice 3 | Chat/estado de proposta/integração IA ausentes no inventário. Listas e agendadas com continuidade é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| R9-totais: Consulta independente de totais sem período usa este mês e declara o padrão; continuação explícita pode reutilizar filtros; dúvida exige esclarecimento. | Slice 2 | Chat/estado de proposta/integração IA ausentes no inventário. Totais por período e categoria é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| R9-listas: Lista independente sem período usa este mês; agendadas sem período usa todas futuras. Continuação explícita conserva filtros; dúvida pede esclarecer. | Slice 3 | Chat/estado de proposta/integração IA ausentes no inventário. Listas e agendadas com continuidade é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| R10-totais: Saldo/totais usam só próprios não excluídos até hoje. Intervalos incluem início/fim; invertido/ambíguo pede correção. | Slice 2 | Chat/estado de proposta/integração IA ausentes no inventário. Totais por período e categoria é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| R10-listas: Listas comuns excluem agendadas salvo inclusão expressa; quando incluídas, distinguir futuras dos contabilizados sem somá-las a valores realizados. | Slice 3 | Chat/estado de proposta/integração IA ausentes no inventário. Listas e agendadas com continuidade é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| R11: Até10 registros por resposta, data decrescente/cadastro mais recente em empate, quantidade total e Ver mais. Manter filtros e consultar dados reais; novos critérios iniciam nova lista. Totais usam conjunto completo, não página. | Slice 3 | Chat/estado de proposta/integração IA ausentes no inventário. Listas e agendadas com continuidade é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| R12-saldo: Resposta de saldo identifica todo histórico até hoje e usa reais/centavos; não inventa valores ou transações. | Slice 1 | Chat/estado de proposta/integração IA ausentes no inventário. Conversa persistida e saldo real é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| R12-totais: Resposta de totais identifica período/filtros, distingue contabilizado de agendado e usa reais com centavos. | Slice 2 | Chat/estado de proposta/integração IA ausentes no inventário. Totais por período e categoria é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| R12-listas: Resposta de listas identifica período/filtros, mostra dados reais e distingue agendados; não cria transações/categorias/valores fictícios. | Slice 3 | Chat/estado de proposta/integração IA ausentes no inventário. Listas e agendadas com continuidade é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| R12-confirmacao: Sucesso de registro só após persistência conhecida; futura significa agendada, não pagamento/recebimento realizado. | Slice 6 | Chat/estado de proposta/integração IA ausentes no inventário. Confirmação única e reconciliação é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| CA1: ‘Gastei R$35 no almoço’ sem data prepara despesa35, descrição coerente, categoria sugerida e hoje em Brasília, revisáveis; não grava antes de Confirmar. | Slice 4 | Chat/estado de proposta/integração IA ausentes no inventário. Preparação e retomada de proposta é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| CA2: Dados ausentes/ambíguos geram perguntas; inválido/categoria incompatível impede confirmar, sem inventar informação financeira. | Slice 4 | Chat/estado de proposta/integração IA ausentes no inventário. Preparação e retomada de proposta é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| CA3: Mensagem com duas movimentações pede envio de uma por vez, sem escolha silenciosa nem gravação parcial. | Slice 4 | Chat/estado de proposta/integração IA ausentes no inventário. Preparação e retomada de proposta é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| CA4: Corrigir todos os campos atualiza proposta, exige nova revisão e invalida confirmação antiga; cancelar não grava e registra cancelamento; ‘sim’ escrito não grava e orienta botão atual. | Slice 5 | Chat/estado de proposta/integração IA ausentes no inventário. Correção e cancelamento de proposta é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| CA5: Confirmar válida cria um único registro próprio e sucesso após persistência; repetição após voltar ao chat não duplica. | Slice 6 | Chat/estado de proposta/integração IA ausentes no inventário. Confirmação única e reconciliação é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| CA6: Confirmar futura grava agendada, fora dos totais até a data, quando entra pela regra de Gestão de transações. | Slice 6 | Chat/estado de proposta/integração IA ausentes no inventário. Confirmação única e reconciliação é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| CA7-mensagens: Sair/voltar restaura mensagens da conversa própria. | Slice 1 | Chat/estado de proposta/integração IA ausentes no inventário. Conversa persistida e saldo real é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| CA7-preparacao: Sair/voltar restaura preparação pendente/incompleta sem perder dados, gravar ou trocar data por novo hoje. | Slice 4 | Chat/estado de proposta/integração IA ausentes no inventário. Preparação e retomada de proposta é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| CA8: Consulta durante preparação responde com dados reais e mantém proposta. Segundo registro orienta confirmar/cancelar anterior; ambiguidade não sobrescreve dados. | Slice 4 | Chat/estado de proposta/integração IA ausentes no inventário. Preparação e retomada de proposta é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| CA9-totais: Totais respeitam padrões, filtros e períodos explícitos de R8–R12, inclusive todo histórico. | Slice 2 | Chat/estado de proposta/integração IA ausentes no inventário. Totais por período e categoria é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| CA9-listas: Listas respeitam períodos/filtros e inclusão explícita de futuras, com critérios visíveis. | Slice 3 | Chat/estado de proposta/integração IA ausentes no inventário. Listas e agendadas com continuidade é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| CA10-saldo: Ausência de dados produz saldo zero real; falha de leitura produz indisponibilidade, nunca zero inventado. | Slice 1 | Chat/estado de proposta/integração IA ausentes no inventário. Conversa persistida e saldo real é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| CA10-totais: Total zero real/ausência difere de falha de leitura, que informa indisponibilidade. | Slice 2 | Chat/estado de proposta/integração IA ausentes no inventário. Totais por período e categoria é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| CA10-listas: Lista sem registros informa ausência; leitura que falha informa indisponibilidade, sem resultados fabricados. | Slice 3 | Chat/estado de proposta/integração IA ausentes no inventário. Listas e agendadas com continuidade é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| CA11-saldo: Após editar/excluir na interface, nova pergunta de saldo reflete estado atual; resposta antiga continua apenas histórico. | Slice 1 | Chat/estado de proposta/integração IA ausentes no inventário. Conversa persistida e saldo real é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| CA11-totais: Nova consulta de totais reflete edição/exclusão na interface, sem reutilizar resposta financeira antiga. | Slice 2 | Chat/estado de proposta/integração IA ausentes no inventário. Totais por período e categoria é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| CA11-listas: Nova consulta/lista ou Ver mais usa registros atuais, refletindo alterações/exclusões. | Slice 3 | Chat/estado de proposta/integração IA ausentes no inventário. Listas e agendadas com continuidade é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| CA12: Mais10 permite Ver mais mantendo filtros e quantidade total; página não representa todo conjunto e totais não são só da página. | Slice 3 | Chat/estado de proposta/integração IA ausentes no inventário. Listas e agendadas com continuidade é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| CA13-gravacao: Falha conhecida mantém proposta para tentar de novo sem sucesso falso; resultado incerto exige conferir gravação antes de repetir, sem duplicar o já efetivado. | Slice 6 | Chat/estado de proposta/integração IA ausentes no inventário. Confirmação única e reconciliação é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| CA13-ia: Falha/indisponibilidade da IA permite tentar novamente ou cadastro manual, sem confirmar automaticamente proposta do chat. | Slice 1 | Chat/estado de proposta/integração IA ausentes no inventário. Conversa persistida e saldo real é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| CA14-conversa: Só titular autenticado/confirmado acessa conversa e finanças; pedido natural não troca proprietário nem permite consultar outra conta; editar/excluir salva orienta Gestão de transações. | Slice 1 | Chat/estado de proposta/integração IA ausentes no inventário. Conversa persistida e saldo real é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| CA14-proposta: Preparação/proposta pertence ao titular; pedir em linguagem natural outro proprietário ou dispensa de confirmação não altera regras. | Slice 4 | Chat/estado de proposta/integração IA ausentes no inventário. Preparação e retomada de proposta é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| F-falha-preparacao: Falha de interpretação/IA preserva preparação existente; repetir ou usar cadastro manual não confirma nem sobrescreve a proposta. | Slice 4 | Chat/estado de proposta/integração IA ausentes no inventário. Preparação e retomada de proposta é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| F-versao-cancelada: Versão antiga, proposta cancelada ou já confirmada não pode gravar novamente, mesmo após recarregar. | Slice 6 | Chat/estado de proposta/integração IA ausentes no inventário. Confirmação única e reconciliação é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| F-limites: Pedido fora de capacidade explica limite ou pede reformulação; não inventa resposta financeira, executa pagamento ou operação bancária. | Slice 1 | Chat/estado de proposta/integração IA ausentes no inventário. Conversa persistida e saldo real é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| F-correcao-validacao: Correção de tipo/valor/descrição/categoria/data mantém limites deR2/R3: R$0,01..999.999.999,99 até2 casas, descrição1..120 aparada, data1900..9999, categoria predefinida compatível; erro não cria transação. | Slice 5 | Chat/estado de proposta/integração IA ausentes no inventário. Correção e cancelamento de proposta é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| F-cancelamento: Cancelar descarta preparação sem excluir transações salvas; resultado fica na conversa e permite iniciar novo registro. | Slice 5 | Chat/estado de proposta/integração IA ausentes no inventário. Correção e cancelamento de proposta é dono deste resultado; reutiliza auth e capacidades financeiras fornecedoras sem duplicá-las. |
| F-primeiro-uso: Primeiro acesso ao chat apresenta orientação sobre consultas disponíveis e registro somente após confirmação; envio de mensagem mostra processamento e resultado ou erro. | Slice 1 | Fluxo principal e dados percebidos do requisito exigem orientação/processamento e ações de revisão; UI de chat/proposta ausente. |
| F-acoes-proposta: Proposta pronta mostra tipo, valor, descrição, categoria e data concreta com Confirmar, Corrigir e Cancelar; incompleta/inválida não libera confirmação. | Slice 4 | Fluxo principal e dados percebidos do requisito exigem orientação/processamento e ações de revisão; UI de chat/proposta ausente. |
| G-conversa: Guardrails aprovados da conversa: manter o papel de assistente financeiro pessoal e limitar respostas às capacidades de registro e consulta financeira previstas; assuntos como política, receitas culinárias, entretenimento ou conhecimento geral recebem explicação do limite e redirecionamento ao contexto financeiro. O conteúdo da mensagem não muda autenticação, titularidade, confirmação ou limites; não inventa dados, não executa pagamentos, não trata falha como zero, não sobrescreve proposta pendente e encaminha edição/exclusão de registros salvos para Gestão de transações. | Slice 1 | Os guardrails já aparecem nos atores, fluxos alternativos, R4-R5/R9-R12 e CA2/CA4/CA8/CA10/CA13/CA14. A jornada base da conversa os consolida sem criar comportamento adicional no item pai. |

Formato das condições: Markdown e DOCX.

## Condições de teste

Estas condições integram a aprovação da decomposição. A validação estrutural não substitui a revisão semântica do tech lead.

### Contexto

Preparar contas A/B confirmadas, conta não confirmada, transações reais de datas/categorias variadas,21registros elegíveis, futuras/excluídas, relógio de Brasília e falhas controladas. Executar jornadas representativas com provedor IA real escolhido na implementação e massa independente. Testes de integração com banco comprovam limites/isolamento/estado; concorrência, confirmação antiga e resposta perdida após commit exigem evidência automatizada reproduzível, além da jornada na interface. Não simular a IA como aceite deR1, nem substituir cálculo/registro por resposta inventada. Aplicar os guardrails aprovados a consultas, preparação, correção, cancelamento e confirmação; conteúdo da mensagem não altera permissões nem regras. Testar também pedidos fora do papel financeiro, incluindo política, receitas culinárias, entretenimento e conhecimento geral. Registrar comando/revisão/massa/instante/esperado/observado; nenhum teste do assistente executado nesta preparação.

#### CT-001 — R1 — Conversa persistida e saldo real

Verificação: Em ambiente integrado ao provedor real, perguntar saldo usando formulações naturais distintas e observar processamento/resposta.

Resultado esperado: Intenção é interpretada por IA real e valor vem dos registros próprios, não de resposta fixa ou regra simulada.

Origem no requisito: R1: Interpretar linguagem natural com IA real; provedor/modelo/mecanismo ficam para implementação. Simulação por regras não satisfaz a entrega.

#### CT-002 — R2 — Preparação e retomada de proposta

Verificação: Preparar com limites válidos e inválidos de valor/precisão/descrição/data, tipo ausente e categoria incompatível.

Resultado esperado: Só proposta com cinco campos válidos fica pronta; inválidos pedem correção e não liberam gravação.

Origem no requisito: R2: Proposta usa tipo receita/despesa, valor R$0,01..999.999.999,99 com até2 casas sem arredondamento silencioso, descrição1..120 após aparar, categoria compatível e data válida01/01/1900..31/12/9999.

#### CT-003 — R3 — Preparação e retomada de proposta

Verificação: Usar mensagem de categoria clara e outra sem correspondência segura; trocar tipo durante complementação.

Resultado esperado: Sugestão está entre categorias compatíveis e é revisável; dúvida exige escolha e não inventa categoria.

Origem no requisito: R3: Categorias: receita Salário/Freelance/Rendimentos/Outras receitas; despesa Alimentação/Moradia/Transporte/Saúde/Educação/Lazer/Compras/Outras despesas. Inferir só categoria compatível e segura; sem segurança pedir escolha, sem criar categoria nem escolher Outras silenciosamente.

#### CT-004 — R4 — Preparação e retomada de proposta

Verificação: Preparar proposta completa e incompleta e consultar saldo/totais antes de confirmar.

Resultado esperado: Uma única preparação é mantida e nenhuma contribuição financeira é criada.

Origem no requisito: R4: No máximo um registro em preparação por usuário, incompleto ou pronto. Mensagens/propostas não são transações e não entram nos cálculos.

#### CT-005 — R5 — Confirmação única e reconciliação

Verificação: Confirmar duas vezes a mesma proposta, inclusive simultaneamente e após recarga; depois iniciar e confirmar nova proposta igual.

Resultado esperado: Uma transação para a primeira proposta; a nova proposta válida pode gerar outra independente.

Origem no requisito: R5: Somente botão Confirmar da versão atual grava. Repetir mesma proposta cria no máximo uma transação; nova proposta distinta com dados iguais pode criar outro registro.

#### CT-006 — R6-mensagens — Conversa persistida e saldo real

Verificação: Conversar, sair/entrar, reabrir mensagens; alterar dados financeiros e fazer nova pergunta de saldo.

Resultado esperado: Conversa persiste e nova resposta usa estado atual; texto histórico não é reescrito como se fosse consulta atual.

Origem no requisito: R6-mensagens: Uma conversa contínua persistida por usuário; mensagens antigas permanecem histórico, não prova de saldo atual. Nova consulta usa dados atuais.

#### CT-007 — R6-proposta — Preparação e retomada de proposta

Verificação: Preparar incompleta e completa em dias controlados; sair e voltar no dia seguinte.

Resultado esperado: Retoma os campos e a data concretos sem transação automática.

Origem no requisito: R6-proposta: Preparação incompleta/pronta retoma dados já coletados sem gravar; data fixada não muda porque o dia mudou.

#### CT-008 — R7 — Preparação e retomada de proposta

Verificação: Usar sem data, ontem/amanhã, data ambígua e data impossível; reabrir após virada de Brasília.

Resultado esperado: Hoje só quando data ausente; relativas fixadas, inválida/ambígua esclarecida; futura pode ser proposta sem contabilização.

Origem no requisito: R7: Datas relativas usam Brasília. Sem data propor hoje; relativa interpretada vira data concreta revisável. Dúvida pergunta; data explicitamente inválida não vira hoje. Futuras permitidas, sem antecipar efeitos.

#### CT-009 — R8-saldo — Conversa persistida e saldo real

Verificação: Com receita100/despesa30 elegíveis e receita50 futura, perguntar saldo após consulta de outro período.

Resultado esperado: SaldoR$70,00 do histórico até hoje; futura excluída e critérios explícitos.

Origem no requisito: R8-saldo: Consulta de saldo geral considera todo histórico próprio elegível até hoje, independentemente de período usado em perguntas anteriores.

#### CT-010 — R8-totais — Totais por período e categoria

Verificação: Preparar registros em limites dos períodos e categorias; perguntar cada período e categoria.

Resultado esperado: Totais reais do conjunto solicitado, com período/categoria descritos na resposta.

Origem no requisito: R8-totais: Consultar totais de receitas/despesas por período e categoria. Reconhecer hoje, ontem, este mês, mês passado, datas/intervalos explícitos e todo histórico.

#### CT-011 — R8-listas — Listas e agendadas com continuidade

Verificação: Pedir listas com cada tipo de período e filtros, além de agendadas.

Resultado esperado: Seleção própria real corresponde aos critérios solicitados e declarados.

Origem no requisito: R8-listas: Listar por período, tipo e categoria e listar agendadas, usando hoje/ontem/este mês/mês passado/datas/intervalos/todo histórico quando solicitados.

#### CT-012 — R9-totais — Totais por período e categoria

Verificação: Perguntar total sem período; continuar explicitamente por outra categoria; enviar continuação ambígua e novo pedido independente.

Resultado esperado: Padrão declarado, continuação coerente e ambiguidade esclarecida sem usar filtros antigos silenciosamente.

Origem no requisito: R9-totais: Consulta independente de totais sem período usa este mês e declara o padrão; continuação explícita pode reutilizar filtros; dúvida exige esclarecimento.

#### CT-013 — R9-listas — Listas e agendadas com continuidade

Verificação: Pedir lista sem período e agendadas sem período; continuar lista; iniciar pedido novo e mensagem ambígua.

Resultado esperado: Padrões corretos e explícitos; nova intenção reinicia critérios e ambiguidade não inventa seleção.

Origem no requisito: R9-listas: Lista independente sem período usa este mês; agendadas sem período usa todas futuras. Continuação explícita conserva filtros; dúvida pede esclarecer.

#### CT-014 — R10-totais — Totais por período e categoria

Verificação: Usar registros nos dois limites, fora do intervalo, excluídos, futuros e de outra conta; solicitar intervalo invertido.

Resultado esperado: Soma apenas conjunto elegível e inclusivo; intervalo inválido solicita correção, sem resultado inventado.

Origem no requisito: R10-totais: Saldo/totais usam só próprios não excluídos até hoje. Intervalos incluem início/fim; invertido/ambíguo pede correção.

#### CT-015 — R10-listas — Listas e agendadas com continuidade

Verificação: Pedir lista comum, lista incluindo futuras e somente agendadas.

Resultado esperado: Futuras aparecem apenas quando solicitadas, identificadas separadamente e sem contaminar valores realizados.

Origem no requisito: R10-listas: Listas comuns excluem agendadas salvo inclusão expressa; quando incluídas, distinguir futuras dos contabilizados sem somá-las a valores realizados.

#### CT-016 — R11 — Listas e agendadas com continuidade

Verificação: Preparar21 registros e empate; navegar páginas10/10/1, alterar dados antes de Ver mais, mudar critérios e solicitar total.

Resultado esperado: Ordem, contagem e continuidade corretas; dados atuais nas novas consultas; critérios novos reiniciam; total não fica limitado à página.

Origem no requisito: R11: Até10 registros por resposta, data decrescente/cadastro mais recente em empate, quantidade total e Ver mais. Manter filtros e consultar dados reais; novos critérios iniciam nova lista. Totais usam conjunto completo, não página.

#### CT-017 — R12-saldo — Conversa persistida e saldo real

Verificação: Consultar conta com saldo negativo/zero e conta com falha de leitura.

Resultado esperado: Valores reais formatados e critérios claros; falha é indisponibilidade, não número fabricado.

Origem no requisito: R12-saldo: Resposta de saldo identifica todo histórico até hoje e usa reais/centavos; não inventa valores ou transações.

#### CT-018 — R12-totais — Totais por período e categoria

Verificação: Solicitar total por categoria/período com futuras presentes.

Resultado esperado: Expõe critérios e soma somente contabilizados, em R$ com centavos.

Origem no requisito: R12-totais: Resposta de totais identifica período/filtros, distingue contabilizado de agendado e usa reais com centavos.

#### CT-019 — R12-listas — Listas e agendadas com continuidade

Verificação: Listar realizados e futuras expressamente com categoria/filtro definidos.

Resultado esperado: Conteúdo corresponde aos registros, critérios explícitos e futura claramente diferenciada.

Origem no requisito: R12-listas: Resposta de listas identifica período/filtros, mostra dados reais e distingue agendados; não cria transações/categorias/valores fictícios.

#### CT-020 — R12-confirmacao — Confirmação única e reconciliação

Verificação: Confirmar proposta atual e futura e conferir mensagem/registro.

Resultado esperado: Estado confirmado corresponde à gravação real; futura é apresentada como agendamento.

Origem no requisito: R12-confirmacao: Sucesso de registro só após persistência conhecida; futura significa agendada, não pagamento/recebimento realizado.

#### CT-021 — CA1 — Preparação e retomada de proposta

Verificação: Enviar a frase com calendário de Brasília controlado e conferir proposta e registros.

Resultado esperado: DespesaR$35 com campos revisáveis e data concreta; nenhum registro ainda.

Origem no requisito: CA1: ‘Gastei R$35 no almoço’ sem data prepara despesa35, descrição coerente, categoria sugerida e hoje em Brasília, revisáveis; não grava antes de Confirmar.

#### CT-022 — CA2 — Preparação e retomada de proposta

Verificação: Enviar valor ambíguo, descrição ausente, data inválida e categoria incompatível; responder complementações.

Resultado esperado: Dados necessários são esclarecidos e preservados; pronta só após validação completa.

Origem no requisito: CA2: Dados ausentes/ambíguos geram perguntas; inválido/categoria incompatível impede confirmar, sem inventar informação financeira.

#### CT-023 — CA3 — Preparação e retomada de proposta

Verificação: Enviar ‘recebi100 e gastei30’ ou duas despesas numa mensagem.

Resultado esperado: Pede separar; não prepara silenciosamente só uma nem grava parte.

Origem no requisito: CA3: Mensagem com duas movimentações pede envio de uma por vez, sem escolha silenciosa nem gravação parcial.

#### CT-024 — CA4 — Correção e cancelamento de proposta

Verificação: Corrigir campos, conservar uma confirmação antiga, cancelar e escrever ‘sim’.

Resultado esperado: Nova versão exige Confirmar; antiga não pode gravar; cancelamento persistido sem transação; texto só orienta.

Origem no requisito: CA4: Corrigir todos os campos atualiza proposta, exige nova revisão e invalida confirmação antiga; cancelar não grava e registra cancelamento; ‘sim’ escrito não grava e orienta botão atual.

#### CT-025 — CA5 — Confirmação única e reconciliação

Verificação: Confirmar, sair/voltar e repetir; observar identidade e quantidade persistida.

Resultado esperado: Exatamente uma transação própria vinculada à proposta, visível no histórico e nas consultas financeiras com efeito conforme sua data; sem sucesso anterior à gravação.

Origem no requisito: CA5: Confirmar válida cria um único registro próprio e sucesso após persistência; repetição após voltar ao chat não duplica.

#### CT-026 — CA6 — Confirmação única e reconciliação

Verificação: Confirmar receita50 para amanhã com saldo70; controlar virada local e consultar novamente.

Resultado esperado: Antes saldo70 e futura agendada; após data saldo120, sem pagamento externo nem nova confirmação.

Origem no requisito: CA6: Confirmar futura grava agendada, fora dos totais até a data, quando entra pela regra de Gestão de transações.

#### CT-027 — CA7-mensagens — Conversa persistida e saldo real

Verificação: Trocar sessão e reabrir chat do titular.

Resultado esperado: Histórico preservado e isolado da outra conta.

Origem no requisito: CA7-mensagens: Sair/voltar restaura mensagens da conversa própria.

#### CT-028 — CA7-preparacao — Preparação e retomada de proposta

Verificação: Preparar parcialmente, sair, avançar data e retornar; repetir com proposta pronta.

Resultado esperado: Mesmo conteúdo e data fixada, ainda não confirmado; faltantes podem ser completados.

Origem no requisito: CA7-preparacao: Sair/voltar restaura preparação pendente/incompleta sem perder dados, gravar ou trocar data por novo hoje.

#### CT-029 — CA8 — Preparação e retomada de proposta

Verificação: Com proposta pendente, consultar saldo/totais/lista, pedir outro registro e enviar mensagem ambígua.

Resultado esperado: Consultas funcionam sem perda; novo registro não substitui anterior e dúvida exige esclarecimento.

Origem no requisito: CA8: Consulta durante preparação responde com dados reais e mantém proposta. Segundo registro orienta confirmar/cancelar anterior; ambiguidade não sobrescreve dados.

#### CT-030 — CA9-totais — Totais por período e categoria

Verificação: Pedir total sem período, intervalo explícito, todo histórico e categoria.

Resultado esperado: Respostas correspondem a cada conjunto e identificam critérios efetivos.

Origem no requisito: CA9-totais: Totais respeitam padrões, filtros e períodos explícitos de R8–R12, inclusive todo histórico.

#### CT-031 — CA9-listas — Listas e agendadas com continuidade

Verificação: Solicitar lista padrão, todo histórico, categoria/tipo e agendadas.

Resultado esperado: Seleção e apresentação respeitam pedido e padrões.

Origem no requisito: CA9-listas: Listas respeitam períodos/filtros e inclusão explícita de futuras, com critérios visíveis.

#### CT-032 — CA10-saldo — Conversa persistida e saldo real

Verificação: Consultar conta vazia e simular falha de leitura de conta com saldo70.

Resultado esperado: VaziaR$0,00; falha avisa indisponibilidade sem alegar saldo zero.

Origem no requisito: CA10-saldo: Ausência de dados produz saldo zero real; falha de leitura produz indisponibilidade, nunca zero inventado.

#### CT-033 — CA10-totais — Totais por período e categoria

Verificação: Consultar filtro sem registros e provocar falha em consulta com registros.

Resultado esperado: Ausência/zero só quando leitura bem-sucedida; falha sem valor fictício.

Origem no requisito: CA10-totais: Total zero real/ausência difere de falha de leitura, que informa indisponibilidade.

#### CT-034 — CA10-listas — Listas e agendadas com continuidade

Verificação: Consultar filtro vazio e interromper leitura de lista existente.

Resultado esperado: Estados distintos; erro não vira lista vazia ou conteúdo inventado.

Origem no requisito: CA10-listas: Lista sem registros informa ausência; leitura que falha informa indisponibilidade, sem resultados fabricados.

#### CT-035 — CA11-saldo — Conversa persistida e saldo real

Verificação: Consultar saldo70, alterar despesa30 para40 na interface e perguntar novamente.

Resultado esperado: Nova resposta60; resposta antiga70 permanece mensagem histórica.

Origem no requisito: CA11-saldo: Após editar/excluir na interface, nova pergunta de saldo reflete estado atual; resposta antiga continua apenas histórico.

#### CT-036 — CA11-totais — Totais por período e categoria

Verificação: Consultar categoria, alterar/excluir registro correspondente e repetir pedido.

Resultado esperado: Total atualizado; mensagem anterior não é prova do valor atual.

Origem no requisito: CA11-totais: Nova consulta de totais reflete edição/exclusão na interface, sem reutilizar resposta financeira antiga.

#### CT-037 — CA11-listas — Listas e agendadas com continuidade

Verificação: Listar, editar/excluir registro na interface e fazer nova consulta/continuidade.

Resultado esperado: Apresentação e quantidade refletem dados atuais, não cópia da lista antiga.

Origem no requisito: CA11-listas: Nova consulta/lista ou Ver mais usa registros atuais, refletindo alterações/exclusões.

#### CT-038 — CA12 — Listas e agendadas com continuidade

Verificação: Com21 receitas deR$1 no filtro, percorrer páginas e pedir total.

Resultado esperado: Páginas10/10/1, quantidade21 e totalR$21,00, nãoR$10,00.

Origem no requisito: CA12: Mais10 permite Ver mais mantendo filtros e quantidade total; página não representa todo conjunto e totais não são só da página.

#### CT-039 — CA13-gravacao — Confirmação única e reconciliação

Verificação: Falhar antes de persistir; em outro cenário perder resposta depois de persistir e repetir confirmação; conferir banco e estado.

Resultado esperado: Primeiro mantém proposta sem sucesso; segundo reconcilia o registro existente, no máximo uma transação.

Origem no requisito: CA13-gravacao: Falha conhecida mantém proposta para tentar de novo sem sucesso falso; resultado incerto exige conferir gravação antes de repetir, sem duplicar o já efetivado.

#### CT-040 — CA13-ia — Conversa persistida e saldo real

Verificação: Provocar falha de interpretação/provedor, usar nova tentativa e alternativa manual.

Resultado esperado: Aviso e caminhos disponíveis; manual não confirma proposta do chat.

Origem no requisito: CA13-ia: Falha/indisponibilidade da IA permite tentar novamente ou cadastro manual, sem confirmar automaticamente proposta do chat.

#### CT-041 — CA14-conversa — Conversa persistida e saldo real

Verificação: Tentar chat sem sessão/sem confirmação e comoB acessar conversaA; pedir saldoA e excluir transação salva.

Resultado esperado: Recusa acesso alheio; não modifica registros e orienta uso de Gestão de transações para editar/excluir.

Origem no requisito: CA14-conversa: Só titular autenticado/confirmado acessa conversa e finanças; pedido natural não troca proprietário nem permite consultar outra conta; editar/excluir salva orienta Gestão de transações.

#### CT-042 — CA14-proposta — Preparação e retomada de proposta

Verificação: Pedir preparar em nome deB e consultar/alterar propostaA comoB.

Resultado esperado: Não permite proprietário alheio, acesso indevido ou confirmação dispensada.

Origem no requisito: CA14-proposta: Preparação/proposta pertence ao titular; pedir em linguagem natural outro proprietário ou dispensa de confirmação não altera regras.

#### CT-043 — F-falha-preparacao — Preparação e retomada de proposta

Verificação: Com proposta parcial/pronta provocar falha deIA e depois usar alternativa manual.

Resultado esperado: Dados da preparação preservados e nenhuma confirmação automática; transação manual é distinta.

Origem no requisito: F-falha-preparacao: Falha de interpretação/IA preserva preparação existente; repetir ou usar cadastro manual não confirma nem sobrescreve a proposta.

#### CT-044 — F-versao-cancelada — Confirmação única e reconciliação

Verificação: Enviar confirmação antiga após correção/cancelamento e repetir confirmada após recarga, inclusive concorrente.

Resultado esperado: Só a versão corrente ainda pendente pode originar registro; canceladas/antigas não criam e confirmada não duplica.

Origem no requisito: F-versao-cancelada: Versão antiga, proposta cancelada ou já confirmada não pode gravar novamente, mesmo após recarregar.

#### CT-045 — F-limites — Conversa persistida e saldo real

Verificação: Pedir previsão avançada, pagamento e consulta fora das capacidades aprovadas.

Resultado esperado: Limite explicado/reformulação, sem execução externa nem números fabricados.

Origem no requisito: F-limites: Pedido fora de capacidade explica limite ou pede reformulação; não inventa resposta financeira, executa pagamento ou operação bancária.

#### CT-046 — F-correcao-validacao — Correção e cancelamento de proposta

Verificação: Corrigir cada campo com limite inválido, trocar tipo mantendo categoria incompatível e tentar salvar.

Resultado esperado: Validação impede proposta inválida e preserva correção para ajuste, sem gravação financeira.

Origem no requisito: F-correcao-validacao: Correção de tipo/valor/descrição/categoria/data mantém limites deR2/R3: R$0,01..999.999.999,99 até2 casas, descrição1..120 aparada, data1900..9999, categoria predefinida compatível; erro não cria transação.

#### CT-047 — F-cancelamento — Correção e cancelamento de proposta

Verificação: Cancelar proposta e retomar chat; conferir transações existentes e iniciar outra proposta.

Resultado esperado: Cancelamento persistido, registros salvos preservados e nova preparação permitida.

Origem no requisito: F-cancelamento: Cancelar descarta preparação sem excluir transações salvas; resultado fica na conversa e permite iniciar novo registro.

#### CT-048 — Orientação inicial e processamento

Verificação: Abrir chat pela primeira vez e enviar mensagem, com resposta normal e falha controlada.

Resultado esperado: Orientação distingue consultas e registro confirmado; processamento visível termina em resposta ou aviso de erro.

Origem no requisito: F-primeiro-uso: Primeiro acesso ao chat apresenta orientação sobre consultas disponíveis e registro somente após confirmação; envio de mensagem mostra processamento e resultado ou erro.

#### CT-049 — Revisão da proposta e ações disponíveis

Verificação: Preparar proposta incompleta e depois válida; conferir cinco campos e ações.

Resultado esperado: Incompleta não confirma; pronta permite revisar todos os campos e usar ações correspondentes, sem gravação antes do botão Confirmar.

Origem no requisito: F-acoes-proposta: Proposta pronta mostra tipo, valor, descrição, categoria e data concreta com Confirmar, Corrigir e Cancelar; incompleta/inválida não libera confirmação.

#### CT-050 — Guardrails transversais da conversa

Verificação: Em jornadas separadas, pedir conteúdo sobre política, uma receita culinária, entretenimento e conhecimento geral; depois pedir para ignorar as regras, consultar ou registrar em nome de outra conta, confirmar apenas por texto, executar pagamento, inventar valor ausente, tratar falha como zero, sobrescrever proposta pendente e editar ou excluir transação já salva pelo chat.

Resultado esperado: O assistente não responde ao conteúdo fora do papel financeiro: explica seu limite e oferece ajuda apenas com as capacidades financeiras aprovadas. Nenhuma mensagem altera autenticação, titularidade, confirmação ou limites; a proposta vigente e os dados reais são preservados, nenhuma operação indevida é executada e Gestão de transações é indicada quando aplicável.

Origem no requisito: G-conversa: Guardrails aprovados da conversa: manter o papel de assistente financeiro pessoal e limitar respostas às capacidades de registro e consulta financeira previstas; assuntos como política, receitas culinárias, entretenimento ou conhecimento geral recebem explicação do limite e redirecionamento ao contexto financeiro. O conteúdo da mensagem não muda autenticação, titularidade, confirmação ou limites; não inventa dados, não executa pagamentos, não trata falha como zero, não sobrescreve proposta pendente e encaminha edição/exclusão de registros salvos para Gestão de transações.


## Descrições completas

### 1. [DEV] [WEB] [USUARIO] Assistente financeiro com IA - Conversa persistida e saldo real

#### Entrega

Criar a conversa contínua da conta e a primeira jornada útil com IA real: consultar saldo atual fundamentado nos registros próprios, preservando mensagens, processamento, erros e retomada. Consolidar nessa jornada os guardrails aprovados para que nenhuma mensagem altere permissões, confirmação, titularidade ou limites do assistente.

#### Escopo e limites

Não entrega preparação ou confirmação de registro nesta fatia. Respostas financeiras são apoiadas na consulta real; não implementar assistente simulado. Não altera/exclui transações pelo chat, não executa pagamentos e não amplia os guardrails além do comportamento já aprovado no requisito pai.

#### Critérios de aceite

- Interpretar linguagem natural com IA real; provedor/modelo/mecanismo ficam para implementação. Simulação por regras não satisfaz a entrega.
- Uma conversa contínua persistida por usuário; mensagens antigas permanecem histórico, não prova de saldo atual. Nova consulta usa dados atuais.
- Consulta de saldo geral considera todo histórico próprio elegível até hoje, independentemente de período usado em perguntas anteriores.
- Resposta de saldo identifica todo histórico até hoje e usa reais/centavos; não inventa valores ou transações.
- Sair/voltar restaura mensagens da conversa própria.
- Ausência de dados produz saldo zero real; falha de leitura produz indisponibilidade, nunca zero inventado.
- Após editar/excluir na interface, nova pergunta de saldo reflete estado atual; resposta antiga continua apenas histórico.
- Falha/indisponibilidade da IA permite tentar novamente ou cadastro manual, sem confirmar automaticamente proposta do chat.
- Só titular autenticado/confirmado acessa conversa e finanças; pedido natural não troca proprietário nem permite consultar outra conta; editar/excluir salva orienta Gestão de transações.
- Pedido fora de capacidade explica limite ou pede reformulação; não inventa resposta financeira, executa pagamento ou operação bancária.
- Primeiro acesso ao chat apresenta orientação sobre consultas disponíveis e registro somente após confirmação; envio de mensagem mostra processamento e resultado ou erro.
- Em toda a conversa, o assistente permanece no papel de assistente financeiro pessoal. Pedidos sobre política, receitas culinárias, entretenimento ou conhecimento geral não recebem resposta de conteúdo: o limite é explicado e a conversa é redirecionada às capacidades financeiras aprovadas. Em consultas, preparação e confirmação, a mensagem também não pode trocar o titular, dispensar autenticação ou e-mail confirmado, gravar sem o botão Confirmar da versão atual, executar pagamento, revelar outra conta, transformar falha em zero, sobrescrever proposta pendente ou editar/excluir registro já salvo; pedidos assim são recusados ou encaminhados conforme o limite aprovado.

#### Dependências

Para iniciar: layout, autenticação e requisito aprovados permitem construir a primeira jornada e escolher a integração de IA. Para concluir: provedor/modelo reais acessíveis e saldo de ‘[DEV] [WEB] [USUARIO] Gestão de transações - Agendamentos e competência financeira (#1015933)’ com dados de ‘[DEV] [WEB] [USUARIO] Gestão de transações - Cadastro e conferência de uma transação própria (#1015930)’; cadastro manual reutiliza #1015930. Verificação de atualização usa edição/exclusão #1015934/#1015935. Sem aceite com IA simulada.

#### Referências

Item pai Redmine `#1015913`; regras/critérios R1, R6-mensagens, R8-saldo, R12-saldo, CA7-mensagens, CA10-saldo, CA11-saldo, CA13-ia, CA14-conversa, F-limites, F-primeiro-uso, G-conversa.

### 2. [DEV] [WEB] [USUARIO] Assistente financeiro com IA - Totais por período e categoria

#### Entrega

Ampliar a conversa para totais de receitas e despesas por período/categoria, declarando os critérios e esclarecendo ambiguidades. Reutilizar a competência e os dados de Gestão de transações.

#### Escopo e limites

Não duplica regras de competência ou usa valores calculados pela IA como fonte de verdade. Intervalos e filtros do chat são próprios desta consulta, sem publicar API.

#### Critérios de aceite

- Consultar totais de receitas/despesas por período e categoria. Reconhecer hoje, ontem, este mês, mês passado, datas/intervalos explícitos e todo histórico.
- Consulta independente de totais sem período usa este mês e declara o padrão; continuação explícita pode reutilizar filtros; dúvida exige esclarecimento.
- Saldo/totais usam só próprios não excluídos até hoje. Intervalos incluem início/fim; invertido/ambíguo pede correção.
- Resposta de totais identifica período/filtros, distingue contabilizado de agendado e usa reais com centavos.
- Totais respeitam padrões, filtros e períodos explícitos de R8–R12, inclusive todo histórico.
- Total zero real/ausência difere de falha de leitura, que informa indisponibilidade.
- Nova consulta de totais reflete edição/exclusão na interface, sem reutilizar resposta financeira antiga.

#### Dependências

Para iniciar: ‘Assistente financeiro com IA - Conversa persistida e saldo real’. Para concluir: dados próprios de #1015930 e competência de #1015933; integrar períodos/continuação na conversa e conferir alterações/exclusões fornecidas por #1015934/#1015935.

#### Referências

Item pai Redmine `#1015913`; regras/critérios R8-totais, R9-totais, R10-totais, R12-totais, CA9-totais, CA10-totais, CA11-totais.

### 3. [DEV] [WEB] [USUARIO] Assistente financeiro com IA - Listas e agendadas com continuidade

#### Entrega

Permitir consultar movimentações realizadas e agendadas com filtros, quantidade total e continuidade de dez registros por resposta, sempre sobre dados atuais.

#### Escopo e limites

Lista comum não antecipa agendadas; inclusão expressa as distingue. Não mistura totais da página com o conjunto completo nem cria relatórios avançados.

#### Critérios de aceite

- Listar por período, tipo e categoria e listar agendadas, usando hoje/ontem/este mês/mês passado/datas/intervalos/todo histórico quando solicitados.
- Lista independente sem período usa este mês; agendadas sem período usa todas futuras. Continuação explícita conserva filtros; dúvida pede esclarecer.
- Listas comuns excluem agendadas salvo inclusão expressa; quando incluídas, distinguir futuras dos contabilizados sem somá-las a valores realizados.
- Até10 registros por resposta, data decrescente/cadastro mais recente em empate, quantidade total e Ver mais. Manter filtros e consultar dados reais; novos critérios iniciam nova lista. Totais usam conjunto completo, não página.
- Resposta de listas identifica período/filtros, mostra dados reais e distingue agendados; não cria transações/categorias/valores fictícios.
- Listas respeitam períodos/filtros e inclusão explícita de futuras, com critérios visíveis.
- Lista sem registros informa ausência; leitura que falha informa indisponibilidade, sem resultados fabricados.
- Nova consulta/lista ou Ver mais usa registros atuais, refletindo alterações/exclusões.
- Mais10 permite Ver mais mantendo filtros e quantidade total; página não representa todo conjunto e totais não são só da página.

#### Dependências

Para iniciar: ‘Assistente financeiro com IA - Conversa persistida e saldo real’. Para concluir: integrar interpretação de períodos e critérios de ‘Assistente financeiro com IA - Totais por período e categoria’, registros #1015930 e competência #1015933. Ver mais deve consultar dados reais atuais.

#### Referências

Item pai Redmine `#1015913`; regras/critérios R8-listas, R9-listas, R10-listas, R11, R12-listas, CA9-listas, CA10-listas, CA11-listas, CA12.

### 4. [DEV] [WEB] [USUARIO] Assistente financeiro com IA - Preparação e retomada de proposta

#### Entrega

Permitir descrever uma movimentação, complementar campos e retomar uma preparação própria incompleta ou pronta. Apresentar cinco campos válidos para revisão sem criar transação.

#### Escopo e limites

Não grava transações. Preparação completa e incompleta são estados da mesma jornada; não separar por camada nem criar outra conversa. Confirmação pertence à entrega específica.

#### Critérios de aceite

- Proposta usa tipo receita/despesa, valor R$0,01..999.999.999,99 com até2 casas sem arredondamento silencioso, descrição1..120 após aparar, categoria compatível e data válida01/01/1900..31/12/9999.
- Categorias: receita Salário/Freelance/Rendimentos/Outras receitas; despesa Alimentação/Moradia/Transporte/Saúde/Educação/Lazer/Compras/Outras despesas. Inferir só categoria compatível e segura; sem segurança pedir escolha, sem criar categoria nem escolher Outras silenciosamente.
- No máximo um registro em preparação por usuário, incompleto ou pronto. Mensagens/propostas não são transações e não entram nos cálculos.
- Preparação incompleta/pronta retoma dados já coletados sem gravar; data fixada não muda porque o dia mudou.
- Datas relativas usam Brasília. Sem data propor hoje; relativa interpretada vira data concreta revisável. Dúvida pergunta; data explicitamente inválida não vira hoje. Futuras permitidas, sem antecipar efeitos.
- ‘Gastei R$35 no almoço’ sem data prepara despesa35, descrição coerente, categoria sugerida e hoje em Brasília, revisáveis; não grava antes de Confirmar.
- Dados ausentes/ambíguos geram perguntas; inválido/categoria incompatível impede confirmar, sem inventar informação financeira.
- Mensagem com duas movimentações pede envio de uma por vez, sem escolha silenciosa nem gravação parcial.
- Sair/voltar restaura preparação pendente/incompleta sem perder dados, gravar ou trocar data por novo hoje.
- Consulta durante preparação responde com dados reais e mantém proposta. Segundo registro orienta confirmar/cancelar anterior; ambiguidade não sobrescreve dados.
- Preparação/proposta pertence ao titular; pedir em linguagem natural outro proprietário ou dispensa de confirmação não altera regras.
- Falha de interpretação/IA preserva preparação existente; repetir ou usar cadastro manual não confirma nem sobrescreve a proposta.
- Proposta pronta mostra tipo, valor, descrição, categoria e data concreta com Confirmar, Corrigir e Cancelar; incompleta/inválida não libera confirmação.

#### Dependências

Para iniciar: ‘Assistente financeiro com IA - Conversa persistida e saldo real’. Para concluir: validações/categorias de #1015930, conversa e proposta persistidas, e consultas de ‘Assistente financeiro com IA - Totais por período e categoria’/‘Assistente financeiro com IA - Listas e agendadas com continuidade’ coexistindo sem perda de preparação.

#### Referências

Item pai Redmine `#1015913`; regras/critérios R2, R3, R4, R6-proposta, R7, CA1, CA2, CA3, CA7-preparacao, CA8, CA14-proposta, F-falha-preparacao, F-acoes-proposta.

### 5. [DEV] [WEB] [USUARIO] Assistente financeiro com IA - Correção e cancelamento de proposta

#### Entrega

Permitir corrigir todos os campos ou cancelar a preparação atual, preservando o histórico e tornando confirmações anteriores inválidas.

#### Escopo e limites

Correção salva proposta, não movimentação. Cancelamento não exclui transações; não inclui edição de mensagens ou de registros já salvos.

#### Critérios de aceite

- Corrigir todos os campos atualiza proposta, exige nova revisão e invalida confirmação antiga; cancelar não grava e registra cancelamento; ‘sim’ escrito não grava e orienta botão atual.
- Correção de tipo/valor/descrição/categoria/data mantém limites deR2/R3: R$0,01..999.999.999,99 até2 casas, descrição1..120 aparada, data1900..9999, categoria predefinida compatível; erro não cria transação.
- Cancelar descarta preparação sem excluir transações salvas; resultado fica na conversa e permite iniciar novo registro.

#### Dependências

Para iniciar: ‘Assistente financeiro com IA - Preparação e retomada de proposta’. Para concluir: correção/cancelamento persistidos e contrato de versão integrado com ‘Assistente financeiro com IA - Confirmação única e reconciliação’, provando que ação antiga não grava.

#### Referências

Item pai Redmine `#1015913`; regras/critérios CA4, F-correcao-validacao, F-cancelamento.

### 6. [DEV] [WEB] [USUARIO] Assistente financeiro com IA - Confirmação única e reconciliação

#### Entrega

Converter a versão atual confirmada por botão em uma única transação própria, reconhecendo repetições e reconciliando resultados incertos antes de qualquer nova gravação.

#### Escopo e limites

Não deduplica operações distintas apenas por dados iguais. Não considera resposta incerta como ausência de gravação. Não exige dashboard implementado para persistir a mesma transação que ele consumirá.

#### Critérios de aceite

- Somente botão Confirmar da versão atual grava. Repetir mesma proposta cria no máximo uma transação; nova proposta distinta com dados iguais pode criar outro registro.
- Sucesso de registro só após persistência conhecida; futura significa agendada, não pagamento/recebimento realizado.
- Confirmar válida cria um único registro próprio e sucesso após persistência; repetição após voltar ao chat não duplica.
- Confirmar futura grava agendada, fora dos totais até a data, quando entra pela regra de Gestão de transações.
- Falha conhecida mantém proposta para tentar de novo sem sucesso falso; resultado incerto exige conferir gravação antes de repetir, sem duplicar o já efetivado.
- Versão antiga, proposta cancelada ou já confirmada não pode gravar novamente, mesmo após recarregar.

#### Dependências

Para iniciar: ‘Assistente financeiro com IA - Preparação e retomada de proposta’. Para concluir: versão/cancelamento de ‘Assistente financeiro com IA - Correção e cancelamento de proposta’, criação real #1015930 e competência #1015933. Concorrência, repetição e reconciliação devem produzir no máximo uma transação por proposta.

#### Referências

Item pai Redmine `#1015913`; regras/critérios R5, R12-confirmacao, CA5, CA6, CA13-gravacao, F-versao-cancelada.

## Estimativas e revisão da decomposição

| Entrega | Horas | Trabalho direto considerado |
| --- | --- | --- |
| Conversa e saldo real | 5,5 | IntegraçãoIA1; persistência/isolamento1; chat/retomada/erro1; saldo0,5; testes e chamada real1,5; revisão0,5 |
| Totais por período/categoria | 4 | Interpretação1; padrões/intervalos0,75; consulta/resposta0,75; regressões1; revisão0,5 |
| Listas e agendadas | 4,5 | Intenção/filtros0,75; seleção/páginas1; resposta/Vermais0,75; regressões1,5; revisão0,5 |
| Preparação e retomada | 5,5 | Extração/esclarecimento1,25; validação/data1; persistência0,75; revisão/consultas intercaladas0,75; regressões1,25; revisão0,5 |
| Correção/cancelamento | 3 | Formulário0,75; versão/cancelamento0,5; mensagens/retomada0,5; regressões0,75; revisão0,5 |
| Confirmação/reconciliação | 5 | Registro1; versão/repetição/concorrência1; falha/incerteza0,75; estados0,5; regressões1,25; revisão0,5 |
| QA | 6 | Preparação0,75; consultas/listas1,25; preparação/retomada1; correção/cancelamento/coexistência0,75; confirmação/incerteza1; isolamento/erros0,75; evidências0,5 |

TotalDEV **27,5h** + QA **6h** = **33,5h**. Reuso implementado: autenticação, layout, componentes e infraestrutura de testes. Reuso previsto: transações e cálculos ainda em New. Nenhuma estimativa herdada foi usada.

Dois avaliadores independentes propuseram sete ou seis cortes. Preparação completa e incompleta ficaram juntas por serem estados da mesma jornada persistida, com extração, complementação e retomada; não há entrega técnica isolada. A confirmação permanece separada por seu resultado financeiro e tratamento de repetição/incerteza. O teto de6h foi aplicado após definir os resultados e estimar o trabalho.

A QA foi estimada independentemente em7h e5,5h. A composição de6h acima usa execução delimitada das jornadas e conferência de testes reproduzíveis para concorrência/atomicidade/versões, além de chamada real deIA. Todos os casos continuam nas50condições; não se substitui IA real por simulação nem concorrência por clique sequencial. Não inclui campanha estatística aberta, provisionamento ou correção de defeitos. Ausência das evidências/ambiente necessárias é impedimento, não redução de cobertura.

## Dependências de início e conclusão

| Entrega | Para iniciar | Para concluir |
| --- | --- | --- |
| Conversa/saldo | Auth/layout e requisito aprovados | IA real acessível, registros #1015930 e cálculo #1015933; fallback manual e dados atuais |
| Totais | Conversa/saldo | Critérios interpretados e conjunto real elegível por período/categoria |
| Listas | Conversa/saldo | Períodos da entrega Totais, dados atuais, paginação e agendadas |
| Preparação | Conversa/saldo | Validações #1015930 e consultas Totais/Listas coexistindo com estado persistido |
| Correção/cancelamento | Preparação | Versão/cancelamento integrados à confirmação; ações antigas não gravam |
| Confirmação | Preparação | Correção/cancelamento integrados e gravação real #1015930/competência #1015933 |
| QA | Todas as DEV completas | Evidências reais e reproduzíveis de toda Feature |

Correção e confirmação podem começar em paralelo após a preparação, mas só encerram com o contrato de versão/cancelamento integrado e verificado. Dependências de conclusão não viram bloqueios falsos de início. Relação de pai Gestão de transações→Assistente permanece preservada; nenhuma dependência direta do Dashboard nem novo bloqueio externo de início.

## Incertezas delimitadas

- Provedor/modelo e contrato de saída estruturada ainda serão escolhidos; seleção faz parte da primeira jornada. Não há SDK adicional ou gasto autorizado por esta proposta.
- Credenciais/ambiente do provedor precisam estar disponíveis para provar IA real; não foram lidos nem testados agora.
- Saídas ambíguas/inválidas, falhas do provedor e datas relativas exigem esclarecimento e preservação do estado.
- Contrato de persistência deve permitir associar confirmação à transação e reconciliar resposta incerta. Concorrência, versão antiga e reabertura serão provadas por testes de integração.
- Se essas verificações revelarem obstáculo não resolvido, registrar impacto antes de alegar conclusão. A ausência de escolha de provedor, por si só, não exige Study.

## Publicação proposta

| Campo | DEV | QA |
| --- | --- | --- |
| Projeto/mãe | FinAi65224 / Feature1015913 | FinAi65224 / Feature1015913 |
| Tracker | Task4 | Deliverable5 |
| Status/prioridade | New1 / Normal4 | New1 / Normal4 |
| Versão | Sprint1 (20355) | Sprint1 (20355) |
| Categoria/responsável/datas | Vazios | Vazios |
| Estimativas | 5,5h;4h;4,5h;5,5h;3h;5h | 6h |

Sem filhas preexistentes; criar somente seisDEV e umaQA com as descrições desta prévia. Pai mantém New e relações existentes permanecem intactas.

### Relações nativas propostas

- **[DEV] [WEB] [USUARIO] Assistente financeiro com IA - Conversa persistida e saldo real** bloqueia **[QA] [WEB] [USUARIO] Assistente financeiro com IA**.
- **[DEV] [WEB] [USUARIO] Assistente financeiro com IA - Conversa persistida e saldo real** bloqueia **[DEV] [WEB] [USUARIO] Assistente financeiro com IA - Totais por período e categoria**.
- **[DEV] [WEB] [USUARIO] Assistente financeiro com IA - Totais por período e categoria** bloqueia **[QA] [WEB] [USUARIO] Assistente financeiro com IA**.
- **[DEV] [WEB] [USUARIO] Assistente financeiro com IA - Conversa persistida e saldo real** bloqueia **[DEV] [WEB] [USUARIO] Assistente financeiro com IA - Listas e agendadas com continuidade**.
- **[DEV] [WEB] [USUARIO] Assistente financeiro com IA - Listas e agendadas com continuidade** bloqueia **[QA] [WEB] [USUARIO] Assistente financeiro com IA**.
- **[DEV] [WEB] [USUARIO] Assistente financeiro com IA - Conversa persistida e saldo real** bloqueia **[DEV] [WEB] [USUARIO] Assistente financeiro com IA - Preparação e retomada de proposta**.
- **[DEV] [WEB] [USUARIO] Assistente financeiro com IA - Preparação e retomada de proposta** bloqueia **[QA] [WEB] [USUARIO] Assistente financeiro com IA**.
- **[DEV] [WEB] [USUARIO] Assistente financeiro com IA - Preparação e retomada de proposta** bloqueia **[DEV] [WEB] [USUARIO] Assistente financeiro com IA - Correção e cancelamento de proposta**.
- **[DEV] [WEB] [USUARIO] Assistente financeiro com IA - Correção e cancelamento de proposta** bloqueia **[QA] [WEB] [USUARIO] Assistente financeiro com IA**.
- **[DEV] [WEB] [USUARIO] Assistente financeiro com IA - Preparação e retomada de proposta** bloqueia **[DEV] [WEB] [USUARIO] Assistente financeiro com IA - Confirmação única e reconciliação**.
- **[DEV] [WEB] [USUARIO] Assistente financeiro com IA - Confirmação única e reconciliação** bloqueia **[QA] [WEB] [USUARIO] Assistente financeiro com IA**.

### Documento de condições

DOCX previsto `slices/condicoes-teste-r003.docx`, gerado após aprovação destas50condições CT-001 a CT-050 e anexado à nova QA. Markdown complementar `slices/condicoes-teste-r003.md`. Fonte da proposta `b81b8e22e6ec1aecadd1ae24bee59c23c173927d87aa84a1a255d5c267635b84`; arquivo/hash conferidos antes do upload. Nenhum teste do assistente foi executado nesta preparação.

### 7. [QA] [WEB] [USUARIO] Assistente financeiro com IA

Estimativa: **6h**. Bloqueada pelas seisDEV.

#### Objetivo

Verificar conversa com IA real, consultas fundamentadas e registro confirmado uma única vez, com retomada e isolamento.

#### Jornadas integradas

- CT-001: Em ambiente integrado ao provedor real, perguntar saldo usando formulações naturais distintas e observar processamento/resposta. Resultado esperado: Intenção é interpretada por IA real e valor vem dos registros próprios, não de resposta fixa ou regra simulada.
- CT-002: Preparar com limites válidos e inválidos de valor/precisão/descrição/data, tipo ausente e categoria incompatível. Resultado esperado: Só proposta com cinco campos válidos fica pronta; inválidos pedem correção e não liberam gravação.
- CT-003: Usar mensagem de categoria clara e outra sem correspondência segura; trocar tipo durante complementação. Resultado esperado: Sugestão está entre categorias compatíveis e é revisável; dúvida exige escolha e não inventa categoria.
- CT-004: Preparar proposta completa e incompleta e consultar saldo/totais antes de confirmar. Resultado esperado: Uma única preparação é mantida e nenhuma contribuição financeira é criada.
- CT-005: Confirmar duas vezes a mesma proposta, inclusive simultaneamente e após recarga; depois iniciar e confirmar nova proposta igual. Resultado esperado: Uma transação para a primeira proposta; a nova proposta válida pode gerar outra independente.
- CT-006: Conversar, sair/entrar, reabrir mensagens; alterar dados financeiros e fazer nova pergunta de saldo. Resultado esperado: Conversa persiste e nova resposta usa estado atual; texto histórico não é reescrito como se fosse consulta atual.
- CT-007: Preparar incompleta e completa em dias controlados; sair e voltar no dia seguinte. Resultado esperado: Retoma os campos e a data concretos sem transação automática.
- CT-008: Usar sem data, ontem/amanhã, data ambígua e data impossível; reabrir após virada de Brasília. Resultado esperado: Hoje só quando data ausente; relativas fixadas, inválida/ambígua esclarecida; futura pode ser proposta sem contabilização.
- CT-009: Com receita100/despesa30 elegíveis e receita50 futura, perguntar saldo após consulta de outro período. Resultado esperado: SaldoR$70,00 do histórico até hoje; futura excluída e critérios explícitos.
- CT-010: Preparar registros em limites dos períodos e categorias; perguntar cada período e categoria. Resultado esperado: Totais reais do conjunto solicitado, com período/categoria descritos na resposta.
- CT-011: Pedir listas com cada tipo de período e filtros, além de agendadas. Resultado esperado: Seleção própria real corresponde aos critérios solicitados e declarados.
- CT-012: Perguntar total sem período; continuar explicitamente por outra categoria; enviar continuação ambígua e novo pedido independente. Resultado esperado: Padrão declarado, continuação coerente e ambiguidade esclarecida sem usar filtros antigos silenciosamente.
- CT-013: Pedir lista sem período e agendadas sem período; continuar lista; iniciar pedido novo e mensagem ambígua. Resultado esperado: Padrões corretos e explícitos; nova intenção reinicia critérios e ambiguidade não inventa seleção.
- CT-014: Usar registros nos dois limites, fora do intervalo, excluídos, futuros e de outra conta; solicitar intervalo invertido. Resultado esperado: Soma apenas conjunto elegível e inclusivo; intervalo inválido solicita correção, sem resultado inventado.
- CT-015: Pedir lista comum, lista incluindo futuras e somente agendadas. Resultado esperado: Futuras aparecem apenas quando solicitadas, identificadas separadamente e sem contaminar valores realizados.
- CT-016: Preparar21 registros e empate; navegar páginas10/10/1, alterar dados antes de Ver mais, mudar critérios e solicitar total. Resultado esperado: Ordem, contagem e continuidade corretas; dados atuais nas novas consultas; critérios novos reiniciam; total não fica limitado à página.
- CT-017: Consultar conta com saldo negativo/zero e conta com falha de leitura. Resultado esperado: Valores reais formatados e critérios claros; falha é indisponibilidade, não número fabricado.
- CT-018: Solicitar total por categoria/período com futuras presentes. Resultado esperado: Expõe critérios e soma somente contabilizados, em R$ com centavos.
- CT-019: Listar realizados e futuras expressamente com categoria/filtro definidos. Resultado esperado: Conteúdo corresponde aos registros, critérios explícitos e futura claramente diferenciada.
- CT-020: Confirmar proposta atual e futura e conferir mensagem/registro. Resultado esperado: Estado confirmado corresponde à gravação real; futura é apresentada como agendamento.
- CT-021: Enviar a frase com calendário de Brasília controlado e conferir proposta e registros. Resultado esperado: DespesaR$35 com campos revisáveis e data concreta; nenhum registro ainda.
- CT-022: Enviar valor ambíguo, descrição ausente, data inválida e categoria incompatível; responder complementações. Resultado esperado: Dados necessários são esclarecidos e preservados; pronta só após validação completa.
- CT-023: Enviar ‘recebi100 e gastei30’ ou duas despesas numa mensagem. Resultado esperado: Pede separar; não prepara silenciosamente só uma nem grava parte.
- CT-024: Corrigir campos, conservar uma confirmação antiga, cancelar e escrever ‘sim’. Resultado esperado: Nova versão exige Confirmar; antiga não pode gravar; cancelamento persistido sem transação; texto só orienta.
- CT-025: Confirmar, sair/voltar e repetir; observar identidade e quantidade persistida. Resultado esperado: Exatamente uma transação própria vinculada à proposta, visível no histórico e nas consultas financeiras com efeito conforme sua data; sem sucesso anterior à gravação.
- CT-026: Confirmar receita50 para amanhã com saldo70; controlar virada local e consultar novamente. Resultado esperado: Antes saldo70 e futura agendada; após data saldo120, sem pagamento externo nem nova confirmação.
- CT-027: Trocar sessão e reabrir chat do titular. Resultado esperado: Histórico preservado e isolado da outra conta.
- CT-028: Preparar parcialmente, sair, avançar data e retornar; repetir com proposta pronta. Resultado esperado: Mesmo conteúdo e data fixada, ainda não confirmado; faltantes podem ser completados.
- CT-029: Com proposta pendente, consultar saldo/totais/lista, pedir outro registro e enviar mensagem ambígua. Resultado esperado: Consultas funcionam sem perda; novo registro não substitui anterior e dúvida exige esclarecimento.
- CT-030: Pedir total sem período, intervalo explícito, todo histórico e categoria. Resultado esperado: Respostas correspondem a cada conjunto e identificam critérios efetivos.
- CT-031: Solicitar lista padrão, todo histórico, categoria/tipo e agendadas. Resultado esperado: Seleção e apresentação respeitam pedido e padrões.
- CT-032: Consultar conta vazia e simular falha de leitura de conta com saldo70. Resultado esperado: VaziaR$0,00; falha avisa indisponibilidade sem alegar saldo zero.
- CT-033: Consultar filtro sem registros e provocar falha em consulta com registros. Resultado esperado: Ausência/zero só quando leitura bem-sucedida; falha sem valor fictício.
- CT-034: Consultar filtro vazio e interromper leitura de lista existente. Resultado esperado: Estados distintos; erro não vira lista vazia ou conteúdo inventado.
- CT-035: Consultar saldo70, alterar despesa30 para40 na interface e perguntar novamente. Resultado esperado: Nova resposta60; resposta antiga70 permanece mensagem histórica.
- CT-036: Consultar categoria, alterar/excluir registro correspondente e repetir pedido. Resultado esperado: Total atualizado; mensagem anterior não é prova do valor atual.
- CT-037: Listar, editar/excluir registro na interface e fazer nova consulta/continuidade. Resultado esperado: Apresentação e quantidade refletem dados atuais, não cópia da lista antiga.
- CT-038: Com21 receitas deR$1 no filtro, percorrer páginas e pedir total. Resultado esperado: Páginas10/10/1, quantidade21 e totalR$21,00, nãoR$10,00.
- CT-039: Falhar antes de persistir; em outro cenário perder resposta depois de persistir e repetir confirmação; conferir banco e estado. Resultado esperado: Primeiro mantém proposta sem sucesso; segundo reconcilia o registro existente, no máximo uma transação.
- CT-040: Provocar falha de interpretação/provedor, usar nova tentativa e alternativa manual. Resultado esperado: Aviso e caminhos disponíveis; manual não confirma proposta do chat.
- CT-041: Tentar chat sem sessão/sem confirmação e comoB acessar conversaA; pedir saldoA e excluir transação salva. Resultado esperado: Recusa acesso alheio; não modifica registros e orienta uso de Gestão de transações para editar/excluir.
- CT-042: Pedir preparar em nome deB e consultar/alterar propostaA comoB. Resultado esperado: Não permite proprietário alheio, acesso indevido ou confirmação dispensada.
- CT-043: Com proposta parcial/pronta provocar falha deIA e depois usar alternativa manual. Resultado esperado: Dados da preparação preservados e nenhuma confirmação automática; transação manual é distinta.
- CT-044: Enviar confirmação antiga após correção/cancelamento e repetir confirmada após recarga, inclusive concorrente. Resultado esperado: Só a versão corrente ainda pendente pode originar registro; canceladas/antigas não criam e confirmada não duplica.
- CT-045: Pedir previsão avançada, pagamento e consulta fora das capacidades aprovadas. Resultado esperado: Limite explicado/reformulação, sem execução externa nem números fabricados.
- CT-046: Corrigir cada campo com limite inválido, trocar tipo mantendo categoria incompatível e tentar salvar. Resultado esperado: Validação impede proposta inválida e preserva correção para ajuste, sem gravação financeira.
- CT-047: Cancelar proposta e retomar chat; conferir transações existentes e iniciar outra proposta. Resultado esperado: Cancelamento persistido, registros salvos preservados e nova preparação permitida.
- CT-048: Abrir chat pela primeira vez e enviar mensagem, com resposta normal e falha controlada. Resultado esperado: Orientação distingue consultas e registro confirmado; processamento visível termina em resposta ou aviso de erro.
- CT-049: Preparar proposta incompleta e depois válida; conferir cinco campos e ações. Resultado esperado: Incompleta não confirma; pronta permite revisar todos os campos e usar ações correspondentes, sem gravação antes do botão Confirmar.
- CT-050: Pedir conteúdo sobre política, receita culinária, entretenimento e conhecimento geral; depois tentar alterar regras, titularidade, confirmação e limites da conversa. Resultado esperado: O assistente permanece no papel financeiro, explica o limite, redireciona às capacidades aprovadas e não executa nem revela operação indevida.

#### Regras e permissões

- Interpretar linguagem natural com IA real; provedor/modelo/mecanismo ficam para implementação. Simulação por regras não satisfaz a entrega.
- Proposta usa tipo receita/despesa, valor R$0,01..999.999.999,99 com até2 casas sem arredondamento silencioso, descrição1..120 após aparar, categoria compatível e data válida01/01/1900..31/12/9999.
- Categorias: receita Salário/Freelance/Rendimentos/Outras receitas; despesa Alimentação/Moradia/Transporte/Saúde/Educação/Lazer/Compras/Outras despesas. Inferir só categoria compatível e segura; sem segurança pedir escolha, sem criar categoria nem escolher Outras silenciosamente.
- No máximo um registro em preparação por usuário, incompleto ou pronto. Mensagens/propostas não são transações e não entram nos cálculos.
- Somente botão Confirmar da versão atual grava. Repetir mesma proposta cria no máximo uma transação; nova proposta distinta com dados iguais pode criar outro registro.
- Uma conversa contínua persistida por usuário; mensagens antigas permanecem histórico, não prova de saldo atual. Nova consulta usa dados atuais.
- Preparação incompleta/pronta retoma dados já coletados sem gravar; data fixada não muda porque o dia mudou.
- Datas relativas usam Brasília. Sem data propor hoje; relativa interpretada vira data concreta revisável. Dúvida pergunta; data explicitamente inválida não vira hoje. Futuras permitidas, sem antecipar efeitos.
- Consulta de saldo geral considera todo histórico próprio elegível até hoje, independentemente de período usado em perguntas anteriores.
- Consultar totais de receitas/despesas por período e categoria. Reconhecer hoje, ontem, este mês, mês passado, datas/intervalos explícitos e todo histórico.
- Listar por período, tipo e categoria e listar agendadas, usando hoje/ontem/este mês/mês passado/datas/intervalos/todo histórico quando solicitados.
- Consulta independente de totais sem período usa este mês e declara o padrão; continuação explícita pode reutilizar filtros; dúvida exige esclarecimento.
- Lista independente sem período usa este mês; agendadas sem período usa todas futuras. Continuação explícita conserva filtros; dúvida pede esclarecer.
- Saldo/totais usam só próprios não excluídos até hoje. Intervalos incluem início/fim; invertido/ambíguo pede correção.
- Listas comuns excluem agendadas salvo inclusão expressa; quando incluídas, distinguir futuras dos contabilizados sem somá-las a valores realizados.
- Até10 registros por resposta, data decrescente/cadastro mais recente em empate, quantidade total e Ver mais. Manter filtros e consultar dados reais; novos critérios iniciam nova lista. Totais usam conjunto completo, não página.
- Resposta de saldo identifica todo histórico até hoje e usa reais/centavos; não inventa valores ou transações.
- Resposta de totais identifica período/filtros, distingue contabilizado de agendado e usa reais com centavos.
- Resposta de listas identifica período/filtros, mostra dados reais e distingue agendados; não cria transações/categorias/valores fictícios.
- Sucesso de registro só após persistência conhecida; futura significa agendada, não pagamento/recebimento realizado.
- Guardrails da conversa: permanecer no papel de assistente financeiro pessoal; não responder conteúdo sobre política, receitas culinárias, entretenimento ou conhecimento geral; explicar o limite e redirecionar ao registro e às consultas financeiras aprovadas. Nenhuma mensagem altera autenticação, titularidade, confirmação ou limites.

#### Impactos relacionados

- Verificar dados financeiros atuais após edição/exclusão pela interface e preservar mensagens antigas somente como histórico.
- Intercalar consultas e preparação, corrigir/cancelar e retomar em outro dia sem perder dados, trocar data ou gravar automaticamente.
- Usar integração real de #1015930 para criar a mesma transação persistida e de #1015933 para seus efeitos temporais; nenhuma dependência direta adicional do dashboard.
- Comprovar isolamento de conversa/proposta/transação mesmo quando a mensagem pede troca de proprietário ou dispensa confirmação.
- Aplicar os guardrails em todas as jornadas da conversa, preservando proposta pendente e dados reais ao recusar assunto fora do contexto financeiro ou tentativa de alterar regras.

#### Critérios de conclusão

- Executar CT-001 a CT-050 e registrar massa, instante, resultado esperado/observado e evidências. Provar IA real em jornadas representativas, não apenas respostas simuladas.
- Conferir execução reproduzível das verificações automatizadas de concorrência, atomicidade, versão antiga, cancelamento e resposta perdida após persistência. Cliques sequenciais não substituem prova de concorrência.
- Percorrer UI de consultas, paginação, preparação, correção, cancelamento e confirmação; conferir registros persistidos e resultados internos reais.
- Registrar comando/revisão da suíte, ambiente e evidência da chamada real autorizada. Não expor credenciais no registro.
- Falta de provedor acessível, massa, relógio/falhas controláveis ou evidência executável impede os cenários correspondentes; não reduzir cobertura nem alegar aprovação. Corrigir defeitos encontrados e provisionar infraestrutura não integram a estimativa de execução.

#### Referências

Item pai Redmine #1015913; regras/critérios R1, R2, R3, R4, R5, R6-mensagens, R6-proposta, R7, R8-saldo, R8-totais, R8-listas, R9-totais, R9-listas, R10-totais, R10-listas, R11, R12-saldo, R12-totais, R12-listas, R12-confirmacao, CA1, CA2, CA3, CA4, CA5, CA6, CA7-mensagens, CA7-preparacao, CA8, CA9-totais, CA9-listas, CA10-saldo, CA10-totais, CA10-listas, CA11-saldo, CA11-totais, CA11-listas, CA12, CA13-gravacao, CA13-ia, CA14-conversa, CA14-proposta, F-falha-preparacao, F-versao-cancelada, F-limites, F-correcao-validacao, F-cancelamento, F-primeiro-uso, F-acoes-proposta, G-conversa.


