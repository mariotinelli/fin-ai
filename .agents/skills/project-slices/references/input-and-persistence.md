# Input and local persistence

## Layout

Preserve canonical `project-flow` layout: `feature.md` or `bug.md` remains the parent's only root requirement document. Use:

- `.work/slices-remote.json` for disposable sanitized Redmine read snapshots;
- `.flow/slices-input-check.json` for durable functional-verification evidence;
- `.work/slices-proposal.json` for the current unrecorded proposal;
- `.work/slices-existing-children.json` for disposable sanitized existing-child pagination;
- `.flow/slices-state.json` for durable revisions, hashes and approvals;
- `.flow/slices-divergence.json` for material corrections, tech lead decision, local/remote alignment, attempts and readback;
- `.flow/slices-change-review.json` for append-only semantic comparison of current requirement and published baseline;
- `.flow/slices-revision-application.json` for authorized delta, per-task approvals, attempts, observations and readback;
- `slices/slices.md` for the current human-readable preview;
- `slices/condicoes-teste-r<revision>.docx` for the local document generated from approved structured source, preserving previous revisions;
- `slices/divergence.md` for exact correction/impact presented before parent alignment;
- `slices/change-review.md` for classification, localized impact and still-valid items;
- `slices/revision-application.md` for concrete mutation/preservation preview;
- `.flow/slices-publication.json` for final review, approval, IDs, attempts, observations and completion;
- `.work/slices-sequencing-snapshot.json` for fresh complete project/version occupancy evidence; v3 publication/Study states embed the approved block and numbering operations under [Sequencing](sequencing.md);
- `.flow/sequencing-history/<sha256>.json` for immutable prior states supporting approved numbering-only changes; canonical artifacts change only after verified readback;
- `.flow/slices-condition-revisions.json`, `.flow/condition-evidence/` and `slices/conditions-revision-rNNN.md` for immutable history/previews of [localized condition revisions](condition-revisions.md), without rewriting original publication;
- `.flow/slices-reconciliation.json` and `slices/reconciliation.md` for exact preview/decision on local materialization of historical publication;
- `.flow/slices-dependencies.json` for external-dependency revisions, approvals, operations and readbacks;
- `slices/publication.md` for the approved final preview;
- `tasks/dev-<id>-<slug>/task.md`, `tasks/qa-<id>-<slug>/task.md` and `tasks/study-<id>-<slug>/task.md` for canonical representations created only after complete readback of their workflow.

Reject symlinks in every written path. Stage candidates in the same directory and replace atomically only after validation. Preserve previous state for transition validation; revisions/approvals are append-only. Human-facing artifacts and explanations remain in Portuguese.

## Parent verification

The helper accepts `project-flow` states v2–v5, but input must be Feature/Bug, `completed`, with `redmine.issue_id`, valid `requirement` approval and no pending divergence. Sanitized snapshots are structured issue responses restricted to verifier-required public fields (`id`/`issue_id`, `subject`, `description` and, when present, `status`, `status_id`, `relations`). Include no headers, credentials or MCP configuration. Abbreviated example:

```json
{
  "issue": {
    "id": 123,
    "subject": "[WEB] [OPERACIONAL] Gestão de Usuários",
    "description": "<!-- project-flow:start -->...<!-- project-flow:end -->"
  }
}
```

Without Redmine, validate local document/state, inspect code and prepare sources, evidence, conditions and candidate in `.work` only. Do not create `slices-state.json`, approval or artifacts claiming remote alignment. Unavailability blocks verification/publication, not local analysis. Preserve the candidate for resume and identify pending verification; once access returns, retrieve a new snapshot, run `check-input` and revisit only what comparison invalidates.

Run:

```sh
python <project-slices>/scripts/manage_slices.py check-input <feature-dir> --remote .work/slices-remote.json --output .flow/slices-input-check.json --at "<ISO-8601>"
```

The agent retrieves remote projection; the script compares identity, title and managed functional sections without calling the API. Divergent content, attribution or delimiters block proposals. Structural validation does not prove readability or semantic slicing quality; apply discipline/evaluation scenarios before approval.

