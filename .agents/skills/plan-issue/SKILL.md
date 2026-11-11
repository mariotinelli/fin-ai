---
name: plan-issue
description: Technically plan a DEV child task in executable phases and produce the single planning.md consumed by Ralph. Use when a developer requests child-task planning; do not use to implement its phases.
---

# Plan issue

Turn a DEV child into a human-readable `planning.md` executable by Ralph. Use `task.md` and the parent requirement as product sources, inspect the repository for technical facts, and never read or modify Redmine.

Respond in Brazilian Portuguese (pt-BR) from the first announcement, including questions, progress, diagnostics, planning documents and final delivery. Preserve technical identifiers, paths and the Portuguese document headings required by the executor. Apply this language rule to delegated work.

## 1. Locate the task

Receive the DEV child ID and locate exactly one `tasks/dev-<id>-<slug>/task.md` under `docs/harness/features` or `docs/harness/bugs`. Also read the parent's `feature.md` or `bug.md`. Study and QA are outside this workflow.

Read applicable repository instructions, architecture, ADRs, conventions, automation, related implementation and existing tests. Before describing current state, architecture and risks, apply [technical inspection](references/technical-inspection.md). Discover the aggregate command and its verifiers from actual configuration rather than inferring its contents from its name.

Read published Sequencing and supplier/blocker references as execution context. Numbering is owned by approved `project-slices` publication, not technical planning; preserve it and expose a dependency conflict instead of renumbering tasks. A lower number alone does not clear an unresolved blocker.

For UI work, read the parent's and task's visual references and approved adaptations. Compare the existing UI with the primary design rather than treating the current theme as authority. Missing visual acceptance or a material mismatch in fields/states/navigation returns to requirement/task alignment; preserve unaffected planning while that decision is pending. Do not silently repair approved product documents or substitute the starter layout.

**Complete when:** task, parent requirement, standards and verifiers are understood, and claims supporting decisions have traceable evidence.

## 2. Observe the baseline

Check runtime, tools and command prerequisites before execution. Use a compatible runtime through the project's mechanism or process-local selection without changing global configuration or requirements. Selection must also work in Ralph's environment, not merely through a session alias.

Run the complete suite once without modifying tracked files. First check whether scripts apply fixes: use the project's equivalent check mode; if none exists, record the obstacle instead of silently mutating files. Read [the planning contract](references/planning-contract.md) to record command, gate composition and results per verifier.

If the environment prevents execution, identify necessary preparation and unexecuted steps. This does not demonstrate an application defect. The observed baseline does not authorize a failing test gate and has no separate approval, hash or state.

**Complete when:** the reproducible command, prerequisites and observed results are described in `planning.md`, distinguishing failures from unexecuted steps and environment obstacles.

## 3. Write the plan

Read [the planning contract](references/planning-contract.md) and create only `<dev-directory>/planning.md`. Ensure `<dev-directory>/.gitignore` contains `/.flow/`; add that line if absent. The `.flow` directory holds only Ralph's local resume state.

Split work into small sequential phases. Each phase must fit a fresh session, produce a verifiable change and end ready for commit. Write for a human developer: explain behavior, likely files, boundaries, acceptance and verification without turning the plan into a mechanical command sequence.

Check correspondence between requirements, changes and acceptance evidence as specified by the contract. A localized task may need only one phase; avoid repeating the same explanation in objective, strategy and expected changes.

Present the complete plan to the developer and incorporate requested adjustments. The developer decides when to commit the plan.

**Complete when:** the developer has reviewed the content, exactly one `planning.md` exists, and every phase has observable acceptance criteria.

## 4. Hand off to Ralph

Read [Ralph execution](references/ralph-execution.md). If a safe complete baseline command could not be determined, deliver only the blocked draft and missing information; do not hand that draft to Ralph. Otherwise provide this command with the actual path:

```sh
bash <plan-issue>/ralph.sh execute <dev-directory>/planning.md
```

Do not generate state, manifests, readback, approval or hashes. Ralph creates its minimal state automatically when it starts. If an operational obstacle remains, deliver the plan with necessary preparation and make execution conditional on resolution rather than announcing readiness.

**Complete when:** the simple command has been provided and no task implementation code has been written.

When evaluating the skill or building semantic regressions, use [evaluation scenarios](references/evaluation-scenarios.json). They evaluate planner decisions, not demonstrated product execution.
