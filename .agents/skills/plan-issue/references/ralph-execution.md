# Ralph execution

Run:

```sh
bash <plan-issue>/ralph.sh execute <dev-directory>/planning.md
```

Ralph reads phases and the suite command directly from `planning.md`. It automatically creates `.flow/ralph-state.json` beside the plan, containing only the current phase, current gate, completed phases and their commits. Deleting this file forgets local progress; it does not undo commits or Git changes.

Before starting gates, the executor validates the plan's `Referências visuais` section under [the planning contract](planning-contract.md). Its declared normalized source files are included in required reading for development, correction and validation. Missing sections/sources and unsafe paths stop execution without changing progress. Historical plans need an explicitly reviewed amendment; the workflow never erases resume state to introduce visual criteria.

Gate 3 selects its interpreter from the baseline fence according to [the contract](planning-contract.md), including on Windows, without interactive profiles. A missing interpreter, invalid Bash syntax, Bash exit 126/127 and cmd exit 9009 stop execution as operational failures, preserving changes and state without returning to development in that run. Other nonzero exits stay in the correction loop; this classification does not identify every possible environment failure. Internal scripts of tools such as Composer may use another shell; check portability when preparing the baseline.

## Per-phase gates

Retain the Portuguese stage names in user-facing updates:

1. **Desenvolvimento:** opens a fresh Codex session to implement only the phase, without committing.
2. **Validação:** opens another fresh read-only session to review requirement, diff, tests, security, standards and applicable visual acceptance against the primary design and approved adaptations.
3. **Testes:** the script directly runs the complete suite declared in the baseline.
4. **Commit:** the script runs `git commit --no-verify` and moves to the next phase.

Implementation defects or test rejection start another development session with the reported error and repeat gates. The default stops after three attempts; override with `--max-attempts N`. Pure verification blockers stop immediately and preserve changes rather than consuming repeated development attempts.

Missing captures for an existing state use `kind: evidence-missing`, separately from environmental `verification-blocked`. Each missing-evidence finding quotes the governing phase/shared plan excerpt in `plan_basis`; the executor checks that the quote exists in the approved scope and stops on an invalid request. The reviewer must justify the requested coverage, including any full viewport/theme product. Scope ambiguity stops for alignment; it never authorizes more implementation or an invented capture matrix. Historical results without the new kind retain their conservative blocked behavior.

When only missing captures remain, Ralph saves a sanitized evidence request in the task's Git runtime and runs the already approved capture command once more with `RALPH_EVIDENCE_REQUEST` pointing to it. The console announces **Evidências**; no development session starts and no test/commit gate runs until independent validation approves. The next review receives both original and supplementary reports/images. The JSON is diagnostic data, not a new approval manifest or an executable command. The capture command must implement the requested fixture/coverage under [the capture contract](planning-contract.md).

One supplemental capture/review is allowed per validation attempt. Remaining gaps, missing capture commands or unavailable fixture support save `evidence-blocked` and preserve the complete request and code. Rerunning the same command feeds that request to capture before review, without repeating development. Interrupted `evidence-preparation` also resumes at validation. Environmental blockers stop rather than trigger evidence preparation; mixed findings return only demonstrated defects to development. Evidence completion cannot synthesize application changes or modify the approved plan.

Validation results include `visual_validation` with status `verified`, `not-applicable` or `blocked` and evidence/reason. Findings distinguish `kind: defect` from `kind: verification-blocked`. A mixed verdict corrects only demonstrated defects; if only blockers remain, execution stops before tests/commit and saves `current_gate: validation-blocked`. Resuming the same command then regenerates evidence and returns directly to validation. Legacy custom results with untyped findings and blocked visual verification stop conservatively rather than guessing a code defect. A blocked comparison or nonempty findings cannot accompany approval. Gate 3 passing does not supersede missing Gate 2 visual evidence.

