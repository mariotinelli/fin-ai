# Prévia completa — Adequação visual do FinAI

Revisão 002, ainda não aprovada. Uma decisão do tech lead cobre a decomposição, as condições de teste e somente as publicações descritas aqui. Não houve criação ou alteração de issues.

## Entregas e estimativas

Todos os títulos DEV abaixo são prefixados por [DEV] [WEB] [USUARIO] Adequação visual do FinAI - .

| # | Entrega | Esforço | Bloqueio de início |
| --- | --- | --- | --- |
| 1 | Identidade e temas no painel atual | 2h | Nenhum |
| 2 | Estrutura e navegação responsiva atuais | 2h | Nenhum |
| 3 | Página inicial e jornadas de acesso | 2h | Nenhum |
| 4 | Perfil, senha e aparência | 2h | Nenhum |
| 5 | Dois fatores e passkeys | 2h | Nenhum |
| QA | [QA] [WEB] [USUARIO] Adequação visual do FinAI | 1,5h | As cinco entregas DEV |

Total: **10h DEV + 1,5h QA = 11,5h**. Estimativas são esforço, não prazo de calendário.

A QA de 1,5h é correção explícita de Mário Tinelli nesta conversa, preservando no histórico as duas avaliações independentes de 8h. A cobertura não foi reduzida. Os cinco DEV foram corrigidos explicitamente por Mário Tinelli para 2h cada, substituindo a primeira estimativa de 22,5h DEV. A análise independente e os valores anteriores permanecem no histórico; o novo total é calibração do tech lead, sem redução de conteúdo ou cobertura.

## Integração e relações

A ordem preferida é identidade, estrutura e composições de páginas. Layouts e variáveis já existentes permitem iniciar os DEV sem bloqueio técnico obrigatório entre eles; para concluir, integrar identidade/temas e estrutura conforme as dependências nomeadas em cada descrição. Não serão criadas arestas nativas por simples preferência de ordem.

Cada um dos cinco DEV bloqueia a QA integrada, usando relação nativa blocks. Nenhum bloqueio externo adicional é necessário para esta primeira Feature. As Features financeiras futuras continuam dependendo da adequação visual implementada e verificada, sem antecipar suas telas.

## Campos e operações autorizáveis

- Pai nativo: #1016101, [WEB] [USUARIO] Adequação visual do FinAI. Estado atual New permanece preservado.
- Criar cinco filhas DEV no tracker Task (4) e uma filha QA no tracker Deliverable (5).
- Projeto FinAi (65224); versão Sprint 1 (20355) herdada; sem categoria, responsável ou datas.
- Todas as filhas começam em New (1), prioridade Normal (4), com estimated_hours apresentado nesta prévia.
- Criar cinco relações blocks, de cada novo DEV para a nova QA. Os extremos serão exclusivamente os IDs devolvidos para estas seis criações.
- Gerar da revisão aprovada o documento Condições de teste, fazer upload e anexá-lo somente à nova QA, preservando os demais campos e anexos.
- Nenhuma filha existente: o pai foi consultado com children e retornou lista vazia. Nada para adotar ou excluir. Nenhuma task antiga é contexto ou alvo.
- Descrições funcionais completas abaixo serão preservadas. Na preparação após o consentimento, o helper acrescenta apenas seus marcadores de recuperação e vincula metadados da aprovação, documento e IDs retornados; isso não autoriza mudança material de conteúdo ou nova confirmação equivalente.

## Documento de condições incluído nesta decisão

- Formato: DOCX obrigatório, com complemento Markdown legível.
- Arquivo final: slices/condicoes-teste-r002.docx; complemento: slices/condicoes-teste-r002.md.
- Destino: [QA] [WEB] [USUARIO] Adequação visual do FinAI, criada por esta publicação.
- Fonte: as 24 condições integrais desta revisão, com seus IDs e vínculos ao requisito. Não haverá edição de conteúdo ao gerar o Word.
- Conforme o contrato da skill, o arquivo oficial é gerado após o consentimento; o helper vincula o hash dos bytes gerados ao plano e verifica o anexo no readback. A aprovação desta fonte também autoriza sua geração e associação à QA; diferenças de conteúdo exigem nova prévia.

