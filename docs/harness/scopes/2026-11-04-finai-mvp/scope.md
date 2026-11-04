# FinAI — MVP inicial

## Objetivo do escopo

Controle financeiro pessoal com IA, cadastro público e dados separados por usuário. Projeto FinAi #65224; versão Sprint 1 #20355 selecionada pelo usuário. Design apenas visual. Recuperação de senha incluída pela resposta “sim”.

Catálogo aprovado pelo usuário nesta conversa: “catalogo aprovado”. As quatro issues foram publicadas; consulte o resumo final. Mapeamento proposto: Feature #2, estado inicial New #1; contexto operacional remoto será consolidado antes dos itens.

Correção de extração: a primeira escrita por pipe apresentou perda de acentos; a transcrição foi revisada antes de qualquer aprovação. Não houve mudança de escopo.

<!-- project-flow:catalog:start -->
## Convenção de títulos

- Convenção de públicos: single
- Públicos:
  - USUARIO
- Confirmação:
  - Confirmado em: 2026\-11\-04T17:13:03\.457919\+00:00
  - Confirmado por: Assistente — proposta, não aprovação do usuário
  - Decisão: Proposta de convenção apresentada para aprovação conjunta do catálogo; ainda sem confirmação do usuário\.
- Telas compartilhadas e públicas: USUARIO inclui a pessoa antes do cadastro nas telas públicas de acesso e a pessoa autenticada nas áreas financeiras\.
- Superfícies:
  - WEB

## Catálogo

### 1. acesso — Feature: \[WEB\] \[USUARIO\] Acesso à conta

- Público:
  - USUARIO
- Entrega visível: Acesso à conta
- Resultado para o usuário: Qualquer pessoa cria sua conta, entra, sai e recupera acesso\.
- Incluído:
  - Cadastro público, Login e saída, Recuperação de senha
- Limite: Reutiliza e adequa a base de acesso existente; os detalhes de aceitação serão entrevistados\.
- Dependências:
  - Nenhum.
- Justificativas dos bloqueios:
  - Nenhum.
- Motivo da posição:
  - Critério de ordem: usage\-lifecycle
  - Evidências:
    - conversation\-input\-001, conversation\-input\-002
  - Item: acesso
  - Justificativa: Acesso antecede uso de finanças pessoais\.

- Atores:
  - Pessoa usuária
- Candidatos:
  - c\-acesso
- Evidências:
  - conversation\-input\-002
- Objetivo humano: Qualquer pessoa cria sua conta, entra, sai e recupera acesso\.
- Ciclo de vida: active
- Resultado ou desvio: Qualquer pessoa cria sua conta, entra, sai e recupera acesso\.
- Justificativa do limite: Reutiliza e adequa a base de acesso existente; os detalhes de aceitação serão entrevistados\.
- Posição: 1

### 2. transacoes — Feature: \[WEB\] \[USUARIO\] Gestão de transações

- Público:
  - USUARIO
- Entrega visível: Gestão de transações
- Resultado para o usuário: Usuário mantém e consulta suas movimentações, sem acessar as de outra pessoa\.
- Incluído:
  - Cadastrar receitas e despesas, Editar e excluir transações, Consultar histórico, Classificar por categorias predefinidas, Persistir transações vinculadas ao usuário
- Limite: Categorias predefinidas integram a classificação; não há demanda de manutenção de categorias\.
- Dependências:
  - acesso
- Justificativas dos bloqueios:
  - Registro 1:
    - Bloqueado por: acesso
    - Por que impede a entrega: Sem esta capacidade, a entrega integrada não pode ser aceita com dados reais e isolados\.
    - Evidências:
      - conversation\-input\-001, conversation\-input\-002
    - Item: transacoes
    - Capacidade fornecida: Identidade autenticada
- Motivo da posição:
  - Critério de ordem: dependency
  - Evidências:
    - conversation\-input\-001, conversation\-input\-002
  - Item: transacoes
  - Justificativa: As movimentações precisam de autoria e acesso individual\.

- Atores:
  - Pessoa usuária
- Candidatos:
  - c\-transacoes
- Evidências:
  - conversation\-input\-001, conversation\-input\-002
- Objetivo humano: Usuário mantém e consulta suas movimentações, sem acessar as de outra pessoa\.
- Ciclo de vida: active
- Resultado ou desvio: Usuário mantém e consulta suas movimentações, sem acessar as de outra pessoa\.
- Justificativa do limite: Categorias predefinidas integram a classificação; não há demanda de manutenção de categorias\.
- Posição: 2

