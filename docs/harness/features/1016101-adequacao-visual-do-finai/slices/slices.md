# Fatiamento de [WEB] [USUARIO] Adequação visual do FinAI

Revisão: 2  
Hash: `540128f28be94249ccff366dd1fbf77104534212247956b3db835830993f08f4`

## Prévia numerada

1. **[DEV] [WEB] [USUARIO] Adequação visual do FinAI - Identidade e temas no painel atual** — 2h
   - Entrega: Aplicar a marca e a identidade FinAI aos componentes compartilhados e ao dashboard atual, preservando os mecanismos existentes de aparência. A base atual é neutra e ainda contém a marca do starter; esta entrega deve produzir uma base visual inspecionável em claro, escuro e sistema.
   - Bloqueado por: Nenhum
   - Bloqueios externos: Nenhum
2. **[DEV] [WEB] [USUARIO] Adequação visual do FinAI - Estrutura e navegação responsiva atuais** — 2h
   - Entrega: Adequar estrutura, cabeçalho, navegação e menu do usuário da área autenticada à composição FinAI responsiva, mantendo os destinos atualmente disponíveis. A sidebar e o menu móvel atuais diferem da geometria e organização superior da referência.
   - Bloqueado por: Nenhum
   - Bloqueios externos: Nenhum
3. **[DEV] [WEB] [USUARIO] Adequação visual do FinAI - Página inicial e jornadas de acesso** — 2h
   - Entrega: Adequar a página pública atual e as telas de cadastro, login, solicitação de recuperação, redefinição e confirmação de e-mail à identidade FinAI, preservando seu conteúdo funcional e suas ações. Aplicar a linguagem de formulário da referência onde não existe composição própria dessas telas.
   - Bloqueado por: Nenhum
   - Bloqueios externos: Nenhum
4. **[DEV] [WEB] [USUARIO] Adequação visual do FinAI - Perfil, senha e aparência** — 2h
   - Entrega: Adequar perfil, alteração de senha, preferência de aparência e o diálogo atual de exclusão da conta à identidade FinAI. Reutilizar as operações e os componentes atuais, preservando validações, feedback e confirmação/cancelamento.
   - Bloqueado por: Nenhum
   - Bloqueios externos: Nenhum
5. **[DEV] [WEB] [USUARIO] Adequação visual do FinAI - Dois fatores e passkeys** — 2h
   - Entrega: Adequar configuração e desafio de dois fatores, confirmação de senha e gestão/entrada/confirmação de passkeys, incluindo os estados e diálogos atuais, à identidade FinAI. Preservar os mecanismos de autenticação existentes.
   - Bloqueado por: Nenhum
   - Bloqueios externos: Nenhum

## Cobertura

