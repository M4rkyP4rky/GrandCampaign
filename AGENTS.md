# GrandCampaign agent guide

## Purpose

This repository is the persistent, Git-versioned source of knowledge for multiple tabletop RPG campaigns in one shared world. Repository files—not conversation history—are authoritative project memory.

## Critical invariants

- Do not fabricate lore, dates, names, relationships, or certainty.
- Preserve conflicting accounts; never silently reconcile them into one history.
- Never rewrite raw material under `sources/` to make derived records cleaner.
- Preserve uncertainty and the precision of the source.
- Give every derived factual section or meaningful content block identifiable supporting sources; use statement-level attribution when ambiguity, dispute, or conflicting sourcing requires it.
- Inspect existing records before assigning a new entity, event, campaign, or snapshot ID.
- Explicitly proper-named fictional things normally receive persistent entity records; resolve spelling and naming variants against existing identities rather than creating duplicates.
- Every persistent record has a permanent, readable ASCII ID with a type prefix. Renaming a record does not change its ID.
- Keep identity, time-dependent state, and events distinct.
- Treat events as intervals when the evidence supports an interval; do not equate sessions with events.
- Use stable physical geography as the location hierarchy. Political control is time-dependent data.
- Use human-readable UTF-8 Markdown and simple YAML frontmatter with ordinary relative Markdown links.
- Do not make source-authority decisions that the governance documents leave unresolved.
- Apply [read and output modes](docs/output-modes.md) to repository-backed answers: default to FAST, and never read anything under `sources/` in FAST.

## Documentation map

Start with [docs/index.md](docs/index.md), then read only the documentation relevant to the current task:

- Record structure and identity: [docs/data-model.md](docs/data-model.md)
- Dates, intervals, AP, Ages, and calendar: [docs/temporal-model.md](docs/temporal-model.md)
- Durable chronology, segments, and threads: [chronologies/README.md](chronologies/README.md)
- Canonical validation commands and scope: [tools/README.md](tools/README.md)
- Locations, physical hierarchy, and political change: [docs/geography-model.md](docs/geography-model.md)
- Evidence, accounts, contradictions, and reconstruction: [docs/provenance-model.md](docs/provenance-model.md)
- FAST, DEEP, and COMPARE read/output behavior: [docs/output-modes.md](docs/output-modes.md)
- Ingestion workflow: [docs/ingestion.md](docs/ingestion.md)
- Actionable content uncertainties and curator review: [curation/README.md](curation/README.md)
- Unresolved repository and design decisions: [docs/open-questions.md](docs/open-questions.md)

## Working rules

1. Read the relevant governance document and inspect related existing records.
2. When changing persistent derived factual content, trace it to repository sources at section or meaningful-block granularity at minimum.
3. Add or update the smallest appropriate record without manufacturing missing values.
4. Keep raw evidence separate from derived records and perspectives.
5. Update governing documentation when an explicitly approved model rule changes; do not rely on chat memory.
6. During ingestion, reconsider relevant open content curation items; queue non-blocking actionable ambiguities and ask the curator immediately only when safe ingestion is materially blocked.
7. Review `git diff` before considering any data-changing task complete.
8. Before ingestion tmp cleanup, apply the derived-knowledge retention gate in [docs/ingestion.md](docs/ingestion.md#derived-knowledge-retention-gate). Unique source-backed derivations must be durable or explicitly classified as disposable with a recorded rationale.

Do not add nested `AGENTS.md` files unless repository governance later requires them.
