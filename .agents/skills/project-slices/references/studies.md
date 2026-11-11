# Exceptional Study and resume

This branch publishes one exceptional DEV child when `vertical-slicing` identifies uncertainty blocking the complete proposal. It neither publishes remaining DEV/QA nor completes slicing, parent or current scope item.

## Prepare and approve

For new block-policy inputs, apply [version block Sequencing](sequencing.md). Add `sequencing` snapshot/config to the Study plan; its one early child position is included in this Study's exact preview and v3 state. The parent remains unnumbered. Add `--sequencing-snapshot` to `begin-create` and `complete`; ordinary slicing later retains the Study's number as part of its block. Existing Study states resume with their historical payloads.

Save `.work/slices-study-plan.json` with source `slices-input-check.json`, sanitized parent/metadata snapshots, native fields and `study` containing `subject`, `question`, `expected_result`, `effort_limit`, `estimate_hours`. Description must be understandable without conversation and remain Portuguese. Run:

```sh
python <project-slices>/scripts/manage_study.py prepare .flow/slices-study.json .work/slices-study-plan.json --input-check .flow/slices-input-check.json --preview slices/study.md --actor "<tech lead>" --at "<ISO-8601>" --reason "<motivo>"
```

The helper derives exactly `[DEV] <título completo do item pai> - Estudo: <assunto>`, preserving parent tokens. Provisional identity remains only in state and `slices/study.md` preview. Show full preview/hash. Approval is specific to that hash and exclusively the tech lead's:

```sh
python <project-slices>/scripts/manage_study.py approve .flow/slices-study.json --actor "<tech lead>" --at "<ISO-8601>"
```

**Complete when:** question, expected result, bound, native fields, description and hash were presented, and approved state contains current-revision tech lead approval.

## Publish without duplication

Run `begin-create` before `redmine_create_issue`, then `finish-create`. Uncertainty requires complete `project-slices-study` search among open/closed children and `observe-create` before retry. Reconciled creation retains `remote_id`; another run never calls MCP again for this Study.

```sh
python <project-slices>/scripts/manage_study.py begin-create .flow/slices-study.json --at "<ISO-8601>"
python <project-slices>/scripts/manage_study.py finish-create .flow/slices-study.json --attempt 1 --outcome completed --issue-id 501 --at "<ISO-8601>"
```

After creation/reconciliation, reread parent/Study with complete fields/relations into `.work/slices-study-readback.json`, then:

```sh
python <project-slices>/scripts/manage_study.py complete .flow/slices-study.json --readback .work/slices-study-readback.json --at "<ISO-8601>"
```

Readback has `parent`/`study`. The helper requires approved content/native fields, reconciled ID, complete relations and original parent execution status. Only then atomically write confirmed state and `tasks/study-<id>-<slug>/task.md`; exclude operational status, assignee/dates. Existing same-type/ID directory fixes/reuses slug. Failure, ambiguity, divergence or incomplete readback retains resumable state only without canonical directories.

State becomes `awaiting-result`: slicing remains in progress/paused for evidence. Neither prepare ordinary DEV/QA publication nor mark parent/scope completed.

**Complete when:** creation is reconciled once, full readback preserves parent status, ID/slug are durable, `task.md` has stable identity/content only, and no future child was anticipated.

## Record result and resume

Without a result, `resume` refuses progress. With a result, save `.work/slices-study-result.json` containing `study_remote_id`, `result`, `source` (`kind`/`reference`), `authored_by`, `authored_at`; run `record-result` with recorder/time. The helper binds evidence to question, bound, approved revision, remote ID and source bytes.

Prepare a complete new `.work/slices-proposal.json` and run:

```sh
python <project-slices>/scripts/manage_study.py resume .flow/slices-study.json .work/slices-proposal.json --slices-state .flow/slices-state.json --input-check .flow/slices-input-check.json --actor "<tech lead>" --at "<ISO-8601>" --reason "<como o resultado orientou a revisão>"
```

The helper incorporates `study_evidence`, appends an immutable revision using the ordinary slicing semantic basis and leaves `slices-state.json` proposed. Show rendered proposal and resume ordinary approval; exceptional Study approval does not approve decomposition.

Study is evidence for new slicing, not Ralph-executable work: its directory receives only `task.md`; `planning.md` remains exclusive to ordinary DEV.

On later ordinary publication, child discovery shows Study again to the tech lead. Preserve ID/baseline as existing `keep-external`; it occupies no decomposition DEV key and QA-only still requires full `existing` coverage.

**Complete when:** attributed result/source stay intact, new revision cites them explicitly and no ordinary approval is valid before the tech lead's new decision.
