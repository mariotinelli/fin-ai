# Publicação das filhas de [WEB] [USUARIO] Acesso à conta

Item pai Redmine: `1015909`

## Campos nativos aprovados

- Projeto: `65224`
- Pai nativo: `1015909`
- Tracker da mãe: Feature (`2`)
- Tracker DEV: Task (`4`)
- Tracker QA: Deliverable (`5`)
- Status inicial: New (`1`)
- Prioridade inicial: Normal (`4`, regra fixa)
- Categoria herdada: `None`
- Versão herdada: `20355`
- Responsável, início e vencimento: vazios

## Campos nativos e descrições

### [DEV] [WEB] [USUARIO] Acesso à conta - Política de senha no cadastro e na redefinição

- Chave interna: `dev-1`
- Tipo: DEV
- Estimativa: 2h
- Payload SHA-256: `bfe9ac20f3d6f5542f539a58def14851a73238dab62022ec75e21fb79207a870`

## Entrega

Completar a aplicação da política de senha aprovada no cadastro e na redefinição. A base já valida os formulários, mas a regra forte depende do ambiente de produção. Preservar as validações dos demais campos e os caminhos de cadastro, confirmação e retorno ao login.

## Escopo e limites

Abrange criação da conta e redefinição de senha esquecida. Não amplia gestão de perfil, autenticação social, passkeys ou dois fatores.

## Critérios de aceite

- Cadastro e redefinição aceitam senha de 12 a 255 caracteres que contenha maiúscula, minúscula, número e símbolo, não conste em vazamentos e tenha confirmação igual.
- Senha com menos de 12 ou mais de 255 caracteres impede cadastro e redefinição, com erro no campo.
- A ausência de maiúscula, minúscula, número ou símbolo impede cadastro e redefinição, com erro no campo para cada composição inválida.
- Senha conhecida em vazamentos impede cadastro e redefinição e apresenta erro, mesmo quando atende ao tamanho e à composição.
- Senha ou confirmação ausente, ou confirmação diferente, impede concluir os dois fluxos e apresenta erro.
- No cadastro, nome e e-mail ausentes ou maiores que 255 caracteres, e-mail inválido ou já cadastrado continuam recusados com erros; na redefinição, e-mail ausente ou inválido continua recusado.
- Com cadastro válido, uma única conta é criada e segue para confirmação por e-mail, sem solicitar dados financeiros.
- Com link de recuperação válido e senha conforme a regra, redefinir retorna ao login; a nova senha permite entrar e a anterior deixa de permitir novos logins.
- Redefinir a senha não confirma o e-mail: a conta anteriormente não confirmada continua sem acesso financeiro.

## Dependências

Pode iniciar com os fluxos de acesso existentes. A verificação integrada da Feature inclui ‘Acesso à conta - Confirmação de e-mail com nova tentativa’ e ‘Acesso à conta - Recuperação de senha com nova tentativa’.

## Referências

Item pai Redmine #1015909; regras/critérios R3, CA2, CA8.

<!-- project-slices-child:89130df3d7ca12a7a388b8cbaa37ab962fe850792afbb6a891f00f5ec9255aa7 -->


### [DEV] [WEB] [USUARIO] Acesso à conta - Confirmação de e-mail com nova tentativa

- Chave interna: `dev-2`
- Tipo: DEV
- Estimativa: 2h
- Payload SHA-256: `0a416c65d21dacf909c593552aff9f83355e1e3fad800bebabc0449bbe7c98e2`

## Entrega

Completar a orientação de nova tentativa quando o envio de confirmação falhar no cadastro ou no reenvio, e quando um link de confirmação for recusado. Preservar o cadastro público, a confirmação pelo titular, a restrição financeira e o reenvio que já existem.

## Escopo e limites

Abrange cadastro, envio/reenvio e confirmação do e-mail. A política de senha pertence a ‘Acesso à conta - Política de senha no cadastro e na redefinição’; a recuperação de senha pertence a ‘Acesso à conta - Recuperação de senha com nova tentativa’.

## Critérios de aceite