### 3. dashboard — Feature: \[WEB\] \[USUARIO\] Dashboard financeiro

- Público:
  - USUARIO
- Entrega visível: Dashboard financeiro
- Resultado para o usuário: Usuário acompanha a situação financeira calculada de seus registros\.
- Incluído:
  - Visualizar saldo geral, Visualizar receitas e despesas do mês, Consultar movimentações recentes, Refletir os registros do usuário
- Limite: Resumo financeiro, sem relatórios avançados\.
- Dependências:
  - transacoes
- Justificativas dos bloqueios:
  - Registro 1:
    - Bloqueado por: transacoes
    - Por que impede a entrega: Sem esta capacidade, a entrega integrada não pode ser aceita com dados reais e isolados\.
    - Evidências:
      - conversation\-input\-001, conversation\-input\-002
    - Item: dashboard
    - Capacidade fornecida: Transações pessoais persistidas
- Motivo da posição:
  - Critério de ordem: dependency
  - Evidências:
    - conversation\-input\-001, conversation\-input\-002
  - Item: dashboard
  - Justificativa: A visão financeira usa movimentações persistidas\.

- Atores:
  - Pessoa usuária
- Candidatos:
  - c\-dashboard
- Evidências:
  - conversation\-input\-001, conversation\-input\-002
- Objetivo humano: Usuário acompanha a situação financeira calculada de seus registros\.
- Ciclo de vida: active
- Resultado ou desvio: Usuário acompanha a situação financeira calculada de seus registros\.
- Justificativa do limite: Resumo financeiro, sem relatórios avançados\.
- Posição: 3

### 4. assistente — Feature: \[WEB\] \[USUARIO\] Assistente financeiro com IA

- Público:
  - USUARIO
- Entrega visível: Assistente financeiro com IA
- Resultado para o usuário: Usuário registra e consulta suas finanças por conversa, com confirmação antes de gravar\.
- Incluído:
  - Interagir por chat com IA real, Identificar valor, descrição e categoria, Solicitar informações faltantes, Solicitar confirmação antes de persistir, Registrar receitas e despesas, Consultar apenas dados reais do próprio usuário
- Limite: Registro e consulta compõem uma capacidade única; sem múltiplos agentes ou recomendações futuras\.
- Dependências:
  - transacoes
- Justificativas dos bloqueios:
  - Registro 1:
    - Bloqueado por: transacoes
    - Por que impede a entrega: Sem esta capacidade, a entrega integrada não pode ser aceita com dados reais e isolados\.
    - Evidências:
      - conversation\-input\-001, conversation\-input\-002
    - Item: assistente
    - Capacidade fornecida: Transações pessoais persistidas
- Motivo da posição:
  - Critério de ordem: usage\-lifecycle
  - Evidências:
    - conversation\-input\-001, conversation\-input\-002
  - Item: assistente
  - Justificativa: Depois do registro manual e da visualização, acrescentar a interação por IA\.

- Atores:
  - Pessoa usuária
- Candidatos:
  - c\-assistente
- Evidências:
  - conversation\-input\-001, conversation\-input\-002
- Objetivo humano: Usuário registra e consulta suas finanças por conversa, com confirmação antes de gravar\.
- Ciclo de vida: active
- Resultado ou desvio: Usuário registra e consulta suas finanças por conversa, com confirmação antes de gravar\.
- Justificativa do limite: Registro e consulta compõem uma capacidade única; sem múltiplos agentes ou recomendações futuras\.
- Posição: 4

## Cobertura comportamental

- Registro 1:
  - Públicos:
    - USUARIO
  - Itens consumidores: Nenhum.
  - Decisão: Nenhum.
  - Comportamento: Cadastro público
  - Destino: covered
  - Evidências:
    - Registro 1:
      - Localizador: Resposta do usuário
      - Fonte: conversation\-input\-002
  - Tipo de evidência: annotation
  - ID: b\-acesso\-1
  - Item responsável: acesso
  - Confronto com o repositório:
    - Evidências:
      - routes/web\.php, app/Models/User\.php, resources/js/pages/dashboard\.tsx
    - Mudança proposta: Qualquer pessoa cria sua conta, entra, sai e recupera acesso\.
    - Estado: partial
