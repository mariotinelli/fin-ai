---
name: ralph
description: Plan and execute a DEV child task through Ralph using its Redmine ID. Use to start, resume or replace its plan; delegate new plans to plan-issue and wait for approval before execution.
---

# Ralph

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

Communicate observed changes in short messages highlighting **fase**, stage name and **resultado**. Prefer Desenvolvimento, Validação, Testes and Commit; keep gate number secondary. Use phase count and plan title when known. Gate 1 ends as **finalizado**, not approved. Distinguish internal rejection followed by script retry from process interruption.

User-facing examples, filled only with observed facts:

- **Fase 1 de 2 — Política de senha** · **Desenvolvimento em andamento** (Gate 1).
- **Fase 1 de 2** · **Validação aprovada**. Iniciando os testes (Gate 3).
- **Fase 1 de 2 concluída** — testes aprovados e commit criado. **Próxima: Fase 2 de 2 — Desenvolvimento**.
- **Fase 2 de 2** · **Testes reprovados — tentativa 2 de 3**. O executor iniciou a correção nesta mesma fase.

Each update contains only new progress. Do not repeat a growing history or send a message per poll. Without changes, continue monitoring and, when an update is needed, use one Portuguese line: **Fase 2 de 2 · Desenvolvimento** — sem nova saída desde a última atualização. Respect the environment's communication frequency; avoid repetitive variations. Missing output proves neither activity nor a hang: do not invent progress, percentages or times.

On phase transitions, explicitly announce the previous phase's completion and next phase's start so it does not look like returning to Gate 1 of the same phase. Include times and commit identifiers only when available and useful; do not use code blocks for prose status.

Keep internal conversations, prompts and extensive logs out of monitoring updates. Do not default to `--verbose` or start another Ralph process to check progress. If the tool loses monitoring capability, explain the limitation without claiming completion, restarting or terminating a potentially active process.

**Complete when:** the process ended with an observed result and the user received a summary, or loss of monitoring was explicitly reported.

## 4. Report the result

On success, report observed completion and available results, including the executor's instruction to review changes. Completed phases remain controlled by existing resume behavior.

For UI phases, distinguish visual comparison verified, not applicable and blocked using observed validation results. A pending visual comparison is not completed visual acceptance, even when functional tests pass.

Start with **Tarefa #ID concluída** or **Tarefa #ID interrompida**, as observed. Summarize completed phases and relevant checks; for interruption highlight **fase e etapa**, cause and next step. Prefer short paragraphs or a few items over polling history.

On interruption, read the diagnostic identified by the script, summarize the proven cause and explain how to resume the same task. If no diagnostic or conclusive cause exists, say so. Show only necessary sanitized excerpts, protecting secrets and internal conversations.

For `validation-blocked`, explain the missing environment/access/evidence instead of requesting code corrections without a demonstrated defect. The same command resumes capture and validation directly after the obstacle is resolved. Keep the validator read-only; an existing plan missing its parent-side capture command needs ordinary reviewed amendment, not deletion of state or acceptance removal. Mixed findings may correct real defects before stopping on the remaining blocker.

After interruption, wait for user direction before fixing or rerunning. Do not remove state, undo commits or restart independently. Internal attempts and per-phase commits belong exclusively to the script.

**Complete when:** the user knows the result and, on interruption, available diagnostics and next step, without unsolicited further execution.
