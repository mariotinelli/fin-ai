# Local reconciliation of historical publications

Use only when DEV/QA v1 publication or Study v1 completed creation/adoption but retains a historical positional representation rather than `tasks/<type>-<id>-<slug>/task.md`. It materializes a local projection; remote mutations are outside this branch, and historical state, descriptions, hashes, approvals, attempts and baselines remain byte-for-byte unchanged.

## Readback and exact preview

Reread parent/every managed child with complete fields/relations through read-only Redmine tools. Save only sanitized response to `.work/slices-reconciliation-readback.json`. DEV/QA uses `{"parent": {...}, "children": [...]}` with every managed child exactly once; Study uses `{"parent": {...}, "study": {...}}`.

Run:

```sh
python <project-slices>/scripts/manage_reconciliation.py prepare .flow/slices-reconciliation.json \
  --legacy .flow/<estado-historico>.json \
  --readback .work/slices-reconciliation-readback.json \
  --preview slices/reconciliation.md
```

The helper accepts only v1 state with completed remote outcome/unambiguous ID. It validates parent, project, type, tracker, status, priority, inheritance, empty assignee/dates, estimate, title, description and relevant relations. Divergence, partial publication, missing/duplicate IDs, changed evidence, unsafe path or collision stops without task writes.

`slices/reconciliation.md` shows destinations, SHA-256 and exact Markdown bytes. Show it completely to the tech lead in Portuguese. This phase ends only when preview exists, historical-state/readback hashes remain current and no canonical directory was created.

## Current decision and materialization

After explicit approval of the current preview, run:

```sh
python <project-slices>/scripts/manage_reconciliation.py approve .flow/slices-reconciliation.json \
  --actor "<tech lead>" --at "<ISO-8601>"
python <project-slices>/scripts/manage_reconciliation.py materialize .flow/slices-reconciliation.json \
  --at "<ISO-8601>"
```

Decision references the hash combining source, readback, destinations and exact content. Before approval/materialization, the helper rereads evidence and repeats validation. Changes require preserving the record, resolving divergence and preparing another deliberate reconciliation; old approval never transfers.

Atomic writes produce the current publication's `task.md` contract. Existing same-type/ID directories retain slugs when content matches; multiple directories or different content are conflicts. Completed execution may repeat without file changes.

**Complete when:** `.flow/slices-reconciliation.json` is `completed`, each `task.md` matches approved bytes, historical files retain original hashes and no remote mutation was requested.
