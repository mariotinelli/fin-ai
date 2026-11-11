# Prévia completa — Acesso à conta pessoal

Proposta ainda não aprovada para publicação. Um único consentimento cobre o requisito integral e exatamente as três operações abaixo.

## Destino e escolhas de publicação

- Servidor https://redmine.remsoft.com.br; identidade verificada Mário Tinelli (131789).
- Projeto FinAi (65224); Sprint 1 (20355), selecionada pelo usuário e confirmada aberta.
- Feature, tracker 2; estado inicial New (1), sem categoria. Tipo e título herdados do catálogo aprovado; não há categoria disponível na consulta de metadados.
- Título: [WEB] [USUARIO] Acesso à conta pessoal.
- Sequencing: campo 2, valor 2, correspondente à segunda posição deste catálogo. Mantém a sequência própria iniciada em 1 na primeira Feature, conforme exceção explicitamente aprovada para desconsiderar todas as tasks antigas. Não utiliza conteúdo ou sequência das issues antigas e não alega máximo histórico observado.
- Nova demanda deste fluxo; nenhuma task antiga é reutilizada ou importada.
- Pré-requisito: #1016101, [WEB] [USUARIO] Adequação visual do FinAI, criada neste fluxo. O requisito está publicado, mas a issue continua New; não se afirma implementação concluída.

## Operações propostas

1. Criar uma nova Feature com os atributos exatos e a descrição funcional integral abaixo.
2. Persistir o ID retornado e atualizar somente a descrição e fixed_version_id dessa mesma issue, acrescentando o caminho definitivo do requisito e sua atribuição. {{created_issue_id}} é substituído exclusivamente pelo ID retornado na criação. Preservar estado remoto e qualquer texto externo à seção gerenciada.
3. Criar ou reconciliar a relação nativa blocks, chave visual-blocks-acesso, da issue #1016101 para a nova issue {{created_issue_id}}. A adequação visual é pré-requisito da implementação do acesso; uma relação equivalente já existente não é duplicada. A relação não muda o estado de nenhuma issue.

Nenhuma outra issue é criada, excluída, encerrada ou alterada. A #1016101 recebe somente o vínculo de dependência descrito. As tasks antigas continuam desconsideradas.

## Requisito canônico integral

# [WEB] [USUARIO] Acesso à conta pessoal

## Objetivo

Permitir que qualquer pessoa crie uma conta pessoal, confirme seu e-mail, entre, saia e recupere uma senha esquecida. A conta dá acesso ao espaço pessoal do FinAI; o uso da área do sistema exige autenticação e confirmação do próprio e-mail.

## Resultado esperado

O titular conclui cadastro e confirmação, acessa o sistema com suas credenciais, encerra o acesso e recupera a senha quando necessário. Dados inválidos, confirmação pendente e falhas de envio ou de links apresentam orientação para retomar a jornada sem liberar acesso indevido.

## Atores e permissões

Visitantes podem cadastrar-se, entrar e solicitar recuperação de senha. Contas não confirmadas ficam restritas à jornada de confirmação, reenvio, recuperação e saída, sem acesso à área autenticada do produto, inclusive perfil e configurações. Contas confirmadas e autenticadas acessam seu espaço pessoal. A confirmação deve corresponder ao próprio titular.

## Histórias de usuário

1. Como visitante, quero criar minha conta sem convite para começar a usar o FinAI.
2. Como titular, quero confirmar meu e-mail e reenviar o link quando necessário para liberar o acesso.
3. Como titular, quero entrar com e-mail e senha para acessar meu espaço pessoal.
4. Como titular, quero sair para encerrar meu acesso atual.
5. Como titular, quero recuperar a senha por e-mail para voltar a entrar quando a esquecer.
6. Como usuário, quero orientações nos erros de cadastro, confirmação, login e recuperação para corrigir os dados ou tentar novamente.

## Fluxo principal

1. O visitante informa nome, e-mail, senha e confirmação. Com dados válidos e e-mail disponível, criar uma única conta, enviar o link de confirmação e apresentar a orientação para confirmar o e-mail. Não solicitar dados financeiros no cadastro.
2. Enquanto não confirmar, manter a área do sistema bloqueada e oferecer reenvio de confirmação e saída. O simples recebimento do e-mail não confirma o endereço.
3. O titular abre o link válido da própria conta, autenticando-se quando necessário. Confirmar o e-mail e liberar o acesso à área inicial do sistema.
4. Nos próximos acessos, informar e-mail e senha. Credenciais válidas de conta confirmada permitem entrar na área inicial ou no destino protegido solicitado, respeitando as permissões existentes.
5. Ao sair, encerrar a sessão atual e retornar à página pública inicial. A área protegida volta a exigir autenticação.
6. Na recuperação, informar o e-mail. Apresentar resposta genérica de que o link será enviado se a conta existir; o titular cadastrado recebe o link para redefinir a senha.
7. Com link próprio válido e não utilizado, informar nova senha e confirmação. Após redefinição bem-sucedida, retornar ao login; a senha nova permite entrar e a antiga deixa de permitir novos logins.

