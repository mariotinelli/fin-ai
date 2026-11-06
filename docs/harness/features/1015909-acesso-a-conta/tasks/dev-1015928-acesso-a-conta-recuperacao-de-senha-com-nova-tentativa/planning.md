# DEV #1015928 — Acesso à conta: recuperação de senha com nova tentativa

## Identidade e fontes

- Filha DEV: `#1015928`, descrita em `docs/harness/features/1015909-acesso-a-conta/tasks/dev-1015928-acesso-a-conta-recuperacao-de-senha-com-nova-tentativa/task.md`.
- Requisito pai: `docs/harness/features/1015909-acesso-a-conta/feature.md`, especialmente R4, R5, CA7, CA8, CA9 e CA10.
- Implementação inspecionada: `routes/web.php`; `app/Actions/CreateUserEmailResetNotification.php`; `app/Actions/CreateUserPassword.php`; `app/Http/Controllers/UserEmailResetNotificationController.php`; `app/Http/Controllers/UserPasswordController.php`; `app/Http/Requests/CreateUserEmailResetNotificationRequest.php`; `app/Http/Requests/CreateUserPasswordRequest.php`; `app/Models/User.php`; `config/auth.php`; e as páginas Inertia em `resources/js/pages/user-email-reset-notification/create.tsx` e `resources/js/pages/user-password/create.tsx`.
- Cobertura existente inspecionada: `tests/Feature/Controllers/UserEmailResetNotificationTest.php`, `tests/Feature/Controllers/UserPasswordControllerTest.php`, `tests/Unit/Actions/CreateUserEmailResetNotificationTest.php` e `tests/Unit/Actions/CreateUserPasswordTest.php`.
- Comportamento do framework confirmado em `Illuminate\Auth\Passwords\PasswordBroker` e `Illuminate\Auth\Passwords\DatabaseTokenRepository`, na versão instalada de `laravel/framework` 13.40.0.

## Objetivo

Completar a recuperação de senha para que uma falha real na entrega do e-mail resulte em orientação genérica e permita nova tentativa, enquanto links inválidos, expirados após 60 minutos ou já utilizados preservem a senha e ofereçam um caminho visível para solicitar outro link. Manter a resposta indistinguível para contas existentes e inexistentes no fluxo normal, o uso único do token, a troca efetiva das credenciais e o estado de verificação do e-mail.

## Estado atual

- As rotas guest `password.request`, `password.email`, `password.reset` e `password.store` já formam um fluxo próprio com controladores, Actions, Form Requests, páginas Inertia e rotas Wayfinder (`routes/web.php`).
- `UserEmailResetNotificationController::store()` ignora o status retornado pela Action e sempre apresenta a mensagem genérica. Isso já evita distinguir conta existente de inexistente, mas uma exceção do canal de notificação não é convertida em orientação de nova tentativa.
- `CreateUserEmailResetNotification::handle()` delega diretamente a `Password::sendResetLink()`. O broker cria o token antes de chamar `User::sendPasswordResetNotification()`; se a entrega lançar uma exceção, o token permanece e o throttle de 60 segundos pode bloquear a nova tentativa imediata.
- `config/auth.php` fixa a validade do token em 60 minutos e o throttle em 60 segundos. O broker valida expiração e hash, e remove o token depois de uma redefinição bem-sucedida, garantindo uso único.
- `UserPasswordController::store()` já converte token ou conta inválidos em erro de validação no campo `email`. A página `user-password/create.tsx` exibe esse erro, mas não oferece um link para `password.request`.
- O teste de redefinição bem-sucedida já prova retorno ao login, nova senha válida, senha anterior inválida, evento de reset e preservação de `email_verified_at = null` com bloqueio do dashboard. Há teste de token inválido, porém ele não comprova explicitamente a preservação do hash; não há casos explícitos para expiração e reutilização.

## Escopo

Entra no escopo:

- tratamento observável da indisponibilidade do envio de recuperação, com registro da exceção, mensagem genérica e possibilidade de repetir a solicitação;
- limpeza do token criado quando a entrega falhar, sem alterar a resposta normal de conta existente, inexistente ou throttled;
- caminho visível e tipado por Wayfinder para voltar à solicitação de recuperação após erro de token;
- cobertura dos tokens inválido, expirado e já usado, incluindo não alteração da senha;
- preservação e reutilização da cobertura existente para sucesso, troca de credenciais e conta não verificada.