When the approved phase contains `### Verificação renderizada`, Ralph runs its single command on the parent host before review, exporting `RALPH_EVIDENCE_DIR` and `RALPH_PHASE_NUMBER`. Each attempt gets fresh private artifacts/logs under `.git/ralph-runtime`; the command must produce actual captures and preserve repository source. The reviewer receives this report and inspects the images without launching a browser or writing temporary files inside its read-only sandbox. A failed command cannot be silently approved, but its output can establish an actionable application defect. Source modifications by capture or validation interrupt execution and are preserved for inspection. No agent receives broader sandbox permissions.

Existing UI plans without a capture command need a reviewed amendment when accessible current evidence is missing. Do not delete resume state, erase changes or approve static inspection as visual acceptance. Runtime artifacts are diagnostic evidence; no new approval manifest or state hash is introduced.

Development returns a complete report with `checks` and labelled `visual_evidence` (path, reference, screen, state, viewport and theme). Ralph saves the sanitized report under the task's Git runtime directory and injects it in full into validation, including when resuming a blocked or interrupted validation session. Corrections replace that report. Historical runs without a saved report explicitly report its absence; accessible evidence can still be inspected. The local `.flow` state remains minimal. Evidence is input to independent comparison, never an inherited approval.

Development/correction returns `status: completed` only after implementation, or `status: blocked` when an environment/access/scope obstacle prevents completion. A blocked report supplies the concrete reason in `summary`, nonempty diagnostic `checks` and preserved partial files. Ralph saves the full sanitized report before checking status or Git changes, stops in `development-blocked`, and shows the cause and report path without opening validation/tests/commit. Runtime/protocol failures also stop at that stage. A completed result without repository changes still fails its gate, but now retains and displays the agent's explanation. Rerun the same command after fixing the obstacle: preflight runs again, followed by development with partial work preserved. The environmental reason is not sent as a focused code correction; demonstrated defects retain their ordinary correction flow.

The parent preflight report is included in both development and correction prompts. A completed parent check establishes readiness for implementation; the agent may inspect its existing log/images and proceeds without relaunching preflight inside its sandbox. The parent supplies capture variables only to the capture subprocess; their absence in a model session is expected. A `CAPTURE_OK` line is a project script's diagnostic, not an additional marker to obtain inside each agent. New implementation obstacles return a blocked development result. Preflight images still do not demonstrate acceptance of the implementation that follows.

When code, tests and capture support are implemented and only sandbox-limited check execution remains, development/correction returns `ready-for-host-checks` with nonempty `pending_checks`: `host` maps to the approved phase `Verificação no host`, `rendered` to `Verificação renderizada`. Completed/blocked results use an empty array; legacy custom results without it retain their existing interpretation. The console reports implementation ready with checks pending. The parent opens a **Verificações no host** stage before validation, using only the approved commands; it never executes a command from the result JSON or guesses readiness from a blocked summary. Missing implementation/test/fixture logic remains development-blocked. Required undeclared commands require plan amendment.

Every declared host command runs after development/correction, even for an ordinary completed result, with source-change protection and isolated `TEMP`/`TMP`/`TMPDIR`. Capture-specific variables are not inherited by this command. It must use check-only modes, isolated test data and cleanup of owned processes. Rendered checks retain their existing evidence environment. Their completed images/report feed validation without an immediate duplicate capture. The full sanitized host report is saved under the task Git runtime and supplied to independent review alongside development and rendered evidence. Host success is verification input, not code approval.

Host failure, missing declared commands or source modifications save `host-checks-blocked` and stop before validation/tests/commit. Inspect the failed command/log to distinguish environment failures from actual implementation errors; no failure is blindly turned into another development attempt. Repair and rerun the same command to resume host checks directly with the saved explicit handoff and preserved work. Interrupted `host-checks` resumes there too; a failed preflight on that resume retains the host stage. Validation resume reuses the saved successful host report; missing proof stops and routes the next resume through host checks. Historical development-blocked tasks first need an explicit ready/completed report from development, preserving their partial implementation.

