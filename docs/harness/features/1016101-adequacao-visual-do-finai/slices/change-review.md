# Revisão de mudança do requisito

Classificação semântica: **functional**  
Revisão: 4  
Hash da revisão: `1223d205919faaa1c0b7b47343616f4b700c4b6d440e8b1c01926f80243f3e01`

## Resumo

Tradução integral da interface e URLs em duas DEV de2h, com /login preservada e endereços anteriores funcionais. Preservar as sete filhas atuais e seus critérios; QA existente passa a2h e recebe oito condições adicionais, mantendo as27 vigentes. Novas DEV Sequencing7/8; QA9; demais posições8–23 avançam para10–25. Revisão anterior de layout permanece histórica e concluída.

## Mudanças observadas

### translation-R2 — functional

- Antes: Adequar aparência preserva os campos, validações, mensagens funcionais, operações, permissões, destinos e preferências existentes. Não acrescentar regras de autenticação ou financeiras nesta entrega.
- Agora: Adequar aparência e idioma preserva campos, validações, significado das mensagens funcionais, operações, permissões, destinos e preferências existentes. Traduzir a apresentação dos textos para português brasileiro sem alterar seus efeitos. Os novos endereços seguem R9 e os antigos continuam funcionais conforme R10. Não acrescentar regras de autenticação ou financeiras nesta entrega.
- Justificativa: Revisão de idioma e URLs expressamente aprovada por Mário Tinelli, incluindo manutenção de /login, todos os caminhos anteriores e configurações.

### translation-R8 — functional

- Antes: Obrigação não existente na versão anterior aprovada.
- Agora: Apresentar em português brasileiro todos os textos controlados pela aplicação nas superfícies atuais de R1: página pública, navegação, títulos e breadcrumbs, formulários, botões, placeholders, avisos, feedback, estados vazios/carregamento/erro, validações, diálogos, textos de ajuda, tooltips e nomes/instruções acessíveis. Abranger os e-mails e notificações já enviados pela aplicação, inclusive recuperação e verificação de e-mail; preservar as mensagens que já estejam corretamente traduzidas. O idioma padrão e o fallback não devem reintroduzir inglês em conteúdo próprio exibido ao usuário.
- Justificativa: Revisão de idioma e URLs expressamente aprovada por Mário Tinelli, incluindo manutenção de /login, todos os caminhos anteriores e configurações.

### translation-R9 — functional

- Antes: Obrigação não existente na versão anterior aprovada.
- Agora: Usar caminhos em português, sem acentos e conforme o mapa de URLs desta regra, para as jornadas e operações próprias existentes, incluindo links, formulários, notificações, redirecionamentos e retomada após autenticação. /login permanece /login por decisão expressa do usuário; a página inicial permanece /. Preservar métodos HTTP, parâmetros, valores, tokens, assinaturas, expiração, restrições de acesso e mecanismos de segurança. Identificadores internos de rotas, classes e campos não precisam ser traduzidos. Endpoints padronizados de protocolo e infraestrutura, como /.well-known/passkey-endpoints, não recebem tradução que viole seu contrato.
- Justificativa: Revisão de idioma e URLs expressamente aprovada por Mário Tinelli, incluindo manutenção de /login, todos os caminhos anteriores e configurações.

### translation-R10 — functional

- Antes: Obrigação não existente na versão anterior aprovada.
- Agora: Todos os endereços próprios anteriores continuam funcionando para seus mesmos destinos e operações, inclusive favoritos, formulários abertos e links de recuperação/verificação já enviados por e-mail. As navegações e comunicações novas passam a usar os caminhos principais em português, com /login preservado. Links antigos válidos mantêm o efeito e o prazo originais; links inválidos, expirados ou adulterados continuam recusados. Compatibilidade não reduz proteção nem repete operações.
- Justificativa: Revisão de idioma e URLs expressamente aprovada por Mário Tinelli, incluindo manutenção de /login, todos os caminhos anteriores e configurações.

### translation-R11 — functional

