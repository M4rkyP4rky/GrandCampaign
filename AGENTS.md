# GrandCampaign agent guide

## Purpose

This repository is the persistent, Git-versioned source of knowledge for multiple tabletop RPG campaigns in one shared world. Repository files—not conversation history—are authoritative project memory.

## Critical invariants

- Do not fabricate lore, dates, names, relationships, or certainty.
- Preserve conflicting accounts; never silently reconcile them into one history.
- Never rewrite raw material under `sources/` to make derived records cleaner.
- Preserve uncertainty and the precision of the source.
- Inspect existing records before assigning a new entity, event, campaign, or snapshot ID.
- Every persistent record has a permanent, readable ASCII ID with a type prefix. Renaming a record does not change its ID.
- Keep identity, time-dependent state, and events distinct.
- Treat events as intervals when the evidence supports an interval; do not equate sessions with events.
- Use stable physical geography as the location hierarchy. Political control is time-dependent data.
- Use human-readable UTF-8 Markdown and simple YAML frontmatter with ordinary relative Markdown links.
- Do not make source-authority decisions that the governance documents leave unresolved.

## Documentation map

Start with [docs/index.md](docs/index.md), then read only the documentation relevant to the current task:

- Record structure and identity: [docs/data-model.md](docs/data-model.md)
- Dates, intervals, AP, Ages, and calendar: [docs/temporal-model.md](docs/temporal-model.md)
- Locations, physical hierarchy, and political change: [docs/geography-model.md](docs/geography-model.md)
- Evidence, accounts, contradictions, and reconstruction: [docs/provenance-model.md](docs/provenance-model.md)
- Future ingestion workflow: [docs/ingestion.md](docs/ingestion.md)
- Unresolved decisions: [docs/open-questions.md](docs/open-questions.md)

## Working rules

1. Read the relevant governance document and inspect related existing records.
2. Trace derived content to repository sources where possible.
3. Add or update the smallest appropriate record without manufacturing missing values.
4. Keep raw evidence separate from derived records and perspectives.
5. Update governing documentation when an explicitly approved model rule changes; do not rely on chat memory.
6. Review `git diff` before considering any data-changing task complete.

Do not add nested `AGENTS.md` files unless repository governance later requires them.
