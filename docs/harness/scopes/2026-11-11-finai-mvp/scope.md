# FinAI — MVP inicial (catálogo aprovado)

## Objetivo do escopo

Controle financeiro pessoal manual e por IA real, com persistência no sistema e contas individuais. Projeto FinAi (65224); Sprint 1 (20355), selecionada pelo usuário.

### Contexto confirmado nesta conversa

- Selecionar Sprint 1 (20355)
- Design visual + persistência no sistema e IA real
- nao use nada como contexto das tasks no redmine
- eu esqueci de apaga-las
- nnenhum esta feita
- Contas individuais e finanças separadas por usuário

Todas as issues antigas do Redmine foram desconsideradas por instrução expressa do usuário. Apenas os metadados de conexão, projeto, versão, trackers e status são usados. Nenhuma entrega é considerada concluída. Nenhuma issue antiga será alterada ou excluída neste fluxo.

### Comparação visual

Base divergente: tema neutro, marca e navegação do starter e dashboard com placeholders. Evidências: resources/css/app.css, resources/js/components/app-sidebar.tsx e resources/js/pages/dashboard.tsx. Referência: sources/design-input-001.md, estilos :root, navegação e superfícies #overview, #transactions e #assistant. A primeira Feature trata a adequação visual compartilhada. A aparência do protótipo será preservada com os textos de armazenamento e IA ajustados conforme a decisão do usuário.

### Limites gerais

Fora do MVP: integração bancária, importação de extratos, cartões de crédito, metas, relatórios avançados, gestão empresarial e múltiplos agentes. Análises inteligentes, automações, importação de documentos, recomendações e atendimento a pequenos negócios são evoluções futuras.


<!-- project-flow:catalog:start -->
## Convenção de títulos

- Convenção de públicos: single
- Públicos:
  - USUARIO
- Confirmação:
  - Confirmado em: 2026\-11\-11T12:06:47\.153690\+00:00
  - Confirmado por: Agente — proposta ainda não aprovada pelo usuário
  - Decisão: Proposta do agente: \[WEB\] \[USUARIO\] Nome da capacidade; sujeita à aprovação integral do catálogo\.
- Telas compartilhadas e públicas: USUARIO identifica o titular da conta pessoal; os fluxos públicos de acesso pertencem à mesma jornada\. Proposta de títulos para este catálogo, independente das issues antigas\.
- Superfícies:
  - WEB

## Catálogo

### 1. visual — Feature: \[WEB\] \[USUARIO\] Adequação visual do FinAI

- Público:
  - USUARIO
- Entrega visível: Identidade, estrutura de página e navegação responsiva inspecionáveis conforme a referência\.
- Resultado para o usuário: Navegar por uma base visual coerente com o design informado\.
- Incluído:
  - Marca, cores, tipografia, espaçamento, componentes e estrutura compartilhada do design, Navegação responsiva entre Visão geral, Transações e Assistente; estados visuais e acessibilidade demonstrados, Adequar as superfícies existentes incluídas na entrevista, preservando seu comportamento; adaptar textos de armazenamento e IA
- Limite: Entrega visual própria; não inclui operações financeiras nem apresenta simulações como funcionalidades prontas\.
- Dependências:
  - Nenhum.
- Justificativas dos bloqueios:
  - Nenhum.
- Motivo da posição:
  - Critério de ordem: usage\-lifecycle
  - Evidências:
    - conversation\-input\-001, conversation\-input\-002, design\-input\-001
  - Item: visual
  - Justificativa: Primeiro estabelecer a identidade e a navegação da experiência aprovada\.

- Atores:
  - Titular de conta pessoal
- Candidatos:
  - c\-visual
- Evidências:
  - conversation\-input\-001, conversation\-input\-002, design\-input\-001
- Objetivo humano: Navegar por uma base visual coerente com o design informado\.
- Ciclo de vida: active
- Resultado ou desvio: Identidade, estrutura de página e navegação responsiva inspecionáveis conforme a referência\.
- Justificativa do limite: Entrega visual própria; não inclui operações financeiras nem apresenta simulações como funcionalidades prontas\.
- Posição: 1

### 2. acesso — Feature: \[WEB\] \[USUARIO\] Acesso à conta pessoal

- Público:
  - USUARIO
- Entrega visível: Cadastro, entrada, saída e recuperação de senha disponíveis ao titular\.
- Resultado para o usuário: Criar e acessar uma conta própria para manter o espaço financeiro pessoal separado\.
- Incluído:
  - Cadastro, login, saída e recuperação de senha, Estados de validação, sucesso e falha na jornada de acesso, Identificação da conta atual; delimitação de acesso ao espaço pessoal
- Limite: Capacidade completa de acesso; isolamento de cada operação e consulta financeira é coberto na Feature que a realiza\. Não se presume nenhuma entrega anterior\.
- Dependências:
  - visual
- Justificativas dos bloqueios:
  - Registro 1:
    - Bloqueado por: visual
    - Por que impede a entrega: A política de entrega visual primeiro requer validar a base antes das funcionalidades que a consomem; não afirma impossibilidade de desenvolvimento técnico independente\.
    - Evidências:
      - design\-input\-001, conversation\-input\-002, conversation\-input\-001
    - Item: acesso
    - Capacidade fornecida: Base visual compartilhada adequada ao design
- Motivo da posição:
  - Critério de ordem: dependency
  - Evidências:
    - conversation\-input\-001, conversation\-input\-002, design\-input\-001
  - Item: acesso
  - Justificativa: Habilitar a conta pessoal antes de aceitar operações sobre finanças do titular\.

