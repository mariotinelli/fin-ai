# New scope: complete an approved catalog

Use this path after explicit selection of `new-scope`; local catalog preparation does not require Redmine. Read [catalog discipline](catalog-discipline.md) before delimiting the catalog. Orchestration stays here; each item uses the reusable discipline in `new-issue.md` and its Feature or Bug branch.

## 1. Normalize and orient once

Follow `intake.md` for every declared source and `design-inputs.md` for design evidence. Create `docs/harness/scopes/<YYYY-MM-DD>-<scope-slug>/`, using deterministic suffixes `-02`, `-03`, and so on for collisions, and acquire a scope lock before its first write. Inspect the repository once and retain the result in scope state.

After verifying the project, list every open Redmine version and ask which version owns this scope. Record its ID, name, open status and selection attribution in scope state before catalog approval. Before item creation, also record that version's observed maximum `Sequencing` as `sequencing_baseline`. The selection and baseline apply to every catalog item and are inherited unchanged by each requirement state; starting another item does not ask or recalculate against earlier items from the same scope. A different version requires an explicit scope-level change before any affected remote operation.

Allocate each normalized source once. A source supporting two or more items is `scope-shared`, stays under the scope, and is referenced from item states by a relative path. For a new catalog, place an `item-exclusive` source at `items/<stable-item-id>/sources/<source>.md` under the scope and retain that approved allocation through interview and issue creation; the requirement references it relatively. This gives evidence a durable owner before a remote ID exists, without copying files or changing the approved catalog hash. Existing allocations keep their paths. If discovery yields one item, preserve the scope artifacts and continue directly without restarting context selection, intake, normalization, orientation, or conversation.

**Complete when:** every retained source is readable, normalized once, and has exactly one ownership/path allocation; repository orientation is recorded without secrets; the scope owns its lock; and every observed candidate is represented.

## 2. Build and approve the complete catalog

Account for every observable objective or deviation with a stable candidate record. Mark unresolved classification or allocation as `undecided`; it blocks catalog approval and item work. Each catalog item records its candidate IDs, stable ID, Feature/Bug type, name, complete human objective, actors, observable result or deviation, evidence, direct functional dependencies, separate-acceptance rationale, lifecycle, status, and deterministic position.

Apply a **catalog-first gate** after repository orientation. Turn the evidence into candidate vertical items before starting an item's proportional functional interview. When a catalog field cannot be determined, ask only the smallest product question whose answer can change candidate inclusion, Feature/Bug classification, item boundary, direct dependency, source allocation, or processing order. Then recompute and present the catalog. Preserve every other behavioral uncertainty as input for the future owning item; it does not trigger `requirements-grilling`, a numbered item interview, or a decision ledger in `scope.md` during `repository-analyzed`, `catalog-proposed`, or `catalog-approved`.

Apply the capability cohesion, title convention, behavioral coverage and delivery-dependency criteria in the shared discipline. Build `input_inventory`, `behaviors`, `title_convention`, item `delivery`, `dependency_reasons` and `order_reasons` in scope v3. Keep candidate and physical source allocation records separate from behavior responsibility. Scope-only contextual/excluded sources use `scope-context` with no item IDs.

Generate the complete catalog/coverage block and approval preview with `render_catalog.py`. Reconcile the preview against every normalized source before seeking approval; the validator cannot discover behavior omitted from both the evidence inventory and catalog. Use the resulting hash for the attributed approval, then rerun validation before creating any issue.

**Complete when:** every relevant reference is resolved; every behavior has a verifiable destination; every active item has a cohesive boundary and confirmed title; the graph and order are justified and valid; the full generated projection is approved; and no item-level functional interview has started.

## 3. Process the next eligible item

Before starting remote item work, resolve context through [operation-specific checks](redmine-preflight.md), reusing prior selections and the same scope state. Select the first eligible active item in the approved preferred order: it is incomplete, has no unresolved own impediment, and its direct dependencies are completed without open gaps. Earlier blocked items do not prevent independent work. Record the missing decision or capability and its resolution condition in the owning item's `functional_gaps`; identify dependent items through the approved graph. Existing runs retain their schema. For an explicit legacy review, follow the enrichment and preservation contract in `artifact-contract.md` before resuming.

Initialize requirement state v5 in `docs/harness/.runs/<run-id>/` with `mode: new-scope`, `creation_timing: after-requirement`, `early_creation_request: null`, `scope_item` (relative `state_path`, `catalog_item_id`, approved `catalog_sha256`), and relative evidence links. Copy the confirmed `title_convention` and item `delivery` exactly; inherit classification, audiences and boundaries without repeating catalog questions. Record the selected item's run ID and staging location in scope history. Set its progress to `in-progress` or `blocked` as appropriate, retaining `issue_id`, `artifact_path` and `state_path` as null until creation establishes the definitive paths. Execute the shared `new-issue.md` interview and complete preview before creating anything. Populate the definitive progress paths and ID only after creation is durable; keep existing assigned paths immutable.

