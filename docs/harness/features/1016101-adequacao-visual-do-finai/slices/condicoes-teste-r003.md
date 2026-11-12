# Condições de teste

## Contexto

Comparar as telas atuais com a referência visual clara e com as adaptações aprovadas de todas as telas e tema escuro. Usar visitante, conta autenticada, estados de confirmação e configuração de 2FA/passkeys conforme cada jornada atual. Matriz: 360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080. Cobrir claro e escuro e verificar seleção/persistência e acompanhar o sistema. Leitura de testes existentes não é execução nem prova de fidelidade visual. Registrar os resultados observados e impedimentos, sem declarar sucesso para condição não executada.

## Identidade e navegação

### CT-001 — Marca e linguagem clara

Verificação: Comparar painel e componentes compartilhados atuais com design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md (:root,.brand,.btn,campos e diálogos). Conferir os valores de R3 e telas consumidoras.

Resultado esperado: Marca FinAI substitui a do starter; fundo #F5F7F8/superfícies brancas, paleta de R3, títulos Georgia/corpo system-ui, controles8px/painéis16px e hierarquia/estados aplicáveis correspondem à referência.

Origem no requisito: R1: A entrega abrange a página inicial atual, cadastro, login, recuperação e redefinição de senha, confirmação de senha, verificação de e-mail, desafio de dois fatores, dashboard atual, perfil, alteração de senha, aparência, configuração de dois fatores e passkeys, incluindo seus estados e componentes existentes. Essa lista é inventário do código, não comprovação de aceite funcional anterior.; R3: A referência clara usa fundo #F5F7F8, superfícies brancas, texto #172622, texto secundário #52615C, verde principal #145C46, verde positivo #146345, vermelho negativo #A12B36, bordas #D6DFDB e destaque suave #E4F0E9. Preservar a hierarquia do design: títulos de destaque em Georgia e corpo em system-ui; controles com raio de 8px e painéis com 16px; espaçamento, bordas, sombras, estados e proporções conforme o pacote.; R6: A marca FinAI substitui a identidade visual genérica do starter nas superfícies atuais. Não apresentar rótulos do protótipo que afirmem armazenamento apenas no navegador ou assistente simulado; persistência e IA real serão tratadas pelas Features responsáveis.; CA1: Ao visitar cada superfície de R1 que esteja disponível para o usuário, reconhecer a identidade FinAI na marca, tipografia, paleta e componentes; nas superfícies sem desenho próprio, preservar campos e finalidade com a mesma linguagem visual.; CA2: No tema claro, comparar as estruturas e os componentes aplicáveis com a referência design-input-001 e as alterações compartilhadas de design-input-002, conforme R4 e verificar cores de R3, títulos Georgia, corpo system-ui, hierarquia, espaçamentos, proporções, raios, bordas e estados, sem manter a aparência genérica do starter.

### CT-002 — Variante escura

Verificação: Abrir cada tela/estado atual no escuro e compará-lo ao claro e à linguagem FinAI, incluindo avisos, erros, menus, diálogos e QR.

Resultado esperado: Conteúdo e ações equivalentes; superfícies,textos,bordas,foco e estados são distinguíveis e legíveis. Tema escuro do starter foi adequado, e QR permanece legível.

Origem no requisito: R5: Preservar claro, escuro e acompanhar o sistema. A variante escura é uma adaptação aprovada da identidade fornecida, mantendo hierarquia visual, distinção entre superfícies, leitura dos textos e identificação dos estados. Não reutilizar o tema escuro neutro do starter sem adequação à identidade FinAI.; CA5: No tema escuro, abrir as mesmas superfícies e estados do tema claro; manter conteúdo e ações equivalentes, identidade FinAI, textos legíveis e distinção visual entre superfícies, bordas, foco, erros e demais estados existentes.

### CT-003 — Navegação desktop/tablet/celular

Verificação: Nos nove viewports de CA6, navegar pelo painel e configurações com mouse, toque e teclado. Comparar a estrutura compartilhada com design-input-002 — docs/harness/features/1016101-adequacao-visual-do-finai/sources/design-input-002.md, index.html, regras responsivas finais de .app, .sidebar nav, .workspace e .topbar. Abrir o menu da conta e conferir acesso a configurações, links atuais e saída.

Resultado esperado: Até 767px, marca superior e navegação principal fixa no rodapé; de 768 a 1024px inclusive, lateral compacta de 72px mais a área segura e conteúdo ao lado, sem barra inferior; a partir de 1025px, navegação lateral desktop com recolhimento atual. A partir de 768px, conteúdo contornado e arredondado com entorno contínuo. Ativo, foco, acesso aos destinos, conta, configurações, links e saída preservados, sem novos destinos financeiros.

