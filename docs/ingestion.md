# Ingestion

Ingestion is a reviewed workflow, not an implemented tool:

1. Preserve incoming material unchanged in [`sources/inbox/`](../sources/inbox/) while it awaits review, and record an integrity digest where practical.
2. Inspect existing records and identify referenced existing entities before proposing new IDs.
3. Create minimal persistent source metadata that identifies the raw file and records supported classification, authorship or narrator, perspective, relationship to play, origin metadata, integrity information, curator metadata, and useful locators as applicable. Omit fields the source does not need.
4. Identify candidate new entities, events, campaigns, accounts, and snapshots without assuming every name is a distinct entity, every source section is a session or event, or every session is an historical event.
5. Derive or update the smallest appropriate records, giving every factual section or meaningful block identifiable supporting sources and retaining contradiction, uncertainty, and original language. Add source locators when a whole-file link would be ambiguous.
6. Add statement-level attribution where disputes, contradictions, mixed sourcing within a section, or attribution of a particular claim require it.
7. Record curator-supplied corrections in source metadata without changing the raw source; retain both the source-stated and corrected values, and use the corrected value in derived data where applicable.
8. After successful review, move the immutable raw source and its metadata out of `sources/inbox/` to the permanent location defined in [`sources/README.md`](../sources/README.md). Update provenance links and verify the raw digest after the move.
9. Review the complete Git diff for unsupported or insufficiently sourced facts, accidental source edits, broken relative links, and manufactured precision.

Never silently edit raw sources. Corrections or normalizations belong in source metadata or derived records with provenance, while the preserved evidence remains unchanged.

Do not implement ingestion tooling yet. Bulk ingestion must wait until the schema and unresolved epistemology are reviewed and explicitly approved against representative real material.