- Antes: Obrigação não existente na versão anterior aprovada.
- Agora: A tradução preserva a identidade, temas claro/escuro/sistema, composição responsiva e finalidade de cada tela. Não traduzir conteúdo informado pelos usuários, nomes próprios, marcas, endereços de terceiros nem valores técnicos que precisem permanecer exatos. Textos nativos do navegador, sistema operacional ou autenticador seguem o idioma desses ambientes; os textos controlados pelo FinAI permanecem em português. Esta revisão não cria seletor de idioma ou novas telas financeiras.
- Justificativa: Revisão de idioma e URLs expressamente aprovada por Mário Tinelli, incluindo manutenção de /login, todos os caminhos anteriores e configurações.

### translation-CA12 — functional

- Antes: Obrigação não existente na versão anterior aprovada.
- Agora: Percorrer todas as telas atuais de R1, menus e estados existentes, como visitante e usuário autenticado: títulos, textos, campos, ações, mensagens e conteúdo acessível próprio estão em português brasileiro, sem rótulos ingleses remanescentes da aplicação. Dados informados pelo usuário e marcas mantêm seu conteúdo original.
- Justificativa: Revisão de idioma e URLs expressamente aprovada por Mário Tinelli, incluindo manutenção de /login, todos os caminhos anteriores e configurações.

### translation-CA13 — functional

- Antes: Obrigação não existente na versão anterior aprovada.
- Agora: Executar ações atuais válidas e inválidas, incluindo acesso, recuperação/verificação de e-mail, perfil, senha, exclusão, 2FA e chaves de acesso: feedback, validação e e-mails controlados pela aplicação estão em português, com os mesmos efeitos e restrições. Inglês não reaparece no conteúdo próprio por fallback.
- Justificativa: Revisão de idioma e URLs expressamente aprovada por Mário Tinelli, incluindo manutenção de /login, todos os caminhos anteriores e configurações.

### translation-CA14 — functional

- Antes: Obrigação não existente na versão anterior aprovada.
- Agora: Abrir e utilizar cada caminho próprio do mapa aprovado, por links, formulários e comunicação nova; as URLs principais estão em português. /login continua atendendo acesso e envio do login no mesmo endereço, e / permanece como início. Preservar destinos, parâmetros e métodos, inclusive nas operações que não abrem uma página própria.
- Justificativa: Revisão de idioma e URLs expressamente aprovada por Mário Tinelli, incluindo manutenção de /login, todos os caminhos anteriores e configurações.

### translation-CA15 — functional

- Antes: Obrigação não existente na versão anterior aprovada.
- Agora: Acessar todos os caminhos anteriores, incluindo favoritos, envio de formulários antigos e e-mails de recuperação/verificação gerados antes da mudança: os acessos válidos continuam realizando somente as operações esperadas. Testar token, assinatura ou prazo inválidos e acesso sem permissão: manter a recusa original com mensagens próprias em português, sem ampliar validade, contornar proteção ou duplicar efeitos.
- Justificativa: Revisão de idioma e URLs expressamente aprovada por Mário Tinelli, incluindo manutenção de /login, todos os caminhos anteriores e configurações.

### translation-CA16 — functional

- Antes: Obrigação não existente na versão anterior aprovada.
- Agora: Nos temas e larguras já exigidos por CA3–CA7, os textos traduzidos e nomes acessíveis permanecem legíveis e utilizáveis, sem sobreposição, corte de ações ou rolagem horizontal da página. Navegação, retornos após autenticação e acesso a configurações e saída continuam disponíveis, consumindo a composição já aprovada.
- Justificativa: Revisão de idioma e URLs expressamente aprovada por Mário Tinelli, incluindo manutenção de /login, todos os caminhos anteriores e configurações.

## Impactos localizados

### Tarefas

