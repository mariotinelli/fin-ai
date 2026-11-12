# Focused correction for phase {{PHASE_NUMBER}}

Correct only the findings below in repository `{{REPOSITORY}}`. This is a fresh DEV session: directly read every listed file before editing, including repository instructions, architecture/context/ADRs, `task.md`, parent requirement and the current `planning.md`. Work without subagents and without accessing or modifying Redmine or YouTrack. Write user-facing prose, summaries and JSON free-text fields in Brazilian Portuguese; preserve schema keys and enum values.

If you start servers or test processes, record their PIDs and stop only those processes when finished. Do not perform general process or temporary-directory cleanup; preserve the Ralph executor and its artifacts.

## Required reading

{{CONTEXT_PATHS}}

## Approved phase

{{PHASE}}

## Focused gate report

{{CORRECTION_REPORT}}

Preserve correct work already done, address only demonstrated findings and leave changes uncommitted. Return only the schema JSON: `status: completed` after implementing the corrections (**finalizado**, not approved), or `status: blocked` when a concrete obstacle prevents completion. A blocked result explains the cause and remaining work in `summary`, supplies nonempty diagnostic `checks` and lists preserved partial changes.

When corrections, tests and capture support are implemented and only sandbox-limited execution remains, use `status: ready-for-host-checks` and nonempty `pending_checks`: `host` for the approved `Verificação no host`, `rendered` for the approved `Verificação renderizada`. Describe the attempted checks and sandbox obstacle in `checks`; the parent runs those approved commands, including a build/browser verification they already contain. Use empty `pending_checks` for completed/blocked results. Actual unfinished code/test/fixture work or a required undeclared command remains blocked. Preserve correct work; never encode executable commands in JSON or broaden permissions to complete checks.

## Parent-side preflight result

{{VALIDATION_PREFLIGHT}}

This check already ran in the parent host. On `completed`, proceed with the focused correction; inspect the supplied artifacts without repeating preflight inside this session or requiring a new `CAPTURE_OK`. Capture environment variables are intentionally limited to the parent's capture subprocess. Their absence in this agent session is expected. If a new implementation obstacle appears, report `blocked` with diagnostic evidence.

Retain the primary visual source and approved adaptations during corrections. For affected UI, compare the corrected rendered state with that source and report evidence or the exact verification blocker in `checks`. Resolve findings within approved criteria; new material differences in fields, states or visual scope require requirement alignment. A functional-test correction must preserve the approved appearance.

Return the complete current `visual_evidence` collection, including preserved captures that still represent the corrected implementation. Each item identifies `path`, `screen`, `state`, `viewport`, `theme` and `reference`; paths must remain readable after your session and temporary processes close. Replace stale captures and explain unavailable coverage or the isolated authenticated fixture invocation in `checks`, without credentials or session data. This report replaces the previous development handoff for independent review.

The correction report contains actionable implementation defects. The parent executor reruns the approved `Verificação renderizada` command after correction; do not repeat browser-launch attempts inside the agent sandbox solely to clear EPERM or declare a blocked comparison verified. Preserve the capture contract, test isolation and evidence directory; changes to the approved command require plan review.