## Descrições completas e campos por filha

### [DEV] [WEB] [USUARIO] Adequação visual do FinAI - Identidade e temas no painel atual

```json
{
  "project_id": 65224,
  "parent_issue_id": 1016101,
  "tracker_id": 4,
  "status_id": 1,
  "subject": "[DEV] [WEB] [USUARIO] Adequação visual do FinAI - Identidade e temas no painel atual",
  "assigned_to_id": null,
  "start_date": null,
  "due_date": null,
  "estimated_hours": 2,
  "priority_id": 4,
  "fixed_version_id": 20355
}
```

## Entrega

Aplicar a marca e a identidade FinAI aos componentes compartilhados e ao dashboard atual, preservando os mecanismos existentes de aparência. A base atual é neutra e ainda contém a marca do starter; esta entrega deve produzir uma base visual inspecionável em claro, escuro e sistema.

## Escopo e limites

Responsável pela aparência compartilhada: marca, tipografia, paleta, raios, bordas, sombras, controles e seus estados. A composição da navegação pertence à entrega de estrutura; as composições particulares das outras telas pertencem às entregas correspondentes. Não transformar o dashboard placeholder em dashboard financeiro.

## Critérios de aceite

- No painel atual e nos componentes compartilhados, apresentar marca FinAI e, no claro, fundo #F5F7F8, superfícies brancas, texto #172622, secundário #52615C, principal #145C46, positivo #146345, negativo #A12B36, bordas #D6DFDB e destaque #E4F0E9, títulos Georgia, corpo system-ui, controles com raio8px e painéis16px; preservar proporções, espaçamentos e estados aplicáveis da referência.
- No escuro, adaptar fundos, superfícies, bordas, textos e estados à identidade FinAI com leitura e distinção visual, sem conservar a aparência neutra do starter.
- Manter claro, escuro e acompanhar o sistema, preferência persistida conforme comportamento atual e reação às mudanças do dispositivo somente quando sistema estiver selecionado.
- Aplicar linguagem comum de hover, foco, ativo, desabilitado, carregamento, erro e feedback aos componentes existentes, preservando os significados e interações.
- O painel continua sem números ou operações financeiras novas, e a base não apresenta rótulos de armazenamento apenas local ou assistente simulado.
- Nas superfícies desta entrega, conferir os nove viewports (360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080), temas claro e escuro, estados aplicáveis e ausência de rolagem horizontal da página; manter acesso às ações atuais, rótulos e foco visível.

## Dependências

Pode iniciar com a base atual. Fornece identidade e aparência compartilhada às entregas Estrutura e navegação responsiva atuais, Página inicial e jornadas de acesso, Perfil, senha e aparência e Dois fatores e passkeys. A aceitação desta base é demonstrada no painel atual; a QA conjunta verifica a aplicação em todas as composições.

## Referências

Item pai Redmine #1016101; regras/critérios R1, R2, R3, R5, R6, CA1, CA2, CA5, CA7.

- design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; :root, .brand, .btn, campos, diálogos, cores/tipografia; #overview como referência de linguagem, sem transportar suas capacidades futuras
- Adaptações aprovadas: todas as telas atuais, claro/escuro/sistema preservados; telas futuras nas próximas Features.


### [DEV] [WEB] [USUARIO] Adequação visual do FinAI - Estrutura e navegação responsiva atuais

```json
{
  "project_id": 65224,
  "parent_issue_id": 1016101,
  "tracker_id": 4,
  "status_id": 1,
  "subject": "[DEV] [WEB] [USUARIO] Adequação visual do FinAI - Estrutura e navegação responsiva atuais",
  "assigned_to_id": null,
  "start_date": null,
  "due_date": null,
  "estimated_hours": 2,
  "priority_id": 4,
  "fixed_version_id": 20355
}
```

## Entrega

