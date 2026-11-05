# Planejamento DEV 1015926 — Política de senha no cadastro e na redefinição

## Identidade e fontes

- Filha DEV `#1015926`: `docs/harness/features/1015909-acesso-a-conta/tasks/dev-1015926-acesso-a-conta-politica-de-senha-no-cadastro-e-na-redefinicao/task.md`.
- Requisito pai `#1015909`: `docs/harness/features/1015909-acesso-a-conta/feature.md`, especialmente R3, CA2 e CA8.
- Implementação inspecionada: `app/Providers/AppServiceProvider.php`, `config/essentials.php`, `app/Http/Requests/CreateUserRequest.php`, `app/Http/Requests/CreateUserPasswordRequest.php`, `app/Http/Requests/UpdateUserPasswordRequest.php`, `app/Http/Controllers/UserController.php`, `app/Http/Controllers/UserPasswordController.php`, `app/Actions/CreateUser.php`, `app/Actions/CreateUserPassword.php`, `app/Models/User.php` e `routes/web.php`.
- Dependência que configura a regra atual: `vendor/nunomaduro/essentials/src/Configurables/SetDefaultPassword.php`, versão direta `nunomaduro/essentials 1.2.0`; APIs conferidas para `laravel/framework 13.40.0` e `laravel/fortify 1.41.0`.
- Cobertura existente inspecionada: `tests/Feature/Controllers/UserControllerTest.php`, `tests/Feature/Controllers/UserPasswordControllerTest.php`, `tests/Feature/Controllers/SessionControllerTest.php`, `tests/Unit/Actions/CreateUserTest.php`, `tests/Unit/Actions/CreateUserPasswordTest.php` e `tests/Pest.php`.

## Objetivo

Aplicar a mesma política de senha de 12 a 255 caracteres, com maiúscula, minúscula, número, símbolo, confirmação e rejeição de senha vazada tanto no cadastro quanto na redefinição, independentemente do ambiente, preservando as demais validações, a criação única da conta, o fluxo de confirmação de e-mail e o retorno ao login após uma redefinição válida.

## Estado atual

`CreateUserRequest` e `CreateUserPasswordRequest` já exigem presença, confirmação e `Password::defaults()`. Os controladores também convertem essa regra no atributo HTML `passwordrules`. A configuração efetiva vem de `NunoMaduro\Essentials\Configurables\SetDefaultPassword`: fora dos testes ela define 12–255, letras, caixa mista, número, símbolo e `uncompromised()` somente quando `app()->isProduction()`; nos demais ambientes a regra do framework recua para mínimo de 8, e durante testes o configurable nem é habilitado. Assim, a suíte atual aceita senhas como `password1234` e `new-password`, sem demonstrar R3.

O cadastro valida nome, e-mail e senha antes de `CreateUser`, cria o usuário em transação, dispara `Registered`, autentica a conta ainda não confirmada e a encaminha ao dashboard, cuja rota exige `verified`. A redefinição valida token, e-mail e senha antes de `CreateUserPassword`; o broker troca o hash, renova o remember token, dispara `PasswordReset` e o controlador retorna ao login. O modelo mantém `email_verified_at` separado da senha, portanto a redefinição não confirma a conta.

Os testes existentes cobrem presença e confirmação, parte das validações de nome/e-mail, criação, token de redefinição, troca do hash e redirecionamentos. Faltam os limites 12/255, cada requisito de composição, a resposta para senha vazada nos dois endpoints, os máximos de nome/e-mail, o e-mail inválido na redefinição e uma prova integrada de que a senha nova autentica, a antiga deixa de autenticar e a conta não confirmada continua barrada pela rota financeira.

## Escopo

Entra a propriedade da configuração padrão de senha pela aplicação, sua aplicação uniforme no cadastro e na redefinição, a preservação dos consumidores existentes e testes comportamentais dos critérios desta filha.

Não entram novas telas, alteração visual, dados financeiros no cadastro, gestão de perfil, autenticação social, passkeys, dois fatores, recuperação/expiração de token além do necessário para exercitar a redefinição válida, nem mudança de dependências.

## Arquitetura

A aplicação já centraliza a política em `Illuminate\Validation\Rules\Password::defaults()` e a reutiliza nos Form Requests e nas props `passwordRules`; a mudança deve conservar esse ponto único em vez de duplicar cadeias de regras. `AppServiceProvider`, carregado depois do provider descoberto do Essentials na lista de serviços, deve registrar explicitamente a política aprovada para todos os ambientes, enquanto `config/essentials.php` desabilita `SetDefaultPassword` para que a aplicação, e não um default condicional de pacote, seja a fonte inequívoca da regra.

