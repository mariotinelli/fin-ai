# Focused correction for phase {{PHASE_NUMBER}}

Correct only the findings below in repository `{{REPOSITORY}}`. This is a fresh DEV session: directly read every listed file before editing, including repository instructions, architecture/context/ADRs, `task.md`, parent requirement and the current `planning.md`. Work without subagents and without accessing or modifying Redmine or YouTrack. Write user-facing prose, summaries and JSON free-text fields in Brazilian Portuguese; preserve schema keys and enum values.

If you start servers or test processes, record their PIDs and stop only those processes when finished. Do not perform general process or temporary-directory cleanup; preserve the Ralph executor and its artifacts.

## Required reading

{{CONTEXT_PATHS}}

## Approved phase

{{PHASE}}

## Focused gate report

{{CORRECTION_REPORT}}

Preserve correct work already done, address only demonstrated findings and leave changes uncommitted. Finally return only the JSON required by the schema, with `status` equal to `completed`; this means **finalizado**, not approved.

Retain the primary visual source and approved adaptations during corrections. For affected UI, compare the corrected rendered state with that source and report evidence or the exact verification blocker in `checks`. Resolve findings within approved criteria; new material differences in fields, states or visual scope require requirement alignment. A functional-test correction must preserve the approved appearance.

Return the complete current `visual_evidence` collection, including preserved captures that still represent the corrected implementation. Each item identifies `path`, `screen`, `state`, `viewport`, `theme` and `reference`; paths must remain readable after your session and temporary processes close. Replace stale captures and explain unavailable coverage or the isolated authenticated fixture invocation in `checks`, without credentials or session data. This report replaces the previous development handoff for independent review.

The correction report contains actionable implementation defects. The parent executor reruns the approved `Verificação renderizada` command after correction; do not repeat browser-launch attempts inside the agent sandbox solely to clear EPERM or declare a blocked comparison verified. Preserve the capture contract, test isolation and evidence directory; changes to the approved command require plan review.
