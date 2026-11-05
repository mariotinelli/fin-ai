# Condições de teste

## Contexto

Preparar contas A/B confirmadas, conta não confirmada, transações reais de datas/categorias variadas,21registros elegíveis, futuras/excluídas, relógio de Brasília e falhas controladas. Executar jornadas representativas com provedor IA real escolhido na implementação e massa independente. Testes de integração com banco comprovam limites/isolamento/estado; concorrência, confirmação antiga e resposta perdida após commit exigem evidência automatizada reproduzível, além da jornada na interface. Não simular a IA como aceite deR1, nem substituir cálculo/registro por resposta inventada. Aplicar os guardrails aprovados a consultas, preparação, correção, cancelamento e confirmação; conteúdo da mensagem não altera permissões nem regras. Testar também pedidos fora do papel financeiro, incluindo política, receitas culinárias, entretenimento e conhecimento geral. Registrar comando/revisão/massa/instante/esperado/observado; nenhum teste do assistente executado nesta preparação.

### CT-001 — R1 — Conversa persistida e saldo real

Verificação: Em ambiente integrado ao provedor real, perguntar saldo usando formulações naturais distintas e observar processamento/resposta.

Resultado esperado: Intenção é interpretada por IA real e valor vem dos registros próprios, não de resposta fixa ou regra simulada.

Origem no requisito: R1: Interpretar linguagem natural com IA real; provedor/modelo/mecanismo ficam para implementação. Simulação por regras não satisfaz a entrega.

### CT-002 — R2 — Preparação e retomada de proposta

Verificação: Preparar com limites válidos e inválidos de valor/precisão/descrição/data, tipo ausente e categoria incompatível.

Resultado esperado: Só proposta com cinco campos válidos fica pronta; inválidos pedem correção e não liberam gravação.

Origem no requisito: R2: Proposta usa tipo receita/despesa, valor R$0,01..999.999.999,99 com até2 casas sem arredondamento silencioso, descrição1..120 após aparar, categoria compatível e data válida01/01/1900..31/12/9999.

### CT-003 — R3 — Preparação e retomada de proposta

Verificação: Usar mensagem de categoria clara e outra sem correspondência segura; trocar tipo durante complementação.

Resultado esperado: Sugestão está entre categorias compatíveis e é revisável; dúvida exige escolha e não inventa categoria.

Origem no requisito: R3: Categorias: receita Salário/Freelance/Rendimentos/Outras receitas; despesa Alimentação/Moradia/Transporte/Saúde/Educação/Lazer/Compras/Outras despesas. Inferir só categoria compatível e segura; sem segurança pedir escolha, sem criar categoria nem escolher Outras silenciosamente.

### CT-004 — R4 — Preparação e retomada de proposta

Verificação: Preparar proposta completa e incompleta e consultar saldo/totais antes de confirmar.

Resultado esperado: Uma única preparação é mantida e nenhuma contribuição financeira é criada.

Origem no requisito: R4: No máximo um registro em preparação por usuário, incompleto ou pronto. Mensagens/propostas não são transações e não entram nos cálculos.

### CT-005 — R5 — Confirmação única e reconciliação

Verificação: Confirmar duas vezes a mesma proposta, inclusive simultaneamente e após recarga; depois iniciar e confirmar nova proposta igual.

Resultado esperado: Uma transação para a primeira proposta; a nova proposta válida pode gerar outra independente.

Origem no requisito: R5: Somente botão Confirmar da versão atual grava. Repetir mesma proposta cria no máximo uma transação; nova proposta distinta com dados iguais pode criar outro registro.

### CT-006 — R6-mensagens — Conversa persistida e saldo real

Verificação: Conversar, sair/entrar, reabrir mensagens; alterar dados financeiros e fazer nova pergunta de saldo.

Resultado esperado: Conversa persiste e nova resposta usa estado atual; texto histórico não é reescrito como se fosse consulta atual.

Origem no requisito: R6-mensagens: Uma conversa contínua persistida por usuário; mensagens antigas permanecem histórico, não prova de saldo atual. Nova consulta usa dados atuais.