Ficam fora do escopo:

- política de composição da senha, pertencente à DEV #1015926;
- confirmação e reenvio de verificação de e-mail, pertencentes à DEV #1015927;
- alteração global do canal de e-mail, filas, templates de notificação, throttle, validade de 60 minutos ou recursos Fortify opcionais;
- mudanças em login, passkeys, 2FA ou perfil sem relação direta com a recuperação.

## Arquitetura

- Preservar o padrão Action da aplicação: o controlador coordena request e resposta, enquanto `CreateUserEmailResetNotification` mantém a operação de envio e a compensação do token quando a entrega falha.
- Continuar usando o password broker configurado em `config/auth.php`; não duplicar validação de tokens nem criar armazenamento paralelo.
- Manter a notificação síncrona neste fluxo, pois a resposta precisa distinguir uma indisponibilidade real de entrega de uma solicitação normalmente processada. Dentro do callback suportado por `PasswordBroker::sendResetLink()`, enviar a notificação e disparar `PasswordResetLinkSent` no sucesso; ao capturar falha, apagar somente o token do usuário daquela tentativa e propagar a exceção para o controlador reportá-la e produzir a orientação segura.
- Não expor a existência da conta: `INVALID_USER`, `RESET_LINK_SENT` e `RESET_THROTTLED` continuam recebendo a mesma confirmação genérica. Somente uma exceção operacional observada durante a entrega gera a orientação também genérica de tentar novamente, sem mencionar conta, endereço encontrado ou token criado.
- Reutilizar os componentes de formulário, erro, botão e link existentes. A navegação cliente deve importar a rota nomeada de `@/routes/password`, sem URL literal, e seguir o padrão Inertia `<Form>`/`TextLink` já presente.
- Não alterar defaults compartilhados de notificações, autenticação ou middleware; os consumidores de cadastro, confirmação de e-mail e atualização de senha permanecem fora do alcance.

## Estratégia

Primeiro tornar a solicitação resiliente e demonstrar que uma falha de entrega não deixa o usuário preso pelo token/throttle. Depois completar a saída de erro da redefinição e os casos de validade e uso único do token. Cada fase atualiza os testes de feature que comprovam o contrato HTTP e o estado persistido; testes unitários das Actions permanecem focados nos resultados do broker e na compensação específica. Ao fim de cada fase, executar os testes focados e o Gate 3 completo.

## Baseline

O script agregado `composer test` foi inspecionado: ele encadeia Pint em modo teste, Rector dry-run, lint frontend, PHPStan, TypeScript, cobertura de tipos e Pest paralelo com cobertura exata de 100%. No Windows, sua etapa `test:unit` usa a atribuição Unix `XDEBUG_MODE="coverage"` e falhou no `cmd` depois que as etapas anteriores passaram. O comando abaixo preserva todos os verificadores, seleciona PHP 8.5 somente no processo e usa a sintaxe PowerShell suportada pelo executor:

```powershell
$env:Path = 'C:\Users\maari\.config\herd\bin\php85;' + $env:Path
$env:XDEBUG_MODE = 'coverage'
composer test:lint
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
composer test:types
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
composer test:type-coverage
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& '.\vendor\bin\pest.bat' --parallel --coverage --exactly=100.0
exit $LASTEXITCODE
```

Pré-requisitos observados: Windows PowerShell, Composer, Bun 1.4.4, dependências instaladas, PHP 8.5 do Herd no caminho acima e Xdebug 3.5.0. O PHP padrão do terminal é 8.4.27 e não atende ao projeto. O PHP 8.5 emite um aviso de incompatibilidade ao tentar carregar uma cópia antiga do OPcache, mas continua com PHP 8.5.12 e Xdebug; o aviso não interrompeu nenhum verificador.

