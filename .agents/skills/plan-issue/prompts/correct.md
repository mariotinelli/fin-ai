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
