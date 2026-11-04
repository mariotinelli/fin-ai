# New issue: shared Feature and Bug cycle

Use this path after selecting or recovering the local run in `SKILL.md`. New runs use requirement state v5 and prepare the complete requirement before remote creation by default. Intake, interview and an unapproved draft can proceed while Redmine is unavailable. Read [catalog discipline](catalog-discipline.md) for capability boundaries, evidence reconciliation and title conventions.

## 1. Normalize and orient

Follow `intake.md` to inventory, fully extract, and separately normalize every declared source. For design evidence, apply `design-inputs.md`. Acquire the run's item lock before its first write and read [pause and resume](pause-resume.md). Inspect repository facts and vocabulary, excluding dependencies, generated output and secret-bearing files. Normalize evidence once and preserve prior answers.

For a fresh run, set `creation_timing: after-requirement` and `early_creation_request: null`. Use `docs/harness/.runs/<run-id>/` until an issue ID is durable. If the user explicitly requests registration before the interview, use the early-creation branch below. Existing v2-v4 runs retain their version, phase order and completed operations; use the legacy-resume branch below.

After verifying the project for a standalone demand, list every open Redmine version and ask the user which one owns this Feature or Bug. Persist the selected ID, name, open status and attribution in `redmine.version` before `item-ready`. A scope item inherits the scope selection and does not ask again.

If the evidence describes multiple capabilities, recommend `new-scope`, explain the split and resolve that material scope decision. Preserve normalization and orientation when switching paths. A scope with one item continues here without restarting intake.

**Complete when:** sources are normalized and hashed, design evidence passes its applicable gate, repository facts are recorded without secrets, the lock is held, and exactly one demand is selected.

## 2. Interview and prepare the complete requirement

For a Feature, read [the Feature document contract](new-issue-feature.md); for a Bug, read [the Bug document contract](new-issue-bug.md). Suggest the type from the demand's observable goal or deviation. Carry an evidence-based, unambiguous suggestion into the final preview; ask separately only when the distinction changes the delivery or remains materially ambiguous.

Create `history/interview.md` at the first round or final review if no questions are needed. Invoke `requirements-grilling` with all normalized sources, repository evidence and the selected document contract. Reuse prior clarification answers and the local draft; ask again only when evidence reopens a decision. Use small prioritized rounds. Record questions, supported recommendations, answers, provenance, reopened decisions and explicit scope boundaries. Technical choices remain with implementation.

For an item inherited from `new-scope`, start this phase only after the user-facing item context handoff required by `new-scope.md`. The first functional question follows that handoff; it never substitutes for the Feature/Bug name and approved catalog context.

A material deferred or third-party decision follows the pause/resume contract and blocks approval. Continue independent questions in small rounds. Record approved exclusions as attributed `decisions`; if an existing pending question is settled by that boundary, retain its history and add the attributed `resolution`. An unapproved draft can keep visible questions, but a proposed exclusion cannot silently remove a blocker.

For late evidence, return to intake and reconcile confirmed, contradicted and reopened decisions before final review. Use `domain-modeling` only when its invocation gate fires. Keep item-specific decisions in the requirement; only resolved reusable terminology updates domain documentation. Flag architecture candidates for the later role.

**Complete when:** the full Feature/Bug document passes its contract, no material in-scope ambiguity or contradiction remains, exclusions are attributable, and the document is ready for the combined preview. No separate understanding or document confirmation is required here.

## 3. Resolve novelty and propose publication choices

Before remote reads, follow [operation-specific checks](redmine-preflight.md). Verify identity and destination, reusing conversation selections. Search the selected project for semantically similar issues using goal, actors, current/expected behavior and domain terms. Read missing candidate details. Present credible candidates with ID, title, status and reason. A match never authorizes reuse or an update. Resolve ambiguity about whether a candidate is the same demand before proposing creation. If the search finds no credible matches, include that result and its evidence in the final preview without asking for a separate confirmation.

If the user identifies an existing demand, persist `similarity.decision: existing-demand` and the candidate ID at `item-ready`, report it and stop without editing, commenting on, linking, or changing the existing issue. An existing issue created by this same run follows recovery instead of this novelty branch.

Propose Feature/Bug classification, an existing category or no category, tracker, initial status, title convention and delivery title using repository and project metadata. Show the evidence and rationale in the preview together with the selected version. Ask a separate question only for a material ambiguity that prevents a concrete preview; do not require a confirmation for each clear proposal. A scope item inherits its approved classification, convention, delivery and version. Category creation, priority, assignee, dates and estimates remain outside this flow.

In v5, classification can retain `suggested_type` and `rationale`, category can retain `id` and `name`, and `title_convention.confirmation` can be null until preview approval. Do not invent confirmation provenance. Resolve Feature Sequencing through [the publication contract](redmine-publication.md), including its automatic maximum-plus-one calculation for standalone Features.

**Complete when:** the verified destination, novelty result and metadata support a concrete complete preview, or the existing-demand branch has stopped without a mutation. Unavailable remote context preserves the complete local draft at `requirement-proposed`.