An approved `### Preflight da validação` command exercises the real bootstrap/browser/authenticated fixture and writes a protected-screen capture before development and again on resume, under the same parent capture environment. Failure saves `preflight-blocked` before development or retains `validation-blocked` on review resume, preserving source changes. Repairing the environment and rerunning continues at the appropriate stage. Plans without the section do not perform this check; prepare it under [the capture contract](planning-contract.md) before claiming readiness. Authentication must be recreated independently or replaced by durable, labelled rendered evidence; closing development's browser must not invalidate review.

The executor defaults to `gpt-6.1-sol` for development and validation gates. Choose another model with `ralph.sh execute <planning.md> --model <model>`. The default runner fixes reasoning effort at `medium` in both gates, overriding Codex CLI configuration for those runs. The executor does not access Redmine or YouTrack and uses no subagents. Its default backend requires Codex CLI; `RALPH_AGENT_COMMAND_JSON` may provide another compatible runner as a JSON argument array, and the chosen model is available as `RALPH_MODEL`. This backend dependency is separate from the `ralph` skill, which can be operated through Codex, Claude Code or OpenCode.

Before opening a model session, the default runner probes the selected `CODEX_BIN`/PATH executable with `codex exec --help` and checks its advertised model/config/sandbox/structured-output flags and the required role mode. Missing options, startup errors and probe timeout produce an explicit compatibility/configuration diagnostic without launching a model or falling back to broader permissions. This checks the CLI interface, not whether an effective sandbox implementation is available. Windows implementation selection remains with the user's/administrator's configuration; Ralph does not force MXC, clone/filter `config.toml`, disable user configuration or enable network access. Development remains `workspace-write` and review remains `read-only`. Validation startup/protocol failures save the same blocked stage for direct validation resume.

Each parent-side capture receives a separately owned short-lived temporary directory through process-local `TEMP`, `TMP` and `TMPDIR`. The parent environment and global settings remain unchanged. Browser profiles/build temporaries are cleaned after the command, including failures; capture scripts must still close their own processes. Images and sanitized logs belong to the separate persistent `RALPH_EVIDENCE_DIR`, so cleanup does not invalidate evidence returned to the reviewer or later diagnostics.

## Resume and minimal safety

A task allows only one simultaneous execution. A new phase requires a clean worktree. If a phase attempt already left changes, rerunning the same command resumes that phase from development, except that interrupted or blocked validation resumes directly at validation with the saved handoff. If execution ended immediately after commit, state at the commit gate with a clean worktree recognizes current `HEAD` as the phase commit and continues.

The `.flow` directory must be Git-ignored. There are no hashes, fingerprints, manifests, baseline approval, trailer proof or evidence reconciliation. The developer remains responsible for reviewing history and deciding when to delete state or undo work.

## Output

By default, the terminal shows only human-readable Portuguese messages:

```text
Fase 1 iniciada
[DESENVOLVIMENTO] Gate 1 em andamento [08:48]
[DESENVOLVIMENTO] Gate 1 finalizado [08:52]
[VALIDAÇÃO] Gate 2 aprovado [08:55]
[TESTES] Gate 3 aprovado [08:58]
[COMMIT] Gate 4 finalizado [08:58]
Fase 1 finalizada
```

Errors show the sanitized cause and diagnostic path. Prompts, stdout, stderr, tests and structured events remain in `.git/ralph-runtime`. Use `--verbose` to display technical events in the terminal.

Agent stdout/stderr are drained concurrently and sanitized line by line into their diagnostic files while the process runs, including before timeout or cancellation. Every 30 seconds the console reports that the gate remains active and identifies the diagnostic log; this heartbeat is liveness, not a claim of completed work. Partial lines become available when the runner flushes a newline or closes its output.

Default timeouts are 60 minutes for development, 30 for validation, 10 for parent-side capture and 60 for tests. Adjust with `--dev-timeout-minutes`, `--validation-timeout-minutes`, `--render-timeout-minutes` and `--tests-timeout-minutes`. Capture owns its declared processes and must clean them up; timeout/cancellation terminates only the subprocess tree started by Ralph.

Host checks default to 10 minutes per command, configurable with `--host-timeout-minutes`; this also applies to a rendered command explicitly deferred to that stage. A normal validation-side capture still uses `--render-timeout-minutes`.
