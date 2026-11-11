# Prévia completa — Acesso à conta pessoal

Revisão002, ainda não aprovada. Uma decisão do tech lead cobre a decomposição, condições de teste e exatamente as publicações/vínculos abaixo. Nenhuma filha de acesso foi criada.

## Entregas e estimativas

Os títulos DEV preservam [DEV] [WEB] [USUARIO] Acesso à conta pessoal - seguido do nome da entrega.

| # | Entrega | Esforço | Bloqueio de início |
| --- | --- | --- | --- |
| 1 | Cadastro e redefinição com política de senha consistente | 1.5h | QA visual #1016117 |
| 2 | Confirmação de e-mail com acesso restrito e retomada | 2h | QA visual #1016117 |
| 3 | Recuperação de senha com nova tentativa | 2h | QA visual #1016117 |
| QA | [QA] [WEB] [USUARIO] Acesso à conta pessoal | 1h | Os três DEV de acesso |

Total: **5,5h DEV + 1h QA = 6,5h**. Horas são esforço, não prazo de calendário.

A inspeção preserva login, saída, lembrar acesso, limitação após cinco falhas e o broker de redefinição, com cobertura existente na QA. Não criar trabalho para reconstruir essas capacidades. As três adaptações cobrem política de senha consistente, confirmação/restrição e retomada de falhas. As duas avaliações independentes e os valores da revisão001 permanecem no histórico. Mário Tinelli corrigiu explicitamente esta proposta para1,5h/2h/2h nos DEV e1h na QA,sem reduzir conteúdo,cobertura ou dependências.

## Dependências e vínculos exatos