### CT-007 — R6-proposta — Preparação e retomada de proposta

Verificação: Preparar incompleta e completa em dias controlados; sair e voltar no dia seguinte.

Resultado esperado: Retoma os campos e a data concretos sem transação automática.

Origem no requisito: R6-proposta: Preparação incompleta/pronta retoma dados já coletados sem gravar; data fixada não muda porque o dia mudou.

### CT-008 — R7 — Preparação e retomada de proposta

Verificação: Usar sem data, ontem/amanhã, data ambígua e data impossível; reabrir após virada de Brasília.

Resultado esperado: Hoje só quando data ausente; relativas fixadas, inválida/ambígua esclarecida; futura pode ser proposta sem contabilização.

Origem no requisito: R7: Datas relativas usam Brasília. Sem data propor hoje; relativa interpretada vira data concreta revisável. Dúvida pergunta; data explicitamente inválida não vira hoje. Futuras permitidas, sem antecipar efeitos.

### CT-009 — R8-saldo — Conversa persistida e saldo real

Verificação: Com receita100/despesa30 elegíveis e receita50 futura, perguntar saldo após consulta de outro período.

Resultado esperado: SaldoR$70,00 do histórico até hoje; futura excluída e critérios explícitos.

Origem no requisito: R8-saldo: Consulta de saldo geral considera todo histórico próprio elegível até hoje, independentemente de período usado em perguntas anteriores.

### CT-010 — R8-totais — Totais por período e categoria

Verificação: Preparar registros em limites dos períodos e categorias; perguntar cada período e categoria.

Resultado esperado: Totais reais do conjunto solicitado, com período/categoria descritos na resposta.

Origem no requisito: R8-totais: Consultar totais de receitas/despesas por período e categoria. Reconhecer hoje, ontem, este mês, mês passado, datas/intervalos explícitos e todo histórico.

### CT-011 — R8-listas — Listas e agendadas com continuidade

Verificação: Pedir listas com cada tipo de período e filtros, além de agendadas.

Resultado esperado: Seleção própria real corresponde aos critérios solicitados e declarados.

Origem no requisito: R8-listas: Listar por período, tipo e categoria e listar agendadas, usando hoje/ontem/este mês/mês passado/datas/intervalos/todo histórico quando solicitados.

### CT-012 — R9-totais — Totais por período e categoria

Verificação: Perguntar total sem período; continuar explicitamente por outra categoria; enviar continuação ambígua e novo pedido independente.

Resultado esperado: Padrão declarado, continuação coerente e ambiguidade esclarecida sem usar filtros antigos silenciosamente.

Origem no requisito: R9-totais: Consulta independente de totais sem período usa este mês e declara o padrão; continuação explícita pode reutilizar filtros; dúvida exige esclarecimento.

### CT-013 — R9-listas — Listas e agendadas com continuidade

Verificação: Pedir lista sem período e agendadas sem período; continuar lista; iniciar pedido novo e mensagem ambígua.

Resultado esperado: Padrões corretos e explícitos; nova intenção reinicia critérios e ambiguidade não inventa seleção.

Origem no requisito: R9-listas: Lista independente sem período usa este mês; agendadas sem período usa todas futuras. Continuação explícita conserva filtros; dúvida pede esclarecer.

### CT-014 — R10-totais — Totais por período e categoria

Verificação: Usar registros nos dois limites, fora do intervalo, excluídos, futuros e de outra conta; solicitar intervalo invertido.

Resultado esperado: Soma apenas conjunto elegível e inclusivo; intervalo inválido solicita correção, sem resultado inventado.

Origem no requisito: R10-totais: Saldo/totais usam só próprios não excluídos até hoje. Intervalos incluem início/fim; invertido/ambíguo pede correção.

### CT-015 — R10-listas — Listas e agendadas com continuidade

Verificação: Pedir lista comum, lista incluindo futuras e somente agendadas.

Resultado esperado: Futuras aparecem apenas quando solicitadas, identificadas separadamente e sem contaminar valores realizados.

