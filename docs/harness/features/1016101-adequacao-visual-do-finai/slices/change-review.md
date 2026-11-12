# Revisão de mudança do requisito

Classificação semântica: **functional**  
Revisão: 3  
Hash da revisão: `c45d623d1d604562cbf782d40089d17185ad695169c9da7171e3ddeca4a2f63c`

## Resumo

Uma DEV complementar atende ao novo layout desktop/tablet/celular. Preservar #1016112 e #1016113 encerradas e as três DEV específicas New. Na mesma QA #1016117, revisar CT-003 e CT-023, acrescentar CT-025 a CT-027 e propor estimativa total 2,25h. Preservar os demais 22 CTs, anexos e relações anteriores; acrescentar somente nova DEV bloqueando a QA.

## Mudanças observadas

### layout-R4 — functional

- Antes: Preservar a organização visual responsiva do design nas estruturas aplicáveis: navegação lateral no desktop e adaptação superior no tablet/celular; controles e conteúdo reorganizados conforme o espaço. Não transportar os destinos financeiros futuros para telas atuais apenas para reproduzir a navegação do protótipo.
- Agora: Aplicar a revisão design-input-002 à estrutura autenticada compartilhada: até 767px, marca no topo e navegação principal fixa no rodapé, de largura total, com base de 56px acrescida da área segura inferior e ícones de 24px, alvos de pelo menos 44px, sem legendas visíveis e com nomes acessíveis; de 768 a 1024px inclusive, navegação lateral compacta de 72px acrescida da área segura lateral, marca compacta, alvos de pelo menos 48px e conteúdo ao lado, sem barra inferior; a partir de 1025px, navegação lateral desktop, preservando o recolhimento e os destinos atuais. A partir de 768px, apresentar o conteúdo em superfície com fundo de trabalho, contorno de 1px, raio de 16px e margem de 8px, com a navegação integrada ao entorno e cabeçalho transparente conforme a referência. Reservar espaço para navegação e áreas seguras, sem encobrir conteúdo, foco, mensagens ou controles. Preservar acesso ao menu da conta, configurações, links e saída em todas as larguras, adaptando sua apresentação quando o protótipo esconder o rodapé lateral. Não transportar destinos financeiros futuros para as telas atuais.
- Justificativa: O novo design altera resultados visuais verificáveis e exige complemento; aprovação da correção registrada em slices-divergence.json.

### layout-CA2 — functional

- Antes: No tema claro, comparar as estruturas e os componentes aplicáveis com o ZIP e verificar cores de R3, títulos Georgia, corpo system-ui, hierarquia, espaçamentos, proporções, raios, bordas e estados, sem manter a aparência genérica do starter.
- Agora: No tema claro, comparar as estruturas e os componentes aplicáveis com a referência design-input-001 e as alterações compartilhadas de design-input-002, conforme R4 e verificar cores de R3, títulos Georgia, corpo system-ui, hierarquia, espaçamentos, proporções, raios, bordas e estados, sem manter a aparência genérica do starter.
- Justificativa: O novo design altera resultados visuais verificáveis e exige complemento; aprovação da correção registrada em slices-divergence.json.

### layout-CA6 — functional

- Antes: Verificar as telas atuais em 360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080; layout e navegação se adaptam sem rolagem horizontal da página, mantendo acesso às operações atuais.
- Agora: Verificar as telas atuais em 360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080; layout e navegação se adaptam sem rolagem horizontal da página, mantendo acesso às operações atuais. Conferir também as transições 767/768px e 1024/1025px, incluindo redimensionamento após recolher a navegação desktop; cada largura aplica o modo de R4 e mantém os destinos e ações atuais disponíveis.
- Justificativa: O novo design altera resultados visuais verificáveis e exige complemento; aprovação da correção registrada em slices-divergence.json.

### layout-CA10 — functional

- Antes: Critério inexistente na versão anterior.
- Agora: Em largura de até 767px, reconhecer a marca no topo e a navegação principal fixa no rodapé em largura total, com base de 56px mais a área segura, ícones de 24px, alvos de pelo menos 44px, destino ativo e nomes acessíveis mesmo sem legenda visível. Percorrer até o fim da página, focar controles e abrir menus/diálogos: a navegação não encobre ações, mensagens ou foco, e o acesso à conta, configurações, links e saída permanece disponível.
- Justificativa: O novo design altera resultados visuais verificáveis e exige complemento; aprovação da correção registrada em slices-divergence.json.