Origem no requisito: R4: Aplicar a revisão design-input-002 à estrutura autenticada compartilhada: até 767px, marca no topo e navegação principal fixa no rodapé, de largura total, com base de 56px acrescida da área segura inferior e ícones de 24px, alvos de pelo menos 44px, sem legendas visíveis e com nomes acessíveis; de 768 a 1024px inclusive, navegação lateral compacta de 72px acrescida da área segura lateral, marca compacta, alvos de pelo menos 48px e conteúdo ao lado, sem barra inferior; a partir de 1025px, navegação lateral desktop, preservando o recolhimento e os destinos atuais. A partir de 768px, apresentar o conteúdo em superfície com fundo de trabalho, contorno de 1px, raio de 16px e margem de 8px, com a navegação integrada ao entorno e cabeçalho transparente conforme a referência. Reservar espaço para navegação e áreas seguras, sem encobrir conteúdo, foco, mensagens ou controles. Preservar acesso ao menu da conta, configurações, links e saída em todas as larguras, adaptando sua apresentação quando o protótipo esconder o rodapé lateral. Não transportar destinos financeiros futuros para as telas atuais.; R7: A base visual é aceita sobre as telas atuais. Não criar páginas de Transações ou Assistente, formulários financeiros, números demonstrativos ou operações simuladas nesta Feature. As novas telas e suas composições específicas seguem a base nas próximas Features.; CA6: Verificar as telas atuais em 360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080; layout e navegação se adaptam sem rolagem horizontal da página, mantendo acesso às operações atuais. Conferir também as transições 767/768px e 1024/1025px, incluindo redimensionamento após recolher a navegação desktop; cada largura aplica o modo de R4 e mantém os destinos e ações atuais disponíveis.; CA7: Navegar e utilizar formulários, menus e diálogos atuais com mouse e teclado; preservar rótulos, foco visível e estados aplicáveis de hover, ativo, desabilitado e carregamento demonstrados no design ou existentes na aplicação.; CA9: Ao navegar pela entrega, não encontrar novas páginas financeiras, dados fictícios, operações simuladas, rótulos de armazenamento apenas local ou assistente simulado apresentados como funcionalidades prontas. O dashboard atual permanece sem antecipar as capacidades da Feature Dashboard financeiro.; CA10: Em largura de até 767px, reconhecer a marca no topo e a navegação principal fixa no rodapé em largura total, com base de 56px mais a área segura, ícones de 24px, alvos de pelo menos 44px, destino ativo e nomes acessíveis mesmo sem legenda visível. Percorrer até o fim da página, focar controles e abrir menus/diálogos: a navegação não encobre ações, mensagens ou foco, e o acesso à conta, configurações, links e saída permanece disponível.; CA11: De 768 a 1024px inclusive, verificar lateral compacta de 72px mais a área segura, marca compacta, alvos de pelo menos 48px e conteúdo ao lado, sem navegação inferior. A partir de 1025px, verificar navegação lateral desktop com recolhimento atual preservado. Em ambas as faixas, comparar contorno de 1px, raio de 16px, margem de 8px, entorno contínuo e cabeçalho transparente com design-input-002, nos temas claro e escuro; em sistema, manter a preferência existente. Navegação, conta, configurações, links, saída e estados de foco/ativo continuam acessíveis.

## Página pública e acesso

### CT-004 — Página inicial atual

Verificação: Como visitante e autenticado, abrir a página pública atual nos dois temas; conferir marca, composição e links/destinos existentes.

Resultado esperado: Identidade FinAI e linguagem aprovada aplicadas sem remover conteúdo funcional, destinos ou permissões existentes.

Origem no requisito: V-Publica: Desdobramento de R1/R2/CA1/CA6/CA8: composição da página inicial atual com identidade FinAI, preservando conteúdo funcional e destinos.; R1: A entrega abrange a página inicial atual, cadastro, login, recuperação e redefinição de senha, confirmação de senha, verificação de e-mail, desafio de dois fatores, dashboard atual, perfil, alteração de senha, aparência, configuração de dois fatores e passkeys, incluindo seus estados e componentes existentes. Essa lista é inventário do código, não comprovação de aceite funcional anterior.; R2: Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega.; CA1: Ao visitar cada superfície de R1 que esteja disponível para o usuário, reconhecer a identidade FinAI na marca, tipografia, paleta e componentes; nas superfícies sem desenho próprio, preservar campos e finalidade com a mesma linguagem visual.; CA8: Executar ações atuais com dados válidos e inválidos, onde aplicável; campos, validações, mensagens, cancelamentos, confirmações e resultados funcionais permanecem equivalentes após a adequação visual. O mesmo vale para restrições de acesso de visitantes e usuários autenticados.

### CT-005 — Cadastro com sucesso e validação

Verificação: Abrir cadastro, tentar dados válidos e inválidos, conferir processamento/erros/resultado e navegação atual; comparar campos e botões com a linguagem da referência.

Resultado esperado: Mesmos campos,validações,mensagens funcionais,destinos e resultados; composição,estados e temas recebem identidade FinAI.

Origem no requisito: V-Acesso: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de cadastro, login, recuperação/redefinição e verificação de e-mail.; R2: Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega.; CA8: Executar ações atuais com dados válidos e inválidos, onde aplicável; campos, validações, mensagens, cancelamentos, confirmações e resultados funcionais permanecem equivalentes após a adequação visual. O mesmo vale para restrições de acesso de visitantes e usuários autenticados.

