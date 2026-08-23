# Repository and design open questions

This file contains unresolved questions whose answers would change the archive's general rules, schema, representation, or operation. They may remain open without immediate curator intervention. Actionable uncertainties about particular imported content or world records belong in the [content curation queue](../curation/README.md), not here.

Do not infer answers from convenience or conversation history; record an approved design decision in the relevant governance document.

## Calendar and chronology

- Should the provisional structured-date precision vocabulary be finalized or revised after representative records are tested?
- What evidence, if any, will define the boundaries of the seven Ages?

## Provenance and authority

- What precedence, if any, applies among GM preparation and adventure modules, other raw materials, campaign accounts, in-world traditions, and GM reconstructions?
- How should direct quotation, paraphrase, transcription corrections, and redactions be represented?
- How should competing GM reconstructions or later revisions be retained?

## Identity and relationships

- Which structured relationship types are useful after representative data is reviewed, rather than leaving relationships in prose?
- How should overlapping, nested, or disputed location snapshots be queried or presented?
- Which additional structured descriptive dimensions for beings—beyond the approved open-world `kind` and `faction` values—become useful after representative data is reviewed? In particular, ancestry, condition, ontology, divinity, transformation, and culture must not be collapsed into one axis merely for convenience.

## Sources and sessions

- What is the minimal session-record schema, and how should a session link to one or more sections of a compound source? Until this is decided, the first ingestion retains date/system pairs at source-section level without creating standalone session records.
- When two source sections carry the same real-world date and RPG system, what additional evidence is required to treat them as one session rather than two separately dated sections?

## Repository operations

- At what repository size, if any, should Git LFS or another asset policy be considered? It is not configured now.
- Which internal validation tools are worth implementing after the schema is approved?
