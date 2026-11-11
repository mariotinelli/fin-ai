# [WEB] [USUARIO] Adequação visual do FinAI

## Objetivo

Adequar todas as telas atualmente existentes à identidade visual do FinAI, oferecendo uma experiência consistente em computadores, tablets e celulares. Preservar as funcionalidades existentes e estabelecer o padrão visual que será seguido pelas próximas Features.

## Resultado esperado

As telas atuais compartilham marca, cores, tipografia, componentes, estrutura e navegação coerentes com o design fornecido. O usuário mantém as opções de aparência clara, escura e acompanhar o sistema. Telas financeiras novas serão desenvolvidas nas respectivas Features, seguindo essa base.

## Atores e permissões

Visitantes utilizam as telas públicas já disponíveis. Usuários autenticados utilizam as telas protegidas conforme suas permissões atuais. A adequação visual mantém as restrições de acesso e não altera quais ações cada pessoa pode executar.

## Histórias de usuário

1. Como visitante, quero reconhecer a identidade FinAI na página inicial e nas telas de acesso para ter uma experiência visual consistente.
2. Como usuário, quero encontrar a mesma identidade na área autenticada, perfil e configurações para navegar com continuidade visual.
3. Como usuário, quero continuar escolhendo aparência clara, escura ou acompanhar o sistema para manter minha preferência.
4. Como usuário em celular, tablet ou computador, quero navegar e utilizar os controles atuais com o layout adaptado à minha tela.
5. Como usuário, quero reconhecer campos, erros, confirmações e estados indisponíveis dentro do mesmo padrão visual, mantendo os fluxos que já existem.

## Fluxo principal

1. Abrir uma tela atual. Apresentar marca e identidade FinAI na composição adequada à tela e ao estado de autenticação.
2. Navegar entre os destinos atualmente disponíveis, mantendo os caminhos e os controles de acesso existentes. Indicar o destino ativo onde já houver navegação.
3. Apresentar formulários, botões, links, menus e diálogos existentes com a linguagem visual do design, mantendo conteúdo funcional, campos e operações.
4. Na preferência de aparência, permitir escolher claro, escuro ou acompanhar o sistema. Aplicar o tema selecionado e manter a preferência conforme o comportamento atual.
5. Ao utilizar diferentes larguras de tela, adaptar estrutura, navegação e composição dos controles sem esconder operações que continuam disponíveis no sistema.

## Fluxos alternativos e exceções

- No tema escuro, adaptar fundos, superfícies, textos, bordas, destaques e estados à identidade FinAI, mantendo conteúdo e operações equivalentes ao tema claro.
- Em acompanhar o sistema, a aparência segue a preferência do dispositivo e suas mudanças, conforme o comportamento atual. Escolhas explícitas de claro ou escuro permanecem independentes dessa preferência.
- Erros de validação, mensagens de sucesso ou falha, carregamento, controles desabilitados, confirmação e cancelamento já existentes mantêm seu significado e comportamento, recebendo adequação visual.
- Telas atuais sem composição específica no ZIP, como acesso, perfil e configurações, recebem a mesma marca, tipografia, paleta, espaçamento e linguagem de componentes, preservando sua finalidade e operações.
- O dashboard atual recebe adequação visual do que já existe; não recebe saldo, totais, histórico ou outros dados financeiros antecipados nesta Feature.
- A ausência de uma tela financeira futura não produz um destino fictício ou uma simulação funcional. Sua tela e seu destino serão entregues pela Feature responsável.

## Regras de negócio

R1. A entrega abrange a página inicial atual, cadastro, login, recuperação e redefinição de senha, confirmação de senha, verificação de e-mail, desafio de dois fatores, dashboard atual, perfil, alteração de senha, aparência, configuração de dois fatores e passkeys, incluindo seus estados e componentes existentes. Essa lista é inventário do código, não comprovação de aceite funcional anterior.

R2. Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega.

R3. A referência clara usa fundo #F5F7F8, superfícies brancas, texto #172622, texto secundário #52615C, verde principal #145C46, verde positivo #146345, vermelho negativo #A12B36, bordas #D6DFDB e destaque suave #E4F0E9. Preservar a hierarquia do design: títulos de destaque em Georgia e corpo em system-ui; controles com raio de 8px e painéis com 16px; espaçamento, bordas, sombras, estados e proporções conforme o pacote.

R4. Preservar a organização visual responsiva do design nas estruturas aplicáveis: navegação lateral no desktop e adaptação superior no tablet/celular; controles e conteúdo reorganizados conforme o espaço. Não transportar os destinos financeiros futuros para telas atuais apenas para reproduzir a navegação do protótipo.

R5. Preservar claro, escuro e acompanhar o sistema. A variante escura é uma adaptação aprovada da identidade fornecida, mantendo hierarquia visual, distinção entre superfícies, leitura dos textos e identificação dos estados. Não reutilizar o tema escuro neutro do starter sem adequação à identidade FinAI.

R6. A marca FinAI substitui a identidade visual genérica do starter nas superfícies atuais. Não apresentar rótulos do protótipo que afirmem armazenamento apenas no navegador ou assistente simulado; persistência e IA real serão tratadas pelas Features responsáveis.