Adequar estrutura, cabeçalho, navegação e menu do usuário da área autenticada à composição FinAI responsiva, mantendo os destinos atualmente disponíveis. A sidebar e o menu móvel atuais diferem da geometria e organização superior da referência.

## Escopo e limites

Responsável pela disposição compartilhada e adaptações por largura, sem redefinir marca ou tema. Não criar destinos Transações/Assistente nem números, formulários ou operações financeiras.

## Critérios de aceite

- No desktop, apresentar geometria compatível com sidebar240px, cabeçalho80px e conteúdo da referência nos espaços aplicáveis; em larguras intermediárias e celulares, reorganizar a navegação no topo conforme o design.
- Manter acesso aos destinos atuais, configurações, menu do usuário e saída, com indicação do destino ativo onde aplicável. Não criar links para páginas futuras.
- Integrar a identidade e os temas fornecidos por Identidade e temas no painel atual, mantendo conteúdo e ações equivalentes entre claro e escuro.
- Os caminhos e restrições de acesso existentes permanecem iguais; navegação e menus continuam utilizáveis por teclado com foco visível.
- Nas superfícies desta entrega, conferir os nove viewports (360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080), temas claro e escuro, estados aplicáveis e ausência de rolagem horizontal da página; manter acesso às ações atuais, rótulos e foco visível.

## Dependências

Pode iniciar com a estrutura atual e a referência. Para concluir o aceite visual, integrar Identidade e temas no painel atual. As composições de acesso e configurações integram esta estrutura quando aplicável, sem bloqueio técnico de início entre essas entregas.

## Referências

Item pai Redmine #1016101; regras/critérios R1, R2, R4, R7, CA1, CA6, CA7, CA9.

- design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; .app, .sidebar, .topbar, navegação, main e @media(767/1023/1200/1440)
- Adaptações aprovadas: todas as telas atuais, claro/escuro/sistema preservados; telas futuras nas próximas Features.


### [DEV] [WEB] [USUARIO] Adequação visual do FinAI - Página inicial e jornadas de acesso

```json
{
  "project_id": 65224,
  "parent_issue_id": 1016101,
  "tracker_id": 4,
  "status_id": 1,
  "subject": "[DEV] [WEB] [USUARIO] Adequação visual do FinAI - Página inicial e jornadas de acesso",
  "assigned_to_id": null,
  "start_date": null,
  "due_date": null,
  "estimated_hours": 2,
  "priority_id": 4,
  "fixed_version_id": 20355
}
```

## Entrega

Adequar a página pública atual e as telas de cadastro, login, solicitação de recuperação, redefinição e confirmação de e-mail à identidade FinAI, preservando seu conteúdo funcional e suas ações. Aplicar a linguagem de formulário da referência onde não existe composição própria dessas telas.

## Escopo e limites

A composição e estados destas páginas pertencem a esta entrega. Preservar a presença/encaixe da entrada por passkey no login; os estados próprios de passkeys, 2FA e confirmação de senha pertencem a Dois fatores e passkeys. Não alterar políticas de acesso, campos, validações ou mensagens funcionais.

## Critérios de aceite

- Página pública, cadastro, login, recuperação, redefinição e verificação de e-mail apresentam marca, títulos, campos, botões, links e espaçamento coerentes com FinAI, sem identidade visual genérica do starter.
- As telas sem composição própria do ZIP usam a mesma linguagem visual, preservando campos, finalidade e destinos.
- Com dados válidos e inválidos, estados de processamento, mensagens de erro/sucesso e reenvio, manter o comportamento funcional existente e aplicar o visual correspondente.
- Os caminhos de cadastro/login/recuperação/retorno e a presença das alternativas atuais de autenticação continuam disponíveis; visitantes e autenticados mantêm as restrições atuais.
- Conferir as páginas nos temas claro e escuro integrados à base; o modo sistema continua utilizando a preferência vigente.
- Nas superfícies desta entrega, conferir os nove viewports (360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080), temas claro e escuro, estados aplicáveis e ausência de rolagem horizontal da página; manter acesso às ações atuais, rótulos e foco visível.

