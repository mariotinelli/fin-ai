# Histórico da entrevista — Acesso à conta pessoal

## Contexto herdado do catálogo aprovado

Item 2: [WEB] [USUARIO] Acesso à conta pessoal. Objetivo: criar e acessar uma conta própria, com cadastro, login, saída e recuperação de senha. Atores: visitante e titular da conta. Pré-requisito: adequação visual do FinAI, requisito publicado como #1016101, sem alegar implementação concluída. Esta entrevista pode continuar; as condições de implementação visual devem ser respeitadas depois.

Resultado: acesso ao espaço pessoal. Isolamento de transações, dashboard e consultas da IA pertence às Features responsáveis. A identidade visual vem da base, sem nova reformulação. O usuário já confirmou contas individuais, persistência no sistema e IA real. Não repetir essas perguntas. Todas as tasks antigas do Redmine permanecem excluídas; não são fonte de decisões ou implementação.

## Evidências do código atual

Cadastro público possui rota e formulário; campos nome, e-mail, senha e confirmação (app/Http/Requests/CreateUserRequest.php). E-mail único e até 255 caracteres; nome até 255. User implementa MustVerifyEmail e o dashboard exige auth + verified (app/Models/User.php e routes/web.php). Login/saída atuais em SessionController. Recuperação de senha existente; configuração prevê 60 minutos (config/auth.php). Esses são fatos de código, sujeitos ao aceite desta Feature, sem presumir entrega aprovada.

## Rodada inicial

### Q5 — Entrada de novos usuários

Contexto: o código atual expõe cadastro; contas individuais já foram confirmadas, mas não foi decidido se qualquer visitante pode criar a sua.
Por que importa: define a porta de entrada do produto e eventual necessidade de liberação externa.
Pergunta: o cadastro será aberto a qualquer pessoa ou dependerá de convite/liberação?
Opções: cadastro aberto permite criação direta; acesso restrito impede criação sem liberação e exige delimitar a forma de entrada.
Recomendação: cadastro aberto, coerente com o sistema pessoal e o fluxo de cadastro já presente.
Resposta: aguardando usuário.
Estado: bloqueante.

### Q6 — Confirmação do e-mail para acessar finanças

Contexto: o código atual restringe a área inicial a contas com e-mail confirmado. O requisito do MVP ainda não confirma essa regra de produto.
Por que importa: define o que a pessoa pode fazer logo após o cadastro e a necessidade da etapa de confirmação.
Pergunta: exigir confirmação do e-mail antes do acesso financeiro ou liberar logo após cadastrar?
Opções: confirmar antes mantém a área financeira restrita até o titular confirmar; acesso imediato permite usar as finanças sem esperar essa confirmação.
Recomendação: exigir confirmação antes, preservando o fluxo já representado no código.
Resposta: aguardando usuário.
Estado: bloqueante.

## Fronteiras ainda a reconciliar após esta rodada

Regras dos campos e senha; jornadas de recuperação; estados de falha e retomada aplicáveis. Reutilizar fatos do código e perguntar somente diferenças materiais. Não ampliar para gestão administrativa, redes sociais ou novas capacidades de passkeys/dois fatores sem demanda.


## Resolução de Q5 e Q6

Resposta exata do usuário: “q5. A q6. acredito que sem confirmar e-mail ele nao consegue acessar o sistema”.

Q5 resolvida: cadastro público, sem convite ou aprovação prévia. Q6 resolvida: confirmação obrigatória antes de acessar a área do sistema. Antes dela, manter orientação, reenvio e saída para concluir a jornada ou encerrá-la. A restrição não deve liberar telas protegidas indevidamente. O código atual de perfil exige apenas autenticação, portanto sua permissão deverá ser conciliada com essa regra de produto durante a implementação; o código não prevalece sobre a decisão do usuário.

### Q7 — Regra de senha no cadastro e na redefinição

Contexto: os formulários atuais compartilham o padrão de validação. A configuração instalada aplica em produção senha de 12 a 255 caracteres, com maiúscula, minúscula, número, símbolo e rejeição de senhas conhecidas em vazamentos; em outros ambientes esse mesmo padrão forte não está explicitamente garantido. Fato obtido por inspeção pontual da configuração instalada, sem importar dependências ou tasks antigas como requisitos.
Por que importa: define quais senhas são aceitas no cadastro e na recuperação; precisa ser a mesma regra verificável nos ambientes de aceite e uso.
Pergunta: adotar essa regra de produção para cadastro e redefinição do MVP, ou definir outra regra?
Opções: A — adotar a regra descrita, explicitamente consistente nos ambientes; B — usuário informa a regra alternativa desejada.
Recomendação: A, reaproveitando a regra já prevista para produção e evitando validações diferentes para o usuário e para o aceite.
Resposta: aguardando usuário.
Estado: bloqueante.

## Demais fatos para a proposta de requisito

Nome e e-mail obrigatórios até 255 caracteres; e-mail válido e único; senha com confirmação igual. Recuperação atual tem validade configurada de 60 minutos, informa resposta genérica independentemente de existência da conta e retorna ao login após redefinição. Login possui bloqueio temporário após cinco falhas e opção de lembrar acesso. Na proposta final, explicitar estados de validação, links inválidos/expirados/já usados, falhas de envio e retomada sem falso sucesso ou duplicação. Esses fluxos serão apresentados para aprovação integral, sem criar novas perguntas sobre cada detalhe claro.


## Resolução de Q7 e revisão final da entrevista

Resposta do usuário: “a”. Q7 resolvida: senha de 12 a 255 caracteres, com maiúscula, minúscula, número e símbolo, rejeitando senhas conhecidas em vazamentos; mesma validação no cadastro e na redefinição, nos ambientes de teste e uso.

Não restam perguntas funcionais abertas nesta Feature. Q5, Q6 e Q7 resolvidas pelas respostas acima. A proposta integral incorpora os fluxos de erro e retomada, requisitos de campos existentes, recuperação por 60 minutos, bloqueio de login após cinco falhas e lembrar acesso, para uma única revisão do requisito e das operações. Não é declaração de implementação ou teste funcional já concluído.

A prévia mantém a sequência própria do catálogo (posição 2), conforme a exceção já aprovada no primeiro item para desconsiderar todas as tasks anteriores. Não usa conteúdo nem sequência das issues antigas. Apenas #1016101, criada por este fluxo, é referenciada como pré-requisito visual.


## Prévia pronta para revisão

Requisito integral consolidado em feature.md, com Q5, Q6 e Q7 resolvidas. Plano e prévia completos em .flow/publications/69ab98d6-4dfa-4992-989d-66a892ecb79b/. A prévia apresenta criação, publicação e relação visual-blocks-acesso, incluindo IDs conhecidos e vinculação exclusiva ao ID retornado. Fontes, estado, todas as seções funcionais e operações foram conferidos. Aguardando uma única aprovação; nenhuma mutação remota realizada neste item.


## Aprovação e publicação concluídas

O usuário aprovou a prévia integral. Consentimento único registrado para requisito e plano, com criação, publicação e relação visual-blocks-acesso. Criada #1016104, Sprint 1, Sequencing 2, estado New preservado. Descrição integral validada pelo checker funcional. Relação 835 (#1016101 blocks #1016104) confirmada em ambos os extremos. Estados locais validados em completed. Não foi executada implementação. Baseline de comparação normaliza apenas CRLF/LF no conteúdo funcional; resposta original retida.