## Fluxos alternativos e exceções

- Campos ausentes, e-mail inválido ou já cadastrado, senha fora das regras ou confirmação diferente impedem concluir o respectivo formulário e exibem erros nos campos. Um e-mail duplicado não cria outra conta; o titular pode entrar ou recuperar o acesso.
- Conta não confirmada com credenciais corretas continua restrita à jornada de confirmação e saída; não libera acesso financeiro, perfil ou configurações. A opção de lembrar acesso não dispensa a confirmação.
- Credenciais incorretas não autenticam. Após cinco tentativas consecutivas inválidas, uma nova tentativa durante o bloqueio informa a espera; terminado o prazo, credenciais válidas permitem retomar o login.
- Link de confirmação inválido, expirado ou pertencente a outra conta não confirma um endereço indevido e não libera a área do sistema. Apresentar orientação e caminho para pedir novo link da própria conta.
- Reabrir um link de confirmação ainda válido de uma conta já confirmada mantém a confirmação e permite seguir à área inicial, sem desfazer o estado.
- Link de recuperação inválido, expirado ou já utilizado não altera a senha; apresentar orientação e opção de solicitar outro link.
- Falha de envio na confirmação inicial, no reenvio ou na recuperação informa que não foi possível concluir o envio e orienta nova tentativa, sem apresentar sucesso. Na recuperação, não revelar explicitamente se a conta existe.
- Após restabelecer o envio, nova tentativa permite receber o link e concluir a jornada. Repetir o cadastro depois de falha de envio não deve produzir contas duplicadas nem deixar o titular sem caminho de confirmação ou recuperação.
- Redefinir a senha de uma conta não confirmada altera a senha, mas não confirma o e-mail nem libera o acesso à área do sistema.

## Regras de negócio

R1. Cadastro aberto, sem convite ou liberação administrativa. Contas são individuais; nenhum dado financeiro é solicitado nesta jornada.

R2. Nome e e-mail são obrigatórios, com até 255 caracteres cada; e-mail válido e único por conta. Senha e confirmação são obrigatórias e devem coincidir. Na recuperação e redefinição, o e-mail informado deve ser válido; na redefinição, nova senha e confirmação também são obrigatórias.

R3. Cadastro e redefinição exigem senha de 12 a 255 caracteres, com ao menos uma maiúscula, uma minúscula, um número e um símbolo, rejeitando senhas conhecidas em vazamentos. A mesma regra vale nos ambientes de teste e uso.

R4. Acesso à área do sistema exige autenticação e confirmação do próprio e-mail, incluindo acesso direto às páginas protegidas. Conta não confirmada pode concluir a jornada restrita de confirmação, reenvio, recuperação e saída; não acessa as funcionalidades do produto. Receber um e-mail ou redefinir a senha não equivale a confirmar o endereço.

R5. O link de recuperação é válido por 60 minutos a partir da emissão e não pode ser reutilizado após sucesso. A senha anterior deixa de permitir novos logins depois da redefinição.

R6. Após cinco falhas consecutivas de login para o mesmo e-mail e origem, bloquear temporariamente as novas tentativas e informar a espera, preservando o comportamento atual. Após o prazo, permitir nova tentativa.

R7. Preservar a opção existente de lembrar acesso. Ela não dispensa confirmação do e-mail nem impede a saída explícita; sair encerra a sessão atual e exige novo login para voltar à área protegida.

R8. Falha de envio ou de link não deve ser apresentada como confirmação ou recuperação concluída. As alternativas de reenvio e novo pedido devem permitir retomar sem duplicar contas nem alterar senhas indevidamente.

R9. As telas de acesso usam a base visual FinAI da Feature de adequação visual, com tipografia, paleta, campos, botões, erros e estados coerentes, adaptação para celular, tablet e computador e manutenção dos temas claro, escuro e acompanhar o sistema. Esta Feature não redefine a identidade visual.

## Dados percebidos pelo usuário

Nome, e-mail, senha, confirmação de senha, opção de lembrar acesso, links recebidos por e-mail, orientações para confirmar ou recuperar, mensagens de erro, espera e sucesso. Não apresentar dados financeiros na jornada de criação da conta. Senha e sua confirmação são tratadas como campos de senha na interface.

## Critérios de aceite

CA1. Como visitante, cadastrar nome e e-mail válidos e disponíveis, senha conforme R3 e confirmação igual; criar uma única conta, enviar o link e orientar a confirmação, sem pedir dados financeiros ou liberar a área do produto antes de confirmar.

