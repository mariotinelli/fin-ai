# Gate 1 — phase {{PHASE_NUMBER}} development

Implement only the approved phase below in repository `{{REPOSITORY}}`. This is a fresh Codex session: directly read every listed file before editing, including repository instructions, architecture/context/ADRs, `task.md`, parent requirement and `planning.md`. Work without subagents and without accessing or modifying Redmine or YouTrack. Write user-facing prose, summaries and JSON free-text fields in Brazilian Portuguese; preserve schema keys and enum values.

If you start servers or test processes, record their PIDs and stop only those processes when finished. Do not perform general process or temporary-directory cleanup; preserve the Ralph executor and its artifacts.

## Required reading

{{CONTEXT_PATHS}}

## Approved phase

{{PHASE}}

Respect discovered boundaries and standards, implement appropriate focused tests and leave changes uncommitted. Finally return only the JSON required by the schema, with `status` equal to `completed`; this means **finalizado**, not approved.

For UI in this phase, inspect the required visual sources and implement their appearance with the approved field/state adaptations. Reusing components does not authorize retaining a conflicting starter theme. Compare the rendered result with the applicable reference screens/states and viewports; report concrete observations and evidence locations in `checks`. If comparison cannot run, record what was not verified and why. A new material visual/functional conflict needs requirement alignment rather than an invented adaptation. Backend-only phases report why visual comparison does not apply to their changes.

When the phase declares `Verificação renderizada`, prepare its approved capture script/fixture as needed within phase scope; the parent executor runs that command after development with normal host permissions and a dedicated `RALPH_EVIDENCE_DIR`. Capture output belongs there; preserve repository source and clean up only processes/test data started by the capture. Do not broaden permissions or alter the approved plan to work around a sandbox EPERM. Independent comparison and approval remain with validation.