| Verificador | Invocação/configuração | Exigência relevante | Resultado observado |
| --- | --- | --- | --- |
| Pint | `composer test:lint` → `pint --parallel --test` | Apenas verificação | Passou |
| Rector | `composer test:lint` → `rector --dry-run` | Nenhuma alteração permitida | Passou, zero arquivos alterados |
| Frontend lint/format | `composer test:lint` → `bun run test:lint` | Vite Plus em modo check/lint | Passou em 66 arquivos |
| PHPStan | `composer test:types` → `phpstan` | PHP 8.5 selecionado no processo | Passou, zero erros |
| TypeScript | `composer test:types` → `bun run test:types` | `tsc --noEmit` | Passou |
| Cobertura de tipos | `composer test:type-coverage` | Mínimo de 100% | Passou, 100% |
| Pest e cobertura | chamada direta a `vendor/bin/pest.bat` | Paralelo e cobertura exata de 100% com Xdebug | Passou: 208 testes, 1.017 asserções, 100% |

## Riscos

- O broker cria o token antes de enviar a notificação. Sem compensação restrita à exceção de entrega, uma indisponibilidade deixa um token não entregue e ativa o throttle; apagar tokens em outros resultados invalidaria links válidos e não deve ocorrer.
- Capturar a exceção sem reportá-la esconderia uma falha operacional. A resposta ao usuário deve ser sanitizada, mas o erro original deve seguir o mecanismo de reporte do Laravel.
- Reimplementar o envio via callback do broker exige preservar o evento `PasswordResetLinkSent` no caminho de sucesso, pois o callback substitui o envio padrão do broker.
- Mensagens diferentes para `INVALID_USER`, sucesso ou throttle permitiriam enumeração. Esses resultados devem continuar convergindo para a mesma confirmação.
- Os erros de token chegam hoje no campo `email`; mudar a chave pode quebrar o formulário e testes existentes. O caminho de nova solicitação deve complementar esse contrato, sem revelar se o erro decorreu de token expirado, inválido ou usado.
- Testes de expiração dependem de tempo controlado e os de reutilização precisam provar que a segunda tentativa não altera novamente o hash. Evitar sleeps e controlar o relógio com os helpers do framework.
- O Gate 3 depende do caminho local do PHP 8.5 e do PowerShell; uma mudança na instalação do Herd exigirá atualizar o baseline antes de executar.

## Fase 1 — Envio resiliente e nova tentativa segura

### Objetivo

Quando a entrega do e-mail de recuperação falhar, orientar o visitante a tentar novamente sem afirmar envio nem revelar a existência da conta, além de permitir que a próxima solicitação válida envie um link sem ficar bloqueada pelo token criado na tentativa falha.

### Dependências

Fluxo existente de solicitação de recuperação, password broker `users`, notificação padrão `ResetPassword` e resposta Inertia da página `user-email-reset-notification/create`.

### Mudanças esperadas

- Adaptar `CreateUserEmailResetNotification` para controlar o callback de envio do broker: preservar o resultado e evento de sucesso, remover o token recém-criado se a notificação lançar e propagar a falha.
- Tratar a falha no `UserEmailResetNotificationController`, reportando a exceção e retornando uma orientação genérica de nova tentativa em prop/flash separada do status de sucesso.
- Exibir a orientação na página de solicitação com os componentes e estados visuais existentes, sem ecoar dados da conta nem substituir a confirmação genérica dos resultados normais.
- Expandir testes da Action e do endpoint para provar sucesso, conta inexistente indistinguível, falha reportada, ausência de confirmação de envio e uma nova solicitação utilizável após a recuperação do canal.

### Arquivos prováveis

- `app/Actions/CreateUserEmailResetNotification.php`
- `app/Http/Controllers/UserEmailResetNotificationController.php`
- `resources/js/pages/user-email-reset-notification/create.tsx`
- `tests/Unit/Actions/CreateUserEmailResetNotificationTest.php`
- `tests/Feature/Controllers/UserEmailResetNotificationTest.php`

### Limites

- Não alterar validade, throttle, driver de e-mail, template da notificação ou respostas de cadastro/confirmação.
- Não mostrar mensagens diferentes para conta inexistente, solicitação aceita ou throttle.
- Apagar somente o token criado para o usuário cuja entrega lançou; não limpar tokens por validação, inexistência de conta ou resultados normais do broker.
- Não engolir a exceção sem reporte e não expor detalhes técnicos ao usuário.