CA2. No cadastro e na redefinição, quando aplicável, omitir campos obrigatórios, exceder os limites de nome/e-mail, informar e-mail inválido ou duplicado, senha fora de qualquer condição de R3 ou confirmação diferente; impedir a operação e indicar os respectivos erros sem criar contas ou alterar senhas indevidamente.

CA3. Com conta não confirmada, tentar a área inicial, perfil, configurações e destinos financeiros protegidos quando entregues; manter o acesso restrito à jornada de confirmação, reenvio, recuperação e saída, inclusive com lembrar acesso selecionado.

CA4. Como titular autenticado, abrir link válido da própria conta; confirmar o e-mail e permitir seguir à área inicial. Se iniciar sem sessão, solicitar autenticação quando necessária antes de concluir a confirmação.

CA5. Abrir link de confirmação inválido, expirado ou de outra conta; não confirmar endereço indevido nem liberar acesso e apresentar caminho para solicitar novo link próprio. Reabrir link ainda válido de conta já confirmada mantém a confirmação.

CA6. Entrar com credenciais corretas de conta confirmada; acessar a área inicial ou destino protegido solicitado. Credenciais incorretas não autenticam. Depois de cinco falhas consecutivas, a nova tentativa durante bloqueio informa espera; após o prazo, permitir nova tentativa válida.

CA7. Entrar e sair, com lembrar acesso marcado e desmarcado; retornar à página pública e exigir login ao tentar reabrir a área protegida.

CA8. Solicitar recuperação para e-mail cadastrado e inexistente, com envio disponível; apresentar a mesma resposta genérica. O titular cadastrado recebe o link, sem revelar a existência da conta ao solicitante pela resposta.

CA9. Com link de recuperação próprio, não usado e antes de 60 minutos, definir senha conforme R3 e confirmação igual; retornar ao login, permitir novos logins com a senha nova e recusar a anterior. Uma conta anteriormente não confirmada continua sem acesso ao sistema.

CA10. Tentar redefinir com link inválido, após sua expiração ou já utilizado; não alterar a senha e oferecer novo pedido. Um novo link válido permite retomar a jornada.

CA11. Provocar falha de envio na confirmação inicial, no reenvio e na recuperação; informar falha e nova tentativa sem sucesso fictício. Após restabelecer o envio, permitir retomar com link utilizável sem contas duplicadas e sem revelar explicitamente a existência de conta na recuperação.

CA12. Utilizar as telas e estados de acesso em computador, tablet e celular, nos temas claro, escuro e acompanhar o sistema; manter a linguagem visual FinAI definida pela adequação visual, controles utilizáveis e erros reconhecíveis.

## Dependências

Adequação visual do FinAI, issue #1016101: fornece a identidade, componentes e navegação compartilhados. A implementação desta Feature deve seguir essa base, preservando o pré-requisito visual do catálogo. A conclusão do requisito e sua publicação não provam que a adequação visual já foi implementada.

Envio de e-mails é necessário à confirmação e recuperação. Registros financeiros, seu isolamento, totais e consultas por IA serão entregues pelas respectivas Features.

## Designs e evidências

Fontes compartilhadas: conversation-input-001, conversation-input-002 e design-input-001, em ../../scopes/2026-11-11-finai-mvp/sources/. O ZIP não contém composição própria de telas de acesso; aplicar a linguagem visual da base aprovada em docs/harness/features/1016101-adequacao-visual-do-finai/feature.md. As adaptações de tema e de todas as telas existentes foram aprovadas na primeira Feature. Aceitação visual aplicável: R9 e CA12.

Evidências locais da jornada atual: app/Http/Requests/CreateUserRequest.php, app/Http/Requests/CreateUserPasswordRequest.php, app/Http/Requests/CreateSessionRequest.php, app/Http/Controllers/UserController.php, SessionController.php, UserEmailVerificationController.php, UserEmailVerificationNotificationController.php, UserEmailResetNotificationController.php, UserPasswordController.php, app/Models/User.php, routes/web.php e config/auth.php. Respostas Q5, Q6 e Q7 em history/interview.md. As decisões vêm desta conversa e do catálogo; nenhuma task antiga do Redmine é fonte de requisito ou conclusão.

## Dentro do escopo

Cadastro público, confirmação e reenvio de e-mail, login, opção de lembrar acesso, saída, recuperação e redefinição de senha esquecida; campos, validações e recuperação de falhas descritos; restrição da área do produto enquanto o e-mail não estiver confirmado; uso da base visual aprovada.

## Fora do escopo

