# Planejamento DEV 1015927 — Confirmação de e-mail com nova tentativa

## Identidade e fontes

- Filha DEV `#1015927`: `docs/harness/features/1015909-acesso-a-conta/tasks/dev-1015927-acesso-a-conta-confirmacao-de-e-mail-com-nova-tentativa/task.md`.
- Requisito pai `#1015909`: `docs/harness/features/1015909-acesso-a-conta/feature.md`, especialmente R4, CA1, CA3, CA4 e CA10.
- Implementação inspecionada: `routes/web.php`, `bootstrap/app.php`, `app/Actions/CreateUser.php`, `app/Actions/CreateUserEmailVerificationNotification.php`, `app/Http/Controllers/UserController.php`, `app/Http/Controllers/UserEmailVerificationController.php`, `app/Http/Controllers/UserEmailVerificationNotificationController.php`, `app/Http/Requests/UpdateEmailVerificationRequest.php`, `app/Models/User.php`, `resources/js/pages/user/create.tsx`, `resources/js/pages/user-email-verification-notification/create.tsx`, `resources/js/components/alert-error.tsx` e `app/Http/Middleware/HandleInertiaRequests.php`.
- Comportamento do framework inspecionado: `Illuminate\Auth\Listeners\SendEmailVerificationNotification`, `Illuminate\Foundation\Auth\EmailVerificationRequest`, `Illuminate\Routing\Middleware\ValidateSignature` e `Illuminate\Routing\Exceptions\InvalidSignatureException`, nas versões instaladas `laravel/framework 13.40.0`, `laravel/fortify 1.41.0`, `inertiajs/inertia-laravel 3.7.0`, `@inertiajs/react 3.11.0` e `laravel/wayfinder 0.1.23`.
- Cobertura existente inspecionada: `tests/Feature/Controllers/UserControllerTest.php`, `tests/Feature/Controllers/UserEmailVerificationTest.php`, `tests/Feature/Controllers/UserEmailVerificationNotificationControllerTest.php`, `tests/Unit/Actions/CreateUserTest.php` e `tests/Unit/Actions/CreateUserEmailVerificationNotificationTest.php`.

## Objetivo

Completar a jornada de confirmação de e-mail para que cadastro e reenvio comuniquem falhas reais de entrega e ofereçam nova tentativa sem sucesso falso ou conta duplicada, enquanto links inválidos, expirados ou pertencentes a outra conta conduzem o titular autenticado à solicitação de um novo link. Preservar a confirmação por link válido, a autenticação antes da confirmação quando necessária, a idempotência de links válidos já usados e a restrição do dashboard a e-mails confirmados.

## Estado atual

O cadastro valida os dados, chama `CreateUser` e autentica o resultado. A Action cria o usuário e dispara `Registered` dentro de `DB::transaction()`. O listener síncrono instalado pelo framework chama `sendEmailVerificationNotification()` antes de a transação terminar; portanto uma exceção do transporte de e-mail hoje propaga até a resposta e desfaz a criação, mas aparece ao usuário como erro do servidor, sem orientação. A transação já fornece a semântica necessária para uma nova submissão criar somente uma conta, desde que a falha seja convertida em resposta recuperável sem ocultar exceções não relacionadas.

O reenvio passa por `CreateUserEmailVerificationNotification` e só grava `verification-link-sent` depois que a chamada retorna. Uma falha também propaga como erro do servidor; a página sabe apresentar apenas o status de sucesso e não renderiza os erros do formulário. O endpoint já evita envio para uma conta confirmada e possui limite de seis tentativas por minuto.

O link de confirmação exige autenticação, assinatura válida e o limite de seis tentativas por minuto. `EmailVerificationRequest` compara o `id` e o hash do e-mail da URL com o usuário autenticado antes de `fulfill()`. Assim, uma assinatura inválida ou expirada termina em `InvalidSignatureException` 403 no middleware; um link válido de outra conta ou com hash incompatível termina em `AuthorizationException` 403 no Form Request. Nenhum desses caminhos confirma e-mail, porém também não apresenta a orientação nem o caminho de reenvio exigidos. Um link válido da própria conta confirma e redireciona ao dashboard; se a conta já estiver confirmada, o controlador mantém o estado e faz o mesmo redirecionamento.

Os testes atuais demonstram criação única e evento `Registered`, bloqueio do dashboard para conta não confirmada, reenvio bem-sucedido, confirmação válida, reabertura de link válido e 403 para assinatura ausente. Ainda não demonstram a notificação efetiva no cadastro, falhas de transporte e recuperação, expiração, link de outra conta, autenticação intermediária nem mensagens recuperáveis para links recusados.

## Escopo