- Atores:
  - Visitante, Titular de conta pessoal
- Candidatos:
  - c\-acesso
- Evidências:
  - conversation\-input\-001, conversation\-input\-002, design\-input\-001
- Objetivo humano: Criar e acessar uma conta própria para manter o espaço financeiro pessoal separado\.
- Ciclo de vida: active
- Resultado ou desvio: Cadastro, entrada, saída e recuperação de senha disponíveis ao titular\.
- Justificativa do limite: Capacidade completa de acesso; isolamento de cada operação e consulta financeira é coberto na Feature que a realiza\. Não se presume nenhuma entrega anterior\.
- Posição: 2

### 3. transacoes — Feature: \[WEB\] \[USUARIO\] Gestão de transações

- Público:
  - USUARIO
- Entrega visível: Titular cadastra, consulta, edita e exclui suas movimentações persistidas no sistema\.
- Resultado para o usuário: Registrar e manter receitas e despesas pessoais com categorias predefinidas e histórico\.
- Incluído:
  - Criar receitas e despesas manualmente; editar e excluir com confirmação, Disponibilizar e selecionar categorias predefinidas compatíveis com receita ou despesa, Histórico, detalhes, busca por descrição, mês, filtros de tipo/categoria, limpeza e paginação demonstrados, Persistência no sistema e isolamento por titular em todas as operações, Formulário e lista do design; estados vazio, sem resultados, validação, salvamento, sucesso e falha
- Limite: Categorias são parte da classificação da transação; não há demanda de manutenção independente de categorias\. Não inclui dashboard nem interação por IA\.
- Dependências:
  - acesso
- Justificativas dos bloqueios:
  - Registro 1:
    - Bloqueado por: acesso
    - Por que impede a entrega: A entrega integrada das transações exige um titular autenticado e um espaço pessoal para provar o isolamento confirmado pelo usuário\.
    - Evidências:
      - design\-input\-001, conversation\-input\-002, conversation\-input\-001
    - Item: transacoes
    - Capacidade fornecida: Acesso a uma conta individual identificada
- Motivo da posição:
  - Critério de ordem: dependency
  - Evidências:
    - conversation\-input\-001, conversation\-input\-002, design\-input\-001
  - Item: transacoes
  - Justificativa: Disponibilizar os registros e categorias que alimentam as consultas\.

- Atores:
  - Titular de conta pessoal
- Candidatos:
  - c\-transacoes
- Evidências:
  - conversation\-input\-001, conversation\-input\-002, design\-input\-001
- Objetivo humano: Registrar e manter receitas e despesas pessoais com categorias predefinidas e histórico\.
- Ciclo de vida: active
- Resultado ou desvio: Titular cadastra, consulta, edita e exclui suas movimentações persistidas no sistema\.
- Justificativa do limite: Categorias são parte da classificação da transação; não há demanda de manutenção independente de categorias\. Não inclui dashboard nem interação por IA\.
- Posição: 3

### 4. dashboard — Feature: \[WEB\] \[USUARIO\] Dashboard financeiro

- Público:
  - USUARIO
- Entrega visível: Saldo geral, receitas e despesas do mês e últimas movimentações refletem os dados do titular\.
- Resultado para o usuário: Compreender a situação financeira pessoal a partir dos registros reais\.
- Incluído:
  - Saldo geral e totais mensais; seleção de mês, Balanço simples de receitas/despesas e resultado mensal demonstrados no design, Movimentações recentes e acessos ao histórico, cadastro e assistente, Atualização após alterações persistidas; isolamento por titular; estados vazio e indisponibilidade
- Limite: Entrega de leitura e síntese; o histórico completo e as operações pertencem à gestão de transações\. O balanço simples não amplia para relatórios avançados\.
- Dependências:
  - transacoes
- Justificativas dos bloqueios:
  - Registro 1:
    - Bloqueado por: transacoes
    - Por que impede a entrega: O aceite integrado usa dados financeiros reais persistidos; dados fictícios não demonstram a entrega final\.
    - Evidências:
      - design\-input\-001, conversation\-input\-002, conversation\-input\-001
    - Item: dashboard
    - Capacidade fornecida: Movimentações pessoais persistidas e classificadas
- Motivo da posição:
  - Critério de ordem: usage\-lifecycle
  - Evidências:
    - conversation\-input\-001, conversation\-input\-002, design\-input\-001
  - Item: dashboard
  - Justificativa: Após os registros, apresentar a situação financeira antes da jornada conversacional na ordem sugerida\.

- Atores:
  - Titular de conta pessoal
- Candidatos:
  - c\-dashboard
- Evidências:
  - conversation\-input\-001, conversation\-input\-002, design\-input\-001
- Objetivo humano: Compreender a situação financeira pessoal a partir dos registros reais\.
- Ciclo de vida: active
- Resultado ou desvio: Saldo geral, receitas e despesas do mês e últimas movimentações refletem os dados do titular\.
- Justificativa do limite: Entrega de leitura e síntese; o histórico completo e as operações pertencem à gestão de transações\. O balanço simples não amplia para relatórios avançados\.
- Posição: 4

### 5. assistente — Feature: \[WEB\] \[USUARIO\] Assistente financeiro com IA

- Público:
  - USUARIO