Gestão administrativa de usuários, convites, autenticação social, novas capacidades ou ampliação de perfil, passkeys e dois fatores. Não se solicita remover recursos existentes. Operações financeiras, isolamento dos registros, cálculos e IA pertencem às Features seguintes. Esta etapa define requisitos e publicação, sem decomposição em tarefas técnicas.

## Atributos exatos da criação

```json
{
  "project_id": 65224,
  "tracker_id": 2,
  "status_id": 1,
  "category_id": null,
  "fixed_version_id": 20355,
  "custom_fields": [
    {
      "id": 2,
      "value": "2"
    }
  ],
  "subject": "[WEB] [USUARIO] Acesso à conta pessoal"
}
```

## Descrição integral da criação

````markdown
<!-- project-flow:run 92c15ad8-bf89-4c23-bf1f-6c6c4b7f6710 -->
<!-- project-flow:start -->
## Objetivo

Permitir que qualquer pessoa crie uma conta pessoal, confirme seu e-mail, entre, saia e recupere uma senha esquecida. A conta dá acesso ao espaço pessoal do FinAI; o uso da área do sistema exige autenticação e confirmação do próprio e-mail.

## Resultado esperado

O titular conclui cadastro e confirmação, acessa o sistema com suas credenciais, encerra o acesso e recupera a senha quando necessário. Dados inválidos, confirmação pendente e falhas de envio ou de links apresentam orientação para retomar a jornada sem liberar acesso indevido.

## Atores e permissões

Visitantes podem cadastrar-se, entrar e solicitar recuperação de senha. Contas não confirmadas ficam restritas à jornada de confirmação, reenvio, recuperação e saída, sem acesso à área autenticada do produto, inclusive perfil e configurações. Contas confirmadas e autenticadas acessam seu espaço pessoal. A confirmação deve corresponder ao próprio titular.

## Histórias de usuário

1. Como visitante, quero criar minha conta sem convite para começar a usar o FinAI.
2. Como titular, quero confirmar meu e-mail e reenviar o link quando necessário para liberar o acesso.
3. Como titular, quero entrar com e-mail e senha para acessar meu espaço pessoal.
4. Como titular, quero sair para encerrar meu acesso atual.
5. Como titular, quero recuperar a senha por e-mail para voltar a entrar quando a esquecer.
6. Como usuário, quero orientações nos erros de cadastro, confirmação, login e recuperação para corrigir os dados ou tentar novamente.

## Fluxo principal

1. O visitante informa nome, e-mail, senha e confirmação. Com dados válidos e e-mail disponível, criar uma única conta, enviar o link de confirmação e apresentar a orientação para confirmar o e-mail. Não solicitar dados financeiros no cadastro.
2. Enquanto não confirmar, manter a área do sistema bloqueada e oferecer reenvio de confirmação e saída. O simples recebimento do e-mail não confirma o endereço.
3. O titular abre o link válido da própria conta, autenticando-se quando necessário. Confirmar o e-mail e liberar o acesso à área inicial do sistema.
4. Nos próximos acessos, informar e-mail e senha. Credenciais válidas de conta confirmada permitem entrar na área inicial ou no destino protegido solicitado, respeitando as permissões existentes.
5. Ao sair, encerrar a sessão atual e retornar à página pública inicial. A área protegida volta a exigir autenticação.
6. Na recuperação, informar o e-mail. Apresentar resposta genérica de que o link será enviado se a conta existir; o titular cadastrado recebe o link para redefinir a senha.
7. Com link próprio válido e não utilizado, informar nova senha e confirmação. Após redefinição bem-sucedida, retornar ao login; a senha nova permite entrar e a antiga deixa de permitir novos logins.

## Fluxos alternativos e exceções

- Campos ausentes, e-mail inválido ou já cadastrado, senha fora das regras ou confirmação diferente impedem concluir o respectivo formulário e exibem erros nos campos. Um e-mail duplicado não cria outra conta; o titular pode entrar ou recuperar o acesso.
- Conta não confirmada com credenciais corretas continua restrita à jornada de confirmação e saída; não libera acesso financeiro, perfil ou configurações. A opção de lembrar acesso não dispensa a confirmação.
- Credenciais incorretas não autenticam. Após cinco tentativas consecutivas inválidas, uma nova tentativa durante o bloqueio informa a espera; terminado o prazo, credenciais válidas permitem retomar o login.
- Link de confirmação inválido, expirado ou pertencente a outra conta não confirma um endereço indevido e não libera a área do sistema. Apresentar orientação e caminho para pedir novo link da própria conta.
- Reabrir um link de confirmação ainda válido de uma conta já confirmada mantém a confirmação e permite seguir à área inicial, sem desfazer o estado.
- Link de recuperação inválido, expirado ou já utilizado não altera a senha; apresentar orientação e opção de solicitar outro link.
- Falha de envio na confirmação inicial, no reenvio ou na recuperação informa que não foi possível concluir o envio e orienta nova tentativa, sem apresentar sucesso. Na recuperação, não revelar explicitamente se a conta existe.
- Após restabelecer o envio, nova tentativa permite receber o link e concluir a jornada. Repetir o cadastro depois de falha de envio não deve produzir contas duplicadas nem deixar o titular sem caminho de confirmação ou recuperação.
- Redefinir a senha de uma conta não confirmada altera a senha, mas não confirma o e-mail nem libera o acesso à área do sistema.