### CT-006 — Login e alternativas presentes

Verificação: Abrir login, usar credenciais válidas/inválidas, lembrar acesso e links atuais; conferir presença da entrada por passkey e encaminhamento para2FA quando exigido pela conta.

Resultado esperado: Aparência é adequada; login,erros,processamento e alternativas atuais continuam disponíveis e respeitam suas restrições.

Origem no requisito: V-Acesso: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de cadastro, login, recuperação/redefinição e verificação de e-mail.; R2: Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega.; CA8: Executar ações atuais com dados válidos e inválidos, onde aplicável; campos, validações, mensagens, cancelamentos, confirmações e resultados funcionais permanecem equivalentes após a adequação visual. O mesmo vale para restrições de acesso de visitantes e usuários autenticados.

### CT-007 — Solicitação de recuperação

Verificação: Percorrer a solicitação atual com e-mail válido/inválido e observar mensagens de sucesso/falha disponíveis, além do retorno ao login.

Resultado esperado: Campos,links,mensagens e comportamento atual preservados; erros e processamento seguem identidade FinAI.

Origem no requisito: V-Acesso: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de cadastro, login, recuperação/redefinição e verificação de e-mail.; R2: Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega.; CA8: Executar ações atuais com dados válidos e inválidos, onde aplicável; campos, validações, mensagens, cancelamentos, confirmações e resultados funcionais permanecem equivalentes após a adequação visual. O mesmo vale para restrições de acesso de visitantes e usuários autenticados.

### CT-008 — Redefinição de senha

Verificação: Com link de teste utilizável e cenários de rejeição atuais, conferir senha/confirmação, validação e retorno após sucesso.

Resultado esperado: A operação mantém comportamento e validação atuais com os estados visuais adequados; não altera políticas de senha.

Origem no requisito: V-Acesso: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de cadastro, login, recuperação/redefinição e verificação de e-mail.; R2: Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega.; CA8: Executar ações atuais com dados válidos e inválidos, onde aplicável; campos, validações, mensagens, cancelamentos, confirmações e resultados funcionais permanecem equivalentes após a adequação visual. O mesmo vale para restrições de acesso de visitantes e usuários autenticados.

### CT-009 — Verificação de e-mail

Verificação: Com conta no estado atual de confirmação pendente, abrir aviso, reenviar e sair; conferir retorno com estado confirmado conforme o fluxo existente.

Resultado esperado: Orientações,ações e restrições atuais continuam equivalentes, com aparência FinAI e estados de feedback preservados.

Origem no requisito: V-Acesso: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de cadastro, login, recuperação/redefinição e verificação de e-mail.; R2: Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega.; CA8: Executar ações atuais com dados válidos e inválidos, onde aplicável; campos, validações, mensagens, cancelamentos, confirmações e resultados funcionais permanecem equivalentes após a adequação visual. O mesmo vale para restrições de acesso de visitantes e usuários autenticados.

## Perfil e preferências

### CT-010 — Perfil e avisos existentes

Verificação: Com usuário permitido, alterar perfil com entradas válidas/inválidas e verificar avisos/reenvio de confirmação quando aplicáveis ao estado atual.

Resultado esperado: Dados,erros,avisos e sucesso mantêm o comportamento existente; campos e feedback recebem a identidade FinAI.

Origem no requisito: V-Conta: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de perfil, senha, aparência e exclusão de conta.; R2: Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega.; CA8: Executar ações atuais com dados válidos e inválidos, onde aplicável; campos, validações, mensagens, cancelamentos, confirmações e resultados funcionais permanecem equivalentes após a adequação visual. O mesmo vale para restrições de acesso de visitantes e usuários autenticados.

### CT-011 — Alteração de senha

Verificação: Percorrer alteração atual com senha atual/novas informações válidas e inválidas e observar resultados e mensagens.

Resultado esperado: Apenas aparência é alterada; campos,validações,feedback e efeito funcional permanecem iguais.

Origem no requisito: V-Conta: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de perfil, senha, aparência e exclusão de conta.; R2: Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega.; CA8: Executar ações atuais com dados válidos e inválidos, onde aplicável; campos, validações, mensagens, cancelamentos, confirmações e resultados funcionais permanecem equivalentes após a adequação visual. O mesmo vale para restrições de acesso de visitantes e usuários autenticados.

### CT-012 — Escolha de aparência

Verificação: Selecionar claro, escuro e sistema na página atual; conferir cada seleção nas superfícies adaptadas e voltar à aplicação.

Resultado esperado: Três escolhas preservadas; modo aplicado e preferência mantida conforme o comportamento existente.

Origem no requisito: CA3: Selecionar claro, escuro e acompanhar o sistema; cada opção continua disponível e aplica a aparência correspondente. Ao retornar à aplicação, manter a preferência conforme o comportamento existente.; R5: Preservar claro, escuro e acompanhar o sistema. A variante escura é uma adaptação aprovada da identidade fornecida, mantendo hierarquia visual, distinção entre superfícies, leitura dos textos e identificação dos estados. Não reutilizar o tema escuro neutro do starter sem adequação à identidade FinAI.; V-Conta: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de perfil, senha, aparência e exclusão de conta.

