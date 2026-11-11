# [QA] [WEB] [USUARIO] Adequação visual do FinAI

- Redmine: `#1016117`
- Tipo: `QA`
- Tracker: Deliverable (`5`)
- Item pai: `#1016101`
- Estimativa: `1.5h`

## Descrição

## Objetivo

Verificar a adequação visual de todas as telas atuais à identidade FinAI, nos temas e larguras aprovados, preservando operações,estados e permissões existentes.

## Jornadas integradas

- Marca e linguagem clara: Comparar painel e componentes compartilhados atuais com design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md (:root,.brand,.btn,campos e diálogos). Conferir os valores de R3 e telas consumidoras. Resultado esperado: Marca FinAI substitui a do starter; fundo #F5F7F8/superfícies brancas, paleta de R3, títulos Georgia/corpo system-ui, controles8px/painéis16px e hierarquia/estados aplicáveis correspondem à referência.
- Variante escura: Abrir cada tela/estado atual no escuro e compará-lo ao claro e à linguagem FinAI, incluindo avisos, erros, menus, diálogos e QR. Resultado esperado: Conteúdo e ações equivalentes; superfícies,textos,bordas,foco e estados são distinguíveis e legíveis. Tema escuro do starter foi adequado, e QR permanece legível.
- Navegação desktop/tablet/celular: Nos viewports aplicáveis de 360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080, navegar por painel, configurações e menu usuário, usando mouse e teclado. Referência .app,.sidebar,.topbar e media queries. Resultado esperado: Geometria desktop e reorganização superior em telas menores preservam hierarquia e destinos atuais; ativo/foco visíveis e ações disponíveis, sem novos destinos financeiros.
- Página inicial atual: Como visitante e autenticado, abrir a página pública atual nos dois temas; conferir marca, composição e links/destinos existentes. Resultado esperado: Identidade FinAI e linguagem aprovada aplicadas sem remover conteúdo funcional, destinos ou permissões existentes.
- Cadastro com sucesso e validação: Abrir cadastro, tentar dados válidos e inválidos, conferir processamento/erros/resultado e navegação atual; comparar campos e botões com a linguagem da referência. Resultado esperado: Mesmos campos,validações,mensagens funcionais,destinos e resultados; composição,estados e temas recebem identidade FinAI.
- Login e alternativas presentes: Abrir login, usar credenciais válidas/inválidas, lembrar acesso e links atuais; conferir presença da entrada por passkey e encaminhamento para2FA quando exigido pela conta. Resultado esperado: Aparência é adequada; login,erros,processamento e alternativas atuais continuam disponíveis e respeitam suas restrições.
- Solicitação de recuperação: Percorrer a solicitação atual com e-mail válido/inválido e observar mensagens de sucesso/falha disponíveis, além do retorno ao login. Resultado esperado: Campos,links,mensagens e comportamento atual preservados; erros e processamento seguem identidade FinAI.
- Redefinição de senha: Com link de teste utilizável e cenários de rejeição atuais, conferir senha/confirmação, validação e retorno após sucesso. Resultado esperado: A operação mantém comportamento e validação atuais com os estados visuais adequados; não altera políticas de senha.
- Verificação de e-mail: Com conta no estado atual de confirmação pendente, abrir aviso, reenviar e sair; conferir retorno com estado confirmado conforme o fluxo existente. Resultado esperado: Orientações,ações e restrições atuais continuam equivalentes, com aparência FinAI e estados de feedback preservados.
- Perfil e avisos existentes: Com usuário permitido, alterar perfil com entradas válidas/inválidas e verificar avisos/reenvio de confirmação quando aplicáveis ao estado atual. Resultado esperado: Dados,erros,avisos e sucesso mantêm o comportamento existente; campos e feedback recebem a identidade FinAI.
- Alteração de senha: Percorrer alteração atual com senha atual/novas informações válidas e inválidas e observar resultados e mensagens. Resultado esperado: Apenas aparência é alterada; campos,validações,feedback e efeito funcional permanecem iguais.
- Escolha de aparência: Selecionar claro, escuro e sistema na página atual; conferir cada seleção nas superfícies adaptadas e voltar à aplicação. Resultado esperado: Três escolhas preservadas; modo aplicado e preferência mantida conforme o comportamento existente.
- Mudança da preferência do dispositivo: Em sistema, alterar a preferência do dispositivo; repetir após selecionar claro e escuro explicitamente. Resultado esperado: Sistema acompanha a mudança; escolhas explícitas não são substituídas pela preferência do dispositivo.
- Exclusão da conta e cancelamento: Com conta de teste, abrir diálogo atual, cancelar/fechar, provocar erro disponível e concluir a confirmação válida; observar estados e foco. Resultado esperado: Cancelamentos/erro não excluem indevidamente; confirmação válida mantém o efeito existente. Diálogo e estados seguem a identidade FinAI.
- Configuração2FA: Com contas/estados adequados, percorrer QR,chave manual,confirmaçãoOTP,continuação/cancelamento,carregamento e erros atuais, em claro/escuro. Resultado esperado: Controles e estados são preservados com identidade FinAI; QR legível no escuro; cancelamentos e erros mantêm seus efeitos atuais.
- Códigos e desativação2FA: Com2FA configurada, conferir apresentação/ações atuais de códigos de recuperação e desativação, incluindo falhas disponíveis. Resultado esperado: Mesmas operações e permissões; estado e resultados equivalentes com aparência adequada.
- Desafio2FA: Entrar com conta que exija2FA e percorrer código válido/inválido e alternativa atual de recuperação. Resultado esperado: Jornada,campos,erros e resultado de autenticação preservados, com estados visualmente coerentes.
- Confirmação de senha: Abrir ação atual que solicite confirmação de senha; usar senha válida/inválida e observar continuidade. Resultado esperado: Exigência,resultado e erros atuais mantidos, com aparência FinAI e foco utilizável.
- Passkeys sem dados e suporte indisponível: Abrir gestão sem passkeys e conferir a alternativa de entrada em navegador suportado e no estado de indisponibilidade existente. Resultado esperado: Estado vazio e indisponibilidade comunicados como antes; aparência FinAI aplicada sem oferecer recurso funcional novo.
- Registro,listagem e remoção de passkeys: Com suporte e dados de teste, registrar,consultar e remover passkey; cancelar remoção e observar estados de carregamento/erro atuais. Resultado esperado: Ações,resultados e cancelamentos atuais preservados; lista vazia/preenchida,diálogo e feedback seguem a identidade FinAI.
- Entrada e confirmação por passkey: Percorrer a entrada/verificação atuais com sucesso e falha quando suportado e conferir o encaixe no login. Resultado esperado: Integração entre páginas de acesso e componentes de passkey preservada, sem mudança de permissões ou mecanismo.
- Teclado e estados de controles: Percorrer formulários,menus e diálogos atuais com teclado/mouse e conferir rótulos,foco,hover,ativo,desabilitado e carregamento onde aplicáveis. Resultado esperado: Operações atuais acessíveis pelos mesmos controles, com rótulos e foco visíveis; identidade visual dos estados corresponde à referência e adaptações.
- Matriz visual completa: Verificar todas as superfícies de R1 e estados existentes aplicáveis em 360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080, tanto no claro quanto no escuro; incluir página pública,acesso,painel,perfil,senha,aparência,2FA,confirmações e passkeys. Comparar identidade clara com design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md e adaptação escura aprovada. Resultado esperado: Cada tela preserva identidade,composição aplicável,conteúdo e acesso aos controles, sem rolagem horizontal da página. As composições sem desenho próprio seguem a linguagem FinAI; nenhum viewport ou superfície é dispensado.
- Permissões e ausência de antecipação financeira: Como visitante e contas em estados diferentes, tentar caminhos atuais públicos/protegidos e navegar após sair. Conferir painel e menu sem páginas futuras. Resultado esperado: Mesmas restrições e destinos anteriores; sem novas regras de acesso,sem dados/ações financeiras simuladas,sem destinos Transações/Assistente e sem rótulos de armazenamento local/IA simulada como produto pronto.