- `dev-1` — Idioma e caminhos tornam-se obrigações adicionais; preservar as DEV históricas, representar o complemento por duas novas DEV e atualizar a mesma QA.
- `dev-2` — Idioma e caminhos tornam-se obrigações adicionais; preservar as DEV históricas, representar o complemento por duas novas DEV e atualizar a mesma QA.
- `dev-3` — Idioma e caminhos tornam-se obrigações adicionais; preservar as DEV históricas, representar o complemento por duas novas DEV e atualizar a mesma QA.
- `dev-4` — Idioma e caminhos tornam-se obrigações adicionais; preservar as DEV históricas, representar o complemento por duas novas DEV e atualizar a mesma QA.
- `dev-5` — Idioma e caminhos tornam-se obrigações adicionais; preservar as DEV históricas, representar o complemento por duas novas DEV e atualizar a mesma QA.
- `qa` — Idioma e caminhos tornam-se obrigações adicionais; preservar as DEV históricas, representar o complemento por duas novas DEV e atualizar a mesma QA.

### Critérios de aceite

- Nenhum.

### Itens de cobertura

- `R2` — R2 passa a preservar o significado ao traduzir mensagens e trocar URLs com compatibilidade.

### Dependências

- `blocks:dev-3:qa` — Preservar este bloqueio histórico e acrescentar o bloqueio das novas entregas de tradução da jornada à mesma QA.
- `blocks:dev-4:qa` — Preservar este bloqueio histórico e acrescentar o bloqueio das novas entregas de tradução da jornada à mesma QA.
- `blocks:dev-5:qa` — Preservar este bloqueio histórico e acrescentar o bloqueio das novas entregas de tradução da jornada à mesma QA.

### Condições de teste

- Nenhum.

## Itens que permanecem válidos

### Tarefas

- `dev-layout-revision-001` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.

### Critérios de aceite

- `dev-1:criterion-1` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `dev-1:criterion-2` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `dev-1:criterion-3` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `dev-1:criterion-4` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `dev-1:criterion-5` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `dev-1:criterion-6` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `dev-2:criterion-1` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `dev-2:criterion-2` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `dev-2:criterion-3` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `dev-2:criterion-4` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `dev-2:criterion-5` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `dev-3:criterion-1` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `dev-3:criterion-2` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `dev-3:criterion-3` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `dev-3:criterion-4` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `dev-3:criterion-5` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `dev-3:criterion-6` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `dev-4:criterion-1` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `dev-4:criterion-2` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `dev-4:criterion-3` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `dev-4:criterion-4` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `dev-4:criterion-5` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `dev-4:criterion-6` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `dev-5:criterion-1` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `dev-5:criterion-2` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `dev-5:criterion-3` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `dev-5:criterion-4` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `dev-5:criterion-5` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `dev-5:criterion-6` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.

### Itens de cobertura

- `CA1` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `CA2` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `CA3` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `CA4` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `CA5` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `CA6` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `CA7` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `CA8` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `CA9` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `R1` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `R3` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `R4` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `R5` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `R6` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `R7` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `V-Acesso` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `V-Conta` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `V-Publica` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `V-Seguranca` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.

### Dependências

- `blocks:dev-1:qa` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `blocks:dev-2:qa` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `relation-layout-qa-001` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.

### Condições de teste

- `CT-001` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `CT-002` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `CT-003` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `CT-004` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `CT-005` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `CT-006` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `CT-007` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `CT-008` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `CT-009` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `CT-010` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `CT-011` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `CT-012` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `CT-013` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `CT-014` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `CT-015` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `CT-016` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `CT-017` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `CT-018` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `CT-019` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `CT-020` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `CT-021` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `CT-022` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `CT-023` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `CT-024` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `CT-025` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `CT-026` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.
- `CT-027` — Permanece válido e preservado; a nova tradução acrescenta obrigações próprias, mantendo os resultados, dados, permissões e critérios já aprovados. O layout revisado já foi aplicado no ciclo anterior.

## Condições vigentes

`condicoes-teste-r003.docx` — `f278e8d71ed37226e4b92f4377bf27585508e742eaad690e955d3ca181418b04`

## Inclusões autorizadas nas condições

