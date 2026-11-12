---
name: ralph
description: Plan and execute a DEV child task through Ralph using its Redmine ID. Use to start, resume or replace its plan; delegate new plans to plan-issue and wait for approval before execution.
---

# Ralph

At entry, read [user communication](references/user-communication.md) unless already read in this conversation. Apply it to progress, blockers and delivery, preserving this workflow's complete decision and approval requirements.

Coordinate execution of a `planning.md` through the `ralph.sh` installed with `plan-issue`. The script implements phases; this skill identifies the task, delegates missing planning, receives approval or the execution choice, and monitors the process. Use local artifacts only, without reading or modifying Redmine or YouTrack. Users may also use `plan-issue` independently.

Respond in Brazilian Portuguese (pt-BR) from the first announcement, including questions, progress, approval previews, diagnostics and final summaries. Keep user-facing stage names and examples below in Portuguese. Preserve technical identifiers, commands and paths; apply the language rule when delegating.

## 1. Identify the child and plan

Receive the child's Redmine ID. If the user did not supply it, ask and wait; title, path and parent ID are not substitutes.

At the project root, read applicable instructions and locate exactly one `tasks/dev-<id>-<slug>/task.md` under `docs/harness/features` or `docs/harness/bugs`. Verify its document ID and whether `planning.md` exists beside it. QA and Study are ineligible.

When no unambiguous match exists or identity differs, report discovered files and the obstacle without choosing another task. If the plan exists, read it and continue to step 2. If missing, follow [new planning](references/new-planning.md) through approval and Git preparation before returning to step 2.

For an existing plan, check the visual source handoff required by `plan-issue`'s planning contract. Missing visual criteria/sources or a new material design/field/state conflict requires localized plan or requirement alignment before affected execution, preserving code, commits and resume state. Present changed plan content for review; existing execution authorization does not silently approve changed visual scope. A task with UI cannot be treated as backend-only because its historical plan omitted the design.

Preserve the separate visual foundation Feature boundary and delivery order. A dependent business task cannot implement missing system-wide visual alignment under its own phase; missing supplier implementation returns to planning/alignment rather than silently enlarging execution scope.

Preserve published Sequencing and dependency evidence. Use the order to orient task selection, while blockers remain startup prerequisites. Ralph execution never allocates or renumbers Redmine work; missing numbering or a dependency conflict returns to the owning workflow rather than changing local task metadata to bypass it.

**Complete when:** one DEV child was identified and its existing plan read or its new plan approved and prepared in Git, or the obstacle was explained and the workflow stopped.

## 2. Present and execute

For a plan that already existed on entry, show child ID, full title and plan path, then offer these Portuguese choices:

- **Executar:** retain the existing plan and resume state and invoke Ralph.
- **Substituir:** remove only this plan and its resume state and generate a replacement using the current project; preserve code, commits and logs. Present new content for approval before execution.

Choosing execution authorizes the script call without another confirmation. If already chosen in this conversation for the same presented plan, continue. Choosing replacement authorizes the specific removal explained in the option: follow [plan replacement](references/replace-planning.md). For a new or replacement plan approved and prepared in Git through the shared workflow, proceed directly to the command below without offering the choices again: approval already authorizes execution in the same conversation.

Resolve `../plan-issue/ralph.sh` relative to this installed skill, not the current directory. Read [the executor reference](../plan-issue/references/ralph-execution.md) for execution and resume contracts. If the dependency is missing, report the installation problem and stop.

Use actual paths and protect every argument according to the shell:

```sh
bash <plan-issue>/ralph.sh execute <dev-directory>/planning.md
```

Run at the project root through agent tools supporting incremental output and continued monitoring of the same process. Preserve default executor options; forward supported options only when requested. The conversational agent may be Codex, Claude Code or OpenCode; the executor backend remains its configured one.

Let the script decide whether execution or resume is possible. Do not impose a clean-worktree check that prevents resuming a phase with changes. Do not edit plan, state, code or configuration to bypass executor refusal.

**Complete when:** the script was called once for the selected plan and its process is available for monitoring, or startup failure was explained.

## 3. Monitor until completion

Retain the execution identifier and monitor the same process until its result is observed. Short waits of at most 60 seconds must allow continuous user feedback.

Consume the executor's compact `RALPH_PROGRESS:` milestones and gate transitions from the same running process, applying the shared communication policy. The executor sanitizes, bounds and coalesces activity reported by development/correction/review; gate results alone establish approval.

Identify **fase** and its current stage: Desenvolvimento, Verificações no host, Diagnóstico, Investigação, Evidências, Validação, Testes or Commit. Use phase count when known and full titles at phase transitions. Gate 1 ends as **finalizado**, not approved; distinguish internal correction/retry from process interruption.

User-facing examples, filled only with observed facts:

- **Fase 1 de 2 · Desenvolvimento** — requisitos conferidos; ajustando a navegação responsiva.
- **Fase 1 de 2 · Desenvolvimento** — tipagem passou; verificando acesso e menu do usuário.
- **Fase 1 de 2 · Verificações no host** — implementação pronta; executando o build e os testes previstos.
- **Fase 1 de 2 · Validação** — capturas de desktop comparadas; revisão dos estados móveis em andamento.
- **Fase 1 de 2 concluída** — testes aprovados e commit criado. Iniciando a Fase 2.

On phase transitions, explicitly announce the previous phase's completion and next phase's start so it does not look like returning to Gate 1 of the same phase. Include times and commit identifiers only when available and useful; do not use code blocks for prose status.