- Registro 2:
  - Públicos:
    - USUARIO
  - Itens consumidores: Nenhum.
  - Decisão: Nenhum.
  - Comportamento: Login e saída
  - Destino: covered
  - Evidências:
    - Registro 1:
      - Localizador: Resposta do usuário
      - Fonte: conversation\-input\-002
  - Tipo de evidência: annotation
  - ID: b\-acesso\-2
  - Item responsável: acesso
  - Confronto com o repositório:
    - Evidências:
      - routes/web\.php, app/Models/User\.php, resources/js/pages/dashboard\.tsx
    - Mudança proposta: Qualquer pessoa cria sua conta, entra, sai e recupera acesso\.
    - Estado: partial
- Registro 3:
  - Públicos:
    - USUARIO
  - Itens consumidores: Nenhum.
  - Decisão: Nenhum.
  - Comportamento: Recuperação de senha
  - Destino: covered
  - Evidências:
    - Registro 1:
      - Localizador: Complementada pela resposta conversation\-input\-003: sim à recuperação de senha
      - Fonte: conversation\-input\-002
  - Tipo de evidência: annotation
  - ID: b\-acesso\-3
  - Item responsável: acesso
  - Confronto com o repositório:
    - Evidências:
      - routes/web\.php, app/Models/User\.php, resources/js/pages/dashboard\.tsx
    - Mudança proposta: Qualquer pessoa cria sua conta, entra, sai e recupera acesso\.
    - Estado: partial
- Registro 4:
  - Públicos:
    - USUARIO
  - Itens consumidores: Nenhum.
  - Decisão: Nenhum.
  - Comportamento: Cadastrar receitas e despesas
  - Destino: covered
  - Evidências:
    - Registro 1:
      - Localizador: Seção 3\.2 e regras básicas
      - Fonte: conversation\-input\-001
  - Tipo de evidência: annotation
  - ID: b\-transacoes\-1
  - Item responsável: transacoes
  - Confronto com o repositório:
    - Evidências:
      - routes/web\.php, app/Models/User\.php, resources/js/pages/dashboard\.tsx
    - Mudança proposta: Usuário mantém e consulta suas movimentações, sem acessar as de outra pessoa\.
    - Estado: absent
- Registro 5:
  - Públicos:
    - USUARIO
  - Itens consumidores: Nenhum.
  - Decisão: Nenhum.
  - Comportamento: Editar e excluir transações
  - Destino: covered
  - Evidências:
    - Registro 1:
      - Localizador: Seção 3\.2 e regras básicas
      - Fonte: conversation\-input\-001
  - Tipo de evidência: annotation
  - ID: b\-transacoes\-2
  - Item responsável: transacoes
  - Confronto com o repositório:
    - Evidências:
      - routes/web\.php, app/Models/User\.php, resources/js/pages/dashboard\.tsx
    - Mudança proposta: Usuário mantém e consulta suas movimentações, sem acessar as de outra pessoa\.
    - Estado: absent
- Registro 6:
  - Públicos:
    - USUARIO
  - Itens consumidores: Nenhum.
  - Decisão: Nenhum.
  - Comportamento: Consultar histórico
  - Destino: covered
  - Evidências:
    - Registro 1:
      - Localizador: Seção 3\.2 e regras básicas
      - Fonte: conversation\-input\-001
  - Tipo de evidência: annotation
  - ID: b\-transacoes\-3
  - Item responsável: transacoes
  - Confronto com o repositório:
    - Evidências:
      - routes/web\.php, app/Models/User\.php, resources/js/pages/dashboard\.tsx
    - Mudança proposta: Usuário mantém e consulta suas movimentações, sem acessar as de outra pessoa\.
    - Estado: absent
- Registro 7:
  - Públicos:
    - USUARIO
  - Itens consumidores: Nenhum.
  - Decisão: Nenhum.
  - Comportamento: Classificar por categorias predefinidas
  - Destino: covered
  - Evidências:
    - Registro 1:
      - Localizador: Seção 3\.2 e regras básicas
      - Fonte: conversation\-input\-001
  - Tipo de evidência: annotation
  - ID: b\-transacoes\-4
  - Item responsável: transacoes
  - Confronto com o repositório:
    - Evidências:
      - routes/web\.php, app/Models/User\.php, resources/js/pages/dashboard\.tsx
    - Mudança proposta: Usuário mantém e consulta suas movimentações, sem acessar as de outra pessoa\.
    - Estado: absent
