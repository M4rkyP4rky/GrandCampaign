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

Every persistent record has a permanent ASCII `id` with a readable type prefix, such as `person-...`, `location-...`, `event-...`, `campaign-...`, `polity-...`, `organization-...`, `object-...`, `snapshot-location-...`, or `source-...`.

- Identity is independent of display name.
- A corrected or changed `reference_name` does not change the ID or normal ID-based filename.
- Inspect existing records before creating an ID to avoid duplicates.
- Do not reuse retired IDs for different records.

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

## Links and filenames

Persistent record filenames normally equal their stable ID plus `.md`. Use ordinary relative Markdown links, for example `[reference name](../entities/people/<person-stable-id>.md)`, adjusted for the linking file's location. Do not depend on proprietary wiki-link syntax.

An ID is the machine-stable identity; a Markdown link provides navigability; the link label is human-facing and may change without changing the target filename.

## Identity, state, and events

- An **entity record** says what persistent subject a stable ID denotes.
- A **snapshot** describes an entity's time-specific state without replacing its identity record.
- An **event** describes a temporally situated development, normally as an interval, and may link affected entities or locations.
- A **session** is source context for play and is not automatically an historical event.

Keep these roles separate. Do not place an assumed universal “current state” in a historical identity record. Every derived factual Markdown section or meaningful content block must identify its supporting source or sources. Use statement-level attribution when section-level sourcing would be ambiguous, disputed, contradictory, or insufficient to preserve who made a claim. Whole-record source lists are optional metadata, not sufficient provenance for derived facts; when retained, use the explicit `record_sources` field. Detailed source ranking remains unresolved; see [provenance model](provenance-model.md).