Entram o tratamento localizado da indisponibilidade do transporte nos endpoints de cadastro e reenvio, a apresentação dos erros na interface de confirmação, a recuperação de links recusados no endpoint de verificação e testes comportamentais dos casos de sucesso, falha e preservação descritos pela filha.

Não entram troca de provedor ou configuração de e-mail, filas ou retentativas automáticas, mudanças na política de senha, recuperação de senha, perfil, passkeys, dois fatores, relaxamento de assinatura/autorização, alteração dos limites de requisição, novas dependências, schema ou dados financeiros.

## Arquitetura

As Actions existentes continuam sendo as fronteiras das operações de criação e reenvio, e os controladores permanecem responsáveis por converter o resultado ou uma falha esperada de infraestrutura em resposta HTTP. O tratamento deve reconhecer somente falhas do transporte de e-mail compatíveis com o contrato do Symfony Mailer; erros de programação ou de persistência não devem ser apresentados como simples indisponibilidade de envio. No cadastro, a captura acontece fora da Action para que a exceção atravesse `DB::transaction()`, provoque rollback e permita repetir o mesmo cadastro sem violar a unicidade. No reenvio, a mensagem de sucesso só pode ser gravada depois da entrega aceita.

As mensagens ao usuário não devem expor host, credenciais, destinatários adicionais ou texto bruto da exceção. A falha deve continuar observável pelo mecanismo de reporte da aplicação, enquanto a resposta orienta uma nova tentativa. A tela de cadastro já possui um erro junto ao e-mail; a tela de confirmação deve reutilizar o componente `AlertError` e os erros fornecidos pelo `<Form>` do Inertia. Os formulários e links continuam usando as funções tipadas existentes do Wayfinder (`store`, `send` e `logout`), sem URLs literais nem regeneração de rotas.

A assinatura e a autorização do framework permanecem ativas. A política de exceções em `bootstrap/app.php` pode converter `InvalidSignatureException` e `AuthorizationException` em redirecionamento com erro somente quando a rota atual for `verification.verify`; fora dela, o comportamento padrão continua intacto. Uma mensagem genérica comum para assinatura inválida, expiração, hash incompatível e link de outra conta evita revelar a existência ou o endereço de outra conta e conduz à tela autenticada que já oferece reenvio e saída.

## Estratégia

Primeiro, tornar cadastro e reenvio recuperáveis diante de falha real do transporte, completar a apresentação de erro e provar rollback, ausência de sucesso falso, nova tentativa e envio efetivo. Depois, transformar apenas as recusas do link de confirmação em orientação para reenvio, cobrindo assinatura inválida, expiração e outra conta sem enfraquecer os controles nem alterar 403 alheios. Cada fase preserva uma mudança comportamental completa e verificável para commit.

## Baseline

O agregado `composer test` executa Pint, Rector, lint/formatação frontend, PHPStan, TypeScript e cobertura de tipos, mas no Windows falha antes da cobertura de código porque seu script `test:unit` usa a atribuição Bash `XDEBUG_MODE="coverage"`, interpretada pelo `cmd.exe` como um comando inexistente. O gate reproduzível abaixo mantém os mesmos verificadores, seleciona PHP 8.5 localmente para todos os subprocessos e define a variável de cobertura com sintaxe PowerShell. Cada etapa interrompe o gate com seu código de saída e nenhuma aplica correções.

```powershell
$phasePhpDirectory = 'C:\Users\maari\.config\herd\bin\php85'
$env:Path = $phasePhpDirectory + ';' + $env:Path
composer test:lint
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
composer test:types
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
composer test:type-coverage
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
$env:XDEBUG_MODE = 'coverage'
php vendor/bin/pest --parallel --coverage --exactly=100.0
exit $LASTEXITCODE
```

Pré-requisitos observados: PHP 8.5.12 do Herd, Xdebug 3.5.0, Bun 1.4.4, PostgreSQL configurado para testes e dependências já instaladas. O PHP emite um aviso não bloqueante de OPcache compilado para uma API anterior do Zend Engine, e o Rector emite a depreciação conhecida de `withSetProviders()`.

Resultado inicial: passou. Foram executados 198 testes com 769 assertions; cobertura de tipos e cobertura de código ficaram em 100%. Pint, Rector, formatação/lint frontend, PHPStan e TypeScript também passaram. O `composer test` original foi observado separadamente até a falha operacional de shell em `test:unit`; o bloco acima foi então executado integralmente e passou. Nenhum arquivo versionado foi alterado pelo baseline.