- Cadastro válido cria uma única conta, envia o link e orienta confirmar o e-mail; receber o e-mail por si só não libera finanças.
- Conta não confirmada permanece sem acesso financeiro, com orientação para confirmar, reenviar o link ou sair.
- Titular com link válido da própria conta confirma o endereço e acessa a área inicial, autenticando-se antes quando necessário.
- Link de confirmação inválido não confirma o endereço nem libera acesso e apresenta orientação e caminho para solicitar outro.
- Link de confirmação expirado não confirma o endereço nem libera acesso e apresenta orientação e caminho para solicitar outro.
- Link de outra conta não confirma nenhum endereço indevido nem libera acesso e permite ao usuário solicitar confirmação da própria conta.
- Reabrir link ainda válido de uma conta já confirmada mantém a confirmação e permite seguir à área inicial.
- Falha de envio no cadastro informa a impossibilidade de concluir a etapa dependente do e-mail e orienta nova tentativa; repetir depois da falha não cria contas duplicadas.
- Falha no reenvio informa que o envio não foi concluído e orienta nova tentativa, sem mensagem de sucesso.
- Restabelecido o envio, a nova tentativa permite receber o link e concluir a confirmação.

## Dependências

Pode iniciar com cadastro e confirmação existentes. Para a jornada integrada, usar a política de senha entregue por ‘Acesso à conta - Política de senha no cadastro e na redefinição’.

## Referências

Item pai Redmine #1015909; regras/critérios CA4, CA10-confirmacao.

<!-- project-slices-child:ddf0296c61c38b8e25654e171f6f823ea2c83bb0a0dd78409f5837df906f00ba -->


### [DEV] [WEB] [USUARIO] Acesso à conta - Recuperação de senha com nova tentativa

- Chave interna: `dev-3`
- Tipo: DEV
- Estimativa: 2h
- Payload SHA-256: `958bccd185e254bb54d1a38d8e9d3c8d18390c53ca099f924e620dd68c0c92fc`

## Entrega

Completar a recuperação de senha com orientação quando o envio falhar e uma opção de novo pedido quando o link for inválido, expirado ou já utilizado. Preservar a resposta genérica, a validade de 60 minutos, o uso único e a restrição de contas sem e-mail confirmado.

## Escopo e limites

Abrange solicitação e redefinição de senha esquecida. A composição da senha pertence a ‘Acesso à conta - Política de senha no cadastro e na redefinição’; envio de confirmação pertence a ‘Acesso à conta - Confirmação de e-mail com nova tentativa’.

## Critérios de aceite

- Solicitar recuperação apresenta que um link será enviado se a conta existir, sem distinguir conta existente de inexistente; para conta existente, envia ao e-mail cadastrado.
- Falha no envio orienta nova tentativa sem afirmar conclusão do envio ou revelar explicitamente se a conta existe.
- Depois de restabelecer o envio, nova solicitação permite ao titular receber um link utilizável.
- Link de recuperação inválido não altera senha e oferece caminho para solicitar outro.
- Link de recuperação expirado após 60 minutos não altera senha e oferece caminho para solicitar outro.
- Link já utilizado com sucesso não altera senha novamente e oferece caminho para solicitar outro.
- Link válido, dentro de 60 minutos e ainda não usado, com nova senha e confirmação válidas, permite redefinir e retorna ao login.
- Após redefinição, nova senha permite novos logins e senha anterior não; o link utilizado deixa de funcionar.
- Redefinição não confirma e-mail e mantém a restrição financeira das contas não confirmadas.

## Dependências

Pode iniciar com a recuperação existente. Para concluir a jornada integrada, usar a política de senha entregue por ‘Acesso à conta - Política de senha no cadastro e na redefinição’.

## Referências

Item pai Redmine #1015909; regras/critérios CA9, CA10-recuperacao.

<!-- project-slices-child:28aa773b04bfe04f5fc70806ce834f75a777f973a592ffc8d7a532349e237cbd -->


### [QA] [WEB] [USUARIO] Acesso à conta

- Chave interna: `qa`
- Tipo: QA
- Estimativa: 1.5h
- Payload SHA-256: `88c5287a00c60d008fa680876525023854cdb10dce690fca62ae1c061aa88339`

