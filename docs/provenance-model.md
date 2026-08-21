# Provenance model

## Layers of knowledge

The archive distinguishes these concepts without assuming a complete epistemology:

- **Raw source material**: preserved evidence under [`sources/`](../sources/), such as campaign notes or exported logs. It must never be silently rewritten to make derived data cleaner or consistent.
- **Campaign account**: an historical account produced by played campaign material. It is a perspective, not automatically objective truth.
- **In-world tradition or legend**: a belief or narrative attested within the fictional world, which may differ from other accounts.
- **GM reconstruction**: an explicitly labeled attempt to reconstruct events as objectively as available information permits. It remains derived material and must retain provenance and uncertainty.

A record can link multiple accounts. Contradictions are valid archive data. Preserve each supported version, identify its source or perspective, and do not invent facts to reconcile them.

## Uncertainty

Use plain language for uncertainty and retain the source's precision. Distinguish “not recorded,” “unknown,” “approximate,” and “disputed” when that difference is supported. Do not convert absence of evidence into a factual negative.

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

## Intentionally unresolved authority

The relative authority and precedence of raw sources, campaign accounts, traditions, and GM reconstructions has not been designed. There is no source-ranking algorithm and no automatic winner in a conflict. Questions about quotation, paraphrase, transcription correction, redaction, and competing or revised reconstructions also remain unresolved. These are explicit questions in [open-questions.md](open-questions.md); future rules require review and approval before being added to governance documentation.