| Regra ou critério | Destino | Evidência |
| --- | --- | --- |
| R1: A entrega abrange a página inicial atual, cadastro, login, recuperação e redefinição de senha, confirmação de senha, verificação de e-mail, desafio de dois fatores, dashboard atual, perfil, alteração de senha, aparência, configuração de dois fatores e passkeys, incluindo seus estados e componentes existentes. Essa lista é inventário do código, não comprovação de aceite funcional anterior. | Slice 1 | Inspeção: resources/css/app.css. Responsável pela política/aparência compartilhada; aplicação por tela verificada também nas entregas de composição e QA integrada. |
| R2: Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega. | Slice 1 | Inspeção: resources/css/app.css. Responsável pela política/aparência compartilhada; aplicação por tela verificada também nas entregas de composição e QA integrada. |
| R3: A referência clara usa fundo #F5F7F8, superfícies brancas, texto #172622, texto secundário #52615C, verde principal #145C46, verde positivo #146345, vermelho negativo #A12B36, bordas #D6DFDB e destaque suave #E4F0E9. Preservar a hierarquia do design: títulos de destaque em Georgia e corpo em system-ui; controles com raio de 8px e painéis com 16px; espaçamento, bordas, sombras, estados e proporções conforme o pacote. | Slice 1 | Inspeção: resources/css/app.css. Responsável pela política/aparência compartilhada; aplicação por tela verificada também nas entregas de composição e QA integrada. |
| R4: Preservar a organização visual responsiva do design nas estruturas aplicáveis: navegação lateral no desktop e adaptação superior no tablet/celular; controles e conteúdo reorganizados conforme o espaço. Não transportar os destinos financeiros futuros para telas atuais apenas para reproduzir a navegação do protótipo. | Slice 2 | Inspeção: resources/js/layouts/app/app-sidebar-layout.tsx; resources/js/components/app-sidebar.tsx; app-sidebar-header.tsx; nav-user.tsx; ui/sidebar.tsx. Responsável pela estrutura responsiva compartilhada; particularidades por tela permanecem nas entregas correspondentes. |
| R5: Preservar claro, escuro e acompanhar o sistema. A variante escura é uma adaptação aprovada da identidade fornecida, mantendo hierarquia visual, distinção entre superfícies, leitura dos textos e identificação dos estados. Não reutilizar o tema escuro neutro do starter sem adequação à identidade FinAI. | Slice 1 | Inspeção: resources/css/app.css. Responsável pela política/aparência compartilhada; aplicação por tela verificada também nas entregas de composição e QA integrada. |
| R6: A marca FinAI substitui a identidade visual genérica do starter nas superfícies atuais. Não apresentar rótulos do protótipo que afirmem armazenamento apenas no navegador ou assistente simulado; persistência e IA real serão tratadas pelas Features responsáveis. | Slice 1 | Inspeção: resources/css/app.css. Responsável pela política/aparência compartilhada; aplicação por tela verificada também nas entregas de composição e QA integrada. |
| R7: A base visual é aceita sobre as telas atuais. Não criar páginas de Transações ou Assistente, formulários financeiros, números demonstrativos ou operações simuladas nesta Feature. As novas telas e suas composições específicas seguem a base nas próximas Features. | Slice 2 | Inspeção: resources/js/layouts/app/app-sidebar-layout.tsx; resources/js/components/app-sidebar.tsx; app-sidebar-header.tsx; nav-user.tsx; ui/sidebar.tsx. Responsável pela estrutura responsiva compartilhada; particularidades por tela permanecem nas entregas correspondentes. |
| CA1: Ao visitar cada superfície de R1 que esteja disponível para o usuário, reconhecer a identidade FinAI na marca, tipografia, paleta e componentes; nas superfícies sem desenho próprio, preservar campos e finalidade com a mesma linguagem visual. | Slice 1 | Inspeção: resources/css/app.css. Responsável pela política/aparência compartilhada; aplicação por tela verificada também nas entregas de composição e QA integrada. |
| CA2: No tema claro, comparar as estruturas e os componentes aplicáveis com o ZIP e verificar cores de R3, títulos Georgia, corpo system-ui, hierarquia, espaçamentos, proporções, raios, bordas e estados, sem manter a aparência genérica do starter. | Slice 1 | Inspeção: resources/css/app.css. Responsável pela política/aparência compartilhada; aplicação por tela verificada também nas entregas de composição e QA integrada. |
| CA3: Selecionar claro, escuro e acompanhar o sistema; cada opção continua disponível e aplica a aparência correspondente. Ao retornar à aplicação, manter a preferência conforme o comportamento existente. | Slice 4 | Inspeção: resources/js/layouts/settings/layout.tsx; resources/js/pages/user-profile/edit.tsx; user-password/edit.tsx; appearance/update.tsx; resources/js/components/delete-user.tsx. Responsável pela composição e preservação dos fluxos das superfícies explicitadas na entrega. Regras transversais também são aplicadas pelos demais DEV em suas próprias telas. |
| CA4: Com acompanhar o sistema selecionado, alterar a preferência do dispositivo; a aparência acompanha a mudança. Com claro ou escuro explicitamente selecionado, a preferência do dispositivo não substitui a escolha. | Slice 4 | Inspeção: resources/js/layouts/settings/layout.tsx; resources/js/pages/user-profile/edit.tsx; user-password/edit.tsx; appearance/update.tsx; resources/js/components/delete-user.tsx. Responsável pela composição e preservação dos fluxos das superfícies explicitadas na entrega. Regras transversais também são aplicadas pelos demais DEV em suas próprias telas. |
| CA5: No tema escuro, abrir as mesmas superfícies e estados do tema claro; manter conteúdo e ações equivalentes, identidade FinAI, textos legíveis e distinção visual entre superfícies, bordas, foco, erros e demais estados existentes. | Slice 1 | Inspeção: resources/css/app.css. Responsável pela política/aparência compartilhada; aplicação por tela verificada também nas entregas de composição e QA integrada. |
| CA6: Verificar as telas atuais em 360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080; layout e navegação se adaptam sem rolagem horizontal da página, mantendo acesso às operações atuais. | Slice 2 | Inspeção: resources/js/layouts/app/app-sidebar-layout.tsx; resources/js/components/app-sidebar.tsx; app-sidebar-header.tsx; nav-user.tsx; ui/sidebar.tsx. Responsável pela estrutura responsiva compartilhada; particularidades por tela permanecem nas entregas correspondentes. |
| CA7: Navegar e utilizar formulários, menus e diálogos atuais com mouse e teclado; preservar rótulos, foco visível e estados aplicáveis de hover, ativo, desabilitado e carregamento demonstrados no design ou existentes na aplicação. | Slice 1 | Inspeção: resources/css/app.css. Responsável pela política/aparência compartilhada; aplicação por tela verificada também nas entregas de composição e QA integrada. |
| CA8: Executar ações atuais com dados válidos e inválidos, onde aplicável; campos, validações, mensagens, cancelamentos, confirmações e resultados funcionais permanecem equivalentes após a adequação visual. O mesmo vale para restrições de acesso de visitantes e usuários autenticados. | Slice 3 | Inspeção: resources/js/pages/welcome.tsx; resources/js/layouts/auth/auth-simple-layout.tsx; resources/js/pages/session/create.tsx; user/create.tsx; user-email-reset-notification/create.tsx; user-password/create.tsx; user-email-verification-notification/create.tsx. Responsável pela composição e preservação dos fluxos das superfícies explicitadas na entrega. Regras transversais também são aplicadas pelos demais DEV em suas próprias telas. |
| CA9: Ao navegar pela entrega, não encontrar novas páginas financeiras, dados fictícios, operações simuladas, rótulos de armazenamento apenas local ou assistente simulado apresentados como funcionalidades prontas. O dashboard atual permanece sem antecipar as capacidades da Feature Dashboard financeiro. | Slice 2 | Inspeção: resources/js/layouts/app/app-sidebar-layout.tsx; resources/js/components/app-sidebar.tsx; app-sidebar-header.tsx; nav-user.tsx; ui/sidebar.tsx. Responsável pela estrutura responsiva compartilhada; particularidades por tela permanecem nas entregas correspondentes. |
| V-Publica: Desdobramento de R1/R2/CA1/CA6/CA8: composição da página inicial atual com identidade FinAI, preservando conteúdo funcional e destinos. | Slice 3 | Inspeção: resources/js/pages/welcome.tsx; resources/js/layouts/auth/auth-simple-layout.tsx; resources/js/pages/session/create.tsx; user/create.tsx; user-email-reset-notification/create.tsx; user-password/create.tsx; user-email-verification-notification/create.tsx. Responsável pela composição e preservação dos fluxos das superfícies explicitadas na entrega. Regras transversais também são aplicadas pelos demais DEV em suas próprias telas. |
| V-Acesso: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de cadastro, login, recuperação/redefinição e verificação de e-mail. | Slice 3 | Inspeção: resources/js/pages/welcome.tsx; resources/js/layouts/auth/auth-simple-layout.tsx; resources/js/pages/session/create.tsx; user/create.tsx; user-email-reset-notification/create.tsx; user-password/create.tsx; user-email-verification-notification/create.tsx. Responsável pela composição e preservação dos fluxos das superfícies explicitadas na entrega. Regras transversais também são aplicadas pelos demais DEV em suas próprias telas. |
| V-Conta: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de perfil, senha, aparência e exclusão de conta. | Slice 4 | Inspeção: resources/js/layouts/settings/layout.tsx; resources/js/pages/user-profile/edit.tsx; user-password/edit.tsx; appearance/update.tsx; resources/js/components/delete-user.tsx. Responsável pela composição e preservação dos fluxos das superfícies explicitadas na entrega. Regras transversais também são aplicadas pelos demais DEV em suas próprias telas. |
| V-Seguranca: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de 2FA, confirmação de senha e passkeys. | Slice 5 | Inspeção: resources/js/pages/user-two-factor-authentication/show.tsx; user-two-factor-authentication-challenge/show.tsx; user-password-confirmation/create.tsx; user-passkey/index.tsx; resources/js/components/two-factor-setup-modal.tsx; two-factor-recovery-codes.tsx; manage-passkeys.tsx; passkey-register.tsx; passkey-item.tsx; passkey-verify.tsx. Responsável pela composição e preservação dos fluxos das superfícies explicitadas na entrega. Regras transversais também são aplicadas pelos demais DEV em suas próprias telas. |

