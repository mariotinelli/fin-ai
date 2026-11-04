# Revisão de mudança do requisito

Se o requisito permanece igual e o ajuste se limita às condições ou ao DOCX já publicado, siga [revisão localizada das condições](condition-revisions.md). Esse ramo não altera o baseline da decomposição nem substitui esta análise quando houver mudança do requisito.

Use esta fase quando o item pai aprovado atual não tiver o mesmo SHA-256 do requisito que fundamentou a publicação concluída. Leia primeiro a [disciplina de mudança semântica](../../vertical-slicing/references/semantic-changes.md). O fluxo registra a análise e a decisão; não implementa a política geral de atualizar ou remover tarefas.

## Preparar o plano

Confirme que `slices-state.json` está aprovado, `slices-publication.json` está concluído e ambos carregam o mesmo `semantic_baseline`. Leia o requisito atual e sua aprovação pelo contrato do `project-flow`. Monte `.work/slices-change-review-plan.json` com `classification`, `summary`, `changes` e `impact`. Cada mudança traz `id`, `classification`, `before`, `after` e `rationale`. O impacto contém listas `affected_*` e `unaffected_*` para `tasks`, `acceptance_criteria`, `coverage` e `dependencies`; cada item possui `id` e `reason`, e o conjunto precisa particionar integralmente o baseline.

Quando a publicação já possui condições deste fluxo, com ou sem DOCX, inclua também `affected_test_conditions` e `unaffected_test_conditions`, por ID estável. Considere as condições da última revisão **concluída**, incluindo ajustes anteriores feitos no ramo localizado; propostas pendentes ou rejeitadas não são o vigente. Resolva uma publicação documental com progresso remoto antes de abrir outra análise.

Nesse caso, o plano exige `conditions: {"requirements": [{"id": "R1", "summary": "..."}], "additions": [{"id": "CT-003", "reason": "..."}]}`. `requirements` representa o requisito atual aprovado; `additions` lista apenas condições novas propostas, e pode ser vazio. Particione todas as condições já vigentes no impacto, indicando quais permanecem válidas e quais precisam de alteração ou remoção. Condições preservadas devem continuar apontando para requisitos existentes. Discuta comportamento novo, contraditório ou ambíguo no requisito antes de aprovar a revisão; hashes e referências estruturais não comprovam equivalência semântica.

Execute:

```sh
python <project-slices>/scripts/manage_change_review.py prepare .flow/slices-change-review.json .work/slices-change-review-plan.json --slices-state .flow/slices-state.json --publication-state .flow/slices-publication.json --current-requirement feature.md --preview slices/change-review.md --actor "<tech lead>" --at "<ISO-8601>" --reason "<motivo>"
```

O helper deriva uma identidade estável do pai e das duas versões, inclui evidências de preservação das filhas publicadas, decisões de adoção/externalidade, Studies, divergências e dependências, e reutiliza a mesma revisão numa retomada idêntica. Mostre a prévia completa; ela separa impactos localizados dos itens ainda válidos.

Cada versão do requisito e sua aprovação possuem cópias imutáveis; somente a revisão corrente exige correspondência com os arquivos atuais. Mudanças posteriores acrescentam revisões sem apagar decisões anteriores. Após uma aplicação concluída, inclua no impacto também as filhas e relações criadas por ela.

**Concluído quando:** a comparação semântica cobre todas as diferenças e todo item do baseline aparece exatamente uma vez como afetado ou não afetado, com prévia legível e hashes íntegros.

## Decidir

Somente o tech lead da aprovação do fatiamento decide. Registre `approved` ou `rejected`:

```sh
python <project-slices>/scripts/manage_change_review.py decide .flow/slices-change-review.json --decision approved --actor "<tech lead>" --at "<ISO-8601>" --reason "<motivo>"
```

Enquanto a revisão estiver pendente ou rejeitada, mantenha publicação, documento vigente, IDs, aprovações e todo histórico intactos. Mudança editorial aprovada fica registrada e não invalida filhas nem exige refatiamento. Se todas as condições continuam válidas, preserve os artefatos vigentes: cada um mantém a identificação do requisito de origem, e a decisão semântica registra sua validade para o requisito atualizado. Esse caso não gera upload nem nota de vigência.

**Concluído quando:** uma decisão única referencia o hash corrente da classificação e do impacto; estados pendente ou rejeitado não alteraram nenhum artefato publicado.

## Liberar somente o conteúdo afetado

Para mudança funcional aprovada, peça ao helper a autorização local das keys afetadas antes de preparar qualquer mutação:

```sh
python <project-slices>/scripts/manage_change_review.py authorize .flow/slices-change-review.json --keys "dev-1" --at "<ISO-8601>"
```

O comando falha diante de baseline, requisito, classificação, impacto ou aprovação alterados; em retomada, reutiliza a autorização sem duplicá-la. Ele não chama o MCP nem atualiza/remove tarefas. Prepare depois novas revisões e aprovações vinculadas somente ao conteúdo afetado, preservando IDs e evidências dos itens não afetados.

Com condições documentadas, siga [condições após mudança do requisito](requirement-condition-revisions.md) para preparar a fonte e o formato de entrega ligados a essa decisão e incluí-los na prévia concreta da aplicação. O conjunto de IDs afetados e inclusões da revisão semântica delimita o delta documental; a autorização de uma tarefa não libera alterações em outras condições.

**Concluído quando:** a autorização referencia a revisão semântica aprovada, contém somente keys afetadas e nenhuma operação remota foi criada por esta fase.
