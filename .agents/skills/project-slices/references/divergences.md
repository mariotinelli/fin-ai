# Material divergences and parent alignment

Use when inspection finds a material difference among approved parent requirement, proposed children and intended description. A new API is always material when the approved requirement promises no consumable API. The tech lead alone decides; they may consult the requirement owner, but this creates no second approver or QA gate.

## Prepare the exact correction

In `.work/slices-divergence-plan.json`, save the proposed corrected canonical document, fresh sanitized parent snapshot, slice proposal exposing the difference, every divergence's approved meaning, proposed correction, impact, all affected children and publication effect. Run:

```sh
python <project-slices>/scripts/manage_divergence.py prepare .flow/slices-divergence.json .work/slices-divergence-plan.json --feature-dir . --preview slices/divergence.md --actor "<tech lead>" --at "<ISO-8601>" --reason "<motivo>"
```

Show complete `slices/divergence.md` in Portuguese. The preview includes functional delta, affected children and resulting remote description, preserving content outside delimiters, status and baseline relations.

**Complete when:** every material difference has a specific correction/impact, affected-child coverage is exact and presented hash binds sources, baseline, correction and remote payload.

## Decide

Record `decide --decision rejected` or `decide --decision approved` with actor, time and reason. Rejection preserves requirement/parent bytes and blocks affected publication. Approval authorizes only correction/payload bound to the current hash.

**Complete when:** exactly one tech lead decision exists for the current revision; optional consultation introduced no additional gate.

## Align local and remote

After approval, run `apply-local`. The helper invalidates prior approval, appends new requirement approval and replaces document, state and alignment record as one local transaction. Then run `begin-update`, send only its payload to `redmine_update_issue`, record outcome with `finish-update` and always read back through `observe-update`.

Uncertain outcomes require reading. `matched` completes without another write; `baseline` proves absence and permits retry of the same payload. Any third description or changed status, relations, subject, source, evidence or approval blocks progress. Completed operations never return to MCP.

**Complete when:** corrected local requirement has valid new approval, remote parent exactly matches approved payload, status/relations match baseline and history records attempts/evidence without rewriting.

## Resume children

Rerun `check-input`, rebuild the proposal with the new hash and obtain ordinary decomposition/publication approvals. Pre-alignment approvals do not authorize changed children. Studies, adopted/external children remain historical and follow existing contracts.

**Complete when:** proposal, input check and both ordinary approvals reference corrected source; no affected child uses previous authority.
