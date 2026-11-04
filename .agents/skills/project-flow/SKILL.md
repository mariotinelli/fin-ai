---
name: project-flow
description: Turn readable conversation, file, URL, image, or design evidence into an approved Feature/Bug catalog or canonical requirements with recoverable Redmine projections. Use for new-scope and new-issue work, including multi-item scope completion, safe pause, resume, catalog revision, relations, publication alignment of completed items, and partial-failure reconciliation; this flow does not edit an existing issue as a new demand.
---

# Project Flow

Respond in Brazilian Portuguese (pt-BR) from the first announcement, including questions, progress, preflight diagnostics, approval previews, final summaries, and authored requirements in local artifacts and Redmine. Translate prose from skill instructions, references, and tool diagnostics when explaining or citing it to the user, including excerpts used to justify an approval request or blocker; identify translated quotations as translations. Preserve technical identifiers, schema keys, commands, and file paths. Keep original source evidence verbatim in its evidence artifacts; when the user requests an exact quotation, include the original with a translation. Apply this language choice when invoking the supporting disciplines unless the user explicitly requests another language.

Deliver approved requirements: `new-scope` discovers an ordered Feature/Bug catalog and completes every item in that order; `new-issue` handles one Feature or Bug. The local Markdown is canonical; Redmine preserves its approved functional content through the [checked projection](references/redmine-publication.md). Product decisions belong to the user, and implementation decisions belong to later roles.

## Understand and recover locally

For an explicitly requested local artifact organization, follow [artifact organization](references/artifact-organization.md) instead of demand intake.

Read and clarify the demand immediately, including when Redmine is unavailable. Reuse project and identity already determined in the conversation; ask only about missing information or relevant ambiguity. A remembered selection identifies intent, not proof of current remote access. Keep an uncertain destination unresolved.

Before creating files, look for matching incomplete state under `docs/harness/.runs/`, `docs/harness/features/`, `docs/harness/bugs/`, and `docs/harness/scopes/`, checking legacy root states and `.flow/` states. Exclude `.work/` candidates and reconcile duplicate states for the same identity. Read the demand and existing local history to match the run without a network gate. For a match, follow [pause and resume](references/pause-resume.md), validate state, and acquire or explicitly recover its lock. Retain sources, answers, drafts, UUIDs, item IDs and completed operations.

For a fresh run, use the confirmed project and intended artifact identity as the stable lock key when available; otherwise use the intended repository-relative staging/scope folder. Keep this key after remote context is resolved and after issue creation. Acquire the lock before the first write and follow [the artifact contract](references/artifact-contract.md). New requirement v5 and scope v3 permit `identity: null` and `redmine: null` during local preparation; never invent remote IDs or an authenticated identity. Preserve known selections and their provenance in human history until verified. Retain v2-v4 requirement states on resume.

**Complete when:** the requested path and available context are understood, exactly one run is selected, and this execution owns its lock before writing.

## Verify only the next remote operation

Local source intake, clarification, repository inspection and drafting need no Redmine capability. Before a remote read or mutation, follow [operation-specific Redmine checks](references/redmine-preflight.md), using the host's tool discovery/search when tools are deferred. Discover only capabilities needed by that operation: `redmine_get_context` and its reads/writes; every fresh flow requires `redmine_list_versions`; `redmine_create_relation` is required only for a planned relation mutation.

Reuse the selected project and identity. Resolve an explicit project directly; list projects only when selection or disambiguation needs it. For every fresh `new-issue` or `new-scope` flow, list that project's open versions and ask the user to select one before item work; a scope makes one selection inherited by all its items. Read tracker, initial-status and category metadata when preparing the complete preview. Include grounded mapping proposals in that preview; ask separately only about material ambiguity. Before every mutation validate current connection, authenticated identity, selected version and the exact destination against the intended context and approved payload. A mismatch blocks that mutation for resolution, without silently replacing recorded context.

On failure, preserve local work and the first incomplete phase/operation, report the specific sanitized impediment and the saved paths, and continue independent local work. An unavailable remote operation is not a reason to restart intake or discard a draft. On reconnection, verify the required operation and reconcile any unknown outcome before retrying; unchanged payload approvals and completed operations retain their existing recovery rules.

**Complete when:** the next remote operation's capabilities, authenticated identity and destination are verified, or that operation is explicitly blocked with local progress preserved.

For an explicitly requested publication alignment of a completed item created by this flow, follow the completed-publication branch in [the Redmine projection contract](references/redmine-publication.md). Verify only its required reads and update; preserve the completed catalog and interview.

## Run the selected path

Now read [the source intake contract](references/intake.md) and [the artifact contract](references/artifact-contract.md) before the first local write. Follow its storage and retention policy for every generated file; prepare new directories with `manage_artifacts.py`. For `new-scope`, read [the new-scope workflow](references/new-scope.md); for `new-issue`, read [the shared item workflow](references/new-issue.md). Both paths route the selected item through that same shared Feature or Bug cycle. Read [the design contract](references/design-inputs.md) only when an input is presented as a design or design evidence. Read [the Redmine projection contract](references/redmine-publication.md) before preparing either remote write.

Invoke `requirements-grilling` for a `new-issue` interview before creation by default. For `new-scope`, follow the catalog-first interview gate in `references/new-scope.md`: approve the complete catalog, select its next eligible item in the approved preferred order, and interview that item before its combined requirement/publication preview. Creation before interview is an explicit user-requested exception. One approval covers the complete requirement and operations shown in the preview; retries reuse unchanged authorization. Invoke `domain-modeling` only if the interview resolves a reusable canonical term or exposes a genuine architecture candidate under that skill's triggers.

**Complete when:** `new-issue` validates at `completed`; or `new-scope` validates at `completed` with every active item completed respecting real dependencies, every relation and remote operation reconciled, every approval and validation recorded, no open functional gap or undecided candidate, and a final summary. The scope request authorizes continuing between eligible items; show progress, honor user pauses immediately, and retain product decisions and publication approvals. Follow the eligibility and resume rules in `references/new-scope.md`.

## Boundaries

Access Redmine exclusively through the connected MCP. Local scripts only validate or transform artifacts; they never call the Redmine HTTP API or read credentials.

Requirement approval and flow completion are local workflow milestones. Publication preserves the current Redmine issue status; follow the publication contract for the exact update payload and legacy mappings.

This flow never edits an existing issue found by similarity search or creates categories. It never creates commits, technical tasks, architecture decisions, or extra issues automatically. Closing, canceling, relating, or otherwise mutating Redmine always consumes an explicit recorded approval; a retry may reuse an approval only when its payload fingerprint is unchanged.