- Registro 8:
  - Públicos:
    - USUARIO
  - Itens consumidores: Nenhum.
  - Decisão: Nenhum.
  - Comportamento: Persistir transações vinculadas ao usuário
  - Destino: covered
  - Evidências:
    - Registro 1:
      - Localizador: Seção 3\.2 e regras básicas
      - Fonte: conversation\-input\-001
  - Tipo de evidência: annotation
  - ID: b\-transacoes\-5
  - Item responsável: transacoes
  - Confronto com o repositório:
    - Evidências:
      - routes/web\.php, app/Models/User\.php, resources/js/pages/dashboard\.tsx
    - Mudança proposta: Usuário mantém e consulta suas movimentações, sem acessar as de outra pessoa\.
    - Estado: absent
- Registro 9:
  - Públicos:
    - USUARIO
  - Itens consumidores: Nenhum.
  - Decisão: Nenhum.
  - Comportamento: Visualizar saldo geral
  - Destino: covered
  - Evidências:
    - Registro 1:
      - Localizador: Seção 3\.1 e regras básicas
      - Fonte: conversation\-input\-001
  - Tipo de evidência: annotation
  - ID: b\-dashboard\-1
  - Item responsável: dashboard
  - Confronto com o repositório:
    - Evidências:
      - routes/web\.php, app/Models/User\.php, resources/js/pages/dashboard\.tsx
    - Mudança proposta: Usuário acompanha a situação financeira calculada de seus registros\.
    - Estado: absent
- Registro 10:
  - Públicos:
    - USUARIO
  - Itens consumidores: Nenhum.
  - Decisão: Nenhum.
  - Comportamento: Visualizar receitas e despesas do mês
  - Destino: covered
  - Evidências:
    - Registro 1:
      - Localizador: Seção 3\.1 e regras básicas
      - Fonte: conversation\-input\-001
  - Tipo de evidência: annotation
  - ID: b\-dashboard\-2
  - Item responsável: dashboard
  - Confronto com o repositório:
    - Evidências:
      - routes/web\.php, app/Models/User\.php, resources/js/pages/dashboard\.tsx
    - Mudança proposta: Usuário acompanha a situação financeira calculada de seus registros\.
    - Estado: absent
- Registro 11:
  - Públicos:
    - USUARIO
  - Itens consumidores: Nenhum.
  - Decisão: Nenhum.
  - Comportamento: Consultar movimentações recentes
  - Destino: covered
  - Evidências:
    - Registro 1:
      - Localizador: Seção 3\.1 e regras básicas
      - Fonte: conversation\-input\-001
  - Tipo de evidência: annotation
  - ID: b\-dashboard\-3
  - Item responsável: dashboard
  - Confronto com o repositório:
    - Evidências:
      - routes/web\.php, app/Models/User\.php, resources/js/pages/dashboard\.tsx
    - Mudança proposta: Usuário acompanha a situação financeira calculada de seus registros\.
    - Estado: absent
- Registro 12:
  - Públicos:
    - USUARIO
  - Itens consumidores: Nenhum.
  - Decisão: Nenhum.
  - Comportamento: Refletir os registros do usuário
  - Destino: covered
  - Evidências:
    - Registro 1:
      - Localizador: Seção 3\.1 e regras básicas
      - Fonte: conversation\-input\-001
  - Tipo de evidência: annotation
  - ID: b\-dashboard\-4
  - Item responsável: dashboard
  - Confronto com o repositório:
    - Evidências:
      - routes/web\.php, app/Models/User\.php, resources/js/pages/dashboard\.tsx
    - Mudança proposta: Usuário acompanha a situação financeira calculada de seus registros\.
    - Estado: absent
- Registro 13:
  - Públicos:
    - USUARIO
  - Itens consumidores: Nenhum.
  - Decisão: Nenhum.
  - Comportamento: Interagir por chat com IA real
  - Destino: covered
  - Evidências:
    - Registro 1:
      - Localizador: Seção 3\.4 e regras básicas
      - Fonte: conversation\-input\-001
  - Tipo de evidência: annotation
  - ID: b\-assistente\-1
  - Item responsável: assistente
  - Confronto com o repositório:
    - Evidências:
      - routes/web\.php, app/Models/User\.php, resources/js/pages/dashboard\.tsx
    - Mudança proposta: Usuário registra e consulta suas finanças por conversa, com confirmação antes de gravar\.
    - Estado: absent
