---
name: project-slices
description: Prepare, approve, publish, and safely resume vertical DEV and QA child issues for an approved project-flow Feature, Bug, or scope. Use when a tech lead wants an implementation breakdown, sequential scope slicing, native Redmine children and blockers, localized test-condition or Word document revisions, or interrupted publication reconciliation.
---

# Project Slices

Respond in Brazilian Portuguese (pt-BR) from the first announcement, including questions, progress, previews, task descriptions, documents, diagnostics and final delivery. Preserve technical identifiers and Portuguese output headings. Apply this rule to supporting disciplines and delegated evaluations. This workflow is operated and approved exclusively by the tech lead. It turns canonical `project-flow` Features and Bugs into published DEV/QA work, preserves parent execution state and never assigns approval decisions to QA.

## Choose the branch

With an explicit Feature or Bug, follow the individual workflow below. With a scope or no input, read [sequential scope slicing](references/scope-orchestration.md). That branch selects and monitors Features/Bugs but invokes this same individual workflow for each; approvals are never collective.

**Complete when:** input is classified as Feature, Bug or scope and, without input, the tech lead selected from presented eligible scopes.

## Prepare input

Read [input and persistence](references/input-and-persistence.md) before writing artifacts. Require a Feature/Bug directory with canonical `feature.md` or `bug.md`, completed state, valid local approval and `redmine.issue_id`. Validate these local facts and begin inspection even when Redmine is unavailable; then keep snapshots, proposal and previews only in `.work` and explain that remote verification still blocks recording and approval.

Before `record-proposal`, retrieve the parent through Redmine MCP, save only the structured sanitized issue object in temporary storage and run `check-input`. The helper reuses `project-flow` functional verification, including layouts preserving approved bytes while changing only link destinations. Divergence among canonical requirement, state or remote projection stops proposal recording. Once Redmine returns, reuse local inspection/candidate and ask again only about decisions affected by observed divergence.

**Complete when:** local input is inspectable and, before durable state or approval, parent identity, approved hash, Redmine binding and remote alignment were verified without divergence.

## Review requirement changes

When completed publication exists and the current approved requirement differs from its recorded semantic baseline, read [requirement-change review](references/change-review.md) before inspecting or preparing new tasks. Byte differences open comparison; semantic analysis alone distinguishes editorial from functional change. Preserve current publication while review is pending or rejected.

Include current test conditions in impact analysis. Approved editorial change with still-valid conditions preserves current artifacts; functional change follows [conditions after requirement change](references/requirement-condition-revisions.md), linking source, delivery format and application preview to the authorized delta.

**Complete when:** editorial change is recorded without invalidating slicing, or functional change has classification, localized impact and a specific tech lead decision before any mutation preparation.

## Revise test conditions only

When QA has published Markdown/DOCX conditions and the tech lead requests editorial correction, condition addition/removal or Word edits without requirement change, follow [localized condition revision](references/condition-revisions.md). Review structured source, present conditions and selected DOCX for approval, and publish a new version to the same QA with a current-version note and safe resume. New or contradictory behavior returns to requirement resolution before approval; completed QA requires discussing the next action.

**Complete when:** revision is complete with note and any attachment verified, current version identified and original publication, children and earlier versions preserved; or the proposal was rejected without remote mutation.

## Apply the approved revision

When functional change has current localized authorization, read [approved revision application](references/revision-application.md). Reread each task before mutation, preserve completed tasks and prior history, and treat creates, updates, cancellations and relations as resumable operations. In-progress changes and cancellation of unstarted tasks need additional tech lead approval bound to the exact snapshot and mutation.

**Complete when:** readback proves the whole authorized delta, affected managed-child `task.md` files were atomically replaced without changing IDs or slugs, tasks/relations outside it remain intact and the parent retains execution status.

## Inspect code