### CT-013 — Mudança da preferência do dispositivo

Verificação: Em sistema, alterar a preferência do dispositivo; repetir após selecionar claro e escuro explicitamente.

Resultado esperado: Sistema acompanha a mudança; escolhas explícitas não são substituídas pela preferência do dispositivo.

Origem no requisito: CA4: Com acompanhar o sistema selecionado, alterar a preferência do dispositivo; a aparência acompanha a mudança. Com claro ou escuro explicitamente selecionado, a preferência do dispositivo não substitui a escolha.; R5: Preservar claro, escuro e acompanhar o sistema. A variante escura é uma adaptação aprovada da identidade fornecida, mantendo hierarquia visual, distinção entre superfícies, leitura dos textos e identificação dos estados. Não reutilizar o tema escuro neutro do starter sem adequação à identidade FinAI.; V-Conta: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de perfil, senha, aparência e exclusão de conta.

### CT-014 — Exclusão da conta e cancelamento

Verificação: Com conta de teste, abrir diálogo atual, cancelar/fechar, provocar erro disponível e concluir a confirmação válida; observar estados e foco.

Resultado esperado: Cancelamentos/erro não excluem indevidamente; confirmação válida mantém o efeito existente. Diálogo e estados seguem a identidade FinAI.

Origem no requisito: V-Conta: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de perfil, senha, aparência e exclusão de conta.; R2: Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega.; CA7: Navegar e utilizar formulários, menus e diálogos atuais com mouse e teclado; preservar rótulos, foco visível e estados aplicáveis de hover, ativo, desabilitado e carregamento demonstrados no design ou existentes na aplicação.; CA8: Executar ações atuais com dados válidos e inválidos, onde aplicável; campos, validações, mensagens, cancelamentos, confirmações e resultados funcionais permanecem equivalentes após a adequação visual. O mesmo vale para restrições de acesso de visitantes e usuários autenticados.

## Segurança existente

### CT-015 — Configuração2FA

Verificação: Com contas/estados adequados, percorrer QR,chave manual,confirmaçãoOTP,continuação/cancelamento,carregamento e erros atuais, em claro/escuro.

Resultado esperado: Controles e estados são preservados com identidade FinAI; QR legível no escuro; cancelamentos e erros mantêm seus efeitos atuais.

Origem no requisito: V-Seguranca: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de 2FA, confirmação de senha e passkeys.; R2: Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega.; CA5: No tema escuro, abrir as mesmas superfícies e estados do tema claro; manter conteúdo e ações equivalentes, identidade FinAI, textos legíveis e distinção visual entre superfícies, bordas, foco, erros e demais estados existentes.; CA8: Executar ações atuais com dados válidos e inválidos, onde aplicável; campos, validações, mensagens, cancelamentos, confirmações e resultados funcionais permanecem equivalentes após a adequação visual. O mesmo vale para restrições de acesso de visitantes e usuários autenticados.

### CT-016 — Códigos e desativação2FA

Verificação: Com2FA configurada, conferir apresentação/ações atuais de códigos de recuperação e desativação, incluindo falhas disponíveis.

Resultado esperado: Mesmas operações e permissões; estado e resultados equivalentes com aparência adequada.

Origem no requisito: V-Seguranca: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de 2FA, confirmação de senha e passkeys.; R2: Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega.; CA8: Executar ações atuais com dados válidos e inválidos, onde aplicável; campos, validações, mensagens, cancelamentos, confirmações e resultados funcionais permanecem equivalentes após a adequação visual. O mesmo vale para restrições de acesso de visitantes e usuários autenticados.

### CT-017 — Desafio2FA

Verificação: Entrar com conta que exija2FA e percorrer código válido/inválido e alternativa atual de recuperação.

Resultado esperado: Jornada,campos,erros e resultado de autenticação preservados, com estados visualmente coerentes.

Origem no requisito: V-Seguranca: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de 2FA, confirmação de senha e passkeys.; R2: Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega.; CA8: Executar ações atuais com dados válidos e inválidos, onde aplicável; campos, validações, mensagens, cancelamentos, confirmações e resultados funcionais permanecem equivalentes após a adequação visual. O mesmo vale para restrições de acesso de visitantes e usuários autenticados.

### CT-018 — Confirmação de senha

Verificação: Abrir ação atual que solicite confirmação de senha; usar senha válida/inválida e observar continuidade.

Resultado esperado: Exigência,resultado e erros atuais mantidos, com aparência FinAI e foco utilizável.

Origem no requisito: V-Seguranca: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de 2FA, confirmação de senha e passkeys.; R2: Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega.; CA8: Executar ações atuais com dados válidos e inválidos, onde aplicável; campos, validações, mensagens, cancelamentos, confirmações e resultados funcionais permanecem equivalentes após a adequação visual. O mesmo vale para restrições de acesso de visitantes e usuários autenticados.

### CT-019 — Passkeys sem dados e suporte indisponível

Verificação: Abrir gestão sem passkeys e conferir a alternativa de entrada em navegador suportado e no estado de indisponibilidade existente.

