<!-- project-flow:run 3e8baa5a-37ce-4543-a114-d102e55b5830 -->
<!-- project-flow:start -->
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

R2. Adequar aparência e idioma preserva campos, validações, significado das mensagens funcionais, operações, permissões, destinos e preferências existentes. Traduzir a apresentação dos textos para português brasileiro sem alterar seus efeitos. Os novos endereços seguem R9 e os antigos continuam funcionais conforme R10. Não acrescentar regras de autenticação ou financeiras nesta entrega.

R3. A referência clara usa fundo #F5F7F8, superfícies brancas, texto #172622, texto secundário #52615C, verde principal #145C46, verde positivo #146345, vermelho negativo #A12B36, bordas #D6DFDB e destaque suave #E4F0E9. Preservar a hierarquia do design: títulos de destaque em Georgia e corpo em system-ui; controles com raio de 8px e painéis com 16px; espaçamento, bordas, sombras, estados e proporções conforme o pacote.

R4. Aplicar a revisão design-input-002 à estrutura autenticada compartilhada: até 767px, marca no topo e navegação principal fixa no rodapé, de largura total, com base de 56px acrescida da área segura inferior e ícones de 24px, alvos de pelo menos 44px, sem legendas visíveis e com nomes acessíveis; de 768 a 1024px inclusive, navegação lateral compacta de 72px acrescida da área segura lateral, marca compacta, alvos de pelo menos 48px e conteúdo ao lado, sem barra inferior; a partir de 1025px, navegação lateral desktop, preservando o recolhimento e os destinos atuais. A partir de 768px, apresentar o conteúdo em superfície com fundo de trabalho, contorno de 1px, raio de 16px e margem de 8px, com a navegação integrada ao entorno e cabeçalho transparente conforme a referência. Reservar espaço para navegação e áreas seguras, sem encobrir conteúdo, foco, mensagens ou controles. Preservar acesso ao menu da conta, configurações, links e saída em todas as larguras, adaptando sua apresentação quando o protótipo esconder o rodapé lateral. Não transportar destinos financeiros futuros para as telas atuais.

R5. Preservar claro, escuro e acompanhar o sistema. A variante escura é uma adaptação aprovada da identidade fornecida, mantendo hierarquia visual, distinção entre superfícies, leitura dos textos e identificação dos estados. Não reutilizar o tema escuro neutro do starter sem adequação à identidade FinAI.

R6. A marca FinAI substitui a identidade visual genérica do starter nas superfícies atuais. Não apresentar rótulos do protótipo que afirmem armazenamento apenas no navegador ou assistente simulado; persistência e IA real serão tratadas pelas Features responsáveis.

R7. A base visual é aceita sobre as telas atuais. Não criar páginas de Transações ou Assistente, formulários financeiros, números demonstrativos ou operações simuladas nesta Feature. As novas telas e suas composições específicas seguem a base nas próximas Features.

R8. Apresentar em português brasileiro todos os textos controlados pela aplicação nas superfícies atuais de R1: página pública, navegação, títulos e breadcrumbs, formulários, botões, placeholders, avisos, feedback, estados vazios/carregamento/erro, validações, diálogos, textos de ajuda, tooltips e nomes/instruções acessíveis. Abranger os e-mails e notificações já enviados pela aplicação, inclusive recuperação e verificação de e-mail; preservar as mensagens que já estejam corretamente traduzidas. O idioma padrão e o fallback não devem reintroduzir inglês em conteúdo próprio exibido ao usuário.

R9. Usar caminhos em português, sem acentos e conforme o mapa de URLs desta regra, para as jornadas e operações próprias existentes, incluindo links, formulários, notificações, redirecionamentos e retomada após autenticação. /login permanece /login por decisão expressa do usuário; a página inicial permanece /. Preservar métodos HTTP, parâmetros, valores, tokens, assinaturas, expiração, restrições de acesso e mecanismos de segurança. Identificadores internos de rotas, classes e campos não precisam ser traduzidos. Endpoints padronizados de protocolo e infraestrutura, como /.well-known/passkey-endpoints, não recebem tradução que viole seu contrato.

