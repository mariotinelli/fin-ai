# Fatiamento de [WEB] [USUARIO] Acesso à conta pessoal

Revisão: 2  
Hash: `4a49a9cc65ee865a263909eb45154673ec3ef5327efe8a0defc20860bf47de3c`

## Prévia numerada

1. **[DEV] [WEB] [USUARIO] Acesso à conta pessoal - Cadastro e redefinição com política de senha consistente** — 1.5h
   - Entrega: Completar a validação de senha no cadastro público e na redefinição esquecida, aplicando a mesma regra forte em teste e uso. Os formulários e demais validações já existem; falta a consistência exigida pelo requisito.
   - Bloqueado por: Nenhum
   - Bloqueios externos: slice Redmine 1016117 ([QA] [WEB] [USUARIO] Adequação visual do FinAI): Base visual das telas atuais implementada e verificada no aceite integrado da Feature visual - O catálogo e o requisito exigem a base visual antes da implementação de negócio. A QA #1016117 verifica os cinco DEV fornecedores; o início aguarda essa capacidade de fato concluída, e não sua mera publicação em New.
2. **[DEV] [WEB] [USUARIO] Acesso à conta pessoal - Confirmação de e-mail com acesso restrito e retomada** — 2h
   - Entrega: Completar a confirmação de e-mail, do envio inicial à retomada, e impedir que contas não confirmadas acessem perfil e demais funcionalidades. Confirmação própria e reenvio já existem; faltam restrição integral e orientação nas falhas de link/envio.
   - Bloqueado por: Nenhum
   - Bloqueios externos: slice Redmine 1016117 ([QA] [WEB] [USUARIO] Adequação visual do FinAI): Base visual das telas atuais implementada e verificada no aceite integrado da Feature visual - O catálogo e o requisito exigem a base visual antes da implementação de negócio. A QA #1016117 verifica os cinco DEV fornecedores; o início aguarda essa capacidade de fato concluída, e não sua mera publicação em New.
3. **[DEV] [WEB] [USUARIO] Acesso à conta pessoal - Recuperação de senha com nova tentativa** — 2h
   - Entrega: Completar os estados de recuperação quando o envio falhar ou o link de redefinição for inválido, expirado ou já usado. O pedido genérico e o broker já existem; falta retomada sem apresentar envio ou alteração como concluídos indevidamente.
   - Bloqueado por: Nenhum
   - Bloqueios externos: slice Redmine 1016117 ([QA] [WEB] [USUARIO] Adequação visual do FinAI): Base visual das telas atuais implementada e verificada no aceite integrado da Feature visual - O catálogo e o requisito exigem a base visual antes da implementação de negócio. A QA #1016117 verifica os cinco DEV fornecedores; o início aguarda essa capacidade de fato concluída, e não sua mera publicação em New.

## Cobertura