## Dependências

Pode iniciar a composição das páginas atuais. Para concluir, integrar Identidade e temas no painel atual e, onde houver navegação autenticada, Estrutura e navegação responsiva atuais. Integrar o encaixe da entrada por passkey com Dois fatores e passkeys, sem relação nativa de bloqueio de início.

## Referências

Item pai Redmine #1016101; regras/critérios R1, R2, R3, R5, R6, CA1, CA2, CA5, CA6, CA7, CA8, V-Publica, V-Acesso.

- design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; .brand, títulos, campos, botões e mensagens do index.html; adaptação aprovada para página inicial e telas de acesso sem desenho específico
- Adaptações aprovadas: todas as telas atuais, claro/escuro/sistema preservados; telas futuras nas próximas Features.


### [DEV] [WEB] [USUARIO] Adequação visual do FinAI - Perfil, senha e aparência

```json
{
  "project_id": 65224,
  "parent_issue_id": 1016101,
  "tracker_id": 4,
  "status_id": 1,
  "subject": "[DEV] [WEB] [USUARIO] Adequação visual do FinAI - Perfil, senha e aparência",
  "assigned_to_id": null,
  "start_date": null,
  "due_date": null,
  "estimated_hours": 2,
  "priority_id": 4,
  "fixed_version_id": 20355
}
```

## Entrega

Adequar perfil, alteração de senha, preferência de aparência e o diálogo atual de exclusão da conta à identidade FinAI. Reutilizar as operações e os componentes atuais, preservando validações, feedback e confirmação/cancelamento.

## Escopo e limites

Não alterar dados, regras de senha, permissões ou o efeito de exclusão. Esta entrega possui a composição das páginas de perfil/senha/aparência; o mecanismo e a aparência compartilhada dos temas vêm de Identidade e temas no painel atual.

## Critérios de aceite

- Perfil, formulário de senha, página de aparência e diálogo de exclusão usam a paleta, tipografia, hierarquia, campos, botões, erros e superfícies FinAI.
- Alterar perfil e senha com entradas válidas/inválidas mantém resultados e mensagens funcionais; avisos de verificação de e-mail e reenvio presentes no perfil permanecem quando aplicáveis.
- Excluir a conta continua exigindo a confirmação existente; cancelar/fechar preserva a conta; erro e sucesso mantêm seu comportamento atual com aparência adequada.
- Claro, escuro e acompanhar o sistema continuam selecionáveis; retornar à aplicação conserva preferência, e mudança do dispositivo altera a aparência apenas em sistema.
- Manter navegação entre configurações e acesso às ações atuais sem criar novas regras de confirmação de e-mail ou autenticação.
- Nas superfícies desta entrega, conferir os nove viewports (360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080), temas claro e escuro, estados aplicáveis e ausência de rolagem horizontal da página; manter acesso às ações atuais, rótulos e foco visível.

## Dependências

Pode iniciar a adequação das páginas atuais. Para concluir o aceite, integrar Identidade e temas no painel atual e Estrutura e navegação responsiva atuais. A preservação funcional não depende de implementar a futura Feature Acesso à conta pessoal.

## Referências

Item pai Redmine #1016101; regras/critérios R1, R2, R3, R5, CA1, CA2, CA3, CA4, CA5, CA6, CA7, CA8, V-Conta.

- design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; .btn, inputs, mensagens, dialog e tokens; adaptação aprovada para perfil/configurações sem composição específica
- Adaptações aprovadas: todas as telas atuais, claro/escuro/sistema preservados; telas futuras nas próximas Features.


### [DEV] [WEB] [USUARIO] Adequação visual do FinAI - Dois fatores e passkeys

```json
{
  "project_id": 65224,
  "parent_issue_id": 1016101,
  "tracker_id": 4,
  "status_id": 1,
  "subject": "[DEV] [WEB] [USUARIO] Adequação visual do FinAI - Dois fatores e passkeys",
  "assigned_to_id": null,
  "start_date": null,
  "due_date": null,
  "estimated_hours": 2,
  "priority_id": 4,
  "fixed_version_id": 20355
}
```