## Objetivo

Verificar o acesso à conta completo, do cadastro à confirmação, entrada, saída e recuperação de senha.

## Jornadas integradas

- Cadastro público válido: Como visitante, cadastrar nome e e-mail disponíveis, senha conforme R3 e confirmação igual. Resultado esperado: Uma única conta é criada sem convite, aprovação administrativa ou dados financeiros; recebe link e é orientada a confirmar, sem acesso financeiro ainda.
- Campos obrigatórios: No cadastro, omitir separadamente nome, e-mail, senha e confirmação; na redefinição, omitir e-mail, senha e confirmação. Resultado esperado: Cada ausência aplicável impede concluir e exibe erro no campo; conta/senha não é criada/alterada indevidamente.
- Limites de nome e e-mail: No cadastro, usar nome/e-mail válidos com 255 caracteres e, separadamente, com 256 caracteres; demais dados válidos. Resultado esperado: Até 255 caracteres é aceito; acima disso exibe erro e não conclui.
- E-mail inválido e duplicado: Cadastrar com e-mail inválido e com e-mail já usado; testar e-mail inválido na redefinição e acessar login/recuperação pelo fluxo existente. Resultado esperado: Erros impedem conclusão e duplicação; o usuário consegue seguir para entrar ou recuperar acesso.
- Limites de senha: No cadastro e na redefinição com link válido, testar senhas não vazadas de 11, 12, 255 e 256 caracteres, com todas as classes e confirmação igual. Resultado esperado: 12 e 255 são aceitas; 11 e 256 são recusadas com erro, sem concluir a operação.
- Composição da senha: Nos dois fluxos, testar separadamente senha sem maiúscula, sem minúscula, sem número e sem símbolo, mantendo demais regras válidas. Resultado esperado: Cada ausência é recusada com erro; a combinação completa não é recusada por composição.
- Senha conhecida em vazamentos: Usar dado de teste reconhecido como vazado, que atenda tamanho e composição, no cadastro e na redefinição. Resultado esperado: Ambos recusam com erro e não concluem.
- Confirmação diferente: No cadastro e redefinição, informar senha válida e confirmação diferente. Resultado esperado: Erro impede criar a conta ou alterar a senha.
- Acesso sem autenticação: Como visitante, abrir a área inicial protegida. Resultado esperado: Exige login e não apresenta área financeira.
- Conta não confirmada: Entrar com conta não confirmada, tentar área protegida e reenviar confirmação; repetir com lembrar acesso selecionado. Resultado esperado: Mantém restrição financeira, mostra orientação e permite reenviar/sair. Receber e-mail ou lembrar acesso não confirma a conta.
- Confirmação válida: Abrir link válido próprio como titular autenticado; repetir jornada começando sem sessão. Resultado esperado: Solicita autenticação quando necessária, confirma o endereço do titular e libera a área inicial.
- Confirmação com link inválido: Alterar um link de confirmação e abri-lo como titular não confirmado. Resultado esperado: Recusa confirmação e acesso financeiro, orienta e oferece novo pedido.
- Confirmação expirada: Abrir link cuja validade tenha expirado, com titular não confirmado. Resultado esperado: Recusa confirmação e acesso financeiro, orienta e oferece novo pedido.
- Confirmação de outra conta: Autenticado como A não confirmado, abrir link válido de B. Resultado esperado: Não confirma A nem B indevidamente, não libera finanças e permite solicitar link da própria conta.
- Reabertura de confirmação: Confirmar conta e reabrir o mesmo link ainda válido como titular. Resultado esperado: Mantém confirmação e permite seguir à área inicial, sem desfazer estado.
- Falha de envio no cadastro: Provocar falha controlada no envio durante cadastro válido; restaurar envio e repetir conforme orientação. Resultado esperado: Informa falha e nova tentativa sem falso sucesso; retomada permite receber confirmação sem contas duplicadas.
- Falha de envio no reenvio: Com conta não confirmada, provocar falha de reenvio, restaurar serviço e tentar novamente. Resultado esperado: Apresenta orientação sem alegar envio concluído; nova tentativa recebe link e permite confirmação.
- Login e destino solicitado: Com conta confirmada, entrar com credenciais corretas diretamente e após solicitar página protegida. Resultado esperado: Acessa área inicial ou destino protegido solicitado.
- Credenciais incorretas: Tentar entrar com senha errada ou conta inexistente. Resultado esperado: Não autentica e apresenta erro.
- Bloqueio temporário de login: Para o mesmo e-mail e origem, realizar cinco falhas consecutivas; tentar novamente durante bloqueio e após a espera informada. Resultado esperado: A nova tentativa durante bloqueio informa espera sem autenticar; terminado o prazo, credenciais válidas permitem entrar.
- Saída explícita: Entrar em conta confirmada, sair e reabrir área protegida; repetir com lembrar acesso selecionado. Resultado esperado: Retorna à página pública, encerra sessão atual e exige login novamente mesmo com lembrança anterior.
- Resposta genérica de recuperação: Solicitar recuperação para e-mail cadastrado e para e-mail inexistente, com envio disponível. Resultado esperado: Exibe a mesma resposta genérica; titular cadastrado recebe link sem informação de existência ao solicitante.
- Redefinição válida: Com link próprio não usado, antes de 60 minutos, definir senha conforme R3 e confirmação igual; testar logins com senha anterior e nova. Resultado esperado: Retorna ao login; nova senha funciona e antiga não permite novos logins.
- Redefinição de conta não confirmada: Redefinir com link válido uma conta não confirmada e entrar com a nova senha. Resultado esperado: Senha é alterada, mas e-mail não é confirmado e finanças continuam restritas.
- Recuperação com token inválido: Tentar redefinir com token inválido e senha válida; usar opção de novo pedido. Resultado esperado: Não altera senha e permite solicitar outro link.
- Recuperação expirada: Tentar redefinir após ultrapassar 60 minutos da emissão, com senha válida; solicitar novo link. Resultado esperado: Recusa sem alterar senha e oferece nova solicitação; link novo válido permite retomar.
- Recuperação já utilizada: Após redefinição bem-sucedida, reutilizar o link para outra senha e usar novo pedido. Resultado esperado: Não altera novamente a senha; informa recusa e permite solicitar outro link.
- Falha no envio da recuperação: Provocar falha controlada no envio, observar orientação e repetir após restabelecimento. Resultado esperado: Orienta nova tentativa sem falso sucesso nem afirmação explícita de existência da conta; nova solicitação permite ao titular receber link.