Before the first item-level question, present an **item context handoff** from the approved catalog. Identify the selected Feature or Bug by name and position, then summarize its complete human objective, actors, observable result or deviation, included delivery, explicit boundaries, evidence, and direct dependencies. State material uncertainties that the interview will resolve. This is orientation, not another catalog approval. Do it even when the catalog contains exactly one item; a single-item scope does not make its name or context implicit.

The **item-interview gate** opens only when `catalog-approved` is in the scope's completed phase prefix, the next eligible item is selected, its staging requirement state, lock and evidence references are durable, and the item context handoff has been shown. An issue ID is not a prerequisite. Invoke `requirements-grilling` for that item only after the handoff. If the user requests early creation, record that request and use the shared exception; retain legacy state order on resume.

Execute the complete shared Feature/Bug cycle. If an unresolved gap or unavailable capability prevents progress, record it in both histories, mark the item `blocked`, and suspend that item's work with an objective resolution condition. Continue independent eligible items; retain dependent items as pending or blocked with the missing dependency identified. Complete the item only when its requirement state validates at `completed`, its Redmine projection and operations reconcile, and every gap is resolved.

When the recorded condition is satisfied, resolve the gap with its evidence and return the blocked item to `pending` (or `in-progress` when resuming its saved work). Apply the same update to dependent items whose prerequisites are now complete. Validate before selecting the next eligible item; resume its saved requirement phase rather than reinitializing it.

Include the selected item's addressable native `blocks` relations in its combined preview, using the explicit returned-ID binding for this item when needed. Once both IDs exist, bind the already approved endpoints and publish/reconcile without another equivalent confirmation. A relation absent from the approved preview needs its own authorization. Never duplicate an equivalent relation.

**Complete when:** the selected item is completed and validated with durable issue/artifact links and reconciled addressable relations, or its impediment and resolution condition are durable and the next independent eligible item is identified.

## 4. Continue within the authorized scope

The request to process the scope authorizes advancement between its items. After each completion or impediment, show completed items, pending items, missing decisions/capabilities and the next eligible item, then return to step 3 without asking for continue/stop. Product decisions and publication approvals remain required when their actual content is ready; reuse valid approvals for unchanged payloads.

Honor a user pause immediately, including during an item: finish only an atomic local write, start no further operation, and append a `voluntary-stop` pause preserving catalog, progress, issues, relations, approvals, sources and histories. Resume validates states, marks the pause resumed, reconciles uncertain outcomes before any retry, and selects the next eligible item in preferred order. Retain legacy `continuation_decisions` as history; new per-item decisions are unnecessary. A resumed legacy stop needs no replacement continue/finish decision.

If no item is eligible while work remains, report the scope as incomplete with completed items, pending items, their resolution conditions and next steps. Retain item impediments without inventing a user pause or declaring completion.

**Complete when:** progress is durable and the next eligible item is selected, all work is ready for final reconciliation, or a user pause/no-eligible-item report explains exactly what remains and how to resume.

## 5. Reconcile and close the scope

After all active items complete, reread every issue and relation. Reconcile unknown outcomes and divergences in operation order. Validate every separate requirement state and the scope state, and run the [functional publication check](redmine-publication.md) for every issue against its approved canonical document. Surface incomplete or summarized projections even when their historical publication fingerprints match. Build the final `scope.md` summary listing all issues, native relations, canonical artifacts, approvals, validations, and one actionable next recommendation. Present its exact projection and persist one attributed scope-completion approval.

The scope may reach `completed` only when every active item is completed, every retained/retired item preserves any existing issue and artifacts, every relation is published and reconciled, every required approval is valid, every validation passes, all candidates are decided, and no functional gap is open.

**Complete when:** `validate_scope_state.py` accepts phase `completed`, the final summary contains all six required sections, and no item, relation, approval, reconciliation, candidate, gap, or validation remains incomplete.

## Catalog revision

New evidence that changes names, audiences, deliveries, coverage, conventions, or divides, combines, adds, removes, retypes, reorders, or changes dependencies pauses the scope before mutation. Show its effect on names, audiences, deliveries, coverage, candidate mapping, source ownership, graph, order, issues, relations, and artifacts. Invalidate the prior catalog approval, append an approved `catalog_changes` record, retain retired entries and every created issue/artifact, update the active catalog, and obtain approval of the complete revised projection. Only unstarted, unpublished items and relations may retire locally; a split or merge never closes, deletes, reuses, retires, or rewrites an existing issue automatically. Any later remote disposition is a separate previewed decision.

**Complete when:** history is append-only, every prior issue ID remains in item progress, the revised active graph/order/source allocation validate, and exactly one approval covers the current complete catalog.