Formato das condições: Markdown e DOCX.

## Condições de teste

Estas condições integram a aprovação da decomposição. A validação estrutural não substitui a revisão semântica do tech lead.

### Contexto

Comparar as telas atuais com a referência visual clara e com as adaptações aprovadas de todas as telas e tema escuro. Usar visitante, conta autenticada, estados de confirmação e configuração de 2FA/passkeys conforme cada jornada atual. Matriz: 360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080. Cobrir claro e escuro e verificar seleção/persistência e acompanhar o sistema. Leitura de testes existentes não é execução nem prova de fidelidade visual. Registrar os resultados observados e impedimentos, sem declarar sucesso para condição não executada.

### Identidade e navegação

#### CT-001 — Marca e linguagem clara

Verificação: Comparar painel e componentes compartilhados atuais com design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md (:root,.brand,.btn,campos e diálogos). Conferir os valores de R3 e telas consumidoras.

Resultado esperado: Marca FinAI substitui a do starter; fundo #F5F7F8/superfícies brancas, paleta de R3, títulos Georgia/corpo system-ui, controles8px/painéis16px e hierarquia/estados aplicáveis correspondem à referência.

Origem no requisito: R1: A entrega abrange a página inicial atual, cadastro, login, recuperação e redefinição de senha, confirmação de senha, verificação de e-mail, desafio de dois fatores, dashboard atual, perfil, alteração de senha, aparência, configuração de dois fatores e passkeys, incluindo seus estados e componentes existentes. Essa lista é inventário do código, não comprovação de aceite funcional anterior.; R3: A referência clara usa fundo #F5F7F8, superfícies brancas, texto #172622, texto secundário #52615C, verde principal #145C46, verde positivo #146345, vermelho negativo #A12B36, bordas #D6DFDB e destaque suave #E4F0E9. Preservar a hierarquia do design: títulos de destaque em Georgia e corpo em system-ui; controles com raio de 8px e painéis com 16px; espaçamento, bordas, sombras, estados e proporções conforme o pacote.; R6: A marca FinAI substitui a identidade visual genérica do starter nas superfícies atuais. Não apresentar rótulos do protótipo que afirmem armazenamento apenas no navegador ou assistente simulado; persistência e IA real serão tratadas pelas Features responsáveis.; CA1: Ao visitar cada superfície de R1 que esteja disponível para o usuário, reconhecer a identidade FinAI na marca, tipografia, paleta e componentes; nas superfícies sem desenho próprio, preservar campos e finalidade com a mesma linguagem visual.; CA2: No tema claro, comparar as estruturas e os componentes aplicáveis com o ZIP e verificar cores de R3, títulos Georgia, corpo system-ui, hierarquia, espaçamentos, proporções, raios, bordas e estados, sem manter a aparência genérica do starter.

#### CT-002 — Variante escura

Verificação: Abrir cada tela/estado atual no escuro e compará-lo ao claro e à linguagem FinAI, incluindo avisos, erros, menus, diálogos e QR.

Resultado esperado: Conteúdo e ações equivalentes; superfícies,textos,bordas,foco e estados são distinguíveis e legíveis. Tema escuro do starter foi adequado, e QR permanece legível.

Origem no requisito: R5: Preservar claro, escuro e acompanhar o sistema. A variante escura é uma adaptação aprovada da identidade fornecida, mantendo hierarquia visual, distinção entre superfícies, leitura dos textos e identificação dos estados. Não reutilizar o tema escuro neutro do starter sem adequação à identidade FinAI.; CA5: No tema escuro, abrir as mesmas superfícies e estados do tema claro; manter conteúdo e ações equivalentes, identidade FinAI, textos legíveis e distinção visual entre superfícies, bordas, foco, erros e demais estados existentes.

#### CT-003 — Navegação desktop/tablet/celular

Verificação: Nos viewports aplicáveis de 360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080, navegar por painel, configurações e menu usuário, usando mouse e teclado. Referência .app,.sidebar,.topbar e media queries.

Resultado esperado: Geometria desktop e reorganização superior em telas menores preservam hierarquia e destinos atuais; ativo/foco visíveis e ações disponíveis, sem novos destinos financeiros.

Origem no requisito: R4: Preservar a organização visual responsiva do design nas estruturas aplicáveis: navegação lateral no desktop e adaptação superior no tablet/celular; controles e conteúdo reorganizados conforme o espaço. Não transportar os destinos financeiros futuros para telas atuais apenas para reproduzir a navegação do protótipo.; R7: A base visual é aceita sobre as telas atuais. Não criar páginas de Transações ou Assistente, formulários financeiros, números demonstrativos ou operações simuladas nesta Feature. As novas telas e suas composições específicas seguem a base nas próximas Features.; CA6: Verificar as telas atuais em 360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080; layout e navegação se adaptam sem rolagem horizontal da página, mantendo acesso às operações atuais.; CA7: Navegar e utilizar formulários, menus e diálogos atuais com mouse e teclado; preservar rótulos, foco visível e estados aplicáveis de hover, ativo, desabilitado e carregamento demonstrados no design ou existentes na aplicação.; CA9: Ao navegar pela entrega, não encontrar novas páginas financeiras, dados fictícios, operações simuladas, rótulos de armazenamento apenas local ou assistente simulado apresentados como funcionalidades prontas. O dashboard atual permanece sem antecipar as capacidades da Feature Dashboard financeiro.

### Página pública e acesso

#### CT-004 — Página inicial atual