- Registro 14:
  - Públicos:
    - USUARIO
  - Itens consumidores: Nenhum.
  - Decisão: Nenhum.
  - Comportamento: Identificar valor, descrição e categoria
  - Destino: covered
  - Evidências:
    - Registro 1:
      - Localizador: Seção 3\.4 e regras básicas
      - Fonte: conversation\-input\-001
  - Tipo de evidência: annotation
  - ID: b\-assistente\-2
  - Item responsável: assistente
  - Confronto com o repositório:
    - Evidências:
      - routes/web\.php, app/Models/User\.php, resources/js/pages/dashboard\.tsx
    - Mudança proposta: Usuário registra e consulta suas finanças por conversa, com confirmação antes de gravar\.
    - Estado: absent
- Registro 15:
  - Públicos:
    - USUARIO
  - Itens consumidores: Nenhum.
  - Decisão: Nenhum.
  - Comportamento: Solicitar informações faltantes
  - Destino: covered
  - Evidências:
    - Registro 1:
      - Localizador: Seção 3\.4 e regras básicas
      - Fonte: conversation\-input\-001
  - Tipo de evidência: annotation
  - ID: b\-assistente\-3
  - Item responsável: assistente
  - Confronto com o repositório:
    - Evidências:
      - routes/web\.php, app/Models/User\.php, resources/js/pages/dashboard\.tsx
    - Mudança proposta: Usuário registra e consulta suas finanças por conversa, com confirmação antes de gravar\.
    - Estado: absent
- Registro 16:
  - Públicos:
    - USUARIO
  - Itens consumidores: Nenhum.
  - Decisão: Nenhum.
  - Comportamento: Solicitar confirmação antes de persistir
  - Destino: covered
  - Evidências:
    - Registro 1:
      - Localizador: Seção 3\.4 e regras básicas
      - Fonte: conversation\-input\-001
  - Tipo de evidência: annotation
  - ID: b\-assistente\-4
  - Item responsável: assistente
  - Confronto com o repositório:
    - Evidências:
      - routes/web\.php, app/Models/User\.php, resources/js/pages/dashboard\.tsx
    - Mudança proposta: Usuário registra e consulta suas finanças por conversa, com confirmação antes de gravar\.
    - Estado: absent
- Registro 17:
  - Públicos:
    - USUARIO
  - Itens consumidores: Nenhum.
  - Decisão: Nenhum.
  - Comportamento: Registrar receitas e despesas
  - Destino: covered
  - Evidências:
    - Registro 1:
      - Localizador: Seção 3\.4 e regras básicas
      - Fonte: conversation\-input\-001
  - Tipo de evidência: annotation
  - ID: b\-assistente\-5
  - Item responsável: assistente
  - Confronto com o repositório:
    - Evidências:
      - routes/web\.php, app/Models/User\.php, resources/js/pages/dashboard\.tsx
    - Mudança proposta: Usuário registra e consulta suas finanças por conversa, com confirmação antes de gravar\.
    - Estado: absent
- Registro 18:
  - Públicos:
    - USUARIO
  - Itens consumidores: Nenhum.
  - Decisão: Nenhum.
  - Comportamento: Consultar apenas dados reais do próprio usuário
  - Destino: covered
  - Evidências:
    - Registro 1:
      - Localizador: Seção 3\.4 e regras básicas
      - Fonte: conversation\-input\-001
  - Tipo de evidência: annotation
  - ID: b\-assistente\-6
  - Item responsável: assistente
  - Confronto com o repositório:
    - Evidências:
      - routes/web\.php, app/Models/User\.php, resources/js/pages/dashboard\.tsx
    - Mudança proposta: Usuário registra e consulta suas finanças por conversa, com confirmação antes de gravar\.
    - Estado: absent
- Registro 19:
  - Públicos:
    - USUARIO
  - Itens consumidores:
    - dashboard, assistente
  - Decisão: Nenhum.
  - Comportamento: Finanças separadas por usuário em todas as operações, inclusive consultas da IA\.
  - Destino: covered
  - Evidências:
    - Registro 1:
      - Localizador: Resposta sobre login e finanças separadas
      - Fonte: conversation\-input\-002
  - Tipo de evidência: annotation
  - ID: b\-isolamento
  - Item responsável: transacoes
  - Confronto com o repositório:
    - Evidências:
      - app/Models/User\.php, routes/web\.php
    - Mudança proposta: Vincular e limitar operações financeiras ao próprio usuário\.
    - Estado: absent