Resultado esperado: Estado vazio e indisponibilidade comunicados como antes; aparência FinAI aplicada sem oferecer recurso funcional novo.

Origem no requisito: V-Seguranca: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de 2FA, confirmação de senha e passkeys.; R2: Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega.; CA8: Executar ações atuais com dados válidos e inválidos, onde aplicável; campos, validações, mensagens, cancelamentos, confirmações e resultados funcionais permanecem equivalentes após a adequação visual. O mesmo vale para restrições de acesso de visitantes e usuários autenticados.

### CT-020 — Registro,listagem e remoção de passkeys

Verificação: Com suporte e dados de teste, registrar,consultar e remover passkey; cancelar remoção e observar estados de carregamento/erro atuais.

Resultado esperado: Ações,resultados e cancelamentos atuais preservados; lista vazia/preenchida,diálogo e feedback seguem a identidade FinAI.

Origem no requisito: V-Seguranca: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de 2FA, confirmação de senha e passkeys.; R2: Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega.; CA7: Navegar e utilizar formulários, menus e diálogos atuais com mouse e teclado; preservar rótulos, foco visível e estados aplicáveis de hover, ativo, desabilitado e carregamento demonstrados no design ou existentes na aplicação.; CA8: Executar ações atuais com dados válidos e inválidos, onde aplicável; campos, validações, mensagens, cancelamentos, confirmações e resultados funcionais permanecem equivalentes após a adequação visual. O mesmo vale para restrições de acesso de visitantes e usuários autenticados.

### CT-021 — Entrada e confirmação por passkey

Verificação: Percorrer a entrada/verificação atuais com sucesso e falha quando suportado e conferir o encaixe no login.

Resultado esperado: Integração entre páginas de acesso e componentes de passkey preservada, sem mudança de permissões ou mecanismo.

Origem no requisito: V-Seguranca: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de 2FA, confirmação de senha e passkeys.; V-Acesso: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de cadastro, login, recuperação/redefinição e verificação de e-mail.; R2: Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega.; CA8: Executar ações atuais com dados válidos e inválidos, onde aplicável; campos, validações, mensagens, cancelamentos, confirmações e resultados funcionais permanecem equivalentes após a adequação visual. O mesmo vale para restrições de acesso de visitantes e usuários autenticados.

## Verificação integrada

### CT-022 — Teclado e estados de controles

Verificação: Percorrer formulários,menus e diálogos atuais com teclado/mouse e conferir rótulos,foco,hover,ativo,desabilitado e carregamento onde aplicáveis.

Resultado esperado: Operações atuais acessíveis pelos mesmos controles, com rótulos e foco visíveis; identidade visual dos estados corresponde à referência e adaptações.

Origem no requisito: CA7: Navegar e utilizar formulários, menus e diálogos atuais com mouse e teclado; preservar rótulos, foco visível e estados aplicáveis de hover, ativo, desabilitado e carregamento demonstrados no design ou existentes na aplicação.; R2: Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega.

### CT-023 — Matriz visual completa

Verificação: Verificar todas as superfícies de R1 e estados atuais aplicáveis nos nove viewports de CA6, no claro e no escuro; incluir página pública, acesso, painel, perfil, senha, aparência, 2FA, confirmações e passkeys. Comparar identidade preservada com design-input-001 e, na estrutura autenticada compartilhada, a composição revisada de design-input-002 — docs/harness/features/1016101-adequacao-visual-do-finai/sources/design-input-002.md. Conferir sistema, áreas seguras, acesso aos controles e integração das páginas com a nova estrutura.

Resultado esperado: Cada tela preserva identidade, conteúdo, operações e acesso aos controles, sem rolagem horizontal da página. A estrutura autenticada aplica barra inferior no celular, lateral compacta no tablet até 1024px e navegação desktop a partir de 1025px, com contorno e raio na área de conteúdo a partir de 768px. Claro e escuro mantêm linguagem FinAI; sistema acompanha a preferência existente. Telas públicas e sem desenho próprio mantêm a linguagem aprovada, sem inserir navegação autenticada onde não existe. Nenhuma superfície ou viewport da matriz é dispensado.