## Regras e permissões

- Cadastro público, sem convite ou aprovação administrativa; nome/e-mail obrigatórios até 255 caracteres, e-mail válido e único, senha e confirmação obrigatórias e iguais.
- Cadastro e redefinição exigem senha de 12 a 255 caracteres, com maiúscula, minúscula, número, símbolo e rejeição de senhas conhecidas em vazamentos.
- Acesso financeiro exige autenticação e confirmação do próprio e-mail; apenas receber a mensagem ou redefinir a senha não confirma a conta.
- Link de recuperação vale 60 minutos e não pode ser reutilizado após sucesso; a senha anterior deixa de permitir novos logins.
- Após cinco falhas consecutivas de login, a nova tentativa deve informar bloqueio temporário e espera. Lembrar acesso não dispensa confirmação nem impede saída explícita.

## Impactos relacionados

- Preservar a unicidade da conta ao repetir cadastro após falha de envio, a resposta genérica de recuperação e a confirmação idempotente de links ainda válidos.
- Preservar os campos e mensagens de validação existentes e a navegação para login e recuperação; nenhum dado financeiro é pedido no cadastro.
- Verificar conjuntamente ‘Acesso à conta - Política de senha no cadastro e na redefinição’, ‘Acesso à conta - Confirmação de e-mail com nova tentativa’ e ‘Acesso à conta - Recuperação de senha com nova tentativa’, além dos fluxos existentes de login e saída.

## Critérios de conclusão

