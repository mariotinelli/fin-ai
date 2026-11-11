# [DEV] [WEB] [USUARIO] Acesso à conta pessoal - Cadastro e redefinição com política de senha consistente

- Redmine: `#1016119`
- Tipo: `DEV`
- Tracker: Task (`4`)
- Item pai: `#1016104`
- Estimativa: `1.5h`

## Descrição

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

<!-- project-slices-child:f6a85150bfafae5a82feae42414505ba47b7545a09e8b7ec43b2b92ff06d657a -->

## Relações

- `#1016119` blocks `#1016122`
