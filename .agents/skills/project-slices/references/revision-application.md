# Approved revision application

Use after a current functional review reaches `authorized`. First read [revision-application discipline](../../vertical-slicing/references/revision-application.md). The helper processes local JSON/Markdown only; the agent reads/mutates through Redmine MCP tools.

If semantic review contains `conditions`, prepare source/document first under [conditions after requirement change](requirement-condition-revisions.md). The plan requires `condition_revision`, the prepared document-state absolute path. Preview includes the Markdown-condition note or selected exact DOCX/current-version note; approval covers publication. Document-only application may have empty `operations`.

## Prepare the delta

For a numbered source publication, apply [version block Sequencing](sequencing.md) and include `sequencing` in the plan. Existing children retain their positions unless an explicit numbering delta proves they never started. The generated preview includes any QA or later-block shifts separately from functional updates. Execute numbering updates first, using fresh evidence; add `--sequencing-snapshot` to functional `begin` and final `complete`. Preserve initial payload/approval history and reconcile approved numbering-only artifact receipts rather than silently renumbering or dropping task metadata.

Reread parent, all open/closed children and relations; save a sanitized `.work` snapshot `{"parent": {...}, "tasks": [...], "relations": [...], "complete": true}`. Use MCP issue objects with `project`, `parent`, `tracker`, status ID/name and `journals` proving cancellations. Set `complete` only after all pages. Also retrieve native statuses and save `{"statuses": [{"id": 1, "name": "..."}]}`. Local plan contains `preview_snapshot`, `status_metadata`, explicit mapping of `not_started`, `in_progress`, `completed`, `cancelled`, and `create`, `update`, `cancel`, `relation-add` or `relation-remove` operations.

Each operation binds `revision_sha256` to approved hash and lists authorized `impact_ids` only. Creates carry parent, title and description citing this hash; payload adds a stable reconciliation marker to description. Cancellations carry exact native status, reason and `replacement_keys`; relations describe native `blocks` edges. Run `prepare` with `--change-review`, `--publication-state`, `--preview`. Show the full preview in Portuguese, including exact attributes. After approval run `approve --proposal-sha256 <hash returned by prepare> --actor "<tech lead>" --at "<ISO-8601>"`. Semantic authorization identifies impact; this approval binds execution to the concrete preview.

For new children use an unused `task_key`. In `relation-add`, `attributes.issue_id`/`attributes.issue_to_id` accept published IDs or keys such as `dev-new`/`qa`; the helper resolves keys after confirming creation. Execute creates before dependent relations/cancellations. Use fresh operation keys in later cycles.

**Complete when:** tech lead approved the concrete preview hash, review/publication are current, statuses have native IDs/names, operations fit approved impact and preview distinguishes new, in-progress, completed and unstarted tasks.

## Approve sensitive tasks

For every in-progress update and cancellation, reread the complete snapshot and run `approve-task --key ... --snapshot ... --actor ... --reason ...`. Additional approval is exclusively the tech lead's and binds current task/intent hashes. Unstarted-task updates, creates and relations require no other approver.

**Complete when:** every in-progress or canceled task has specific approval for current snapshot/mutation; no broad or old approval was reused.

## Apply and resume

Before each call, produce a fresh snapshot and run `begin --key ... --snapshot ...`; it returns exact tool/payload. Record response with `finish`. Unknown results or interruption after `begin` require full readback and `observe --outcome matched|absent` before retry. Observation applies to the latest attempt: `absent` requires a complete search without a matching result; multiple matches/changed content keep reconciliation pending. For matched create/add, supply observed remote ID.

The helper rejects changed snapshots, completed tasks, cancellation without non-start proof, expanded impact and completed operations. Reconcile changes through new `prepare`. Preserve completed operations from partial application and reconcile uncertain attempts before replanning. A changed attempted intent receives a new key. Present the new preview/approvals while preserving earlier IDs, results and approvals in history.

For document application, complete task/relation operations before uploading. Then publish/verify attachment and note in document state. Preserve existing QA description/identity. Title/estimate changes follow application delta/approvals; condition revision does not implicitly authorize them.

**Complete when:** every operation completed once, with append-only attempts/observations and no duplication after partial failure.

## Verify and complete

Reread parent, tasks and relations and run `complete --readback`. The helper requires mutation payload/status, readable cancellation evidence, affected DEV→QA blockers, exact preservation of unaffected tasks/relations and unchanged parent status.

With `condition_revision`, include complete QA attachments/journals in readback. Document revision must be completed and match application preview; attachment, current-version note and previous attachments/journals are verified before overall completion.

Only after full verification does `complete` atomically replace each managed child's `task.md` whose content/relations belong to the authorized delta. It reuses paths found by type/ID, preserving ID and initially fixed slug, and applies initial publication's stable-content rules. Completed, external, adopted-but-unaffected and all out-of-delta children retain files byte-for-byte. Failure, uncertainty, partial application, divergent readback or changed local artifacts leave current `task.md` intact.

**Complete when:** `.flow/slices-revision-application.json` is `completed`, readback/canonical replacements are hash-bound, only authorized-delta `task.md` files changed, and previous adoption/externality, Study, divergence and semantic-review history is preserved.

After completed application, new requirement changes may start another cycle in the same state files. The next review includes child/relation IDs created by completed cycles. Requirement evidence, previews, observations/readbacks are copied to content-addressed files; preserve them with state.
