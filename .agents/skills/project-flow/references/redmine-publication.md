# Redmine projection contract

Before each remote read or write, apply [operation-specific checks](redmine-preflight.md). Creation, publication alignment and relation publication each verify only their own prerequisites. A failed check preserves the canonical document, approved payload and history; retry starts at the incomplete operation after reconciliation, never at intake.

Use one complete requirement/publication preview by default. Its approval covers the requirement and only the operations explicitly included, including planned native relations. Read [the combined preview and binding contract](publication-preview.md) for v5 preparation, authorization and delta handling. Closing, canceling, or another unlisted mutation requires its own concrete authorization.

## Creation preview

Show project, selected open version, proposed classification and tracker, title convention and title, proposed category (or none), initial status, evidence/rationale and the full requirement before the first creation. Ask separately only for material ambiguity. Include the selected version as `fixed_version_id` in creation and in the subsequent previewed update that adds the definitive canonical path; both operations share one consent.

Only when registration before interview was requested, show an initial-objective creation preview and approve that exact payload separately. Its description explains the observable goal/deviation and collection status inside the managed delimiters:

```markdown
<!-- project-flow:start -->
<initial human-readable objective and collection status>
<!-- project-flow:end -->
```

Persist approval before the first call. An early-registration approval covers its exact initial payload and retries; unspecified later requirement content needs the final combined review. A normal combined preview already includes the complete requirement and the listed creation/publication operations, so do not ask again for equivalent authorization.

### Feature Sequencing

New runs use `sequencing_policy: blocks-v1` in canonical scope/requirement state. Create Feature and Bug parents **without Sequencing**: the catalog records their preferred order, and `project-slices` assigns the definitive project/version block after slicing. Resolve the field through project metadata before the creation preview and retain its ID as `sequencing_field_id` in requirement state (null only before resolution). Omit that field from creation custom fields while preserving other required custom fields. If the instance requires a number during creation, stop for configuration alignment; do not invent a provisional value.

The approved slicing/publication preview later includes parent anchor and all child values; no numbering mutation is authorized merely by creating the parent. Preserve the parent's status and other fields. Studies receive their early child position during their own approved publication; the parent remains unnumbered until full slicing. All new child types share the same counter within the project/version.

Sequence numbers are independent per Redmine version. New block allocations account for all trackers and statuses in that project/version; blank parent values do not reserve a range.

For historical runs without `blocks-v1`, read [legacy parent Sequencing](legacy-sequencing.md) only when resuming their already approved creation/retry contract. Do not add/remove the policy or renumber existing issues during resume.

## Generate and verify publication

Reread the issue. Require exactly one ordered delimiter pair. Replace only content inside the delimiters and preserve byte-for-byte content before and after them; absent, nested, duplicated, or reversed delimiters block publication rather than replacing the whole description.

Compare the managed section with the last successfully persisted managed fingerprint. Classify changes outside it as preserved human content. Present changes inside it as requirement divergences with the old, remote, and canonical meanings. `pending` blocks publication. `accepted` first updates and reapproves the canonical document; `rejected` records the attributed decision and restores the approved projection. Never treat a remote edit as canonical merely because it is newer.

The managed section must stand alone for a reader without the interview or local artifact access. Prepare it through the combined preview helper, which uses the same projection as `scripts/render_publication.py`; use the latter to check the approved result. Preserve the section order and functional wording, including every story, flow, exception, rule, observable datum, acceptance/correction criterion, dependency and scope boundary. Preserve existing rule and criterion identifiers and references; one criterion in the canonical document remains one criterion in Redmine. The issue subject carries the canonical title, so the description does not repeat its H1 or local Issue/version metadata.

For Features, only the `Designs e evidências` provenance section stays local. Any condition needed to implement or accept the delivery must already appear in the functional sections before canonical approval; a local evidence pointer cannot substitute for it. For Bugs, retain evidence and reproduction limitations because they define the deviation. Append the repository-relative canonical path and approval attribution. Interview history and operational state remain local.

Use the storage and retention policy in [the artifact contract](artifact-contract.md): unapproved output belongs in `.work/`; exact evidence required by an approved operation belongs in its `.flow/publications/<operation-uuid>/` directory before approval. Use a sanitized fresh issue snapshot with `subject`, `description`, status and relations, either at the JSON root or inside `issue`. Identity may be `id` or `issue_id`; all identity fields present must agree. From the repository root:

```sh
python <project-flow-skill>/scripts/render_publication.py <feature-or-bug-state.json> --before <issue-before.json> --output <publish-preview.md> --payload <publish-payload.json>
python <project-flow-skill>/scripts/render_publication.py <feature-or-bug-state.json> --before <issue-before.json> --check <issue-after.json>
```

Normal rendering/checking requires a valid canonical approval matching the document bytes and the same issue identity/title. For a legacy run's unapproved combined review, add `--draft --reviewer <name>`; this prepares the full preview without prior canonical approval and cannot be used with `--check`. This projection-only checker emits `issue_id` and `changes.description`; the normal combined publication plan adds the selected `changes.fixed_version_id`. Its printed SHA-256 covers the exact UTF-8 payload file. The checker compares all functional sections, permits CRLF/LF differences and equivalent canonical-reference footer wording, and separately verifies unmanaged content, status and relations. Review semantic completeness before approval; this check proves faithful publication, not requirement quality.