## Entrega

Adequar configuração e desafio de dois fatores, confirmação de senha e gestão/entrada/confirmação de passkeys, incluindo os estados e diálogos atuais, à identidade FinAI. Preservar os mecanismos de autenticação existentes.

## Escopo e limites

Esta entrega possui composições e estados específicos de QR/chave manual/OTP/códigos, confirmação de senha e passkeys. Não adicionar métodos de autenticação, trocar validações ou redesenhar o restante do login; sua presença é integrada com Página inicial e jornadas de acesso.

## Critérios de aceite

- Configuração/desafio2FA, confirmação de senha e passkeys apresentam identidade FinAI no claro e escuro, mantendo conteúdo e ações equivalentes.
- Preservar os estados atuais de QR/chave manual, confirmação OTP, códigos de recuperação, ativação/desativação, carregamento e erros; o QR continua legível no tema escuro.
- Preservar passkeys vazias/preenchidas, indisponibilidade do navegador quando aplicável, registro, entrada/verificação, remoção, cancelamento e erros existentes, com seus resultados e controles atuais.
- Diálogos mantêm abertura/fechamento, rótulos, foco visível e operação por teclado; cancelamentos e falhas não passam a concluir ações indevidamente.
- Preservar as permissões e a exigência atual de confirmação de senha, sem ampliar ou remover recursos.
- Nas superfícies desta entrega, conferir os nove viewports (360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080), temas claro e escuro, estados aplicáveis e ausência de rolagem horizontal da página; manter acesso às ações atuais, rótulos e foco visível.

## Dependências

Pode iniciar com os recursos e telas atuais. Para concluir, integrar a identidade de Identidade e temas no painel atual e a estrutura aplicável de Estrutura e navegação responsiva atuais; integrar a entrada por passkey com Página inicial e jornadas de acesso. Não há bloqueio nativo de início entre esses DEV.

## Referências

Item pai Redmine #1016101; regras/critérios R1, R2, R3, R5, CA1, CA2, CA5, CA6, CA7, CA8, V-Seguranca.

- design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; .btn, inputs, dialog, mensagens e tokens; adaptação aprovada para telas e estados de segurança atuais sem desenho específico
- Adaptações aprovadas: todas as telas atuais, claro/escuro/sistema preservados; telas futuras nas próximas Features.


### [QA] [WEB] [USUARIO] Adequação visual do FinAI

```json
{
  "project_id": 65224,
  "parent_issue_id": 1016101,
  "tracker_id": 5,
  "status_id": 1,
  "subject": "[QA] [WEB] [USUARIO] Adequação visual do FinAI",
  "assigned_to_id": null,
  "start_date": null,
  "due_date": null,
  "estimated_hours": 1.5,
  "priority_id": 4,
  "fixed_version_id": 20355
}
```

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


## Condições de teste integrais

# Condições de teste

## Contexto

Comparar as telas atuais com a referência visual clara e com as adaptações aprovadas de todas as telas e tema escuro. Usar visitante, conta autenticada, estados de confirmação e configuração de 2FA/passkeys conforme cada jornada atual. Matriz: 360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080. Cobrir claro e escuro e verificar seleção/persistência e acompanhar o sistema. Leitura de testes existentes não é execução nem prova de fidelidade visual. Registrar os resultados observados e impedimentos, sem declarar sucesso para condição não executada.

## Identidade e navegação

### CT-001 — Marca e linguagem clara

Verificação: Comparar painel e componentes compartilhados atuais com design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md (:root,.brand,.btn,campos e diálogos). Conferir os valores de R3 e telas consumidoras.

Resultado esperado: Marca FinAI substitui a do starter; fundo #F5F7F8/superfícies brancas, paleta de R3, títulos Georgia/corpo system-ui, controles8px/painéis16px e hierarquia/estados aplicáveis correspondem à referência.