R7. A base visual é aceita sobre as telas atuais. Não criar páginas de Transações ou Assistente, formulários financeiros, números demonstrativos ou operações simuladas nesta Feature. As novas telas e suas composições específicas seguem a base nas próximas Features.

## Dados percebidos pelo usuário

Marca, cores, tipografia, títulos, textos funcionais atuais, campos, botões, menus, links, diálogos, mensagens, indicadores de estado e escolha de aparência. Esta Feature não cria nem modifica dados financeiros e não transforma placeholders atuais em informações financeiras reais.

## Critérios de aceite

CA1. Ao visitar cada superfície de R1 que esteja disponível para o usuário, reconhecer a identidade FinAI na marca, tipografia, paleta e componentes; nas superfícies sem desenho próprio, preservar campos e finalidade com a mesma linguagem visual.

CA2. No tema claro, comparar as estruturas e os componentes aplicáveis com o ZIP e verificar cores de R3, títulos Georgia, corpo system-ui, hierarquia, espaçamentos, proporções, raios, bordas e estados, sem manter a aparência genérica do starter.

CA3. Selecionar claro, escuro e acompanhar o sistema; cada opção continua disponível e aplica a aparência correspondente. Ao retornar à aplicação, manter a preferência conforme o comportamento existente.

CA4. Com acompanhar o sistema selecionado, alterar a preferência do dispositivo; a aparência acompanha a mudança. Com claro ou escuro explicitamente selecionado, a preferência do dispositivo não substitui a escolha.

CA5. No tema escuro, abrir as mesmas superfícies e estados do tema claro; manter conteúdo e ações equivalentes, identidade FinAI, textos legíveis e distinção visual entre superfícies, bordas, foco, erros e demais estados existentes.

CA6. Verificar as telas atuais em 360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080; layout e navegação se adaptam sem rolagem horizontal da página, mantendo acesso às operações atuais.

CA7. Navegar e utilizar formulários, menus e diálogos atuais com mouse e teclado; preservar rótulos, foco visível e estados aplicáveis de hover, ativo, desabilitado e carregamento demonstrados no design ou existentes na aplicação.

CA8. Executar ações atuais com dados válidos e inválidos, onde aplicável; campos, validações, mensagens, cancelamentos, confirmações e resultados funcionais permanecem equivalentes após a adequação visual. O mesmo vale para restrições de acesso de visitantes e usuários autenticados.

CA9. Ao navegar pela entrega, não encontrar novas páginas financeiras, dados fictícios, operações simuladas, rótulos de armazenamento apenas local ou assistente simulado apresentados como funcionalidades prontas. O dashboard atual permanece sem antecipar as capacidades da Feature Dashboard financeiro.

## Dependências

Sem dependência de outra Feature do catálogo. O pacote de design informado é a referência visual. A implementação das próximas Features deve usar esta base; seus próprios campos, fluxos, dados e composições de tela serão aceitos nos respectivos requisitos. A conclusão deste requisito não significa que a adequação visual já foi implementada.

## Designs e evidências

Referência principal: design-input-001, ../../scopes/2026-11-11-finai-mvp/sources/design-input-001.md. Original: C:/Users/maari/Downloads/FinAI-Controle-Financeiro.zip. Identificador: d5659f24-e48f-439f-bda3-af5cf97f4591.

Localizadores: index.html, estilos :root, .app, .sidebar, .topbar, .btn, campos, diálogos e media queries; superfícies #overview, #transactions e #assistant fornecem referências da linguagem visual para as entregas que as utilizarão. DESIGN-MANIFEST.json define os nove viewports de CA6; CSS, estrutura e comportamento foram extraídos integralmente sem executar o pacote.

Comparação atual: resources/css/app.css, resources/js/components/app-sidebar.tsx, resources/js/components/app-logo.tsx, resources/js/pages/dashboard.tsx e demais páginas em resources/js/pages. O código atual possui tema do starter e dashboard de placeholders. Preferência existente comprovada em resources/js/hooks/use-appearance.tsx e resources/js/pages/appearance/update.tsx.

Adaptações: o usuário confirmou nesta entrevista adequar todas as telas atuais, desenvolver as novas nas próximas Features e manter as opções de tema. Não há composição escura no ZIP; a variante escura aplica a identidade às telas existentes conforme R5 e CA5. Persistência no sistema e IA real prevalecem sobre rótulos do protótipo por decisão anterior do usuário. Não criar telas futuras para demonstrar a base visual.

## Dentro do escopo

Adequação visual de todas as telas, componentes, estados e navegação atuais; identidade FinAI; responsividade; temas claro e escuro com preferência acompanhar o sistema; preservação do comportamento existente. Critérios visuais aplicáveis à base compartilhada, sem antecipar as composições específicas das Features financeiras.

## Fora do escopo

Novas telas e destinos de Transações ou Assistente; operações financeiras; dashboard com dados reais; integração de IA; mudanças de autenticação, perfil, permissões ou validações; remoção de recursos existentes; decomposição em tarefas técnicas. As capacidades novas pertencem às demais Features do catálogo aprovado.