| Endereço atual | Endereço principal em português |
| --- | --- |
| `/` | `/` |
| `/login` | `/login` |
| `/dashboard` | `/painel` |
| `/register` | `/cadastro` |
| `/logout` | `/sair` |
| `/forgot-password` | `/recuperar-senha` |
| `/reset-password` | `/redefinir-senha` |
| `/reset-password/{token}` | `/redefinir-senha/{token}` |
| `/verify-email` | `/verificar-email` |
| `/verify-email/{id}/{hash}` | `/verificar-email/{id}/{hash}` |
| `/email/verification-notification` | `/email/notificacao-de-verificacao` |
| `/settings` | `/configuracoes` |
| `/settings/profile` | `/configuracoes/perfil` |
| `/settings/password` | `/configuracoes/senha` |
| `/settings/appearance` | `/configuracoes/aparencia` |
| `/settings/two-factor` | `/configuracoes/autenticacao-de-dois-fatores` |
| `/settings/passkeys` | `/configuracoes/chaves-de-acesso` |
| `/two-factor-challenge` | `/desafio-de-dois-fatores` |
| `/user` | `/usuario` |
| `/user/confirm-password` | `/usuario/confirmar-senha` |
| `/user/confirmed-password-status` | `/usuario/status-de-confirmacao-de-senha` |
| `/user/confirmed-two-factor-authentication` | `/usuario/confirmacao-de-autenticacao-de-dois-fatores` |
| `/user/two-factor-authentication` | `/usuario/autenticacao-de-dois-fatores` |
| `/user/two-factor-qr-code` | `/usuario/autenticacao-de-dois-fatores/codigo-qr` |
| `/user/two-factor-secret-key` | `/usuario/autenticacao-de-dois-fatores/chave-secreta` |
| `/user/two-factor-recovery-codes` | `/usuario/autenticacao-de-dois-fatores/codigos-de-recuperacao` |
| `/user/passkeys` | `/usuario/chaves-de-acesso` |
| `/user/passkeys/options` | `/usuario/chaves-de-acesso/opcoes` |
| `/user/passkeys/{passkey}` | `/usuario/chaves-de-acesso/{passkey}` |
| `/passkeys/login` | `/chaves-de-acesso/entrar` |
| `/passkeys/login/options` | `/chaves-de-acesso/entrar/opcoes` |
| `/passkeys/confirm` | `/chaves-de-acesso/confirmar` |
| `/passkeys/confirm/options` | `/chaves-de-acesso/confirmar/opcoes` |

R10. Todos os endereços próprios anteriores continuam funcionando para seus mesmos destinos e operações, inclusive favoritos, formulários abertos e links de recuperação/verificação já enviados por e-mail. As navegações e comunicações novas passam a usar os caminhos principais em português, com /login preservado. Links antigos válidos mantêm o efeito e o prazo originais; links inválidos, expirados ou adulterados continuam recusados. Compatibilidade não reduz proteção nem repete operações.

R11. A tradução preserva a identidade, temas claro/escuro/sistema, composição responsiva e finalidade de cada tela. Não traduzir conteúdo informado pelos usuários, nomes próprios, marcas, endereços de terceiros nem valores técnicos que precisem permanecer exatos. Textos nativos do navegador, sistema operacional ou autenticador seguem o idioma desses ambientes; os textos controlados pelo FinAI permanecem em português. Esta revisão não cria seletor de idioma ou novas telas financeiras.

## Dados percebidos pelo usuário

Marca, cores, tipografia, títulos, textos funcionais atuais, campos, botões, menus, links, diálogos, mensagens, indicadores de estado e escolha de aparência. Esta Feature não cria nem modifica dados financeiros e não transforma placeholders atuais em informações financeiras reais.

## Critérios de aceite

CA1. Ao visitar cada superfície de R1 que esteja disponível para o usuário, reconhecer a identidade FinAI na marca, tipografia, paleta e componentes; nas superfícies sem desenho próprio, preservar campos e finalidade com a mesma linguagem visual.

CA2. No tema claro, comparar as estruturas e os componentes aplicáveis com a referência design-input-001 e as alterações compartilhadas de design-input-002, conforme R4 e verificar cores de R3, títulos Georgia, corpo system-ui, hierarquia, espaçamentos, proporções, raios, bordas e estados, sem manter a aparência genérica do starter.

CA3. Selecionar claro, escuro e acompanhar o sistema; cada opção continua disponível e aplica a aparência correspondente. Ao retornar à aplicação, manter a preferência conforme o comportamento existente.

CA4. Com acompanhar o sistema selecionado, alterar a preferência do dispositivo; a aparência acompanha a mudança. Com claro ou escuro explicitamente selecionado, a preferência do dispositivo não substitui a escolha.

CA5. No tema escuro, abrir as mesmas superfícies e estados do tema claro; manter conteúdo e ações equivalentes, identidade FinAI, textos legíveis e distinção visual entre superfícies, bordas, foco, erros e demais estados existentes.

CA6. Verificar as telas atuais em 360×800, 390×844, 430×932, 600×960, 820×1180, 1024×768, 1366×768, 1440×900 e 1920×1080; layout e navegação se adaptam sem rolagem horizontal da página, mantendo acesso às operações atuais. Conferir também as transições 767/768px e 1024/1025px, incluindo redimensionamento após recolher a navegação desktop; cada largura aplica o modo de R4 e mantém os destinos e ações atuais disponíveis.