Read the parent with `children` and follow [existing children and QA-only path](references/existing-children.md) when children exist. For every discovered child, propose adoption or preservation and include all in grouped review; approval of the complete preview decides the set without separate per-child dialogues.

Always inspect the repository and related capabilities before proposing cuts, applying [inspection evidence](../vertical-slicing/references/inspection-evidence.md). Record origins/conclusions in `inspection` and each destination's justification in `coverage.evidence`, as required by the input contract. Include files/symbols only as inspection evidence; technical context in descriptions is optional and depends on an approved decision, not an implementation recipe.

For a parent with design evidence, read its normalized visual sources, applicable screens/states and approved adaptations before invoking `vertical-slicing`. Carry visual criteria through `requirements`, `coverage`, DEV descriptions/references and QA conditions under the existing proposal fields. Inspect shared UI against the design: absent/divergent foundations belong to a separate first visual Feature with its own decomposition; business Features consume it through named external dependencies. A starter shell or a published supplier is not evidence of visual completion. If the catalog/parent hides foundational adaptation inside a business Feature or omits its supplier, use the existing divergence/alignment path before approval. Missing visual acceptance, unavailable comparison sources and unresolved visual/functional differences follow the same path.

**Complete when:** every parent behavior has a classification supported by complete inspection, adaptations/uncertainties are explicit, and no functional gap or divergence remains open.

If inspection or slicing proposes behavior missing from the approved requirement, read [material divergences and parent alignment](references/divergences.md). Show the exact correction and child impact to the tech lead. Rejection preserves requirement/parent and blocks children; approval aligns local canonical requirement first and remote parent afterward, with resumable operation/readback. A consumable API absent from the requirement is always material divergence. After alignment, discard earlier approval authority and redo ordinary proposal/approval on corrected source.

**Complete when:** correction was rejected and affected children remain blocked, or local/remote alignments were verified and a new proposal still awaits ordinary approval.

If technical uncertainty prevents complete vertical slicing, read [exceptional Study and resume](references/studies.md). Study is the only branch allowed to publish a child before the complete proposal and needs specific tech lead approval; its existence keeps this workflow in progress.

**Complete when:** inspection supports a complete proposal or isolates one blocking uncertainty for the Study branch.

## Propose and review

Present verifiable outcome, hours basis and startup/completion dependencies in the preview. Record context, calibration sources, assumptions and attributed corrections in `decisions`. Preserve earlier estimates in history and identify human corrections as such. Use local references supplied by user/project without requiring new configuration or distributing their values as universal defaults.

Prepare test conditions after inspection alongside the proposal: read [test conditions and mandatory DOCX](references/test-conditions.md). Include Feature, Bug and QA-only paths, preserving current QA description. Every new publication generates DOCX, includes `test_document` in the preview and completes only after the QA attachment is observed. Review conditions, coverage and slices jointly with the tech lead.

Invoke `vertical-slicing` with approved requirement and code evidence. Materialize the proposal under [input and persistence](references/input-and-persistence.md), validate through `record-proposal` and render `slices/slices.md`. Present a numbered preview with title, verifiable delivery, independently calculated estimate supported by independent agents when available, blockers and coverage table. For another Feature's capability, read [external dependencies and refinement](references/dependencies.md) before proposing an edge. Ask about granularity, merging, splitting, estimates and blocker edges; record each version without rewriting previous ones.

One DEV child is valid when it entirely fits within six hours. Apply `vertical-slicing` calibration to DEV, QA and Study; no new task may exceed six hours. Larger work must be refined into coherent deliveries before preview without using `estimate_exception` to bypass the limit. Exceptional technical preparation must expose the delivery it enables. API appears in a title only when it is itself an approved consumable Feature delivery.

**Complete when:** granularity, titles, estimates, blockers, coverage and proposed handling of existing children are complete and ready for the single preview decision.

## Approve the complete preview