### Estratégia

Usar o callback público do broker para conservar a geração e validação nativas, adicionando apenas o envio observável, o evento esperado e a compensação em caso de exceção. No limite HTTP, converter essa exceção já compensada em flash seguro. Isolar o canal de notificação nos testes, afirmar o reporte e fazer duas solicitações consecutivas no cenário falha→restabelecimento para demonstrar que o throttle não reteve um token não entregue.

### Aceite

- Conta existente com canal disponível recebe uma notificação de reset e vê a mesma confirmação genérica atual.
- Conta inexistente não recebe notificação e vê confirmação indistinguível da conta existente.
- Exceção de entrega é reportada, não apresenta confirmação de envio e mostra orientação genérica para tentar novamente.
- Restabelecido o canal, uma nova solicitação imediata para o mesmo titular envia um link utilizável, comprovando a remoção do token da tentativa falha.
- Nenhuma mensagem revela explicitamente se o e-mail pertence a uma conta.

### Verificação focada

- `php artisan test --compact tests/Unit/Actions/CreateUserEmailResetNotificationTest.php`
- `php artisan test --compact tests/Feature/Controllers/UserEmailResetNotificationTest.php`
- Revisar a página com o lint/types do frontend incluídos no Gate 3.

## Fase 2 — Recuperação após token inválido, expirado ou utilizado

### Objetivo

Garantir que qualquer token sem validade não altere a senha e ofereça no formulário um caminho claro para solicitar outro, preservando o sucesso de uso único, a troca de credenciais e a restrição da conta não verificada.

### Dependências

Fase 1 concluída para que o caminho de nova solicitação também tenha tratamento de falha e repetição seguro. Configuração existente de expiração em 60 minutos e remoção do token após `Password::reset()`.

### Mudanças esperadas

- Acrescentar à página `user-password/create` um `TextLink` para a rota Wayfinder `password.request`, apresentado junto ao erro de redefinição e sem codificar URL literal.
- Completar os testes de `UserPasswordController` com token inválido, expirado após 60 minutos e reutilizado depois de sucesso, sempre verificando que a tentativa rejeitada não altera a senha.
- Manter e, quando necessário, reutilizar o cenário existente que prova reset válido, redirecionamento ao login, login apenas com a senha nova e preservação de `email_verified_at = null` com área financeira bloqueada.

### Arquivos prováveis

- `resources/js/pages/user-password/create.tsx`
- `tests/Feature/Controllers/UserPasswordControllerTest.php`

### Limites

- Não validar tokens no GET nem inventar um segundo mecanismo de expiração; continuar delegando ao password broker no POST.
- Não distinguir visualmente token inválido, expirado, usado ou e-mail divergente; todos permanecem no contrato sanitizado de erro de redefinição.
- Não alterar a política de senha, o tempo de 60 minutos, a semântica de guest middleware ou o estado de verificação do e-mail.
- Não duplicar em novos testes as matrizes da política de senha já cobertas.

### Estratégia

Usar relógio controlado para ultrapassar 60 minutos sem espera real. Para uso único, concluir um reset, guardar o hash resultante e submeter novamente o mesmo token com outra senha válida, comprovando erro e hash inalterado. Para token inválido e expirado, guardar o hash anterior e afirmar a ausência de mutação. Reutilizar os asserts existentes da jornada de sucesso em vez de criar uma segunda cópia integral.

### Aceite

- Token inválido não altera o hash, retorna erro de redefinição e a página oferece nova solicitação.
- Token expirado depois de 60 minutos não altera o hash, retorna o mesmo contrato sanitizado e oferece nova solicitação.
- Token usado com sucesso não pode alterar a senha novamente; a segunda tentativa preserva o hash da primeira redefinição e oferece nova solicitação.
- Token válido dentro de 60 minutos continua redefinindo uma única vez e retorna ao login.
- A senha nova permite login, a anterior deixa de permitir, e uma conta não verificada continua não verificada e bloqueada da área financeira.

### Verificação focada

- `php artisan test --compact tests/Feature/Controllers/UserPasswordControllerTest.php`
- `bun run test:types`
- Executar o comando completo do Baseline antes do commit da fase.
