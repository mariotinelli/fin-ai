# Publicação e retomada do DOCX

Use este ramo na prévia final, no upload, no vínculo e na conferência de toda nova publicação, que exige `test_conditions.document_format: docx`. O agente chama o MCP; `manage_publication.py` apenas prepara argumentos e registra evidências locais. Não chame HTTP nem leia credenciais em scripts.

Para documentos posteriores a uma mudança de requisito, use [condições após mudança do requisito](requirement-condition-revisions.md): a autorização vem da prévia integrada da aplicação, e as operações documentais ficam em `slices-condition-revisions.json`. O contrato MCP de envio e vínculo continua o mesmo.

## Apresentar e autorizar

Depois da decisão sobre a prévia completa, gere o arquivo conforme [condições de teste](test-conditions.md). `prepare` exige `slices/condicoes-teste-rNNN.docx` correspondente à revisão da decomposição; confere seus bytes determinísticos e inclui `test_document` no hash da publicação. Confira caminho, revisão, tamanho, SHA-256, QA de destino e descrição contra a fonte e o destino já apresentados. O registro de publicação reaproveita a decisão existente; qualquer diferença material exige nova prévia completa.

Para QA adotada, a prévia autoriza acrescentar o anexo e preserva seus outros campos, relações e anexos. O snapshot de metadados usado na preparação deve conter `is_closed` para seu status nativo. QA concluída interrompe a preparação para discussão do impacto. Não interprete a adoção por si só como autorização de upload.

Alterações no documento ou na fonte depois da prévia bloqueiam novas mutações. Antes de haver progresso remoto, prepare e aprove uma nova prévia. Com progresso, preserve IDs e evidências e resolva a divergência antes de continuar; não reescreva o histórico nem regenere silenciosamente sobre edições feitas no Word.

**Concluído quando:** a autorização válida da prévia completa abrange a fonte, o documento determinístico e sua inclusão na QA identificada, sem mudar a descrição da QA.

## Enviar os bytes aprovados

Use o estado `.flow/slices-publication.json`. Todos os exemplos usam `<estado>` como abreviação desse caminho e `<instante>` como timestamp ISO-8601.

```sh
python <project-slices>/scripts/manage_publication.py begin-upload <estado> --at "<instante>"
```

Persista a intenção antes da chamada. Envie exatamente `arguments` à ferramenta `redmine_upload_file` indicada na saída. O objeto contém `path` absoluto e `expected_sha256`; o MCP compara o hash dos mesmos bytes que enviará antes de qualquer requisição remota. Salve somente o objeto `structuredContent` em um arquivo novo sob `.work`, inclusive quando houver erro MCP.

```sh
python <project-slices>/scripts/manage_publication.py finish-upload <estado> --attempt <tentativa> --result .work/upload-result-1.json --at "<instante>"
```

O helper confere tamanho, nome e hash retornados. O token é uma referência operacional para o vínculo, não uma API key; fica no estado de retomada, fora de logs e prévias humanas. Um upload confirmado não é repetido. Se a resposta se perder e não houver token, uma nova tentativa é permitida apenas antes de qualquer intenção de vínculo; a anterior permanece incerta no histórico e pode ter deixado um upload remoto não associado.

**Concluído quando:** há upload confirmado com token e metadados iguais aos do documento aprovado. Envio isolado não conclui a publicação.

## Vincular à QA

Resolva o ID definitivo da QA, criada ou adotada. Releia a issue com `attachments` e seus campos completos; consulte os status nativos. Grave um snapshot novo e sanitizado como `{"issue": {...}, "statuses": [{"id": 1, "is_closed": false}, ...]}`. A lista `attachments` deve estar presente mesmo quando vazia. Evidências referenciadas por tentativas não podem ser sobrescritas.

```sh
python <project-slices>/scripts/manage_publication.py begin-attachment <estado> --snapshot .work/qa-before-1.json --at "<instante>"
```

O helper reconfere aprovação, arquivo, QA aberta, identidade e campos e persiste a intenção e os anexos anteriores. Envie exatamente `arguments` a `redmine_attach_file`. O payload acrescenta somente o upload; a descrição do anexo informa a revisão.

```sh
python <project-slices>/scripts/manage_publication.py finish-attachment <estado> --attempt <tentativa> --result .work/attachment-result-1.json --at "<instante>"
```

Uma resposta `accepted` permanece `unknown` no progresso local até a leitura posterior. Resultados `not_sent` ou `rejected` são falhas registradas; `unconfirmed` permanece incerto. Registre resultados já recebidos mesmo se a fonte local tiver mudado; isso preserva a evidência sem autorizar uma próxima mutação.

**Concluído quando:** o vínculo possui intenção e resultado registrados ou está explicitamente incerto, pronto para reconciliação.

## Conferir e retomar

Leia novamente a QA com `attachments`, salve uma nova evidência e execute:

```sh
python <project-slices>/scripts/manage_publication.py observe-attachment <estado> --snapshot .work/qa-after-1.json --at "<instante>"
```

O helper verifica QA, campos preservados, anexos anteriores e a associação do documento. Quando o upload fornece ID, ele precisa corresponder ao anexo observado. Sem ID, exige um único anexo novo com nome, tamanho e descrição aprovados. Nome isolado não comprova identidade. Ausência de `attachments`, evidência divergente ou múltiplos candidatos impede confirmação; apresente a ambiguidade ao tech lead. Essa conferência não baixa nem compara bytes remotos.

Um vínculo `in-flight` ou `unknown` exige observação posterior de ausência antes de repetir. Falha de consulta não prova ausência. Operação confirmada não é repetida, e uploads confirmados continuam reutilizados. Preserve todas as tentativas, observações e IDs; use `validate --previous` contra a cópia anterior.

Inclua o anexo também no readback integral passado a `complete`. Somente após conferir documento, filhas, relações e status do pai o helper materializa os `task.md` e o estado concluído na mesma transação. O ramo de escopo aplica a mesma exigência.

**Concluído quando:** o anexo aprovado está associado à QA, todas as operações estão reconciliadas e o readback final permite concluir a publicação e materializar os artefatos canônicos.

## Estados históricos

- Publicações históricas concluídas continuam válidas, sem migração, geração ou upload automático.
- Publicação incompleta sem tentativa remota iniciada exige condições aprovadas e nova preparação no formato selecionado; reaproveite a autorização ainda válida somente quando o conteúdo material permanecer idêntico. Preserve revisões e aprovações anteriores.
- Publicação incompleta com tentativa remota iniciada, inclusive incerta, pode terminar pelo contrato histórico. A inclusão posterior do primeiro documento pertence ao fluxo específico de adoção de publicações antigas.
- Com progresso remoto, uma publicação que inclui `test_document` conserva esse contrato até a conferência. Sem progresso, uma nova proposta e prévia aprovadas podem selecionar Markdown, preservando a revisão e os arquivos anteriores.

Considere o histórico das tentativas, não apenas o nome do status, para identificar progresso remoto. Para revisões posteriores de condições, siga [revisão localizada](condition-revisions.md). Publicação retroativa em QA histórica permanece no fluxo específico de adoção.

**Concluído quando:** a retomada usa o contrato adequado ao histórico, sem perder progresso nem ampliar uma autorização antiga.