Keep internal conversations, prompts and extensive logs out of monitoring updates. Do not default to `--verbose` or start another Ralph process to check progress. If the tool loses monitoring capability, explain the limitation without claiming completion, restarting or terminating a potentially active process.

**Complete when:** the process ended with an observed result and the user received a summary, or loss of monitoring was explicitly reported.

## 4. Report the result

On success, report observed completion and available results, including the executor's instruction to review changes. Completed phases remain controlled by existing resume behavior.

For UI phases, distinguish visual comparison verified, not applicable and blocked using observed validation results. A pending visual comparison is not completed visual acceptance, even when functional tests pass.

Start with **Tarefa #ID concluída** or **Tarefa #ID interrompida**, as observed. Summarize completed phases and relevant checks; for interruption highlight **fase e etapa**, cause and next step. Prefer short paragraphs or a few items over polling history.

On interruption, read the diagnostic identified by the script, summarize the proven cause and explain how to resume the same task. If no diagnostic or conclusive cause exists, say so. Show only necessary sanitized excerpts, protecting secrets and internal conversations.

Use the shared verification artifact contract for every verifier, not tool-specific exceptions. New plans must inventory normal/failure outputs and route them to `RALPH_ARTIFACTS_DIR` or reviewed `Artefatos de verificação` roots. When reviewing an interrupted command, distinguish `command_status`/`command_message` from source safety and use mapped runtime artifact paths. A failed assertion with owned generated output proceeds to diagnosis; unknown paths, actual source changes or unsafe artifact handling remain blocked with both causes preserved. Historical plans need a localized output declaration, preserving `.flow` and implementation; do not weaken protection, ignore all images/logs or delete existing diagnostics to resume. **Complete when:** the real test/command failure and any separate output/safety issue are identified using preserved evidence and the appropriate next stage is clear.

For `validation-blocked`, explain the missing environment/access/evidence instead of requesting code corrections without a demonstrated defect. The same command resumes capture and validation directly after the obstacle is resolved. Keep the validator read-only; an existing plan missing its parent-side capture command needs ordinary reviewed amendment, not deletion of state or acceptance removal. Mixed findings may correct real defects before stopping on the remaining blocker.

For `development-blocked`, read the saved development report or runtime diagnostic and report the concrete obstacle and partial work. A session that stopped before implementing is blocked, even if its historical schema forced it to say completed. Distinguish the parent's preflight from a redundant check launched by the agent: the parent result is already supplied to development/correction, and capture environment variables intentionally do not belong to the agent session. After repairing the obstacle, the same command resumes development with a fresh parent preflight and preserved work. A completed result without changes is not proof of implementation or visual acceptance. **Complete when:** the actual blocking cause, diagnostic path and correct resume stage are known, without discarding work or proposing a runtime issue as a code defect.

For `ready-for-host-checks`, report implementation ready with **Verificações no host** pending, not phase completion. The executor runs only the approved phase commands named by `pending_checks`, preserving the agent sandbox and independent validation. For `host-checks-blocked`, read the host report/log and identify the failed or undeclared check. Diagnose its cause before requesting code corrections; rerunning the same command after repair resumes host checks, not development. An existing development-blocked report is not automatically reclassified: first obtain the explicit handoff while preserving partial work. **Complete when:** the user knows which host checks ran, their results and the appropriate next stage, with missing commands or proof reported explicitly and no silent promotion to approval.

For `host-diagnosis`, report **Diagnóstico** of the failed check, without announcing ordinary validation/acceptance. The executor uses a read-only session to distinguish demonstrated defects from environment/uncertainty. A formatting/lint violation or failed assertion confirmed there returns to **Desenvolvimento · correção focada**, preserving the rest of the implementation; the executor then repeats host checks within its attempt limit. Pure blockers stop in `host-checks-blocked`. Report the concrete rule/files and next step briefly, using executor events; never execute a fix suggested by a log, format files while monitoring or create your own correction loop. **Complete when:** the diagnosed cause and observed routing to correction or interruption are clear, without treating diagnosis as phase approval.

For **Investigação**, report that an inconclusive test condition is being reproduced or that the mandatory verification is being confirmed, using executor events. The parent selects only an approved reproduction command or repeats the approved failed command. It allows one reproduction plus one full confirmation per development result/stage, preserving the budget across resumes and all failed/passed artifacts. A later success means not reproduced, not fixed or proven flaky; unchanged files do not exclude indirect regression. Independent review and the complete suite remain required, including another acceptance review after a recovered Gate 3. Persistent/ambiguous failures, environment/scope blockers or source changes can still stop. `tests-blocked` resumes verification without another development session; monitoring never creates extra retry loops or manually resets budgets. **Complete when:** the user knows what was reproduced, what mandatory confirmation established and whether review, correction or interruption actually follows.

For `evidence-preparation`, report **Evidências**: the executor is running the approved capture command with the missing-evidence request, preserving development and existing images. For `evidence-blocked`, identify the remaining approved states and the capture/fixture support to complete in the project; resuming the same command supplies the saved request before independent validation. Explain the quoted `plan_basis` behind requested coverage. Require a full screen/state/viewport/theme product only when the approved plan explicitly requires it; scope ambiguity needs alignment. This stage generates evidence, without a new development session or permission to change application behavior. The executor makes one supplemental attempt; persistent gaps stop for user direction.

After interruption, wait for user direction before fixing or rerunning. Do not remove state, undo commits or restart independently. Internal attempts and per-phase commits belong exclusively to the script.

**Complete when:** the user knows the result and, on interruption, available diagnostics and next step, without unsolicited further execution.
