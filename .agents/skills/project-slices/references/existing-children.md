# Existing children and QA-only path

## Discover and decide

Read the parent with `children`, traverse all pages of open/closed children and retrieve each complete issue with relations through MCP. Save only the sanitized snapshot in `.work`, including project, parent, pagination, IDs, tracker/fields, title, description, estimate and relations. Present all children to the tech lead; existing children do not prove the parent was sliced.

For each child, record an `existing_children_review` disposition of `adopt` linked to a proposed key or `keep-external`. Adoption identifies every accepted difference between proposed delivery and remote baseline; project/parent mismatch prevents adoption. External disposition selects no key and authorizes no change. Complete snapshot, hash, actor, timestamp and reason belong to the approved publication revision.

Before asking, present each child as `#<ID> — <full title exactly as in Redmine>`, preserving every prefix and suffix. Show proposed action in Portuguese (“adotar” or “manter externa”), tracker, status, estimate, relations and differences. For adoption, also identify the destination slice's full title when different; the key is secondary. Identify related blockers by full task title and confirmed ID where available. The approval question must refer to this identified list, not replace titles with `dev-1`, `qa`, suffixes alone or summaries such as “QA da Autenticação”.

Portuguese example: `#1014746 — [DEV] [WEB] [PUBLICO] Autenticação - Entrada e navegação de contas ativas`; proposed action: adopt as the same-title delivery (internal key `dev-1`). Showing the title identifies the task; it still stays outside the published description body.

**Complete when:** every child appears with ID, full title and proposed action in the grouped preview, every discovered ID has exactly one disposition, each adoption references a unique key, and all differences are visible or block the single decision.

## Resume without duplication

For new publication with a document, the final preview identifies adopted QA and explicitly authorizes adding only the approved DOCX. This is the exception to read-only adoption below: preserve all other fields, relations and existing attachments. Check native `is_closed` during preparation and reread QA before association; completed QA requires tech lead impact discussion and stops the operation. See [attachment publication and resume](attachment-publication.md). Completed historical publication receives no document through this branch.

Treat an adopted child as observed remote origin rather than completed creation. Preserve its ID in the revision and use it for already observed relations. Adoption is read-only: it does not change child status, tracker, description, estimate or relations. When an approved blocker touches an adopted child, both endpoints must be adopted existing children and the relation must appear in the complete snapshot; otherwise present the missing relation as reconciliation evidence and stop adoption. On resume, validate hashes and reread before repeating ambiguous operations; `begin-create` is exclusive to new keys and `begin-relation` to relations between new keys. External children remain outside managed `children`/`operations` and appear in readback only to prove preservation.

**Complete when:** adopted keys retain IDs, only new keys have creation/relation operations, and readback fully preserves adopted children, their relations and external children.

## Route to QA only

Use only when code inspection fully covers every requirement. Materialize a proposal without slices, classify every coverage row as `existing`, cite current evidence and show the tech lead no DEV is needed. Decomposition approval binds this confirmation to hash/revision; later change invalidates publication authority.

Prepare exactly one child titled `[QA] ` followed by the full parent title. Only in this branch is `blocked_by` empty, without fictitious DEV relations. QA verifies the whole Feature/Bug and does not approve the decision.

Prepare, review and approve [test conditions](test-conditions.md) with the DEV-free proposal. Cover all approved behavior and relevant existing capabilities; no slices does not waive conditions; DOCX follows persisted format preference. Preserve current QA description content/structure.

**Complete when:** approved proposal has empty slices, exhaustive `existing` coverage and current evidence; approved verified publication contains QA only.