- Entrega visível: A conversa transforma mensagens em propostas revisáveis e responde com dados reais do titular\.
- Resultado para o usuário: Registrar e consultar finanças pessoais em linguagem natural com IA real\.
- Incluído:
  - Chat com IA real e sugestões de início da conversa, Identificar tipo, valor, descrição, categoria e data; solicitar informações ausentes ou ambíguas, Apresentar proposta; permitir corrigir ou cancelar; persistir somente após confirmação do usuário, Consultar saldo, totais, categorias, períodos e movimentações usando registros reais do titular, Estados de processamento, falta de dados, erro de interpretação, falha de serviço e falha de persistência, com isolamento por titular, Aparência do chat e ações do design; substituir rótulos de assistente simulado
- Limite: Única capacidade conversacional reúne registro e consulta, com aceite integrado próprio\. Não inclui editar/excluir por IA nem aconselhamento, automações ou múltiplos agentes\.
- Dependências:
  - transacoes
- Justificativas dos bloqueios:
  - Registro 1:
    - Bloqueado por: transacoes
    - Por que impede a entrega: O aceite integrado usa dados financeiros reais persistidos; dados fictícios não demonstram a entrega final\.
    - Evidências:
      - design\-input\-001, conversation\-input\-002, conversation\-input\-001
    - Item: assistente
    - Capacidade fornecida: Movimentações pessoais persistidas e classificadas
- Motivo da posição:
  - Critério de ordem: usage\-lifecycle
  - Evidências:
    - conversation\-input\-001, conversation\-input\-002, design\-input\-001
  - Item: assistente
  - Justificativa: Concluir a jornada com registro e consulta por IA; pode avançar se o dashboard estiver impedido, pois não depende dele\.

- Atores:
  - Titular de conta pessoal
- Candidatos:
  - c\-assistente
- Evidências:
  - conversation\-input\-001, conversation\-input\-002, design\-input\-001
- Objetivo humano: Registrar e consultar finanças pessoais em linguagem natural com IA real\.
- Ciclo de vida: active
- Resultado ou desvio: A conversa transforma mensagens em propostas revisáveis e responde com dados reais do titular\.
- Justificativa do limite: Única capacidade conversacional reúne registro e consulta, com aceite integrado próprio\. Não inclui editar/excluir por IA nem aconselhamento, automações ou múltiplos agentes\.
- Posição: 5

## Cobertura comportamental

- Registro 1:
  - Públicos:
    - USUARIO
  - Itens consumidores: Nenhum.
  - Decisão: Nenhum.
  - Comportamento: Identidade, tipografia, estrutura, navegação responsiva, componentes e estados acessíveis; aparência preservada com rótulos de persistência e IA adaptados\.
  - Destino: covered
  - Evidências:
    - Registro 1:
      - Localizador: :root; \.app; \.sidebar; \.topbar; @media; DESIGN\-MANIFEST\.json
      - Fonte: design\-input\-001
  - Tipo de evidência: demonstrated
  - ID: b\-visual
  - Item responsável: visual
  - Confronto com o repositório:
    - Evidências:
      - resources/js/components/app\-sidebar\.tsx, resources/js/pages/dashboard\.tsx, routes/web\.php, app/Models/User\.php
    - Mudança proposta: Identidade, tipografia, estrutura, navegação responsiva, componentes e estados acessíveis; aparência preservada com rótulos de persistência e IA adaptados\.
    - Estado: partial
- Registro 2:
  - Públicos:
    - USUARIO
  - Itens consumidores:
    - transacoes, dashboard, assistente
  - Decisão: Nenhum.
  - Comportamento: Cadastro, login, saída e recuperação para contas individuais; nenhuma entrega presumida como pronta\.
  - Destino: covered
  - Evidências:
    - Registro 1:
      - Localizador: Resposta sobre contas individuais
      - Fonte: conversation\-input\-002
  - Tipo de evidência: annotation
  - ID: b\-contas
  - Item responsável: acesso
  - Confronto com o repositório:
    - Evidências:
      - resources/js/components/app\-sidebar\.tsx, resources/js/pages/dashboard\.tsx, routes/web\.php, app/Models/User\.php
    - Mudança proposta: Cadastro, login, saída e recuperação para contas individuais; nenhuma entrega presumida como pronta\.
    - Estado: partial
- Registro 3:
  - Públicos:
    - USUARIO
  - Itens consumidores: Nenhum.
  - Decisão: Nenhum.
  - Comportamento: Cadastro manual de receita/despesa com tipo, valor, descrição, categoria e data; validação e mensagens de salvamento/sucesso/falha\.
  - Destino: covered
  - Evidências:
    - Registro 1:
      - Localizador: \#transaction\-dialog; openForm; fieldError; transaction\-form\.onsubmit
      - Fonte: design\-input\-001
  - Tipo de evidência: demonstrated
  - ID: b\-cadastro
  - Item responsável: transacoes
  - Confronto com o repositório:
    - Evidências:
      - resources/js/components/app\-sidebar\.tsx, resources/js/pages/dashboard\.tsx, routes/web\.php, app/Models/User\.php
    - Mudança proposta: Cadastro manual de receita/despesa com tipo, valor, descrição, categoria e data; validação e mensagens de salvamento/sucesso/falha\.
    - Estado: absent