- `CT-028` — Textos próprios e acessíveis das jornadas iniciais em pt-BR.
- `CT-029` — Configurações, conta e segurança integralmente em pt-BR.
- `CT-030` — Validações, feedback e e-mails controlados pela aplicação em pt-BR.
- `CT-031` — Mapa completo de caminhos principais em português com /login preservado.
- `CT-032` — Compatibilidade de navegação pelos endereços anteriores.
- `CT-033` — Links de e-mails antigos, com assinatura/token/prazo válidos e inválidos.
- `CT-034` — Métodos e efeitos preservados nos endpoints antigos de escrita.
- `CT-035` — Dados do usuário, temas, acessibilidade e encaixe responsivo preservados.

## Requisitos da revisão

- `R1` — A entrega abrange a página inicial atual, cadastro, login, recuperação e redefinição de senha, confirmação de senha, verificação de e-mail, desafio de dois fatores, dashboard atual, perfil, alteração de senha, aparência, configuração de dois fatores e passkeys, incluindo seus estados e componentes existentes. Essa lista é inventário do código, não comprovação de aceite funcional anterior.
- `R2` — Adequar aparência e idioma preserva campos, validações, significado das mensagens funcionais, operações, permissões, destinos e preferências existentes. Traduzir a apresentação dos textos para português brasileiro sem alterar seus efeitos. Os novos endereços seguem R9 e os antigos continuam funcionais conforme R10. Não acrescentar regras de autenticação ou financeiras nesta entrega.
- `R3` — A referência clara usa fundo #F5F7F8, superfícies brancas, texto #172622, texto secundário #52615C, verde principal #145C46, verde positivo #146345, vermelho negativo #A12B36, bordas #D6DFDB e destaque suave #E4F0E9. Preservar a hierarquia do design: títulos de destaque em Georgia e corpo em system-ui; controles com raio de 8px e painéis com 16px; espaçamento, bordas, sombras, estados e proporções conforme o pacote.
- `R4` — Aplicar a revisão design-input-002 à estrutura autenticada compartilhada: até 767px, marca no topo e navegação principal fixa no rodapé, de largura total, com base de 56px acrescida da área segura inferior e ícones de 24px, alvos de pelo menos 44px, sem legendas visíveis e com nomes acessíveis; de 768 a 1024px inclusive, navegação lateral compacta de 72px acrescida da área segura lateral, marca compacta, alvos de pelo menos 48px e conteúdo ao lado, sem barra inferior; a partir de 1025px, navegação lateral desktop, preservando o recolhimento e os destinos atuais. A partir de 768px, apresentar o conteúdo em superfície com fundo de trabalho, contorno de 1px, raio de 16px e margem de 8px, com a navegação integrada ao entorno e cabeçalho transparente conforme a referência. Reservar espaço para navegação e áreas seguras, sem encobrir conteúdo, foco, mensagens ou controles. Preservar acesso ao menu da conta, configurações, links e saída em todas as larguras, adaptando sua apresentação quando o protótipo esconder o rodapé lateral. Não transportar destinos financeiros futuros para as telas atuais.
- `R5` — Preservar claro, escuro e acompanhar o sistema. A variante escura é uma adaptação aprovada da identidade fornecida, mantendo hierarquia visual, distinção entre superfícies, leitura dos textos e identificação dos estados. Não reutilizar o tema escuro neutro do starter sem adequação à identidade FinAI.
- `R6` — A marca FinAI substitui a identidade visual genérica do starter nas superfícies atuais. Não apresentar rótulos do protótipo que afirmem armazenamento apenas no navegador ou assistente simulado; persistência e IA real serão tratadas pelas Features responsáveis.
- `R7` — A base visual é aceita sobre as telas atuais. Não criar páginas de Transações ou Assistente, formulários financeiros, números demonstrativos ou operações simuladas nesta Feature. As novas telas e suas composições específicas seguem a base nas próximas Features.
- `R8` — Apresentar em português brasileiro todos os textos controlados pela aplicação nas superfícies atuais de R1: página pública, navegação, títulos e breadcrumbs, formulários, botões, placeholders, avisos, feedback, estados vazios/carregamento/erro, validações, diálogos, textos de ajuda, tooltips e nomes/instruções acessíveis. Abranger os e-mails e notificações já enviados pela aplicação, inclusive recuperação e verificação de e-mail; preservar as mensagens que já estejam corretamente traduzidas. O idioma padrão e o fallback não devem reintroduzir inglês em conteúdo próprio exibido ao usuário.
- `R9` — Usar caminhos em português, sem acentos e conforme o mapa de URLs desta regra, para as jornadas e operações próprias existentes, incluindo links, formulários, notificações, redirecionamentos e retomada após autenticação. /login permanece /login por decisão expressa do usuário; a página inicial permanece /. Preservar métodos HTTP, parâmetros, valores, tokens, assinaturas, expiração, restrições de acesso e mecanismos de segurança. Identificadores internos de rotas, classes e campos não precisam ser traduzidos. Endpoints padronizados de protocolo e infraestrutura, como /.well-known/passkey-endpoints, não recebem tradução que viole seu contrato.
- `R10` — Todos os endereços próprios anteriores continuam funcionando para seus mesmos destinos e operações, inclusive favoritos, formulários abertos e links de recuperação/verificação já enviados por e-mail. As navegações e comunicações novas passam a usar os caminhos principais em português, com /login preservado. Links antigos válidos mantêm o efeito e o prazo originais; links inválidos, expirados ou adulterados continuam recusados. Compatibilidade não reduz proteção nem repete operações.
- `R11` — A tradução preserva a identidade, temas claro/escuro/sistema, composição responsiva e finalidade de cada tela. Não traduzir conteúdo informado pelos usuários, nomes próprios, marcas, endereços de terceiros nem valores técnicos que precisem permanecer exatos. Textos nativos do navegador, sistema operacional ou autenticador seguem o idioma desses ambientes; os textos controlados pelo FinAI permanecem em português. Esta revisão não cria seletor de idioma ou novas telas financeiras.
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
- `CA12` — Percorrer todas as telas atuais de R1, menus e estados existentes, como visitante e usuário autenticado: títulos, textos, campos, ações, mensagens e conteúdo acessível próprio estão em português brasileiro, sem rótulos ingleses remanescentes da aplicação. Dados informados pelo usuário e marcas mantêm seu conteúdo original.
- `CA13` — Executar ações atuais válidas e inválidas, incluindo acesso, recuperação/verificação de e-mail, perfil, senha, exclusão, 2FA e chaves de acesso: feedback, validação e e-mails controlados pela aplicação estão em português, com os mesmos efeitos e restrições. Inglês não reaparece no conteúdo próprio por fallback.
- `CA14` — Abrir e utilizar cada caminho próprio do mapa aprovado, por links, formulários e comunicação nova; as URLs principais estão em português. /login continua atendendo acesso e envio do login no mesmo endereço, e / permanece como início. Preservar destinos, parâmetros e métodos, inclusive nas operações que não abrem uma página própria.
- `CA15` — Acessar todos os caminhos anteriores, incluindo favoritos, envio de formulários antigos e e-mails de recuperação/verificação gerados antes da mudança: os acessos válidos continuam realizando somente as operações esperadas. Testar token, assinatura ou prazo inválidos e acesso sem permissão: manter a recusa original com mensagens próprias em português, sem ampliar validade, contornar proteção ou duplicar efeitos.
- `CA16` — Nos temas e larguras já exigidos por CA3–CA7, os textos traduzidos e nomes acessíveis permanecem legíveis e utilizáveis, sem sobreposição, corte de ações ou rolagem horizontal da página. Navegação, retornos após autenticação e acesso a configurações e saída continuam disponíveis, consumindo a composição já aprovada.
- `V-Publica` — Desdobramento de R1/R2/CA1/CA6/CA8: composição da página inicial atual com identidade FinAI, preservando conteúdo funcional e destinos.
- `V-Acesso` — Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de cadastro, login, recuperação/redefinição e verificação de e-mail.
- `V-Conta` — Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de perfil, senha, aparência e exclusão de conta.
- `V-Seguranca` — Desdobramento de R1/R2/CA1/CA6/CA8: composição e estados de 2FA, confirmação de senha e passkeys.
## Preservação

Filhas publicadas, decisões sobre filhas existentes/externas, estudos, divergências e evidências de dependência permanecem intactos enquanto esta revisão estiver pendente ou rejeitada.