When `.flow/slices-divergence.json` exists, `check-input`, approval and child publication stay blocked until `completed`, with current local correction and verified remote readback. `pending`, `rejected`, `approved`, `local-aligned` and `aligning` are resumable but authorize no children.

## Proposal and approval

Create `.work/slices-proposal.json` under `schemas/slices-state.schema.json` and field examples in `templates/slices.md`. Proposal contains `feature`, `inspection`, `requirements`, `slices`, `coverage`, `decisions` and, for new proposals, `test_conditions`. Prepare the latter under [test conditions and local DOCX](test-conditions.md); persisted revision is durable structured source. Record/render:

When a design applies, use these same fields for approved visual criteria and adaptations: `requirements` retains their canonical IDs, `coverage` assigns ownership, and `description.visual_references` is a nonempty string array naming source IDs, repository-relative normalized paths and screen/state locators. Both preview and DEV publication render that optional field under `Referências`; omit it for tasks without applicable design. Keep comparison conditions and source locators in `test_conditions` so rendered preview, QA, DOCX and materialized `task.md` retain them. Record approved adaptation provenance in existing `decisions`; no new operational manifest is needed. Semantically compare rendered descriptions and conditions with the visual sources before requesting approval; structural coverage alone cannot establish visual completeness. Historical descriptions without the optional field remain readable and are not rewritten on resume.

```sh
python <project-slices>/scripts/manage_slices.py record-proposal .flow/slices-state.json .work/slices-proposal.json --input-check .flow/slices-input-check.json --actor "<tech lead>" --at "<ISO-8601>" --reason "<motivo da revisão>"
python <project-slices>/scripts/manage_slices.py render .flow/slices-state.json slices/slices.md
```

`record-proposal` is the first step making a candidate durable and requires current remote `input-check`. Offline candidates gain no authority and cannot bypass verification.

For new proposals, `record-proposal` rejects any slice above six hours and requires `estimate_exception: null`; that field exists only for historical reading. Publication applies the same ceiling to QA, and Study applies it to the exceptional child. Source estimates do not enter calculations or evidence supplied to estimating agents.

Each `record-proposal` appends an immutable revision and invalidates current approval. After explicit tech lead confirmation, preserve previous state and run:

```sh
python <project-slices>/scripts/manage_slices.py approve .flow/slices-state.json --actor "<tech lead>" --at "<ISO-8601>"
python <project-slices>/scripts/manage_slices.py validate .flow/slices-state.json --previous <estado-anterior.json>
```

`approve` rereads approved requirement/state and checks title, identity and paths against `input-check`; changes require fresh verification/proposal. `technical_context` may be omitted/null; include text and render the section only when an approved decision requires it.

**Complete when:** approved revision, Markdown preview, hash and attribution survive in versionable files outside `.work/`, and no earlier revision changed.

Generate local DOCX from approved revision under [test conditions](test-conditions.md). Generation neither changes QA description nor authorizes file publication.

Then follow [DEV and QA publication](publication.md). Plan/remote snapshots stay disposable in `.work/`; state, approvals and progress remain in `.flow/`, and preview stays in `slices/` until canonical ID-based materialization in `tasks/`.

For completed historical v1 publication, follow [local reconciliation](legacy-reconciliation.md) instead of preparing/repeating remote operations.

## Operational state and resume

Helpers persist/validate local progress; keep this maintenance internal. Record product decisions and sources once rather than copying the conversation. New scope states omit `awaiting_decision_for`, `continuation_decisions` and `resumes`; historical records remain readable/preserved. `resume` reconciles progress and selects the first eligible item without new continuation confirmation. Pauses/obstacles preserve reasons needed to resume. IDs, content revisions, uncertain operations and publication evidence remain durable; resume does not authorize repeating remote mutations.

**Complete when:** the helper validates persisted state, preserves verified publications and selects the next eligible item or retains the actual obstacle.