- Registro 4:
  - Públicos:
    - USUARIO
  - Itens consumidores:
    - dashboard, assistente
  - Decisão: Nenhum.
  - Comportamento: Categorias predefinidas por tipo, disponíveis na classificação das receitas e despesas\.
  - Destino: covered
  - Evidências:
    - Registro 1:
      - Localizador: §§3\.2 e 3\.3; design: cats; categoryOptions
      - Fonte: conversation\-input\-001
  - Tipo de evidência: annotation
  - ID: b\-categorias
  - Item responsável: transacoes
  - Confronto com o repositório:
    - Evidências:
      - resources/js/components/app\-sidebar\.tsx, resources/js/pages/dashboard\.tsx, routes/web\.php, app/Models/User\.php
    - Mudança proposta: Categorias predefinidas por tipo, disponíveis na classificação das receitas e despesas\.
    - Estado: absent
- Registro 5:
  - Públicos:
    - USUARIO
  - Itens consumidores: Nenhum.
  - Decisão: Nenhum.
  - Comportamento: Consultar detalhes; editar; excluir somente após confirmação; refletir alterações persistidas\.
  - Destino: covered
  - Evidências:
    - Registro 1:
      - Localizador: \#detail\-dialog; \#delete\-dialog; openDetail; confirm\-delete
      - Fonte: design\-input\-001
  - Tipo de evidência: demonstrated
  - ID: b\-manutencao
  - Item responsável: transacoes
  - Confronto com o repositório:
    - Evidências:
      - resources/js/components/app\-sidebar\.tsx, resources/js/pages/dashboard\.tsx, routes/web\.php, app/Models/User\.php
    - Mudança proposta: Consultar detalhes; editar; excluir somente após confirmação; refletir alterações persistidas\.
    - Estado: absent
- Registro 6:
  - Públicos:
    - USUARIO
  - Itens consumidores: Nenhum.
  - Decisão: Nenhum.
  - Comportamento: Histórico por mês, busca por descrição, tipo/categoria, limpar filtros, paginação e estados vazio/sem resultados\.
  - Destino: covered
  - Evidências:
    - Registro 1:
      - Localizador: \#transactions; renderHistory; clear\-filters; pagination
      - Fonte: design\-input\-001
  - Tipo de evidência: demonstrated
  - ID: b\-historico
  - Item responsável: transacoes
  - Confronto com o repositório:
    - Evidências:
      - resources/js/components/app\-sidebar\.tsx, resources/js/pages/dashboard\.tsx, routes/web\.php, app/Models/User\.php
    - Mudança proposta: Histórico por mês, busca por descrição, tipo/categoria, limpar filtros, paginação e estados vazio/sem resultados\.
    - Estado: absent
- Registro 7:
  - Públicos:
    - USUARIO
  - Itens consumidores:
    - dashboard, assistente
  - Decisão: Nenhum.
  - Comportamento: Persistir todas as transações no sistema e isolar operações por titular, adaptando o armazenamento apenas local demonstrado\.
  - Destino: covered
  - Evidências:
    - Registro 1:
      - Localizador: Resposta sobre persistência no sistema; resposta sobre finanças separadas
      - Fonte: conversation\-input\-002
  - Tipo de evidência: annotation
  - ID: b\-persistencia
  - Item responsável: transacoes
  - Confronto com o repositório:
    - Evidências:
      - resources/js/components/app\-sidebar\.tsx, resources/js/pages/dashboard\.tsx, routes/web\.php, app/Models/User\.php
    - Mudança proposta: Persistir todas as transações no sistema e isolar operações por titular, adaptando o armazenamento apenas local demonstrado\.
    - Estado: absent
- Registro 8:
  - Públicos:
    - USUARIO
  - Itens consumidores: Nenhum.
  - Decisão: Nenhum.
  - Comportamento: Saldo geral; totais e contagens mensais; balanço simples e resultado; últimas movimentações; mês e atalhos; estados vazio/indisponível\.
  - Destino: covered
  - Evidências:
    - Registro 1:
      - Localizador: \#overview; render; \#recent; \#month; \#open\-chat
      - Fonte: design\-input\-001
  - Tipo de evidência: demonstrated
  - ID: b\-dashboard
  - Item responsável: dashboard
  - Confronto com o repositório:
    - Evidências:
      - resources/js/components/app\-sidebar\.tsx, resources/js/pages/dashboard\.tsx, routes/web\.php, app/Models/User\.php
    - Mudança proposta: Saldo geral; totais e contagens mensais; balanço simples e resultado; últimas movimentações; mês e atalhos; estados vazio/indisponível\.
    - Estado: absent
- Registro 9:
  - Públicos:
    - USUARIO
  - Itens consumidores: Nenhum.
  - Decisão: Nenhum.
  - Comportamento: Dashboard usa somente registros reais do titular e reflete criações, edições e exclusões\.
  - Destino: covered
  - Evidências:
    - Registro 1:
      - Localizador: §§3\.1 e 4
      - Fonte: conversation\-input\-001
  - Tipo de evidência: annotation
  - ID: b\-coerencia
  - Item responsável: dashboard
  - Confronto com o repositório:
    - Evidências:
      - resources/js/components/app\-sidebar\.tsx, resources/js/pages/dashboard\.tsx, routes/web\.php, app/Models/User\.php
    - Mudança proposta: Dashboard usa somente registros reais do titular e reflete criações, edições e exclusões\.
    - Estado: absent