Origem no requisito: R10-listas: Listas comuns excluem agendadas salvo inclusão expressa; quando incluídas, distinguir futuras dos contabilizados sem somá-las a valores realizados.

### CT-016 — R11 — Listas e agendadas com continuidade

Verificação: Preparar21 registros e empate; navegar páginas10/10/1, alterar dados antes de Ver mais, mudar critérios e solicitar total.

Resultado esperado: Ordem, contagem e continuidade corretas; dados atuais nas novas consultas; critérios novos reiniciam; total não fica limitado à página.

Origem no requisito: R11: Até10 registros por resposta, data decrescente/cadastro mais recente em empate, quantidade total e Ver mais. Manter filtros e consultar dados reais; novos critérios iniciam nova lista. Totais usam conjunto completo, não página.

### CT-017 — R12-saldo — Conversa persistida e saldo real

Verificação: Consultar conta com saldo negativo/zero e conta com falha de leitura.

Resultado esperado: Valores reais formatados e critérios claros; falha é indisponibilidade, não número fabricado.

Origem no requisito: R12-saldo: Resposta de saldo identifica todo histórico até hoje e usa reais/centavos; não inventa valores ou transações.

### CT-018 — R12-totais — Totais por período e categoria

Verificação: Solicitar total por categoria/período com futuras presentes.

Resultado esperado: Expõe critérios e soma somente contabilizados, em R$ com centavos.

Origem no requisito: R12-totais: Resposta de totais identifica período/filtros, distingue contabilizado de agendado e usa reais com centavos.

### CT-019 — R12-listas — Listas e agendadas com continuidade

Verificação: Listar realizados e futuras expressamente com categoria/filtro definidos.

Resultado esperado: Conteúdo corresponde aos registros, critérios explícitos e futura claramente diferenciada.

Origem no requisito: R12-listas: Resposta de listas identifica período/filtros, mostra dados reais e distingue agendados; não cria transações/categorias/valores fictícios.

### CT-020 — R12-confirmacao — Confirmação única e reconciliação

Verificação: Confirmar proposta atual e futura e conferir mensagem/registro.

Resultado esperado: Estado confirmado corresponde à gravação real; futura é apresentada como agendamento.

Origem no requisito: R12-confirmacao: Sucesso de registro só após persistência conhecida; futura significa agendada, não pagamento/recebimento realizado.

### CT-021 — CA1 — Preparação e retomada de proposta

Verificação: Enviar a frase com calendário de Brasília controlado e conferir proposta e registros.

Resultado esperado: DespesaR$35 com campos revisáveis e data concreta; nenhum registro ainda.

Origem no requisito: CA1: ‘Gastei R$35 no almoço’ sem data prepara despesa35, descrição coerente, categoria sugerida e hoje em Brasília, revisáveis; não grava antes de Confirmar.

### CT-022 — CA2 — Preparação e retomada de proposta

Verificação: Enviar valor ambíguo, descrição ausente, data inválida e categoria incompatível; responder complementações.

Resultado esperado: Dados necessários são esclarecidos e preservados; pronta só após validação completa.

Origem no requisito: CA2: Dados ausentes/ambíguos geram perguntas; inválido/categoria incompatível impede confirmar, sem inventar informação financeira.

### CT-023 — CA3 — Preparação e retomada de proposta

Verificação: Enviar ‘recebi100 e gastei30’ ou duas despesas numa mensagem.

Resultado esperado: Pede separar; não prepara silenciosamente só uma nem grava parte.

Origem no requisito: CA3: Mensagem com duas movimentações pede envio de uma por vez, sem escolha silenciosa nem gravação parcial.

### CT-024 — CA4 — Correção e cancelamento de proposta

Verificação: Corrigir campos, conservar uma confirmação antiga, cancelar e escrever ‘sim’.

Resultado esperado: Nova versão exige Confirmar; antiga não pode gravar; cancelamento persistido sem transação; texto só orienta.

Origem no requisito: CA4: Corrigir todos os campos atualiza proposta, exige nova revisão e invalida confirmação antiga; cancelar não grava e registra cancelamento; ‘sim’ escrito não grava e orienta botão atual.