Verificação: Como visitante e autenticado, abrir a página pública atual nos dois temas; conferir marca, composição e links/destinos existentes.

Resultado esperado: Identidade FinAI e linguagem aprovada aplicadas sem remover conteúdo funcional, destinos ou permissões existentes.

Origem no requisito: V-Publica: Desdobramento de R1/R2/CA1/CA6/CA8: composição da página inicial atual com identidade FinAI, preservando conteúdo funcional e destinos.; R1: A entrega abrange a página inicial atual, cadastro, login, recuperação e redefinição de senha, confirmação de senha, verificação de e-mail, desafio de dois fatores, dashboard atual, perfil, alteração de senha, aparência, configuração de dois fatores e passkeys, incluindo seus estados e componentes existentes. Essa lista é inventário do código, não comprovação de aceite funcional anterior.; R2: Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega.; CA1: Ao visitar cada superfície de R1 que esteja disponível para o usuário, reconhecer a identidade FinAI na marca, tipografia, paleta e componentes; nas superfícies sem desenho próprio, preservar campos e finalidade com a mesma linguagem visual.; CA8: Executar ações atuais com dados válidos e inválidos, onde aplicável; campos, validações, mensagens, cancelamentos, confirmações e resultados funcionais permanecem equivalentes após a adequação visual. O mesmo vale para restrições de acesso de visitantes e usuários autenticados.

#### CT-005 — Cadastro com sucesso e validação

Verificação: Abrir cadastro, tentar dados válidos e inválidos, conferir processamento/erros/resultado e navegação atual; comparar campos e botões com a linguagem da referência.

Resultado esperado: Mesmos campos,validações,mensagens funcionais,destinos e resultados; composição,estados e temas recebem identidade FinAI.

Origem no requisito: V-Acesso: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de cadastro, login, recuperação/redefinição e verificação de e-mail.; R2: Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega.; CA8: Executar ações atuais com dados válidos e inválidos, onde aplicável; campos, validações, mensagens, cancelamentos, confirmações e resultados funcionais permanecem equivalentes após a adequação visual. O mesmo vale para restrições de acesso de visitantes e usuários autenticados.

#### CT-006 — Login e alternativas presentes

Verificação: Abrir login, usar credenciais válidas/inválidas, lembrar acesso e links atuais; conferir presença da entrada por passkey e encaminhamento para2FA quando exigido pela conta.

Resultado esperado: Aparência é adequada; login,erros,processamento e alternativas atuais continuam disponíveis e respeitam suas restrições.

Origem no requisito: V-Acesso: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de cadastro, login, recuperação/redefinição e verificação de e-mail.; R2: Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega.; CA8: Executar ações atuais com dados válidos e inválidos, onde aplicável; campos, validações, mensagens, cancelamentos, confirmações e resultados funcionais permanecem equivalentes após a adequação visual. O mesmo vale para restrições de acesso de visitantes e usuários autenticados.

#### CT-007 — Solicitação de recuperação

Verificação: Percorrer a solicitação atual com e-mail válido/inválido e observar mensagens de sucesso/falha disponíveis, além do retorno ao login.

Resultado esperado: Campos,links,mensagens e comportamento atual preservados; erros e processamento seguem identidade FinAI.

Origem no requisito: V-Acesso: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de cadastro, login, recuperação/redefinição e verificação de e-mail.; R2: Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega.; CA8: Executar ações atuais com dados válidos e inválidos, onde aplicável; campos, validações, mensagens, cancelamentos, confirmações e resultados funcionais permanecem equivalentes após a adequação visual. O mesmo vale para restrições de acesso de visitantes e usuários autenticados.

#### CT-008 — Redefinição de senha

Verificação: Com link de teste utilizável e cenários de rejeição atuais, conferir senha/confirmação, validação e retorno após sucesso.

Resultado esperado: A operação mantém comportamento e validação atuais com os estados visuais adequados; não altera políticas de senha.

Origem no requisito: V-Acesso: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de cadastro, login, recuperação/redefinição e verificação de e-mail.; R2: Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega.; CA8: Executar ações atuais com dados válidos e inválidos, onde aplicável; campos, validações, mensagens, cancelamentos, confirmações e resultados funcionais permanecem equivalentes após a adequação visual. O mesmo vale para restrições de acesso de visitantes e usuários autenticados.

#### CT-009 — Verificação de e-mail

Verificação: Com conta no estado atual de confirmação pendente, abrir aviso, reenviar e sair; conferir retorno com estado confirmado conforme o fluxo existente.

Resultado esperado: Orientações,ações e restrições atuais continuam equivalentes, com aparência FinAI e estados de feedback preservados.

Origem no requisito: V-Acesso: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de cadastro, login, recuperação/redefinição e verificação de e-mail.; R2: Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega.; CA8: Executar ações atuais com dados válidos e inválidos, onde aplicável; campos, validações, mensagens, cancelamentos, confirmações e resultados funcionais permanecem equivalentes após a adequação visual. O mesmo vale para restrições de acesso de visitantes e usuários autenticados.

### Perfil e preferências

#### CT-010 — Perfil e avisos existentes

Verificação: Com usuário permitido, alterar perfil com entradas válidas/inválidas e verificar avisos/reenvio de confirmação quando aplicáveis ao estado atual.

Resultado esperado: Dados,erros,avisos e sucesso mantêm o comportamento existente; campos e feedback recebem a identidade FinAI.

Origem no requisito: V-Conta: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de perfil, senha, aparência e exclusão de conta.; R2: Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega.; CA8: Executar ações atuais com dados válidos e inválidos, onde aplicável; campos, validações, mensagens, cancelamentos, confirmações e resultados funcionais permanecem equivalentes após a adequação visual. O mesmo vale para restrições de acesso de visitantes e usuários autenticados.

#### CT-011 — Alteração de senha

Verificação: Percorrer alteração atual com senha atual/novas informações válidas e inválidas e observar resultados e mensagens.

Resultado esperado: Apenas aparência é alterada; campos,validações,feedback e efeito funcional permanecem iguais.

Origem no requisito: V-Conta: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de perfil, senha, aparência e exclusão de conta.; R2: Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega.; CA8: Executar ações atuais com dados válidos e inválidos, onde aplicável; campos, validações, mensagens, cancelamentos, confirmações e resultados funcionais permanecem equivalentes após a adequação visual. O mesmo vale para restrições de acesso de visitantes e usuários autenticados.

