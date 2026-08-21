# Sources

This directory holds preserved raw material and the metadata needed to interpret and trace it.

- `inbox/`: intake material whose ingestion has not yet completed.
- `campaigns/`: successfully ingested campaign-specific material.
- `shared/`: raw material that is not specific to one campaign.

## Inbox lifecycle and permanent locations

Keep an incoming file in `inbox/` while it is being classified, checked, and used to derive reviewed records. After ingestion succeeds, move the raw file and its source metadata out of `inbox/`; the inbox must not be used as permanent storage for completed imports.

Campaign-specific sources use this convention:

```text
sources/campaigns/<campaign-id>/
  <preserved raw source filename>
  <source-id>.md
```

Use the stable campaign ID for the directory even if the campaign's display name later changes. Keep the raw source's supplied filename when it is portable and unambiguous. A non-campaign source and its metadata live directly under `sources/shared/` unless representative material later demonstrates a need for another simple grouping.

Moving or renaming a source must not alter its contents. Update all repository-relative provenance links and verify the recorded digest after the move.

## Source metadata

Each imported raw source has a persistent `source-...` metadata record stored beside it. Record only applicable information, which may include source classification, real-world authorship, in-world authorship or narrator, perspective, epistemic role, relationship to play, origin or export metadata, raw-file integrity, curator-supplied metadata and corrections, and locators for meaningful sections or blocks. Keep the metadata concise and human-readable; no single export format or exact field set is mandatory for every source.

Raw sources are evidence. Never silently rewrite them to normalize spelling, resolve contradictions, or match derived records. Put interpretation and corrections in source metadata or derived records with explicit provenance, leaving the original source intact.

Use portable, repository-contained formats where practical. Do not ingest campaign content until the schema has been reviewed and an ingestion task explicitly authorizes it.