- Registro 20:
  - Públicos:
    - USUARIO
  - Itens consumidores: Nenhum.
  - Decisão:
    - Confirmado em: 2026\-11\-04T17:13:03\.457919\+00:00
    - Confirmado por: Usuário — escopo inicial
    - Decisão: Exclusões e evoluções futuras declaradas no escopo inicial\.
  - Comportamento: Fora do MVP: bancos, extratos, cartões, metas, relatórios avançados, finanças empresariais, múltiplos agentes e evoluções futuras\.
  - Destino: excluded
  - Evidências:
    - Registro 1:
      - Localizador: Seções 5 e 7
      - Fonte: conversation\-input\-001
  - Tipo de evidência: annotation
  - ID: b\-exclusoes
  - Item responsável: Nenhum.
  - Confronto com o repositório:
    - Evidências:
      - routes/web\.php
    - Mudança proposta: Não incluir nesta entrega\.
    - Estado: absent

## Inventário e referências

- Inventário:
  - Registro 1:
    - Decisão: Nenhum.
    - Origem: Conversa: texto do escopo fornecido pelo usuário
    - Papel da fonte: behavioral
    - Fonte: conversation\-input\-001
  - Registro 2:
    - Decisão: Nenhum.
    - Origem: Conversa: respostas posteriores ao escopo
    - Papel da fonte: behavioral
    - Fonte: conversation\-input\-002
  - Registro 3:
    - Decisão: Nenhum.
    - Origem: C:/Users/maari/Downloads/FinAI\-Controle\-Financeiro\.zip
    - Papel da fonte: contextual
    - Fonte: design\-001
  - Registro 4:
    - Decisão: Nenhum.
    - Origem: Conversa: resposta sobre Esqueci minha senha
    - Papel da fonte: contextual
    - Fonte: conversation\-input\-003
- Referências entre fontes: Nenhum.
- Material solicitado:
  - Escopo escrito e respostas do usuário, FinAI\-Controle\-Financeiro\.zip completo, apenas visual
- Tipo de seleção: complete\-package

## Fontes

- Registro 1:
  - decision_reconciliation: not\-applicable
  - extraction_method: Transcrição do trecho relevante da conversa em UTF\-8
  - fully_read: true
  - hash_unavailable_reason: Nenhum.
  - ID: conversation\-input\-001
  - Nome: Escopo inicial do MVP
  - normalized_sha256: 5792eb0b8be57808b3eadfd6920fe7eafebb906d7e6c9f9d62158cc5e733f92f
  - Origem: Conversa: texto do escopo fornecido pelo usuário
  - original_sha256: 29fa58bcdc4ae160539e5f1330109f2b86a6d44316d454f58c554c8598aa444a
  - Caminho: sources/conversation\-input\-001\.md
  - Estado: normalized
  - Tipo: escopo funcional
- Registro 2:
  - decision_reconciliation: not\-applicable
  - extraction_method: Transcrição das respostas do usuário, na ordem original
  - fully_read: true
  - hash_unavailable_reason: Nenhum.
  - ID: conversation\-input\-002
  - Nome: Definições de contexto e acesso
  - normalized_sha256: e7ff248be0322113001b0f2f6b3f1258ba92286d50001752a0122efe164e8fc2
  - Origem: Conversa: respostas posteriores ao escopo
  - original_sha256: f81dab197b815e50998fea40abb55f14695abd108330711b5d665dd7273586d3
  - Caminho: sources/conversation\-input\-002\.md
  - Estado: normalized
  - Tipo: decisões do usuário
- Registro 3:
  - decision_reconciliation: not\-applicable
  - extraction_method: Leitura integral dos três arquivos UTF\-8 com zipfile, sem execução ou extração dos originais
  - fully_read: true
  - hash_unavailable_reason: Nenhum.
  - ID: design\-001
  - Nome: FinAI\-Controle\-Financeiro\.zip
  - normalized_sha256: 020819a1f9d30e7b39c7bde4b5d94008c0c224da2308b789bd3d88835eade551
  - Origem: C:/Users/maari/Downloads/FinAI\-Controle\-Financeiro\.zip
  - original_sha256: d7fec0da8d116208b921ee8cb152b8c3710cf4a7500e30aca6d7b43270dddbd5
  - Caminho: sources/design\-001\.md
  - Estado: normalized
  - Tipo: referência visual
- Registro 4:
  - decision_reconciliation: not\-applicable
  - extraction_method: Transcrição UTF\-8
  - fully_read: true
  - hash_unavailable_reason: Nenhum.
  - ID: conversation\-input\-003
  - Nome: Inclusão de recuperação de senha
  - normalized_sha256: 5d9c08993113ca6d72689522a0e6ba9622b399b3af964971bcf936dfd46dbe24
  - Origem: Conversa: resposta sobre Esqueci minha senha
  - original_sha256: 507a9a8be3d145a86daa9644b28bf42a8dc0720d8baeabdf0406c393692bf082
  - Caminho: sources/conversation\-input\-003\.md
  - Estado: normalized
  - Tipo: resposta do usuário