### CT-025 — CA5 — Confirmação única e reconciliação

Verificação: Confirmar, sair/voltar e repetir; observar identidade e quantidade persistida.

Resultado esperado: Exatamente uma transação própria vinculada à proposta, visível no histórico e nas consultas financeiras com efeito conforme sua data; sem sucesso anterior à gravação.

Origem no requisito: CA5: Confirmar válida cria um único registro próprio e sucesso após persistência; repetição após voltar ao chat não duplica.

### CT-026 — CA6 — Confirmação única e reconciliação

Verificação: Confirmar receita50 para amanhã com saldo70; controlar virada local e consultar novamente.

Resultado esperado: Antes saldo70 e futura agendada; após data saldo120, sem pagamento externo nem nova confirmação.

Origem no requisito: CA6: Confirmar futura grava agendada, fora dos totais até a data, quando entra pela regra de Gestão de transações.

### CT-027 — CA7-mensagens — Conversa persistida e saldo real

Verificação: Trocar sessão e reabrir chat do titular.

Resultado esperado: Histórico preservado e isolado da outra conta.

Origem no requisito: CA7-mensagens: Sair/voltar restaura mensagens da conversa própria.

### CT-028 — CA7-preparacao — Preparação e retomada de proposta

Verificação: Preparar parcialmente, sair, avançar data e retornar; repetir com proposta pronta.

Resultado esperado: Mesmo conteúdo e data fixada, ainda não confirmado; faltantes podem ser completados.

Origem no requisito: CA7-preparacao: Sair/voltar restaura preparação pendente/incompleta sem perder dados, gravar ou trocar data por novo hoje.

### CT-029 — CA8 — Preparação e retomada de proposta

Verificação: Com proposta pendente, consultar saldo/totais/lista, pedir outro registro e enviar mensagem ambígua.

Resultado esperado: Consultas funcionam sem perda; novo registro não substitui anterior e dúvida exige esclarecimento.

Origem no requisito: CA8: Consulta durante preparação responde com dados reais e mantém proposta. Segundo registro orienta confirmar/cancelar anterior; ambiguidade não sobrescreve dados.

### CT-030 — CA9-totais — Totais por período e categoria

Verificação: Pedir total sem período, intervalo explícito, todo histórico e categoria.

Resultado esperado: Respostas correspondem a cada conjunto e identificam critérios efetivos.

Origem no requisito: CA9-totais: Totais respeitam padrões, filtros e períodos explícitos de R8–R12, inclusive todo histórico.

### CT-031 — CA9-listas — Listas e agendadas com continuidade

Verificação: Solicitar lista padrão, todo histórico, categoria/tipo e agendadas.

Resultado esperado: Seleção e apresentação respeitam pedido e padrões.

Origem no requisito: CA9-listas: Listas respeitam períodos/filtros e inclusão explícita de futuras, com critérios visíveis.

### CT-032 — CA10-saldo — Conversa persistida e saldo real

Verificação: Consultar conta vazia e simular falha de leitura de conta com saldo70.

Resultado esperado: VaziaR$0,00; falha avisa indisponibilidade sem alegar saldo zero.

Origem no requisito: CA10-saldo: Ausência de dados produz saldo zero real; falha de leitura produz indisponibilidade, nunca zero inventado.

### CT-033 — CA10-totais — Totais por período e categoria

Verificação: Consultar filtro sem registros e provocar falha em consulta com registros.

Resultado esperado: Ausência/zero só quando leitura bem-sucedida; falha sem valor fictício.

Origem no requisito: CA10-totais: Total zero real/ausência difere de falha de leitura, que informa indisponibilidade.

### CT-034 — CA10-listas — Listas e agendadas com continuidade

Verificação: Consultar filtro vazio e interromper leitura de lista existente.

Resultado esperado: Estados distintos; erro não vira lista vazia ou conteúdo inventado.

Origem no requisito: CA10-listas: Lista sem registros informa ausência; leitura que falha informa indisponibilidade, sem resultados fabricados.

