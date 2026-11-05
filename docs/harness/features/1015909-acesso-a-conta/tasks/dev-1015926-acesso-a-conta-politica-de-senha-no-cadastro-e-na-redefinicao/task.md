# [DEV] [WEB] [USUARIO] Acesso à conta - Política de senha no cadastro e na redefinição

- Redmine: `#1015926`
- Tipo: `DEV`
- Tracker: Task (`4`)
- Item pai: `#1015909`
- Estimativa: `2h`

## Descrição

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

## Relações

- `#1015926` blocks `#1015929`