## Regras de negócio

R1. Cadastro aberto, sem convite ou liberação administrativa. Contas são individuais; nenhum dado financeiro é solicitado nesta jornada.

R2. Nome e e-mail são obrigatórios, com até 255 caracteres cada; e-mail válido e único por conta. Senha e confirmação são obrigatórias e devem coincidir. Na recuperação e redefinição, o e-mail informado deve ser válido; na redefinição, nova senha e confirmação também são obrigatórias.

R3. Cadastro e redefinição exigem senha de 12 a 255 caracteres, com ao menos uma maiúscula, uma minúscula, um número e um símbolo, rejeitando senhas conhecidas em vazamentos. A mesma regra vale nos ambientes de teste e uso.

R4. Acesso à área do sistema exige autenticação e confirmação do próprio e-mail, incluindo acesso direto às páginas protegidas. Conta não confirmada pode concluir a jornada restrita de confirmação, reenvio, recuperação e saída; não acessa as funcionalidades do produto. Receber um e-mail ou redefinir a senha não equivale a confirmar o endereço.

R5. O link de recuperação é válido por 60 minutos a partir da emissão e não pode ser reutilizado após sucesso. A senha anterior deixa de permitir novos logins depois da redefinição.

R6. Após cinco falhas consecutivas de login para o mesmo e-mail e origem, bloquear temporariamente as novas tentativas e informar a espera, preservando o comportamento atual. Após o prazo, permitir nova tentativa.

R7. Preservar a opção existente de lembrar acesso. Ela não dispensa confirmação do e-mail nem impede a saída explícita; sair encerra a sessão atual e exige novo login para voltar à área protegida.

R8. Falha de envio ou de link não deve ser apresentada como confirmação ou recuperação concluída. As alternativas de reenvio e novo pedido devem permitir retomar sem duplicar contas nem alterar senhas indevidamente.

R9. As telas de acesso usam a base visual FinAI da Feature de adequação visual, com tipografia, paleta, campos, botões, erros e estados coerentes, adaptação para celular, tablet e computador e manutenção dos temas claro, escuro e acompanhar o sistema. Esta Feature não redefine a identidade visual.

## Dados percebidos pelo usuário

Nome, e-mail, senha, confirmação de senha, opção de lembrar acesso, links recebidos por e-mail, orientações para confirmar ou recuperar, mensagens de erro, espera e sucesso. Não apresentar dados financeiros na jornada de criação da conta. Senha e sua confirmação são tratadas como campos de senha na interface.

## Critérios de aceite

CA1. Como visitante, cadastrar nome e e-mail válidos e disponíveis, senha conforme R3 e confirmação igual; criar uma única conta, enviar o link e orientar a confirmação, sem pedir dados financeiros ou liberar a área do produto antes de confirmar.

CA2. No cadastro e na redefinição, quando aplicável, omitir campos obrigatórios, exceder os limites de nome/e-mail, informar e-mail inválido ou duplicado, senha fora de qualquer condição de R3 ou confirmação diferente; impedir a operação e indicar os respectivos erros sem criar contas ou alterar senhas indevidamente.

CA3. Com conta não confirmada, tentar a área inicial, perfil, configurações e destinos financeiros protegidos quando entregues; manter o acesso restrito à jornada de confirmação, reenvio, recuperação e saída, inclusive com lembrar acesso selecionado.

CA4. Como titular autenticado, abrir link válido da própria conta; confirmar o e-mail e permitir seguir à área inicial. Se iniciar sem sessão, solicitar autenticação quando necessária antes de concluir a confirmação.

CA5. Abrir link de confirmação inválido, expirado ou de outra conta; não confirmar endereço indevido nem liberar acesso e apresentar caminho para solicitar novo link próprio. Reabrir link ainda válido de conta já confirmada mantém a confirmação.

CA6. Entrar com credenciais corretas de conta confirmada; acessar a área inicial ou destino protegido solicitado. Credenciais incorretas não autenticam. Depois de cinco falhas consecutivas, a nova tentativa durante bloqueio informa espera; após o prazo, permitir nova tentativa válida.

CA7. Entrar e sair, com lembrar acesso marcado e desmarcado; retornar à página pública e exigir login ao tentar reabrir a área protegida.

