# Ingestion

Ingestion is a reviewed workflow, not an implemented tool:

1. Preserve incoming material unchanged in [`sources/inbox/`](../sources/inbox/) while it awaits review, and record an integrity digest where practical.
2. Inspect existing records and identify referenced existing entities before proposing new IDs.
3. Create minimal persistent source metadata that identifies the raw file and records supported classification, authorship or narrator, perspective, relationship to play, origin metadata, integrity information, curator metadata, and useful locators as applicable. Omit fields the source does not need.
4. Identify candidate new entities, events, campaigns, accounts, and snapshots without assuming every name is a distinct entity, every source section is a session or event, or every session is an historical event.
5. Derive or update the smallest appropriate records, giving every factual section or meaningful block identifiable supporting sources and retaining contradiction, uncertainty, and original language. Add source locators when a whole-file link would be ambiguous.
6. Add statement-level attribution where disputes, contradictions, mixed sourcing within a section, or attribution of a particular claim require it.
7. Record curator-supplied corrections in source metadata without changing the raw source; retain both the source-stated and corrected values, and use the corrected value in derived data where applicable.
8. Review [`curation/open.md`](../curation/open.md) for existing items relevant to the new source's campaign, entities, locations, events, or other scope. For each relevant item, determine whether the new evidence resolves it, adds evidence without resolving it, requires reformulation or splitting, or has no material effect.
9. Update affected derived records and the curation queue together. Add newly discovered actionable content uncertainties to the queue when they can safely remain unresolved; do not queue ordinary unknown facts merely because they are unknown.
10. After successful review, move the immutable raw source and its metadata out of `sources/inbox/` to the permanent location defined in [`sources/README.md`](../sources/README.md). Update provenance links and verify the raw digest after the move.
11. Review the complete Git diff for unsupported or insufficiently sourced facts, accidental source edits, broken relative links, manufactured precision, and curation items inconsistent with the derived records.

## Reconsidering curation items

A new source does not resolve a curation item merely because it mentions the same subject. Resolution must follow from what the source actually establishes, interpreted according to its provenance, perspective, epistemic role, and relationship to play. Prepared GM material, for example, is not automatically evidence that a possible event occurred during play.

When new evidence resolves an item, retain its ID, original question, earlier evidence, resolution, resolving source and locator, and whether the resolution came from source evidence or a curator-supplied decision or correction. Move the complete item to [`curation/resolved.md`](../curation/resolved.md) and update affected records. If an item is reformulated or split, retain it as superseded and link its replacement IDs. Follow the lightweight process in [`curation/README.md`](../curation/README.md).

## When to ask the curator

Ingestion should normally produce useful derived records plus explicit unresolved content questions without interrupting the curator. If an ambiguity can safely remain unresolved, preserve it in the records, add or update a curation item, and continue.

Ask immediately only when the uncertainty materially prevents safe ingestion, especially when proceeding would risk a destructive or ambiguous identity decision, loss of provenance, overwriting conflicting information, or another difficult-to-reverse structural choice. The curator may later request an interactive review of open items for a particular campaign or scope after surviving sources have had the opportunity to supply evidence.

Never silently edit raw sources. Corrections or normalizations belong in source metadata or derived records with provenance, while the preserved evidence remains unchanged.

Do not implement ingestion tooling yet. Bulk ingestion must wait until the schema and unresolved epistemology are reviewed and explicitly approved against representative real material.