Há um terceiro consumidor compartilhado: `UpdateUserPasswordRequest` e a página de alteração de senha também usam `Password::defaults()`. A política forte já é o comportamento de produção desse consumidor por causa do Essentials; torná-la uniforme preserva produção e apenas alinha desenvolvimento e testes. A cobertura existente de atualização deve usar uma senha conforme a política para continuar provando o fluxo, sem ampliar a filha com uma nova matriz de gestão de perfil.

`uncompromised()` usa o contrato `Illuminate\Contracts\Validation\UncompromisedVerifier`, cuja implementação instalada consulta a API Pwned Passwords por prefixo de hash. Os testes devem substituir esse contrato no contêiner por respostas determinísticas de senha segura ou vazada, sem tráfego de rede. A implementação instalada reporta exceções e trata resposta ausente ou malsucedida como coleção vazia, portanto indisponibilidade externa mantém comportamento fail-open; o requisito não autoriza alterar essa semântica nesta filha.

## Estratégia

Primeiro, assumir a configuração padrão no provider da aplicação com a cadeia exata aprovada e desligar somente o configurable concorrente do Essentials. Em seguida, atualizar os dados válidos dos testes afetados e acrescentar datasets de fronteira/composição nos dois endpoints, isolando o verificador externo pelo contrato. Por fim, completar a prova integrada da redefinição e as preservações de nome/e-mail e conta não confirmada. Uma única fase mantém configuração e regressão comportamental no mesmo commit verificável.

## Baseline

Comando agregado do projeto: `composer test`. Para reproduzi-lo neste Windows com o PHP 8.5 isolado, os verificadores foram observados com `PATH=/c/Users/maari/.config/herd/bin/php85:$PATH` e o Composer PHAR do Herd. O comando agregado é somente de verificação: Pint usa `--test`, Rector usa `--dry-run`, o frontend usa `fmt --check`/lint sem `--fix`, e os demais passos são análises ou testes.

Resultado inicial: interrompido antes dos testes Pest com cobertura. Pint, Rector, formatação/lint frontend, PHPStan, TypeScript e type coverage passaram. O script `test:unit` não iniciou porque `XDEBUG_MODE="coverage" pest ...` foi interpretado por `cmd.exe` e `XDEBUG_MODE` não é um comando válido no Windows. Além disso, o PHP 8.5.12 isolado disponível possui PostgreSQL, mas não possui PCOV nem Xdebug; o PHP 8.4 global possui cobertura, porém é incompatível com o requisito `php ^8.5.0`. Nenhum arquivo versionado foi alterado pelo baseline.

Pré-requisito operacional pendente: disponibilizar ao executor um PHP 8.5 com PCOV ou Xdebug e uma invocação do gate compatível com o shell, preservando todos os verificadores e a exigência de cobertura exata de 100%. Até isso ser resolvido, o plano não está apto a ser encaminhado ao Ralph e não há bloco de comando executável seguro para o parser.

| Verificador | Invocação/configuração | Exigência relevante | Resultado observado |
| --- | --- | --- | --- |
| Pint | `pint --parallel --test` | Verificação, sem correção | Passou |
| Rector | `rector --dry-run` | Verificação, sem reescrita | Passou; emitiu aviso de depreciação de `withSetProviders()` |
| Frontend lint/formato | `bun run test:lint` | `vp fmt --check resources/` e `vp lint` | Passou |
| PHPStan | `phpstan` | Nível máximo conforme `phpstan.neon` | Passou sem erros |
| TypeScript | `bun run test:types` | `tsc --noEmit` | Passou |
| Cobertura de tipos | `pest --type-coverage --min=100` | 100% | Passou |
| Testes e cobertura de código | `XDEBUG_MODE="coverage" pest --parallel --coverage --exactly=100.0` | PHP 8.5, PostgreSQL e driver de cobertura | Não executado: sintaxe de variável incompatível com `cmd.exe`; PHP 8.5 local também sem driver de cobertura |

## Riscos

- Uma configuração global mal posicionada pode ser sobrescrita pelo Essentials ou divergir entre ambientes; desabilitar o configurable específico e registrar a regra no provider da aplicação elimina a disputa.
- Senhas vazadas dependem de serviço externo em produção. A implementação instalada é fail-open em falha/indisponibilidade; mudar para fail-closed alteraria disponibilidade e não está autorizado.
- O mock do verificador deve ser limitado aos casos que chegam a `uncompromised()`, mantendo os testes de composição independentes da rede e sem mascarar chamadas inesperadas.
- A regra compartilhada alcança alteração de senha do perfil. Esse alcance já existe em produção; fixtures válidas desse fluxo precisam ser alinhadas sem converter esta filha em expansão funcional de perfil.
- A suíte exige 100% de cobertura. Novas linhas no provider e novos ramos de teste devem permanecer exercitados, e o gate completo continua obrigatório apesar do baseline local impedido.

