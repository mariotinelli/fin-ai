# Localized condition revision

Use to correct/add/remove conditions of QA from completed publication with Markdown/DOCX conditions, even without requirement change. Preserve original publication and do not recreate children. Historical QA without conditions uses its specific adoption workflow; changed requirements use [requirement-change review](change-review.md).

## Check and propose

Read approved requirement/current conditions. Inspect related code and present reason/proposed differences to the tech lead in Portuguese. Editorial corrections and additional conditions for already approved behavior fit here. New, contradictory or ambiguous behavior needs requirement resolution before approval; the helper verifies structure/hashes rather than semantic equivalence.

Reread the same QA through MCP with `attachments`, `relations`, `journals` and native statuses. Save a sanitized `.work` snapshot containing `issue`, `statuses`, `parent` (parent ID/current execution status). Completed QA stops for impact/next-action discussion; this branch does not reopen it.

Copy decomposition proposal to `.work/conditions-proposal.json` and change only `test_conditions`. After the first published revision, start from `current_proposal` returned by `validate` and preserve other fields, retaining current requirement after completed functional revision. Preserve IDs for the same verification despite edits/reordering. New conditions use fresh IDs. IDs are reserved from proposal recording, even if rejected; removed IDs cannot be reused.

For approved editorial requirement change or functional revision, follow [conditions after requirement change](requirement-condition-revisions.md). This binding authorizes only explicitly reviewed context; hashes do not imply behavioral equality.

Examples use `<helper>` for `<project-slices>/scripts/manage_condition_revision.py` and `<estado>` for `.flow/slices-condition-revisions.json`. Substitute actual actor/time.

```sh
python <helper> propose <estado> .work/conditions-proposal.json --snapshot .work/qa-current.json --unchanged-behavior --reason "<motivo>" --actor "<tech lead>" --at "<ISO-8601>"
```

`--unchanged-behavior` records semantic-review conclusion; pass it only after verifying approved-behavior boundaries. Output gives revision/proposal hash. New proposals preserve prior revisions and invalidate authority for new operations; after remote progress, reconcile/complete that cycle before another.

State stores hash-chained events and immutable evidence under `.flow/condition-evidence/`. Preserve files with state. Existing `slices-state.json`, `slices-publication.json` and `task.md` stay intact. Document numbering continues after original revision and advances for rejected proposals; gaps are expected.

**Complete when:** tech lead received the full delta, conditions retain traceability/identity, requirement stays approved and no semantic question remains open.

## Incorporate Word edits

Obtain an intact copy of current DOCX and the edited file. The helper reads paragraphs, including tables, and presents original/edited text and differences:

```sh
python <helper> compare-word <estado> --original slices/condicoes-teste-r001.docx --edited .work/edited.docx --output .work/word-review.json
```

Use the actual current revision. Original copy must match published hash; edited file never replaces that evidence. Report/immutable copies support review independently of later temporary files.

Read every difference and propose incorporation into structured source. Show additions/removals/changes to the tech lead. Clarify ambiguous IDs and tracked changes, comments or Word elements absent from extracted text; extraction neither interprets meaning nor automatically accepts edits. Record accepted/rejected adjustments and resolved ambiguities.

Append to `propose`:

```sh
--word-review .work/word-review.json --resolution "<incorporação revisada e decisões do tech lead>"
```

**Complete when:** Word differences were reviewed, decisions recorded and structured proposal contains accepted adjustments only.

## Approve source and exact delivery

After conditions/Word review, obtain explicit tech lead source approval:

```sh
python <helper> approve-source <estado> --sha256 "<proposal_sha256>" --actor "<tech lead>" --at "<ISO-8601>"
python <helper> prepare-preview <estado> --actor "<tech lead>" --at "<ISO-8601>"
```

The helper produces `slices/conditions-revision-rNNN.md`. With `test_conditions.document_format: markdown`, preview contains the complete condition note without Word. With `docx`, also produce `slices/condicoes-teste-rNNN.docx`. Preview identifies QA, source, file, hash, attachment description and exact current-version note. The document distinguishes document revision from original decomposition. Preserve earlier documents.

Present conditions in the note or selected DOCX alongside preview. Final approval authorizes shown delivery only:

```sh
python <helper> approve-publication <estado> --sha256 "<preview_sha256>" --actor "<tech lead>" --at "<ISO-8601>"
```

Source/file/preview changes need new proposal/approval. Before remote progress, another proposal is possible; afterward preserve/reconcile prior effects before escalating divergence. Reject without remote mutation through:

```sh
python <helper> reject <estado> --reason "<motivo>" --actor "<tech lead>" --at "<ISO-8601>"
```

**Complete when:** reviewed source/exact delivery have explicit tech lead decisions bound to corresponding hashes. Rejection preserves current conditions/artifacts.

## Publish and verify selected attachment

For Markdown, proceed directly to the note. For DOCX, finish this phase first.

Use the MCP contract in [document publication](attachment-publication.md). The helper handles local files only; remotely execute only returned `tool`/`arguments`.

```sh
python <helper> begin-upload <estado> --actor "<tech lead>" --at "<ISO-8601>"
python <helper> finish-upload <estado> --attempt <id> --result .work/upload-result.json --actor "<tech lead>" --at "<ISO-8601>"
python <helper> begin-attachment <estado> --snapshot .work/qa-before-link.json --actor "<tech lead>" --at "<ISO-8601>"
python <helper> finish-attachment <estado> --attempt <id> --result .work/link-result.json --actor "<tech lead>" --at "<ISO-8601>"
python <helper> observe-attachment <estado> --snapshot .work/qa-after-link.json --actor "<tech lead>" --at "<ISO-8601>"
```

Save MCP `structuredContent` objects to result files. Before association, reread QA/native statuses. Acceptance does not confirm association. Readback checks identity, metadata, earlier attachments and preserved fields; uploads without ID require a unique candidate. Verification does not download remote bytes.

Do not repeat confirmed uploads. Lost responses without token allow retry only before association intent; an unassociated remote upload may remain. Before association retry, record positive absence observation. Read failure does not prove absence. Results/observations remain recordable after local divergence without authorizing new mutations.

**Complete when:** new attachment is confirmed on the same QA and previous attachments are preserved.

## Identify current version and complete

Reread QA with all journals/attachments. The helper returns `redmine_add_comment` with the exact preview note:

```sh
python <helper> begin-note <estado> --snapshot .work/qa-before-note.json --actor "<tech lead>" --at "<ISO-8601>"
```

Call it and reread journals even after MCP success. Textual confirmation lacks note ID and is insufficient:

```sh
python <helper> observe-note <estado> --snapshot .work/qa-after-note.json --actor "<tech lead>" --at "<ISO-8601>"
python <helper> complete <estado> --snapshot .work/final-readback.json --actor "<tech lead>" --at "<ISO-8601>"
```

Final snapshot contains complete QA in `issue` and reread parent in `parent`. The note has a stable QA/revision/hash marker. Lost responses require observation before retry; absence requires complete journals. Do not resend confirmed notes. Multiple matching notes stop for tech lead reconciliation.

Only `completed` makes new delivery current in `validate`. Until then preserve previous reference and explain partial progress; if note exists, finish verification without republishing. Readback requires note, selected attachment and preserved original parent execution status. QA description/`task.md` receive no additional references.

Preserve previous state and validate history/resume:

```sh
python <helper> validate <estado> --previous .work/conditions-before.json
```

**Complete when:** state validates as completed, note/selected attachment are verified, current revision is unambiguous and proposal/decision/operation history stays intact.
