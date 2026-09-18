# Ingestion

Ingestion is a reviewed workflow, not an implemented tool:

1. Preserve incoming material unchanged in [`sources/inbox/`](../sources/inbox/) while it awaits review, and record an integrity digest where practical.
2. Inspect existing records and identify referenced existing entities before proposing new IDs.
3. Create minimal persistent source metadata that identifies the raw file and records supported classification, authorship or narrator, perspective, relationship to play, origin metadata, integrity information, curator metadata, and useful locators as applicable. Omit fields the source does not need.
4. Identify candidate new entities, events, campaigns, accounts, and snapshots. Treat every explicitly proper-named fictional thing as normally requiring a persistent entity record, while resolving it against existing records before assigning an ID; different spellings, titles, or name occurrences do not by themselves establish distinct entities. Do not assume every source section is a session or event, or every session is an historical event.
5. Derive or update the smallest appropriate records, giving every factual section or meaningful block identifiable supporting sources and retaining contradiction, uncertainty, and original language. Add source locators when a whole-file link would be ambiguous.
6. Add statement-level attribution where disputes, contradictions, mixed sourcing within a section, or attribution of a particular claim require it.
7. Record curator-supplied corrections in source metadata without changing the raw source; retain both the source-stated and corrected values, and use the corrected value in derived data where applicable.
8. Review [`curation/open.md`](../curation/open.md) for existing items relevant to the new source's campaign, entities, locations, events, or other scope. For each relevant item, determine whether the new evidence resolves it, adds evidence without resolving it, requires reformulation or splitting, or has no material effect.
9. Update affected derived records and the curation queue together. Add newly discovered actionable content uncertainties to the queue when they can safely remain unresolved; do not queue ordinary unknown facts merely because they are unknown.
10. After successful review, move the immutable raw source and its metadata out of `sources/inbox/` to the permanent location defined in [`sources/README.md`](../sources/README.md). Update provenance links and verify the raw digest after the move.
11. Review the complete Git diff for unsupported or insufficiently sourced facts, accidental source edits, broken relative links, manufactured precision, and curation items inconsistent with the derived records.
12. Apply the [derived-knowledge retention gate](#derived-knowledge-retention-gate) before finalization or any tmp cleanup. Record the audit outcome durably; cleanup is blocked while unique derivations remain unaccounted for.

## Story chronology reconstruction

Whenever source material contains a story sequence, assess and preserve useful derived fictional chronology using the [durable chronology model](../chronologies/README.md). Build it from evidence, retain partial order and uncertainty, and never manufacture a total order. Forum posting order, letters, journals, session sequence, chat timestamps, transcript order, and mixed-source document order are source-specific reconstruction scaffolds, not automatic fictional time.

Distinguish a letter's document position, fictional writing time, and narrated events; distinguish real session dates/order, fictional time, and retrospectives. Separate narrative continuity/splits/reunions from locally evidenced temporal constraints. Do not require a segment per source item, an event per segment, or chronology for sources without useful story chronology.

Resolve source labels to persistent identities when later ingestion phases supply enough evidence. Support each participant inclusion, boundary, event link, temporal relation, and anchor locally. Reconsider relevant existing curation items and link actionable unresolved questions from the chronology manifest. Materialize unique source-backed chronology before finalization, even when reconstruction remains partial or disputed. Recovery JSON remains recovery/audit input, not canonical durable chronology after materialization.

## Derived-knowledge retention gate

Before deleting an ingestion tmp workspace, explicitly audit every artifact for **unique source-backed derived knowledge not represented in durable repository state**. This includes detailed fictional chronology, unresolved curator decisions, unique relation graphs, and temporal anchors. Raw-source preservation alone does not preserve a unique derivation.

Record a concise audit in the durable ingestion/source-metadata completion notes (or the chronology method notes when appropriate): artifact/derivation inventory, durable destination and coverage, intentionally disposable items with rationale, reviewer/date, and the gate outcome. An artifact name may identify the cleanup inventory; it is not final provenance. Cite preserved sources or durable curator clarification for retained claims.

If any unique derived knowledge exists, **tmp cleanup is BLOCKED** until it is either durably materialized or explicitly classified as intentionally disposable with a recorded rationale. “It is in tmp,” “raw evidence survives,” and “recovery JSON exists” are not sufficient rationales for discarding unique useful knowledge. Preserve non-blocking actionable curator questions in the existing queue; ask immediately only under the existing safe-ingestion blocking rule.

Review durable coverage and links, run applicable validation, and record that the gate passed before cleanup/finalization. A workflow phase being marked complete does not bypass this gate.

Use the [canonical validation commands](../tools/README.md#run): `python tools/validate.py`, `python -m unittest discover -s tools/tests -v`, and `git diff --check`. Temporary inspection helpers are noncanonical and do not replace this gate or its review of retained knowledge.

## GM preparation and adventure modules

GM preparation is evidence of what was prepared for play. It is neither a played campaign account nor a later GM reconstruction of what happened. Preserve that distinction in source classification and in every derived use of the material.

The general immutable-source rule applies to the complete preparation or module, including material that is not selected for world-model records. Transcriptions, extracted assets, and other derivatives may aid access but do not replace the preserved original.

Importing or retaining an adventure module as a source does not by itself establish its contents as a campaign prepared baseline. Module content supports prepared state for a campaign only to the extent that adoption or preparation of that content for the campaign is established by evidence; otherwise preserve it as source material without promoting it to campaign state.

Once adoption or preparation for the campaign is established, declarative GM preparation may establish prepared world state whether or not player characters ever encountered, activated, discovered, or interacted with the material. Lack of played confirmation does not by itself weaken or invalidate that prepared state. Omission of a prepared detail from another preparation source is likewise not evidence that the detail was abandoned, superseded, or false. Later play may establish a changed state for a later temporal point without erasing the earlier prepared baseline. Directly incompatible claims about the same relevant state and time must retain their separate provenance and use the curation workflow when actionable rather than being silently reconciled.

A preparation document or adventure module may mix several epistemically different kinds of content. Classify relevant blocks according to what they actually establish:

- declarative prepared baselines and hidden established backstory may support state, backstory, and relationships at the preparation's temporal point, without making them character knowledge;
- NPC knowledge, beliefs, motivations, and intentions describe the prepared NPC perspective or disposition, not necessarily external fact or later action;
- intended developments, conditional contingencies, tactical instructions, game procedures, encounter tables, dice chances, and other random possibilities are possibilities or play machinery, not historical events;
- drafts, placeholders, unfinished passages, and `TBD` material remain incomplete and must not be silently completed;
- numbered rooms, keyed locations, maps, encounter notes, and similar adventure-local reference material may remain addressable within the source rather than becoming independent world records, except that explicitly proper-named identity-bearing things within that material follow the named-things invariant below.

In particular, do not create an event merely because preparation says that someone intends an action, an outcome will occur under a condition, or a procedure can generate it. Materialize an event only when evidence supports it as part of the fictional history, retaining the supporting source's relationship to play and provenance in the relevant records.

Compare prepared and played claims at the relevant temporal points. When play changes a prepared baseline, the normal interpretation is a state transition rather than a source conflict: preserve the earlier prepared state and represent the later played change through an appropriate event or later state record when useful. If preparation and played evidence instead make materially incompatible claims about the same relevant state and time, preserve both claims and their provenance and use the curation workflow when the uncertainty is actionable. Do not resolve the case through a universal ranking of GM preparation over played evidence, or the reverse; see the [provenance model](provenance-model.md).

Use a hybrid materialization policy. Create or update a persistent entity record for every explicitly proper-named fictional person, being, place, geographic feature, organization, object, or other identifiable thing, subject to the normal identity and duplicate-resolution rules in the [data model](data-model.md#named-things-and-persistent-identity). A named thing is not excluded because it appears only in preparation, was never encountered, seems minor to the immediate adventure, has little information, or appears only once. Also materialize other persistent or world-significant state, backstory, relationships, and supported played changes when doing so improves the archive.

Do not mechanically duplicate unnamed keyed rooms, architectural features, mundane items, tactical instructions, minor encounters, or random procedures into the world model merely because they occur in a module. Generic guards, ordinary furniture, an unnamed sword, an unnamed hill, an unnamed tavern, and comparable non-identity-bearing material may remain source-local unless another reason justifies persistent materialization. Information left source-local must remain practically retrievable through source-native headings, keys, pages, sections, or equivalent locators recorded in source metadata or citations. The complete original source remains preserved, and this policy does not require a general room, module, or encounter schema.

Preserve materially useful maps, floorplans, diagrams, and other composed visual information as source evidence. Text extraction is not a substitute when position, overlays, labels, arrows, layers, or page composition carry meaning. An extracted component image must not be presented as the complete visual when important composition or overlays remain outside it. Identify a practical locator for the composed visual and record relevant extraction or rendering limitations.

The completed [Hrad Penbrok GM-preparation source record](../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/source-hrad-penbrok-gm-preparation.md) is a demonstrated application of this workflow, not a mandatory source-record template.

## Reconsidering curation items

A new source does not resolve a curation item merely because it mentions the same subject. Resolution must follow from what the source actually establishes, interpreted according to its provenance, perspective, epistemic role, and relationship to play. Prepared GM material, for example, is not automatically evidence that a possible event occurred during play.

When new evidence resolves an item, retain its ID, original question, earlier evidence, resolution, resolving source and locator, and whether the resolution came from source evidence or a curator-supplied decision or correction. Move the complete item to [`curation/resolved.md`](../curation/resolved.md) and update affected records. If an item is reformulated or split, retain it as superseded and link its replacement IDs. Follow the lightweight process in [`curation/README.md`](../curation/README.md).

## When to ask the curator

Ingestion should normally produce useful derived records plus explicit unresolved content questions without interrupting the curator. If an ambiguity can safely remain unresolved, preserve it in the records, add or update a curation item, and continue.

Ask immediately only when the uncertainty materially prevents safe ingestion, especially when proceeding would risk a destructive or ambiguous identity decision, loss of provenance, overwriting conflicting information, or another difficult-to-reverse structural choice. The curator may later request an interactive review of open items for a particular campaign or scope after surviving sources have had the opportunity to supply evidence.

Never silently edit raw sources. Corrections or normalizations belong in source metadata or derived records with provenance, while the preserved evidence remains unchanged.

Do not implement ingestion tooling yet. Bulk ingestion must wait until the schema and unresolved epistemology are reviewed and explicitly approved against representative real material.
