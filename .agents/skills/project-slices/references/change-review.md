# Requirement-change review

If the requirement is unchanged and adjustments concern only published conditions/DOCX, follow [localized condition revision](condition-revisions.md). It neither changes decomposition baseline nor replaces this analysis when requirements change.

Use when the current approved parent requirement's SHA-256 differs from the source of completed publication. First read [semantic-change discipline](../../vertical-slicing/references/semantic-changes.md). This workflow records analysis/decision rather than implementing general task-update/removal policy.

## Prepare the plan

Confirm approved `slices-state.json`, completed `slices-publication.json` and matching `semantic_baseline` in both. Read current requirement/approval under the `project-flow` contract. Build `.work/slices-change-review-plan.json` with `classification`, `summary`, `changes` and `impact`. Each change has `id`, `classification`, `before`, `after`, `rationale`. Impact contains `affected_*`/`unaffected_*` lists for `tasks`, `acceptance_criteria`, `coverage`, `dependencies`; entries have `id` and `reason`, fully partitioning baseline.

When publication already has this workflow's conditions, with/without DOCX, also include `affected_test_conditions`/`unaffected_test_conditions` by stable ID. Use conditions from the latest **completed** revision, including earlier localized adjustments; pending/rejected proposals are not current. Resolve document publication with remote progress before opening another analysis.

Then require `conditions: {"requirements": [{"id": "R1", "summary": "..."}], "additions": [{"id": "CT-003", "reason": "..."}]}`. `requirements` represents the current approved requirement; `additions` lists proposed new conditions only and may be empty. Partition all current conditions, identifying still-valid, changed and removed ones. Preserved conditions must reference existing requirements. Discuss new, contradictory or ambiguous behavior in the requirement before approval; hashes and structural references do not prove semantic equivalence.

Run:

```sh
python <project-slices>/scripts/manage_change_review.py prepare .flow/slices-change-review.json .work/slices-change-review-plan.json --slices-state .flow/slices-state.json --publication-state .flow/slices-publication.json --current-requirement feature.md --preview slices/change-review.md --actor "<tech lead>" --at "<ISO-8601>" --reason "<motivo>"
```

The helper derives a stable parent/two-version identity, includes preservation evidence for published children, adoption/externality decisions, Studies, divergences and dependencies, and reuses the revision on identical resume. Show the full Portuguese preview separating localized impact from still-valid items.

Each requirement version/approval has immutable copies; only the current revision must match current files. Later changes append revisions without deleting decisions. After completed application, also include its created children/relations in impact.

**Complete when:** semantic comparison covers every difference and every baseline item appears exactly once as affected/unaffected, with readable preview and intact hashes.

## Decide

Only the tech lead who approved slicing decides. Record `approved` or `rejected`:

```sh
python <project-slices>/scripts/manage_change_review.py decide .flow/slices-change-review.json --decision approved --actor "<tech lead>" --at "<ISO-8601>" --reason "<motivo>"
```

While pending/rejected, preserve publication, current document, IDs, approvals and history. Approved editorial change is recorded without invalidating children or requiring reslicing. If all conditions remain valid, preserve current artifacts with their original requirement identity; the semantic decision records validity against the updated requirement. This case generates neither upload nor current-version note.

**Complete when:** one decision references the current classification/impact hash; pending/rejected states changed no published artifact.

## Release affected content only

For approved functional change, request local authorization of affected keys before preparing mutations:

```sh
python <project-slices>/scripts/manage_change_review.py authorize .flow/slices-change-review.json --keys "dev-1" --at "<ISO-8601>"
```

The command fails if baseline, requirement, classification, impact or approval changed; identical resume reuses authorization without duplication. It neither calls MCP nor updates/removes tasks. Then prepare revisions/approvals bound only to affected content, preserving unaffected IDs/evidence.

With documented conditions, follow [conditions after requirement change](requirement-condition-revisions.md) to prepare source/delivery format linked to this decision and include them in the concrete application preview. Affected/new condition IDs from semantic review bound the document delta; task authorization does not release unrelated condition changes.

**Complete when:** authorization references approved semantic review, contains affected keys only and this phase created no remote operation.
