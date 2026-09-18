# Content curation workflow

This directory is the persistent queue for actionable uncertainties about particular sources, campaigns, entities, locations, events, or other world records. General questions whose answers would change repository rules, schema, representation, or operation belong in [`docs/open-questions.md`](../docs/open-questions.md), not here.

## What belongs in the queue

Create a curation item when a concrete uncertainty could materially improve or correct derived records, such as uncertain entity or location identity, a suspected source error, an ambiguous passage referent, or a content-specific chronology question that surviving evidence or a curator could reasonably clarify.

Do not create an item merely because a fact is unknown. An event with no recorded fictional date, for example, remains uncertain in its event record unless there is a concrete reason to expect that the date should or can be resolved.

Chronology questions and contradictory temporal constraints use this same queue. Link relevant items from the chronology manifest, preserve all competing locally supported claims, and update affected assertions/relations when an item is resolved. There is no parallel chronology-only question system. Unique unresolved curator decisions discovered during ingestion must survive the [retention gate](../docs/ingestion.md#derived-knowledge-retention-gate).

Active items live in [`open.md`](open.md). Each item uses a stable lightweight ASCII ID such as `curation-penbrok-001` and records:

- status;
- campaign or other scope;
- the uncertainty and why it matters;
- affected records where known;
- source links and human-readable locators;
- current evidence and current handling.

An item asks a traceable question; it does not require a speculative answer.

## Reconsideration during ingestion

After deriving information from a newly ingested source, inspect open items relevant to that source's campaign, entities, locations, events, or other scope. Determine whether the new evidence resolves an item, adds evidence without resolving it, requires reformulation or splitting, or has no material effect.

A mention of the same subject is not enough to resolve an item. Interpret the new evidence according to its provenance, perspective, epistemic role, and relationship to play. Prepared GM material, for example, may establish an intended possibility without establishing that an event occurred during play.

Update affected derived records and curation items together. For a split or reformulation, give replacement items new IDs and retain the earlier item as superseded so the change remains auditable.

When curation confirms that two existing entity records are duplicates, follow the [confirmed duplicate entity policy](../docs/data-model.md#confirmed-duplicate-entity-records). Preserve both stable IDs, keep the non-surviving record as an auditable superseded record, and ask the curator if the surviving ID cannot be chosen safely under that policy.

## Resolution and audit

Move a resolved or superseded item from `open.md` to [`resolved.md`](resolved.md) without changing its ID or erasing its original uncertainty. Add:

- the resolution or reason it was superseded;
- whether the basis was source evidence or a curator-supplied decision or correction;
- the resolving source and locator, when applicable;
- affected records updated;
- the real-world archive or curation date on which the item was resolved, never a date in fictional chronology.

This is a lightweight audit trail, not a ticketing system or comprehensive issue history.

## Curator interaction

Ingestion normally continues when uncertainty can safely remain explicit: preserve it in derived records, add or update a curation item, and finish the useful import. Ask the curator immediately only when proceeding would materially risk an ambiguous or destructive identity decision, loss of provenance, overwriting conflict, or another difficult-to-reverse structural choice.

A curator may later request review of open items for a campaign, entity, location, event, or other scope. The intended sequence is:

```text
raw source
→ ingestion
→ derived records
→ actionable unresolved content questions enter the curation queue
→ later sources are ingested
→ relevant items are reconsidered
→ surviving items can be reviewed with the curator
```
