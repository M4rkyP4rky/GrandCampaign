# Provenance model

## Layers of knowledge

The archive distinguishes these concepts without assuming a complete epistemology:

- **Raw source material**: preserved evidence under [`sources/`](../sources/), such as campaign notes or exported logs. It must never be silently rewritten to make derived data cleaner or consistent.
- **GM preparation or adventure module**: material recording campaign preparation or offering content that could be adopted for play. It supports a campaign prepared baseline only where adoption or preparation for that campaign is established by evidence; otherwise it establishes only what the source contains or proposes. It is not by itself a played account or a retrospective reconstruction of what happened.
- **Campaign account**: an historical account produced by played campaign material. It is a perspective, not automatically objective truth.
- **In-world tradition or legend**: a belief or narrative attested within the fictional world, which may differ from other accounts.
- **GM reconstruction**: an explicitly labeled attempt to reconstruct events as objectively as available information permits. It remains derived material and must retain provenance and uncertainty.

A record can link multiple accounts. Contradictions are valid archive data. Preserve each supported version, identify its source or perspective, and do not invent facts to reconcile them.

## Preparation, possibility, and later play

GM preparation can contain both declarative prepared assertions and non-asserted possibilities. Once adoption or preparation for the campaign is established, a declarative baseline or hidden backstory may establish prepared world state at its documented temporal point even if player characters never encountered, activated, discovered, or interacted with it. Lack of played confirmation does not by itself weaken or invalidate prepared-state information. NPC intentions, contingencies, game procedures, random outcomes, and draft material do not establish that the described events occurred. Preserve the epistemic role of the relevant block when deriving records; the detailed ingestion policy is in [ingestion.md](ingestion.md#gm-preparation-and-adventure-modules).

Omission of a prepared detail from another preparation source is absence of evidence in that source, not by itself evidence that the detail was abandoned, superseded, or false. A later played outcome may supersede the earlier prepared state for the affected later time or state, but the earlier baseline remains valid evidence of what had been prepared. This temporal succession is normally change, not contradiction. Claims become a potential conflict when they are materially incompatible about the same relevant subject, state, and time. In that case retain the competing provenance and uncertainty, and create or update a content curation item when clarification could materially improve the records rather than silently reconciling them. Neither GM preparation nor played evidence wins automatically.

## Uncertainty

Use plain language for uncertainty and retain the source's precision. Distinguish “not recorded,” “unknown,” “approximate,” and “disputed” when that difference is supported. Do not convert absence of evidence into a factual negative.

When a concrete content uncertainty could materially improve or correct records if clarified, track it in the [content curation queue](../curation/README.md) while preserving the uncertainty in the affected records. Do not queue ordinary unknown facts merely because they are unknown. General representation or authority questions remain in [repository and design open questions](open-questions.md).

## Required granularity

Whole-record source lists may be retained as useful discovery metadata, but they do not by themselves provide sufficient provenance for derived factual content. The minimum required granularity is a meaningful content block or Markdown section. A reader must be able to identify which source or sources support each derived factual block or section.

A simple section-level pattern is sufficient when its scope is unambiguous:

```markdown
## <Section title>

<Derived factual content supported by the sources below.>

Sources:

- [<source label>](<relative path>) — <what this source supports in the section>
```

Structured metadata can meet the same rule by placing source links within the relevant mapping or list item, or by pointing to a clearly scoped sourced section that supports the values. A record-level source list alone is not a substitute.

## Source locators

A compound source can contain independently meaningful sections or blocks. When a link to the entire file would leave the supporting passage ambiguous, add a human-readable `locator` to the source reference. Use the source's own stable heading or block label when available:

```yaml
sources:
  - source: <relative link to source>
    locator: section "<heading as recorded>"
```

The locator identifies evidence within the source; it is not a claim ID, session ID, event ID, or replacement for the source link. A prose citation may express the same information by naming the relevant section after its link. One source section need not equal one session or fictional event, and one event may cite multiple sections.

## Curator-supplied corrections

An immutable raw source and a later curator-supplied correction are separate evidence. Never edit the raw source to apply a correction. Source metadata must retain the source-stated value, the corrected value, the field and source locator to which it applies, and an explicit indication that the correction is curator-supplied. Derived data may use the corrected value while remaining traceable to both values.

A small mapping on the source metadata record is sufficient for demonstrated cases:

```yaml
curator_corrections:
  - field: <corrected field>
    locator: <human-readable source locator>
    source_value: <value preserved in the raw source>
    corrected_value: <curator-confirmed value>
    provenance: <identification of the curator-supplied correction>
```

This does not authorize rewriting quotations or transcriptions, establish source-authority precedence, or require a general correction/version history.

Use statement-level provenance when section-level attribution would be ambiguous, especially when:

- a claim is disputed or uncertain;
- different accounts contradict one another;
- statements within one section come from different sources;
- preserving who made a particular claim or interpretation matters.

Do not add a citation to every ordinary sentence when a section-level source attribution is unambiguous. Event records may list accounts by kind and source, providing statement- or account-level attribution where needed.

Do not introduce an atomic claim database, claim IDs, or another complex claim model at this stage. A more granular claim model remains possible later if representative real data demonstrates a need for it.

## Chronology provenance

[Durable chronology](../chronologies/README.md) is derived knowledge. Every individual temporal assertion/anchor, relation, segment boundary, participant inclusion, location inclusion, and segment/event link must carry local `basis`, `confidence`, and `sources` or a durable, identifiable `curator_clarification`. Mechanical grouping must identify its source span and explain that it is grouping rather than fictional temporal evidence. Aggregate `source_spans`, `record_sources`, and record-level `chronology_confidence` do not replace this support.

Chronology must not cite itself as proof of fictional facts when preserved primary evidence exists. Do not use tmp or host filesystem paths as final provenance. Recovery JSON is restoration/audit input; after materialization the Markdown chronology is the canonical derived chronology, while primary sources retain their evidence role.

Preserve competing temporal claims, including contradictions between existing `time` and optional `temporal.assertions`. No representation wins automatically. Report contradictions and route actionable interpretation through the existing curation queue; do not delete constraints merely to make a graph acyclic.

## Intentionally unresolved authority

The relative authority and precedence of GM preparation and adventure modules, other raw sources, campaign accounts, traditions, and GM reconstructions has not been designed. There is no source-ranking algorithm and no automatic winner in a conflict. Questions about quotation, paraphrase, transcription correction, redaction, and competing or revised reconstructions also remain unresolved. These are explicit questions in [open-questions.md](open-questions.md); future rules require review and approval before being added to governance documentation.