## Regras e permissões

- Manter todos os campos,validações,mensagens funcionais,operações,permissões,destinos e preferências existentes; esta Feature não implementa novas regras de acesso ou financeiras.
- Preservar claro,escuro e acompanhar o sistema, incluindo persistência e reação ao dispositivo.
- Usar a referência clara fornecida e a adaptação escura aprovada,com a matriz completa de noveviewports e todas as superfícies atuais.

## Impactos relacionados

- Aparência dos componentes compartilhados atravessa todas as telas; conferir integração entre base,navegação,páginas públicas,acesso e configurações.
- Login e passkeys compartilham uma superfície; confirmar a integração com os desafios2FA e confirmação de senha existentes.
- O dashboard atual continua com sua finalidade anterior,sem antecipar números e operações financeiras.

## Critérios de conclusão

- Executar CT-001 a CT-024 do documento Condições de teste, registrar resultado observado e evidência por condição e indicar impedimentos ou desvios reproduzíveis sem declarar aprovação de condição não executada.
- Conferir conjuntamente as cinco entregas DEV, a matriz completa,estados e preservação das jornadas, sem reduzir a cobertura por causa da estimativa.
- Manter o documento de condições da revisão aprovada associado a esta QA e registrar os resultados da verificação.

## Referências

Item pai Redmine #1016101; regras/critérios R1, R2, R3, R4, R5, R6, R7, CA1, CA2, CA3, CA4, CA5, CA6, CA7, CA8, CA9, V-Publica, V-Acesso, V-Conta, V-Seguranca.

<!-- project-slices-child:9e432c5673bd2629655031b04f7bcb870bc37f0ae57ab13fb7f77551d07cb9e2 -->

## Relações

- `#1016112` blocks `#1016117`
- `#1016113` blocks `#1016117`
- `#1016114` blocks `#1016117`
- `#1016115` blocks `#1016117`
- `#1016116` blocks `#1016117`
