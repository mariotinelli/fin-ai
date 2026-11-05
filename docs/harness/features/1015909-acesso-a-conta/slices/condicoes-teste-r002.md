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
