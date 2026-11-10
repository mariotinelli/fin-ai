# Conditions after requirement change

Use after [impact analysis](change-review.md) for a Feature/Bug with published Markdown/DOCX conditions. This integrates document revision with existing application. Historical publications lacking conditions retain their previous contract without automatic attachments.

## Prepare revised source

Reread approved requirement/current semantic review. In `.flow/slices-change-review.json`, `revisions[-1].conditions.baseline.path` points to immutable current condition/document evidence. Copy its `proposal` to `.work/conditions-proposal.json`. Update `feature.requirement_sha256` to `current_requirement.sha256` and `requirements` to approved `conditions.requirements`. Preserve other decomposition fields.

Change affected conditions only; add IDs listed in `conditions.additions` only. Unaffected conditions keep content. Retain IDs for preserved checks; new checks use fresh IDs. History reserves IDs from proposal creation, even rejection, and is shared with localized revisions. Check context, expected results, traceability and whole-requirement coverage. Resolve discovered new/contradictory behavior in the requirement first.

Reread QA through MCP with complete attachments, relations/journals, native statuses and parent execution status. Use the [localized revision](condition-revisions.md) snapshot. Completed QA needs impact presentation/next-action discussion before changes; this branch does not reopen it.

```sh
python <project-slices>/scripts/manage_condition_revision.py propose .flow/slices-condition-revisions.json .work/conditions-proposal.json --change-review .flow/slices-change-review.json --snapshot .work/qa-current.json --reason "<delta revisado>" --actor "<tech lead>" --at "<ISO-8601>"
python <project-slices>/scripts/manage_condition_revision.py approve-source .flow/slices-condition-revisions.json --sha256 "<proposal_sha256>" --actor "<tech lead>" --at "<ISO-8601>"
python <project-slices>/scripts/manage_condition_revision.py prepare-preview .flow/slices-condition-revisions.json --actor "<tech lead>" --at "<ISO-8601>"
```

Source approval needs explicit tech lead review. Incorporate/review Word edits in source first; edited copies do not replace published evidence. Generated document identifies updated requirement and receives a new revision, preserving earlier files. User-facing document/note content stays Portuguese.

**Complete when:** approved source contains authorized delta only, origins reference current requirement and Markdown conditions/selected DOCX are available for application preview.

## Approve integrated preview

Add `condition_revision` with absolute `.flow/slices-condition-revisions.json` path to the [revision-application](revision-application.md) plan. Prepare authorized task/relation operations; `operations` may be empty for document-only application. Preserve QA description/identity. Title, estimate or relation changes need their own approved delta operations and existing workflow's specific approvals.

Run `manage_revision_application.py prepare` under existing contract. Preview includes conditions in a note or, for DOCX, document/hash/attachment description/current-version note, destination QA and operations. Present full preview/file. After tech lead approval record `manage_revision_application.py approve` with `proposal_sha256`.

Record that same authorization in document state using `preview_sha256` from `prepare-preview`:

```sh
python <project-slices>/scripts/manage_condition_revision.py approve-publication .flow/slices-condition-revisions.json --sha256 "<preview_sha256>" --actor "<tech lead>" --at "<ISO-8601>"
```

This record checks corresponding application approval, not a second decision on the same preview. Changed source, requirement, impact, DOCX or application proposal needs a new approved preview. Preserve prior decisions.

**Complete when:** application/document publication bind the same semantic revision and exact approved preview.

## Apply, publish and verify

First execute/reconcile task/relation operations through application workflow. For DOCX, use `begin-upload`, `finish-upload`, `begin-attachment`, `finish-attachment`, `observe-attachment`, `begin-note`, `observe-note`, `complete` from [localized revision](condition-revisions.md), always on document state. Markdown uses only `begin-note`, `observe-note`, `complete`; note contains approved conditions. The agent executes returned MCP calls; scripts remain local.

QA snapshots reflect actually applied metadata/relations. The helper preserves application evidence per observation and accepts confirmed approved-delta changes only. Preserve description, out-of-delta fields, prior attachments and parent execution status. Received responses/observations may be recorded after local divergence; new mutations remain blocked until resolution/authorization.

After document completion, reread parent, children, relations, attachments/journals. Run `manage_revision_application.py complete --readback ... --at ...`. Application completes only after note/selected document verification too. QA readback includes complete attachments/journals.

**Complete when:** application/document revision are complete, note/selected attachment verified, confirmed operations not duplicated and out-of-delta history/artifacts preserved.

## Continue after editorial change

Approved editorial review preserves current conditions/artifacts. For later localized correction, use `propose --change-review ... --unchanged-behavior` with that editorial revision's hash/requirement map. Review/approve source/publication under localized branch; no task application is needed for editorial continuation.

After completed functional revision, document-state `validate` returns `current_proposal`, `current_conditions`, `current_document`. Use current proposal for subsequent localized adjustments. New requirement changes require new impact analysis; retain historical approvals.

**Complete when:** selected branch matches current requirement/proposal without automatic editorial republication or reused old functional authorization.