CA8. Solicitar recuperação para e-mail cadastrado e inexistente, com envio disponível; apresentar a mesma resposta genérica. O titular cadastrado recebe o link, sem revelar a existência da conta ao solicitante pela resposta.

CA9. Com link de recuperação próprio, não usado e antes de 60 minutos, definir senha conforme R3 e confirmação igual; retornar ao login, permitir novos logins com a senha nova e recusar a anterior. Uma conta anteriormente não confirmada continua sem acesso ao sistema.

CA10. Tentar redefinir com link inválido, após sua expiração ou já utilizado; não alterar a senha e oferecer novo pedido. Um novo link válido permite retomar a jornada.

CA11. Provocar falha de envio na confirmação inicial, no reenvio e na recuperação; informar falha e nova tentativa sem sucesso fictício. Após restabelecer o envio, permitir retomar com link utilizável sem contas duplicadas e sem revelar explicitamente a existência de conta na recuperação.

CA12. Utilizar as telas e estados de acesso em computador, tablet e celular, nos temas claro, escuro e acompanhar o sistema; manter a linguagem visual FinAI definida pela adequação visual, controles utilizáveis e erros reconhecíveis.

## Dependências

Adequação visual do FinAI, issue #1016101: fornece a identidade, componentes e navegação compartilhados. A implementação desta Feature deve seguir essa base, preservando o pré-requisito visual do catálogo. A conclusão do requisito e sua publicação não provam que a adequação visual já foi implementada.

Envio de e-mails é necessário à confirmação e recuperação. Registros financeiros, seu isolamento, totais e consultas por IA serão entregues pelas respectivas Features.

## Dentro do escopo

Cadastro público, confirmação e reenvio de e-mail, login, opção de lembrar acesso, saída, recuperação e redefinição de senha esquecida; campos, validações e recuperação de falhas descritos; restrição da área do produto enquanto o e-mail não estiver confirmado; uso da base visual aprovada.

## Fora do escopo

Gestão administrativa de usuários, convites, autenticação social, novas capacidades ou ampliação de perfil, passkeys e dois fatores. Não se solicita remover recursos existentes. Operações financeiras, isolamento dos registros, cálculos e IA pertencem às Features seguintes. Esta etapa define requisitos e publicação, sem decomposição em tarefas técnicas.
<!-- project-flow:end -->
````

## Atualização posterior — destino e campos

```json
{
  "issue_id": "{{created_issue_id}}",
  "changes": {
    "fixed_version_id": 20355,
    "description": "Descrição integral apresentada a seguir"
  }
}
```

## Descrição integral da publicação final

````markdown
<!-- project-flow:run 92c15ad8-bf89-4c23-bf1f-6c6c4b7f6710 -->
<!-- project-flow:start -->
## Objetivo

Permitir que qualquer pessoa crie uma conta pessoal, confirme seu e-mail, entre, saia e recupere uma senha esquecida. A conta dá acesso ao espaço pessoal do FinAI; o uso da área do sistema exige autenticação e confirmação do próprio e-mail.

## Resultado esperado

O titular conclui cadastro e confirmação, acessa o sistema com suas credenciais, encerra o acesso e recupera a senha quando necessário. Dados inválidos, confirmação pendente e falhas de envio ou de links apresentam orientação para retomar a jornada sem liberar acesso indevido.

## Atores e permissões

Visitantes podem cadastrar-se, entrar e solicitar recuperação de senha. Contas não confirmadas ficam restritas à jornada de confirmação, reenvio, recuperação e saída, sem acesso à área autenticada do produto, inclusive perfil e configurações. Contas confirmadas e autenticadas acessam seu espaço pessoal. A confirmação deve corresponder ao próprio titular.

## Histórias de usuário

1. Como visitante, quero criar minha conta sem convite para começar a usar o FinAI.
2. Como titular, quero confirmar meu e-mail e reenviar o link quando necessário para liberar o acesso.
3. Como titular, quero entrar com e-mail e senha para acessar meu espaço pessoal.
4. Como titular, quero sair para encerrar meu acesso atual.
5. Como titular, quero recuperar a senha por e-mail para voltar a entrar quando a esquecer.
6. Como usuário, quero orientações nos erros de cadastro, confirmação, login e recuperação para corrigir os dados ou tentar novamente.

## Fluxo principal