| Regra ou critério | Destino | Evidência |
| --- | --- | --- |
| R1: Cadastro aberto, sem convite ou liberação administrativa. Contas são individuais; nenhum dado financeiro é solicitado nesta jornada. | Existente | CreateUserRequest/CreateUser: cadastro público com dados de conta, sem campos financeiros; preservar e verificar sua integração. |
| R2: Nome e e-mail são obrigatórios, com até 255 caracteres cada; e-mail válido e único por conta. Senha e confirmação são obrigatórias e devem coincidir. Na recuperação e redefinição, o e-mail informado deve ser válido; na redefinição, nova senha e confirmação também são obrigatórias. | Existente | Requests já impõem obrigatoriedade, limites de 255, formato/unicidade e confirmação onde aplicáveis; política forte é adaptação de R3. |
| R3: Cadastro e redefinição exigem senha de 12 a 255 caracteres, com ao menos uma maiúscula, uma minúscula, um número e um símbolo, rejeitando senhas conhecidas em vazamentos. A mesma regra vale nos ambientes de teste e uso. | Slice 1 | app/Http/Requests/CreateUserRequest.php; CreateUserPasswordRequest.php; resources/js/pages/user/create.tsx; user-password/create.tsx. Adaptação parcial identificada. CA11 é também desdobrada em confirmação/recuperação para explicitar a responsabilidade de cada jornada. |
| R4: Acesso à área do sistema exige autenticação e confirmação do próprio e-mail, incluindo acesso direto às páginas protegidas. Conta não confirmada pode concluir a jornada restrita de confirmação, reenvio, recuperação e saída; não acessa as funcionalidades do produto. Receber um e-mail ou redefinir a senha não equivale a confirmar o endereço. | Slice 2 | routes/web.php; app/Models/User.php. Adaptação parcial identificada. CA11 é também desdobrada em confirmação/recuperação para explicitar a responsabilidade de cada jornada. |
| R5: O link de recuperação é válido por 60 minutos a partir da emissão e não pode ser reutilizado após sucesso. A senha anterior deixa de permitir novos logins depois da redefinição. | Existente | config/auth expire60; gerenciador converte minutos; broker exclui token após sucesso; Action altera senha sem confirmar e-mail. |
| R6: Após cinco falhas consecutivas de login para o mesmo e-mail e origem, bloquear temporariamente as novas tentativas e informar a espera, preservando o comportamento atual. Após o prazo, permitir nova tentativa. | Existente | CreateSessionRequest verifica cinco falhas por e-mail/origem, informa espera e limpa limitação; testes específicos foram apenas lidos. |
| R7: Preservar a opção existente de lembrar acesso. Ela não dispensa confirmação do e-mail nem impede a saída explícita; sair encerra a sessão atual e exige novo login para voltar à área protegida. | Existente | SessionController preserva remember e destrói sessão; SessionGuard::logout limpa sessão/recaller e renova remember token. Caminho lido sem executar testes. |
| R8: Falha de envio ou de link não deve ser apresentada como confirmação ou recuperação concluída. As alternativas de reenvio e novo pedido devem permitir retomar sem duplicar contas nem alterar senhas indevidamente. | Slice 2 | routes/web.php; app/Models/User.php. Adaptação parcial identificada. CA11 é também desdobrada em confirmação/recuperação para explicitar a responsabilidade de cada jornada. |
| R9: As telas de acesso usam a base visual FinAI da Feature de adequação visual, com tipografia, paleta, campos, botões, erros e estados coerentes, adaptação para celular, tablet e computador e manutenção dos temas claro, escuro e acompanhar o sistema. Esta Feature não redefine a identidade visual. | Outra Feature | Feature visual #1016101, composição de acesso #1016114 e aceite integrado #1016117, ainda New. Os estados novos dos DEV consomem essa base sem reconstruí-la. |
| CA1: Como visitante, cadastrar nome e e-mail válidos e disponíveis, senha conforme R3 e confirmação igual; criar uma única conta, enviar o link e orientar a confirmação, sem pedir dados financeiros ou liberar a área do produto antes de confirmar. | Slice 2 | routes/web.php; app/Models/User.php. Adaptação parcial identificada. CA11 é também desdobrada em confirmação/recuperação para explicitar a responsabilidade de cada jornada. |
| CA2: No cadastro e na redefinição, quando aplicável, omitir campos obrigatórios, exceder os limites de nome/e-mail, informar e-mail inválido ou duplicado, senha fora de qualquer condição de R3 ou confirmação diferente; impedir a operação e indicar os respectivos erros sem criar contas ou alterar senhas indevidamente. | Slice 1 | app/Http/Requests/CreateUserRequest.php; CreateUserPasswordRequest.php; resources/js/pages/user/create.tsx; user-password/create.tsx. Adaptação parcial identificada. CA11 é também desdobrada em confirmação/recuperação para explicitar a responsabilidade de cada jornada. |
| CA3: Com conta não confirmada, tentar a área inicial, perfil, configurações e destinos financeiros protegidos quando entregues; manter o acesso restrito à jornada de confirmação, reenvio, recuperação e saída, inclusive com lembrar acesso selecionado. | Slice 2 | routes/web.php; app/Models/User.php. Adaptação parcial identificada. CA11 é também desdobrada em confirmação/recuperação para explicitar a responsabilidade de cada jornada. |
| CA4: Como titular autenticado, abrir link válido da própria conta; confirmar o e-mail e permitir seguir à área inicial. Se iniciar sem sessão, solicitar autenticação quando necessária antes de concluir a confirmação. | Slice 2 | routes/web.php; app/Models/User.php. Adaptação parcial identificada. CA11 é também desdobrada em confirmação/recuperação para explicitar a responsabilidade de cada jornada. |
| CA5: Abrir link de confirmação inválido, expirado ou de outra conta; não confirmar endereço indevido nem liberar acesso e apresentar caminho para solicitar novo link próprio. Reabrir link ainda válido de conta já confirmada mantém a confirmação. | Slice 2 | routes/web.php; app/Models/User.php. Adaptação parcial identificada. CA11 é também desdobrada em confirmação/recuperação para explicitar a responsabilidade de cada jornada. |
| CA6: Entrar com credenciais corretas de conta confirmada; acessar a área inicial ou destino protegido solicitado. Credenciais incorretas não autenticam. Depois de cinco falhas consecutivas, a nova tentativa durante bloqueio informa espera; após o prazo, permitir nova tentativa válida. | Existente | Credenciais, destino solicitado e limitação possuem caminhos e testes específicos; não reconstruir a capacidade. |
| CA7: Entrar e sair, com lembrar acesso marcado e desmarcado; retornar à página pública e exigir login ao tentar reabrir a área protegida. | Existente | Saída retorna à página pública, invalida sessão e descarta lembrança conforme o guard; manter e verificar em QA. |
| CA8: Solicitar recuperação para e-mail cadastrado e inexistente, com envio disponível; apresentar a mesma resposta genérica. O titular cadastrado recebe o link, sem revelar a existência da conta ao solicitante pela resposta. | Existente | Pedido com envio disponível retorna mensagem genérica e usa o broker; falha de transporte é a adaptação específica de CA11-Recuperacao. |
| CA9: Com link de recuperação próprio, não usado e antes de 60 minutos, definir senha conforme R3 e confirmação igual; retornar ao login, permitir novos logins com a senha nova e recusar a anterior. Uma conta anteriormente não confirmada continua sem acesso ao sistema. | Slice 1 | app/Http/Requests/CreateUserRequest.php; CreateUserPasswordRequest.php; resources/js/pages/user/create.tsx; user-password/create.tsx. Adaptação parcial identificada. CA11 é também desdobrada em confirmação/recuperação para explicitar a responsabilidade de cada jornada. |
| CA10: Tentar redefinir com link inválido, após sua expiração ou já utilizado; não alterar a senha e oferecer novo pedido. Um novo link válido permite retomar a jornada. | Slice 3 | app/Http/Controllers/UserEmailResetNotificationController.php; app/Actions/CreateUserEmailResetNotification.php; tests/Feature/Controllers/UserEmailResetNotificationTest.php. Adaptação parcial identificada. CA11 é também desdobrada em confirmação/recuperação para explicitar a responsabilidade de cada jornada. |
| CA11: Provocar falha de envio na confirmação inicial, no reenvio e na recuperação; informar falha e nova tentativa sem sucesso fictício. Após restabelecer o envio, permitir retomar com link utilizável sem contas duplicadas e sem revelar explicitamente a existência de conta na recuperação. | Slice 2 | routes/web.php; app/Models/User.php. Adaptação parcial identificada. CA11 é também desdobrada em confirmação/recuperação para explicitar a responsabilidade de cada jornada. |
| CA12: Utilizar as telas e estados de acesso em computador, tablet e celular, nos temas claro, escuro e acompanhar o sistema; manter a linguagem visual FinAI definida pela adequação visual, controles utilizáveis e erros reconhecíveis. | Slice 2 | routes/web.php; app/Models/User.php. Adaptação parcial identificada. CA11 é também desdobrada em confirmação/recuperação para explicitar a responsabilidade de cada jornada. |
| CA11-Confirmacao: Desdobramento de CA11/R8: falhas de envio inicial e reenvio de confirmação, retomada e unicidade da conta. | Slice 2 | routes/web.php; app/Models/User.php. Adaptação parcial identificada. CA11 é também desdobrada em confirmação/recuperação para explicitar a responsabilidade de cada jornada. |
| CA11-Recuperacao: Desdobramento de CA11/R8: falha e retomada do envio de recuperação, sem falso sucesso ou revelação da conta. | Slice 3 | app/Http/Controllers/UserEmailResetNotificationController.php; app/Actions/CreateUserEmailResetNotification.php; tests/Feature/Controllers/UserEmailResetNotificationTest.php. Adaptação parcial identificada. CA11 é também desdobrada em confirmação/recuperação para explicitar a responsabilidade de cada jornada. |

