---
name: vertical-slicing
description: Evaluate and draft human-readable vertical implementation slices from an approved Feature and inspected code evidence. Use when another planning flow needs behavior-sized DEV work, estimates, real blockers, and exhaustive requirement coverage without publishing tracker issues.
---

# Vertical Slicing

At entry, read [user communication](references/user-communication.md) unless already read in this conversation. Apply it to progress, blockers and delivery, preserving this workflow's complete decision and approval requirements.

Turn an approved Feature and code evidence into narrow, complete, verifiable DEV deliveries. This discipline determines slicing quality; the calling workflow owns selection, dialogue, approval, persistence and any external integration.

Respond in Brazilian Portuguese (pt-BR), including proposals, task titles/descriptions, questions, estimates, progress and final delivery. Preserve technical identifiers and apply this language rule to delegated evaluations.

## Find the slices

Define the functional outcome and how to demonstrate it before estimating. Seek the smallest coherent delivery without fragmenting states that must work together. Registration may include minimal verification of the saved record without absorbing the entire history. An approved internal rule may be verified through reproducible integration with an identified consumer; this does not authorize an out-of-scope screen or API.

Map every rule and criterion to observable behavior. Before classifying creation, adaptation or existing behavior, read and apply [inspection evidence](references/inspection-evidence.md). Group changes that must cross necessary layers together to produce the outcome; do not create tasks per layer or include a layer the behavior does not require.

For UI with a declared design, inspect its normalized sources and the parent's visual criteria/adaptations. Cover visual outcomes alongside functional ones; “visual only” does not remove them. Compare existing components/shell with the reference before claiming reuse or existing coverage. System-wide visual adaptation belongs to a separate visual foundation Feature, delivered first, with its own DEV/QA slices and estimates. Business slices name that supplier and consume its implemented baseline while owning their screen-specific appearance. If a business parent absorbs foundational alignment or omits its prerequisite, return the exact boundary/dependency gap for requirement alignment before affected slicing approval. Every UI slice retains its applicable visual criteria and reference locators; missing visual acceptance or unresolved field/state conflicts likewise return to the caller.

Integrate common technical preparation into its first consuming slice within the responsible Feature. The visual foundation is an independently accepted product Feature, not technical preparation to merge into a business slice. Separate other preparation only when it has its own verifiable purpose and the exception is explicit for approval. A small Feature may be one DEV slice; implemented behavior receives evidence and coverage rather than invented work. When the entire Feature is implemented, propose empty slices with complete `existing` coverage for the caller to confirm through review and route to QA only.

**Complete when:** each slice delivers verifiable behavior and every Feature behavior has exactly one coverage destination.

Compare every proposed delivery with the approved parent requirement's meaning. Material differences do not become slices: return the approved meaning, exact proposed correction, impact and affected children to the caller. Treat a consumable API as material expansion when absent from the approved requirement, even if an endpoint seems technically convenient. The caller owns the decision and parent alignment.

**Complete when:** each delivery is covered by the approved requirement or isolated as an explicit material divergence, without silently expanding scope.

When an objective technical question prevents complete slicing, read [Study discipline](references/studies.md). A Study produces evidence for a later proposal; it is not a behavior slice and does not authorize inventing the rest of the breakdown.

**Complete when:** complete slices are defined or the blocking uncertainty is formulated as a bounded Study.

## Order and estimate

Under the visual-first delivery policy, the separate foundation's implemented and visually verified baseline is a startup prerequisite for dependent business slices, not merely integration needed at final acceptance. Name the supplier and preserve that approved order without duplicating its visual work in consumers.

Separate startup blockers from suppliers required for completion. Publication does not prove implementation, and a simulated presentation does not prove integration. For mutual completion dependencies, define joint verification or revise slices without cyclic native blockers. Apply the ceiling after slicing, reuse review and calibration; it does not determine task count.

Declare only blockers that prevent starting a slice. For another Feature, identify the capability and its single owner; reference its supplier slice when available and, while the Feature has no children, identify the parent as provisional with an explicit reason. Maintain topological order in the relevant graph, not merely proposed edges; no blocker means immediate startup.

Before estimating DEV, QA or Study, read [estimation and calibration](references/estimation.md). Distinguish remaining work, team context, comparable references and explicit tech lead corrections.

When independent agents are available, request parallel effort assessments per slice from at least two agents, supplying the approved requirement, proposed delivery and technical evidence, including context and comparable calibrated references, without exposing either candidate estimate to the other. Each assessment identifies work, uncertainties and hours. Reconcile differences through evidence and own the final estimate; automatic averages or agent votes do not replace accountable judgment. Without independent agents, perform the same analysis directly and disclose that limitation during review.

Every new DEV, QA or Study task must have a positive estimate of at most six hours. If work exceeds six hours, refine it into smaller vertical, verifiable, nonoverlapping deliveries before approval. If evidence supports no coherent split, keep the proposal blocked for scope review; a justification does not authorize publishing an over-limit task.

**Complete when:** edges are real and acyclic, external dependencies do not duplicate supplied capabilities, and every estimate has an explicit basis and attribution, is reviewable by a person, and is greater than zero and at most six hours.

## Name and describe

Preserve the complete Feature name and prefixes. Prefix development with `[DEV]` and append the delivery suffix. For a consumable API delivery already specified in the requirement, insert `[API]` after `[WEB]`, for example `[DEV] [WEB] [API] [OPERACIONAL] Gestão de Usuários - Cadastro`; internal endpoints serving other behavior receive no marker.

Before writing or reviewing descriptions, apply [task writing for implementers](references/task-writing.md). Use existing fields for functional context and expected change, relevant boundaries, verifiable criteria, dependencies and references. Technical context stays optional and does not prescribe implementation and testing.

Compare every assigned requirement with the complete slice description. Express observable conditions needed to verify delivery in acceptance criteria; a `traceability` reference does not replace that explanation. Preserve accessibility, responsiveness, timing and permission conditions when required rather than replacing them with generic adjectives such as “acessível”. Resolve omissions and contradictions between criteria, boundaries and coverage before presenting.

**Complete when:** title and description identify the outcome and boundaries without relying on conversation or prescribing the technical plan, and every assigned requirement's verifiable conditions appear in acceptance criteria.

## Requirement changes

When a new approved requirement supersedes the version used for published slicing, read [semantic-change discipline](references/semantic-changes.md). Classify meaning rather than bytes and locate affected and still-valid items before planning mutations.

**Complete when:** classification is supported by behavioral change and every baseline item is identified as affected or still valid.

When an approved functional review must be applied to published tasks, read [revision-application discipline](references/revision-application.md). It defines safe representation by task state and final preservation proof; the caller owns snapshots, approvals, persistence and MCP.

**Complete when:** each change uses a representation compatible with current remote state and no completed or out-of-impact task has been rewritten.

## Review the proposal

When the caller prepares test conditions alongside slices, apply [test-condition discipline](references/test-conditions.md) to the whole item, including Bugs and QA-only paths. The caller owns persistence, approval and document generation.

Present a numbered list of titles, deliveries, estimates and blockers followed by the coverage table. Invite the tech lead to merge, split and correct granularity or edges. Reassess coverage and dependencies after every change.

Read [evaluation scenarios](references/evaluation-scenarios.json) when evaluating the discipline or building semantic regressions.

**Complete when:** no rule is omitted or duplicated, no delivery expands the Feature, and the tech lead considers granularity appropriate.
