# Sequencing by version blocks

Use this contract for every new publication using `sequencing_policy: blocks-v1`, including Feature/Bug DEV, QA-only deliveries, exceptional Studies and later revisions. One `Sequencing` custom field orders child work across the selected project/version. The parent mirrors its block's first position and consumes no extra slot; QA receives its own final position. The catalog keeps the preferred Feature order before numeric allocation.

## Prepare the block in the complete preview

Read the canonical requirement's policy. New runs inherit `blocks-v1`; absence identifies historical behavior, not permission to drop the policy from a new run. Never convert an approved historical payload during resume. Existing unnumbered/adopted children require explicit migration outside this delivery rather than silent backfilling.

Resolve the field by name through project metadata; retain its returned ID and format. Confirm applicability for the parent and child trackers. If unavailable, ambiguous, incompatible or required during parent creation, expose the configuration obstacle instead of choosing another field, creating configuration or inventing a provisional number.

Through MCP, read **all** issues for the confirmed project and selected `fixed_version_id`, with `status_id: "*"`, following every page. Fetch complete issues when custom fields are omitted. Store a sanitized `.work/slices-sequencing-snapshot.json`:

```json
{
  "server": "https://redmine.example",
  "project": {"id": 7, "issue_custom_fields": [{"id": 37, "name": "Sequencing", "field_format": "int"}]},
  "version_id": 9,
  "status_scope": "all",
  "pages": [{"offset": 0, "limit": 100, "count": 1}],
  "total_count": 1,
  "issues": [{"id": 123, "project": {"id": 7}, "fixed_version": {"id": 9}, "tracker": {"id": 2}, "status": {"id": 1}, "custom_fields": []}]
}
```

Use the selected instance's canonical base URL consistently as `server`. The example illustrates shape only: real snapshots contain complete issue objects. Include journals for issues that could be shifted, proving their not-started state. Missing pages, nonblank invalid numbers or out-of-scope records block calculation. Historical duplicate values remain occupied; they are not repaired automatically.

Add to the ordinary publication, Study or revision-application plan:

```json
"sequencing": {
  "snapshot": ".work/slices-sequencing-snapshot.json",
  "managed_publications": []
}
```

The helper computes numbers; do not supply hand-written assignments. New blocks start after the largest occupied positive integer across all trackers/statuses, without filling gaps. DEV order must respect the approved dependency order; QA comes last. A QA-only parent occupies one position. Allocate scope items in approved catalog order; incompatible cross-Feature dependencies return to slicing rather than silently interleaving blocks.

The generated preview shows destination, field ID, range, each child and every numbering update. Include it in the existing complete-preview decision with the same tech lead/authority; no separate repeated confirmation is needed. Parent status, content and unrelated custom fields remain preserved. Numbered publication/Study states use v3; older states retain their original shapes, hashes and payloads.

**Complete when:** the exact block and all updates are included in the authorized preview, the destination/field evidence is complete, and parent/child ownership and dependencies are reconciled.

## Expand only with explicit numbering review

For an existing new-policy block, preserve its children and Study positions. Revision application derives existing keys and inserts new DEV before an unstarted integrated QA, or uses a newly approved QA when the previous one is protected. Canceled positions remain occupied.

When later blocks must move, list their canonical absolute `.flow/slices-publication.json` paths in `managed_publications`. The helper verifies new-policy ownership and includes the current completed revision application when present. Only issues whose native New status and complete journals prove they never started may shift. External, started or completed issues block the expansion. Parent anchor changes and all affected child numbers must appear in the preview. A published requirement is not proof of implemented work or available positions.

For revision application, `sequencing` is mandatory whenever the source publication is numbered. Numbering updates are distinct from functional content changes and preserve the existing task-specific approval requirements. Completed publications keep their original approval/payload history; authorized numbering-only receipts and archived prior states account for changed canonical task metadata.

**Complete when:** every shifted issue is owned, demonstrably unstarted and explicitly included in the approved delta; protected issues retain their numbers or the proposal stops with the actual conflict.

## Publish, reconcile and release

Before writes, refresh the complete version snapshot. Run the numbering updates in generated order with the appropriate helper (`manage_publication.py`, `manage_study.py` or `manage_revision_application.py`):

```sh
python <helper> begin-numbering <state> --index 0 --snapshot <fresh-snapshot> --at "<ISO-8601>"
python <helper> finish-numbering <state> --index 0 --attempt 1 --outcome completed --at "<ISO-8601>"
```

`begin-numbering` returns the exact `issue_id` and `changes` for `redmine_update_issue`. Record each outcome. An uncertain/in-flight response requires `observe-numbering --index N --snapshot <fresh-snapshot> --outcome matched|absent --at ...` before retry. Never recalculate an approved number to conceal a collision or repeat a completed update.

After numbering updates, create children normally, adding `--sequencing-snapshot <fresh-snapshot>` to each `begin-create` (or revision `begin`). Creation payloads contain the assigned custom field. Standard stable-identity reconciliation also checks this value. Studies allocate one early child slot; the parent remains unnumbered until full slicing incorporates the Study. Keep the scope item incomplete until the Study result and complete decomposition are approved.

Add `--sequencing-snapshot <fresh-snapshot>` to final `complete`. Readback verifies every assignment, the parent anchor, collision-free target positions and preservation of unrelated fields. Only then materialize Sequencing in `task.md` and reconcile numbering-only artifact/history updates atomically.

The shared Git administrative directory contains a persistent lock keyed by server/project/version. Same-workspace publications serialize; interruption retains ownership for the same state/plan. External writers are detected by fresh snapshots and final collision checks, not by a distributed transaction. Preserve work and reconcile on conflict. If execution stops after verified completion but before releasing the lock, `release-numbering <state>` releases only that completed publication's own lock. Pending work must resume; do not delete locks to bypass it.

**Complete when:** all operations and custom-field values are verified, protected fields/history remain intact, canonical metadata matches the approved numbers, and the publication's lock is released.