Origem no requisito: R1: A entrega abrange a página inicial atual, cadastro, login, recuperação e redefinição de senha, confirmação de senha, verificação de e-mail, desafio de dois fatores, dashboard atual, perfil, alteração de senha, aparência, configuração de dois fatores e passkeys, incluindo seus estados e componentes existentes. Essa lista é inventário do código, não comprovação de aceite funcional anterior.; CA1: Ao visitar cada superfície de R1 que esteja disponível para o usuário, reconhecer a identidade FinAI na marca, tipografia, paleta e componentes; nas superfícies sem desenho próprio, preservar campos e finalidade com a mesma linguagem visual.; CA2: No tema claro, comparar as estruturas e os componentes aplicáveis com a referência design-input-001 e as alterações compartilhadas de design-input-002, conforme R4 e verificar cores de R3, títulos Georgia, corpo system-ui, hierarquia, espaçamentos, proporções, raios, bordas e estados, sem manter a aparência genérica do starter.; CA5: No tema escuro, abrir as mesmas superfícies e estados do tema claro; manter conteúdo e ações equivalentes, identidade FinAI, textos legíveis e distinção visual entre superfícies, bordas, foco, erros e demais estados existentes.; CA6: Verificar as telas atuais em 360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080; layout e navegação se adaptam sem rolagem horizontal da página, mantendo acesso às operações atuais. Conferir também as transições 767/768px e 1024/1025px, incluindo redimensionamento após recolher a navegação desktop; cada largura aplica o modo de R4 e mantém os destinos e ações atuais disponíveis.; V-Publica: Desdobramento de R1/R2/CA1/CA6/CA8: composição da página inicial atual com identidade FinAI, preservando conteúdo funcional e destinos.; V-Acesso: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de cadastro, login, recuperação/redefinição e verificação de e-mail.; V-Conta: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de perfil, senha, aparência e exclusão de conta.; V-Seguranca: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de 2FA, confirmação de senha e passkeys.; CA10: Em largura de até 767px, reconhecer a marca no topo e a navegação principal fixa no rodapé em largura total, com base de 56px mais a área segura, ícones de 24px, alvos de pelo menos 44px, destino ativo e nomes acessíveis mesmo sem legenda visível. Percorrer até o fim da página, focar controles e abrir menus/diálogos: a navegação não encobre ações, mensagens ou foco, e o acesso à conta, configurações, links e saída permanece disponível.; CA11: De 768 a 1024px inclusive, verificar lateral compacta de 72px mais a área segura, marca compacta, alvos de pelo menos 48px e conteúdo ao lado, sem navegação inferior. A partir de 1025px, verificar navegação lateral desktop com recolhimento atual preservado. Em ambas as faixas, comparar contorno de 1px, raio de 16px, margem de 8px, entorno contínuo e cabeçalho transparente com design-input-002, nos temas claro e escuro; em sistema, manter a preferência existente. Navegação, conta, configurações, links, saída e estados de foco/ativo continuam acessíveis.

### CT-024 — Permissões e ausência de antecipação financeira

Verificação: Como visitante e contas em estados diferentes, tentar caminhos atuais públicos/protegidos e navegar após sair. Conferir painel e menu sem páginas futuras.

Resultado esperado: Mesmas restrições e destinos anteriores; sem novas regras de acesso,sem dados/ações financeiras simuladas,sem destinos Transações/Assistente e sem rótulos de armazenamento local/IA simulada como produto pronto.

Origem no requisito: R2: Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega.; R6: A marca FinAI substitui a identidade visual genérica do starter nas superfícies atuais. Não apresentar rótulos do protótipo que afirmem armazenamento apenas no navegador ou assistente simulado; persistência e IA real serão tratadas pelas Features responsáveis.; R7: A base visual é aceita sobre as telas atuais. Não criar páginas de Transações ou Assistente, formulários financeiros, números demonstrativos ou operações simuladas nesta Feature. As novas telas e suas composições específicas seguem a base nas próximas Features.; CA8: Executar ações atuais com dados válidos e inválidos, onde aplicável; campos, validações, mensagens, cancelamentos, confirmações e resultados funcionais permanecem equivalentes após a adequação visual. O mesmo vale para restrições de acesso de visitantes e usuários autenticados.; CA9: Ao navegar pela entrega, não encontrar novas páginas financeiras, dados fictícios, operações simuladas, rótulos de armazenamento apenas local ou assistente simulado apresentados como funcionalidades prontas. O dashboard atual permanece sem antecipar as capacidades da Feature Dashboard financeiro.

## Revisão do layout compartilhado

### CT-025 — Transições de celular, tablet e desktop

Verificação: No painel e em uma página atual de configurações, recolher a navegação desktop; redimensionar entre 767/768px e 1024/1025px e retornar, nos temas claro e escuro. Navegar até um destino atual, abrir o menu da conta e conferir foco e nome acessível da navegação.

Resultado esperado: 767px aplica barra inferior; 768px aplica lateral compacta; 1024px ainda aplica tablet; 1025px aplica desktop e mantém o recolhimento atual. A mudança de modo não esconde ações, duplica a navegação, troca o destino ativo ou cria rolagem horizontal; menus e foco continuam operáveis.