Origem no requisito: R1: A entrega abrange a página inicial atual, cadastro, login, recuperação e redefinição de senha, confirmação de senha, verificação de e-mail, desafio de dois fatores, dashboard atual, perfil, alteração de senha, aparência, configuração de dois fatores e passkeys, incluindo seus estados e componentes existentes. Essa lista é inventário do código, não comprovação de aceite funcional anterior.; R3: A referência clara usa fundo #F5F7F8, superfícies brancas, texto #172622, texto secundário #52615C, verde principal #145C46, verde positivo #146345, vermelho negativo #A12B36, bordas #D6DFDB e destaque suave #E4F0E9. Preservar a hierarquia do design: títulos de destaque em Georgia e corpo em system-ui; controles com raio de 8px e painéis com 16px; espaçamento, bordas, sombras, estados e proporções conforme o pacote.; R6: A marca FinAI substitui a identidade visual genérica do starter nas superfícies atuais. Não apresentar rótulos do protótipo que afirmem armazenamento apenas no navegador ou assistente simulado; persistência e IA real serão tratadas pelas Features responsáveis.; CA1: Ao visitar cada superfície de R1 que esteja disponível para o usuário, reconhecer a identidade FinAI na marca, tipografia, paleta e componentes; nas superfícies sem desenho próprio, preservar campos e finalidade com a mesma linguagem visual.; CA2: No tema claro, comparar as estruturas e os componentes aplicáveis com o ZIP e verificar cores de R3, títulos Georgia, corpo system-ui, hierarquia, espaçamentos, proporções, raios, bordas e estados, sem manter a aparência genérica do starter.

### CT-002 — Variante escura

Verificação: Abrir cada tela/estado atual no escuro e compará-lo ao claro e à linguagem FinAI, incluindo avisos, erros, menus, diálogos e QR.

Resultado esperado: Conteúdo e ações equivalentes; superfícies,textos,bordas,foco e estados são distinguíveis e legíveis. Tema escuro do starter foi adequado, e QR permanece legível.

Origem no requisito: R5: Preservar claro, escuro e acompanhar o sistema. A variante escura é uma adaptação aprovada da identidade fornecida, mantendo hierarquia visual, distinção entre superfícies, leitura dos textos e identificação dos estados. Não reutilizar o tema escuro neutro do starter sem adequação à identidade FinAI.; CA5: No tema escuro, abrir as mesmas superfícies e estados do tema claro; manter conteúdo e ações equivalentes, identidade FinAI, textos legíveis e distinção visual entre superfícies, bordas, foco, erros e demais estados existentes.

### CT-003 — Navegação desktop/tablet/celular

Verificação: Nos viewports aplicáveis de 360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080, navegar por painel, configurações e menu usuário, usando mouse e teclado. Referência .app,.sidebar,.topbar e media queries.

Resultado esperado: Geometria desktop e reorganização superior em telas menores preservam hierarquia e destinos atuais; ativo/foco visíveis e ações disponíveis, sem novos destinos financeiros.

Origem no requisito: R4: Preservar a organização visual responsiva do design nas estruturas aplicáveis: navegação lateral no desktop e adaptação superior no tablet/celular; controles e conteúdo reorganizados conforme o espaço. Não transportar os destinos financeiros futuros para telas atuais apenas para reproduzir a navegação do protótipo.; R7: A base visual é aceita sobre as telas atuais. Não criar páginas de Transações ou Assistente, formulários financeiros, números demonstrativos ou operações simuladas nesta Feature. As novas telas e suas composições específicas seguem a base nas próximas Features.; CA6: Verificar as telas atuais em 360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080; layout e navegação se adaptam sem rolagem horizontal da página, mantendo acesso às operações atuais.; CA7: Navegar e utilizar formulários, menus e diálogos atuais com mouse e teclado; preservar rótulos, foco visível e estados aplicáveis de hover, ativo, desabilitado e carregamento demonstrados no design ou existentes na aplicação.; CA9: Ao navegar pela entrega, não encontrar novas páginas financeiras, dados fictícios, operações simuladas, rótulos de armazenamento apenas local ou assistente simulado apresentados como funcionalidades prontas. O dashboard atual permanece sem antecipar as capacidades da Feature Dashboard financeiro.

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