## Alocação física das fontes

- Registro 1:
  - Itens:
    - transacoes, dashboard, assistente
  - Local de armazenamento: scope\-shared
  - Caminho: sources/conversation\-input\-001\.md
  - Fonte: conversation\-input\-001
- Registro 2:
  - Itens:
    - acesso, transacoes, dashboard, assistente
  - Local de armazenamento: scope\-shared
  - Caminho: sources/conversation\-input\-002\.md
  - Fonte: conversation\-input\-002
- Registro 3:
  - Itens: Nenhum.
  - Local de armazenamento: scope\-context
  - Caminho: sources/design\-001\.md
  - Fonte: design\-001
- Registro 4:
  - Itens: Nenhum.
  - Local de armazenamento: scope\-context
  - Caminho: sources/conversation\-input\-003\.md
  - Fonte: conversation\-input\-003

## Candidatos

- Registro 1:
  - Itens:
    - acesso
  - ID: c\-acesso
  - Justificativa: Reutiliza e adequa a base de acesso existente; os detalhes de aceitação serão entrevistados\.
  - Estado: decided
- Registro 2:
  - Itens:
    - transacoes
  - ID: c\-transacoes
  - Justificativa: Categorias predefinidas integram a classificação; não há demanda de manutenção de categorias\.
  - Estado: decided
- Registro 3:
  - Itens:
    - dashboard
  - ID: c\-dashboard
  - Justificativa: Resumo financeiro, sem relatórios avançados\.
  - Estado: decided
- Registro 4:
  - Itens:
    - assistente
  - ID: c\-assistente
  - Justificativa: Registro e consulta compõem uma capacidade única; sem múltiplos agentes ou recomendações futuras\.
  - Estado: decided

## Itens retirados

- Nenhum.

## Grafo de bloqueios

- Registro 1:
  - Bloqueado por: acesso
  - Item: transacoes
- Registro 2:
  - Bloqueado por: transacoes
  - Item: dashboard
- Registro 3:
  - Bloqueado por: transacoes
  - Item: assistente

## Justificativas de dependências

- Registro 1:
  - Bloqueado por: acesso
  - Por que impede a entrega: Sem esta capacidade, a entrega integrada não pode ser aceita com dados reais e isolados\.
  - Evidências:
    - conversation\-input\-001, conversation\-input\-002
  - Item: transacoes
  - Capacidade fornecida: Identidade autenticada
- Registro 2:
  - Bloqueado por: transacoes
  - Por que impede a entrega: Sem esta capacidade, a entrega integrada não pode ser aceita com dados reais e isolados\.
  - Evidências:
    - conversation\-input\-001, conversation\-input\-002
  - Item: dashboard
  - Capacidade fornecida: Transações pessoais persistidas
- Registro 3:
  - Bloqueado por: transacoes
  - Por que impede a entrega: Sem esta capacidade, a entrega integrada não pode ser aceita com dados reais e isolados\.
  - Evidências:
    - conversation\-input\-001, conversation\-input\-002
  - Item: assistente
  - Capacidade fornecida: Transações pessoais persistidas

## Ordem aprovada

- acesso, transacoes, dashboard, assistente

## Justificativas da ordem

- Registro 1:
  - Critério de ordem: usage\-lifecycle
  - Evidências:
    - conversation\-input\-001, conversation\-input\-002
  - Item: acesso
  - Justificativa: Acesso antecede uso de finanças pessoais\.
- Registro 2:
  - Critério de ordem: dependency
  - Evidências:
    - conversation\-input\-001, conversation\-input\-002
  - Item: transacoes
  - Justificativa: As movimentações precisam de autoria e acesso individual\.
- Registro 3:
  - Critério de ordem: dependency
  - Evidências:
    - conversation\-input\-001, conversation\-input\-002
  - Item: dashboard
  - Justificativa: A visão financeira usa movimentações persistidas\.
- Registro 4:
  - Critério de ordem: usage\-lifecycle
  - Evidências:
    - conversation\-input\-001, conversation\-input\-002
  - Item: assistente
  - Justificativa: Depois do registro manual e da visualização, acrescentar a interação por IA\.

## Grupos sem bloqueios entre si no grafo

- Registro 1:
  - acesso
- Registro 2:
  - transacoes