Formato das condições: Markdown e DOCX.

## Condições de teste

Estas condições integram a aprovação da decomposição. A validação estrutural não substitui a revisão semântica do tech lead.

### Contexto

Visitante e contas confirmadas/não confirmadas; links próprios, de outra conta, inválidos, expirados e usados; controle de tempo e falhas de envio reproduzíveis. Preparar fronteiras de campos/senha e dependência controlável para senha vazada. Consumir a base visual implementada e verificada nos cenários de computador, tablet, celular e claro/escuro/sistema. Os testes existentes foram apenas lidos; registrar evidência ou impedimento de cada condição executada posteriormente.

### Cadastro

#### CT-001 — Cadastro público e confirmação

Verificação: Cadastrar nome/e-mail válidos, senha conforme R3 e confirmação igual.

Resultado esperado: Uma conta, sem convite/dados financeiros; enviar link e orientar confirmar, sem acesso ao produto.

Origem no requisito: R1: Cadastro aberto, sem convite ou liberação administrativa. Contas são individuais; nenhum dado financeiro é solicitado nesta jornada.; R2: Nome e e-mail são obrigatórios, com até 255 caracteres cada; e-mail válido e único por conta. Senha e confirmação são obrigatórias e devem coincidir. Na recuperação e redefinição, o e-mail informado deve ser válido; na redefinição, nova senha e confirmação também são obrigatórias.; CA1: Como visitante, cadastrar nome e e-mail válidos e disponíveis, senha conforme R3 e confirmação igual; criar uma única conta, enviar o link e orientar a confirmação, sem pedir dados financeiros ou liberar a área do produto antes de confirmar.

#### CT-002 — Campos obrigatórios

Verificação: Omitir separadamente nome/e-mail/senha/confirmação no cadastro e os campos aplicáveis na redefinição.

Resultado esperado: Impedir conclusão com erro; sem conta ou senha alterada indevidamente.

Origem no requisito: R2: Nome e e-mail são obrigatórios, com até 255 caracteres cada; e-mail válido e único por conta. Senha e confirmação são obrigatórias e devem coincidir. Na recuperação e redefinição, o e-mail informado deve ser válido; na redefinição, nova senha e confirmação também são obrigatórias.; CA2: No cadastro e na redefinição, quando aplicável, omitir campos obrigatórios, exceder os limites de nome/e-mail, informar e-mail inválido ou duplicado, senha fora de qualquer condição de R3 ou confirmação diferente; impedir a operação e indicar os respectivos erros sem criar contas ou alterar senhas indevidamente.

#### CT-003 — Nome e e-mail nos limites

Verificação: Usar entradas válidas de255 e256caracteres; e-mail inválido e duplicado.

Resultado esperado: Até255aceito; excesso/formato/duplicação recusados, sem nova conta indevida.

Origem no requisito: R2: Nome e e-mail são obrigatórios, com até 255 caracteres cada; e-mail válido e único por conta. Senha e confirmação são obrigatórias e devem coincidir. Na recuperação e redefinição, o e-mail informado deve ser válido; na redefinição, nova senha e confirmação também são obrigatórias.; CA2: No cadastro e na redefinição, quando aplicável, omitir campos obrigatórios, exceder os limites de nome/e-mail, informar e-mail inválido ou duplicado, senha fora de qualquer condição de R3 ou confirmação diferente; impedir a operação e indicar os respectivos erros sem criar contas ou alterar senhas indevidamente.

#### CT-004 — Senha nos limites

Verificação: Nos dois fluxos usar senhas de composição completa não-vazadas com11,12,255 e256caracteres.

Resultado esperado: 12/255aceitas;11/256recusadas com erro; mesma regra em teste e uso.

Origem no requisito: R3: Cadastro e redefinição exigem senha de 12 a 255 caracteres, com ao menos uma maiúscula, uma minúscula, um número e um símbolo, rejeitando senhas conhecidas em vazamentos. A mesma regra vale nos ambientes de teste e uso.; CA2: No cadastro e na redefinição, quando aplicável, omitir campos obrigatórios, exceder os limites de nome/e-mail, informar e-mail inválido ou duplicado, senha fora de qualquer condição de R3 ou confirmação diferente; impedir a operação e indicar os respectivos erros sem criar contas ou alterar senhas indevidamente.