1. O visitante informa nome, e-mail, senha e confirmação. Com dados válidos e e-mail disponível, criar uma única conta, enviar o link de confirmação e apresentar a orientação para confirmar o e-mail. Não solicitar dados financeiros no cadastro.
2. Enquanto não confirmar, manter a área do sistema bloqueada e oferecer reenvio de confirmação e saída. O simples recebimento do e-mail não confirma o endereço.
3. O titular abre o link válido da própria conta, autenticando-se quando necessário. Confirmar o e-mail e liberar o acesso à área inicial do sistema.
4. Nos próximos acessos, informar e-mail e senha. Credenciais válidas de conta confirmada permitem entrar na área inicial ou no destino protegido solicitado, respeitando as permissões existentes.
5. Ao sair, encerrar a sessão atual e retornar à página pública inicial. A área protegida volta a exigir autenticação.
6. Na recuperação, informar o e-mail. Apresentar resposta genérica de que o link será enviado se a conta existir; o titular cadastrado recebe o link para redefinir a senha.
7. Com link próprio válido e não utilizado, informar nova senha e confirmação. Após redefinição bem-sucedida, retornar ao login; a senha nova permite entrar e a antiga deixa de permitir novos logins.

## Fluxos alternativos e exceções

- Campos ausentes, e-mail inválido ou já cadastrado, senha fora das regras ou confirmação diferente impedem concluir o respectivo formulário e exibem erros nos campos. Um e-mail duplicado não cria outra conta; o titular pode entrar ou recuperar o acesso.
- Conta não confirmada com credenciais corretas continua restrita à jornada de confirmação e saída; não libera acesso financeiro, perfil ou configurações. A opção de lembrar acesso não dispensa a confirmação.
- Credenciais incorretas não autenticam. Após cinco tentativas consecutivas inválidas, uma nova tentativa durante o bloqueio informa a espera; terminado o prazo, credenciais válidas permitem retomar o login.
- Link de confirmação inválido, expirado ou pertencente a outra conta não confirma um endereço indevido e não libera a área do sistema. Apresentar orientação e caminho para pedir novo link da própria conta.
- Reabrir um link de confirmação ainda válido de uma conta já confirmada mantém a confirmação e permite seguir à área inicial, sem desfazer o estado.
- Link de recuperação inválido, expirado ou já utilizado não altera a senha; apresentar orientação e opção de solicitar outro link.
- Falha de envio na confirmação inicial, no reenvio ou na recuperação informa que não foi possível concluir o envio e orienta nova tentativa, sem apresentar sucesso. Na recuperação, não revelar explicitamente se a conta existe.
- Após restabelecer o envio, nova tentativa permite receber o link e concluir a jornada. Repetir o cadastro depois de falha de envio não deve produzir contas duplicadas nem deixar o titular sem caminho de confirmação ou recuperação.
- Redefinir a senha de uma conta não confirmada altera a senha, mas não confirma o e-mail nem libera o acesso à área do sistema.

## Regras de negócio

R1. Cadastro aberto, sem convite ou liberação administrativa. Contas são individuais; nenhum dado financeiro é solicitado nesta jornada.

R2. Nome e e-mail são obrigatórios, com até 255 caracteres cada; e-mail válido e único por conta. Senha e confirmação são obrigatórias e devem coincidir. Na recuperação e redefinição, o e-mail informado deve ser válido; na redefinição, nova senha e confirmação também são obrigatórias.

R3. Cadastro e redefinição exigem senha de 12 a 255 caracteres, com ao menos uma maiúscula, uma minúscula, um número e um símbolo, rejeitando senhas conhecidas em vazamentos. A mesma regra vale nos ambientes de teste e uso.

R4. Acesso à área do sistema exige autenticação e confirmação do próprio e-mail, incluindo acesso direto às páginas protegidas. Conta não confirmada pode concluir a jornada restrita de confirmação, reenvio, recuperação e saída; não acessa as funcionalidades do produto. Receber um e-mail ou redefinir a senha não equivale a confirmar o endereço.

R5. O link de recuperação é válido por 60 minutos a partir da emissão e não pode ser reutilizado após sucesso. A senha anterior deixa de permitir novos logins depois da redefinição.

R6. Após cinco falhas consecutivas de login para o mesmo e-mail e origem, bloquear temporariamente as novas tentativas e informar a espera, preservando o comportamento atual. Após o prazo, permitir nova tentativa.

R7. Preservar a opção existente de lembrar acesso. Ela não dispensa confirmação do e-mail nem impede a saída explícita; sair encerra a sessão atual e exige novo login para voltar à área protegida.

R8. Falha de envio ou de link não deve ser apresentada como confirmação ou recuperação concluída. As alternativas de reenvio e novo pedido devem permitir retomar sem duplicar contas nem alterar senhas indevidamente.

R9. As telas de acesso usam a base visual FinAI da Feature de adequação visual, com tipografia, paleta, campos, botões, erros e estados coerentes, adaptação para celular, tablet e computador e manutenção dos temas claro, escuro e acompanhar o sistema. Esta Feature não redefine a identidade visual.

## Dados percebidos pelo usuário

