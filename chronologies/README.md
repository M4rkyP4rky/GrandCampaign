# Durable fictional chronology

Chronology is optional, campaign-scoped derived knowledge in the FAST materialized layer. Primary evidence remains under `sources/`. This directory contains conventions only until a separate ingestion or restoration task authorizes data materialization.

## Identity and storage

```text
chronologies/<campaign-id>/
  chronology.md
  segments/
    chronology-segment-<campaign-slug>-<stable-suffix>.md
```

The manifest has `record_type: chronology`, a global stable `chronology-...` ID, `reference_name`, exactly one matching H1, and `record_sources`. **`chronology.md` is an intentional filename exception**: identity still comes from frontmatter `id`; all other record-envelope rules apply. The containing directory uses the campaign's permanent ID.

Segments have `record_type: chronology_segment`, a global stable `chronology-segment-...` ID, `reference_name`, exactly one matching H1, and `record_sources`. Their filenames equal their IDs plus `.md`. Inspect existing identities before assigning either ID; renaming does not change identity.

- An **event** is a semantically meaningful fictional occurrence.
- A **segment** is a derived story-navigation/time-order unit containing zero, one, or several events. It is not a replacement event or necessarily a source item/session.
- A **story thread** is an analytical branch, not a fictional entity. Declare a readable ASCII `thread-...` ID once within its chronology; the same local ID may occur in another chronology.
- A **chronology** is a directed graph with a partial temporal order supported by temporal constraints. Narrative traversal, overlap, simultaneity, and qualified hypotheses add information without forcing a total order.

## Manifest contract

Required fields: the envelope above, `campaign` (relative link), `status` (`draft`, `reviewed`, or `disputed`), `threads` (list of `{id, label}`), and `segments` (list of links; may be empty while drafting). Status describes review, not source authority. A segment's `thread` must resolve in its own manifest.