- Registro 3:
  - dashboard, assistente

<!-- project-flow:catalog:end -->




## Aprovação do catálogo

Aprovado pelo usuário: “catalogo aprovado”. Hash: `9abbb769af4a171a921c8561fa6bd14f23d1d92176ce5ce9f4928301926b4b7d`. Data de registro: 2026-11-04T17:36:50.965471+00:00.

## Progresso

Acesso à conta em entrevista. Run: f22e3842-5619-41f2-8357-1df62241a7b8. Staging: `docs/harness/.runs/f22e3842-5619-41f2-8357-1df62241a7b8`. Demais itens pendentes.

## Pausas e retomadas

## Relações nativas

## Alterações do catálogo

## Pendências, dependências e condições de retomada

## Resumo final

### Issues

| Sequência | Issue | Feature |
|---|---|---|
| 1 | [#1015909](https://redmine.remsoft.com.br/issues/1015909) | Acesso à conta |
| 2 | [#1015911](https://redmine.remsoft.com.br/issues/1015911) | Gestão de transações |
| 3 | [#1015912](https://redmine.remsoft.com.br/issues/1015912) | Dashboard financeiro |
| 4 | [#1015913](https://redmine.remsoft.com.br/issues/1015913) | Assistente financeiro com IA |

Todas na Sprint 1, status New.

### Relações

- #1015909 bloqueia #1015911 (relação 763).
- #1015911 bloqueia #1015912 (relação 764).
- #1015911 bloqueia #1015913 (relação 765).

### Artefatos

- [Acesso à conta](../../features/1015909-acesso-a-conta/feature.md).
- [Gestão de transações](../../features/1015911-gestao-de-transacoes/feature.md).
- [Dashboard financeiro](../../features/1015912-dashboard-financeiro/feature.md).
- [Assistente financeiro com IA](../../features/1015913-assistente-financeiro-ia/feature.md).

Catálogo, fontes, decisões, aprovações e evidências de publicação preservados neste escopo e nos diretórios das Features.

### Aprovações

Catálogo, quatro requisitos e seus planos de publicação e encerramento consolidado aprovados pelo usuário nesta conversa.

### Validações

Quatro requisitos em completed; quatro descrições integrais conferidas; três relações confirmadas; Sprint 1, Sequencing 1 a 4 e status New preservados; escopo concluído e validado, sem lacunas funcionais abertas.

### Próxima recomendação

Preparar o desdobramento DEV/QA dos requisitos aprovados, começando por Acesso à conta, com project-slices. Nenhuma implementação ou tarefa técnica foi criada neste fluxo.

## Histórico de progresso

## Atualização de progresso — 2026-11-04T19:11:25.460953+00:00

Acesso à conta concluído: issue #1015909, [requisito](../../features/1015909-acesso-a-conta/feature.md), aprovação e publicação integral validadas. Status remoto New preservado. Gestão de transações em entrevista; staging `docs/harness/.runs/277b06fc-6870-437c-b237-eacfdd666e39`, run 277b06fc-6870-437c-b237-eacfdd666e39. Dashboard e Assistente pendentes.


## Atualização de progresso — 2026-11-04T19:34:00.718377+00:00

Gestão de transações concluída: #1015911, [requisito](../../features/1015911-gestao-de-transacoes/feature.md). Relação blocks #1015909 → #1015911 confirmada, ID 763. Ambas em New. Dashboard financeiro em entrevista, staging `docs/harness/.runs/8ec14130-5e6e-453e-96a6-4ca421be6cba`, run 8ec14130-5e6e-453e-96a6-4ca421be6cba. Assistente pendente.


## Atualização de progresso — 2026-11-04T20:11:15.486234+00:00

Dashboard concluído: #1015912, [requisito](../../features/1015912-dashboard-financeiro/feature.md). Relação #1015911 → #1015912, ID 764, confirmada. Status New preservado. Assistente financeiro em entrevista; staging `docs/harness/.runs/1a34fdd3-9440-446c-8725-76246ece59ff`, run 1a34fdd3-9440-446c-8725-76246ece59ff. Três de quatro requisitos publicados.


## Encerramento aprovado

Usuário: “aprovado”. Registro em 2026-11-04T20:29:35.999639+00:00. Escopo validado em `completed`. [Resumo apresentado e aprovado](.flow/publications/2ac84340-9d23-4970-b366-faccca170697/summary.json). As quatro issues permanecem em New; nenhuma implementação ou tarefa técnica foi criada.
