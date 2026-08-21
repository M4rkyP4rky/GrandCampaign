# Ingestion

Ingestion is a future reviewed workflow, not an implemented tool:

1. Preserve the incoming material as raw source data under the appropriate [`sources/`](../sources/) area.
2. Inspect existing records and identify referenced existing entities before proposing new IDs.
3. Identify candidate new entities, events, campaigns, accounts, and snapshots without assuming every name is a distinct entity or every session is an event.
4. Derive or update the smallest appropriate records, retaining provenance, contradiction, uncertainty, and original language.
5. Review the complete Git diff for unsupported facts, accidental source edits, broken relative links, and manufactured precision.

Never silently edit raw sources. Corrections or normalizations belong in derived records with provenance, while the preserved evidence remains unchanged.

Do not implement ingestion tooling yet. Bulk ingestion must wait until the schema and unresolved epistemology are reviewed and explicitly approved against representative real material.
