# Redmine preflight diagnostics

Use the session's discovered tools and sanitized read responses as evidence. Connection, capability availability, and Redmine authentication are separate checks. Apply checks only to the next remote operation. Local intake, clarification, drafting, state validation and lock recovery remain available without Redmine.

## Required capabilities by operation

All remote operations use the connected MCP exclusively. Helpers remain local and never read credentials or call Redmine HTTP APIs.

| Next operation | Discover and verify |
| --- | --- |
| Local understanding, normalization, draft or resume inspection | No Redmine tools |
| Resolve context | `redmine_get_context`, `redmine_get_project`, `redmine_list_versions`; `redmine_list_projects` only for an unresolved or ambiguous destination |
| Similarity or Feature sequence search | Context checks plus `redmine_search_issues` filtered by the selected `fixed_version_id`; `redmine_get_issue` for missing details |
| Creation preparation | Context checks plus `redmine_list_trackers`, `redmine_list_statuses`, `redmine_list_categories`; selected open version, project metadata and sequence reads when applicable |
| Create an approved issue | Context checks plus `redmine_create_issue` and `redmine_get_issue` for readback; search for recovery if the outcome is unknown |
| Publish or align an existing issue | Context checks plus `redmine_get_issue` and `redmine_update_issue` |
| Publish an approved relation | Context checks plus `redmine_get_issue` for endpoints and existing relations, and `redmine_create_relation` |

Discover schemas as well as tool names. Positive discovery of every capability needed now is enough; an absent relation tool cannot block a demand without relations. Immediately before a mutation, call `redmine_get_context`, read the selected project and any existing target issue/endpoints, and compare server, authenticated user and destination with the intended context and exact approved payload. Reuse explicit conversation selections without asking for the same confirmation again. Resolve missing context or mismatches before writing. Never probe write access through a mutation.

For every fresh flow, call `redmine_list_versions` for the verified project. Retain only entries whose returned `status` is `open`, present all of them with ID, name and available date/description metadata, and ask the user to choose one. Persist the attributed selection as `redmine.version`. An empty open-version list blocks item creation and publication; never substitute a closed or locked version or create one. On resume, preserve the recorded selection and verify that its ID still belongs to the intended project before mutation. If its status changed, report that change and request a new explicit selection.

**Complete when:** the current operation has its required schemas and successful read checks, or its specific unmet prerequisite is recorded without discarding local work.

## Diagnose and recover

- **Incomplete discovery:** search deferred tools through the host's available discovery mechanism and inspect exposed names, descriptions, and schemas, accounting for namespace prefixes. For paginated `tools/list` or host-equivalent results, pass each returned `nextCursor` or continuation token into the next request, accumulate every page, and stop only when the token is absent or empty. When only host search is available, search each unresolved required capability by exact name and then operation name, inspecting the returned schemas. Once every required capability is confirmed, continue with the authentication and reads required by this operation; a full inventory of unrelated tools is unnecessary. If required capabilities remain unresolved after these searches and the host cannot provide the full inventory, report discovery as incomplete, identify the unresolved capabilities and the attempted searches, and request the missing discovery access. A search response without a cursor is not proof of an exhaustive server inventory. Do not assert that a tool is absent based on a first page, page-size count, partial search result, or any other partial list.
- **Connected but missing a required capability:** identify the exact capability missing from the complete inventory. Explain that the MCP is connected but does not expose that operation. For example: “O MCP Redmine está conectado, mas a lista completa de ferramentas desta sessão não inclui `redmine_create_relation`, necessária para publicar esta relação.” Refresh or reconnect the server if the executable was already updated; otherwise update the Rem Soft Tools executable used by the host and run `remsoft install:mcp`, then reconnect and repeat discovery. Reinstalling configuration alone does not update an old executable. Tool count alone cannot identify a missing operation or prove an outdated version.
- **Server absent or disconnected:** report the observed connection state. Use `remsoft install:mcp` when configuration is absent; inspect the host's sanitized connection error when configured but disconnected.
- **Authentication rejected:** recommend `remsoft redmine login` only when the tool reports a missing, expired, or rejected session. Never request or display credentials.
- **Identity missing or a read failed:** identify the specific probe and sanitized error. A permission, network, or server error requires its own correction; do not prescribe login or reinstallation without evidence.

Report blockers in pt-BR with the operation, failed check, sanitized evidence, specific corrective action, saved artifact paths and next incomplete step. Preserve sources, drafts, attributed answers, approvals and operation history. Keep the current phase incomplete; record the impediment in human history without inventing a remote attempt when no call occurred. Continue independent local preparation.

After connection returns, validate existing state and verify only the pending operation. Fill previously null context from successful checks, validate the transition with `--previous`, and preserve UUIDs, lock key, source files and answers. Reconcile unknown outcomes before retrying; a recorded issue ID or completed create operation prevents another create. Never test write capabilities by creating or modifying remote data.

**Complete when:** the blocked operation can safely resume from retained state, or the precise remaining impediment is reported with all local progress preserved.