CA7. Navegar e utilizar formulários, menus e diálogos atuais com mouse e teclado; preservar rótulos, foco visível e estados aplicáveis de hover, ativo, desabilitado e carregamento demonstrados no design ou existentes na aplicação.

CA8. Executar ações atuais com dados válidos e inválidos, onde aplicável; campos, validações, mensagens, cancelamentos, confirmações e resultados funcionais permanecem equivalentes após a adequação visual. O mesmo vale para restrições de acesso de visitantes e usuários autenticados.

CA9. Ao navegar pela entrega, não encontrar novas páginas financeiras, dados fictícios, operações simuladas, rótulos de armazenamento apenas local ou assistente simulado apresentados como funcionalidades prontas. O dashboard atual permanece sem antecipar as capacidades da Feature Dashboard financeiro.

CA10. Em largura de até 767px, reconhecer a marca no topo e a navegação principal fixa no rodapé em largura total, com base de 56px mais a área segura, ícones de 24px, alvos de pelo menos 44px, destino ativo e nomes acessíveis mesmo sem legenda visível. Percorrer até o fim da página, focar controles e abrir menus/diálogos: a navegação não encobre ações, mensagens ou foco, e o acesso à conta, configurações, links e saída permanece disponível.

CA11. De 768 a 1024px inclusive, verificar lateral compacta de 72px mais a área segura, marca compacta, alvos de pelo menos 48px e conteúdo ao lado, sem navegação inferior. A partir de 1025px, verificar navegação lateral desktop com recolhimento atual preservado. Em ambas as faixas, comparar contorno de 1px, raio de 16px, margem de 8px, entorno contínuo e cabeçalho transparente com design-input-002, nos temas claro e escuro; em sistema, manter a preferência existente. Navegação, conta, configurações, links, saída e estados de foco/ativo continuam acessíveis.

CA12. Percorrer todas as telas atuais de R1, menus e estados existentes, como visitante e usuário autenticado: títulos, textos, campos, ações, mensagens e conteúdo acessível próprio estão em português brasileiro, sem rótulos ingleses remanescentes da aplicação. Dados informados pelo usuário e marcas mantêm seu conteúdo original.

CA13. Executar ações atuais válidas e inválidas, incluindo acesso, recuperação/verificação de e-mail, perfil, senha, exclusão, 2FA e chaves de acesso: feedback, validação e e-mails controlados pela aplicação estão em português, com os mesmos efeitos e restrições. Inglês não reaparece no conteúdo próprio por fallback.

CA14. Abrir e utilizar cada caminho próprio do mapa aprovado, por links, formulários e comunicação nova; as URLs principais estão em português. /login continua atendendo acesso e envio do login no mesmo endereço, e / permanece como início. Preservar destinos, parâmetros e métodos, inclusive nas operações que não abrem uma página própria.

CA15. Acessar todos os caminhos anteriores, incluindo favoritos, envio de formulários antigos e e-mails de recuperação/verificação gerados antes da mudança: os acessos válidos continuam realizando somente as operações esperadas. Testar token, assinatura ou prazo inválidos e acesso sem permissão: manter a recusa original com mensagens próprias em português, sem ampliar validade, contornar proteção ou duplicar efeitos.

CA16. Nos temas e larguras já exigidos por CA3–CA7, os textos traduzidos e nomes acessíveis permanecem legíveis e utilizáveis, sem sobreposição, corte de ações ou rolagem horizontal da página. Navegação, retornos após autenticação e acesso a configurações e saída continuam disponíveis, consumindo a composição já aprovada.

## Dependências

Sem dependência de outra Feature do catálogo. O pacote de design informado é a referência visual. A implementação das próximas Features deve usar esta base; seus próprios campos, fluxos, dados e composições de tela serão aceitos nos respectivos requisitos. A conclusão deste requisito não significa que a adequação visual já foi implementada.

## Dentro do escopo

Esta revisão acrescenta tradução integral dos textos próprios e dos endereços funcionais existentes, com compatibilidade dos endereços anteriores e exceção expressa de /login, conforme R8–R11 e CA12–CA16.

Adequação visual de todas as telas, componentes, estados e navegação atuais; identidade FinAI; responsividade; temas claro e escuro com preferência acompanhar o sistema; preservação do comportamento existente. Critérios visuais aplicáveis à base compartilhada, sem antecipar as composições específicas das Features financeiras.

## Fora do escopo

Novas telas e destinos de Transações ou Assistente; operações financeiras; dashboard com dados reais; integração de IA; mudanças de autenticação, perfil, permissões ou validações; remoção de recursos existentes; decomposição em tarefas técnicas. As capacidades novas pertencem às demais Features do catálogo aprovado.

## Requisito canônico

Documento aprovado por Mário Tinelli: docs/harness/features/1016101-adequacao-visual-do-finai/feature.md
<!-- project-flow:end -->