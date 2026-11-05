# [QA] [WEB] [USUARIO] Acesso à conta

- Redmine: `#1015929`
- Tipo: `QA`
- Tracker: Deliverable (`5`)
- Item pai: `#1015909`
- Estimativa: `1.5h`

## Descrição

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

## Relações

- `#1015926` blocks `#1015929`
- `#1015927` blocks `#1015929`
- `#1015928` blocks `#1015929`
