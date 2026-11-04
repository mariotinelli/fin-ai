# Revisão localizada das condições

Use este ramo para corrigir, acrescentar ou remover condições de uma QA de publicação concluída com condições em Markdown ou DOCX, mesmo sem mudança do requisito. Ele preserva a publicação original e não recria filhas. Para uma QA histórica sem condições, use o fluxo específico de adoção; para requisito alterado, siga [revisão de mudança do requisito](change-review.md).

## Conferir e propor

Leia o requisito aprovado e as condições vigentes. Inspecione o código relacionado e apresente ao tech lead o motivo e as diferenças propostas. Correções editoriais e condições adicionais de comportamentos já aprovados cabem neste ramo. Comportamento novo, contraditório ou ambíguo exige resolução no requisito antes da aprovação; o helper verifica estrutura e hashes, não equivalência semântica.

Releia a mesma QA pelo MCP, incluindo `attachments`, `relations` e `journals`, e consulte os status nativos. Salve um snapshot sanitizado em `.work`, com `issue`, `statuses` e `parent` (ID e status de execução atual do pai). QA concluída interrompe a operação para discussão do impacto e encaminhamento com o tech lead; este ramo não a reabre.

Copie a proposta da decomposição para `.work/conditions-proposal.json` e altere somente `test_conditions`. Depois da primeira revisão publicada, parta de `current_proposal` retornada por `validate` e preserve seus demais campos. Isso mantém o requisito vigente após uma revisão funcional concluída. Mantenha o ID de cada condição que continua representando a mesma verificação, mesmo quando editada ou reordenada. Atribua IDs inéditos às novas condições. IDs são reservados desde o registro da proposta, inclusive se rejeitada; depois de removidos não podem ser reutilizados.

Para uma mudança editorial de requisito já aprovada ou uma revisão funcional, siga [condições após mudança do requisito](requirement-condition-revisions.md). Esse vínculo autoriza somente o contexto explicitamente revisado; a igualdade de comportamento não pode ser inferida de hashes.

Os exemplos usam `<helper>` para `<project-slices>/scripts/manage_condition_revision.py` e `<estado>` para `.flow/slices-condition-revisions.json`. Substitua ator e instante pelos dados da operação.

```sh
python <helper> propose <estado> .work/conditions-proposal.json --snapshot .work/qa-current.json --unchanged-behavior --reason "<motivo>" --actor "<tech lead>" --at "<ISO-8601>"
```

`--unchanged-behavior` registra a conclusão da revisão semântica; só o informe depois de conferir que os ajustes se limitam ao comportamento aprovado. A saída informa revisão e hash da proposta. Uma nova proposta preserva a anterior e invalida sua autorização para novas operações; após progresso remoto, reconcilie e conclua o ciclo antes de abrir outro.

O estado guarda eventos encadeados por hash e referências a evidências imutáveis sob `.flow/condition-evidence/`. Preserve esses arquivos junto com o estado. `slices-state.json`, `slices-publication.json` e os `task.md` existentes permanecem intactos. A numeração dos documentos continua depois da revisão original e avança também para propostas rejeitadas; lacunas na sequência são esperadas.

**Concluído quando:** o tech lead recebeu o delta completo, as condições mantêm rastreabilidade e identidade, o requisito permanece aprovado e nenhuma dúvida semântica está aberta.

## Incorporar ajustes do Word

Se houve edição no Word, obtenha uma cópia íntegra do DOCX vigente e o arquivo editado. O helper lê os parágrafos, inclusive em tabelas, e apresenta o texto anterior, o texto editado e suas diferenças:

```sh
python <helper> compare-word <estado> --original slices/condicoes-teste-r001.docx --edited .work/edited.docx --output .work/word-review.json
```

Use a revisão efetivamente vigente. Uma cópia do arquivo original precisa corresponder ao hash publicado; o arquivo editado nunca substitui essa evidência. O relatório e as cópias imutáveis permitem revisar as mudanças sem depender de arquivos temporários posteriores.

O agente lê todas as diferenças e propõe sua incorporação na fonte estruturada. Mostre inclusões, remoções e alterações ao tech lead. Esclareça associações ambíguas a IDs e alterações controladas, comentários ou elementos do Word que não sejam representados pelo texto extraído; a extração não decide seu significado nem aceita mudanças automaticamente. Registre como cada ajuste foi incorporado ou rejeitado e as ambiguidades resolvidas.

Acrescente ao comando `propose`:

```sh
--word-review .work/word-review.json --resolution "<incorporação revisada e decisões do tech lead>"
```

**Concluído quando:** as diferenças do Word foram revisadas, as decisões estão registradas e a proposta estruturada contém somente os ajustes aceitos.

## Aprovar a fonte e a entrega exata

Depois da revisão das condições e dos ajustes do Word, obtenha a aprovação explícita do tech lead sobre a fonte:

```sh
python <helper> approve-source <estado> --sha256 "<proposal_sha256>" --actor "<tech lead>" --at "<ISO-8601>"
python <helper> prepare-preview <estado> --actor "<tech lead>" --at "<ISO-8601>"
```

O helper produz `slices/conditions-revision-rNNN.md`. Com `test_conditions.document_format: markdown`, a prévia contém a nota integral com as condições e não gera arquivo Word. Com `docx`, produz também `slices/condicoes-teste-rNNN.docx`. A prévia identifica QA, fonte, arquivo, hash, descrição do anexo e texto exato da nota de vigência. O documento distingue a revisão documental da decomposição original. Documentos anteriores permanecem preservados.

Apresente as condições na nota ou o DOCX selecionado junto da prévia. A aprovação final autoriza somente a entrega mostrada:

```sh
python <helper> approve-publication <estado> --sha256 "<preview_sha256>" --actor "<tech lead>" --at "<ISO-8601>"
```

Alteração da fonte, do arquivo ou da prévia exige nova proposta e aprovação. Antes de progresso remoto, é possível registrar outra proposta; com progresso, preserve e reconcilie o que já aconteceu antes de encaminhar a divergência. Para rejeitar sem mutação remota:

```sh
python <helper> reject <estado> --reason "<motivo>" --actor "<tech lead>" --at "<ISO-8601>"
```

**Concluído quando:** a fonte revisada e a entrega exata possuem decisões explícitas do tech lead, ligadas aos hashes correspondentes. Rejeição conserva as condições e os artefatos vigentes.

## Publicar e conferir o anexo quando selecionado

Com Markdown, avance diretamente para a nota. Com DOCX, conclua esta fase antes da nota.

Use o mesmo contrato MCP de [publicação do documento](attachment-publication.md). O helper só manipula arquivos locais; execute remotamente apenas o `tool` com os `arguments` retornados.

```sh
python <helper> begin-upload <estado> --actor "<tech lead>" --at "<ISO-8601>"
python <helper> finish-upload <estado> --attempt <id> --result .work/upload-result.json --actor "<tech lead>" --at "<ISO-8601>"
python <helper> begin-attachment <estado> --snapshot .work/qa-before-link.json --actor "<tech lead>" --at "<ISO-8601>"
python <helper> finish-attachment <estado> --attempt <id> --result .work/link-result.json --actor "<tech lead>" --at "<ISO-8601>"
python <helper> observe-attachment <estado> --snapshot .work/qa-after-link.json --actor "<tech lead>" --at "<ISO-8601>"
```

Salve os objetos `structuredContent` do MCP nos arquivos de resultado. Antes do vínculo, releia QA e status nativos. Uma resposta de aceite não confirma associação. O readback confere identidade, metadados, anexos anteriores e campos preservados; sem ID no upload, exige candidato único. A conferência não baixa os bytes remotos.

Um upload confirmado não é repetido. Resposta perdida sem token permite nova tentativa somente antes da intenção de vínculo; pode restar um upload remoto sem associação. Para repetir vínculo, registre antes uma observação positiva de ausência. Falha de consulta não prova ausência. Resultados recebidos e observações continuam registráveis depois de uma divergência local, sem autorizar novas mutações.

**Concluído quando:** o novo anexo está confirmado na mesma QA e os anteriores permanecem preservados.

## Indicar o vigente e concluir

Releia a QA com todos os journals e anexos. O helper retorna `redmine_add_comment` com a nota exata da prévia:

```sh
python <helper> begin-note <estado> --snapshot .work/qa-before-note.json --actor "<tech lead>" --at "<ISO-8601>"
```

Execute a chamada e releia os journals, mesmo que o MCP tenha retornado sucesso. A confirmação textual não contém o ID da nota e não basta para concluir:

```sh
python <helper> observe-note <estado> --snapshot .work/qa-after-note.json --actor "<tech lead>" --at "<ISO-8601>"
python <helper> complete <estado> --snapshot .work/final-readback.json --actor "<tech lead>" --at "<ISO-8601>"
```

O snapshot final contém a QA integral em `issue` e o pai relido em `parent`. A nota tem um marcador estável por QA, revisão e hash. Se a resposta se perder, observe antes de repetir; ausência exige lista completa de journals. Nota confirmada não é reenviada. Múltiplas notas correspondentes interrompem para reconciliação com o tech lead.

Somente `completed` passa a indicar a nova entrega como vigente no resultado de `validate`. Até lá, preserve a referência anterior e informe o progresso parcial; se a nota já existe, conclua sua conferência, sem republicá-la. O readback exige nota, anexo quando selecionado e preservação do status original de execução do pai. A descrição da QA e os `task.md` não recebem referências adicionais.

Para conferir histórico e retomada, preserve uma cópia do estado anterior e execute:

```sh
python <helper> validate <estado> --previous .work/conditions-before.json
```

**Concluído quando:** o estado valida como `completed`, a nota e o novo anexo quando selecionado estão conferidos, a revisão vigente é inequívoca e o histórico de propostas, decisões e operações permanece íntegro.