- Executar as condições CT-001 a CT-028 do documento de condições de teste desta Feature, registrando dados/contexto, resultado observado e evidência por condição.
- Confirmar resultados de sucesso, limites, erros, titularidade, restrição financeira, validade e uso único, incluindo as jornadas existentes e a integração das três entregas.
- Registrar desvios reproduzíveis com resultado esperado e observado; condições não executadas por falta de ambiente, e-mail observável, falha controlável ou validade conhecida permanecem explicitamente impedidas, sem alegação de aprovação.

## Referências

Item pai Redmine #1015909; regras/critérios R1, R2, R3, R4, R5, R6, CA1, CA2, CA3, CA4, CA5, CA6, CA7, CA8, CA9, CA10-confirmacao, CA10-recuperacao, F1, F2, F3.

<!-- project-slices-child:0925f6bf5f31b9ce0480e1f658610ab27c0758627ab8cfadd8c3faf1252610e2 -->


## Bloqueios nativos

- [DEV] [WEB] [USUARIO] Acesso à conta - Política de senha no cadastro e na redefinição bloqueia [QA] [WEB] [USUARIO] Acesso à conta (`blocks`).
- [DEV] [WEB] [USUARIO] Acesso à conta - Confirmação de e-mail com nova tentativa bloqueia [QA] [WEB] [USUARIO] Acesso à conta (`blocks`).
- [DEV] [WEB] [USUARIO] Acesso à conta - Recuperação de senha com nova tentativa bloqueia [QA] [WEB] [USUARIO] Acesso à conta (`blocks`).

# Condições de teste

## Contexto

Feature #1015909, Acesso à conta. Preparar contas confirmadas e não confirmadas, e-mails disponíveis/inexistentes, dados válidos e inválidos e ambiente autorizado com observação de e-mails, falha de envio controlada e links com validade conhecida. Condições para execução futura; os 54 testes da base não equivalem à aprovação destes cenários.

### CT-001 — Cadastro público válido

Verificação: Como visitante, cadastrar nome e e-mail disponíveis, senha conforme R3 e confirmação igual.

Resultado esperado: Uma única conta é criada sem convite, aprovação administrativa ou dados financeiros; recebe link e é orientada a confirmar, sem acesso financeiro ainda.

Origem no requisito: R1: Cadastro público sem convite ou aprovação administrativa.; R2: Nome/e-mail obrigatórios até 255 caracteres, e-mail válido e único, senha e confirmação obrigatórias e iguais.; CA1: Cadastro válido cria uma única conta, envia confirmação e apresenta fluxo de confirmação.; F3: Dados e exceções: cadastro não solicita dados financeiros; duplicidade permite seguir para login ou recuperação.

### CT-002 — Campos obrigatórios

Verificação: No cadastro, omitir separadamente nome, e-mail, senha e confirmação; na redefinição, omitir e-mail, senha e confirmação.

Resultado esperado: Cada ausência aplicável impede concluir e exibe erro no campo; conta/senha não é criada/alterada indevidamente.

Origem no requisito: R2: Nome/e-mail obrigatórios até 255 caracteres, e-mail válido e único, senha e confirmação obrigatórias e iguais.; CA2: Ausências, e-mail inválido/duplicado, senha fora de R3 e confirmação diferente impedem conclusão e mostram erros aplicáveis.

### CT-003 — Limites de nome e e-mail

Verificação: No cadastro, usar nome/e-mail válidos com 255 caracteres e, separadamente, com 256 caracteres; demais dados válidos.

Resultado esperado: Até 255 caracteres é aceito; acima disso exibe erro e não conclui.

Origem no requisito: R2: Nome/e-mail obrigatórios até 255 caracteres, e-mail válido e único, senha e confirmação obrigatórias e iguais.; CA2: Ausências, e-mail inválido/duplicado, senha fora de R3 e confirmação diferente impedem conclusão e mostram erros aplicáveis.

### CT-004 — E-mail inválido e duplicado

Verificação: Cadastrar com e-mail inválido e com e-mail já usado; testar e-mail inválido na redefinição e acessar login/recuperação pelo fluxo existente.

Resultado esperado: Erros impedem conclusão e duplicação; o usuário consegue seguir para entrar ou recuperar acesso.