### CT-035 — CA11-saldo — Conversa persistida e saldo real

Verificação: Consultar saldo70, alterar despesa30 para40 na interface e perguntar novamente.

Resultado esperado: Nova resposta60; resposta antiga70 permanece mensagem histórica.

Origem no requisito: CA11-saldo: Após editar/excluir na interface, nova pergunta de saldo reflete estado atual; resposta antiga continua apenas histórico.

### CT-036 — CA11-totais — Totais por período e categoria

Verificação: Consultar categoria, alterar/excluir registro correspondente e repetir pedido.

Resultado esperado: Total atualizado; mensagem anterior não é prova do valor atual.

Origem no requisito: CA11-totais: Nova consulta de totais reflete edição/exclusão na interface, sem reutilizar resposta financeira antiga.

### CT-037 — CA11-listas — Listas e agendadas com continuidade

Verificação: Listar, editar/excluir registro na interface e fazer nova consulta/continuidade.

Resultado esperado: Apresentação e quantidade refletem dados atuais, não cópia da lista antiga.

Origem no requisito: CA11-listas: Nova consulta/lista ou Ver mais usa registros atuais, refletindo alterações/exclusões.

### CT-038 — CA12 — Listas e agendadas com continuidade

Verificação: Com21 receitas deR$1 no filtro, percorrer páginas e pedir total.

Resultado esperado: Páginas10/10/1, quantidade21 e totalR$21,00, nãoR$10,00.

Origem no requisito: CA12: Mais10 permite Ver mais mantendo filtros e quantidade total; página não representa todo conjunto e totais não são só da página.

### CT-039 — CA13-gravacao — Confirmação única e reconciliação

Verificação: Falhar antes de persistir; em outro cenário perder resposta depois de persistir e repetir confirmação; conferir banco e estado.

Resultado esperado: Primeiro mantém proposta sem sucesso; segundo reconcilia o registro existente, no máximo uma transação.

Origem no requisito: CA13-gravacao: Falha conhecida mantém proposta para tentar de novo sem sucesso falso; resultado incerto exige conferir gravação antes de repetir, sem duplicar o já efetivado.

### CT-040 — CA13-ia — Conversa persistida e saldo real

Verificação: Provocar falha de interpretação/provedor, usar nova tentativa e alternativa manual.

Resultado esperado: Aviso e caminhos disponíveis; manual não confirma proposta do chat.

Origem no requisito: CA13-ia: Falha/indisponibilidade da IA permite tentar novamente ou cadastro manual, sem confirmar automaticamente proposta do chat.

### CT-041 — CA14-conversa — Conversa persistida e saldo real

Verificação: Tentar chat sem sessão/sem confirmação e comoB acessar conversaA; pedir saldoA e excluir transação salva.

Resultado esperado: Recusa acesso alheio; não modifica registros e orienta uso de Gestão de transações para editar/excluir.

Origem no requisito: CA14-conversa: Só titular autenticado/confirmado acessa conversa e finanças; pedido natural não troca proprietário nem permite consultar outra conta; editar/excluir salva orienta Gestão de transações.

### CT-042 — CA14-proposta — Preparação e retomada de proposta

Verificação: Pedir preparar em nome deB e consultar/alterar propostaA comoB.

Resultado esperado: Não permite proprietário alheio, acesso indevido ou confirmação dispensada.

Origem no requisito: CA14-proposta: Preparação/proposta pertence ao titular; pedir em linguagem natural outro proprietário ou dispensa de confirmação não altera regras.

### CT-043 — F-falha-preparacao — Preparação e retomada de proposta

Verificação: Com proposta parcial/pronta provocar falha deIA e depois usar alternativa manual.

Resultado esperado: Dados da preparação preservados e nenhuma confirmação automática; transação manual é distinta.

Origem no requisito: F-falha-preparacao: Falha de interpretação/IA preserva preparação existente; repetir ou usar cadastro manual não confirma nem sobrescreve a proposta.

### CT-044 — F-versao-cancelada — Confirmação única e reconciliação

Verificação: Enviar confirmação antiga após correção/cancelamento e repetir confirmada após recarga, inclusive concorrente.