Nome, e-mail, senha, confirmação de senha, opção de lembrar acesso, links recebidos por e-mail, orientações para confirmar ou recuperar, mensagens de erro, espera e sucesso. Não apresentar dados financeiros na jornada de criação da conta. Senha e sua confirmação são tratadas como campos de senha na interface.

## Critérios de aceite

CA1. Como visitante, cadastrar nome e e-mail válidos e disponíveis, senha conforme R3 e confirmação igual; criar uma única conta, enviar o link e orientar a confirmação, sem pedir dados financeiros ou liberar a área do produto antes de confirmar.

CA2. No cadastro e na redefinição, quando aplicável, omitir campos obrigatórios, exceder os limites de nome/e-mail, informar e-mail inválido ou duplicado, senha fora de qualquer condição de R3 ou confirmação diferente; impedir a operação e indicar os respectivos erros sem criar contas ou alterar senhas indevidamente.

CA3. Com conta não confirmada, tentar a área inicial, perfil, configurações e destinos financeiros protegidos quando entregues; manter o acesso restrito à jornada de confirmação, reenvio, recuperação e saída, inclusive com lembrar acesso selecionado.

CA4. Como titular autenticado, abrir link válido da própria conta; confirmar o e-mail e permitir seguir à área inicial. Se iniciar sem sessão, solicitar autenticação quando necessária antes de concluir a confirmação.

CA5. Abrir link de confirmação inválido, expirado ou de outra conta; não confirmar endereço indevido nem liberar acesso e apresentar caminho para solicitar novo link próprio. Reabrir link ainda válido de conta já confirmada mantém a confirmação.

CA6. Entrar com credenciais corretas de conta confirmada; acessar a área inicial ou destino protegido solicitado. Credenciais incorretas não autenticam. Depois de cinco falhas consecutivas, a nova tentativa durante bloqueio informa espera; após o prazo, permitir nova tentativa válida.

CA7. Entrar e sair, com lembrar acesso marcado e desmarcado; retornar à página pública e exigir login ao tentar reabrir a área protegida.

CA8. Solicitar recuperação para e-mail cadastrado e inexistente, com envio disponível; apresentar a mesma resposta genérica. O titular cadastrado recebe o link, sem revelar a existência da conta ao solicitante pela resposta.

CA9. Com link de recuperação próprio, não usado e antes de 60 minutos, definir senha conforme R3 e confirmação igual; retornar ao login, permitir novos logins com a senha nova e recusar a anterior. Uma conta anteriormente não confirmada continua sem acesso ao sistema.

CA10. Tentar redefinir com link inválido, após sua expiração ou já utilizado; não alterar a senha e oferecer novo pedido. Um novo link válido permite retomar a jornada.

CA11. Provocar falha de envio na confirmação inicial, no reenvio e na recuperação; informar falha e nova tentativa sem sucesso fictício. Após restabelecer o envio, permitir retomar com link utilizável sem contas duplicadas e sem revelar explicitamente a existência de conta na recuperação.

CA12. Utilizar as telas e estados de acesso em computador, tablet e celular, nos temas claro, escuro e acompanhar o sistema; manter a linguagem visual FinAI definida pela adequação visual, controles utilizáveis e erros reconhecíveis.

## Dependências

Adequação visual do FinAI, issue #1016101: fornece a identidade, componentes e navegação compartilhados. A implementação desta Feature deve seguir essa base, preservando o pré-requisito visual do catálogo. A conclusão do requisito e sua publicação não provam que a adequação visual já foi implementada.

Envio de e-mails é necessário à confirmação e recuperação. Registros financeiros, seu isolamento, totais e consultas por IA serão entregues pelas respectivas Features.

## Dentro do escopo

Cadastro público, confirmação e reenvio de e-mail, login, opção de lembrar acesso, saída, recuperação e redefinição de senha esquecida; campos, validações e recuperação de falhas descritos; restrição da área do produto enquanto o e-mail não estiver confirmado; uso da base visual aprovada.

## Fora do escopo

Gestão administrativa de usuários, convites, autenticação social, novas capacidades ou ampliação de perfil, passkeys e dois fatores. Não se solicita remover recursos existentes. Operações financeiras, isolamento dos registros, cálculos e IA pertencem às Features seguintes. Esta etapa define requisitos e publicação, sem decomposição em tarefas técnicas.

## Requisito canônico

Documento aprovado por Mário Tinelli: docs/harness/features/{{created_issue_id}}-acesso-a-conta-pessoal/feature.md
<!-- project-flow:end -->
````

## Relação nativa exata e vinculação do ID

```json
[
  {
    "key": "visual-blocks-acesso",
    "payload": {
      "issue_id": 1016101,
      "issue_to_id": "{{created_issue_id}}",
      "relation_type": "blocks"
    }
  }
]
```