#### CT-012 — Escolha de aparência

Verificação: Selecionar claro, escuro e sistema na página atual; conferir cada seleção nas superfícies adaptadas e voltar à aplicação.

Resultado esperado: Três escolhas preservadas; modo aplicado e preferência mantida conforme o comportamento existente.

Origem no requisito: CA3: Selecionar claro, escuro e acompanhar o sistema; cada opção continua disponível e aplica a aparência correspondente. Ao retornar à aplicação, manter a preferência conforme o comportamento existente.; R5: Preservar claro, escuro e acompanhar o sistema. A variante escura é uma adaptação aprovada da identidade fornecida, mantendo hierarquia visual, distinção entre superfícies, leitura dos textos e identificação dos estados. Não reutilizar o tema escuro neutro do starter sem adequação à identidade FinAI.; V-Conta: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de perfil, senha, aparência e exclusão de conta.

#### CT-013 — Mudança da preferência do dispositivo

Verificação: Em sistema, alterar a preferência do dispositivo; repetir após selecionar claro e escuro explicitamente.

Resultado esperado: Sistema acompanha a mudança; escolhas explícitas não são substituídas pela preferência do dispositivo.

Origem no requisito: CA4: Com acompanhar o sistema selecionado, alterar a preferência do dispositivo; a aparência acompanha a mudança. Com claro ou escuro explicitamente selecionado, a preferência do dispositivo não substitui a escolha.; R5: Preservar claro, escuro e acompanhar o sistema. A variante escura é uma adaptação aprovada da identidade fornecida, mantendo hierarquia visual, distinção entre superfícies, leitura dos textos e identificação dos estados. Não reutilizar o tema escuro neutro do starter sem adequação à identidade FinAI.; V-Conta: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de perfil, senha, aparência e exclusão de conta.

#### CT-014 — Exclusão da conta e cancelamento

Verificação: Com conta de teste, abrir diálogo atual, cancelar/fechar, provocar erro disponível e concluir a confirmação válida; observar estados e foco.

Resultado esperado: Cancelamentos/erro não excluem indevidamente; confirmação válida mantém o efeito existente. Diálogo e estados seguem a identidade FinAI.

Origem no requisito: V-Conta: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de perfil, senha, aparência e exclusão de conta.; R2: Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega.; CA7: Navegar e utilizar formulários, menus e diálogos atuais com mouse e teclado; preservar rótulos, foco visível e estados aplicáveis de hover, ativo, desabilitado e carregamento demonstrados no design ou existentes na aplicação.; CA8: Executar ações atuais com dados válidos e inválidos, onde aplicável; campos, validações, mensagens, cancelamentos, confirmações e resultados funcionais permanecem equivalentes após a adequação visual. O mesmo vale para restrições de acesso de visitantes e usuários autenticados.

### Segurança existente

#### CT-015 — Configuração2FA

Verificação: Com contas/estados adequados, percorrer QR,chave manual,confirmaçãoOTP,continuação/cancelamento,carregamento e erros atuais, em claro/escuro.

Resultado esperado: Controles e estados são preservados com identidade FinAI; QR legível no escuro; cancelamentos e erros mantêm seus efeitos atuais.

Origem no requisito: V-Seguranca: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de 2FA, confirmação de senha e passkeys.; R2: Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega.; CA5: No tema escuro, abrir as mesmas superfícies e estados do tema claro; manter conteúdo e ações equivalentes, identidade FinAI, textos legíveis e distinção visual entre superfícies, bordas, foco, erros e demais estados existentes.; CA8: Executar ações atuais com dados válidos e inválidos, onde aplicável; campos, validações, mensagens, cancelamentos, confirmações e resultados funcionais permanecem equivalentes após a adequação visual. O mesmo vale para restrições de acesso de visitantes e usuários autenticados.

#### CT-016 — Códigos e desativação2FA

Verificação: Com2FA configurada, conferir apresentação/ações atuais de códigos de recuperação e desativação, incluindo falhas disponíveis.

Resultado esperado: Mesmas operações e permissões; estado e resultados equivalentes com aparência adequada.

Origem no requisito: V-Seguranca: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de 2FA, confirmação de senha e passkeys.; R2: Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega.; CA8: Executar ações atuais com dados válidos e inválidos, onde aplicável; campos, validações, mensagens, cancelamentos, confirmações e resultados funcionais permanecem equivalentes após a adequação visual. O mesmo vale para restrições de acesso de visitantes e usuários autenticados.

#### CT-017 — Desafio2FA

Verificação: Entrar com conta que exija2FA e percorrer código válido/inválido e alternativa atual de recuperação.

Resultado esperado: Jornada,campos,erros e resultado de autenticação preservados, com estados visualmente coerentes.

Origem no requisito: V-Seguranca: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de 2FA, confirmação de senha e passkeys.; R2: Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega.; CA8: Executar ações atuais com dados válidos e inválidos, onde aplicável; campos, validações, mensagens, cancelamentos, confirmações e resultados funcionais permanecem equivalentes após a adequação visual. O mesmo vale para restrições de acesso de visitantes e usuários autenticados.

#### CT-018 — Confirmação de senha

Verificação: Abrir ação atual que solicite confirmação de senha; usar senha válida/inválida e observar continuidade.

Resultado esperado: Exigência,resultado e erros atuais mantidos, com aparência FinAI e foco utilizável.

Origem no requisito: V-Seguranca: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de 2FA, confirmação de senha e passkeys.; R2: Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega.; CA8: Executar ações atuais com dados válidos e inválidos, onde aplicável; campos, validações, mensagens, cancelamentos, confirmações e resultados funcionais permanecem equivalentes após a adequação visual. O mesmo vale para restrições de acesso de visitantes e usuários autenticados.

#### CT-019 — Passkeys sem dados e suporte indisponível

Verificação: Abrir gestão sem passkeys e conferir a alternativa de entrada em navegador suportado e no estado de indisponibilidade existente.

Resultado esperado: Estado vazio e indisponibilidade comunicados como antes; aparência FinAI aplicada sem oferecer recurso funcional novo.