| Verificador | Invocação/configuração | Exigência relevante | Resultado observado |
| --- | --- | --- | --- |
| Pint | `composer test:lint` → `pint --parallel --test` | Verificação sem correção | Passou |
| Rector | `composer test:lint` → `rector --dry-run` | PHP 8.5 e verificação sem reescrita | Passou; emitiu aviso de depreciação de `withSetProviders()` |
| Frontend lint/formato | `composer test:lint` → `bun run test:lint` | `vp fmt --check resources/` e `vp lint` | Passou |
| PHPStan | `composer test:types` → `phpstan` | PHP 8.5 e nível máximo de `phpstan.neon` | Passou sem erros |
| TypeScript | `composer test:types` → `bun run test:types` | `tsc --noEmit` | Passou |
| Cobertura de tipos | `composer test:type-coverage` | Mínimo de 100% | Passou com 100% |
| Testes e cobertura de código | `php vendor/bin/pest --parallel --coverage --exactly=100.0` | PostgreSQL, PHP 8.5 e Xdebug em modo `coverage` | Passou: 198 testes, 769 assertions e 100% de cobertura |

## Riscos

- Capturar `Throwable` ou uma exceção HTTP ampla mascararia defeitos e poderia alterar fluxos fora desta filha; limitar a recuperação à falha de transporte e à rota de verificação preserva a política global.
- O evento `Registered` envia a notificação de forma síncrona dentro da transação. Mover o envio para depois do commit, enfileirá-lo ou engolir a exceção criaria conta sem a confirmação entregue e mudaria a semântica de nova tentativa; essas alternativas ficam fora do escopo.
- Um erro de link que revele se o `id` ou o hash pertence a outra conta cria risco de enumeração. Todos os links recusados devem usar orientação genérica, sem confirmar dados da URL.
- A recuperação não pode remover `signed`, `auth`, `throttle` nem as comparações de `EmailVerificationRequest`; os testes precisam afirmar que nenhum usuário indevido é confirmado e que o dashboard continua protegido.
- A página de confirmação distingue sucesso e erro. Um caminho de falha não pode manter `verification-link-sent`, e a interface precisa evitar uma mensagem de sucesso simultânea.
- A suíte exige 100% de cobertura. Cada ramo novo dos controladores precisa de cenário de sucesso e falha; o gate completo continua obrigatório após cada fase.

## Fase 1 — Recuperar falhas de envio no cadastro e no reenvio

### Objetivo

Transformar uma indisponibilidade real do transporte de e-mail em orientação segura de nova tentativa, preservando a atomicidade do cadastro e exibindo sucesso somente quando a notificação for aceita.

### Dependências

Depende do envio síncrono já instalado pelo listener de `Registered`, da transação existente em `CreateUser`, da Action de reenvio e dos componentes Inertia/Wayfinder existentes. Não requer fila, migração ou dependência nova.

### Mudanças esperadas

- Tratar nos endpoints de cadastro e reenvio somente a exceção de transporte do Symfony Mailer, reportando a causa internamente e retornando uma mensagem sanitizada com ação de tentar novamente.
- Manter a exceção do cadastro atravessando `DB::transaction()` antes da resposta recuperável, garantindo rollback do usuário, sessão de convidado e possibilidade de repetir os mesmos dados.
- Manter `verification-link-sent` exclusivo do reenvio concluído; em falha, retornar à tela de confirmação com erro e sem status de sucesso.
- Reutilizar `AlertError` na página de confirmação para renderizar os erros do `<Form>`, mantendo o botão de reenvio, estado de processamento e opção de sair.
- Fortalecer o sucesso do cadastro para provar que a notificação `VerifyEmail` é realmente enviada, além da conta única, autenticação e bloqueio do dashboard já cobertos.
- Simular falha determinística no limite do mailer, sem rede: no cadastro, afirmar mensagem de nova tentativa, nenhuma conta persistida e nenhum login; em seguida, restabelecer o envio e repetir os dados, obtendo uma única conta não confirmada e a notificação. No reenvio, afirmar erro visível, ausência de sucesso falso e, após restabelecimento, notificação e status de sucesso.

### Arquivos prováveis

- `app/Http/Controllers/UserController.php`
- `app/Http/Controllers/UserEmailVerificationNotificationController.php`
- `resources/js/pages/user-email-verification-notification/create.tsx`
- `tests/Feature/Controllers/UserControllerTest.php`
- `tests/Feature/Controllers/UserEmailVerificationNotificationControllerTest.php`

### Limites

Não capturar falhas de validação, banco ou erros arbitrários; não manter uma conta parcialmente cadastrada após falha; não enfileirar, repetir automaticamente ou trocar o transporte. Não alterar senha, throttle, rota, schema, destinatário ou conteúdo do e-mail.

### Estratégia

Preservar as Actions e o listener do framework, tratando o limite de infraestrutura na coordenação HTTP. Nos testes de endpoint, substituir o contrato de mailer no contêiner por uma falha de transporte controlada e depois restaurar uma entrega fake, exercitando os endpoints e o banco reais em vez de testar apenas um `catch` isolado.

