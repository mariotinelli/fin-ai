# External dependencies and refinement

Use when a DEV slice can start only after another Feature delivers a capability. This configures blockers rather than declaring implementation. Feature→Feature relations published by `project-flow` remain that workflow's responsibility and serve only as graph evidence.

## Record in slicing

For every capability genuinely preventing DEV startup, fill `external_blockers` with stable key, supplier Feature, capability, reason and specific supplier-slice issue when published. Consult the external Feature/children through MCP before proposing: select only children delivering that capability; without children, leave slice fields null and propose the parent as provisional blocker. Do not duplicate supplier implementation in the dependent slice.

**Complete when:** each blocker truly prevents startup, has one capability owner and uses available slices or explicitly justifies a provisional edge.

## Prepare and approve relations

After dependent-child publication readback, read all issues/relations in the relevant blocking graph through MCP. Save a sanitized `.work` snapshot with `scope: "relevant-blocking-graph"`, `complete: true`, project, issues (`id`, `parent_issue_id`, `title`) and native relations. Include outside relations to detect cycles and preserve them.

Collect reachable endpoint relations and children of every supplier Feature through MCP until no new issue appears; only then mark `complete: true`. Build `.work/slices-dependencies-plan.json` with `graph_snapshot` and `changes`. Each change supplies `key`, `action`, `dependency_key`, `source_issue_id`, `target_key` and `relation_id` (null for additions). Prepare:

```sh
python <project-slices>/scripts/manage_dependencies.py prepare .flow/slices-dependencies.json .work/slices-dependencies-plan.json --slices-state .flow/slices-state.json --publication-state .flow/slices-publication.json --actor "<tech lead>" --at "<ISO-8601>" --reason "<motivo>"
```

Show delta, coverage and returned hash in Portuguese. Only after explicit confirmation run:

```sh
python <project-slices>/scripts/manage_dependencies.py approve .flow/slices-dependencies.json --actor "<tech lead>" --at "<ISO-8601>"
```

Present hash, complete coverage and exact delta. Corrections before the first operation create an append-only revision and invalidate previous approval. Only the tech lead approves; plan, source or graph changes require a new preview and approval.

**Complete when:** current revision covers all `external_blockers`, is acyclic in the complete graph and has valid approval bound to its current hash.

## Apply and resume

Run `begin` before MCP and `finish` afterward for every change. `begin` returns exact tool/payload: additions use `redmine_create_relation`; removals use `redmine_delete_relation` with native ID. For refinement, complete/verify all specific relations before removing the provisional one. Removal is accepted only for the exact provisional relation created/reconciled by this state; parent/third-party relations stay intact.

```sh
python <project-slices>/scripts/manage_dependencies.py begin .flow/slices-dependencies.json --key "<mudança>" --at "<ISO-8601>"
python <project-slices>/scripts/manage_dependencies.py finish .flow/slices-dependencies.json --key "<mudança>" --attempt <n> --outcome completed --relation-id <id-apenas-para-add> --at "<ISO-8601>"
```

Unknown results or interruption require a fresh complete read and `observe` before retry. For add, `matched` completes and `absent` permits retry; for remove, `absent` completes and `matched` permits retry. Divergence returns to the tech lead.

**Complete when:** approved delta operations are reconciled, attempts/observations remain append-only and ambiguous calls are never retried without reading.

## Verify

Reread the complete graph, save the snapshot in `.work` and run `complete --readback`. The helper requires new edges, absence of the exact removed provisional relation, preservation of unaffected initial relations and an acyclic graph. `manage_scope` retains sliced/published Feature status but shows separate `dependency_status`: `pending`, `refining` or `ready`. `ready` means verified configured relations only, not implemented capability or automatic startup clearance.

**Complete when:** state is `completed`, readback/hash are durable in history, and implementation clearance remains based on actual capability state.