Origem no requisito: R2: Nome/e-mail obrigatórios até 255 caracteres, e-mail válido e único, senha e confirmação obrigatórias e iguais.; CA2: Ausências, e-mail inválido/duplicado, senha fora de R3 e confirmação diferente impedem conclusão e mostram erros aplicáveis.; F3: Dados e exceções: cadastro não solicita dados financeiros; duplicidade permite seguir para login ou recuperação.

### CT-005 — Limites de senha

Verificação: No cadastro e na redefinição com link válido, testar senhas não vazadas de 11, 12, 255 e 256 caracteres, com todas as classes e confirmação igual.

Resultado esperado: 12 e 255 são aceitas; 11 e 256 são recusadas com erro, sem concluir a operação.

Origem no requisito: R3: Cadastro e redefinição: senha de 12 a 255 caracteres, maiúscula, minúscula, número, símbolo e rejeição de senha vazada.; CA2: Ausências, e-mail inválido/duplicado, senha fora de R3 e confirmação diferente impedem conclusão e mostram erros aplicáveis.

### CT-006 — Composição da senha

Verificação: Nos dois fluxos, testar separadamente senha sem maiúscula, sem minúscula, sem número e sem símbolo, mantendo demais regras válidas.

Resultado esperado: Cada ausência é recusada com erro; a combinação completa não é recusada por composição.

Origem no requisito: R3: Cadastro e redefinição: senha de 12 a 255 caracteres, maiúscula, minúscula, número, símbolo e rejeição de senha vazada.; CA2: Ausências, e-mail inválido/duplicado, senha fora de R3 e confirmação diferente impedem conclusão e mostram erros aplicáveis.

### CT-007 — Senha conhecida em vazamentos

Verificação: Usar dado de teste reconhecido como vazado, que atenda tamanho e composição, no cadastro e na redefinição.

Resultado esperado: Ambos recusam com erro e não concluem.

Origem no requisito: R3: Cadastro e redefinição: senha de 12 a 255 caracteres, maiúscula, minúscula, número, símbolo e rejeição de senha vazada.; CA2: Ausências, e-mail inválido/duplicado, senha fora de R3 e confirmação diferente impedem conclusão e mostram erros aplicáveis.

### CT-008 — Confirmação diferente

Verificação: No cadastro e redefinição, informar senha válida e confirmação diferente.

Resultado esperado: Erro impede criar a conta ou alterar a senha.

Origem no requisito: R2: Nome/e-mail obrigatórios até 255 caracteres, e-mail válido e único, senha e confirmação obrigatórias e iguais.; CA2: Ausências, e-mail inválido/duplicado, senha fora de R3 e confirmação diferente impedem conclusão e mostram erros aplicáveis.

### CT-009 — Acesso sem autenticação

Verificação: Como visitante, abrir a área inicial protegida.

Resultado esperado: Exige login e não apresenta área financeira.

Origem no requisito: R4: Área financeira exige autenticação e e-mail confirmado; recebimento de e-mail não confirma.

### CT-010 — Conta não confirmada

Verificação: Entrar com conta não confirmada, tentar área protegida e reenviar confirmação; repetir com lembrar acesso selecionado.

Resultado esperado: Mantém restrição financeira, mostra orientação e permite reenviar/sair. Receber e-mail ou lembrar acesso não confirma a conta.

Origem no requisito: R4: Área financeira exige autenticação e e-mail confirmado; recebimento de e-mail não confirma.; R6: Saída encerra sessão atual; lembrar acesso não dispensa confirmação nem impede saída explícita.; CA3: Conta não confirmada não acessa finanças e pode confirmar, reenviar e sair.

### CT-011 — Confirmação válida

Verificação: Abrir link válido próprio como titular autenticado; repetir jornada começando sem sessão.

Resultado esperado: Solicita autenticação quando necessária, confirma o endereço do titular e libera a área inicial.

Origem no requisito: CA4: Titular autenticado confirma com link válido próprio; inválido, expirado ou de outra conta é recusado e permite novo pedido.

### CT-012 — Confirmação com link inválido

Verificação: Alterar um link de confirmação e abri-lo como titular não confirmado.

Resultado esperado: Recusa confirmação e acesso financeiro, orienta e oferece novo pedido.

