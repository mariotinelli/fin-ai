# Plan replacement

Use only after the developer chooses to replace the identified plan knowing that the plan and its resume state will be removed. This choice authorizes that specific removal; approval of new content happens later. All explanations and questions remain in Brazilian Portuguese.

## 1. Check before removal

Check complete Git status, including staged, unstaged and untracked files. Any pending change, including to the old plan or its `.gitignore`, prevents replacement. Report paths and wait for developer resolution, preserving files and index. Do not stash, discard or create cleanup commits. After resolution, recheck before removing anything.

Confirm [plan-issue](../../plan-issue/SKILL.md) and the installed executor are available. Resolve exact `planning.md` and `.flow/ralph-state.json` paths inside the selected child directory. Preserve ambiguous destinations, directories replacing files, and links or path components redirecting outside the task; report the obstacle.

Check for active execution of this task using the monitored process and, if necessary, existing `ralph-locks` records in the Git-reported administrative directory. `owner.json` identifies `state_path` and the owning process; consult the installed executor contract to interpret these records. If execution is active or completion cannot be determined, stop before removal. Preserve processes and locks; do not invoke another executor to probe activity.

**Complete when:** the choice is authorized, Git has no pending changes, dependencies and destinations were verified, and there is no active or indeterminate task execution.

## 2. Remove only the two selected files

Keep the pre-removal Git observation and authorized paths in the conversation. Remove only this child's `planning.md` and, when present, `.flow/ralph-state.json`. Use shell-protected literal paths; in PowerShell use `-LiteralPath`. Do not recursively delete directories.

Preserve `.flow`, its other files, neighboring tasks, `ralph-runtime` logs, locks, code and Git history. Missing state is valid. Verify both selected files are absent. If any operation fails, report which removals occurred and stop; do not broaden cleanup, restore old progress automatically or start the executor.

**Complete when:** only the plan and its matching state were removed with everything else preserved, or a failure was reported without continuing.

## 3. Plan from the current project

Follow [new planning](new-planning.md), carrying the pre-removal observation and identifying plan deletion as authorized replacement work. Let `plan-issue` inspect current code, requirement and tests; do not reuse the discarded plan's completed-phase list.

Reuse that workflow's complete presentation, adjustments, explicit approval, limited `--no-verify` commit when differences exist, and monitored execution. If approved content is already tracked without differences, continue without an empty commit. The initial replacement choice does not approve the new plan in advance.

If planning fails or old state reappears, explain and stop. Do not restore or reuse discarded progress. The executor creates its minimal state when the approved plan starts.

**Complete when:** the new plan passed review and preparation through the shared workflow and was passed once to execution, or the obstacle was reported without execution.
