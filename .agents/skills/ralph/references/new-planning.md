# New planning

Use this path when the identified DEV child has no `planning.md`, either originally or after [authorized replacement](replace-planning.md). Planning belongs to `plan-issue`; continuation, preparing the approved plan in Git and invoking the executor belong to `ralph`. Deliver all user-facing content in Brazilian Portuguese.

## 1. Delegate while preserving existing work

Before delegation, observe project Git status: staged, unstaged and untracked files. Read the diff of an already modified child-directory `.gitignore`, if any. Keep this observation in the conversation to distinguish preexisting changes from planning output; do not create state or manifests for it.

On replacement, retain the pre-removal observation too: authorized deletion of the plan belongs to this workflow rather than unrelated changes. The replacement plan must consider current code and preserve existing implementation.

Read and apply [plan-issue](../../plan-issue/SKILL.md) for the child ID. Resolve the reference relative to this installed package. If missing, report the installation problem and stop.

Let the delegated skill conduct project/parent inspection, baseline, writing and plan review. Do not duplicate its procedure or implement task code. Independent `plan-issue` usage is unchanged; when invoked by `ralph`, final command delivery returns control here instead of ending the conversation.

**Complete when:** planning produced the complete child plan and specified ignore adjustments, or explained an obstacle without starting the executor.

## 2. Review and approve

Ensure the developer received the complete plan and incorporate requested adjustments through the delegated workflow. Wait for explicit approval of the final version. Explain that approval permits committing planning files with `--no-verify` when differences exist, then starting Ralph in the same conversation.

Reuse approval already obtained during `plan-issue` for this content rather than requesting equivalent confirmation. If content changes after approval, present changes and wait for approval of the result before continuing. Do not record approval, hashes or readback in additional files.

**Complete when:** final content was presented and approved by the developer. Without approval, neither commit nor execute.

## 3. Commit only planning

Compare current Git status with the previous observation and inspect diffs. The only commit candidates are this child's `planning.md` and necessary `.gitignore` adjustment produced by planning. Authorization covers that content, not every file in the directory.

If unrelated changes exist, including code, untracked files or already staged content, identify paths and wait for the developer to resolve the obstacle. Preserve files and index; do not stash, discard changes or create another commit to clean the project. If the same `.gitignore` contains preexisting unrelated changes, neither include the whole file nor split them automatically. After resolution, recheck the approved plan and Git status.

With only authorized content pending, explicitly stage relevant paths and inspect the index diff before committing. Use repository-relative paths, shell-protected arguments and literal pathspecs; do not select all files or the whole directory.

If approved plan and relevant `.gitignore` are already tracked and identical to `HEAD`, with clean index and worktree, explain there are no differences to commit and continue to execution. Do not create an empty commit. Verify Git content: absence of a diff alone does not prove an ignored or untracked file is versioned.

Reference sequence, substituting reviewed paths and omitting `.gitignore` when unnecessary:

```sh
git --literal-pathspecs add -- <planning.md> <.gitignore-if-changed>
git diff --cached --name-only
git diff --cached
git --literal-pathspecs commit --no-verify --only -m "docs: plan DEV <id>" -- <planning.md> <.gitignore-if-changed>
```

The staged diff must contain only approved planning and the relevant ignore adjustment. If unrelated content appears or the plan changed, stop before committing. Limiting commit paths adds protection; it does not authorize ignoring unrelated changes.

On commit failure, explain the error and wait for direction. Do not change Git configuration, identity or hooks to bypass it, and do not invoke the executor. On success, verify committed files/diff and current project status; if changes remain, report the obstacle before starting. Do not push.

**Complete when:** approved plan and ignore adjustment are tracked through a successful limited commit or were already identical to `HEAD`, and no pending project changes prevent startup.

## 4. Continue in the same conversation

Return to the `ralph` execution step and invoke the existing executor for this plan without another skill invocation or confirmation. Reuse existing monitoring and interruption handling.

This path neither creates nor removes resume state. If old state or another obstacle exists, preserve it and report the situation rather than deleting it to force startup. The change check for new planning does not apply to the separate existing-plan resume path.

**Complete when:** the approved Git-prepared plan was passed once to monitored execution, or the obstacle was reported without starting a process.
