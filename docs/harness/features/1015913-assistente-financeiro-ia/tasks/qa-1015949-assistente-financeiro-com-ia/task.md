# [QA] [WEB] [USUARIO] Assistente financeiro com IA

- Redmine: `#1015949`
- Tipo: `QA`
- Tracker: Deliverable (`5`)
- Item pai: `#1015913`
- Estimativa: `3h`

## Descrição

## Objetivo

Verificar conversa com IA real, consultas fundamentadas e registro confirmado uma única vez, com retomada e isolamento.

## Jornadas integradas

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

## Regras e permissões

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

## Impactos relacionados

- Verificar dados financeiros atuais após edição/exclusão pela interface e preservar mensagens antigas somente como histórico.
- Intercalar consultas e preparação, corrigir/cancelar e retomar em outro dia sem perder dados, trocar data ou gravar automaticamente.
- Usar integração real de #1015930 para criar a mesma transação persistida e de #1015933 para seus efeitos temporais; nenhuma dependência direta adicional do dashboard.
- Comprovar isolamento de conversa/proposta/transação mesmo quando a mensagem pede troca de proprietário ou dispensa confirmação.
- Aplicar os guardrails em todas as jornadas da conversa, preservando proposta pendente e dados reais ao recusar assunto fora do contexto financeiro ou tentativa de alterar regras.

## Critérios de conclusão

- Executar CT-001 a CT-050 e registrar massa, instante, resultado esperado/observado e evidências. Provar IA real em jornadas representativas, não apenas respostas simuladas.
- Conferir execução reproduzível das verificações automatizadas de concorrência, atomicidade, versão antiga, cancelamento e resposta perdida após persistência. Cliques sequenciais não substituem prova de concorrência.
- Percorrer UI de consultas, paginação, preparação, correção, cancelamento e confirmação; conferir registros persistidos e resultados internos reais.
- Registrar comando/revisão da suíte, ambiente e evidência da chamada real autorizada. Não expor credenciais no registro.
- Falta de provedor acessível, massa, relógio/falhas controláveis ou evidência executável impede os cenários correspondentes; não reduzir cobertura nem alegar aprovação. Corrigir defeitos encontrados e provisionar infraestrutura não integram a estimativa de execução.

## Referências

Item pai Redmine #1015913; regras/critérios R1, R2, R3, R4, R5, R6-mensagens, R6-proposta, R7, R8-saldo, R8-totais, R8-listas, R9-totais, R9-listas, R10-totais, R10-listas, R11, R12-saldo, R12-totais, R12-listas, R12-confirmacao, CA1, CA2, CA3, CA4, CA5, CA6, CA7-mensagens, CA7-preparacao, CA8, CA9-totais, CA9-listas, CA10-saldo, CA10-totais, CA10-listas, CA11-saldo, CA11-totais, CA11-listas, CA12, CA13-gravacao, CA13-ia, CA14-conversa, CA14-proposta, F-falha-preparacao, F-versao-cancelada, F-limites, F-correcao-validacao, F-cancelamento, F-primeiro-uso, F-acoes-proposta, G-conversa.

<!-- project-slices-child:ee1d47fd568342a47906cfb3e51d604b9d2b91d97e588195237dfe4d814134f8 -->

## Relações

- `#1015943` blocks `#1015949`
- `#1015944` blocks `#1015949`
- `#1015945` blocks `#1015949`
- `#1015946` blocks `#1015949`
- `#1015947` blocks `#1015949`
- `#1015948` blocks `#1015949`
