# Data model

## Records and files

Primary archive data is UTF-8 Markdown with concise YAML frontmatter where structured metadata is useful. Each persistent record represents one primary entity, event, campaign, snapshot, or imported source and has one H1 heading matching its human-facing `reference_name` or title. Immutable raw evidence may use its original portable format beside its source metadata record under [`sources/`](../sources/).

Use readable YAML:

- two-space indentation and no tabs;
- block mappings and sequences;
- no anchors, aliases, custom tags, or implicit tricks;
- omit unknown optional values rather than using empty strings;
- represent meaningful uncertainty explicitly;
- keep field names stable and metadata comfortably editable by hand.

## Stable identity

Every persistent record has a permanent ASCII `id` with a readable type prefix, such as `being-...`, `location-...`, `event-...`, `campaign-...`, `polity-...`, `organization-...`, `object-...`, `snapshot-location-...`, or `source-...`.

- Identity is independent of display name.
- A corrected or changed `reference_name` does not change the ID or normal ID-based filename.
- Inspect existing records before creating an ID to avoid duplicates.
- Do not reuse retired IDs for different records.
- Stable IDs assigned before a model migration remain unchanged even if their old prefix no longer matches the current record type. Existing `person-...` IDs therefore remain permanent IDs for records migrated to `being`.

The `reference_name` is the archive's human-facing name, normally the name under which the subject first appears in campaign material. Alternate or historical names may use this modest structure:

```yaml
names:
  - name: <name as attested>
    role: <reference | alternate | historical>
    language_or_context: <optional language or cultural context>
    valid_time:
      description: <optional human-readable temporal validity>
    sources:
      - <relative link supporting this name block>
```

Omit optional keys when unsupported. Different names do not by themselves imply different entities. Preserve original spellings, languages, quotations, and campaign terminology.

## Named things and persistent identity

If a fictional person, being, place, geographic feature, organization, object, or other identifiable thing is given an explicit proper name, it should normally receive a persistent entity record. The project principle is: “If we gave it a name in the game/world, it matters.” This applies even when the named thing appears only in GM preparation, was never encountered by player characters, is minor in the immediate adventure, currently has little information beyond its name, or appears only once in available sources.

Resolve each named thing against existing records before creating a new ID. Spelling variants, titles, translations, aliases, historical names, and uncertain name forms do not by themselves justify duplicate records; use the normal identity and confirmed-duplicate rules, preserving uncertainty and provenance where equivalence is not yet established.

This invariant concerns identity-bearing named things. Unnamed generic material may remain source-local unless another reason makes it persistent or world-significant: generic guards, ordinary furniture, an unnamed sword, an unnamed hill, or an unnamed tavern do not require separate records merely because they occur in a source. Nor does the invariant require independent records for every unnamed room, architectural feature, mundane item, tactical instruction, encounter procedure, or other adventure-local detail. The hybrid module-ingestion policy preserves complete source-local detail while materializing named identities and other persistent or world-significant information; see [ingestion.md](ingestion.md#gm-preparation-and-adventure-modules).

## Links and filenames

Persistent record filenames normally equal their stable ID plus `.md`. Use ordinary relative Markdown links, for example `[reference name](../entities/beings/<being-stable-id>.md)`, adjusted for the linking file's location. Do not depend on proprietary wiki-link syntax.

An ID is the machine-stable identity; a Markdown link provides navigability; the link label is human-facing and may change without changing the target filename.

## Beings

A **being** is an individual actor or animate entity, ordinary or extraordinary. Being records live under [`entities/beings/`](../entities/beings/) and new stable IDs use the `being-...` prefix. Humans, elves, goblins or similar peoples, werewolves, spirits, dragons, local divinities, conscious springs or other nonstandard animate entities, and gods can all be beings when supported by source material.

Natural, supernatural, mortal, divine, humanoid, non-humanoid, and similar distinctions do not determine the top-level storage category. Such boundaries may themselves be culturally, historically, or ontologically uncertain. A record may describe what kind of being an entity appears to be when sources support that description, while preserving competing classifications and uncertainty.

Do not define a closed list of kinds, require every being to have a precise nature, or infer a classification from its storage history. In particular, a record migrated from `entities/people/` is not thereby established to be human. Whether future structured characterization should distinguish species, ancestry, condition, ontology, divinity, transformation, or other dimensions remains open until representative data demonstrates a need.

Existing `person-...` records have moved to `entities/beings/` and use `record_type: being`; their stable IDs and filenames remain unchanged.

## Confirmed duplicate entity records

When curation establishes that two existing entity records represent the same entity, choose one surviving record and preserve the other at its existing stable-ID filename as a superseded record pointing to the survivor. Stable IDs are never reused, and the superseded record must retain the identity and provenance needed to audit the merge.

Use the original entity `record_type`, add `record_status: superseded`, and record the disposition in a small mapping:

```yaml
record_status: superseded
superseded_by:
  entity: <relative link to surviving record>
  merge_date: <real-world archive or curation date>
  basis:
    description: <what established that the records are duplicates>
    provenance:
      - <source evidence with locator or curator-supplied decision>
```

New references use the surviving ID. Existing links may be changed to the survivor where safe, while the superseded file remains available at its original path so the former ID and merge history do not disappear. Retain the evidence or curator decision that established equivalence and any earlier sourced content needed to understand the identity decision.

Prefer the older established stable ID as the survivor unless a material reason supports another choice. If the choice is genuinely ambiguous or consequential, ask the curator rather than selecting arbitrarily. This superseded-record convention is the complete merge mechanism for now; do not build a broader redirect framework without representative need and approval.

## Identity, state, and events

- An **entity record** says what persistent subject a stable ID denotes.
- A **snapshot** describes an entity's time-specific state without replacing its identity record.
- An **event** describes a temporally situated development, normally as an interval, and may link affected entities or locations.
- A **session** is source context for play and is not automatically an historical event.

Keep these roles separate. Do not place an assumed universal “current state” in a historical identity record. Every derived factual Markdown section or meaningful content block must identify its supporting source or sources. Use statement-level attribution when section-level sourcing would be ambiguous, disputed, contradictory, or insufficient to preserve who made a claim. Whole-record source lists are optional metadata, not sufficient provenance for derived facts; when retained, use the explicit `record_sources` field. Detailed source ranking remains unresolved; see [provenance model](provenance-model.md).