- Registro 10:
  - Públicos:
    - USUARIO
  - Itens consumidores: Nenhum.
  - Decisão: Nenhum.
  - Comportamento: Chat com IA real, sugestões, envio, processamento e falhas de interpretação/serviço; aparência do design\.
  - Destino: covered
  - Evidências:
    - Registro 1:
      - Localizador: \#assistant; \#chat\-form; suggestions; send; handle
      - Fonte: design\-input\-001
  - Tipo de evidência: demonstrated
  - ID: b\-chat
  - Item responsável: assistente
  - Confronto com o repositório:
    - Evidências:
      - resources/js/components/app\-sidebar\.tsx, resources/js/pages/dashboard\.tsx, routes/web\.php, app/Models/User\.php
    - Mudança proposta: Chat com IA real, sugestões, envio, processamento e falhas de interpretação/serviço; aparência do design\.
    - Estado: absent
- Registro 11:
  - Públicos:
    - USUARIO
  - Itens consumidores: Nenhum.
  - Decisão: Nenhum.
  - Comportamento: Extrair tipo, valor, descrição, categoria e data; pedir complementação; proposta com confirmar, corrigir e cancelar; nenhuma persistência antes de confirmar\.
  - Destino: covered
  - Evidências:
    - Registro 1:
      - Localizador: completePending; showProposal; cancelProposal; chatCorrection
      - Fonte: design\-input\-001
  - Tipo de evidência: demonstrated
  - ID: b\-proposta
  - Item responsável: assistente
  - Confronto com o repositório:
    - Evidências:
      - resources/js/components/app\-sidebar\.tsx, resources/js/pages/dashboard\.tsx, routes/web\.php, app/Models/User\.php
    - Mudança proposta: Extrair tipo, valor, descrição, categoria e data; pedir complementação; proposta com confirmar, corrigir e cancelar; nenhuma persistência antes de confirmar\.
    - Estado: absent
- Registro 12:
  - Públicos:
    - USUARIO
  - Itens consumidores: Nenhum.
  - Decisão: Nenhum.
  - Comportamento: Consultas de saldo, receitas/despesas, períodos, categorias e últimas movimentações baseadas em dados reais do titular, sem inventar dados\.
  - Destino: covered
  - Evidências:
    - Registro 1:
      - Localizador: §3\.4; §4; design: query
      - Fonte: conversation\-input\-001
  - Tipo de evidência: annotation
  - ID: b\-consultas
  - Item responsável: assistente
  - Confronto com o repositório:
    - Evidências:
      - resources/js/components/app\-sidebar\.tsx, resources/js/pages/dashboard\.tsx, routes/web\.php, app/Models/User\.php
    - Mudança proposta: Consultas de saldo, receitas/despesas, períodos, categorias e últimas movimentações baseadas em dados reais do titular, sem inventar dados\.
    - Estado: absent
- Registro 13:
  - Públicos:
    - USUARIO
  - Itens consumidores: Nenhum.
  - Decisão:
    - Confirmado em: 2026\-11\-11T12:06:47\.153690\+00:00
    - Confirmado por: Usuário nesta conversa
    - Decisão: Exclusões e evoluções futuras explicitadas pelo usuário no escopo inicial\.
  - Comportamento: Fora do MVP: bancos, extratos, cartões, metas, relatórios avançados, gestão empresarial, múltiplos agentes; evoluções futuras permanecem fora desta entrega\.
  - Destino: excluded
  - Evidências:
    - Registro 1:
      - Localizador: §§5 e 7
      - Fonte: conversation\-input\-001
  - Tipo de evidência: annotation
  - ID: b\-fora
  - Item responsável: Nenhum.
  - Confronto com o repositório:
    - Evidências:
      - resources/js/components/app\-sidebar\.tsx, resources/js/pages/dashboard\.tsx, routes/web\.php, app/Models/User\.php
    - Mudança proposta: Preservar exclusões expressas do MVP\.
    - Estado: absent

## Inventário e referências

- Inventário:
  - Registro 1:
    - Decisão: Nenhum.
    - Origem: Conversa com o usuário
    - Papel da fonte: behavioral
    - Fonte: conversation\-input\-001
  - Registro 2:
    - Decisão: Nenhum.
    - Origem: Conversa com o usuário
    - Papel da fonte: behavioral
    - Fonte: conversation\-input\-002
  - Registro 3:
    - Decisão: Nenhum.
    - Origem: C:\\Users\\maari\\Downloads\\FinAI\-Controle\-Financeiro\.zip
    - Papel da fonte: behavioral
    - Fonte: design\-input\-001
- Referências entre fontes:
  - Registro 1:
    - Decisão: Nenhum.
    - Fonte de origem: design\-input\-001
    - ID: zip\-entry
    - Fonte: design\-input\-001
    - Estado: included
    - Destino da referência: index\.html
  - Registro 2:
    - Decisão: Nenhum.
    - Fonte de origem: design\-input\-001
    - ID: zip\-handoff
    - Fonte: design\-input\-001
    - Estado: included
    - Destino da referência: DESIGN\-HANDOFF\.md
  - Registro 3:
    - Decisão: Nenhum.
    - Fonte de origem: design\-input\-001
    - ID: zip\-manifest
    - Fonte: design\-input\-001
    - Estado: included
    - Destino da referência: DESIGN\-MANIFEST\.json
- Material solicitado:
  - Escopo MVP enviado na conversa, C:/Users/maari/Downloads/FinAI\-Controle\-Financeiro\.zip, Respostas de delimitação do usuário
- Tipo de seleção: complete\-package

## Fontes

