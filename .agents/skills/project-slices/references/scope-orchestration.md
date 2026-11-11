# Sequential scope slicing

For block-policy scopes, allocate definitive Sequencing in the approved catalog order as each item's complete slicing is published. Parents merely published by `project-flow` are still unnumbered. A Study keeps its item incomplete; later items cannot consume its pending block. Read [version block Sequencing](sequencing.md) for snapshots, serialized allocation and collision handling.

Use when the tech lead requests a scope or provides no Feature/Bug. Coordinate multiple main-workflow executions; each item keeps its own inspection, complete-preview approval, publication and readback.

## Select

Without input, run `manage_scope.py list <docs/harness>` and present only scopes with at least one active approved Feature/Bug still pending/in progress. In Portuguese, also show `fatiadas/total` and counts for `pendente`, `em andamento`, `concluída`, `aguardando requisitos`, then ask which scope to process. Total includes every active catalog Feature/Bug, excluding removed entries.

The helper validates actual `project-flow` state, full catalog-projection approval and order. Missing artifact/completed requirement means `aguardando requisitos`; the item remains in total and does not block other eligible items. Unsafe paths, stale catalog binding, type, delivery or Redmine-ID mismatch are errors, not waiting.

**Complete when:** tech lead chose an approved-catalog-derived option and saw the full active Feature/Bug distribution.

## Start or resume

For a new selection:

```sh
python <project-slices>/scripts/manage_scope.py start <scope-dir> --actor "<tech lead>" --at "<ISO-8601>"
```

State is `<scope-dir>/.flow/slices-scope-state.json`, separate from `project-flow` requirement/execution progress. It binds `internal_identity`, project and approved catalog-projection hash rather than mutable `scope-state.json` bytes.

For paused state run `resume`; active state uses `refresh`. Resume `current_item_id`, never a conversational flag. Prior completion counts only when `slices-publication.json` passes RST13 validation, has current final approval, completed creates/relations and readback evidence. Resume then skips published items without repeated gates/operations.

**Complete when:** durable state points to the first unprocessed eligible item in approved order or explicitly shows only waiting requirements remain.

## Process a Feature or Bug

Run this skill's complete parent-item branch for `current_item_id`. Catalog dependencies explain order but do not block slicing. Implementation blockers belong to children and likewise do not stop subsequent-item processing.

Each item independently retains:

1. approved/published requirement verification;
2. one tech lead decision on complete decomposition/publication preview;
3. reuse of that decision while authorized content stays valid;
4. reconciled creation/relations;
5. full child/blocker readback.

Do not aggregate approvals/publications across items.

**Complete when:** individual publication is completed with validated readback, or the item remains explicitly pending/in progress without claiming completion.

## Show progress and continue

Reuse [condition-format preference](test-conditions.md) across items. Pass the same preference file to `record-proposal`; resume preserves already approved format without asking about Word again.

Scope processing authorizes advancing between eligible items. After completion run `refresh`, show completed/pending items, obstacles and next step, then process `current_item_id` without another continue/stop question. `refresh` also clears legacy `awaiting_decision_for` waits while preserving `continuation_decisions` history without requiring new records. Product decisions and publication-preview approval remain necessary; valid authorizations are not renewed on resume.

When a necessary decision/capability is missing, record the obstacle and concrete resolution condition:

```sh
python <project-slices>/scripts/manage_scope.py block <scope-dir> --item <catalog-item-id> --reason "<decisão/capacidade ausente e condição de retomada>" --actor "<responsável>" --at "<ISO-8601>"
```

The helper selects the next independent item in preferred order. Also record items whose slicing genuinely depends on the missing decision; child implementation dependencies alone do not prevent slicing preparation/publication. Show unresolved blocking events with progress. After verifying resolution, use `unblock` with equivalent arguments and evidence in `--reason`, then `refresh` to revalidate artifacts before acting.

Honor pause requests immediately, including mid-item. Finish only an ongoing atomic local write, then run without new remote operations:

```sh
python <project-slices>/scripts/manage_scope.py pause <scope-dir> --reason "<pedido do usuário>" --actor "<tech lead>" --at "<ISO-8601>"
```

`pause` saves progress without remote access. `refresh` preserves pause; `resume <scope-dir> --actor "<tech lead>" --at "<ISO-8601>"` records resume/recalculates next eligible item. Reconcile uncertain outcomes through the individual workflow before retry; retain completed operations, human-readable content and valid approvals.

**Complete when:** progress is persisted and next step matches validated state, or pause is recorded with no new operation started.

## Complete

Automatic completion occurs only when `fatiadas == total`. An active Feature/Bug awaiting requirements keeps scope incomplete even without another eligible item. Report waiting without marking missing requirements as removed. Also show `dependency_status`: external relations may be pending, refining or ready without undoing completed publication or claiming implemented blocker capabilities.

**Complete when:** all active Features/Bugs have complete verified individual DEV/QA routing; otherwise report incomplete scope, completed/pending items, missing decision/capability and next steps. Preserve exact progress and observable waiting reason.