## 4. Approve one complete preview

Follow [the combined preview contract](redmine-publication.md). Present the whole requirement, proposed classification/category/convention with rationale, complete creation description and final publication description, and every included operation. A normal new run previews creation with the full functional requirement, followed by the description update that adds the definitive canonical path after the returned issue ID is persisted. The preview explicitly shows that ID binding. Include any addressable native relations and their endpoints; authorization covers only listed operations.

One approval confirms the requirement, selections and the presented operations. Record attributable selection confirmations and the `requirement` plus `publication-plan` machine records from that same consent. Persist the plan bytes, hashes and approvals before any mutation. Do not ask an equivalent question about understanding, the document or publication again.

For a material change after approval, show the delta and its consequences for content or operations. Keep the prior approved bytes and history while preparing the revised draft; no affected mutation runs during review. After the delta is approved, invalidate superseded approvals and append the new plan and canonical approval. Unchanged authorized retries reuse the existing consent. An unknown outcome must be reconciled before revising that operation. A change to an already approved scope/catalog follows its catalog-change procedure; do not create another issue implicitly.

**Complete when:** one attributable consent covers the exact full requirement and the listed operations, all material decisions are settled, and the approved state and durable plan validate.

## 5. Create and publish the approved content

Bind and persist one approved operation at a time using the publication helper. Verify capabilities, connection, identity, destination and the item lock immediately before each call. Run `redmine_create_issue` only if no issue ID exists and creation has not completed. If state already has an issue ID or the create operation is completed, never call create.

After a successful create response, immediately persist the returned issue ID, attempt, observation and completed create operation before moving files or advancing phases. Move the staging directory without overwriting an existing destination to `docs/harness/features/<REDMINE-ID>-<slug>/` or `docs/harness/bugs/<REDMINE-ID>-<slug>/`, and run `manage_artifacts.py prepare` there. Keep `.flow/`, history and sources together. Update source and scope references without changing IDs, hashes or approved bytes; an authorized relocation is not a product delta.

On a known failure, retain the approved payload and append a sanitized attempt. On an unknown create outcome, search the verified project using immutable run identity, approved fields and full content. Compare every credible candidate, including Sequencing. One exact match completes locally with that ID; proven absence allows the unchanged payload to retry; ambiguity or divergence blocks for resolution. Never infer absence from a failed or incomplete search.

Reread the created issue and verify Sequencing when applicable. Bind the preview's returned-ID placeholder only to the persisted issue ID. Preserve byte-for-byte content before and after the managed delimiters. A changed managed section is a divergence requiring attributed resolution and delta review, not permission to overwrite it. Persist the exact bound publication payload and baseline before the update. A generated binding or preserved outside human text does not require another equivalent approval.

Publish only the approved description, preserving remote status. Reconcile unknown update results by comparing the issue with the exact bound payload before any retry. For each listed relation, check existing native relations first, preserve its stable key, and persist its outcome before starting another operation. An equivalent relation completes locally without another create. Relations absent from the approved preview need their own concrete authorization.

Run the functional publication checker as well as state validation. Release the lock only after the final state is durable. Report issue, canonical path, approvals, validation and next role. Offer a commit only when appropriate; create one only with explicit permission.

**Complete when:** exactly one issue exists, the full approved functional content is published, human content/status are preserved, create/publish/planned relations are reconciled, and final state validates.

## Requested early creation

Use `creation_timing: before-interview` only with `early_creation_request` containing the user's identity, date and reason. This v5 branch uses the historical phase order: prepare metadata and novelty at `item-ready`, show a concrete initial-objective creation preview, obtain its approval and persist creation before interviewing. Record the exact `create-payload` approval. The user requested this exception; it is never the default or a prerequisite for other demands.

After creation, run the interview and present the complete requirement plus final update and relations together. Prepare a publication plan from the fresh existing issue snapshot, with `create: null`; one final consent covers the requirement and those operations. The early creation approval does not authorize unspecified future content.

**Complete when:** the request and initial creation authorization are attributable, exactly one issue is retained, and the later full requirement and publication share one review.

## Resume a v2-v4 run

Retain its schema, phase order, issue identity, approvals and operations. Do not migrate merely to reorder phases or recreate an issue already present. If creation is still pending, finish the requirement draft and combined preview before the historical creation phase; advance the legacy interview phases later using those retained answers. If creation is complete, resume the first incomplete operation and reuse all still-valid decisions.

Legacy approvals remain exact-payload records. To combine an outstanding requirement review and publication approval, prepare the full update with `render_publication.py --draft --reviewer <name>`, then record the existing `requirement` and `publish-payload` kinds from the same user consent. For a legacy pre-creation run, show the full creation content and later ID-bound publication as one explicit authorization; retain that consent and its bounds in history, and record each exact payload once its ID is known. Ask again only for a material delta or an operation not authorized by that preview. Existing approved retries keep their fingerprints; completed operations remain immutable.

**Complete when:** the old state validates under its original contract, retained history and identities are unchanged, and recovery continues without duplicate creation or equivalent confirmation.