- Registro 1:
  - decision_reconciliation: not\-applicable
  - extraction_method: Transcrição UTF\-8 da entrada do usuário, com quebras de linha LF
  - fully_read: true
  - hash_unavailable_reason: Nenhum.
  - ID: conversation\-input\-001
  - Nome: Escopo Inicial do MVP
  - normalized_sha256: 370f11679cbcf03951fa694bb3975f55b4325039258033749e57e93a226a3086
  - Origem: Conversa com o usuário
  - original_sha256: f64ad2f891515ac642c71cc7731d86335e1d33a81347c5109f42b788f9abbd2c
  - Caminho: sources/conversation\-input\-001\.md
  - Estado: normalized
  - Tipo: conversa
- Registro 2:
  - decision_reconciliation: not\-applicable
  - extraction_method: Transcrição UTF\-8 da entrada do usuário, com quebras de linha LF
  - fully_read: true
  - hash_unavailable_reason: Nenhum.
  - ID: conversation\-input\-002
  - Nome: Decisões de delimitação do catálogo
  - normalized_sha256: 6ae4c34f0e767dcfc6c6c7b897409aca147a455870118fbc2490aab6b0c5592f
  - Origem: Conversa com o usuário
  - original_sha256: cd643306d1cc5f905e8db3e64d8f0d63861f785ae4811e7a35d7be2673b8c79a
  - Caminho: sources/conversation\-input\-002\.md
  - Estado: normalized
  - Tipo: conversa
- Registro 3:
  - decision_reconciliation: not\-applicable
  - extraction_method: zipfile; três membros UTF\-8 lidos integralmente sem executar o conteúdo
  - fully_read: true
  - hash_unavailable_reason: Nenhum.
  - ID: design\-input\-001
  - Nome: FinAI\-Controle\-Financeiro\.zip
  - normalized_sha256: 867b473644faa8058016c35bdf58adc874597f5b7c6aa17e41f484cb5be8e7ee
  - Origem: C:\\Users\\maari\\Downloads\\FinAI\-Controle\-Financeiro\.zip
  - original_sha256: d7fec0da8d116208b921ee8cb152b8c3710cf4a7500e30aca6d7b43270dddbd5
  - Caminho: sources/design\-input\-001\.md
  - Estado: normalized
  - Tipo: pacote de design

## Alocação física das fontes

- Registro 1:
  - Itens:
    - visual, acesso, transacoes, dashboard, assistente
  - Local de armazenamento: scope\-shared
  - Caminho: sources/conversation\-input\-001\.md
  - Fonte: conversation\-input\-001
- Registro 2:
  - Itens:
    - visual, acesso, transacoes, dashboard, assistente
  - Local de armazenamento: scope\-shared
  - Caminho: sources/conversation\-input\-002\.md
  - Fonte: conversation\-input\-002
- Registro 3:
  - Itens:
    - visual, acesso, transacoes, dashboard, assistente
  - Local de armazenamento: scope\-shared
  - Caminho: sources/design\-input\-001\.md
  - Fonte: design\-input\-001

## Candidatos

- Registro 1:
  - Itens:
    - visual
  - ID: c\-visual
  - Justificativa: Entrega visual própria; não inclui operações financeiras nem apresenta simulações como funcionalidades prontas\.
  - Estado: decided
- Registro 2:
  - Itens:
    - acesso
  - ID: c\-acesso
  - Justificativa: Capacidade completa de acesso; isolamento de cada operação e consulta financeira é coberto na Feature que a realiza\. Não se presume nenhuma entrega anterior\.
  - Estado: decided
- Registro 3:
  - Itens:
    - transacoes
  - ID: c\-transacoes
  - Justificativa: Categorias são parte da classificação da transação; não há demanda de manutenção independente de categorias\. Não inclui dashboard nem interação por IA\.
  - Estado: decided
- Registro 4:
  - Itens:
    - dashboard
  - ID: c\-dashboard
  - Justificativa: Entrega de leitura e síntese; o histórico completo e as operações pertencem à gestão de transações\. O balanço simples não amplia para relatórios avançados\.
  - Estado: decided
- Registro 5:
  - Itens:
    - assistente
  - ID: c\-assistente
  - Justificativa: Única capacidade conversacional reúne registro e consulta, com aceite integrado próprio\. Não inclui editar/excluir por IA nem aconselhamento, automações ou múltiplos agentes\.
  - Estado: decided

## Itens retirados

- Nenhum.

## Grafo de bloqueios

- Registro 1:
  - Bloqueado por: visual
  - Item: acesso
- Registro 2:
  - Bloqueado por: acesso
  - Item: transacoes
- Registro 3:
  - Bloqueado por: transacoes
  - Item: dashboard
- Registro 4:
  - Bloqueado por: transacoes
  - Item: assistente

## Justificativas de dependências

- Registro 1:
  - Bloqueado por: visual
  - Por que impede a entrega: A política de entrega visual primeiro requer validar a base antes das funcionalidades que a consomem; não afirma impossibilidade de desenvolvimento técnico independente\.
  - Evidências:
    - design\-input\-001, conversation\-input\-002, conversation\-input\-001
  - Item: acesso
  - Capacidade fornecida: Base visual compartilhada adequada ao design
- Registro 2:
  - Bloqueado por: acesso
  - Por que impede a entrega: A entrega integrada das transações exige um titular autenticado e um espaço pessoal para provar o isolamento confirmado pelo usuário\.
  - Evidências:
    - design\-input\-001, conversation\-input\-002, conversation\-input\-001
  - Item: transacoes
  - Capacidade fornecida: Acesso a uma conta individual identificada
