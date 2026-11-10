# Test conditions and local DOCX

For condition changes after completed publication, including Word edits without requirement changes, follow [localized condition revision](condition-revisions.md). The branch below prepares decomposition and its initial document.

## Use DOCX for new publications

Every new Feature/Bug decomposition and QA-only path delivers conditions in DOCX and attaches that file to QA. Readable Markdown remains a preview/complementary local artifact; it neither replaces Word nor completes publication.

Record `test_conditions.document_format: docx`. When absent in a new proposal, `record-proposal` sets `docx`; a new proposal or preference selecting Markdown is rejected before approval. Format is bound to approved proposal hash; publication completes only after generating, uploading, associating and observing DOCX in QA.

Historical states lacking the field retain their DOCX contract. A new revision may change format through preview approval while preserving files, attachments and decisions. Reads/resume do not migrate history.

**Complete when:** proposal records DOCX and no new publication treats local Markdown as a substitute for the QA attachment.

## Prepare and review

After inspection and alongside proposal, apply [test-condition discipline](../../vertical-slicing/references/test-conditions.md). Record `test_conditions` in `.work/slices-proposal.json`; `record-proposal` fully preserves this structured source in each `.flow/slices-state.json` revision.

Field example using actual proposal `requirements` IDs; human-facing values stay Portuguese:

```json
{
  "test_conditions": {
    "context": "Operador autenticado na área de gestão de usuários.",
    "conditions": [
      {
        "id": "CT-001",
        "title": "Consultar o cadastro concluído",
        "context": "Conta com a permissão aprovada de gestão.",
        "verification": "Cadastrar um usuário permitido e consultar seu cadastro.",
        "expected_result": "A consulta apresenta os dados persistidos do usuário cadastrado.",
        "requirement_ids": ["R1"]
      }
    ]
  }
}
```

Document `context` and nonempty condition list are required. Each condition requires `id`, `title`, `verification`, `expected_result`, `requirement_ids`; `context`, `group`, `impact_justification` are optional text when useful. Use `impact_justification` for external regression impact. Omit empty optional fields. Schema is `schemas/slices-state.schema.json`.

Each condition references at least one requirement ID; every proposal rule/criterion needs condition references. Requirement IDs map approved local source: semantically check canonical origins. The helper checks fields, references and unique IDs, not meaning or scenario sufficiency. Removed condition IDs remain reserved; reordering/editing retained conditions preserves identity.

Run `record-proposal`/`render` under [input and persistence](input-and-persistence.md). `slices/slices.md` presents context, conditions and expected outcomes alongside slices. Resolve requirement gaps before affected-condition approval. Obtain joint tech lead approval, run `approve`, then `validate --previous` against preserved previous state.

**Complete when:** current revision contains semantically reviewed conditions and valid tech lead approval references the exact complete proposal hash. Changes require new `record-proposal`/approval while preserving previous revisions.

## Deliver Markdown and generate mandatory DOCX

Alongside DOCX, publication generates `slices/condicoes-teste-rNNN.md` from approved source and includes conditions in the complete preview. Give readable Markdown and Word document to the tech lead with child links. Preserve existing QA description.

Generate with `document_format: docx` using Python 3.10+ and its standard library, without additional libraries:

```sh
python <project-slices>/scripts/manage_slices.py render-test-conditions .flow/slices-state.json slices/condicoes-teste-r001.docx
```

Replace `001` with current decomposition revision padded to at least three digits. The document identifies Feature/Bug, Redmine ID, decomposition revision, proposal hash, requirement SHA-256, context and conditions with origins. Its Portuguese title is **Condições de teste**. This guides future verification rather than inventing execution results/evidence.

The helper requires valid approval, rechecks requirement and generates deterministic bytes for the same source/approval. It reports DOCX path/SHA-256. Earlier revisions keep their files. Identical repetition is allowed; existing different bytes are preserved. For Word edits, incorporate adjustments into structured source and review/approve a new proposal before regenerating.

**Complete when:** tech lead reviewed conditions in complete preview, receives versioned Markdown and deterministic same-source document, and the Word file was included under [attachment publication/resume](attachment-publication.md). Publication records reuse the complete-preview decision without equivalent confirmation; source/document/presented-content divergence needs a new preview.

## Compatibility

After requirement changes, follow [conditions after requirement change](requirement-condition-revisions.md). New documents identify their approved source requirement; purely editorial change may preserve the original document through approved semantic review. Condition IDs share history across localized/functional branches.

New proposals require DOCX conditions. Historical revisions/approvals without the field or with Markdown remain valid and are not auto-migrated; the generator reports the historical contract. Once DOCX contract is included, later revisions cannot discard it. Local generation does not change QA description, current publication, parent state or canonical child artifacts.
