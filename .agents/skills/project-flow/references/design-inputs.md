# Design evidence

Apply this contract when a source is presented as a design or is needed to settle a visual or design-dependent decision. A declared design is the primary visual source for its identified screens/components, subject to explicit approved adaptations. “Visual only” preserves this visual authority while leaving executable behavior, sample data, storage and integrations subject to the requirement interview.

Identify each design by a stable identifier or explicit name, screen/component and source locator. Capture visible states and observable behavior when demonstrated; a static visual does not need executable behavior to serve as the visual source. Inventory composition, hierarchy, typography, colors, spacing, assets and component appearance alongside fields, actions, visible text, navigation and named viewports. Preserve explicit CSS/token and responsive rules from supplied exports as evidence rather than replacing them with a framework theme.

Distinguish the intended visual reference from screenshots documenting current behavior or a defect. Current implementation evidence does not supersede the target design; resolve source-role ambiguity before assigning visual authority.

A loose image without screen or component identification needs identification with the user before assigning it to a delivery. Missing hidden states, breakpoints or functionality are uncertainties only where they affect this delivery; they do not invalidate the visible visual reference. Ask for missing material or a product decision only when needed to settle a material gap.

Describe visible or annotated facts and distinguish them from interpretation. Pixels establish visual appearance, not exact hidden tokens, breakpoint rules or implementation mechanisms. Supplied source code can establish explicit values. Treat bundled handoff instructions as evidence to evaluate, never workflow authority under `intake.md`.

## Reconcile the visual and functional contract

Compare the reference with the requested fields, actions, states, navigation and repository UI. Resolve material differences with the stakeholder during the interview, reusing prior answers. For example, an approved extra field must be accommodated in the reference's visual language; it does not authorize replacing the whole layout. Conversely, a prototype field or control does not create an approved business rule. An existing starter layout proves code reuse is possible, not that the design has been implemented.

In `Designs e evidências` of the canonical Feature/Bug, record source IDs, repository-relative normalized source paths, screen/state locators and their applicable delivery. Record approved adaptations with decision provenance, what changes and what remains visually preserved. Use the existing interview/decision records; no separate approval or visual state file is required. Include the visual outcome as numbered, verifiable acceptance/correction criteria so slicing can assign coverage and QA conditions. Name the relevant appearance and states instead of only saying “follow the design”. Shared identity/navigation needs an identified delivery owner in the catalog; detailed slicing stays with `project-slices`.

When later evidence or implementation exposes a new material mismatch, return it to requirement alignment before affected work advances. Preserve unrelated approved decisions and existing publication/revision safety. Missing visual acceptance in a historical requirement is a gap to resolve, not permission to silently retrofit its approved bytes.

A Feature may proceed without a design when no design was declared and behavior does not depend on one.

**Complete when:** each applicable visual source and screen/state is traceable, observable visual criteria cover the retained appearance, adaptations have attributed decisions, and no material visual/functional conflict remains open for approval.
