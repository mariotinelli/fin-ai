# Feature interview and document contract

Use this branch only after the shared workflow confirms `Feature` and the run lock is held. On resume, keep every valid decision, answer, approval, source reconciliation, and completed remote operation, then continue at the state's first incomplete phase.

Use objective and success, actors and permissions, inputs and observable results, flows, states, validation and recovery, functional integrations, and scope boundaries as coverage lenses for relevant evidence. Reuse settled answers; ask only material gaps in small rounds under `requirements-grilling`. A simple Feature need not traverse every lens as a question. Implementation choices and non-functional requirements not explicit in the evidence remain outside the interview.

Draft `feature.md` from `templates/feature.md`. Its objective explains actor, need, observable change, value, and essential limits. Numbered user stories cover every confirmed functional behavior without an artificial limit. Cover main and alternate flows, rules, observable data, verifiable acceptance criteria, dependencies, evidence, and scope boundaries. Each criterion states a condition, action, and result and traces to a described flow or rule.

When a design applies, reconcile it under `design-inputs.md` and populate `Designs e evidências` with the visual sources, applicable screens/states and approved adaptations. Include numbered visual acceptance criteria in the same acceptance section. A design declared visual-only is an explicit visual requirement, not an unrequested non-functional target or an optional inspiration.

For the separate visual foundation Feature, apply the existing-screen and future-navigation boundaries in `design-inputs.md`. Present the inspected screen inventory as coverage, including existing access/profile/settings, rather than reopening which screens to adapt. Future business pages and navigation are delivered by their own Features; do not manufacture a product question about placeholders versus disabled destinations to verify the foundation. Keep questions for material conflicts that remain after inspection and reuse settled answers.

When late evidence exists, the shared workflow must reconcile its confirmed, contradicted, and reopened decisions before this contract can pass.

**Complete when:** every required Feature section is substantive or explains why it is not applicable, each confirmed functional behavior appears in the document, every criterion is independently observable, explicit exclusions are attributed, and no material in-scope gap, contradiction, deferred question, or source reconciliation remains.