### Aceite

- Cadastro válido envia `VerifyEmail`, persiste exatamente uma conta não confirmada, autentica o titular e mantém o dashboard redirecionando para a confirmação.
- Falha de transporte no cadastro retorna à jornada com orientação de nova tentativa, não expõe a exceção, não persiste usuário e não autentica; a repetição posterior bem-sucedida cria uma única conta e envia o link.
- Falha de transporte no reenvio retorna erro orientando nova tentativa, não exibe nem grava o status de sucesso e não envia notificação.
- Restabelecido o transporte, o mesmo usuário consegue reenviar, recebe a notificação e vê a confirmação de envio.
- A tela de confirmação continua permitindo sair e impede submissões duplicadas enquanto processa.

### Verificação focada

Executar com PHP 8.5 `php artisan test --compact tests/Feature/Controllers/UserControllerTest.php tests/Feature/Controllers/UserEmailVerificationNotificationControllerTest.php`. Executar `bun run test:types` e `bun run test:lint` para a página alterada; depois executar o gate completo do baseline.

## Fase 2 — Orientar nova tentativa para links de confirmação recusados

### Objetivo

Levar links inválidos, expirados ou pertencentes a outra conta à tela autenticada de confirmação com uma orientação genérica e caminho de reenvio, sem confirmar nenhum endereço indevido nem enfraquecer assinatura ou autorização.

### Dependências

Depende da tela de confirmação capaz de exibir erros concluída na fase 1, dos middlewares `auth`, `signed` e `throttle`, de `EmailVerificationRequest` e da política central de exceções existente em `bootstrap/app.php`.

### Mudanças esperadas

- Registrar respostas de exceção localizadas para `InvalidSignatureException` e para a recusa de autorização ocorridas na rota `verification.verify`, redirecionando a `verification.notice` com uma mensagem genérica que orienta solicitar outro link.
- Preservar o render padrão das mesmas exceções em qualquer outra rota e manter intactos os middlewares, a verificação de `id`/hash e o `fulfill()` do framework.
- Substituir o teste atual que espera 403 do link sem assinatura pela jornada recuperável e acrescentar casos de assinatura expirada e link válido assinado para outra conta, afirmando que nenhum usuário é confirmado e que a própria conta autenticada pode reenviar.
- Cobrir a entrada por link válido quando o titular ainda não está autenticado: redirecionamento ao login, preservação do destino e confirmação somente depois da autenticação.
- Manter os testes existentes de confirmação válida e reabertura de link válido para conta já confirmada, incluindo acesso ao dashboard, e afirmar que receber ou reenviar a notificação sem abrir um link válido não remove a restrição financeira.

### Arquivos prováveis

- `bootstrap/app.php`
- `tests/Feature/Controllers/UserEmailVerificationTest.php`
- `tests/Feature/Controllers/UserEmailVerificationNotificationControllerTest.php`

### Limites

Não remover ou contornar assinatura, autenticação, autorização ou rate limit; não revelar se a URL pertence a outra conta; não transformar outros 403 da aplicação em redirecionamento; não confirmar automaticamente ao reenviar ou apenas ao receber a notificação.

### Estratégia

Usar os callbacks de renderização documentados do Laravel, condicionados pelo nome da rota, para preservar os controles do framework e alterar somente a experiência após a recusa. Gerar URLs temporárias assinadas nos testes, controlar o tempo para expiração e usar dois usuários distintos para provar isolamento; verificar resposta, sessão, estado persistido e acesso ao dashboard.

### Aceite

- Link inválido ou sem assinatura não confirma e-mail nem libera dashboard e conduz à tela de confirmação com orientação e botão de reenvio.
- Link expirado produz a mesma resposta recuperável e mantém a conta não confirmada.
- Link assinado de outra conta não confirma o usuário autenticado nem o titular do link, não revela qual conta estava na URL e permite solicitar confirmação da própria conta.
- Titular que abre um link válido sem sessão é levado ao login e, depois de autenticado, retorna ao destino, confirma o próprio e-mail e acessa o dashboard.
- Link válido da própria conta confirma uma única vez; reabrir o link ainda válido de uma conta já confirmada mantém a confirmação e permite seguir ao dashboard.
- Reenvio ou recebimento da notificação, sem visita válida ao link, mantém `email_verified_at` nulo e o dashboard protegido.

### Verificação focada

Executar com PHP 8.5 `php artisan test --compact tests/Feature/Controllers/UserEmailVerificationTest.php tests/Feature/Controllers/UserEmailVerificationNotificationControllerTest.php`. Depois executar o gate completo do baseline e revisar que a política de exceções está estritamente condicionada a `verification.verify`.