#### CT-005 — Composição da senha

Verificação: Nos dois fluxos omitir separadamente maiúscula, minúscula, número e símbolo, mantendo demais condições.

Resultado esperado: Cada falta recusada; composição completa não rejeitada por esse motivo.

Origem no requisito: R3: Cadastro e redefinição exigem senha de 12 a 255 caracteres, com ao menos uma maiúscula, uma minúscula, um número e um símbolo, rejeitando senhas conhecidas em vazamentos. A mesma regra vale nos ambientes de teste e uso.; CA2: No cadastro e na redefinição, quando aplicável, omitir campos obrigatórios, exceder os limites de nome/e-mail, informar e-mail inválido ou duplicado, senha fora de qualquer condição de R3 ou confirmação diferente; impedir a operação e indicar os respectivos erros sem criar contas ou alterar senhas indevidamente.

#### CT-006 — Senha conhecida em vazamentos

Verificação: Com dado controlado da verificação de senha vazada, tentar os dois fluxos com tamanho/composição válidos.

Resultado esperado: Recusar ambos com erro e sem persistência indevida.

Origem no requisito: R3: Cadastro e redefinição exigem senha de 12 a 255 caracteres, com ao menos uma maiúscula, uma minúscula, um número e um símbolo, rejeitando senhas conhecidas em vazamentos. A mesma regra vale nos ambientes de teste e uso.; CA2: No cadastro e na redefinição, quando aplicável, omitir campos obrigatórios, exceder os limites de nome/e-mail, informar e-mail inválido ou duplicado, senha fora de qualquer condição de R3 ou confirmação diferente; impedir a operação e indicar os respectivos erros sem criar contas ou alterar senhas indevidamente.

#### CT-007 — Confirmação diferente

Verificação: Informar senha válida com confirmação diferente no cadastro e redefinição.

Resultado esperado: Impedir e indicar erro sem criar conta ou alterar senha.

Origem no requisito: R2: Nome e e-mail são obrigatórios, com até 255 caracteres cada; e-mail válido e único por conta. Senha e confirmação são obrigatórias e devem coincidir. Na recuperação e redefinição, o e-mail informado deve ser válido; na redefinição, nova senha e confirmação também são obrigatórias.; CA2: No cadastro e na redefinição, quando aplicável, omitir campos obrigatórios, exceder os limites de nome/e-mail, informar e-mail inválido ou duplicado, senha fora de qualquer condição de R3 ou confirmação diferente; impedir a operação e indicar os respectivos erros sem criar contas ou alterar senhas indevidamente.

### Confirmação

#### CT-008 — Visitante na área protegida

Verificação: Sem sessão, abrir área inicial, perfil e configurações protegidas.

Resultado esperado: Exigir login sem mostrar funcionalidades do produto.

Origem no requisito: R4: Acesso à área do sistema exige autenticação e confirmação do próprio e-mail, incluindo acesso direto às páginas protegidas. Conta não confirmada pode concluir a jornada restrita de confirmação, reenvio, recuperação e saída; não acessa as funcionalidades do produto. Receber um e-mail ou redefinir a senha não equivale a confirmar o endereço.; CA3: Com conta não confirmada, tentar a área inicial, perfil, configurações e destinos financeiros protegidos quando entregues; manter o acesso restrito à jornada de confirmação, reenvio, recuperação e saída, inclusive com lembrar acesso selecionado.

#### CT-009 — Conta não confirmada

Verificação: Entrar sem confirmar e tentar área inicial, perfil GET/PATCH e configurações; repetir com lembrar.

Resultado esperado: Manter restrição, orientação, reenvio e saída; sem acesso/alteração indevida no produto.

Origem no requisito: R4: Acesso à área do sistema exige autenticação e confirmação do próprio e-mail, incluindo acesso direto às páginas protegidas. Conta não confirmada pode concluir a jornada restrita de confirmação, reenvio, recuperação e saída; não acessa as funcionalidades do produto. Receber um e-mail ou redefinir a senha não equivale a confirmar o endereço.; CA3: Com conta não confirmada, tentar a área inicial, perfil, configurações e destinos financeiros protegidos quando entregues; manter o acesso restrito à jornada de confirmação, reenvio, recuperação e saída, inclusive com lembrar acesso selecionado.

#### CT-010 — Recuperar antes de confirmar

Verificação: Como não-confirmado autenticado, sair e seguir ao pedido público existente.

Resultado esperado: Permitir a jornada sem liberar produto ou dispensar confirmação.

Origem no requisito: R4: Acesso à área do sistema exige autenticação e confirmação do próprio e-mail, incluindo acesso direto às páginas protegidas. Conta não confirmada pode concluir a jornada restrita de confirmação, reenvio, recuperação e saída; não acessa as funcionalidades do produto. Receber um e-mail ou redefinir a senha não equivale a confirmar o endereço.; CA3: Com conta não confirmada, tentar a área inicial, perfil, configurações e destinos financeiros protegidos quando entregues; manter o acesso restrito à jornada de confirmação, reenvio, recuperação e saída, inclusive com lembrar acesso selecionado.; CA9: Com link de recuperação próprio, não usado e antes de 60 minutos, definir senha conforme R3 e confirmação igual; retornar ao login, permitir novos logins com a senha nova e recusar a anterior. Uma conta anteriormente não confirmada continua sem acesso ao sistema.

#### CT-011 — Confirmar link próprio

Verificação: Abrir link próprio válido iniciando com e sem sessão.

Resultado esperado: Autenticar quando necessário, confirmar titular e liberar área inicial.

