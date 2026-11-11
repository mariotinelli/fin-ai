# Gate 1 — phase {{PHASE_NUMBER}} development

Implement only the approved phase below in repository `{{REPOSITORY}}`. This is a fresh Codex session: directly read every listed file before editing, including repository instructions, architecture/context/ADRs, `task.md`, parent requirement and `planning.md`. Work without subagents and without accessing or modifying Redmine or YouTrack. Write user-facing prose, summaries and JSON free-text fields in Brazilian Portuguese; preserve schema keys and enum values.

If you start servers or test processes, record their PIDs and stop only those processes when finished. Do not perform general process or temporary-directory cleanup; preserve the Ralph executor and its artifacts.

## Required reading

{{CONTEXT_PATHS}}

## Approved phase

{{PHASE}}

Respect discovered boundaries and standards, implement appropriate focused tests and leave changes uncommitted. Finally return only the JSON required by the schema. Use `status: completed` only after implementing the phase; this means **finalizado**, not approved. If a concrete environment/access/scope obstacle prevents implementation, return `status: blocked`, explaining the cause and unperformed work in `summary`, with nonempty diagnostic `checks`. Preserve partial work and list its files. Ending a session before implementation is blocked, even when no file changed.

## Parent-side preflight result

{{VALIDATION_PREFLIGHT}}

The parent executor already ran the plan's preflight before opening this session. A `completed` result establishes that check's readiness: read its report/log/images as needed and proceed with implementation. Do not repeat that preflight inside this agent sandbox or demand another `CAPTURE_OK` marker. `RALPH_CAPTURE_MODE`, `RALPH_EVIDENCE_DIR` and isolated temporary paths belong to the parent capture subprocess, so their absence here is expected. A failed parent preflight prevents this session from starting. `not-configured` means no parent preflight was declared; follow the phase's actual prerequisites and report concrete blockers. If a new obstacle occurs during implementation, report it as blocked with evidence rather than inventing replacement capture settings or marking the phase completed.

For UI in this phase, inspect the required visual sources and implement their appearance with the approved field/state adaptations. Reusing components does not authorize retaining a conflicting starter theme. Compare the rendered result with the applicable reference screens/states and viewports; report concrete observations and evidence locations in `checks`. If comparison cannot run, record what was not verified and why. A new material visual/functional conflict needs requirement alignment rather than an invented adaptation. Backend-only phases report why visual comparison does not apply to their changes.

Return every available capture in `visual_evidence`, with `path` (absolute or repository-relative), `screen`, `state`, `viewport` (width x height), `theme` and `reference` (source path and screen/state locator). Keep images at durable locations readable by the independent validator after closing your browser and processes. For protected screens, use an isolated reproducible authenticated fixture or supply rendered captures with this coverage; explain fixture invocation and missing coverage in `checks`, without credentials or session data. Return an empty array when no captures are available and explain why in `checks`. The report is handed to validation and retained for resume; it does not grant approval.

When the phase declares `Verificação renderizada`, prepare its approved capture script/fixture as needed within phase scope; the parent executor runs that command after development with normal host permissions and a dedicated `RALPH_EVIDENCE_DIR`. Capture output belongs there; preserve repository source and clean up only processes/test data started by the capture. Do not broaden permissions or alter the approved plan to work around a sandbox EPERM. Independent comparison and approval remain with validation.