Origem no requisito: CA4: Titular autenticado confirma com link válido próprio; inválido, expirado ou de outra conta é recusado e permite novo pedido.

### CT-013 — Confirmação expirada

Verificação: Abrir link cuja validade tenha expirado, com titular não confirmado.

Resultado esperado: Recusa confirmação e acesso financeiro, orienta e oferece novo pedido.

Origem no requisito: CA4: Titular autenticado confirma com link válido próprio; inválido, expirado ou de outra conta é recusado e permite novo pedido.

### CT-014 — Confirmação de outra conta

Verificação: Autenticado como A não confirmado, abrir link válido de B.

Resultado esperado: Não confirma A nem B indevidamente, não libera finanças e permite solicitar link da própria conta.

Origem no requisito: CA4: Titular autenticado confirma com link válido próprio; inválido, expirado ou de outra conta é recusado e permite novo pedido.

### CT-015 — Reabertura de confirmação

Verificação: Confirmar conta e reabrir o mesmo link ainda válido como titular.

Resultado esperado: Mantém confirmação e permite seguir à área inicial, sem desfazer estado.

Origem no requisito: F1: Exceções: reabrir link de confirmação ainda válido de conta já confirmada preserva confirmação.

### CT-016 — Falha de envio no cadastro

Verificação: Provocar falha controlada no envio durante cadastro válido; restaurar envio e repetir conforme orientação.

Resultado esperado: Informa falha e nova tentativa sem falso sucesso; retomada permite receber confirmação sem contas duplicadas.

Origem no requisito: CA10-confirmacao: CA10 e exceções: falha de envio no cadastro/reenvio orienta nova tentativa sem afirmar conclusão dependente do e-mail.; CA1: Cadastro válido cria uma única conta, envia confirmação e apresenta fluxo de confirmação.

### CT-017 — Falha de envio no reenvio

Verificação: Com conta não confirmada, provocar falha de reenvio, restaurar serviço e tentar novamente.

Resultado esperado: Apresenta orientação sem alegar envio concluído; nova tentativa recebe link e permite confirmação.

Origem no requisito: CA10-confirmacao: CA10 e exceções: falha de envio no cadastro/reenvio orienta nova tentativa sem afirmar conclusão dependente do e-mail.; CA3: Conta não confirmada não acessa finanças e pode confirmar, reenviar e sair.

### CT-018 — Login e destino solicitado

Verificação: Com conta confirmada, entrar com credenciais corretas diretamente e após solicitar página protegida.

Resultado esperado: Acessa área inicial ou destino protegido solicitado.

Origem no requisito: CA5: Credenciais corretas entram; incorretas não; após cinco falhas, nova tentativa informa bloqueio e espera.; F2: Fluxo principal: login retorna à área inicial ou destino protegido solicitado; saída retorna à página pública.

### CT-019 — Credenciais incorretas

Verificação: Tentar entrar com senha errada ou conta inexistente.

Resultado esperado: Não autentica e apresenta erro.

Origem no requisito: CA5: Credenciais corretas entram; incorretas não; após cinco falhas, nova tentativa informa bloqueio e espera.

### CT-020 — Bloqueio temporário de login

Verificação: Para o mesmo e-mail e origem, realizar cinco falhas consecutivas; tentar novamente durante bloqueio e após a espera informada.

Resultado esperado: A nova tentativa durante bloqueio informa espera sem autenticar; terminado o prazo, credenciais válidas permitem entrar.

Origem no requisito: CA5: Credenciais corretas entram; incorretas não; após cinco falhas, nova tentativa informa bloqueio e espera.

### CT-021 — Saída explícita

Verificação: Entrar em conta confirmada, sair e reabrir área protegida; repetir com lembrar acesso selecionado.

Resultado esperado: Retorna à página pública, encerra sessão atual e exige login novamente mesmo com lembrança anterior.

Origem no requisito: R6: Saída encerra sessão atual; lembrar acesso não dispensa confirmação nem impede saída explícita.; CA6: Após sair, área protegida exige login, inclusive com lembrar acesso selecionado.; F2: Fluxo principal: login retorna à área inicial ou destino protegido solicitado; saída retorna à página pública.

