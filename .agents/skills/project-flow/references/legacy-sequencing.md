# Legacy parent Sequencing

Read only when resuming a historical scope/requirement without `sequencing_policy: blocks-v1`. New flows use deferred parent numbering and version blocks from the main publication contract.

The following calculation applies **only to historical runs without `blocks-v1`**, preserving their already approved creation/retry contract. Do not add or remove the policy on resume or silently migrate existing issues.

For every new Feature, resolve the `Sequencing` issue custom field from the selected project's `issue_custom_fields` returned by `redmine_get_project`. Use the returned field ID and available format/allowed-value metadata; IDs are instance-specific. If the field is missing, ambiguous, or incompatible with the intended value, resolve that material ambiguity before creation. Present a grounded non-literal mapping in the complete preview for its approval.

Sequence numbers are independent per Redmine version. Search only issues whose `fixed_version_id` equals the selected version, include every status, and calculate the maximum from that set. Issues in another version never affect the result.

For `new-scope`, take the selected version's observed maximum before the scope starts and add the item's approved `suggested_position` in `suggested_order`, including when the catalog contains Bugs between Features. Preserve catalog spacing and the recorded baseline maximum for every item instead of recalculating against issues already created by the same scope.

For a standalone `new-issue` Feature, always calculate the next sequence from Redmine during creation preparation. Use `redmine_search_issues` for the confirmed project with `status_id: "*"` and the selected `fixed_version_id`, following `offset`/`limit` through all result pages, and read Sequencing by its resolved custom-field ID. Include closed issues and every tracker using that field; retain only issues belonging to the confirmed project and selected version. Use `redmine_get_issue` when search results omit custom-field values. Set the new value to the largest existing numeric sequence plus one: a maximum of `35` yields `36`, even if earlier numbers are unused. If no issue has a sequence in that version, start at `1`. Treat blank values as unset; an unreadable page or a nonblank invalid sequence must be resolved before calculating the maximum. Calculate automatically rather than asking the user to supply a number or accepting an arbitrary supplied value. Show the version, observed maximum and calculated next value in the creation preview; the existing exact-payload approval still applies.

Show the resolved field name, ID, value, selected version and source of the sequence in the creation preview. Include Sequencing in `redmine_create_issue.attributes.custom_fields` as `{"id": <resolved-field-id>, "value": "<approved-sequence>"}`, alongside `fixed_version_id` and any other required fields. The creation approval and payload fingerprint cover both values. Bugs use the same selected version without a Sequencing custom field.

Persist the returned issue ID and create outcome immediately, then reread the issue with `redmine_get_issue` and verify the custom field by ID against the approved sequence before the next operation. On an unknown create outcome, include Sequencing in the candidate comparison. A missing or different value is a divergence to resolve on that existing issue, never a reason to create another issue. Retries and resumed runs retain the original approved payload; a later catalog reorder does not automatically renumber created issues or change an approved retry. Final description publication preserves Sequencing.

**Complete when:** the creation preview and approved payload include the resolved Sequencing field and value, and readback confirms that value on the persisted Feature issue.

