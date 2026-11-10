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

Validation or test rejection starts another development session with the reported error and repeats gates. The default stops after three attempts; override with `--max-attempts N`. Operational failures stop immediately and preserve changes.

Validation results include `visual_validation` with status `verified`, `not-applicable` or `blocked` and evidence/reason. A blocked required visual comparison cannot accompany approval; the executor refuses that inconsistent result, including from a custom runner. Rejected visual findings follow the ordinary correction/attempt boundary, preserving work if the environment still prevents comparison. Gate 3 passing does not supersede missing Gate 2 visual evidence. The validator's evidence remains a review responsibility; structural checks do not prove that a claimed comparison occurred.

The executor defaults to `gpt-6.1-sol` for development and validation gates. Choose another model with `ralph.sh execute <planning.md> --model <model>`. The default runner fixes reasoning effort at `medium` in both gates, overriding Codex CLI configuration for those runs. The executor does not access Redmine or YouTrack and uses no subagents. Its default backend requires Codex CLI; `RALPH_AGENT_COMMAND_JSON` may provide another compatible runner as a JSON argument array, and the chosen model is available as `RALPH_MODEL`. This backend dependency is separate from the `ralph` skill, which can be operated through Codex, Claude Code or OpenCode.

## Resume and minimal safety

A task allows only one simultaneous execution. A new phase requires a clean worktree. If a phase attempt already left changes, rerunning the same command resumes that phase from development. If execution ended immediately after commit, state at the commit gate with a clean worktree recognizes current `HEAD` as the phase commit and continues.

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

Default timeouts are 60 minutes for development, 30 for validation and 60 for tests. Adjust with `--dev-timeout-minutes`, `--validation-timeout-minutes` and `--tests-timeout-minutes`.
