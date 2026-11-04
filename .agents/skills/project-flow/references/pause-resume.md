# Pause and resume

Use this branch for local recovery even when Redmine is unavailable. Check remote prerequisites only before the next remote operation. It covers a deferred product decision, a question for a third party, a voluntary stop, an incomplete run, an item-lock conflict, an open functional gap, or a `new-scope` catalog change.

## Own the item

Build one item key that is stable for the whole run: use the definitive repository-relative folder when it already exists; otherwise use the confirmed project plus normalized intended item identity, or the intended repository-relative staging/scope folder when the project is unresolved, and retain that key after issue creation. Run `python <project-flow-skill>/scripts/manage_lock.py acquire <docs/harness/.locks> <item-key> <run-id>`, then copy its returned `lock_id`, item key, relative lock path, and acquisition time into state before writing other artifacts. Run `manage_lock.py verify` with that run and lock ID before every state replacement or remote call so a recovered lock fences a straggler.

An existing lock is a recoverable conflict, not permission to continue. Report its run ID, lock ID, and acquisition time. Recover only after the user confirms that exact owner is abandoned: run `manage_lock.py recover` with the existing lock ID and a non-empty reason. The compare-and-replace operation refuses a changed owner. Runs with different item keys use different lock files and remain independent. Release requires the current lock ID and happens after the final durable write on completion or a normal pause. A normal pause preserves all artifacts and remote operation records; it does not abandon the work.

**Complete when:** this execution holds the exact lock recorded in state, or it has stopped without changing the competing run.

## Pause

Finish the current atomic local write, but start no remote mutation or later phase. Append one pause record with status `paused`, kind `decision-deferred`, `third-party-question`, or `voluntary-stop`, the prior phase, explicit reason, objective resume condition, first incomplete `resume_phase`, and timestamp. Set top-level `phase` to `paused` and validate the candidate against the prior state. Persist it atomically, then release the owned lock. Do not release before persistence succeeds. A crash between persistence and release remains an ambiguous lock conflict, handled by the recovery branch above.

For a material deferred decision, third-party question, or functional gap in the delivery, append a stable record with its owner, reason, blocked decisions or items, question or description, and time. Mirror questions in `history/pending-questions.md` (the existing root file for a legacy run). Continue independent questions in small prioritized rounds, recording those decisions normally; approval, publication and downstream work that depend on the missing answer remain blocked. Within an authorized scope, suspend the affected item and continue independent eligible items under `new-scope.md`. Explicit scope boundaries are recorded as decisions; settling a pending question through an approved exclusion preserves its history and adds an attributed resolution under the shared interview contract.

**Complete when:** persisted state and human history agree on why work stopped, what exact observation permits resume, and which phase remains incomplete; no blocked phase or remote operation ran.

## Resume

Read existing local state, source inventory, drafts and history without a remote preflight. Reuse prior context selections and answers. Validate the current state and verify the latest pause's objective condition. After a normal pause, acquire with `--previous-lock-id <state-lock-id>`; this creates a new lock only if none exists, without an abandonment confirmation. If a lock still exists, use the conflict recovery branch above; never infer abandonment from age or a paused state alone. Record the returned replacement lock and recovery reason in state. Mark that pause `resumed` with time and concrete evidence, restore `phase` to its recorded `resume_phase`, and validate the candidate with `--previous`.

Resolve a deferred question by retaining the original fields and adding status `resolved`, answer, answer source, and resolution time. Preserve the corresponding human entry. Never delete or rewrite prior questions, decisions, approvals, completed phases, issue identity, or completed remote operations. A decision may become `reopened` and an approval may become `invalidated` only with attributed reason and time; otherwise it remains valid.

After resuming a `voluntary-stop`, retain any original `stop` decision as history. The resumed pause is sufficient to continue within the existing scope authorization; no per-item `continue` or `finish` decision is required. Preserve any such decisions already recorded by legacy runs.

Before resuming remote work, verify the required capabilities, connection, identity and destination. Reread the issue and any planned relations, compare their fingerprints with local operations, and reconcile every `unknown` outcome before continuing. Preserve completed operations and append reconciliation observations; a remote match completes locally, proven absence permits retry of the unchanged approved payload, and divergence blocks for an attributed decision. Use the state and evidence locations from the [artifact contract](artifact-contract.md); `.work/` candidates are never authoritative resume states. Then continue from the first incomplete remote operation inside the first phase absent from `completed_phases`. For a scope, select the next eligible active item in the approved preferred order using `new-scope.md`; an item impediment suspends only that item and its real dependents; completed items, issue IDs, catalog history, and relations remain intact. Do not repeat a completed phase, operation, or equivalent relation. When state validation identifies unknown schema, invalid content, impossible transition, unresolved divergence, or a lock owned elsewhere, stop with its sanitized diagnostic and corrective action instead of repairing silently.

**Complete when:** the pause is durably marked resumed, all still-valid history is unchanged, the item lock is owned, and execution is positioned at exactly the first incomplete phase.

## Pause a catalog change

In `new-scope`, a proposed division, union, addition, removal, retyping, dependency change, or reorder is a `catalog-change` pause. Record the affected item IDs and show the impact on evidence ownership, graph edges, parallel-ready groups, total order, issues already created, and artifact paths. Invalidate the current catalog approval before modifying catalog data, then require approval of the complete revised catalog and order. Preserve all created issues and item histories. Append the approved split, merge, or other change with affected items, source ownership, graph/order impact, preserved issue IDs, and artifact paths; retired entries remain addressable instead of disappearing.

When a catalog change appears during any item interview, pause both scope and item states with the same reason and objective resume condition. Resume the item only after the revised complete catalog has a valid approval and the current item's identity remains valid.

**Complete when:** no remote mutation occurs during the pause, both states agree when an item has started, and exactly one valid approval covers the current complete catalog and order.