Complete editorial review using [task descriptions for implementers](../vertical-slicing/references/task-writing.md): explicit expected change/preservation, verifiable scenarios, named relations and text free from administrative comments. Apply to new proposals and revisions while preserving historical states, hashes and approvals.

Before requesting approval, finish the requirement/coverage/test-condition/description reconciliation in `vertical-slicing`; structural helper validation does not establish semantic equivalence. Show complete DEV/QA descriptions, rendered conditions, estimates, derived Redmine fields, attachments, relations and proposed handling of every existing child in one preview. Human-readable content must contain delivery, limits, relevant verifiable success/error/permission criteria, dependencies and traceability. Render technical context only when approved content exists. Use one criteria section; file, code and automated-test planning belongs to later implementation.

Request one decision on the complete preview. Run local approval records with the same tech lead, timestamp and authority hash, then `validate --previous` against previous states. This decision approves decomposition and authorizes only described mutations; publication preparation reuses authorization without equivalent confirmation. Later material change invalidates authority and produces a new complete preview. Conflicts discovered after the decision present only the delta and impact before requesting new authorization.

**Complete when:** authorization references current revision/publication preview, covers conditions, children, relations and attachments, local states validate as `approved`, and no outside mutation was authorized.

## Deliver conditions in the approved format

Deliver conditions in Markdown; generate DOCX only when requested by the user or required by project QA process, under [test conditions and local DOCX](references/test-conditions.md). The approved structured proposal is durable source. Resolve Word edits in that source and obtain new approval before regenerating a changed revision.

**Complete when:** conditions are readable in the preview and format selection is persisted; if DOCX was selected, the approved-source file is available for publication. Earlier artifacts remain preserved.

## Prepare and publish children

If DEV, QA or Study was published by a completed historical v1 state, read [local reconciliation](references/legacy-reconciliation.md). This branch requires sanitized readback and a specific tech lead decision on the exact preview; it creates only local canonical artifacts, preserving Redmine and historical files.

Read [DEV and QA publication](references/publication.md). Derive DEV as `Task` for `Feature` parents or `Bug` for `Bug` parents, QA always as `Deliverable`, initial status always `New` and initial priority always `Normal`; do not ask the tech lead for these fields. Compose one QA per parent and materialize complete descriptions/fields before the single decision. Reuse valid complete-preview authorization before first mutation. Publish through existing Redmine MCP and record each result in the local helper; after uncertain results, read before retrying. Finally reread parent, children and relations, completing only after all approved fields/blockers are verified; then materialize each child by ID at `tasks/<type>-<id>-<slug>/task.md`.

When DOCX is selected, include the exact file in the final preview and follow [attachment publication and resume](references/attachment-publication.md). The same approval authorizes adding it to new or adopted incomplete QA. Verify association before completion; preserve historical exceptions in that reference.

**Complete when:** all children have reconciled IDs, each necessary DEV natively blocks QA, full readback verifies mandatory DOCX for new publications (or historical format contract), Markdown conditions exist in `slices/condicoes-teste-rNNN.md`, original parent execution state is unchanged, and every canonical `task.md` exists without volatile operational fields.

## Configure external dependencies

When approved decomposition contains `external_blockers`, follow [external dependencies and refinement](references/dependencies.md). Configure specific relations when supplier children exist; otherwise use the provisional supplier Feature with approved reason. When children appear, present the exact replacement, add/verify specific blockers and only then remove this workflow's provisional relation.

**Complete when:** every approved external dependency has a verified native relation, the relevant graph stays acyclic and state distinguishes ready routing from implemented capability.

## Boundaries

Each individual execution works on one parent at a time and manages only children adopted or approved for creation by the tech lead. The scope branch only coordinates them in catalog order. Excluded children remain untouched. Divergence handling corrects only the parent needed for current cuts and never silently expands scope. Package scripts manipulate local JSON, Markdown and DOCX only; all remote access occurs exclusively through Redmine MCP and its protected session.