Origem no requisito: R4: Aplicar a revisão design-input-002 à estrutura autenticada compartilhada: até 767px, marca no topo e navegação principal fixa no rodapé, de largura total, com base de 56px acrescida da área segura inferior e ícones de 24px, alvos de pelo menos 44px, sem legendas visíveis e com nomes acessíveis; de 768 a 1024px inclusive, navegação lateral compacta de 72px acrescida da área segura lateral, marca compacta, alvos de pelo menos 48px e conteúdo ao lado, sem barra inferior; a partir de 1025px, navegação lateral desktop, preservando o recolhimento e os destinos atuais. A partir de 768px, apresentar o conteúdo em superfície com fundo de trabalho, contorno de 1px, raio de 16px e margem de 8px, com a navegação integrada ao entorno e cabeçalho transparente conforme a referência. Reservar espaço para navegação e áreas seguras, sem encobrir conteúdo, foco, mensagens ou controles. Preservar acesso ao menu da conta, configurações, links e saída em todas as larguras, adaptando sua apresentação quando o protótipo esconder o rodapé lateral. Não transportar destinos financeiros futuros para as telas atuais.; CA6: Verificar as telas atuais em 360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080; layout e navegação se adaptam sem rolagem horizontal da página, mantendo acesso às operações atuais. Conferir também as transições 767/768px e 1024/1025px, incluindo redimensionamento após recolher a navegação desktop; cada largura aplica o modo de R4 e mantém os destinos e ações atuais disponíveis.; CA7: Navegar e utilizar formulários, menus e diálogos atuais com mouse e teclado; preservar rótulos, foco visível e estados aplicáveis de hover, ativo, desabilitado e carregamento demonstrados no design ou existentes na aplicação.; CA10: Em largura de até 767px, reconhecer a marca no topo e a navegação principal fixa no rodapé em largura total, com base de 56px mais a área segura, ícones de 24px, alvos de pelo menos 44px, destino ativo e nomes acessíveis mesmo sem legenda visível. Percorrer até o fim da página, focar controles e abrir menus/diálogos: a navegação não encobre ações, mensagens ou foco, e o acesso à conta, configurações, links e saída permanece disponível.; CA11: De 768 a 1024px inclusive, verificar lateral compacta de 72px mais a área segura, marca compacta, alvos de pelo menos 48px e conteúdo ao lado, sem navegação inferior. A partir de 1025px, verificar navegação lateral desktop com recolhimento atual preservado. Em ambas as faixas, comparar contorno de 1px, raio de 16px, margem de 8px, entorno contínuo e cabeçalho transparente com design-input-002, nos temas claro e escuro; em sistema, manter a preferência existente. Navegação, conta, configurações, links, saída e estados de foco/ativo continuam acessíveis.

### CT-026 — Barra inferior, áreas seguras e acesso à conta no celular

Verificação: Em 360×800, 390×844, 430×932 e 600×960, comparar a navegação com design-input-002. Conferir base de 56px acrescida da área segura inferior, largura total, ícones de 24px e alvos de pelo menos 44px. Rolar até o último controle da página, percorrer o foco, abrir menus e diálogos existentes, incluindo mensagens disponíveis, e acessar conta, configurações, links e saída. Repetir com área segura inferior/lateral aplicável em dispositivo ou emulação documentada, nos temas claro e escuro.

Resultado esperado: Marca no topo e barra fixa no rodapé correspondem à referência; ícones sem legenda visual mantêm nome acessível, ativo e foco visíveis. Conteúdo final, mensagens, controles e foco permanecem visíveis e alcançáveis acima da barra e da área segura. Conta, configurações, links e saída continuam disponíveis, inclusive quando o protótipo esconde o rodapé lateral. Cancelar/fechar menus ou diálogos mantém seu comportamento atual.

Origem no requisito: R2: Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega.; R4: Aplicar a revisão design-input-002 à estrutura autenticada compartilhada: até 767px, marca no topo e navegação principal fixa no rodapé, de largura total, com base de 56px acrescida da área segura inferior e ícones de 24px, alvos de pelo menos 44px, sem legendas visíveis e com nomes acessíveis; de 768 a 1024px inclusive, navegação lateral compacta de 72px acrescida da área segura lateral, marca compacta, alvos de pelo menos 48px e conteúdo ao lado, sem barra inferior; a partir de 1025px, navegação lateral desktop, preservando o recolhimento e os destinos atuais. A partir de 768px, apresentar o conteúdo em superfície com fundo de trabalho, contorno de 1px, raio de 16px e margem de 8px, com a navegação integrada ao entorno e cabeçalho transparente conforme a referência. Reservar espaço para navegação e áreas seguras, sem encobrir conteúdo, foco, mensagens ou controles. Preservar acesso ao menu da conta, configurações, links e saída em todas as larguras, adaptando sua apresentação quando o protótipo esconder o rodapé lateral. Não transportar destinos financeiros futuros para as telas atuais.; R5: Preservar claro, escuro e acompanhar o sistema. A variante escura é uma adaptação aprovada da identidade fornecida, mantendo hierarquia visual, distinção entre superfícies, leitura dos textos e identificação dos estados. Não reutilizar o tema escuro neutro do starter sem adequação à identidade FinAI.; CA5: No tema escuro, abrir as mesmas superfícies e estados do tema claro; manter conteúdo e ações equivalentes, identidade FinAI, textos legíveis e distinção visual entre superfícies, bordas, foco, erros e demais estados existentes.; CA7: Navegar e utilizar formulários, menus e diálogos atuais com mouse e teclado; preservar rótulos, foco visível e estados aplicáveis de hover, ativo, desabilitado e carregamento demonstrados no design ou existentes na aplicação.; CA8: Executar ações atuais com dados válidos e inválidos, onde aplicável; campos, validações, mensagens, cancelamentos, confirmações e resultados funcionais permanecem equivalentes após a adequação visual. O mesmo vale para restrições de acesso de visitantes e usuários autenticados.; CA10: Em largura de até 767px, reconhecer a marca no topo e a navegação principal fixa no rodapé em largura total, com base de 56px mais a área segura, ícones de 24px, alvos de pelo menos 44px, destino ativo e nomes acessíveis mesmo sem legenda visível. Percorrer até o fim da página, focar controles e abrir menus/diálogos: a navegação não encobre ações, mensagens ou foco, e o acesso à conta, configurações, links e saída permanece disponível.