Resultado esperado: Só a versão corrente ainda pendente pode originar registro; canceladas/antigas não criam e confirmada não duplica.

Origem no requisito: F-versao-cancelada: Versão antiga, proposta cancelada ou já confirmada não pode gravar novamente, mesmo após recarregar.

### CT-045 — F-limites — Conversa persistida e saldo real

Verificação: Pedir previsão avançada, pagamento e consulta fora das capacidades aprovadas.

Resultado esperado: Limite explicado/reformulação, sem execução externa nem números fabricados.

Origem no requisito: F-limites: Pedido fora de capacidade explica limite ou pede reformulação; não inventa resposta financeira, executa pagamento ou operação bancária.

### CT-046 — F-correcao-validacao — Correção e cancelamento de proposta

Verificação: Corrigir cada campo com limite inválido, trocar tipo mantendo categoria incompatível e tentar salvar.

Resultado esperado: Validação impede proposta inválida e preserva correção para ajuste, sem gravação financeira.

Origem no requisito: F-correcao-validacao: Correção de tipo/valor/descrição/categoria/data mantém limites deR2/R3: R$0,01..999.999.999,99 até2 casas, descrição1..120 aparada, data1900..9999, categoria predefinida compatível; erro não cria transação.

### CT-047 — F-cancelamento — Correção e cancelamento de proposta

Verificação: Cancelar proposta e retomar chat; conferir transações existentes e iniciar outra proposta.

Resultado esperado: Cancelamento persistido, registros salvos preservados e nova preparação permitida.

Origem no requisito: F-cancelamento: Cancelar descarta preparação sem excluir transações salvas; resultado fica na conversa e permite iniciar novo registro.

### CT-048 — Orientação inicial e processamento

Verificação: Abrir chat pela primeira vez e enviar mensagem, com resposta normal e falha controlada.

Resultado esperado: Orientação distingue consultas e registro confirmado; processamento visível termina em resposta ou aviso de erro.

Origem no requisito: F-primeiro-uso: Primeiro acesso ao chat apresenta orientação sobre consultas disponíveis e registro somente após confirmação; envio de mensagem mostra processamento e resultado ou erro.

### CT-049 — Revisão da proposta e ações disponíveis

Verificação: Preparar proposta incompleta e depois válida; conferir cinco campos e ações.

Resultado esperado: Incompleta não confirma; pronta permite revisar todos os campos e usar ações correspondentes, sem gravação antes do botão Confirmar.

Origem no requisito: F-acoes-proposta: Proposta pronta mostra tipo, valor, descrição, categoria e data concreta com Confirmar, Corrigir e Cancelar; incompleta/inválida não libera confirmação.

### CT-050 — Guardrails transversais da conversa

Verificação: Em jornadas separadas, pedir conteúdo sobre política, uma receita culinária, entretenimento e conhecimento geral; depois pedir para ignorar as regras, consultar ou registrar em nome de outra conta, confirmar apenas por texto, executar pagamento, inventar valor ausente, tratar falha como zero, sobrescrever proposta pendente e editar ou excluir transação já salva pelo chat.

Resultado esperado: O assistente não responde ao conteúdo fora do papel financeiro: explica seu limite e oferece ajuda apenas com as capacidades financeiras aprovadas. Nenhuma mensagem altera autenticação, titularidade, confirmação ou limites; a proposta vigente e os dados reais são preservados, nenhuma operação indevida é executada e Gestão de transações é indicada quando aplicável.

Origem no requisito: G-conversa: Guardrails aprovados da conversa: manter o papel de assistente financeiro pessoal e limitar respostas às capacidades de registro e consulta financeira previstas; assuntos como política, receitas culinárias, entretenimento ou conhecimento geral recebem explicação do limite e redirecionamento ao contexto financeiro. O conteúdo da mensagem não muda autenticação, titularidade, confirmação ou limites; não inventa dados, não executa pagamentos, não trata falha como zero, não sobrescreve proposta pendente e encaminha edição/exclusão de registros salvos para Gestão de transações.