Origem no requisito: R4: Acesso à área do sistema exige autenticação e confirmação do próprio e-mail, incluindo acesso direto às páginas protegidas. Conta não confirmada pode concluir a jornada restrita de confirmação, reenvio, recuperação e saída; não acessa as funcionalidades do produto. Receber um e-mail ou redefinir a senha não equivale a confirmar o endereço.; CA4: Como titular autenticado, abrir link válido da própria conta; confirmar o e-mail e permitir seguir à área inicial. Se iniciar sem sessão, solicitar autenticação quando necessária antes de concluir a confirmação.

#### CT-012 — Confirmação inválida

Verificação: Alterar dados/assinatura do link e abrir como titular não confirmado.

Resultado esperado: Não confirmar nem liberar; orientar novo link próprio.

Origem no requisito: R4: Acesso à área do sistema exige autenticação e confirmação do próprio e-mail, incluindo acesso direto às páginas protegidas. Conta não confirmada pode concluir a jornada restrita de confirmação, reenvio, recuperação e saída; não acessa as funcionalidades do produto. Receber um e-mail ou redefinir a senha não equivale a confirmar o endereço.; R8: Falha de envio ou de link não deve ser apresentada como confirmação ou recuperação concluída. As alternativas de reenvio e novo pedido devem permitir retomar sem duplicar contas nem alterar senhas indevidamente.; CA5: Abrir link de confirmação inválido, expirado ou de outra conta; não confirmar endereço indevido nem liberar acesso e apresentar caminho para solicitar novo link próprio. Reabrir link ainda válido de conta já confirmada mantém a confirmação.

#### CT-013 — Confirmação expirada

Verificação: Abrir link após sua validade.

Resultado esperado: Não confirmar/liberar; orientar e oferecer novo pedido.

Origem no requisito: R4: Acesso à área do sistema exige autenticação e confirmação do próprio e-mail, incluindo acesso direto às páginas protegidas. Conta não confirmada pode concluir a jornada restrita de confirmação, reenvio, recuperação e saída; não acessa as funcionalidades do produto. Receber um e-mail ou redefinir a senha não equivale a confirmar o endereço.; R8: Falha de envio ou de link não deve ser apresentada como confirmação ou recuperação concluída. As alternativas de reenvio e novo pedido devem permitir retomar sem duplicar contas nem alterar senhas indevidamente.; CA5: Abrir link de confirmação inválido, expirado ou de outra conta; não confirmar endereço indevido nem liberar acesso e apresentar caminho para solicitar novo link próprio. Reabrir link ainda válido de conta já confirmada mantém a confirmação.

#### CT-014 — Confirmação de outra conta

Verificação: Como A não confirmado, abrir link válido de B.

Resultado esperado: Não confirmar A/B indevidamente; caminho de novo pedido próprio de A.

Origem no requisito: R4: Acesso à área do sistema exige autenticação e confirmação do próprio e-mail, incluindo acesso direto às páginas protegidas. Conta não confirmada pode concluir a jornada restrita de confirmação, reenvio, recuperação e saída; não acessa as funcionalidades do produto. Receber um e-mail ou redefinir a senha não equivale a confirmar o endereço.; CA5: Abrir link de confirmação inválido, expirado ou de outra conta; não confirmar endereço indevido nem liberar acesso e apresentar caminho para solicitar novo link próprio. Reabrir link ainda válido de conta já confirmada mantém a confirmação.

#### CT-015 — Reabrir confirmação

Verificação: Confirmar conta e reabrir o mesmo link ainda válido.

Resultado esperado: Manter confirmação e permitir área inicial.

Origem no requisito: R4: Acesso à área do sistema exige autenticação e confirmação do próprio e-mail, incluindo acesso direto às páginas protegidas. Conta não confirmada pode concluir a jornada restrita de confirmação, reenvio, recuperação e saída; não acessa as funcionalidades do produto. Receber um e-mail ou redefinir a senha não equivale a confirmar o endereço.; CA5: Abrir link de confirmação inválido, expirado ou de outra conta; não confirmar endereço indevido nem liberar acesso e apresentar caminho para solicitar novo link próprio. Reabrir link ainda válido de conta já confirmada mantém a confirmação.

#### CT-016 — Falha de envio inicial

Verificação: Provocar falha no cadastro, restaurar envio e repetir conforme orientação.

Resultado esperado: Informar falha/retomada sem falso sucesso, duplicação ou titular sem caminho de confirmação/recuperação.

Origem no requisito: R8: Falha de envio ou de link não deve ser apresentada como confirmação ou recuperação concluída. As alternativas de reenvio e novo pedido devem permitir retomar sem duplicar contas nem alterar senhas indevidamente.; CA11: Provocar falha de envio na confirmação inicial, no reenvio e na recuperação; informar falha e nova tentativa sem sucesso fictício. Após restabelecer o envio, permitir retomar com link utilizável sem contas duplicadas e sem revelar explicitamente a existência de conta na recuperação.; CA11-Confirmacao: Desdobramento de CA11/R8: falhas de envio inicial e reenvio de confirmação, retomada e unicidade da conta.

#### CT-017 — Falha no reenvio

Verificação: Como não-confirmado, provocar falha de reenvio, restaurar e tentar de novo.

Resultado esperado: Não alegar envio concluído; após retomada, receber link e confirmar.

Origem no requisito: R8: Falha de envio ou de link não deve ser apresentada como confirmação ou recuperação concluída. As alternativas de reenvio e novo pedido devem permitir retomar sem duplicar contas nem alterar senhas indevidamente.; CA11: Provocar falha de envio na confirmação inicial, no reenvio e na recuperação; informar falha e nova tentativa sem sucesso fictício. Após restabelecer o envio, permitir retomar com link utilizável sem contas duplicadas e sem revelar explicitamente a existência de conta na recuperação.; CA11-Confirmacao: Desdobramento de CA11/R8: falhas de envio inicial e reenvio de confirmação, retomada e unicidade da conta.