### CT-022 — Resposta genérica de recuperação

Verificação: Solicitar recuperação para e-mail cadastrado e para e-mail inexistente, com envio disponível.

Resultado esperado: Exibe a mesma resposta genérica; titular cadastrado recebe link sem informação de existência ao solicitante.

Origem no requisito: CA7: Recuperação tem resposta genérica para e-mail existente/inexistente e envia link ao titular quando existente.

### CT-023 — Redefinição válida

Verificação: Com link próprio não usado, antes de 60 minutos, definir senha conforme R3 e confirmação igual; testar logins com senha anterior e nova.

Resultado esperado: Retorna ao login; nova senha funciona e antiga não permite novos logins.

Origem no requisito: R3: Cadastro e redefinição: senha de 12 a 255 caracteres, maiúscula, minúscula, número, símbolo e rejeição de senha vazada.; R5: Recuperação válida por 60 minutos, uso único e senha anterior sem novos logins após sucesso.; CA8: Redefinição válida com R3 retorna ao login; nova senha funciona, antiga não; e-mail não confirmado continua restrito.

### CT-024 — Redefinição de conta não confirmada

Verificação: Redefinir com link válido uma conta não confirmada e entrar com a nova senha.

Resultado esperado: Senha é alterada, mas e-mail não é confirmado e finanças continuam restritas.

Origem no requisito: R4: Área financeira exige autenticação e e-mail confirmado; recebimento de e-mail não confirma.; CA8: Redefinição válida com R3 retorna ao login; nova senha funciona, antiga não; e-mail não confirmado continua restrito.

### CT-025 — Recuperação com token inválido

Verificação: Tentar redefinir com token inválido e senha válida; usar opção de novo pedido.

Resultado esperado: Não altera senha e permite solicitar outro link.

Origem no requisito: CA9: Recuperação com link inválido, expirado ou utilizado não muda senha e oferece nova solicitação.

### CT-026 — Recuperação expirada

Verificação: Tentar redefinir após ultrapassar 60 minutos da emissão, com senha válida; solicitar novo link.

Resultado esperado: Recusa sem alterar senha e oferece nova solicitação; link novo válido permite retomar.

Origem no requisito: R5: Recuperação válida por 60 minutos, uso único e senha anterior sem novos logins após sucesso.; CA9: Recuperação com link inválido, expirado ou utilizado não muda senha e oferece nova solicitação.

### CT-027 — Recuperação já utilizada

Verificação: Após redefinição bem-sucedida, reutilizar o link para outra senha e usar novo pedido.

Resultado esperado: Não altera novamente a senha; informa recusa e permite solicitar outro link.

Origem no requisito: R5: Recuperação válida por 60 minutos, uso único e senha anterior sem novos logins após sucesso.; CA9: Recuperação com link inválido, expirado ou utilizado não muda senha e oferece nova solicitação.

### CT-028 — Falha no envio da recuperação

Verificação: Provocar falha controlada no envio, observar orientação e repetir após restabelecimento.

Resultado esperado: Orienta nova tentativa sem falso sucesso nem afirmação explícita de existência da conta; nova solicitação permite ao titular receber link.

Origem no requisito: CA10-recuperacao: CA10 e exceções: falha de envio de recuperação orienta nova tentativa sem afirmar conclusão dependente do e-mail.; CA7: Recuperação tem resposta genérica para e-mail existente/inexistente e envia link ao titular quando existente.

## Documento a anexar — incluído nesta aprovação final

- Destino: [QA] [WEB] [USUARIO] Acesso à conta
- Arquivo: [condicoes-teste-r002.docx](file:///C:/Users/maari/Herd/github/fin-ai/docs/harness/features/1015909-acesso-a-conta/slices/condicoes-teste-r002.docx)
- Revisão: 002
- Tamanho: 5418 bytes
- SHA-256: `bb433a8b2a42b3d026cacb0b576ff1386bda52fd6d2a17faa518fdf9ab0defea`
- Descrição do anexo: Condições de teste — revisão 002
- A aprovação autoriza acrescentar exatamente este documento, preservando os demais campos e anexos da QA.