## Fase 1 — Uniformizar a política e comprovar os dois fluxos

### Objetivo

Remover a diferença entre produção, desenvolvimento e testes para a política aprovada e demonstrar, pelos endpoints reais, que cadastro e redefinição aceitam apenas senhas válidas e preservam seus efeitos de negócio.

### Dependências

Requer apenas as versões já instaladas de Laravel, Essentials, Fortify e Pest. A execução do gate completo depende da preparação de PHP 8.5 com cobertura descrita no baseline.

### Mudanças esperadas

- Desabilitar apenas `NunoMaduro\Essentials\Configurables\SetDefaultPassword` em `config/essentials.php` e registrar em `AppServiceProvider` um `Password::defaults()` invariável com mínimo 12, máximo 255, letras, caixa mista, números, símbolos e `uncompromised()`.
- Manter os Form Requests, controladores e páginas consumindo a regra central existente, inclusive o atributo `passwordrules`, sem duplicar a cadeia nem criar validação apenas no frontend.
- Atualizar senhas de sucesso nos testes atingidos, inclusive a preservação do fluxo existente de alteração de senha, para entradas conformes à política de produção.
- Acrescentar datasets de cadastro e redefinição para menos de 12, mais de 255, ausência de maiúscula, minúscula, número ou símbolo; em cada falha, afirmar erro no campo e ausência da criação/troca de senha.
- Simular pelo contrato do verificador uma senha segura e uma senha vazada, comprovando aceitação e rejeição nos dois endpoints sem requisição externa.
- Completar as preservações do cadastro para nome/e-mail acima de 255, além dos casos já existentes de obrigatoriedade, formato e unicidade; acrescentar o e-mail inválido na redefinição.
- Fortalecer o cenário válido de cadastro para uma única conta e evento de registro, sem campos financeiros, mantendo a conta sujeita à confirmação.
- Fortalecer a redefinição válida com conta não confirmada: retorno ao login, novo hash aceito no login, senha anterior recusada, `email_verified_at` ainda nulo e dashboard redirecionando para a confirmação.

### Arquivos prováveis

- `app/Providers/AppServiceProvider.php`
- `config/essentials.php`
- `tests/Feature/Controllers/UserControllerTest.php`
- `tests/Feature/Controllers/UserPasswordControllerTest.php`

### Limites

Não alterar as Actions de persistência, modelo, schema, rotas, telas, dependências, mensagens de produto ou semântica de indisponibilidade do serviço de vazamentos. Não adicionar política própria a passkeys, dois fatores ou perfil além de manter o consumidor compartilhado funcionando como já funciona em produção.

### Estratégia

Usar a regra nativa documentada do Laravel como fonte única. Nos testes Pest, substituir `UncompromisedVerifier` no contêiner somente dentro de cada cenário que precisa de resposta segura/vazada; usar datasets nomeados para as fronteiras e composições, e assertions HTTP/banco/hash/autenticação para os efeitos observáveis.

### Aceite

- Cadastro e redefinição aceitam uma senha entre 12 e 255 caracteres com todos os grupos exigidos, confirmação igual e resposta não vazada.
- Cada limite inválido, cada grupo ausente, confirmação ausente/diferente e resposta vazada produz erro em `password` e não cria conta nem troca o hash.
- Nome/e-mail inválidos ou longos e e-mail duplicado continuam bloqueando cadastro; e-mail ausente ou inválido continua bloqueando redefinição.
- Cadastro válido persiste exatamente uma conta, dispara o fluxo de registro e continua sujeito à confirmação, sem dado financeiro.
- Redefinição válida retorna ao login; a senha nova autentica, a antiga não, e uma conta não confirmada permanece sem acesso ao dashboard financeiro.
- O fluxo existente de alteração de senha continua passando com uma entrada compatível, sem mudança de comportamento de produção.

### Verificação focada

Executar `php artisan test --compact tests/Feature/Controllers/UserControllerTest.php tests/Feature/Controllers/UserPasswordControllerTest.php` com PHP 8.5 e o verificador externo isolado pelos próprios testes. Depois executar o gate completo definido no baseline quando o driver de cobertura e a invocação compatível estiverem disponíveis; revisar qualquer correção automática apenas se uma ferramenta de desenvolvimento for usada fora do gate de verificação.