Verificação: Verificar todas as superfícies de R1 e estados existentes aplicáveis em 360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080, tanto no claro quanto no escuro; incluir página pública,acesso,painel,perfil,senha,aparência,2FA,confirmações e passkeys. Comparar identidade clara com design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md e adaptação escura aprovada.

Resultado esperado: Cada tela preserva identidade,composição aplicável,conteúdo e acesso aos controles, sem rolagem horizontal da página. As composições sem desenho próprio seguem a linguagem FinAI; nenhum viewport ou superfície é dispensado.

Origem no requisito: R1: A entrega abrange a página inicial atual, cadastro, login, recuperação e redefinição de senha, confirmação de senha, verificação de e-mail, desafio de dois fatores, dashboard atual, perfil, alteração de senha, aparência, configuração de dois fatores e passkeys, incluindo seus estados e componentes existentes. Essa lista é inventário do código, não comprovação de aceite funcional anterior.; CA1: Ao visitar cada superfície de R1 que esteja disponível para o usuário, reconhecer a identidade FinAI na marca, tipografia, paleta e componentes; nas superfícies sem desenho próprio, preservar campos e finalidade com a mesma linguagem visual.; CA2: No tema claro, comparar as estruturas e os componentes aplicáveis com o ZIP e verificar cores de R3, títulos Georgia, corpo system-ui, hierarquia, espaçamentos, proporções, raios, bordas e estados, sem manter a aparência genérica do starter.; CA5: No tema escuro, abrir as mesmas superfícies e estados do tema claro; manter conteúdo e ações equivalentes, identidade FinAI, textos legíveis e distinção visual entre superfícies, bordas, foco, erros e demais estados existentes.; CA6: Verificar as telas atuais em 360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080; layout e navegação se adaptam sem rolagem horizontal da página, mantendo acesso às operações atuais.; V-Publica: Desdobramento de R1/R2/CA1/CA6/CA8: composição da página inicial atual com identidade FinAI, preservando conteúdo funcional e destinos.; V-Acesso: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de cadastro, login, recuperação/redefinição e verificação de e-mail.; V-Conta: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de perfil, senha, aparência e exclusão de conta.; V-Seguranca: Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de 2FA, confirmação de senha e passkeys.

### CT-024 — Permissões e ausência de antecipação financeira

Verificação: Como visitante e contas em estados diferentes, tentar caminhos atuais públicos/protegidos e navegar após sair. Conferir painel e menu sem páginas futuras.

Resultado esperado: Mesmas restrições e destinos anteriores; sem novas regras de acesso,sem dados/ações financeiras simuladas,sem destinos Transações/Assistente e sem rótulos de armazenamento local/IA simulada como produto pronto.

Origem no requisito: R2: Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega.; R6: A marca FinAI substitui a identidade visual genérica do starter nas superfícies atuais. Não apresentar rótulos do protótipo que afirmem armazenamento apenas no navegador ou assistente simulado; persistência e IA real serão tratadas pelas Features responsáveis.; R7: A base visual é aceita sobre as telas atuais. Não criar páginas de Transações ou Assistente, formulários financeiros, números demonstrativos ou operações simuladas nesta Feature. As novas telas e suas composições específicas seguem a base nas próximas Features.; CA8: Executar ações atuais com dados válidos e inválidos, onde aplicável; campos, validações, mensagens, cancelamentos, confirmações e resultados funcionais permanecem equivalentes após a adequação visual. O mesmo vale para restrições de acesso de visitantes e usuários autenticados.; CA9: Ao navegar pela entrega, não encontrar novas páginas financeiras, dados fictícios, operações simuladas, rótulos de armazenamento apenas local ou assistente simulado apresentados como funcionalidades prontas. O dashboard atual permanece sem antecipar as capacidades da Feature Dashboard financeiro.

## Cobertura, inspeção e estimativas

