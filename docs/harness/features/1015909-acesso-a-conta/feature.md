# [WEB] [USUARIO] Acesso à conta

## Objetivo

Permitir cadastro público, acesso à conta pessoal e recuperação de senha, aproveitando a base existente.

## Resultado esperado

O usuário cria sua conta, confirma o e-mail, entra, sai e recupera o acesso. A área financeira exige autenticação e e-mail confirmado.

## Atores e permissões

Visitantes podem cadastrar-se, entrar e pedir recuperação. Usuários sem e-mail confirmado podem confirmar, reenviar o link e sair, mas não acessar finanças. Usuários confirmados acessam seu espaço pessoal.

## Histórias de usuário

1. Como visitante, quero cadastrar nome, e-mail e senha para ter uma conta própria.
2. Como titular, quero confirmar meu e-mail para liberar o acesso financeiro.
3. Como titular, quero entrar com minhas credenciais e sair ao terminar.
4. Como titular, quero recuperar uma senha esquecida por link enviado ao meu e-mail.

## Fluxo principal

1. Informar nome, e-mail, senha e confirmação da senha. Com dados válidos, criar a conta, enviar confirmação por e-mail e orientar o usuário a confirmar.
2. Abrir o link válido da própria conta, autenticando-se quando necessário. Confirmar o endereço e liberar a área inicial autenticada.
3. Nos acessos seguintes, entrar com e-mail e senha. Conta confirmada com credenciais corretas acessa a área inicial ou o destino protegido solicitado.
4. Ao sair, encerrar a sessão atual e retornar à página pública inicial.
5. Na recuperação, informar o e-mail, receber o link e definir nova senha com confirmação. Após sucesso, retornar ao login.

## Fluxos alternativos e exceções

- Dados inválidos exibem erros nos campos e impedem a conclusão. E-mail já cadastrado não cria outra conta; o usuário pode entrar ou recuperar o acesso.
- Credenciais incorretas não liberam acesso. Após cinco falhas consecutivas, bloquear novas tentativas temporariamente e informar a espera, conforme a base existente.
- Conta não confirmada recebe orientação para confirmar, reenviar o link ou sair. Link inválido, expirado ou de outra conta não confirma o endereço e permite solicitar outro.
- Recuperação informa que um link será enviado se a conta existir, sem distinguir conta existente de inexistente.
- Link de recuperação inválido, expirado ou já utilizado não altera a senha e permite nova solicitação.
- Falha no envio de e-mail apresenta orientação para nova tentativa, sem afirmar que a confirmação ou recuperação foi concluída.
- Reabrir um link de confirmação ainda válido de conta já confirmada mantém a confirmação. Redefinir senha não confirma o e-mail.

## Regras de negócio

R1. Cadastro público, sem convite ou aprovação administrativa.

R2. Nome e e-mail obrigatórios, com até 255 caracteres cada; e-mail válido e único por conta. Senha e confirmação obrigatórias e iguais.

R3. Cadastro e redefinição exigem senha de 12 a 255 caracteres, com maiúscula, minúscula, número e símbolo, rejeitando senhas conhecidas em vazamentos.

R4. Acesso financeiro exige autenticação e e-mail confirmado. Apenas receber o e-mail não confirma a conta.

R5. Link de recuperação válido por 60 minutos, sem reutilização após sucesso. A senha anterior deixa de permitir novos logins.

R6. Sair encerra a sessão atual. A opção existente de lembrar o acesso pode ser mantida; não dispensa confirmação do e-mail nem impede saída explícita.

## Dados percebidos pelo usuário

Nome, e-mail, senha, confirmação da senha, opção de lembrar acesso, links de confirmação e recuperação, instruções e mensagens de erro, espera e sucesso. Nenhum dado financeiro é solicitado no cadastro.

## Critérios de aceite

CA1. Com dados válidos e e-mail disponível, cadastrar cria uma única conta, envia o link e apresenta o fluxo de confirmação.

CA2. Campos obrigatórios ausentes, e-mail inválido ou duplicado, senha fora de R3 ou confirmação diferente impedem a conclusão e exibem erros, no cadastro e na redefinição quando aplicável.

CA3. Conta não confirmada não acessa finanças; recebe orientação, pode reenviar confirmação e sair.

CA4. Titular autenticado com link válido da própria conta confirma o endereço e libera acesso. Link inválido, expirado ou de outra conta não libera acesso.

CA5. Conta confirmada com credenciais corretas entra; credenciais incorretas não. Após cinco falhas consecutivas, nova tentativa informa bloqueio temporário e espera.

CA6. Ao sair, a área protegida volta a exigir login, inclusive quando lembrar acesso havia sido selecionado.

CA7. Solicitar recuperação apresenta resposta genérica para contas existentes ou inexistentes; para conta existente, envia o link ao e-mail cadastrado.

CA8. Link de recuperação válido e nova senha conforme R3 permitem redefinir e retornar ao login. A nova senha funciona e a anterior não permite novos logins. Sem confirmação prévia do e-mail, a restrição financeira permanece.

CA9. Link de recuperação expirado, inválido ou utilizado não altera a senha e oferece nova solicitação.

CA10. Falha no envio de e-mail apresenta orientação para nova tentativa, sem confirmação de conclusão da operação dependente do e-mail.

## Dependências

Sem dependência de outra Feature. Envio de e-mails necessário à confirmação e recuperação. Os números e operações financeiras serão entregues nas Features seguintes.

## Designs e evidências

Catálogo aprovado e respostas Q1, Q2 e Q3. O design é apenas visual e não contém telas de acesso. Base inspecionada: routes/web.php, CreateUserRequest, CreateSessionRequest, controladores de acesso, notificações, User e config/auth.php. Existência de código não substitui aceite.

## Dentro do escopo

Cadastro público, login, saída, confirmação e reenvio de e-mail, recuperação e redefinição de senha esquecida, com os fluxos e validações descritos.

## Fora do escopo

Gestão administrativa de usuários e ampliação de perfil, autenticação social, passkeys ou autenticação em dois fatores não são entregas deste requisito; não se solicita remover recursos existentes. Operações financeiras, seu isolamento, cálculos e IA pertencem às próximas Features.