### Login e saída

#### CT-018 — Login e destino

Verificação: Entrar diretamente e após solicitar destino protegido; testar credenciais incorretas.

Resultado esperado: Corretas acessam área inicial/destino; incorretas não autenticam.

Origem no requisito: CA6: Entrar com credenciais corretas de conta confirmada; acessar a área inicial ou destino protegido solicitado. Credenciais incorretas não autenticam. Depois de cinco falhas consecutivas, a nova tentativa durante bloqueio informa espera; após o prazo, permitir nova tentativa válida.

#### CT-019 — Cinco falhas e espera

Verificação: Para mesmo e-mail/origem, falhar cinco vezes e tentar durante bloqueio e após espera.

Resultado esperado: Informar espera sem autenticar durante bloqueio; após prazo, aceitar credenciais válidas.

Origem no requisito: R6: Após cinco falhas consecutivas de login para o mesmo e-mail e origem, bloquear temporariamente as novas tentativas e informar a espera, preservando o comportamento atual. Após o prazo, permitir nova tentativa.; CA6: Entrar com credenciais corretas de conta confirmada; acessar a área inicial ou destino protegido solicitado. Credenciais incorretas não autenticam. Depois de cinco falhas consecutivas, a nova tentativa durante bloqueio informa espera; após o prazo, permitir nova tentativa válida.

#### CT-020 — Saída e lembrança

Verificação: Entrar/sair e reabrir área protegida com lembrar marcado e desmarcado.

Resultado esperado: Retornar à página pública e exigir novo login, inclusive após lembrança.

Origem no requisito: R7: Preservar a opção existente de lembrar acesso. Ela não dispensa confirmação do e-mail nem impede a saída explícita; sair encerra a sessão atual e exige novo login para voltar à área protegida.; CA7: Entrar e sair, com lembrar acesso marcado e desmarcado; retornar à página pública e exigir login ao tentar reabrir a área protegida.

### Recuperação

#### CT-021 — Pedido genérico

Verificação: Com envio disponível, pedir recuperação para conta existente e inexistente.

Resultado esperado: Mesma resposta; titular cadastrado recebe link sem revelação pela resposta.

Origem no requisito: CA8: Solicitar recuperação para e-mail cadastrado e inexistente, com envio disponível; apresentar a mesma resposta genérica. O titular cadastrado recebe o link, sem revelar a existência da conta ao solicitante pela resposta.

#### CT-022 — Redefinição válida

Verificação: Com link próprio não usado antes de60min, informar senha conforme R3/confirmação e testar senha anterior/nova.

Resultado esperado: Retornar ao login; nova funciona e antiga não permite novos logins.

Origem no requisito: R3: Cadastro e redefinição exigem senha de 12 a 255 caracteres, com ao menos uma maiúscula, uma minúscula, um número e um símbolo, rejeitando senhas conhecidas em vazamentos. A mesma regra vale nos ambientes de teste e uso.; R5: O link de recuperação é válido por 60 minutos a partir da emissão e não pode ser reutilizado após sucesso. A senha anterior deixa de permitir novos logins depois da redefinição.; CA9: Com link de recuperação próprio, não usado e antes de 60 minutos, definir senha conforme R3 e confirmação igual; retornar ao login, permitir novos logins com a senha nova e recusar a anterior. Uma conta anteriormente não confirmada continua sem acesso ao sistema.

#### CT-023 — Redefinir sem confirmar e-mail

Verificação: Redefinir conta não confirmada e entrar com senha nova.

Resultado esperado: Senha muda, e-mail permanece não confirmado e produto continua restrito.

Origem no requisito: R4: Acesso à área do sistema exige autenticação e confirmação do próprio e-mail, incluindo acesso direto às páginas protegidas. Conta não confirmada pode concluir a jornada restrita de confirmação, reenvio, recuperação e saída; não acessa as funcionalidades do produto. Receber um e-mail ou redefinir a senha não equivale a confirmar o endereço.; CA9: Com link de recuperação próprio, não usado e antes de 60 minutos, definir senha conforme R3 e confirmação igual; retornar ao login, permitir novos logins com a senha nova e recusar a anterior. Uma conta anteriormente não confirmada continua sem acesso ao sistema.

#### CT-024 — Recuperação inválida

Verificação: Tentar redefinir com link inválido e usar novo pedido.

Resultado esperado: Não alterar; orientar e oferecer novo link para retomada.

Origem no requisito: R5: O link de recuperação é válido por 60 minutos a partir da emissão e não pode ser reutilizado após sucesso. A senha anterior deixa de permitir novos logins depois da redefinição.; R8: Falha de envio ou de link não deve ser apresentada como confirmação ou recuperação concluída. As alternativas de reenvio e novo pedido devem permitir retomar sem duplicar contas nem alterar senhas indevidamente.; CA10: Tentar redefinir com link inválido, após sua expiração ou já utilizado; não alterar a senha e oferecer novo pedido. Um novo link válido permite retomar a jornada.

#### CT-025 — Recuperação expirada

Verificação: Tentar após ultrapassar60min da emissão; solicitar outro link.

Resultado esperado: Recusar sem alterar e permitir retomar com novo link válido.

Origem no requisito: R5: O link de recuperação é válido por 60 minutos a partir da emissão e não pode ser reutilizado após sucesso. A senha anterior deixa de permitir novos logins depois da redefinição.; R8: Falha de envio ou de link não deve ser apresentada como confirmação ou recuperação concluída. As alternativas de reenvio e novo pedido devem permitir retomar sem duplicar contas nem alterar senhas indevidamente.; CA10: Tentar redefinir com link inválido, após sua expiração ou já utilizado; não alterar a senha e oferecer novo pedido. Um novo link válido permite retomar a jornada.

