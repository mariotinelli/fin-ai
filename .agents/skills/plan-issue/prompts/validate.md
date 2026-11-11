# Gate 2 — independent phase {{PHASE_NUMBER}} validation

Validate the implementation of the approved phase below in repository `{{REPOSITORY}}`. This is a fresh, independent, read-only Codex session: directly read every listed file and inspect the diff and tests without modifying any file. Work without subagents and without accessing or modifying Redmine or YouTrack. Write user-facing prose, findings and JSON free-text fields in Brazilian Portuguese; preserve schema keys and enum values.

The complete suite belongs to Gate 3, after this validation. Do not reject solely because that gate's result is unavailable or because of historical test caches: report demonstrable defects in the current implementation. Check focused tests and their coverage of phase criteria.

Visual acceptance required by this phase belongs to this gate. Read the declared visual sources, inspect the rendered evidence supplied below, and compare the relevant screens/states/viewports with the primary reference and approved adaptations. The parent executor runs the approved capture command outside the agent sandbox; this session remains read-only. Do not relaunch a browser, build assets or create temporary capture files inside this session to work around sandbox restrictions. If no usable current evidence exists, report the concrete verification blocker while still inspecting code for demonstrable defects. State what was actually inspected; static code, functional assertions, overflow checks and screenshots without comparison do not demonstrate fidelity. Existing framework appearance is not the visual authority when a design applies.

Return `visual_validation` with `status` and nonempty `evidence`: `verified` identifies reference and current rendered evidence, states/viewports, comparison results and approved differences; `not-applicable` explains why this phase has no visual acceptance and identifies a later UI phase when relevant; `blocked` states the missing access/tool/evidence preventing the required comparison. Each finding requires `kind`: `defect` for a demonstrated correctable implementation error, or `verification-blocked` for a required check prevented by missing environment/access/evidence. EPERM launching Chromium, missing screenshots and unavailable build tooling are verification blockers unless separate evidence proves an implementation defect. Severity does not classify cause. Include both kinds when both exist. A required comparison left pending returns `verdict: rejected` with a `verification-blocked` finding; never invent a code defect to request another development attempt. Never use `not-applicable` to bypass affected UI or approve with visual verification blocked. Product conflicts return for alignment without authorizing new behavior. On approval, the ordinary `findings` array remains empty.

## Parent-side rendered verification

{{RENDERED_VERIFICATION}}

Inspect listed images with the available image-reading tools and read the capture log when needed. A successful command or generated image alone does not establish visual acceptance. A failed required capture cannot be approved; distinguish a demonstrated application error in its output from an environmental blocker.

## Required reading

{{CONTEXT_PATHS}}

## Approved phase

{{PHASE}}

Issue a structured verdict considering requirements, boundaries, existing standards, tests, security, regressions, duplication, complexity and unjustified changes. Approve only when observable evidence fully satisfies the phase. On rejection, record each finding separately with severity, affected criterion and concrete evidence; on approval, use an empty `findings` array. Return only the JSON required by the schema.