The body records method/cautions and scoped, source-supported summary information. Optional `temporal.assertions` supplies chronology-wide anchors: each assertion identifies its `subject` event or segment and follows the [temporal contract](../docs/temporal-model.md#optional-temporal-assertions). An anchor does not date every segment automatically.

Optional `curation` links to relevant items in the existing [queue](../curation/README.md), including preserved resolutions. Optional `curator_corrections` entries retain `source_value`, `corrected_value`, and local `basis`, `confidence`, and support identifying the durable clarification. They summarize, rather than replace, the correction/curation audit trail. Do not create a chronology-only question queue.

## Segment contract

Required fields: the envelope, `chronology`, `campaign`, `thread`, `boundaries`, and `chronology_confidence`. Use `reference_name` as the label and a concise sourced Summary section; avoid duplicating event prose.

`boundaries` is a list of locally supported grouping decisions with `description`. Record why material belongs in this segment, including mechanical grouping (for example one source heading) without asserting that a document boundary proves fictional time.

Optional lists:

- `participants`: entries with `entity` links to resolved persistent identities;
- `locations`: entries with `location` links;
- `events`: entries with `event` links; no event is required;
- `source_spans`: source/locator pairs for source coverage, not a substitute for assertion-level support;
- `relations`: edges defined below;
- `temporal.assertions`: exact evidence and/or interpreted constraints using the shared temporal shape.

Every boundary, participant inclusion, location inclusion, event link, relation, correction, and temporal assertion carries its own `basis`, `confidence`, and `sources` or `curator_clarification`. `chronology_confidence` is a record overview only.

## Local evidence shape

`basis` is a nonempty explanation of what the evidence establishes and how it supports this specific derivation. `confidence` is `high`, `medium`, or `low`, expressing evidential/interpretive strength, never source-ranking precedence. Optional `evidence` preserves exact temporal wording with a precise source locator; do not fabricate quotations.

`sources` is a nonempty list of relative source links or `{source, locator}` mappings, using the existing provenance convention. Alternatively, `curator_clarification: {record, locator}` identifies a durable source metadata correction or existing curation item recording the decision. Both may be retained. No host filesystem paths or `tmp`/`temp` artifacts are final provenance. Record-level `record_sources`, aggregate `source_spans`, and confidence summaries cannot supply missing local evidence. Do not cite chronology itself as proof when primary evidence exists.

Filesystem-backed local support must resolve to a concrete file; a directory such as `sources/` is not identifiable evidence. A whole source file can suffice when its scope is unambiguous; existing requirements for locators remain unchanged. A curator clarification must point to a concrete source metadata record or to `curation/open.md` / `curation/resolved.md` with a locator naming an existing `curation-...` item heading. An unresolved question alone is not a curator decision: the identified item must actually preserve the clarification, which remains a human review responsibility. No line/post range is universally required.

## Relations

Each `relations` entry requires `type`, `target` (another segment in this chronology), `certainty`, `basis`, `confidence`, and local support. Self-relations are not allowed. `certainty` is `exact-at-precision`, `approximate`, `bounded`, or `uncertain`; it qualifies the relation rather than adding date precision.

An optional `precision` uses the [temporal vocabulary](../docs/temporal-model.md#direct-contradiction-checks). State it for simultaneity limited to a year, month, or day: comparisons use only mutually supported granularity, and insufficient endpoint precision is not itself a contradiction. Existing relations without this field remain valid. `overlaps` means interval intersection, never equal starts/ends; ordered starts alone cannot contradict overlap.

| Type | Meaning |
| --- | --- |
| `continues_to` | Narrative traversal continues at target. |
| `splits_into` | Narrative branch leads to target; repeat one supported edge per branch. |
| `rejoins` | This branch narratively rejoins target. |
| `precedes` | This unit finishes before target starts; no exact gap asserted. |
| `immediately_precedes` | Same order with source-supported temporal adjacency; no invented numeric gap. |
| `simultaneous_with` | Same temporal placement at the evidenced precision, not necessarily identical duration. |
| `overlaps` | Their fictional intervals share time; endpoints need not be known. |
| `probably_parallel_with` | Hypothesis of concurrent threads; not a hard ordering edge. |

Narrative continuation, splitting, and reunion **never independently prove fictional order or adjacency**. A retrospective may continue narratively while occurring earlier. Add a separately supported temporal relation if evidence establishes that meaning. Never derive time from filenames, manifest list order, or thread declaration order.

Only temporally justified exact constraints contribute to the strict partial order. Approximate/probable relations and hypotheses remain qualified assertions. Inverse navigation may be computed for display; it is not another independently evidenced claim and need not be stored. Simultaneity/overlap are symmetric for navigation; narrative links are not.

Preserve conflicting constraints and their support, mark the affected records as disputed where applicable, and link actionable interpretation to curation. Do not delete an edge to remove a cycle. Narrative cycles are valid navigation; strict temporal cycles are reported contradictions. Validation reports do not choose the true account.

## Relative links and navigation

Paths below are schematic, relative to the **destination record**, not the template directory:

| From | Target |
| --- | --- |
| Manifest | `../../campaigns/<campaign-id>.md` |
| Manifest | `segments/<chronology-segment-id>.md` |
| Segment | `../chronology.md` |
| Segment | `../../../campaigns/<campaign-id>.md` |
| Segment | `../../../entities/beings/<being-id>.md` |
| Segment | `../../../events/<event-id>.md` |
| Segment | `../../../sources/campaigns/<campaign-id>/<source-id>.md` |

Campaigns may add `chronology: ../chronologies/<campaign-id>/chronology.md`. Events may add a `chronology_segments` list of locally supported `{segment, basis, confidence, sources}` entries. Segments may link several events and events several segments. Reciprocal duplication is not required, but supplied links must agree on chronology membership; keep prose in the record where it belongs.

## Templates, examples, and checks

Use the [manifest template](../templates/chronology.md), [segment template](../templates/chronology-segment.md), and [synthetic examples](../docs/chronology-examples.md). Omit unsupported optional values; placeholders are instructions, not data. See [validation](../tools/README.md) for checked constraints and deliberate limitations. No campaign requires chronology and no event requires temporal assertions.
