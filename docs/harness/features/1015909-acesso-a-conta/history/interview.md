# Entrevista — Acesso à conta

Catálogo aprovado pelo usuário: “catalogo aprovado”. Primeiro item, sem dependências. Cadastro público, login, saída e recuperação de senha confirmados; finanças separadas por usuário. A base existe em routes/web.php, UserController e telas do starter kit. Ainda não constitui aceite funcional.

## Rodada 1 — perguntas abertas

Q1 — Identificação da conta: manter cadastro com nome, e-mail e senha, login por e-mail/senha e recuperação por link enviado ao e-mail? Recomendação: manter esse fluxo da base existente; alternativa: indicar outra forma de acesso.

Q2 — Confirmação de e-mail: exigir confirmação antes de acessar as finanças ou permitir acesso imediato? A rota atual do dashboard exige e-mail verificado. Recomendação: exigir confirmação; usuário recebe link e só acessa finanças após confirmar.

As respostas ainda não foram recebidas. Após resolver identificação e confirmação, revisar os fluxos de recuperação, erros e retorno ao acesso. Detalhes técnicos pertencem à implementação.


## Resposta à rodada 1

Usuário: “concordo”. Q1 e Q2 resolvidas: cadastro com nome, e-mail e senha; login por e-mail/senha; recuperação por link no e-mail; confirmação do e-mail obrigatória antes do acesso financeiro.

## Evidências complementares

CreateUserRequest exige nome, e-mail único e confirmação de senha. CreateUser dispara Registered e User implementa MustVerifyEmail. Recuperação retorna mensagem genérica independentemente da existência da conta. Redefinição bem-sucedida retorna ao login. config/auth.php prevê link de recuperação por 60 minutos. A configuração existente de senha em produção exige 12 a 255 caracteres, letras maiúsculas e minúsculas, número, símbolo e rejeição de senhas comprometidas; em outros ambientes a política difere. Esses fatos orientam a proposta, sem constituir decisões do usuário.

## Rodada 2 — validação de senha

Q3 — Manter a regra de senha atual de produção (12 a 255 caracteres, maiúscula, minúscula, número, símbolo e rejeição de senha conhecida em vazamentos) no cadastro e na redefinição, ou adotar outra regra? A regra determina os erros e instruções mostrados ao usuário. Recomendação: manter a regra existente; pendente de resposta.


## Resposta à rodada 2 e revisão

Usuário: “sim”. Q3 resolvida. Requisito completo preparado para revisão conjunta com publicação. Fluxos de exceção e valores existentes explicitados como proposta no documento final, sem atribuir respostas adicionais ao usuário. Busca na Sprint 1: zero issues; baseline 0 + posição 1 = Sequencing 1. Sem categorias no projeto. Nenhuma mutação remota.


Requisito e operações aprovados pelo usuário: “aprovado”. Consentimento registrado em 2026-11-04T19:09:09.832070+00:00.


Publicação concluída: issue #1015909, Sprint 1, Sequencing 1 e status New. Criação e atualização autorizadas concluídas e leitura final validada. Redmine converteu quebras de linha para CRLF; comparada equivalência do conteúdo e preservado o texto externo.