### layout-CA11 — functional

- Antes: Critério inexistente na versão anterior.
- Agora: De 768 a 1024px inclusive, verificar lateral compacta de 72px mais a área segura, marca compacta, alvos de pelo menos 48px e conteúdo ao lado, sem navegação inferior. A partir de 1025px, verificar navegação lateral desktop com recolhimento atual preservado. Em ambas as faixas, comparar contorno de 1px, raio de 16px, margem de 8px, entorno contínuo e cabeçalho transparente com design-input-002, nos temas claro e escuro; em sistema, manter a preferência existente. Navegação, conta, configurações, links, saída e estados de foco/ativo continuam acessíveis.
- Justificativa: O novo design altera resultados visuais verificáveis e exige complemento; aprovação da correção registrada em slices-divergence.json.

### layout-source — functional

- Antes: Design-input-001 com navegação superior tablet/celular.
- Agora: Design-input-002 prevalece nas alterações de navegação e superfície compartilhadas, com a referência original preservada.
- Justificativa: O pacote no mesmo caminho possui outro hash e muda o aceite visual; não é simples correção de localizador.

## Impactos localizados

### Tarefas

- `dev-2` — A entrega de estrutura muda de aceite: preservar #1016113 encerrada e representar a diferença por nova DEV; atualizar as condições e estimativa da QA existente, preservando os demais campos.
- `qa` — A entrega de estrutura muda de aceite: preservar #1016113 encerrada e representar a diferença por nova DEV; atualizar as condições e estimativa da QA existente, preservando os demais campos.

### Critérios de aceite

- `dev-2:criterion-1` — O complemento substitui a navegação superior pelo novo comportamento e acrescenta os limites exatos da matriz; o critério histórico da tarefa encerrada permanece sem edição.
- `dev-2:criterion-5` — O complemento substitui a navegação superior pelo novo comportamento e acrescenta os limites exatos da matriz; o critério histórico da tarefa encerrada permanece sem edição.

### Itens de cobertura

- `CA2` — Nova obrigação visual da navegação/estrutura compartilhada; a diferença será coberta pela DEV complementar e QA integrada.
- `CA6` — Nova obrigação visual da navegação/estrutura compartilhada; a diferença será coberta pela DEV complementar e QA integrada.
- `R4` — Nova obrigação visual da navegação/estrutura compartilhada; a diferença será coberta pela DEV complementar e QA integrada.

### Dependências

- `blocks:dev-2:qa` — O aceite da estrutura que bloqueia QA recebe um complemento: preservar a relação #840 da DEV encerrada com QA e acrescentar uma nova relação da DEV complementar para a mesma QA.

### Condições de teste

- `CT-003` — O esperado de navegação superior e a fonte de comparação da matriz compartilhada passam ao novo design; preservar o ID e atualizar somente essa diferença.
- `CT-023` — O esperado de navegação superior e a fonte de comparação da matriz compartilhada passam ao novo design; preservar o ID e atualizar somente essa diferença.

## Itens que permanecem válidos

### Tarefas

- `dev-1` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `dev-3` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `dev-4` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `dev-5` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.

### Critérios de aceite

- `dev-1:criterion-1` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `dev-1:criterion-2` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `dev-1:criterion-3` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `dev-1:criterion-4` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `dev-1:criterion-5` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `dev-1:criterion-6` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `dev-2:criterion-2` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `dev-2:criterion-3` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `dev-2:criterion-4` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `dev-3:criterion-1` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `dev-3:criterion-2` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `dev-3:criterion-3` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `dev-3:criterion-4` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `dev-3:criterion-5` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `dev-3:criterion-6` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `dev-4:criterion-1` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `dev-4:criterion-2` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `dev-4:criterion-3` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `dev-4:criterion-4` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `dev-4:criterion-5` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `dev-4:criterion-6` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `dev-5:criterion-1` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `dev-5:criterion-2` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `dev-5:criterion-3` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `dev-5:criterion-4` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `dev-5:criterion-5` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `dev-5:criterion-6` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.

### Itens de cobertura