A tabela completa de cobertura por requisito, a evidência de cada destino e as descrições DEV também constam de [slices.md](slices.md). Regras transversais possuem proprietário da política/estrutura compartilhada; as composições particulares preservam os mesmos critérios nas suas telas. Os desdobramentos V-* rastreiam as cláusulas de R1/R2/CA1/CA6/CA8 por superfície, sem requisito funcional novo.

- Fonte de escopo: requisito canônico aprovado #1016101 e design normalizado, com adaptações atribuídas na entrevista: todas as telas atuais, claro/escuro/sistema, novas telas financeiras somente nas Features posteriores. Nenhuma task antiga é contexto ou implementação comprovada.
- Inspeção por leitura de código e testes disponíveis; não foram executados testes nem validada uma implementação visual. Toda a base é classificada como adapt, com capacidades existentes a preservar; nenhuma tela foi declarada visualmente pronta.
- Os IDs canônicos R1–R7 e CA1–CA9 foram mantidos. V-Publica/V-Acesso/V-Conta/V-Seguranca apenas desdobram suas cláusulas por superfície para separar composição da base compartilhada, sem introduzir comportamento novo. A cobertura única indica o proprietário da política/estrutura comum; descrições e condições mantêm a aplicação transversal a todas as telas.
- Estimativa independente A: agregado inicial DEV1=6h, acesso=5h, conta=3h, segurança=5h; após inspeção específica da sidebar, identidade=4h e estrutura=3,5h. QA=8h, incluindo preparação, matriz visual, jornadas e reteste. Autoria: agente estimate_visual_delivery; não recebeu estimativa candidata.
- Estimativa independente B: agregado inicial DEV1=7h, acesso=5,5h, conta=3,5h, segurança=5,5h; refinamento identidade=3,5h e estrutura=4h. QA=8h. Autoria: agente estimate_visual_reuse; não recebeu números da avaliação A.
- Histórico da primeira proposta — estimativas DEV de responsabilidade do agente principal: 4h identidade (variante escura e estados),4h estrutura (mudança real da geometria e nove viewports),5,5h pública/acesso (cores e composições próprias além do layout comum),3,5h conta (reuso dos formulários e diálogo) e5,5h segurança (muitos estados QR/OTP/passkeys). Incluem mudança, integração e verificação da própria entrega. Não são média automática ou medição de execução.
- Ajuste explícito de Mário Tinelli nesta conversa: não há referência histórica, mas considera 1,5h suficiente para QA por serem poucas telas para visualizar. QA final=1,5h por calibração do tech lead; as avaliações independentes de8h são preservadas no histórico. Não houve evidência nova de automação nem redução da matriz, jornadas ou condições de teste.
- Contexto de estimativa: sem calibração histórica local e sem pressupor uso de IA pelo executor. Reuso comprovado de layouts, componentes e mecanismo de tema; não pressupor captura visual ou massa de QA pronta. Preparação/verificação cabe na estimativa adotada; espera externa não é esforço ativo.
- Ordem preferida identidade→estrutura→composições de páginas; não inventar bloqueios nativos de início entre os DEV. Layouts e variáveis já existentes permitem iniciar as adaptações; a integração nomeada é necessária para concluir os critérios. As cinco entregas bloqueiam a QA integrada.
- Publicação proposta: cinco Task DEV e uma Deliverable QA, todos New/Normal, pai1016101, versão Sprint1 herdada; sem responsável ou datas. Nenhuma filha existe no snapshot do pai. DOCX obrigatório de condições será gerado da fonte aprovada e anexado à QA usando o mesmo consentimento da prévia completa.
- Correção explícita de Mário Tinelli nesta conversa: “correções nas estimativas, na ordem apresentada: 2h, 2h, 2h, 2h, 2h, qa esta correta”. Estimativas atuais dos cinco DEV: 2h cada (10h DEV); QA permanece 1,5h; total 11,5h. Esta correção humana substitui os valores 4h/4h/5,5h/3,5h/5,5h da revisão001, sem ser apresentada como cálculo independente ou tempo medido. Entregas, critérios, cobertura, condições e relações permanecem iguais.