- Registro 3:
  - Bloqueado por: transacoes
  - Por que impede a entrega: O aceite integrado usa dados financeiros reais persistidos; dados fictícios não demonstram a entrega final\.
  - Evidências:
    - design\-input\-001, conversation\-input\-002, conversation\-input\-001
  - Item: dashboard
  - Capacidade fornecida: Movimentações pessoais persistidas e classificadas
- Registro 4:
  - Bloqueado por: transacoes
  - Por que impede a entrega: O aceite integrado usa dados financeiros reais persistidos; dados fictícios não demonstram a entrega final\.
  - Evidências:
    - design\-input\-001, conversation\-input\-002, conversation\-input\-001
  - Item: assistente
  - Capacidade fornecida: Movimentações pessoais persistidas e classificadas

## Ordem aprovada

- visual, acesso, transacoes, dashboard, assistente

## Justificativas da ordem

- Registro 1:
  - Critério de ordem: usage\-lifecycle
  - Evidências:
    - conversation\-input\-001, conversation\-input\-002, design\-input\-001
  - Item: visual
  - Justificativa: Primeiro estabelecer a identidade e a navegação da experiência aprovada\.
- Registro 2:
  - Critério de ordem: dependency
  - Evidências:
    - conversation\-input\-001, conversation\-input\-002, design\-input\-001
  - Item: acesso
  - Justificativa: Habilitar a conta pessoal antes de aceitar operações sobre finanças do titular\.
- Registro 3:
  - Critério de ordem: dependency
  - Evidências:
    - conversation\-input\-001, conversation\-input\-002, design\-input\-001
  - Item: transacoes
  - Justificativa: Disponibilizar os registros e categorias que alimentam as consultas\.
- Registro 4:
  - Critério de ordem: usage\-lifecycle
  - Evidências:
    - conversation\-input\-001, conversation\-input\-002, design\-input\-001
  - Item: dashboard
  - Justificativa: Após os registros, apresentar a situação financeira antes da jornada conversacional na ordem sugerida\.
- Registro 5:
  - Critério de ordem: usage\-lifecycle
  - Evidências:
    - conversation\-input\-001, conversation\-input\-002, design\-input\-001
  - Item: assistente
  - Justificativa: Concluir a jornada com registro e consulta por IA; pode avançar se o dashboard estiver impedido, pois não depende dele\.

## Grupos sem bloqueios entre si no grafo

- Registro 1:
  - visual
- Registro 2:
  - acesso
- Registro 3:
  - transacoes
- Registro 4:
  - dashboard, assistente

<!-- project-flow:catalog:end -->

## Aprovação do catálogo

Aprovado pelo usuário nesta conversa com a resposta “aprovado”. Aprovação do catálogo completo e ordem, incluindo a convenção proposta. Hash: 8c275dfb1852fd8d83c9f1d70c12405fec8c1cc3b5ed263b5df4b4f5d61e0f8f.

## Progresso

