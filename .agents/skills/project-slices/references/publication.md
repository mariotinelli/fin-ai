# DEV and QA publication

After completed publication with Markdown/DOCX conditions, condition-only changes follow [localized revision](condition-revisions.md), preserving original publication state/canonical artifacts.

Build this phase's plan while current decomposition is under review so all effects appear in one preview. After the single decision, persist decomposition approval, generate the document and run `prepare`; persisted rendering must be materially identical to the presented set. The local helper stores intent/evidence; the agent reads/mutates exclusively through Redmine MCP tools.

## Confirm fields

With existing children, first complete [existing-child and QA-only review](existing-children.md). `prepare` rejects nonempty child lists without complete dispositions.

Reread parent with children/relations and consult project, trackers, statuses and priorities. Derive without asking: QA always uses native `Deliverable`; DEV uses `Task` for `Feature` parents and `Bug` for `Bug` parents; initial status is `New`; initial priority is `Normal`. Resolve native catalog IDs by name and stop if absent/ambiguous. Use parent's native `project_id`/`parent_issue_id`; inherit `category_id`/`fixed_version_id` when present. Leave assignee/start/due dates empty. Explicitly send Normal's `priority_id` without override. Write estimate to `estimated_hours`.

Save sanitized parent response to `.work/slices-publication-parent.json` and build `.work/slices-publication-plan.json`:

```json
{
  "source": {"slices_state_path": "<caminho absoluto>", "slices_state_sha256": "<sha256>"},
  "parent_snapshot": "<caminho absoluto>",
  "metadata_snapshot": "<caminho absoluto com trackers, statuses e priorities>",
  "native_fields": {
    "project_id": 7,
    "dev_tracker_id": 2,
    "qa_tracker_id": 7,
    "initial_status_id": 1,
    "default_priority_id": 4,
    "priority_override_id": null,
    "priority_override_reason": null
  },
  "qa": {
    "title": "[QA] <título completo do item pai>",
    "estimate_hours": 9,
    "blocked_by": ["dev-1"],
    "description": {
      "objective": "...",
      "integrated_journeys": ["..."],
      "rules_permissions": ["..."],
      "related_impacts": ["..."],
      "completion_criteria": ["..."],
      "requirement_references": ["R1"]
    }
  }
}
```

There is exactly one QA per parent, titled `[QA]` plus full Feature/Bug title without suffix. Its estimate is independent rather than using DEV's six-hour reference. Description covers objective, integrated journeys, rules/permissions, related impacts and completion criteria, referencing requirements without copying all DEV descriptions. `blocked_by` contains all and only DEV tasks needed for integrated verification; it is empty only for approved empty slices and exhaustive `existing` coverage.

QA verifies the complete parent, including `existing` behavior. Translate those scenarios into verifiable journeys/criteria preserving approved conditions; this classification waives DEV work, not integrated verification.

Write a short `objective`. Separate `integrated_journeys` by behavior with each scenario's preparation: profiles, data, devices and session/time conditions. Use `rules_permissions` for relevant restrictions and `related_impacts` for related behavior to preserve without repeating journeys. In `completion_criteria`, explain required outcomes/evidence and obstacle recording. Keep estimates in their own field and administrative decisions in workflow state. All user-facing prose stays Portuguese.

For example, rather than one item for the whole Lembrar-me cycle, describe return in the same browser within 30 days separately from return after expiry without a valid session, including that intermediate visits do not extend remembered access. Preserve other approved scenarios, including logout/deactivation; this example does not replace full coverage.

**Complete when:** parent identity, derived trackers, initial status/priority, inheritance, estimates and QA blockers are explicit in sanitized plan, QA also covers existing behavior and no credentials were persisted.

## Complete preview and single authorization

For new publications, `prepare` preserves readable conditions in `slices/condicoes-teste-rNNN.md` and includes content/format in preview and `publication_sha256`. Give this path to the tech lead with children, including QA-only paths. If DOCX is selected, generate it first: `prepare` verifies bytes and includes file/hash/QA destination in preview. Follow [attachment publication/resume](attachment-publication.md). Markdown involves no upload/association; completion requires preserved conditions and ordinary readbacks.

Child titles belong in Redmine `subject`. Description starts directly at Portuguese `Entrega` for DEV, `Objetivo` for QA or `Pergunta técnica` for Study without repeating title. Identify each child outside its body in grouped previews.

Apply [editorial review](../../vertical-slicing/references/task-writing.md) to QA too, preserving journeys/completion conditions. DEV uses “Critérios de aceite”; QA uses “Critérios de conclusão”. Render DEV criteria without internal classification labels. References identify parent/covered requirements. New rendering does not rewrite stored descriptions/hashes from earlier publications; approved-content changes need a new revision/approval.

Run:

```sh
python <project-slices>/scripts/manage_publication.py prepare .flow/slices-publication.json .work/slices-publication-plan.json --slices-state .flow/slices-state.json --preview slices/publication.md --actor "<tech lead>" --at "<ISO-8601>" --reason "<motivo>"
```