Origem no requisito: V-Seguranca: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de 2FA, confirmação de senha e passkeys.; R2: Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega.; CA8: Executar ações atuais com dados válidos e inválidos, onde aplicável; campos, validações, mensagens, cancelamentos, confirmações e resultados funcionais permanecem equivalentes após a adequação visual. O mesmo vale para restrições de acesso de visitantes e usuários autenticados.

#### CT-020 — Registro,listagem e remoção de passkeys

Verificação: Com suporte e dados de teste, registrar,consultar e remover passkey; cancelar remoção e observar estados de carregamento/erro atuais.

Resultado esperado: Ações,resultados e cancelamentos atuais preservados; lista vazia/preenchida,diálogo e feedback seguem a identidade FinAI.

Origem no requisito: V-Seguranca: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de 2FA, confirmação de senha e passkeys.; R2: Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega.; CA7: Navegar e utilizar formulários, menus e diálogos atuais com mouse e teclado; preservar rótulos, foco visível e estados aplicáveis de hover, ativo, desabilitado e carregamento demonstrados no design ou existentes na aplicação.; CA8: Executar ações atuais com dados válidos e inválidos, onde aplicável; campos, validações, mensagens, cancelamentos, confirmações e resultados funcionais permanecem equivalentes após a adequação visual. O mesmo vale para restrições de acesso de visitantes e usuários autenticados.

#### CT-021 — Entrada e confirmação por passkey

Verificação: Percorrer a entrada/verificação atuais com sucesso e falha quando suportado e conferir o encaixe no login.

Resultado esperado: Integração entre páginas de acesso e componentes de passkey preservada, sem mudança de permissões ou mecanismo.

Origem no requisito: V-Seguranca: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de 2FA, confirmação de senha e passkeys.; V-Acesso: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de cadastro, login, recuperação/redefinição e verificação de e-mail.; R2: Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega.; CA8: Executar ações atuais com dados válidos e inválidos, onde aplicável; campos, validações, mensagens, cancelamentos, confirmações e resultados funcionais permanecem equivalentes após a adequação visual. O mesmo vale para restrições de acesso de visitantes e usuários autenticados.

### Verificação integrada

#### CT-022 — Teclado e estados de controles

Verificação: Percorrer formulários,menus e diálogos atuais com teclado/mouse e conferir rótulos,foco,hover,ativo,desabilitado e carregamento onde aplicáveis.

Resultado esperado: Operações atuais acessíveis pelos mesmos controles, com rótulos e foco visíveis; identidade visual dos estados corresponde à referência e adaptações.

Origem no requisito: CA7: Navegar e utilizar formulários, menus e diálogos atuais com mouse e teclado; preservar rótulos, foco visível e estados aplicáveis de hover, ativo, desabilitado e carregamento demonstrados no design ou existentes na aplicação.; R2: Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega.

#### CT-023 — Matriz visual completa

Verificação: Verificar todas as superfícies de R1 e estados existentes aplicáveis em 360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080, tanto no claro quanto no escuro; incluir página pública,acesso,painel,perfil,senha,aparência,2FA,confirmações e passkeys. Comparar identidade clara com design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md e adaptação escura aprovada.

Resultado esperado: Cada tela preserva identidade,composição aplicável,conteúdo e acesso aos controles, sem rolagem horizontal da página. As composições sem desenho próprio seguem a linguagem FinAI; nenhum viewport ou superfície é dispensado.

Origem no requisito: R1: A entrega abrange a página inicial atual, cadastro, login, recuperação e redefinição de senha, confirmação de senha, verificação de e-mail, desafio de dois fatores, dashboard atual, perfil, alteração de senha, aparência, configuração de dois fatores e passkeys, incluindo seus estados e componentes existentes. Essa lista é inventário do código, não comprovação de aceite funcional anterior.; CA1: Ao visitar cada superfície de R1 que esteja disponível para o usuário, reconhecer a identidade FinAI na marca, tipografia, paleta e componentes; nas superfícies sem desenho próprio, preservar campos e finalidade com a mesma linguagem visual.; CA2: No tema claro, comparar as estruturas e os componentes aplicáveis com o ZIP e verificar cores de R3, títulos Georgia, corpo system-ui, hierarquia, espaçamentos, proporções, raios, bordas e estados, sem manter a aparência genérica do starter.; CA5: No tema escuro, abrir as mesmas superfícies e estados do tema claro; manter conteúdo e ações equivalentes, identidade FinAI, textos legíveis e distinção visual entre superfícies, bordas, foco, erros e demais estados existentes.; CA6: Verificar as telas atuais em 360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080; layout e navegação se adaptam sem rolagem horizontal da página, mantendo acesso às operações atuais.; V-Publica: Desdobramento de R1/R2/CA1/CA6/CA8: composição da página inicial atual com identidade FinAI, preservando conteúdo funcional e destinos.; V-Acesso: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de cadastro, login, recuperação/redefinição e verificação de e-mail.; V-Conta: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de perfil, senha, aparência e exclusão de conta.; V-Seguranca: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de 2FA, confirmação de senha e passkeys.

#### CT-024 — Permissões e ausência de antecipação financeira

Verificação: Como visitante e contas em estados diferentes, tentar caminhos atuais públicos/protegidos e navegar após sair. Conferir painel e menu sem páginas futuras.

Resultado esperado: Mesmas restrições e destinos anteriores; sem novas regras de acesso,sem dados/ações financeiras simuladas,sem destinos Transações/Assistente e sem rótulos de armazenamento local/IA simulada como produto pronto.

Origem no requisito: R2: Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega.; R6: A marca FinAI substitui a identidade visual genérica do starter nas superfícies atuais. Não apresentar rótulos do protótipo que afirmem armazenamento apenas no navegador ou assistente simulado; persistência e IA real serão tratadas pelas Features responsáveis.; R7: A base visual é aceita sobre as telas atuais. Não criar páginas de Transações ou Assistente, formulários financeiros, números demonstrativos ou operações simuladas nesta Feature. As novas telas e suas composições específicas seguem a base nas próximas Features.; CA8: Executar ações atuais com dados válidos e inválidos, onde aplicável; campos, validações, mensagens, cancelamentos, confirmações e resultados funcionais permanecem equivalentes após a adequação visual. O mesmo vale para restrições de acesso de visitantes e usuários autenticados.; CA9: Ao navegar pela entrega, não encontrar novas páginas financeiras, dados fictícios, operações simuladas, rótulos de armazenamento apenas local ou assistente simulado apresentados como funcionalidades prontas. O dashboard atual permanece sem antecipar as capacidades da Feature Dashboard financeiro.