1. Adequação visual do FinAI: requisito concluído e publicação integral validada na issue [#1016101](https://redmine.remsoft.com.br/issues/1016101). Documento: [feature.md](../../features/1016101-adequacao-visual-do-finai/feature.md). Estado remoto New; implementação ainda não executada.

2. Acesso à conta pessoal: requisito concluído e publicação integral validada na issue [#1016104](https://redmine.remsoft.com.br/issues/1016104). Documento: [feature.md](../../features/1016104-acesso-a-conta-pessoal/feature.md). Estado New, Sequencing

2. Relação 835: #1016101 bloqueia #1016104.

3. Gestão de transações: requisito concluído e publicação integral validada na issue [#1016105](https://redmine.remsoft.com.br/issues/1016105). Documento: [feature.md](../../features/1016105-gestao-de-transacoes/feature.md). Estado New, Sequencing

3. Relação 836: #1016104 bloqueia #1016105.

4. Dashboard financeiro: requisito concluído e publicação integral validada na issue [#1016106](https://redmine.remsoft.com.br/issues/1016106). Documento: [feature.md](../../features/1016106-dashboard-financeiro/feature.md). Estado New, Sequencing

4. Relação 837: #1016105 bloqueia #1016106.

5. Assistente financeiro com IA: requisito concluído e publicação integral validada na issue [#1016107](https://redmine.remsoft.com.br/issues/1016107). Documento: [feature.md](../../features/1016107-assistente-financeiro-com-ia/feature.md). Estado New, Sequencing

5. Relação 838: #1016105 bloqueia #1016107. Todos os itens concluídos como requisitos; conferência final validada e fechamento confirmado pelo usuário. Escopo concluído em completed.

Run do assistente: 7a9b23b8-2e46-4ab2-8c08-b95085cc6a6e; destino docs/harness/features/1016107-assistente-financeiro-com-ia/.

Run do dashboard: d346be46-ce4c-418a-a37e-bd652d5d7049; destino docs/harness/features/1016106-dashboard-financeiro/.

Run de transações: e0ce446f-cb31-446d-a20e-bfd460cccfdd; destino docs/harness/features/1016105-gestao-de-transacoes/.

Run do acesso: 92c15ad8-bf89-4c23-bf1f-6c6c4b7f6710; destino docs/harness/features/1016104-acesso-a-conta-pessoal/.

Run do item visual: 3e8baa5a-37ce-4543-a114-d102e55b5830. Destino definitivo: docs/harness/features/1016101-adequacao-visual-do-finai/. Issue criada: 1016101.

## Pausas e retomadas

## Relações nativas

## Alterações do catálogo

## Pendências, dependências e condições de retomada

## Aprovação de fechamento

Fechamento confirmado por Mário Tinelli nesta conversa com a resposta “confirmo”, em 2026-11-11T13:21:20.145136+00:00. Aprovação registrada no estado local sob 7ca363b6-ce28-456c-bf4b-003d038d3117. O resumo final aprovado foi preservado integralmente; hash SHA-256 d2a86ccfcbc8ae65eb17d07db234cf37c1cd1a64bb0322dfbc55acfd51ababc1. As cinco issues permanecem New, sem implementação executada.

## Fatiamento DEV e QA concluído

As cinco Features foram fatiadas e publicadas no projeto FinAi, Sprint 1: 17 tarefas DEV e 5 QA, totalizando 59,5h estimadas (50h DEV e 9,5h QA). Todas permanecem em New, aguardando implementação. As tasks antigas foram desconsideradas e preservadas.

| Feature | DEV | QA | Estimativa total |
| --- | --- | --- | --- |
| Adequação visual | #1016112 a #1016116 | #1016117 | 11,5h |
| Acesso à conta pessoal | #1016119 a #1016121 | #1016122 | 6,5h |
| Gestão de transações | #1016123 a #1016125 | #1016126 | 7,5h |
| Dashboard financeiro | #1016127 | #1016128 | 7h |
| Assistente financeiro com IA | #1016129 a #1016133 | #1016134 | 27h |

A QA do Assistente foi publicada com 3h, conforme correção aprovada. Os cinco documentos Word de condições de teste estão anexados às respectivas QAs e foram conferidos. Bloqueios internos e dependências externas foram publicados e verificados. A sequência vigente consta abaixo; o resumo final posterior registra o fechamento histórico dos requisitos, anterior ao fatiamento.

Os estados locais de decomposição, publicação, dependências e escopo passaram nos validadores. Esta entrega conclui o planejamento e a publicação das tarefas; não representa implementação nem execução dos testes do produto.

## Sequenciamento atual do fatiamento

Política solicitada por Mário Tinelli: a mãe e a primeira filha compartilham o número; demais filhas incrementam, incluindo QA; a próxima mãe inicia após a última filha anterior. Features sem filhas permanecem sem Sequencing até sua publicação. Esta regra substitui a numeração operacional anterior; aprovações e evidências históricas permanecem preservadas.

| Feature | Sequencing da mãe | Filhas |
| --- | --- | --- |
| [WEB] [USUARIO] Adequação visual do FinAI (#1016101) | 1 | 1–6 |
| [WEB] [USUARIO] Acesso à conta pessoal (#1016104) | 7 | 7–10 |
| [WEB] [USUARIO] Gestão de transações (#1016105) | 11 | 11–14 |
| [WEB] [USUARIO] Dashboard financeiro (#1016106) | 15 | 15–16 |
| [WEB] [USUARIO] Assistente financeiro com IA (#1016107) | 17 | 17–22 |

Próximo número disponível: 23. Recalcular após cada nova Feature fatiada, antes de avançar à seguinte. Conferência atual de 27 issues; somente custom field Sequencing foi atualizado, com demais campos verificados.

## Resumo final

### Issues

Projeto **FinAi**, versão **Sprint 1**. As cinco issues permanecem em **New**, com Sequencing de 1 a 5. Os requisitos estão aprovados e publicados; a implementação não foi executada.

| Ordem | Feature | Issue |
| --- | --- | --- |
| 1 | Adequação visual do FinAI | [#1016101](https://redmine.remsoft.com.br/issues/1016101) |
| 2 | Acesso à conta pessoal | [#1016104](https://redmine.remsoft.com.br/issues/1016104) |
| 3 | Gestão de transações | [#1016105](https://redmine.remsoft.com.br/issues/1016105) |
| 4 | Dashboard financeiro | [#1016106](https://redmine.remsoft.com.br/issues/1016106) |
| 5 | Assistente financeiro com IA | [#1016107](https://redmine.remsoft.com.br/issues/1016107) |

### Relações

#1016101 → #1016104 → #1016105 → {#1016106, #1016107}. As quatro relações nativas `blocks` estão publicadas e conferidas (IDs 835, 836, 837 e 838).

### Artefatos

O catálogo, as fontes e os registros de aprovação/validação estão neste scope.md e em suas pastas de apoio. Os cinco requisitos canônicos:

- [Adequação visual do FinAI](../../features/1016101-adequacao-visual-do-finai/feature.md).
- [Acesso à conta pessoal](../../features/1016104-acesso-a-conta-pessoal/feature.md).
- [Gestão de transações](../../features/1016105-gestao-de-transacoes/feature.md).
- [Dashboard financeiro](../../features/1016106-dashboard-financeiro/feature.md).
- [Assistente financeiro com IA](../../features/1016107-assistente-financeiro-com-ia/feature.md).

### Aprovações

Catálogo e cinco requisitos com seus planos de publicação aprovados nesta conversa. As tasks antigas foram desconsideradas; nenhuma foi alterada ou excluída.

### Validações

Cinco estados de requisito, cinco publicações integrais, quatro relações e três fontes normalizadas conferidos; projeto, versão, sequência e estados remotos verificados. Catálogo e estado do escopo validados, sem lacunas funcionais abertas. Foram validados os artefatos e a publicação, sem testes de funcionalidades implementadas.

### Próxima recomendação

Preparar as fatias DEV e QA da **Adequação visual do FinAI (#1016101)**, respeitando a ordem de dependências. A implementação ainda não foi executada.