- `CA1` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `CA3` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `CA4` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `CA5` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `CA7` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `CA8` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `CA9` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `R1` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `R2` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `R3` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `R5` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `R6` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `R7` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `V-Acesso` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `V-Conta` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `V-Publica` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `V-Seguranca` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.

### Dependências

- `blocks:dev-1:qa` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `blocks:dev-3:qa` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `blocks:dev-4:qa` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `blocks:dev-5:qa` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.

### Condições de teste

- `CT-001` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `CT-002` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `CT-004` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `CT-005` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `CT-006` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `CT-007` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `CT-008` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `CT-009` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `CT-010` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `CT-011` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `CT-012` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `CT-013` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `CT-014` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `CT-015` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `CT-016` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `CT-017` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `CT-018` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `CT-019` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `CT-020` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `CT-021` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `CT-022` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.
- `CT-024` — Permanece válido e preservado: a mudança da estrutura compartilhada não altera este resultado, regra, jornada, relação ou obrigação anterior.

## Condições vigentes

`condicoes-teste-r002.docx` — `f8019ab3f94a9dff022db3104885a7aa64c45e433e46780a40f1713cfd48954d`

## Inclusões autorizadas nas condições

- `CT-025` — Transições exatas 767/768px e 1024/1025px, inclusive após recolher a navegação desktop; CA6, CA10 e CA11.
- `CT-026` — Barra inferior e áreas seguras sem ocultar conteúdo, foco, controles ou conta/configurações/saída; CA10.
- `CT-027` — Lateral compacta tablet e superfície contínua desktop/tablet com contorno, raio, margens e cabeçalho; CA11.

## Requisitos da revisão