## Descrições completas

### 1. [DEV] [WEB] [USUARIO] Adequação visual do FinAI - Identidade e temas no painel atual

#### Entrega

Aplicar a marca e a identidade FinAI aos componentes compartilhados e ao dashboard atual, preservando os mecanismos existentes de aparência. A base atual é neutra e ainda contém a marca do starter; esta entrega deve produzir uma base visual inspecionável em claro, escuro e sistema.

#### Escopo e limites

Responsável pela aparência compartilhada: marca, tipografia, paleta, raios, bordas, sombras, controles e seus estados. A composição da navegação pertence à entrega de estrutura; as composições particulares das outras telas pertencem às entregas correspondentes. Não transformar o dashboard placeholder em dashboard financeiro.

#### Critérios de aceite

- No painel atual e nos componentes compartilhados, apresentar marca FinAI e, no claro, fundo #F5F7F8, superfícies brancas, texto #172622, secundário #52615C, principal #145C46, positivo #146345, negativo #A12B36, bordas #D6DFDB e destaque #E4F0E9, títulos Georgia, corpo system-ui, controles com raio8px e painéis16px; preservar proporções, espaçamentos e estados aplicáveis da referência.
- No escuro, adaptar fundos, superfícies, bordas, textos e estados à identidade FinAI com leitura e distinção visual, sem conservar a aparência neutra do starter.
- Manter claro, escuro e acompanhar o sistema, preferência persistida conforme comportamento atual e reação às mudanças do dispositivo somente quando sistema estiver selecionado.
- Aplicar linguagem comum de hover, foco, ativo, desabilitado, carregamento, erro e feedback aos componentes existentes, preservando os significados e interações.
- O painel continua sem números ou operações financeiras novas, e a base não apresenta rótulos de armazenamento apenas local ou assistente simulado.
- Nas superfícies desta entrega, conferir os nove viewports (360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080), temas claro e escuro, estados aplicáveis e ausência de rolagem horizontal da página; manter acesso às ações atuais, rótulos e foco visível.

#### Dependências

Pode iniciar com a base atual. Fornece identidade e aparência compartilhada às entregas Estrutura e navegação responsiva atuais, Página inicial e jornadas de acesso, Perfil, senha e aparência e Dois fatores e passkeys. A aceitação desta base é demonstrada no painel atual; a QA conjunta verifica a aplicação em todas as composições.

#### Referências

Item pai Redmine `#1016101`; regras/critérios R1, R2, R3, R5, R6, CA1, CA2, CA5, CA7.

- design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; :root, .brand, .btn, campos, diálogos, cores/tipografia; #overview como referência de linguagem, sem transportar suas capacidades futuras
- Adaptações aprovadas: todas as telas atuais, claro/escuro/sistema preservados; telas futuras nas próximas Features.

### 2. [DEV] [WEB] [USUARIO] Adequação visual do FinAI - Estrutura e navegação responsiva atuais

#### Entrega

Adequar estrutura, cabeçalho, navegação e menu do usuário da área autenticada à composição FinAI responsiva, mantendo os destinos atualmente disponíveis. A sidebar e o menu móvel atuais diferem da geometria e organização superior da referência.

#### Escopo e limites

Responsável pela disposição compartilhada e adaptações por largura, sem redefinir marca ou tema. Não criar destinos Transações/Assistente nem números, formulários ou operações financeiras.

#### Critérios de aceite

- No desktop, apresentar geometria compatível com sidebar240px, cabeçalho80px e conteúdo da referência nos espaços aplicáveis; em larguras intermediárias e celulares, reorganizar a navegação no topo conforme o design.
- Manter acesso aos destinos atuais, configurações, menu do usuário e saída, com indicação do destino ativo onde aplicável. Não criar links para páginas futuras.
- Integrar a identidade e os temas fornecidos por Identidade e temas no painel atual, mantendo conteúdo e ações equivalentes entre claro e escuro.
- Os caminhos e restrições de acesso existentes permanecem iguais; navegação e menus continuam utilizáveis por teclado com foco visível.
- Nas superfícies desta entrega, conferir os nove viewports (360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080), temas claro e escuro, estados aplicáveis e ausência de rolagem horizontal da página; manter acesso às ações atuais, rótulos e foco visível.

#### Dependências

Pode iniciar com a estrutura atual e a referência. Para concluir o aceite visual, integrar Identidade e temas no painel atual. As composições de acesso e configurações integram esta estrutura quando aplicável, sem bloqueio técnico de início entre essas entregas.

#### Referências

Item pai Redmine `#1016101`; regras/critérios R1, R2, R4, R7, CA1, CA6, CA7, CA9.

- design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; .app, .sidebar, .topbar, navegação, main e @media(767/1023/1200/1440)
- Adaptações aprovadas: todas as telas atuais, claro/escuro/sistema preservados; telas futuras nas próximas Features.

### 3. [DEV] [WEB] [USUARIO] Adequação visual do FinAI - Página inicial e jornadas de acesso

#### Entrega

Adequar a página pública atual e as telas de cadastro, login, solicitação de recuperação, redefinição e confirmação de e-mail à identidade FinAI, preservando seu conteúdo funcional e suas ações. Aplicar a linguagem de formulário da referência onde não existe composição própria dessas telas.

#### Escopo e limites

A composição e estados destas páginas pertencem a esta entrega. Preservar a presença/encaixe da entrada por passkey no login; os estados próprios de passkeys, 2FA e confirmação de senha pertencem a Dois fatores e passkeys. Não alterar políticas de acesso, campos, validações ou mensagens funcionais.

#### Critérios de aceite

