# Focused development investigation — phase {{PHASE_NUMBER}}

Investigate only the observed failures below in repository `{{REPOSITORY}}`. Implementation of the phase already exists: inspect and preserve the current diff. This is a development session with normal workspace-write permissions, not permission to expand product scope, change dependencies/global configuration or bypass checks. Use pt-BR for commentary and JSON free text. Work without subagents or Redmine/YouTrack access.

## Required reading

{{CONTEXT_PATHS}}

## Approved phase

{{PHASE}}

## Identified failures and preserved evidence

{{CORRECTION_REPORT}}

An actual required behavior failed; its root cause need not be known before your investigation. Inspect application, tests, fixtures/capture support, isolated execution configuration and their shared consumers. Missing information about a browser API, permission or transport is uncertainty, not proof of an external blocker. Gather the missing observable facts and distinguish application failure from test/fixture failure. You may instrument and correct those sources within approved scope, including process-local browser/test configuration. Use actual supported tools and isolated data, preserving real transport and intended behavior.

Correct a cause when evidence establishes it and the correction fits the phase. Do not fake API success, weaken assertions, skip cases, alter acceptance criteria, update approval/history records or add repository-wide rules to obtain green output. A real external prerequisite, new dependency/global permission or unresolved product/scope decision must be reported with concrete evidence and the precise next action. Unchanged files alone do not prove the failure unrelated to the task.

If execution needs the parent host, prepare instrumentation/support under the existing approved commands and return `ready-for-host-checks` with the relevant pending selectors. Do not supply executable shell text in JSON or silently edit planning.md to invent another command. Parent commands remain check-only for repository source; they may collect generated outputs under the approved artifact contract. Preserve mapped runtime evidence and record only owned PIDs/processes for cleanup.

Return the development-investigation schema. `investigation_outcome` identifies `cause-established`, `evidence-prepared` or `blocked`, with nonempty concrete findings/evidence for a completed/ready handoff. Distinguish observations from hypotheses and pending verification. `evidence-prepared` requires an actual support/instrumentation change; an unchanged repeated handoff is not progress. If code is unchanged but inspection establishes a cause, explain the new finding and its source so the parent can triage it without blindly repeating checks. A completed investigation is not phase approval. Leave implementation/support changes uncommitted.

Use a few short commentary milestones beginning with `RALPH_PROGRESS: `, at most 180 characters, describing the condition under investigation, newly observed evidence and next action. Keep credentials and transcripts out of progress. Return final JSON separately.