#### CT-026 — Recuperação já usada

Verificação: Redefinir e reutilizar o mesmo link para outra senha.

Resultado esperado: Não alterar de novo; recusar e oferecer novo pedido.

Origem no requisito: R5: O link de recuperação é válido por 60 minutos a partir da emissão e não pode ser reutilizado após sucesso. A senha anterior deixa de permitir novos logins depois da redefinição.; R8: Falha de envio ou de link não deve ser apresentada como confirmação ou recuperação concluída. As alternativas de reenvio e novo pedido devem permitir retomar sem duplicar contas nem alterar senhas indevidamente.; CA10: Tentar redefinir com link inválido, após sua expiração ou já utilizado; não alterar a senha e oferecer novo pedido. Um novo link válido permite retomar a jornada.

#### CT-027 — Falha de envio de recuperação

Verificação: Provocar falha, restaurar e solicitar de novo.

Resultado esperado: Orientar sem sucesso fictício/revelação explícita da conta; titular recebe link após retomada.

Origem no requisito: R8: Falha de envio ou de link não deve ser apresentada como confirmação ou recuperação concluída. As alternativas de reenvio e novo pedido devem permitir retomar sem duplicar contas nem alterar senhas indevidamente.; CA11: Provocar falha de envio na confirmação inicial, no reenvio e na recuperação; informar falha e nova tentativa sem sucesso fictício. Após restabelecer o envio, permitir retomar com link utilizável sem contas duplicadas e sem revelar explicitamente a existência de conta na recuperação.; CA11-Recuperacao: Desdobramento de CA11/R8: falha e retomada do envio de recuperação, sem falso sucesso ou revelação da conta.

### Visual

#### CT-028 — Integração visual

Verificação: Em computador/tablet/celular, claro/escuro/sistema, percorrer as telas e os novos estados de erro/retomada. Comparar com design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; referência clara e adaptações aprovadas na Feature visual #1016101 e o fornecedor de composição #1016114 após base verificada.

Resultado esperado: Identidade, campos, botões, erros e ações coerentes/usáveis, sem reconstruir a aparência fornecida.

Origem no requisito: R9: As telas de acesso usam a base visual FinAI da Feature de adequação visual, com tipografia, paleta, campos, botões, erros e estados coerentes, adaptação para celular, tablet e computador e manutenção dos temas claro, escuro e acompanhar o sistema. Esta Feature não redefine a identidade visual.; CA12: Utilizar as telas e estados de acesso em computador, tablet e celular, nos temas claro, escuro e acompanhar o sistema; manter a linguagem visual FinAI definida pela adequação visual, controles utilizáveis e erros reconhecíveis.


## Descrições completas

### 1. [DEV] [WEB] [USUARIO] Acesso à conta pessoal - Cadastro e redefinição com política de senha consistente

#### Entrega

Completar a validação de senha no cadastro público e na redefinição esquecida, aplicando a mesma regra forte em teste e uso. Os formulários e demais validações já existem; falta a consistência exigida pelo requisito.

#### Escopo e limites

Responsável pela política compartilhada e seus erros nos dois fluxos. Preservar campos, unicidade e jornadas existentes. Envio/confirmacão e retomada dos links pertencem às outras entregas.

#### Critérios de aceite

- Cadastro e redefinição aceitam senha de 12 a 255 caracteres com maiúscula, minúscula, número e símbolo, não reconhecida como vazada e confirmação igual, com a mesma validação em teste e uso.
- Nos dois formulários, menos de 12 ou mais de 255 caracteres, ausência de qualquer classe, senha conhecida em vazamentos, ausência de senha/confirmação ou confirmação diferente impedem concluir com erro no campo, sem criar conta ou alterar senha indevidamente.
- Preservar nome/e-mail obrigatórios e até 255 caracteres, e-mail válido e único no cadastro e e-mail válido obrigatório na redefinição; não solicitar dados financeiros.
- Cadastro válido continua criando uma única conta e seguindo à confirmação. Redefinição válida retorna ao login; nova senha funciona e a anterior deixa de permitir novos logins, sem confirmar e-mail automaticamente.
- Nas telas e estados alterados, consumir marca, tipografia, paleta, campos, botões, erros e feedback da base FinAI em computador, tablet e celular, nos temas claro, escuro e acompanhar o sistema, sem reconstruir identidade ou layouts do fornecedor.

#### Dependências