- Página pública, cadastro, login, recuperação, redefinição e verificação de e-mail apresentam marca, títulos, campos, botões, links e espaçamento coerentes com FinAI, sem identidade visual genérica do starter.
- As telas sem composição própria do ZIP usam a mesma linguagem visual, preservando campos, finalidade e destinos.
- Com dados válidos e inválidos, estados de processamento, mensagens de erro/sucesso e reenvio, manter o comportamento funcional existente e aplicar o visual correspondente.
- Os caminhos de cadastro/login/recuperação/retorno e a presença das alternativas atuais de autenticação continuam disponíveis; visitantes e autenticados mantêm as restrições atuais.
- Conferir as páginas nos temas claro e escuro integrados à base; o modo sistema continua utilizando a preferência vigente.
- Nas superfícies desta entrega, conferir os nove viewports (360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080), temas claro e escuro, estados aplicáveis e ausência de rolagem horizontal da página; manter acesso às ações atuais, rótulos e foco visível.

#### Dependências

Pode iniciar a composição das páginas atuais. Para concluir, integrar Identidade e temas no painel atual e, onde houver navegação autenticada, Estrutura e navegação responsiva atuais. Integrar o encaixe da entrada por passkey com Dois fatores e passkeys, sem relação nativa de bloqueio de início.

#### Referências

Item pai Redmine `#1016101`; regras/critérios R1, R2, R3, R5, R6, CA1, CA2, CA5, CA6, CA7, CA8, V-Publica, V-Acesso.

- design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; .brand, títulos, campos, botões e mensagens do index.html; adaptação aprovada para página inicial e telas de acesso sem desenho específico
- Adaptações aprovadas: todas as telas atuais, claro/escuro/sistema preservados; telas futuras nas próximas Features.

### 4. [DEV] [WEB] [USUARIO] Adequação visual do FinAI - Perfil, senha e aparência

#### Entrega

Adequar perfil, alteração de senha, preferência de aparência e o diálogo atual de exclusão da conta à identidade FinAI. Reutilizar as operações e os componentes atuais, preservando validações, feedback e confirmação/cancelamento.

#### Escopo e limites

Não alterar dados, regras de senha, permissões ou o efeito de exclusão. Esta entrega possui a composição das páginas de perfil/senha/aparência; o mecanismo e a aparência compartilhada dos temas vêm de Identidade e temas no painel atual.

#### Critérios de aceite

- Perfil, formulário de senha, página de aparência e diálogo de exclusão usam a paleta, tipografia, hierarquia, campos, botões, erros e superfícies FinAI.
- Alterar perfil e senha com entradas válidas/inválidas mantém resultados e mensagens funcionais; avisos de verificação de e-mail e reenvio presentes no perfil permanecem quando aplicáveis.
- Excluir a conta continua exigindo a confirmação existente; cancelar/fechar preserva a conta; erro e sucesso mantêm seu comportamento atual com aparência adequada.
- Claro, escuro e acompanhar o sistema continuam selecionáveis; retornar à aplicação conserva preferência, e mudança do dispositivo altera a aparência apenas em sistema.
- Manter navegação entre configurações e acesso às ações atuais sem criar novas regras de confirmação de e-mail ou autenticação.
- Nas superfícies desta entrega, conferir os nove viewports (360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080), temas claro e escuro, estados aplicáveis e ausência de rolagem horizontal da página; manter acesso às ações atuais, rótulos e foco visível.

#### Dependências

Pode iniciar a adequação das páginas atuais. Para concluir o aceite, integrar Identidade e temas no painel atual e Estrutura e navegação responsiva atuais. A preservação funcional não depende de implementar a futura Feature Acesso à conta pessoal.

#### Referências

Item pai Redmine `#1016101`; regras/critérios R1, R2, R3, R5, CA1, CA2, CA3, CA4, CA5, CA6, CA7, CA8, V-Conta.

- design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; .btn, inputs, mensagens, dialog e tokens; adaptação aprovada para perfil/configurações sem composição específica
- Adaptações aprovadas: todas as telas atuais, claro/escuro/sistema preservados; telas futuras nas próximas Features.

### 5. [DEV] [WEB] [USUARIO] Adequação visual do FinAI - Dois fatores e passkeys

#### Entrega

Adequar configuração e desafio de dois fatores, confirmação de senha e gestão/entrada/confirmação de passkeys, incluindo os estados e diálogos atuais, à identidade FinAI. Preservar os mecanismos de autenticação existentes.

#### Escopo e limites

Esta entrega possui composições e estados específicos de QR/chave manual/OTP/códigos, confirmação de senha e passkeys. Não adicionar métodos de autenticação, trocar validações ou redesenhar o restante do login; sua presença é integrada com Página inicial e jornadas de acesso.

#### Critérios de aceite

- Configuração/desafio2FA, confirmação de senha e passkeys apresentam identidade FinAI no claro e escuro, mantendo conteúdo e ações equivalentes.
- Preservar os estados atuais de QR/chave manual, confirmação OTP, códigos de recuperação, ativação/desativação, carregamento e erros; o QR continua legível no tema escuro.
- Preservar passkeys vazias/preenchidas, indisponibilidade do navegador quando aplicável, registro, entrada/verificação, remoção, cancelamento e erros existentes, com seus resultados e controles atuais.
- Diálogos mantêm abertura/fechamento, rótulos, foco visível e operação por teclado; cancelamentos e falhas não passam a concluir ações indevidamente.
- Preservar as permissões e a exigência atual de confirmação de senha, sem ampliar ou remover recursos.
- Nas superfícies desta entrega, conferir os nove viewports (360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080), temas claro e escuro, estados aplicáveis e ausência de rolagem horizontal da página; manter acesso às ações atuais, rótulos e foco visível.

#### Dependências

Pode iniciar com os recursos e telas atuais. Para concluir, integrar a identidade de Identidade e temas no painel atual e a estrutura aplicável de Estrutura e navegação responsiva atuais; integrar a entrada por passkey com Página inicial e jornadas de acesso. Não há bloqueio nativo de início entre esses DEV.

#### Referências

Item pai Redmine `#1016101`; regras/critérios R1, R2, R3, R5, CA1, CA2, CA5, CA6, CA7, CA8, V-Seguranca.

- design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; .btn, inputs, dialog, mensagens e tokens; adaptação aprovada para telas e estados de segurança atuais sem desenho específico
- Adaptações aprovadas: todas as telas atuais, claro/escuro/sistema preservados; telas futuras nas próximas Features.