Present the generated content in the complete preview before approval. After the authorized write, persist the operation outcome first, then reread and run the checker alongside fingerprint reconciliation. A mismatched projection remains incomplete until reconciled. A state validator passing alone does not establish publication completeness.

Show the complete resulting description, preserved human content, resolved divergences and listed relation keys in the combined preview. The `redmine_update_issue` payload contains the issue identifier plus `changes.description` and the selected `changes.fixed_version_id`; omit `status_id`, including the current or initial status. Local approval/completion does not authorize a remote status transition. Bind the reviewed operation to the persisted issue ID and fresh unchanged managed baseline without a second equivalent confirmation; preserve the outside human text. Once bound, retries reuse the exact payload and its recorded fingerprint. Do not publish round-by-round comments.

Keep legacy `approved_status_id`, `approved_status_name`, and `approved-status` mapping confirmations as historical data only. They never supply a publication field or authorize a transition. On resume, inspect any approved publication payload before retrying; if it contains a status field or its original fields cannot be established, pause publication and report that the recorded operation needs recovery. Preserve its fingerprint and history: v2-v4 retain immutable approved payloads, while v5 allows only the explicitly reviewed, append-only delta described in the preview contract. Reconcile unknown outcomes before resolving recovery. A completed publication is not repeated or automatically reversed. Any user-requested status change, including repair of an earlier unintended change, is a separate action with its own exact transition preview and explicit approval.

For a scope dependency, use the native `blocks` relation from prerequisite to dependent. Include its stable catalog-item key and endpoint binding in the complete item preview. Once both IDs exist, resolve only the shown binding, persist the operation fingerprint and existing consent, then call `redmine_create_relation` and reconcile. Unlisted relations require a new preview. A catalog split or merge preserves existing relations and issues until an approved remote mutation changes them.

## Reconciliation loop

Before any remote call, verify the item lock, validate state, and persist the approved operation with its payload fingerprint. After the call, persist its outcome before starting another operation. On resume, reread issue plus relations and compare them with local fingerprints in operation order: create, publish, then stable-sorted relations. Continue from the first incomplete operation only.

A known failure records a new attempt with a stable error code and sanitized human message; it retains no credentials, headers, request bodies, session paths, raw response bodies, or raw exceptions. An unknown outcome always triggers a read comparison. Remote match completes locally without a repeated mutation; proven absence allows the unchanged operation to retry; divergence or ambiguity stops with safe choices and no mutation.

## Aligning an already completed publication

When the user requests publication standardization for an issue created by this flow, retain its completed state, approvals, operations and scope closure as history. Acquire the same item lock and create `.flow/publications/<uuid>/publication-alignment-<uuid>.json` for each new alignment, retaining its baseline, preview, payload and readback in that same operation directory. All file references are relative to the item root (for example `.flow/feature-state.json`, `feature.md`, and `.flow/publications/<uuid>/baseline.json`); a legacy canonical state may remain at `feature-state.json`. Use schema v2 from `schemas/publication-alignment.schema.json`; never reuse an alignment file for a later canonical or remote baseline.

The record keeps issue identity; completed canonical state, document hash and approval; lock acquisition/release; sanitized fresh baseline with status and relations; exact preview and payload paths/hashes; payload approval; append-only attempts and observations; and verified readback. Its append-only status history is `pending → approved → unknown|completed`, with `unknown → completed` after reconciliation. Validate every candidate against its predecessor during operation. Place the candidate at `.work/publications/<uuid>/publication-alignment-<uuid>.json`, so its filename retains the alignment identity and its references resolve from the same item root. On success replace the current record atomically and remove the candidate:

```sh
python <project-flow-skill>/scripts/validate_publication_alignment.py <candidate.json> --previous <publication-alignment-uuid.json>
```

Obtain approval for the concrete generated payload before the first mutation. An unknown outcome is reconciled by readback; retry only after the remote absence of that exact payload is proven, and reuse its unchanged fingerprint. `completed` requires the approved payload to match the readback, every functional section to pass, unmanaged content/status/relations to remain unchanged, and the lock release to be recorded after verified completion. A completed record is immutable.

Legacy `publication-alignment.json` schema v1 records remain valid in read-only mode. Never append transitions to them; a later alignment gets a new UUID-named v2 record. A canonical content change is not an alignment: it requires its own requirement review and approval before a new alignment begins. Historical closure records and unrelated demands remain intact.

## Abandonment after creation

Offer four explicit outcomes: keep the issue in collection and keep local state; request a preview to set an available canceled state; request a preview to update only the managed description; or abandon only local state while leaving Redmine unchanged. Explain the retained artifacts and resumability of each. Closing, canceling, updating, or releasing state in a way that prevents resume occurs only after the user selects the exact effect and approves its payload; otherwise the remote issue remains open and unchanged.

**Complete when:** each mutation matches an approved fingerprint, every completed operation was persisted before the next began, relations are unique by stable key, divergences are resolved, no unmanaged content was changed, the selected version is applied, and the publication payload contains no status field.