- `R1` — A entrega abrange a página inicial atual, cadastro, login, recuperação e redefinição de senha, confirmação de senha, verificação de e-mail, desafio de dois fatores, dashboard atual, perfil, alteração de senha, aparência, configuração de dois fatores e passkeys, incluindo seus estados e componentes existentes. Essa lista é inventário do código, não comprovação de aceite funcional anterior.
- `R2` — Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega.
- `R3` — A referência clara usa fundo #F5F7F8, superfícies brancas, texto #172622, texto secundário #52615C, verde principal #145C46, verde positivo #146345, vermelho negativo #A12B36, bordas #D6DFDB e destaque suave #E4F0E9. Preservar a hierarquia do design: títulos de destaque em Georgia e corpo em system-ui; controles com raio de 8px e painéis com 16px; espaçamento, bordas, sombras, estados e proporções conforme o pacote.
- `R4` — Aplicar a revisão design-input-002 à estrutura autenticada compartilhada: até 767px, marca no topo e navegação principal fixa no rodapé, de largura total, com base de 56px acrescida da área segura inferior e ícones de 24px, alvos de pelo menos 44px, sem legendas visíveis e com nomes acessíveis; de 768 a 1024px inclusive, navegação lateral compacta de 72px acrescida da área segura lateral, marca compacta, alvos de pelo menos 48px e conteúdo ao lado, sem barra inferior; a partir de 1025px, navegação lateral desktop, preservando o recolhimento e os destinos atuais. A partir de 768px, apresentar o conteúdo em superfície com fundo de trabalho, contorno de 1px, raio de 16px e margem de 8px, com a navegação integrada ao entorno e cabeçalho transparente conforme a referência. Reservar espaço para navegação e áreas seguras, sem encobrir conteúdo, foco, mensagens ou controles. Preservar acesso ao menu da conta, configurações, links e saída em todas as larguras, adaptando sua apresentação quando o protótipo esconder o rodapé lateral. Não transportar destinos financeiros futuros para as telas atuais.
- `R5` — Preservar claro, escuro e acompanhar o sistema. A variante escura é uma adaptação aprovada da identidade fornecida, mantendo hierarquia visual, distinção entre superfícies, leitura dos textos e identificação dos estados. Não reutilizar o tema escuro neutro do starter sem adequação à identidade FinAI.
- `R6` — A marca FinAI substitui a identidade visual genérica do starter nas superfícies atuais. Não apresentar rótulos do protótipo que afirmem armazenamento apenas no navegador ou assistente simulado; persistência e IA real serão tratadas pelas Features responsáveis.
- `R7` — A base visual é aceita sobre as telas atuais. Não criar páginas de Transações ou Assistente, formulários financeiros, números demonstrativos ou operações simuladas nesta Feature. As novas telas e suas composições específicas seguem a base nas próximas Features.
- `CA1` — Ao visitar cada superfície de R1 que esteja disponível para o usuário, reconhecer a identidade FinAI na marca, tipografia, paleta e componentes; nas superfícies sem desenho próprio, preservar campos e finalidade com a mesma linguagem visual.
- `CA2` — No tema claro, comparar as estruturas e os componentes aplicáveis com a referência design-input-001 e as alterações compartilhadas de design-input-002, conforme R4 e verificar cores de R3, títulos Georgia, corpo system-ui, hierarquia, espaçamentos, proporções, raios, bordas e estados, sem manter a aparência genérica do starter.
- `CA3` — Selecionar claro, escuro e acompanhar o sistema; cada opção continua disponível e aplica a aparência correspondente. Ao retornar à aplicação, manter a preferência conforme o comportamento existente.
- `CA4` — Com acompanhar o sistema selecionado, alterar a preferência do dispositivo; a aparência acompanha a mudança. Com claro ou escuro explicitamente selecionado, a preferência do dispositivo não substitui a escolha.
- `CA5` — No tema escuro, abrir as mesmas superfícies e estados do tema claro; manter conteúdo e ações equivalentes, identidade FinAI, textos legíveis e distinção visual entre superfícies, bordas, foco, erros e demais estados existentes.
- `CA6` — Verificar as telas atuais em 360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080; layout e navegação se adaptam sem rolagem horizontal da página, mantendo acesso às operações atuais. Conferir também as transições 767/768px e 1024/1025px, incluindo redimensionamento após recolher a navegação desktop; cada largura aplica o modo de R4 e mantém os destinos e ações atuais disponíveis.
- `CA7` — Navegar e utilizar formulários, menus e diálogos atuais com mouse e teclado; preservar rótulos, foco visível e estados aplicáveis de hover, ativo, desabilitado e carregamento demonstrados no design ou existentes na aplicação.
- `CA8` — Executar ações atuais com dados válidos e inválidos, onde aplicável; campos, validações, mensagens, cancelamentos, confirmações e resultados funcionais permanecem equivalentes após a adequação visual. O mesmo vale para restrições de acesso de visitantes e usuários autenticados.
- `CA9` — Ao navegar pela entrega, não encontrar novas páginas financeiras, dados fictícios, operações simuladas, rótulos de armazenamento apenas local ou assistente simulado apresentados como funcionalidades prontas. O dashboard atual permanece sem antecipar as capacidades da Feature Dashboard financeiro.
- `CA10` — Em largura de até 767px, reconhecer a marca no topo e a navegação principal fixa no rodapé em largura total, com base de 56px mais a área segura, ícones de 24px, alvos de pelo menos 44px, destino ativo e nomes acessíveis mesmo sem legenda visível. Percorrer até o fim da página, focar controles e abrir menus/diálogos: a navegação não encobre ações, mensagens ou foco, e o acesso à conta, configurações, links e saída permanece disponível.
- `CA11` — De 768 a 1024px inclusive, verificar lateral compacta de 72px mais a área segura, marca compacta, alvos de pelo menos 48px e conteúdo ao lado, sem navegação inferior. A partir de 1025px, verificar navegação lateral desktop com recolhimento atual preservado. Em ambas as faixas, comparar contorno de 1px, raio de 16px, margem de 8px, entorno contínuo e cabeçalho transparente com design-input-002, nos temas claro e escuro; em sistema, manter a preferência existente. Navegação, conta, configurações, links, saída e estados de foco/ativo continuam acessíveis.
- `V-Publica` — Desdobramento de R1/R2/CA1/CA6/CA8: composição da página inicial atual com identidade FinAI, preservando conteúdo funcional e destinos.
- `V-Acesso` — Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de cadastro, login, recuperação/redefinição e verificação de e-mail.
- `V-Conta` — Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de perfil, senha, aparência e exclusão de conta.
- `V-Seguranca` — Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de 2FA, confirmação de senha e passkeys.
## Preservação

Filhas publicadas, decisões sobre filhas existentes/externas, estudos, divergências e evidências de dependência permanecem intactos enquanto esta revisão estiver pendente ou rejeitada.