### CT-027 — Lateral compacta do tablet e contorno do conteúdo

Verificação: Em 820×1180 e 1024×768, comparar design-input-002 com a lateral de 72px mais a área segura, marca compacta, ícones e alvos de pelo menos 48px. Conferir conteúdo ao lado e acesso aos controles com rolagem vertical quando necessária. Em tablet e em 1366×768, 1440×900 e 1920×1080, comparar contorno de 1px, raio de 16px, margem de 8px, entorno contínuo e cabeçalho transparente. Abrir painel, configurações, menus e conferir navegação recolhida/expandida no desktop, nos temas claro e escuro.

Resultado esperado: Tablet mantém lateral compacta sem barra inferior e sem sobreposição do conteúdo; desktop mantém navegação lateral e recolhimento existentes. A superfície do conteúdo e sua separação do entorno correspondem ao novo design. Navegação, marca, conta, configurações, links, saída, foco e ativo permanecem acessíveis nos dois temas, sem alterar dados ou operações.

Origem no requisito: R2: Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega.; R3: A referência clara usa fundo #F5F7F8, superfícies brancas, texto #172622, texto secundário #52615C, verde principal #145C46, verde positivo #146345, vermelho negativo #A12B36, bordas #D6DFDB e destaque suave #E4F0E9. Preservar a hierarquia do design: títulos de destaque em Georgia e corpo em system-ui; controles com raio de 8px e painéis com 16px; espaçamento, bordas, sombras, estados e proporções conforme o pacote.; R4: Aplicar a revisão design-input-002 à estrutura autenticada compartilhada: até 767px, marca no topo e navegação principal fixa no rodapé, de largura total, com base de 56px acrescida da área segura inferior e ícones de 24px, alvos de pelo menos 44px, sem legendas visíveis e com nomes acessíveis; de 768 a 1024px inclusive, navegação lateral compacta de 72px acrescida da área segura lateral, marca compacta, alvos de pelo menos 48px e conteúdo ao lado, sem barra inferior; a partir de 1025px, navegação lateral desktop, preservando o recolhimento e os destinos atuais. A partir de 768px, apresentar o conteúdo em superfície com fundo de trabalho, contorno de 1px, raio de 16px e margem de 8px, com a navegação integrada ao entorno e cabeçalho transparente conforme a referência. Reservar espaço para navegação e áreas seguras, sem encobrir conteúdo, foco, mensagens ou controles. Preservar acesso ao menu da conta, configurações, links e saída em todas as larguras, adaptando sua apresentação quando o protótipo esconder o rodapé lateral. Não transportar destinos financeiros futuros para as telas atuais.; R5: Preservar claro, escuro e acompanhar o sistema. A variante escura é uma adaptação aprovada da identidade fornecida, mantendo hierarquia visual, distinção entre superfícies, leitura dos textos e identificação dos estados. Não reutilizar o tema escuro neutro do starter sem adequação à identidade FinAI.; CA2: No tema claro, comparar as estruturas e os componentes aplicáveis com a referência design-input-001 e as alterações compartilhadas de design-input-002, conforme R4 e verificar cores de R3, títulos Georgia, corpo system-ui, hierarquia, espaçamentos, proporções, raios, bordas e estados, sem manter a aparência genérica do starter.; CA5: No tema escuro, abrir as mesmas superfícies e estados do tema claro; manter conteúdo e ações equivalentes, identidade FinAI, textos legíveis e distinção visual entre superfícies, bordas, foco, erros e demais estados existentes.; CA6: Verificar as telas atuais em 360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080; layout e navegação se adaptam sem rolagem horizontal da página, mantendo acesso às operações atuais. Conferir também as transições 767/768px e 1024/1025px, incluindo redimensionamento após recolher a navegação desktop; cada largura aplica o modo de R4 e mantém os destinos e ações atuais disponíveis.; CA7: Navegar e utilizar formulários, menus e diálogos atuais com mouse e teclado; preservar rótulos, foco visível e estados aplicáveis de hover, ativo, desabilitado e carregamento demonstrados no design ou existentes na aplicação.; CA11: De 768 a 1024px inclusive, verificar lateral compacta de 72px mais a área segura, marca compacta, alvos de pelo menos 48px e conteúdo ao lado, sem navegação inferior. A partir de 1025px, verificar navegação lateral desktop com recolhimento atual preservado. Em ambas as faixas, comparar contorno de 1px, raio de 16px, margem de 8px, entorno contínuo e cabeçalho transparente com design-input-002, nos temas claro e escuro; em sistema, manter a preferência existente. Navegação, conta, configurações, links, saída e estados de foco/ativo continuam acessíveis.