The helper derives DEV children from approved revision. DEV title is `[DEV]` plus full parent title and approved suffix; external API delivery may contain `[API]` after `[WEB]`. The combined `slices/publication.md` preview shows full content, fields and hashes; `dev-N`/`qa` keys remain internal to preparation/resume state.

Before the decision, present rendered proposal, complete publication plan and conditions together. After explicit decision, record decomposition approval, generate selected DOCX, run `prepare` and check `slices/publication.md` introduces no material difference from the approved set. Record the same authority in publication state with identical actor/time; the second record persists an existing decision rather than asking again. Material differences stop the sequence and require a new complete preview. Preserve previous copies for `validate --previous`:

```sh
python <project-slices>/scripts/manage_publication.py approve .flow/slices-publication.json --actor "<tech lead>" --at "<ISO-8601>"
python <project-slices>/scripts/manage_publication.py validate .flow/slices-publication.json --previous <estado-anterior.json>
```

**Complete when:** one valid decision references decomposition revision/current `publication_sha256` and no remote mutation began beforehand.

## Publish and resume

Adopted children retain approved ID/baseline and never enter `begin-create`; only `create` origins reach creation MCP.

For every new child without completed `create:*`, run `begin-create` before MCP. It persists `in-flight` intent and returns exact `attributes`; send to `redmine_create_issue`. Then `finish-create` records `completed`, `failed` or `unknown`. Interruption between start/result makes `in-flight` uncertain. Persist sanitized errors.

```sh
python <project-slices>/scripts/manage_publication.py begin-create .flow/slices-publication.json --key dev-1 --at "<ISO-8601>"
python <project-slices>/scripts/manage_publication.py finish-create .flow/slices-publication.json --key dev-1 --attempt 1 --outcome completed --issue-id 501 --at "<ISO-8601>"
```

`unknown`/`in-flight` requires searching stable `project-slices-child` identity under confirmed project/parent across open/closed issues. Traverse every page and save project, parent, identity, `all` scope, each page's `offset`/`limit`/`count`, total/candidates in sanitized snapshot. Use `observe-create --outcome matched` only for one fully identical candidate; `absent` only after complete identity search finds none. Ambiguity/divergence stops for tech lead resolution. Completed operations never return to creation MCP.

Once necessary IDs exist, preserve decomposition DEV blockers: dependency is `issue_id`, dependent is `issue_to_id`, `relation_type` is `blocks`. For relations between new children, run `begin-relation` before MCP and `finish-relation` afterward; uncertainty requires reading relations and `observe-relation` before retry. A relation touching an adopted child never generates payload: both endpoints must be adopted and equivalent relation present in approved snapshot/final readback.

Partial failures preserve confirmed IDs/relations. On resume validate state, reconcile each unknown first, then continue pending operations only.

**Complete when:** each new-child `create:*`/`relation:*` is completed once through reconciliation, adopted relations have full evidence without mutation, and attempts/observations remain append-only.

## Verify and complete

Before `complete`, finish upload, association and verification of [the approved document](attachment-publication.md). Include QA `attachments` in reads. MCP acceptance does not confirm association; document-contract publication needs positive observation/final readback presence. No extra condition/reference is inserted into QA description or `task.md`.

Include all managed children and discovered children kept external in readback. The helper compares adopted baselines, new-child plan and external contractual fingerprints without hashing volatile fields such as journals/attachments.

Read parent/all children with relations. Save `.work/slices-publication-readback.json` as `{"parent": {...}, "children": [...]}` and run `complete`. It compares project, parent, tracker, initial status, effective priority, category, version, assignee, dates, estimate, title, description and every `blocks` relation. Parent status ID/name must match baseline.

```sh
python <project-slices>/scripts/manage_publication.py complete .flow/slices-publication.json --readback .work/slices-publication-readback.json --at "<ISO-8601>"
```

After fully verifying IDs, content, tracker, estimate, parent/relations, the helper atomically writes completed state and a stable human-readable representation per child: `tasks/dev-<id>-<slug>/task.md` or `tasks/qa-<id>-<slug>/task.md`. It contains only identity, type, tracker, parent, estimate, description and relations; operational status, assignee and dates stay in Redmine. First materialization fixes the slug; later reads reuse type/ID directory. Historical `slices/descriptions/` remains valid, but new publications neither create nor persist positional artifacts.

Preserve the parent Feature/Bug. QA is a verification child, not an approver of decomposition, content or completion.

**Complete when:** `slices-publication.json` is `completed`, includes readback/all `task.md` hashes and full revision, approval, ID, attempt, observation and progress history. Earlier failure/uncertainty retains resumable state only, without a definitive canonical tree.

If approved decomposition has `external_blockers`, continue with [external dependencies/refinement](dependencies.md). This adds/refines relations without modifying completed publication or recreating children.
