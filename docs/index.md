# Governance documentation

This directory defines how the GrandCampaign archive is maintained. Read only the documents relevant to the task at hand.

- [Data model](data-model.md): record identity, file conventions, names, links, and the separation of identity, state, and events.
- [Temporal model](temporal-model.md): intervals, uncertain time, AP, Ages, and the approved calendar.
- [Geography model](geography-model.md): physical hierarchy, changing political relationships, names, and location snapshots.
- [Provenance model](provenance-model.md): raw evidence, accounts, legends, reconstructions, uncertainty, and contradiction.
- [Read and output modes](output-modes.md): FAST materialized-only answers, DEEP source-grounded answers, and diagnostic COMPARE output.
- [Ingestion](ingestion.md): the reviewed high-level workflow for deriving records from sources.
- [Content curation](../curation/README.md): actionable uncertainties about particular sources and world records.
- [Repository and design open questions](open-questions.md): general decisions intentionally not settled by the current model.

The root [AGENTS.md](../AGENTS.md) is the concise governance entry point. Configuration facts live under [`config/`](../config/), and record examples live under [`templates/`](../templates/).
