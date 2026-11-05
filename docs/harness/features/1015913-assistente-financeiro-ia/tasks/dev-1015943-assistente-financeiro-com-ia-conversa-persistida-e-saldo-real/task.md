# [DEV] [WEB] [USUARIO] Assistente financeiro com IA - Conversa persistida e saldo real

- Redmine: `#1015943`
- Tipo: `DEV`
- Tracker: Task (`4`)
- Item pai: `#1015913`
- Estimativa: `6h`

## Descrição

## Entrega

Criar a conversa contínua da conta e a primeira jornada útil com IA real: consultar saldo atual fundamentado nos registros próprios, preservando mensagens, processamento, erros e retomada. Consolidar nessa jornada os guardrails aprovados para que nenhuma mensagem altere permissões, confirmação, titularidade ou limites do assistente.

## Escopo e limites

Não entrega preparação ou confirmação de registro nesta fatia. Respostas financeiras são apoiadas na consulta real; não implementar assistente simulado. Não altera/exclui transações pelo chat, não executa pagamentos e não amplia os guardrails além do comportamento já aprovado no requisito pai.

## Critérios de aceite

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

## Dependências

Para iniciar: layout, autenticação e requisito aprovados permitem construir a primeira jornada e escolher a integração de IA. Para concluir: provedor/modelo reais acessíveis e saldo de ‘[DEV] [WEB] [USUARIO] Gestão de transações - Agendamentos e competência financeira (#1015933)’ com dados de ‘[DEV] [WEB] [USUARIO] Gestão de transações - Cadastro e conferência de uma transação própria (#1015930)’; cadastro manual reutiliza #1015930. Verificação de atualização usa edição/exclusão #1015934/#1015935. Sem aceite com IA simulada.

## Referências

Item pai Redmine #1015913; regras/critérios R1, R6-mensagens, R8-saldo, R12-saldo, CA7-mensagens, CA10-saldo, CA11-saldo, CA13-ia, CA14-conversa, F-limites, F-primeiro-uso, G-conversa.

<!-- project-slices-child:fecdb4f5536b06ca32ca73867d0cee93da8321bbb792ae7122f75ae82361e9a6 -->

## Relações

- `#1015943` blocks `#1015944`
- `#1015943` blocks `#1015945`
- `#1015943` blocks `#1015946`
- `#1015943` blocks `#1015949`
