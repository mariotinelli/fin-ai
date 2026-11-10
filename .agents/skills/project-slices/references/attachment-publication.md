# DOCX publication and resume

Use for final preview, upload, association and verification of every new publication, which requires `test_conditions.document_format: docx`. The agent calls MCP; `manage_publication.py` only prepares arguments and records local evidence. Scripts must neither call HTTP nor read credentials.

For post-requirement-change documents, use [conditions after requirement change](requirement-condition-revisions.md): authorization comes from integrated application preview and document operations live in `slices-condition-revisions.json`. Upload/association MCP contract is unchanged.

## Present and authorize

After the complete-preview decision, generate the file under [test conditions](test-conditions.md). `prepare` requires `slices/condicoes-teste-rNNN.docx` matching decomposition revision, checks deterministic bytes and includes `test_document` in publication hash. Verify path, revision, size, SHA-256, destination QA and description against already presented source/destination. Publication recording reuses the existing decision; material differences need a new complete preview.

For adopted QA, preview authorizes adding the attachment while preserving other fields, relations and attachments. Preparation metadata snapshot must contain native status `is_closed`. Completed QA stops preparation for impact discussion. Adoption alone does not authorize uploading.

Document/source changes after preview block new mutations. Without remote progress, prepare/approve a new preview. With progress, preserve IDs/evidence and resolve divergence before continuing; do not rewrite history or silently regenerate over Word edits.

**Complete when:** valid complete-preview authorization covers source, deterministic document and its addition to identified QA without changing QA description.

## Upload approved bytes

Use `.flow/slices-publication.json`. Examples abbreviate it as `<estado>` and ISO-8601 timestamp as `<instante>`.

```sh
python <project-slices>/scripts/manage_publication.py begin-upload <estado> --at "<instante>"
```

Persist intent before calling. Send exact returned `arguments` to the indicated `redmine_upload_file` tool. They include absolute `path` and `expected_sha256`; MCP compares the same bytes' hash before remote requests. Save only `structuredContent` to a new `.work` file, including MCP errors.

```sh
python <project-slices>/scripts/manage_publication.py finish-upload <estado> --attempt <tentativa> --result .work/upload-result-1.json --at "<instante>"
```

The helper checks returned size/name/hash. The token is an operational association reference, not an API key; keep it in resume state, outside logs/human previews. Confirmed uploads are not repeated. Lost responses without token allow retry only before any association intent; the previous attempt remains uncertain and may have left an unassociated remote upload.

**Complete when:** confirmed upload has token/metadata matching approved document. Upload alone does not complete publication.

## Associate with QA

Resolve final created/adopted QA ID. Reread issue with `attachments` and complete fields; consult native statuses. Save a fresh sanitized snapshot `{"issue": {...}, "statuses": [{"id": 1, "is_closed": false}, ...]}`. `attachments` must exist even when empty. Do not overwrite attempt-referenced evidence.

```sh
python <project-slices>/scripts/manage_publication.py begin-attachment <estado> --snapshot .work/qa-before-1.json --at "<instante>"
```

The helper rechecks approval, file, open QA, identity/fields and persists intent/prior attachments. Send exact `arguments` to `redmine_attach_file`. Payload adds only this upload; attachment description states revision in Portuguese.

```sh
python <project-slices>/scripts/manage_publication.py finish-attachment <estado> --attempt <tentativa> --result .work/attachment-result-1.json --at "<instante>"
```

An `accepted` response stays locally `unknown` until subsequent reading. `not_sent`/`rejected` are recorded failures; `unconfirmed` remains uncertain. Record received results even if local source changed: this preserves evidence without authorizing another mutation.

**Complete when:** association intent/result are recorded or explicitly uncertain and ready for reconciliation.

## Verify and resume

Reread QA with attachments, save new evidence and run:

```sh
python <project-slices>/scripts/manage_publication.py observe-attachment <estado> --snapshot .work/qa-after-1.json --at "<instante>"
```

The helper checks QA, preserved fields/prior attachments and document association. A returned upload ID must match observed attachment. Without ID, require one unique new attachment with approved name/size/description. Filename alone does not prove identity. Missing `attachments`, divergent evidence or multiple candidates prevent confirmation; explain ambiguity to the tech lead. This does not download/compare remote bytes.

An `in-flight`/`unknown` association needs later observed absence before retry. Failed reads do not prove absence. Confirmed operations are not repeated; confirmed uploads remain reused. Preserve attempts, observations and IDs; use `validate --previous` against a prior copy.

Include attachment in full `complete` readback. Only after document, children, relations and parent status verification does the helper atomically materialize `task.md` files/completed state. Scope branch has the same requirement.

**Complete when:** approved attachment is associated with QA, operations are reconciled and final readback permits publication completion/canonical materialization.

## Historical states

- Completed historical publications remain valid without automatic migration, generation or upload.
- Incomplete publication without remote attempts needs approved conditions and new preparation in selected format; reuse still-valid authorization only when material content stays identical. Preserve previous revisions/approvals.
- Incomplete publication with a started remote attempt, including uncertain attempts, may finish under its historical contract. Later first-document inclusion belongs to the specific historical-publication adoption workflow.
- With remote progress, publication containing `test_document` retains that contract through verification. Without progress, a new approved proposal/preview may select Markdown, preserving previous revision/files.

Use attempt history, not status name alone, to identify remote progress. Subsequent condition revisions follow [localized revision](condition-revisions.md). Retroactive publication to historical QA remains in its specific adoption workflow.

**Complete when:** resume follows the history-appropriate contract without losing progress or broadening old authorization.