- A base visual ainda não está implementada. Os três DEV de acesso aguardam a conclusão do aceite integrado [QA] [WEB] [USUARIO] Adequação visual do FinAI (#1016117), que depende dos cinco DEV visuais já publicados. A composição de acesso é fornecida por #1016114; não reconstruí-la.
- Criar três relações `blocks`: #1016117 → novo DEV1, #1016117 → novo DEV2 e #1016117 → novo DEV3. Cada alvo será exclusivamente o ID retornado na respectiva criação desta prévia.
- Criar três relações `blocks`: cada novo DEV → nova QA de acesso. Os extremos serão exclusivamente os IDs retornados para estas quatro filhas.
- Não há bloqueio interno real de início entre os DEV de acesso; sua conclusão integra a política de senha e as jornadas nomeadas nas descrições.
- O grafo relevante foi lido integralmente, com11issues e9relações atuais; os seis vínculos propostos não geram ciclos. Após criação, reler e verificar o grafo antes de configurar os bloqueios externos. Se houver diferença material, interromper e apresentar o delta; a mera substituição dos alvos pelos IDs retornados não pede nova confirmação equivalente.
- Preservar relações Feature→Feature e relações alheias; não remover ou substituir vínculos existentes.

## Campos e operações autorizáveis

- Pai nativo #1016104, [WEB] [USUARIO] Acesso à conta pessoal; estado atual New preservado.
- Criar três Task DEV (4) e uma Deliverable QA (5), em FinAi (65224), versão Sprint1 (20355), sem categoria, responsável ou datas.
- Filhas em New (1), prioridade Normal (4), com estimated_hours desta prévia.
- Criar/reconciliar os seis vínculos explicitados acima, sem duplicação ou mudança de estado do pai/fornecedor.
- Gerar da fonte aprovada o DOCX de condições, fazer upload e associá-lo somente à nova QA, preservando seus demais campos e anexos.
- O pai foi consultado com children: não há filhas existentes para adotar/excluir. Nenhuma task antiga é alvo ou contexto.
- Descrições funcionais completas abaixo são a autoridade de conteúdo. Após consentimento, os helpers vinculam metadados da aprovação, marcadores técnicos de recuperação, documento e IDs retornados, sem mudança material ou nova autorização equivalente.

## Documento incluído nesta decisão

Formato DOCX obrigatório com complemento Markdown. Arquivo final slices/condicoes-teste-r002.docx; complemento slices/condicoes-teste-r002.md. Destino: [QA] [WEB] [USUARIO] Acesso à conta pessoal, criada por esta publicação.

A fonte são as28condições integrais desta revisão, com os mesmos IDs e vínculos ao requisito. Conforme a skill, o arquivo oficial é gerado após o consentimento; o hash dos bytes é vinculado ao plano e a associação verificada no readback. Esta aprovação autoriza geração/upload/anexo derivados da mesma fonte, sem edição de conteúdo. Diferenças materiais exigem nova prévia.

## Descrições completas e campos por filha

### [DEV] [WEB] [USUARIO] Acesso à conta pessoal - Cadastro e redefinição com política de senha consistente

```json
{
  "project_id": 65224,
  "parent_issue_id": 1016104,
  "tracker_id": 4,
  "status_id": 1,
  "subject": "[DEV] [WEB] [USUARIO] Acesso à conta pessoal - Cadastro e redefinição com política de senha consistente",
  "assigned_to_id": null,
  "start_date": null,
  "due_date": null,
  "estimated_hours": 1.5,
  "priority_id": 4,
  "fixed_version_id": 20355
}
```

## Entrega

Completar a validação de senha no cadastro público e na redefinição esquecida, aplicando a mesma regra forte em teste e uso. Os formulários e demais validações já existem; falta a consistência exigida pelo requisito.

## Escopo e limites

Responsável pela política compartilhada e seus erros nos dois fluxos. Preservar campos, unicidade e jornadas existentes. Envio/confirmacão e retomada dos links pertencem às outras entregas.

## Critérios de aceite

- Cadastro e redefinição aceitam senha de 12 a 255 caracteres com maiúscula, minúscula, número e símbolo, não reconhecida como vazada e confirmação igual, com a mesma validação em teste e uso.
- Nos dois formulários, menos de 12 ou mais de 255 caracteres, ausência de qualquer classe, senha conhecida em vazamentos, ausência de senha/confirmação ou confirmação diferente impedem concluir com erro no campo, sem criar conta ou alterar senha indevidamente.
- Preservar nome/e-mail obrigatórios e até 255 caracteres, e-mail válido e único no cadastro e e-mail válido obrigatório na redefinição; não solicitar dados financeiros.
- Cadastro válido continua criando uma única conta e seguindo à confirmação. Redefinição válida retorna ao login; nova senha funciona e a anterior deixa de permitir novos logins, sem confirmar e-mail automaticamente.
- Nas telas e estados alterados, consumir marca, tipografia, paleta, campos, botões, erros e feedback da base FinAI em computador, tablet e celular, nos temas claro, escuro e acompanhar o sistema, sem reconstruir identidade ou layouts do fornecedor.

## Dependências

Início bloqueado pelo aceite integrado [QA] [WEB] [USUARIO] Adequação visual do FinAI (#1016117), dependente dos cinco DEV visuais e representante da base implementada e verificada. Após a liberação visual, pode avançar sem esperar os demais DEV de acesso. Para concluir a jornada integrada, usar a confirmação/restrição e a retomada de recuperação das entregas correspondentes, sem bloqueio interno de início.

## Referências

Item pai Redmine #1016104; regras/critérios R1, R2, R3, CA1, CA2, CA9, R9, CA12.

- design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; referência clara e adaptações aprovadas na Feature visual #1016101; linguagem de formulários, mensagens e ações de retomada. Não há composição própria de acesso no ZIP.
- Fornecedor de composição: [DEV] [WEB] [USUARIO] Adequação visual do FinAI - Página inicial e jornadas de acesso (#1016114); aceite integrado: [QA] [WEB] [USUARIO] Adequação visual do FinAI (#1016117).


### [DEV] [WEB] [USUARIO] Acesso à conta pessoal - Confirmação de e-mail com acesso restrito e retomada

```json
{
  "project_id": 65224,
  "parent_issue_id": 1016104,
  "tracker_id": 4,
  "status_id": 1,
  "subject": "[DEV] [WEB] [USUARIO] Acesso à conta pessoal - Confirmação de e-mail com acesso restrito e retomada",
  "assigned_to_id": null,
  "start_date": null,
  "due_date": null,
  "estimated_hours": 2,
  "priority_id": 4,
  "fixed_version_id": 20355
}
```

## Entrega

Completar a confirmação de e-mail, do envio inicial à retomada, e impedir que contas não confirmadas acessem perfil e demais funcionalidades. Confirmação própria e reenvio já existem; faltam restrição integral e orientação nas falhas de link/envio.

## Escopo e limites

Responsável pelo envio inicial, jornada restrita de confirmação/reenvio/saída, links de confirmação e restrição da área do produto. Preservar login, lembrar e recuperação atuais. A política de senha e a retomada da recuperação são fornecidas pelas outras entregas.

## Critérios de aceite

- Cadastro público válido cria uma única conta, envia confirmação e orienta o titular; receber o e-mail não libera o produto antes de confirmar.
- Conta não confirmada, com sessão normal ou lembrada, não acessa diretamente área inicial, perfil, configurações ou funcionalidades do produto. Mantém confirmação, reenvio, saída e caminho de recuperação; pode sair e usar a jornada pública existente quando necessário, sem novo mecanismo autenticado.
- Titular com link próprio válido confirma e acessa a área inicial, autenticando-se quando necessário. Reabrir link ainda válido de conta já confirmada conserva a confirmação.
- Links inválidos, expirados ou de outra conta não confirmam endereço indevido nem liberam o sistema; apresentar orientação e caminho para solicitar novo link próprio.
- Falha de envio no cadastro/reenvio informa que o envio não concluiu e orienta nova tentativa, sem sucesso fictício. Após restabelecimento, retomar sem contas duplicadas nem titular sem caminho de confirmação/recuperação.
- Preservar credenciais corretas/incorretas, destino solicitado, lembrar, bloqueio após cinco falhas e saída; contas confirmadas continuam usando operações permitidas.
- Nas telas e estados alterados, consumir marca, tipografia, paleta, campos, botões, erros e feedback da base FinAI em computador, tablet e celular, nos temas claro, escuro e acompanhar o sistema, sem reconstruir identidade ou layouts do fornecedor.

## Dependências

Início bloqueado pelo aceite integrado [QA] [WEB] [USUARIO] Adequação visual do FinAI (#1016117), dependente dos cinco DEV visuais e representante da base implementada e verificada. Após a liberação visual, pode iniciar sem esperar os demais DEV de acesso. Para concluir a jornada integrada, usar Cadastro e redefinição com política de senha consistente e Recuperação de senha com nova tentativa.

## Referências

Item pai Redmine #1016104; regras/critérios R1, R2, R4, R6, R7, R8, CA1, CA3, CA4, CA5, CA6, CA7, CA11, CA11-Confirmacao, R9, CA12.

- design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; referência clara e adaptações aprovadas na Feature visual #1016101; linguagem de formulários, mensagens e ações de retomada. Não há composição própria de acesso no ZIP.
- Fornecedor de composição: [DEV] [WEB] [USUARIO] Adequação visual do FinAI - Página inicial e jornadas de acesso (#1016114); aceite integrado: [QA] [WEB] [USUARIO] Adequação visual do FinAI (#1016117).


### [DEV] [WEB] [USUARIO] Acesso à conta pessoal - Recuperação de senha com nova tentativa

```json
{
  "project_id": 65224,
  "parent_issue_id": 1016104,
  "tracker_id": 4,
  "status_id": 1,
  "subject": "[DEV] [WEB] [USUARIO] Acesso à conta pessoal - Recuperação de senha com nova tentativa",
  "assigned_to_id": null,
  "start_date": null,
  "due_date": null,
  "estimated_hours": 2,
  "priority_id": 4,
  "fixed_version_id": 20355
}
```

## Entrega

Completar os estados de recuperação quando o envio falhar ou o link de redefinição for inválido, expirado ou já usado. O pedido genérico e o broker já existem; falta retomada sem apresentar envio ou alteração como concluídos indevidamente.

## Escopo e limites

Responsável pela solicitação/redefinição esquecida e seus novos pedidos. Preservar resposta genérica, validade de 60 minutos, uso único, retorno ao login e estado de confirmação do e-mail. Não reimplementar a política de senha nem ampliar autenticação.

## Critérios de aceite

- Com envio disponível, pedir recuperação para conta existente ou inexistente mantém a mesma resposta genérica; o titular cadastrado recebe o link.
- Falha no envio orienta nova tentativa sem afirmar sucesso ou revelar explicitamente existência da conta; depois de restabelecer, novo pedido permite receber link utilizável.
- Link inválido, expirado após 60 minutos ou já utilizado não altera senha e oferece novo pedido; novo link válido permite retomar.
- Link próprio, não usado e válido, com senha conforme a política compartilhada e confirmação igual, redefine e retorna ao login; senha nova funciona e a anterior não permite novos logins.
- Redefinir conta não confirmada não confirma e-mail nem libera a área do produto; preservar validações e erros, sem alteração indevida.
- Nas telas e estados alterados, consumir marca, tipografia, paleta, campos, botões, erros e feedback da base FinAI em computador, tablet e celular, nos temas claro, escuro e acompanhar o sistema, sem reconstruir identidade ou layouts do fornecedor.

## Dependências

Início bloqueado pelo aceite integrado [QA] [WEB] [USUARIO] Adequação visual do FinAI (#1016117), dependente dos cinco DEV visuais e representante da base implementada e verificada. Pode iniciar com a recuperação existente após a liberação visual. Para concluir a redefinição integrada, usar Cadastro e redefinição com política de senha consistente. Login, saída e confirmação seguem nas jornadas existentes/entrega responsável, sem bloqueio interno de início.

## Referências

Item pai Redmine #1016104; regras/critérios R2, R3, R4, R5, R8, CA2, CA8, CA9, CA10, CA11, CA11-Recuperacao, R9, CA12.

- design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; referência clara e adaptações aprovadas na Feature visual #1016101; linguagem de formulários, mensagens e ações de retomada. Não há composição própria de acesso no ZIP.
- Fornecedor de composição: [DEV] [WEB] [USUARIO] Adequação visual do FinAI - Página inicial e jornadas de acesso (#1016114); aceite integrado: [QA] [WEB] [USUARIO] Adequação visual do FinAI (#1016117).


### [QA] [WEB] [USUARIO] Acesso à conta pessoal

```json
{
  "project_id": 65224,
  "parent_issue_id": 1016104,
  "tracker_id": 5,
  "status_id": 1,
  "subject": "[QA] [WEB] [USUARIO] Acesso à conta pessoal",
  "assigned_to_id": null,
  "start_date": null,
  "due_date": null,
  "estimated_hours": 1,
  "priority_id": 4,
  "fixed_version_id": 20355
}
```

## Objetivo

Verificar o acesso completo com ajustes de senha, restrição e retomada, preservando as jornadas existentes e consumindo a base visual FinAI.

## Jornadas integradas

- Cadastro público e confirmação: Cadastrar nome/e-mail válidos, senha conforme R3 e confirmação igual. Resultado esperado: Uma conta, sem convite/dados financeiros; enviar link e orientar confirmar, sem acesso ao produto.
- Campos obrigatórios: Omitir separadamente nome/e-mail/senha/confirmação no cadastro e os campos aplicáveis na redefinição. Resultado esperado: Impedir conclusão com erro; sem conta ou senha alterada indevidamente.
- Nome e e-mail nos limites: Usar entradas válidas de255 e256caracteres; e-mail inválido e duplicado. Resultado esperado: Até255aceito; excesso/formato/duplicação recusados, sem nova conta indevida.
- Senha nos limites: Nos dois fluxos usar senhas de composição completa não-vazadas com11,12,255 e256caracteres. Resultado esperado: 12/255aceitas;11/256recusadas com erro; mesma regra em teste e uso.
- Composição da senha: Nos dois fluxos omitir separadamente maiúscula, minúscula, número e símbolo, mantendo demais condições. Resultado esperado: Cada falta recusada; composição completa não rejeitada por esse motivo.
- Senha conhecida em vazamentos: Com dado controlado da verificação de senha vazada, tentar os dois fluxos com tamanho/composição válidos. Resultado esperado: Recusar ambos com erro e sem persistência indevida.
- Confirmação diferente: Informar senha válida com confirmação diferente no cadastro e redefinição. Resultado esperado: Impedir e indicar erro sem criar conta ou alterar senha.
- Visitante na área protegida: Sem sessão, abrir área inicial, perfil e configurações protegidas. Resultado esperado: Exigir login sem mostrar funcionalidades do produto.
- Conta não confirmada: Entrar sem confirmar e tentar área inicial, perfil GET/PATCH e configurações; repetir com lembrar. Resultado esperado: Manter restrição, orientação, reenvio e saída; sem acesso/alteração indevida no produto.
- Recuperar antes de confirmar: Como não-confirmado autenticado, sair e seguir ao pedido público existente. Resultado esperado: Permitir a jornada sem liberar produto ou dispensar confirmação.
- Confirmar link próprio: Abrir link próprio válido iniciando com e sem sessão. Resultado esperado: Autenticar quando necessário, confirmar titular e liberar área inicial.
- Confirmação inválida: Alterar dados/assinatura do link e abrir como titular não confirmado. Resultado esperado: Não confirmar nem liberar; orientar novo link próprio.
- Confirmação expirada: Abrir link após sua validade. Resultado esperado: Não confirmar/liberar; orientar e oferecer novo pedido.
- Confirmação de outra conta: Como A não confirmado, abrir link válido de B. Resultado esperado: Não confirmar A/B indevidamente; caminho de novo pedido próprio de A.
- Reabrir confirmação: Confirmar conta e reabrir o mesmo link ainda válido. Resultado esperado: Manter confirmação e permitir área inicial.
- Falha de envio inicial: Provocar falha no cadastro, restaurar envio e repetir conforme orientação. Resultado esperado: Informar falha/retomada sem falso sucesso, duplicação ou titular sem caminho de confirmação/recuperação.
- Falha no reenvio: Como não-confirmado, provocar falha de reenvio, restaurar e tentar de novo. Resultado esperado: Não alegar envio concluído; após retomada, receber link e confirmar.
- Login e destino: Entrar diretamente e após solicitar destino protegido; testar credenciais incorretas. Resultado esperado: Corretas acessam área inicial/destino; incorretas não autenticam.
- Cinco falhas e espera: Para mesmo e-mail/origem, falhar cinco vezes e tentar durante bloqueio e após espera. Resultado esperado: Informar espera sem autenticar durante bloqueio; após prazo, aceitar credenciais válidas.
- Saída e lembrança: Entrar/sair e reabrir área protegida com lembrar marcado e desmarcado. Resultado esperado: Retornar à página pública e exigir novo login, inclusive após lembrança.
- Pedido genérico: Com envio disponível, pedir recuperação para conta existente e inexistente. Resultado esperado: Mesma resposta; titular cadastrado recebe link sem revelação pela resposta.
- Redefinição válida: Com link próprio não usado antes de60min, informar senha conforme R3/confirmação e testar senha anterior/nova. Resultado esperado: Retornar ao login; nova funciona e antiga não permite novos logins.
- Redefinir sem confirmar e-mail: Redefinir conta não confirmada e entrar com senha nova. Resultado esperado: Senha muda, e-mail permanece não confirmado e produto continua restrito.
- Recuperação inválida: Tentar redefinir com link inválido e usar novo pedido. Resultado esperado: Não alterar; orientar e oferecer novo link para retomada.
- Recuperação expirada: Tentar após ultrapassar60min da emissão; solicitar outro link. Resultado esperado: Recusar sem alterar e permitir retomar com novo link válido.
- Recuperação já usada: Redefinir e reutilizar o mesmo link para outra senha. Resultado esperado: Não alterar de novo; recusar e oferecer novo pedido.
- Falha de envio de recuperação: Provocar falha, restaurar e solicitar de novo. Resultado esperado: Orientar sem sucesso fictício/revelação explícita da conta; titular recebe link após retomada.
- Integração visual: Em computador/tablet/celular, claro/escuro/sistema, percorrer as telas e os novos estados de erro/retomada. Comparar com design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; referência clara e adaptações aprovadas na Feature visual #1016101 e o fornecedor de composição #1016114 após base verificada. Resultado esperado: Identidade, campos, botões, erros e ações coerentes/usáveis, sem reconstruir a aparência fornecida.

## Regras e permissões

- Cadastro aberto e campos/limites de R2, com R3 consistente nos dois fluxos em teste e uso.
- Produto exige autenticação e e-mail próprio confirmado; receber mensagem ou redefinir senha não confirma a conta.
- Recuperação60min e uso único; preservar cinco falhas/espera no login e saída explícita com lembrar.
- Consumir base visual implementada/verificada; conferir os estados de acesso novos sem repetir a homologação visual integral do fornecedor.

## Impactos relacionados

- Preservar login, saída, lembrar e limitação existentes, sem criar DEV para reconstruí-los.
- Restrições incluem acessos diretos a perfil e configurações e o estado de e-mail confirmado.
- Falhas de transporte/links não causam duplicação, senha alterada indevidamente ou sucesso fictício.

## Critérios de conclusão

- Executar CT-001 a CT-028 do documento aprovado, com resultado observado e evidência por condição.
- Confirmar jornadas, fronteiras, titularidade/tempo, retomada e preservação; indicar desvios e impedimentos sem aprovar condição não executada.
- Conservar a revisão de condições associada à QA e registrar preparação, resultado e reteste delimitado conforme executado.

## Referências

Item pai Redmine #1016104; regras/critérios R1, R2, R3, R4, R5, R6, R7, R8, R9, CA1, CA2, CA3, CA4, CA5, CA6, CA7, CA8, CA9, CA10, CA11, CA12, CA11-Confirmacao, CA11-Recuperacao.


## Condições de teste integrais

# Condições de teste

## Contexto

Visitante e contas confirmadas/não confirmadas; links próprios, de outra conta, inválidos, expirados e usados; controle de tempo e falhas de envio reproduzíveis. Preparar fronteiras de campos/senha e dependência controlável para senha vazada. Consumir a base visual implementada e verificada nos cenários de computador, tablet, celular e claro/escuro/sistema. Os testes existentes foram apenas lidos; registrar evidência ou impedimento de cada condição executada posteriormente.

## Cadastro

### CT-001 — Cadastro público e confirmação

Verificação: Cadastrar nome/e-mail válidos, senha conforme R3 e confirmação igual.

Resultado esperado: Uma conta, sem convite/dados financeiros; enviar link e orientar confirmar, sem acesso ao produto.

Origem no requisito: R1: Cadastro aberto, sem convite ou liberação administrativa. Contas são individuais; nenhum dado financeiro é solicitado nesta jornada.; R2: Nome e e-mail são obrigatórios, com até 255 caracteres cada; e-mail válido e único por conta. Senha e confirmação são obrigatórias e devem coincidir. Na recuperação e redefinição, o e-mail informado deve ser válido; na redefinição, nova senha e confirmação também são obrigatórias.; CA1: Como visitante, cadastrar nome e e-mail válidos e disponíveis, senha conforme R3 e confirmação igual; criar uma única conta, enviar o link e orientar a confirmação, sem pedir dados financeiros ou liberar a área do produto antes de confirmar.

### CT-002 — Campos obrigatórios

Verificação: Omitir separadamente nome/e-mail/senha/confirmação no cadastro e os campos aplicáveis na redefinição.

Resultado esperado: Impedir conclusão com erro; sem conta ou senha alterada indevidamente.

Origem no requisito: R2: Nome e e-mail são obrigatórios, com até 255 caracteres cada; e-mail válido e único por conta. Senha e confirmação são obrigatórias e devem coincidir. Na recuperação e redefinição, o e-mail informado deve ser válido; na redefinição, nova senha e confirmação também são obrigatórias.; CA2: No cadastro e na redefinição, quando aplicável, omitir campos obrigatórios, exceder os limites de nome/e-mail, informar e-mail inválido ou duplicado, senha fora de qualquer condição de R3 ou confirmação diferente; impedir a operação e indicar os respectivos erros sem criar contas ou alterar senhas indevidamente.

### CT-003 — Nome e e-mail nos limites

Verificação: Usar entradas válidas de255 e256caracteres; e-mail inválido e duplicado.

Resultado esperado: Até255aceito; excesso/formato/duplicação recusados, sem nova conta indevida.

Origem no requisito: R2: Nome e e-mail são obrigatórios, com até 255 caracteres cada; e-mail válido e único por conta. Senha e confirmação são obrigatórias e devem coincidir. Na recuperação e redefinição, o e-mail informado deve ser válido; na redefinição, nova senha e confirmação também são obrigatórias.; CA2: No cadastro e na redefinição, quando aplicável, omitir campos obrigatórios, exceder os limites de nome/e-mail, informar e-mail inválido ou duplicado, senha fora de qualquer condição de R3 ou confirmação diferente; impedir a operação e indicar os respectivos erros sem criar contas ou alterar senhas indevidamente.

### CT-004 — Senha nos limites

Verificação: Nos dois fluxos usar senhas de composição completa não-vazadas com11,12,255 e256caracteres.

Resultado esperado: 12/255aceitas;11/256recusadas com erro; mesma regra em teste e uso.

Origem no requisito: R3: Cadastro e redefinição exigem senha de 12 a 255 caracteres, com ao menos uma maiúscula, uma minúscula, um número e um símbolo, rejeitando senhas conhecidas em vazamentos. A mesma regra vale nos ambientes de teste e uso.; CA2: No cadastro e na redefinição, quando aplicável, omitir campos obrigatórios, exceder os limites de nome/e-mail, informar e-mail inválido ou duplicado, senha fora de qualquer condição de R3 ou confirmação diferente; impedir a operação e indicar os respectivos erros sem criar contas ou alterar senhas indevidamente.

### CT-005 — Composição da senha

Verificação: Nos dois fluxos omitir separadamente maiúscula, minúscula, número e símbolo, mantendo demais condições.

Resultado esperado: Cada falta recusada; composição completa não rejeitada por esse motivo.

Origem no requisito: R3: Cadastro e redefinição exigem senha de 12 a 255 caracteres, com ao menos uma maiúscula, uma minúscula, um número e um símbolo, rejeitando senhas conhecidas em vazamentos. A mesma regra vale nos ambientes de teste e uso.; CA2: No cadastro e na redefinição, quando aplicável, omitir campos obrigatórios, exceder os limites de nome/e-mail, informar e-mail inválido ou duplicado, senha fora de qualquer condição de R3 ou confirmação diferente; impedir a operação e indicar os respectivos erros sem criar contas ou alterar senhas indevidamente.

### CT-006 — Senha conhecida em vazamentos

Verificação: Com dado controlado da verificação de senha vazada, tentar os dois fluxos com tamanho/composição válidos.

Resultado esperado: Recusar ambos com erro e sem persistência indevida.

Origem no requisito: R3: Cadastro e redefinição exigem senha de 12 a 255 caracteres, com ao menos uma maiúscula, uma minúscula, um número e um símbolo, rejeitando senhas conhecidas em vazamentos. A mesma regra vale nos ambientes de teste e uso.; CA2: No cadastro e na redefinição, quando aplicável, omitir campos obrigatórios, exceder os limites de nome/e-mail, informar e-mail inválido ou duplicado, senha fora de qualquer condição de R3 ou confirmação diferente; impedir a operação e indicar os respectivos erros sem criar contas ou alterar senhas indevidamente.

### CT-007 — Confirmação diferente

Verificação: Informar senha válida com confirmação diferente no cadastro e redefinição.

Resultado esperado: Impedir e indicar erro sem criar conta ou alterar senha.

Origem no requisito: R2: Nome e e-mail são obrigatórios, com até 255 caracteres cada; e-mail válido e único por conta. Senha e confirmação são obrigatórias e devem coincidir. Na recuperação e redefinição, o e-mail informado deve ser válido; na redefinição, nova senha e confirmação também são obrigatórias.; CA2: No cadastro e na redefinição, quando aplicável, omitir campos obrigatórios, exceder os limites de nome/e-mail, informar e-mail inválido ou duplicado, senha fora de qualquer condição de R3 ou confirmação diferente; impedir a operação e indicar os respectivos erros sem criar contas ou alterar senhas indevidamente.

## Confirmação

### CT-008 — Visitante na área protegida

Verificação: Sem sessão, abrir área inicial, perfil e configurações protegidas.

Resultado esperado: Exigir login sem mostrar funcionalidades do produto.

Origem no requisito: R4: Acesso à área do sistema exige autenticação e confirmação do próprio e-mail, incluindo acesso direto às páginas protegidas. Conta não confirmada pode concluir a jornada restrita de confirmação, reenvio, recuperação e saída; não acessa as funcionalidades do produto. Receber um e-mail ou redefinir a senha não equivale a confirmar o endereço.; CA3: Com conta não confirmada, tentar a área inicial, perfil, configurações e destinos financeiros protegidos quando entregues; manter o acesso restrito à jornada de confirmação, reenvio, recuperação e saída, inclusive com lembrar acesso selecionado.

### CT-009 — Conta não confirmada

Verificação: Entrar sem confirmar e tentar área inicial, perfil GET/PATCH e configurações; repetir com lembrar.

Resultado esperado: Manter restrição, orientação, reenvio e saída; sem acesso/alteração indevida no produto.

Origem no requisito: R4: Acesso à área do sistema exige autenticação e confirmação do próprio e-mail, incluindo acesso direto às páginas protegidas. Conta não confirmada pode concluir a jornada restrita de confirmação, reenvio, recuperação e saída; não acessa as funcionalidades do produto. Receber um e-mail ou redefinir a senha não equivale a confirmar o endereço.; CA3: Com conta não confirmada, tentar a área inicial, perfil, configurações e destinos financeiros protegidos quando entregues; manter o acesso restrito à jornada de confirmação, reenvio, recuperação e saída, inclusive com lembrar acesso selecionado.

### CT-010 — Recuperar antes de confirmar

Verificação: Como não-confirmado autenticado, sair e seguir ao pedido público existente.

Resultado esperado: Permitir a jornada sem liberar produto ou dispensar confirmação.

Origem no requisito: R4: Acesso à área do sistema exige autenticação e confirmação do próprio e-mail, incluindo acesso direto às páginas protegidas. Conta não confirmada pode concluir a jornada restrita de confirmação, reenvio, recuperação e saída; não acessa as funcionalidades do produto. Receber um e-mail ou redefinir a senha não equivale a confirmar o endereço.; CA3: Com conta não confirmada, tentar a área inicial, perfil, configurações e destinos financeiros protegidos quando entregues; manter o acesso restrito à jornada de confirmação, reenvio, recuperação e saída, inclusive com lembrar acesso selecionado.; CA9: Com link de recuperação próprio, não usado e antes de 60 minutos, definir senha conforme R3 e confirmação igual; retornar ao login, permitir novos logins com a senha nova e recusar a anterior. Uma conta anteriormente não confirmada continua sem acesso ao sistema.

### CT-011 — Confirmar link próprio

Verificação: Abrir link próprio válido iniciando com e sem sessão.

Resultado esperado: Autenticar quando necessário, confirmar titular e liberar área inicial.

Origem no requisito: R4: Acesso à área do sistema exige autenticação e confirmação do próprio e-mail, incluindo acesso direto às páginas protegidas. Conta não confirmada pode concluir a jornada restrita de confirmação, reenvio, recuperação e saída; não acessa as funcionalidades do produto. Receber um e-mail ou redefinir a senha não equivale a confirmar o endereço.; CA4: Como titular autenticado, abrir link válido da própria conta; confirmar o e-mail e permitir seguir à área inicial. Se iniciar sem sessão, solicitar autenticação quando necessária antes de concluir a confirmação.

### CT-012 — Confirmação inválida

Verificação: Alterar dados/assinatura do link e abrir como titular não confirmado.

Resultado esperado: Não confirmar nem liberar; orientar novo link próprio.

Origem no requisito: R4: Acesso à área do sistema exige autenticação e confirmação do próprio e-mail, incluindo acesso direto às páginas protegidas. Conta não confirmada pode concluir a jornada restrita de confirmação, reenvio, recuperação e saída; não acessa as funcionalidades do produto. Receber um e-mail ou redefinir a senha não equivale a confirmar o endereço.; R8: Falha de envio ou de link não deve ser apresentada como confirmação ou recuperação concluída. As alternativas de reenvio e novo pedido devem permitir retomar sem duplicar contas nem alterar senhas indevidamente.; CA5: Abrir link de confirmação inválido, expirado ou de outra conta; não confirmar endereço indevido nem liberar acesso e apresentar caminho para solicitar novo link próprio. Reabrir link ainda válido de conta já confirmada mantém a confirmação.

### CT-013 — Confirmação expirada

Verificação: Abrir link após sua validade.

Resultado esperado: Não confirmar/liberar; orientar e oferecer novo pedido.

Origem no requisito: R4: Acesso à área do sistema exige autenticação e confirmação do próprio e-mail, incluindo acesso direto às páginas protegidas. Conta não confirmada pode concluir a jornada restrita de confirmação, reenvio, recuperação e saída; não acessa as funcionalidades do produto. Receber um e-mail ou redefinir a senha não equivale a confirmar o endereço.; R8: Falha de envio ou de link não deve ser apresentada como confirmação ou recuperação concluída. As alternativas de reenvio e novo pedido devem permitir retomar sem duplicar contas nem alterar senhas indevidamente.; CA5: Abrir link de confirmação inválido, expirado ou de outra conta; não confirmar endereço indevido nem liberar acesso e apresentar caminho para solicitar novo link próprio. Reabrir link ainda válido de conta já confirmada mantém a confirmação.

### CT-014 — Confirmação de outra conta

Verificação: Como A não confirmado, abrir link válido de B.

Resultado esperado: Não confirmar A/B indevidamente; caminho de novo pedido próprio de A.

Origem no requisito: R4: Acesso à área do sistema exige autenticação e confirmação do próprio e-mail, incluindo acesso direto às páginas protegidas. Conta não confirmada pode concluir a jornada restrita de confirmação, reenvio, recuperação e saída; não acessa as funcionalidades do produto. Receber um e-mail ou redefinir a senha não equivale a confirmar o endereço.; CA5: Abrir link de confirmação inválido, expirado ou de outra conta; não confirmar endereço indevido nem liberar acesso e apresentar caminho para solicitar novo link próprio. Reabrir link ainda válido de conta já confirmada mantém a confirmação.

### CT-015 — Reabrir confirmação

Verificação: Confirmar conta e reabrir o mesmo link ainda válido.

Resultado esperado: Manter confirmação e permitir área inicial.

Origem no requisito: R4: Acesso à área do sistema exige autenticação e confirmação do próprio e-mail, incluindo acesso direto às páginas protegidas. Conta não confirmada pode concluir a jornada restrita de confirmação, reenvio, recuperação e saída; não acessa as funcionalidades do produto. Receber um e-mail ou redefinir a senha não equivale a confirmar o endereço.; CA5: Abrir link de confirmação inválido, expirado ou de outra conta; não confirmar endereço indevido nem liberar acesso e apresentar caminho para solicitar novo link próprio. Reabrir link ainda válido de conta já confirmada mantém a confirmação.

### CT-016 — Falha de envio inicial

Verificação: Provocar falha no cadastro, restaurar envio e repetir conforme orientação.

Resultado esperado: Informar falha/retomada sem falso sucesso, duplicação ou titular sem caminho de confirmação/recuperação.

Origem no requisito: R8: Falha de envio ou de link não deve ser apresentada como confirmação ou recuperação concluída. As alternativas de reenvio e novo pedido devem permitir retomar sem duplicar contas nem alterar senhas indevidamente.; CA11: Provocar falha de envio na confirmação inicial, no reenvio e na recuperação; informar falha e nova tentativa sem sucesso fictício. Após restabelecer o envio, permitir retomar com link utilizável sem contas duplicadas e sem revelar explicitamente a existência de conta na recuperação.; CA11-Confirmacao: Desdobramento de CA11/R8: falhas de envio inicial e reenvio de confirmação, retomada e unicidade da conta.

### CT-017 — Falha no reenvio

Verificação: Como não-confirmado, provocar falha de reenvio, restaurar e tentar de novo.

Resultado esperado: Não alegar envio concluído; após retomada, receber link e confirmar.

Origem no requisito: R8: Falha de envio ou de link não deve ser apresentada como confirmação ou recuperação concluída. As alternativas de reenvio e novo pedido devem permitir retomar sem duplicar contas nem alterar senhas indevidamente.; CA11: Provocar falha de envio na confirmação inicial, no reenvio e na recuperação; informar falha e nova tentativa sem sucesso fictício. Após restabelecer o envio, permitir retomar com link utilizável sem contas duplicadas e sem revelar explicitamente a existência de conta na recuperação.; CA11-Confirmacao: Desdobramento de CA11/R8: falhas de envio inicial e reenvio de confirmação, retomada e unicidade da conta.

## Login e saída

### CT-018 — Login e destino

Verificação: Entrar diretamente e após solicitar destino protegido; testar credenciais incorretas.

Resultado esperado: Corretas acessam área inicial/destino; incorretas não autenticam.

Origem no requisito: CA6: Entrar com credenciais corretas de conta confirmada; acessar a área inicial ou destino protegido solicitado. Credenciais incorretas não autenticam. Depois de cinco falhas consecutivas, a nova tentativa durante bloqueio informa espera; após o prazo, permitir nova tentativa válida.

### CT-019 — Cinco falhas e espera

Verificação: Para mesmo e-mail/origem, falhar cinco vezes e tentar durante bloqueio e após espera.

Resultado esperado: Informar espera sem autenticar durante bloqueio; após prazo, aceitar credenciais válidas.

Origem no requisito: R6: Após cinco falhas consecutivas de login para o mesmo e-mail e origem, bloquear temporariamente as novas tentativas e informar a espera, preservando o comportamento atual. Após o prazo, permitir nova tentativa.; CA6: Entrar com credenciais corretas de conta confirmada; acessar a área inicial ou destino protegido solicitado. Credenciais incorretas não autenticam. Depois de cinco falhas consecutivas, a nova tentativa durante bloqueio informa espera; após o prazo, permitir nova tentativa válida.

### CT-020 — Saída e lembrança

Verificação: Entrar/sair e reabrir área protegida com lembrar marcado e desmarcado.

Resultado esperado: Retornar à página pública e exigir novo login, inclusive após lembrança.

Origem no requisito: R7: Preservar a opção existente de lembrar acesso. Ela não dispensa confirmação do e-mail nem impede a saída explícita; sair encerra a sessão atual e exige novo login para voltar à área protegida.; CA7: Entrar e sair, com lembrar acesso marcado e desmarcado; retornar à página pública e exigir login ao tentar reabrir a área protegida.

## Recuperação

### CT-021 — Pedido genérico

Verificação: Com envio disponível, pedir recuperação para conta existente e inexistente.

Resultado esperado: Mesma resposta; titular cadastrado recebe link sem revelação pela resposta.

Origem no requisito: CA8: Solicitar recuperação para e-mail cadastrado e inexistente, com envio disponível; apresentar a mesma resposta genérica. O titular cadastrado recebe o link, sem revelar a existência da conta ao solicitante pela resposta.

### CT-022 — Redefinição válida

Verificação: Com link próprio não usado antes de60min, informar senha conforme R3/confirmação e testar senha anterior/nova.

Resultado esperado: Retornar ao login; nova funciona e antiga não permite novos logins.

Origem no requisito: R3: Cadastro e redefinição exigem senha de 12 a 255 caracteres, com ao menos uma maiúscula, uma minúscula, um número e um símbolo, rejeitando senhas conhecidas em vazamentos. A mesma regra vale nos ambientes de teste e uso.; R5: O link de recuperação é válido por 60 minutos a partir da emissão e não pode ser reutilizado após sucesso. A senha anterior deixa de permitir novos logins depois da redefinição.; CA9: Com link de recuperação próprio, não usado e antes de 60 minutos, definir senha conforme R3 e confirmação igual; retornar ao login, permitir novos logins com a senha nova e recusar a anterior. Uma conta anteriormente não confirmada continua sem acesso ao sistema.

### CT-023 — Redefinir sem confirmar e-mail

Verificação: Redefinir conta não confirmada e entrar com senha nova.

Resultado esperado: Senha muda, e-mail permanece não confirmado e produto continua restrito.

Origem no requisito: R4: Acesso à área do sistema exige autenticação e confirmação do próprio e-mail, incluindo acesso direto às páginas protegidas. Conta não confirmada pode concluir a jornada restrita de confirmação, reenvio, recuperação e saída; não acessa as funcionalidades do produto. Receber um e-mail ou redefinir a senha não equivale a confirmar o endereço.; CA9: Com link de recuperação próprio, não usado e antes de 60 minutos, definir senha conforme R3 e confirmação igual; retornar ao login, permitir novos logins com a senha nova e recusar a anterior. Uma conta anteriormente não confirmada continua sem acesso ao sistema.

### CT-024 — Recuperação inválida

Verificação: Tentar redefinir com link inválido e usar novo pedido.

Resultado esperado: Não alterar; orientar e oferecer novo link para retomada.

Origem no requisito: R5: O link de recuperação é válido por 60 minutos a partir da emissão e não pode ser reutilizado após sucesso. A senha anterior deixa de permitir novos logins depois da redefinição.; R8: Falha de envio ou de link não deve ser apresentada como confirmação ou recuperação concluída. As alternativas de reenvio e novo pedido devem permitir retomar sem duplicar contas nem alterar senhas indevidamente.; CA10: Tentar redefinir com link inválido, após sua expiração ou já utilizado; não alterar a senha e oferecer novo pedido. Um novo link válido permite retomar a jornada.

### CT-025 — Recuperação expirada

Verificação: Tentar após ultrapassar60min da emissão; solicitar outro link.

Resultado esperado: Recusar sem alterar e permitir retomar com novo link válido.

Origem no requisito: R5: O link de recuperação é válido por 60 minutos a partir da emissão e não pode ser reutilizado após sucesso. A senha anterior deixa de permitir novos logins depois da redefinição.; R8: Falha de envio ou de link não deve ser apresentada como confirmação ou recuperação concluída. As alternativas de reenvio e novo pedido devem permitir retomar sem duplicar contas nem alterar senhas indevidamente.; CA10: Tentar redefinir com link inválido, após sua expiração ou já utilizado; não alterar a senha e oferecer novo pedido. Um novo link válido permite retomar a jornada.

### CT-026 — Recuperação já usada

Verificação: Redefinir e reutilizar o mesmo link para outra senha.

Resultado esperado: Não alterar de novo; recusar e oferecer novo pedido.

Origem no requisito: R5: O link de recuperação é válido por 60 minutos a partir da emissão e não pode ser reutilizado após sucesso. A senha anterior deixa de permitir novos logins depois da redefinição.; R8: Falha de envio ou de link não deve ser apresentada como confirmação ou recuperação concluída. As alternativas de reenvio e novo pedido devem permitir retomar sem duplicar contas nem alterar senhas indevidamente.; CA10: Tentar redefinir com link inválido, após sua expiração ou já utilizado; não alterar a senha e oferecer novo pedido. Um novo link válido permite retomar a jornada.

### CT-027 — Falha de envio de recuperação

Verificação: Provocar falha, restaurar e solicitar de novo.

Resultado esperado: Orientar sem sucesso fictício/revelação explícita da conta; titular recebe link após retomada.

Origem no requisito: R8: Falha de envio ou de link não deve ser apresentada como confirmação ou recuperação concluída. As alternativas de reenvio e novo pedido devem permitir retomar sem duplicar contas nem alterar senhas indevidamente.; CA11: Provocar falha de envio na confirmação inicial, no reenvio e na recuperação; informar falha e nova tentativa sem sucesso fictício. Após restabelecer o envio, permitir retomar com link utilizável sem contas duplicadas e sem revelar explicitamente a existência de conta na recuperação.; CA11-Recuperacao: Desdobramento de CA11/R8: falha e retomada do envio de recuperação, sem falso sucesso ou revelação da conta.

## Visual

### CT-028 — Integração visual

Verificação: Em computador/tablet/celular, claro/escuro/sistema, percorrer as telas e os novos estados de erro/retomada. Comparar com design-input-001 — docs/harness/scopes/2026-11-11-finai-mvp/sources/design-input-001.md; referência clara e adaptações aprovadas na Feature visual #1016101 e o fornecedor de composição #1016114 após base verificada.

Resultado esperado: Identidade, campos, botões, erros e ações coerentes/usáveis, sem reconstruir a aparência fornecida.

Origem no requisito: R9: As telas de acesso usam a base visual FinAI da Feature de adequação visual, com tipografia, paleta, campos, botões, erros e estados coerentes, adaptação para celular, tablet e computador e manutenção dos temas claro, escuro e acompanhar o sistema. Esta Feature não redefine a identidade visual.; CA12: Utilizar as telas e estados de acesso em computador, tablet e celular, nos temas claro, escuro e acompanhar o sistema; manter a linguagem visual FinAI definida pela adequação visual, controles utilizáveis e erros reconhecíveis.

## Cobertura, inspeção e estimativas

A tabela completa está em [slices.md](slices.md). Cobertura existing exige verificação na QA, e cobertura de base visual em outra Feature exige o fornecedor implementado/verificado. CA11 possui desdobramentos de confirmação e recuperação, sem comportamento novo.

- Escopo vem exclusivamente do requisito aprovado #1016104, desta conversa e do código. Tasks antigas não são contexto. Filhas visuais #1016112–#1016117 foram criadas por este fluxo e são fornecedores publicados, sem capacidade pronta presumida.
- Inspeção por leitura de código, testes e padrões instalados. Nenhum teste ou jornada foi executado. Leituras do broker/guard sustentam minutos, uso único e saída lembrada; nenhum valor de credencial/ambiente foi lido.
- Não criar DEV para reconstruir login, saída, lembrar, limitação ou broker existentes. Cobertura existing permanece integralmente em QA. CA11-Confirmacao e CA11-Recuperacao desdobram CA11/R8 por jornada, sem requisito novo.
- Avaliação independente A, estimate_visual_delivery: DEV1=2h, DEV2=3,5h, DEV3=2h e QA=3,5h. Não recebeu estimativa candidata nem números da avaliação B.
- Avaliação independente B, estimate_visual_reuse: DEV1=2,5h, DEV2=4h, DEV3=2,5h e QA=4h. Não recebeu estimativa candidata nem números da avaliação A.
- Histórico da primeira proposta — estimativa do agente responsável: 2,5h para política compartilhada com dois pontos de entrada/fronteiras; 4h para confirmação/restrição, envio inicial/reenvio/links/perfil; 2,5h para recuperação e retomada; QA4h para preparar contas/links/tempo/falhas, verificar jornadas, estados visuais, resultados e reteste delimitado. Total9h DEV+4h QA=13h. É análise de trabalho restante, não média automática ou medição.
- Referência humana específica anterior: Mário Tinelli ajustou os cinco DEV visuais para2h e QA visual para1,5h. Não aplicar automaticamente esses números a acesso, que inclui titularidade/tempo de links, restrições e falhas; não há histórico medido nem premissa de desconto por IA.
- Sem bloqueio interno real de início entre os três DEV, pois os mecanismos atuais já existem. Conclusão integra política/jornadas. Pela política visual-first aprovada, há bloqueio externo de início pelo aceite integrado #1016117, dependente dos cinco DEV visuais; publicação em New não equivale a liberação de implementação.
- Recuperação atual usa rotas guest; a conta não confirmada autenticada pode sair e usar o caminho público existente. Não acrescentar redefinição autenticada que o requisito não exige.
- Publicação: três Task DEV e uma Deliverable QA, New/Normal, pai1016104 e versãoSprint1, sem responsável/datas. Cada DEV bloqueia QA; #1016117 bloqueia cada novo DEV, com vinculação exclusiva ao ID retornado. Pai/fornecedor mantêm estados. DOCX é gerado da fonte aprovada e anexado à QA.
- Correção explícita de Mário Tinelli nesta conversa: “estimativas na sequencia: 1.5h, 2h, 2h, 1h”. Estimativas atuais: política de senha1,5h,confirmação/restrição2h,recuperação2h eQA1h. Total5,5h DEV+1h QA=6,5h. Substitui os valores2,5h/4h/2,5h/4h da revisão001; é calibração humana,não nova avaliação independente nem medição de execução. Conteúdo,cobertura,condições e dependências preservados.
