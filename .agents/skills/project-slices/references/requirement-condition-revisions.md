# Condições após mudança do requisito

Use após a [análise de impacto](change-review.md) de uma Feature ou Bug com condições publicadas, em Markdown ou DOCX. Este ramo integra a revisão documental à aplicação existente. Publicações históricas sem condições conservam o contrato anterior e não recebem anexos automaticamente.

## Preparar a fonte revisada

Releia o requisito aprovado e a revisão semântica corrente. Em `.flow/slices-change-review.json`, `revisions[-1].conditions.baseline.path` aponta para a evidência imutável das condições e do documento vigentes. Copie seu `proposal` para `.work/conditions-proposal.json`. Atualize `feature.requirement_sha256` para `current_requirement.sha256` e `requirements` para o mapa aprovado em `conditions.requirements`. Preserve os demais campos da decomposição.

Altere somente as condições afetadas; inclua apenas os IDs novos listados em `conditions.additions`. Condições não afetadas conservam seu conteúdo. Mantenha IDs das verificações preservadas e atribua IDs inéditos às novas. O histórico reserva IDs desde a proposta, inclusive rejeitada, e é compartilhado com as revisões localizadas. Confira contexto, resultados esperados, rastreabilidade e cobertura do requisito inteiro. Resolva primeiro no requisito qualquer comportamento novo ou contraditório descoberto.

Releia a QA pelo MCP, com anexos, relações e journals completos, status nativos e status de execução do pai. Use o snapshot da [revisão localizada](condition-revisions.md). QA concluída exige apresentação do impacto e discussão do encaminhamento antes de alteração; este ramo não a reabre.

```sh
python <project-slices>/scripts/manage_condition_revision.py propose .flow/slices-condition-revisions.json .work/conditions-proposal.json --change-review .flow/slices-change-review.json --snapshot .work/qa-current.json --reason "<delta revisado>" --actor "<tech lead>" --at "<ISO-8601>"
python <project-slices>/scripts/manage_condition_revision.py approve-source .flow/slices-condition-revisions.json --sha256 "<proposal_sha256>" --actor "<tech lead>" --at "<ISO-8601>"
python <project-slices>/scripts/manage_condition_revision.py prepare-preview .flow/slices-condition-revisions.json --actor "<tech lead>" --at "<ISO-8601>"
```

A aprovação da fonte exige revisão explícita do tech lead. Se houver edições no Word, incorpore e revise essas alterações na fonte antes da aprovação; a cópia editada não substitui a evidência publicada. O documento gerado identifica o requisito atualizado e recebe uma nova revisão, preservando arquivos anteriores.

**Concluído quando:** a fonte aprovada contém apenas o delta autorizado, suas origens apontam para o requisito atual e as condições em Markdown ou o DOCX selecionado estão disponíveis para a prévia da aplicação.

## Aprovar a prévia integrada

No plano de [aplicação da revisão](revision-application.md), acrescente `condition_revision` com o caminho absoluto de `.flow/slices-condition-revisions.json`. Prepare as operações de tarefas e relações autorizadas; `operations` pode ser vazio quando a aplicação concreta exige somente o documento. Preserve a descrição e a identidade da QA. Alterações de título, estimativa ou relações exigem operações próprias no delta aprovado e as aprovações específicas do fluxo existente.

Execute `manage_revision_application.py prepare` conforme o contrato existente. A prévia inclui as condições na nota ou, com DOCX, o documento, hash, descrição do anexo e nota de vigência, além da QA de destino e das operações. Apresente a prévia inteira e o arquivo para revisão. Após a aprovação do tech lead, registre `manage_revision_application.py approve` com seu `proposal_sha256`.

Registre também essa mesma autorização no estado documental, usando o `preview_sha256` retornado por `prepare-preview`:

```sh
python <project-slices>/scripts/manage_condition_revision.py approve-publication .flow/slices-condition-revisions.json --sha256 "<preview_sha256>" --actor "<tech lead>" --at "<ISO-8601>"
```

Esse registro verifica a aprovação da aplicação correspondente; não pede uma segunda decisão sobre a mesma prévia. Se fonte, requisito, impacto, DOCX ou proposta da aplicação mudarem, apresente uma nova prévia e obtenha sua aprovação. Preserve todas as decisões anteriores.

**Concluído quando:** a aplicação e a publicação documental estão vinculadas à mesma revisão semântica e à prévia exata aprovada.

## Aplicar, publicar e conferir

Execute e reconcilie primeiro as operações de tarefas e relações pelo fluxo de aplicação. Com DOCX, use os comandos `begin-upload`, `finish-upload`, `begin-attachment`, `finish-attachment`, `observe-attachment`, `begin-note`, `observe-note` e `complete` da [revisão localizada](condition-revisions.md), sempre no estado documental. Com Markdown, execute somente `begin-note`, `observe-note` e `complete`; a nota contém as condições aprovadas. O agente executa as chamadas MCP retornadas; os scripts permanecem locais.

Os snapshots da QA devem refletir os metadados e as relações efetivamente aplicados. O helper conserva evidências da aplicação em cada observação e aceita somente mudanças confirmadas no delta aprovado. Ele preserva descrição, campos fora do delta, anexos anteriores e status de execução do pai. Respostas recebidas e observações podem ser registradas após uma divergência local; novas mutações continuam bloqueadas até a resolução e autorização correspondentes.

Após concluir a revisão documental, releia pai, filhas, relações, anexos e journals. Execute `manage_revision_application.py complete --readback ... --at ...`. A aplicação só conclui depois de conferir também a nota e o documento quando selecionado. O readback da QA deve incluir os anexos e journals completos.

**Concluído quando:** aplicação e revisão documental estão concluídas, nota e eventual anexo foram conferidos, operações confirmadas não foram duplicadas e os históricos e artefatos fora do delta permanecem preservados.

## Continuar depois de uma mudança editorial

Uma revisão editorial aprovada preserva as condições e seus artefatos vigentes. Se posteriormente o tech lead solicitar uma correção localizada nas condições, use `propose --change-review ... --unchanged-behavior`, com o hash e o mapa de requisitos daquela revisão editorial. Revise e aprove a fonte e a publicação conforme o ramo localizado; não é necessária uma aplicação de tarefas para essa continuidade editorial.

Depois de uma revisão funcional concluída, `validate` do estado documental retorna `current_proposal`, `current_conditions` e `current_document`. Use essa proposta vigente para ajustes localizados subsequentes. Uma nova mudança de requisito exige nova análise de impacto; aprovações anteriores permanecem no histórico.

**Concluído quando:** o ramo escolhido corresponde ao requisito e à proposta vigentes, sem republicação editorial automática nem reaproveitamento de autorização funcional antiga.