Início bloqueado pelo aceite integrado [QA] [WEB] [USUARIO] Adequação visual do FinAI (#1016117), dependente dos cinco DEV visuais e representante da base implementada e verificada. Após a liberação visual, pode avançar sem esperar os demais DEV de acesso. Para concluir a jornada integrada, usar a confirmação/restrição e a retomada de recuperação das entregas correspondentes, sem bloqueio interno de início.

#### Referências

Item pai Redmine `#1016104`; regras/critérios R1, R2, R3, CA1, CA2, CA9, R9, CA12.

- design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; referência clara e adaptações aprovadas na Feature visual #1016101; linguagem de formulários, mensagens e ações de retomada. Não há composição própria de acesso no ZIP.
- Fornecedor de composição: [DEV] [WEB] [USUARIO] Adequação visual do FinAI - Página inicial e jornadas de acesso (#1016114); aceite integrado: [QA] [WEB] [USUARIO] Adequação visual do FinAI (#1016117).

### 2. [DEV] [WEB] [USUARIO] Acesso à conta pessoal - Confirmação de e-mail com acesso restrito e retomada

#### Entrega

Completar a confirmação de e-mail, do envio inicial à retomada, e impedir que contas não confirmadas acessem perfil e demais funcionalidades. Confirmação própria e reenvio já existem; faltam restrição integral e orientação nas falhas de link/envio.

#### Escopo e limites

Responsável pelo envio inicial, jornada restrita de confirmação/reenvio/saída, links de confirmação e restrição da área do produto. Preservar login, lembrar e recuperação atuais. A política de senha e a retomada da recuperação são fornecidas pelas outras entregas.

#### Critérios de aceite

- Cadastro público válido cria uma única conta, envia confirmação e orienta o titular; receber o e-mail não libera o produto antes de confirmar.
- Conta não confirmada, com sessão normal ou lembrada, não acessa diretamente área inicial, perfil, configurações ou funcionalidades do produto. Mantém confirmação, reenvio, saída e caminho de recuperação; pode sair e usar a jornada pública existente quando necessário, sem novo mecanismo autenticado.
- Titular com link próprio válido confirma e acessa a área inicial, autenticando-se quando necessário. Reabrir link ainda válido de conta já confirmada conserva a confirmação.
- Links inválidos, expirados ou de outra conta não confirmam endereço indevido nem liberam o sistema; apresentar orientação e caminho para solicitar novo link próprio.
- Falha de envio no cadastro/reenvio informa que o envio não concluiu e orienta nova tentativa, sem sucesso fictício. Após restabelecimento, retomar sem contas duplicadas nem titular sem caminho de confirmação/recuperação.
- Preservar credenciais corretas/incorretas, destino solicitado, lembrar, bloqueio após cinco falhas e saída; contas confirmadas continuam usando operações permitidas.
- Nas telas e estados alterados, consumir marca, tipografia, paleta, campos, botões, erros e feedback da base FinAI em computador, tablet e celular, nos temas claro, escuro e acompanhar o sistema, sem reconstruir identidade ou layouts do fornecedor.

#### Dependências

Início bloqueado pelo aceite integrado [QA] [WEB] [USUARIO] Adequação visual do FinAI (#1016117), dependente dos cinco DEV visuais e representante da base implementada e verificada. Após a liberação visual, pode iniciar sem esperar os demais DEV de acesso. Para concluir a jornada integrada, usar Cadastro e redefinição com política de senha consistente e Recuperação de senha com nova tentativa.

#### Referências

Item pai Redmine `#1016104`; regras/critérios R1, R2, R4, R6, R7, R8, CA1, CA3, CA4, CA5, CA6, CA7, CA11, CA11-Confirmacao, R9, CA12.

- design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; referência clara e adaptações aprovadas na Feature visual #1016101; linguagem de formulários, mensagens e ações de retomada. Não há composição própria de acesso no ZIP.
- Fornecedor de composição: [DEV] [WEB] [USUARIO] Adequação visual do FinAI - Página inicial e jornadas de acesso (#1016114); aceite integrado: [QA] [WEB] [USUARIO] Adequação visual do FinAI (#1016117).

### 3. [DEV] [WEB] [USUARIO] Acesso à conta pessoal - Recuperação de senha com nova tentativa

#### Entrega

Completar os estados de recuperação quando o envio falhar ou o link de redefinição for inválido, expirado ou já usado. O pedido genérico e o broker já existem; falta retomada sem apresentar envio ou alteração como concluídos indevidamente.

#### Escopo e limites

Responsável pela solicitação/redefinição esquecida e seus novos pedidos. Preservar resposta genérica, validade de 60 minutos, uso único, retorno ao login e estado de confirmação do e-mail. Não reimplementar a política de senha nem ampliar autenticação.

#### Critérios de aceite

- Com envio disponível, pedir recuperação para conta existente ou inexistente mantém a mesma resposta genérica; o titular cadastrado recebe o link.
- Falha no envio orienta nova tentativa sem afirmar sucesso ou revelar explicitamente existência da conta; depois de restabelecer, novo pedido permite receber link utilizável.
- Link inválido, expirado após 60 minutos ou já utilizado não altera senha e oferece novo pedido; novo link válido permite retomar.
- Link próprio, não usado e válido, com senha conforme a política compartilhada e confirmação igual, redefine e retorna ao login; senha nova funciona e a anterior não permite novos logins.
- Redefinir conta não confirmada não confirma e-mail nem libera a área do produto; preservar validações e erros, sem alteração indevida.
- Nas telas e estados alterados, consumir marca, tipografia, paleta, campos, botões, erros e feedback da base FinAI em computador, tablet e celular, nos temas claro, escuro e acompanhar o sistema, sem reconstruir identidade ou layouts do fornecedor.

#### Dependências

Início bloqueado pelo aceite integrado [QA] [WEB] [USUARIO] Adequação visual do FinAI (#1016117), dependente dos cinco DEV visuais e representante da base implementada e verificada. Pode iniciar com a recuperação existente após a liberação visual. Para concluir a redefinição integrada, usar Cadastro e redefinição com política de senha consistente. Login, saída e confirmação seguem nas jornadas existentes/entrega responsável, sem bloqueio interno de início.

#### Referências

Item pai Redmine `#1016104`; regras/critérios R2, R3, R4, R5, R8, CA2, CA8, CA9, CA10, CA11, CA11-Recuperacao, R9, CA12.

- design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; referência clara e adaptações aprovadas na Feature visual #1016101; linguagem de formulários, mensagens e ações de retomada. Não há composição própria de acesso no ZIP.
- Fornecedor de composição: [DEV] [WEB] [USUARIO] Adequação visual do FinAI - Página inicial e jornadas de acesso (#1016114); aceite integrado: [QA] [WEB] [USUARIO] Adequação visual do FinAI (#1016117).
