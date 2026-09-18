# Synthetic chronology examples

These are invented schema demonstrations, **not campaign lore or materialized records**. The numbers, labels, and placeholder links establish no fictional facts. Paths assume a segment in `chronologies/<campaign-id>/segments/`; replace placeholders with inspected existing identities and evidence. Each list item carries independent local support even when the examples repeat a source.

## Absolute, approximate, and bounded time

```yaml
temporal:
  assertions:
    - kind: absolute
      property: start
      precision: exact-date
      certainty: exact-at-precision
      value:
        year_ap: -20
        month: 3
        day: 12
      basis: "Synthetic example: the source explicitly dates the start."
      confidence: high
      sources:
        - source: ../../../sources/campaigns/<campaign-id>/<source-id>.md
          locator: <exact day-level statement>
    - kind: absolute
      property: placement
      precision: year
      certainty: exact-at-precision
      value:
        year_ap: 1032
      basis: "Synthetic year-only claim; no month or day is established."
      confidence: high
      sources:
        - source: ../../../sources/campaigns/<campaign-id>/<source-id>.md
          locator: <year-only statement>
    - kind: absolute
      property: placement
      precision: approximate-year
      certainty: approximate
      value:
        year_ap: 1030
      basis: "Synthetic approximate alternative account, retained separately."
      confidence: medium
      sources:
        - source: ../../../sources/campaigns/<campaign-id>/<other-source-id>.md
          locator: <approximate dating passage>
    - kind: bounded
      property: start
      precision: broad
      certainty: bounded
      earliest:
        precision: year
        year_ap: 1031
      latest:
        precision: exact-date
        year_ap: 1033
        month: 2
        day: 7
      basis: "Synthetic start window with differently precise bounds; not duration."
      confidence: medium
      sources:
        - source: ../../../sources/campaigns/<campaign-id>/<source-id>.md
          locator: <passages supporting both limits>
```

These claims illustrate coexistence, not a coherent solved timeline. The start in year -20 and the start window in years 1031–1033 would be reported as conflicting comparable constraints if attached to one real record. Approximate claims must not be silently tightened to exact bounds.

## Relative before/after and ordering only

```yaml
temporal:
  assertions:
    - kind: relative
      property: start
      precision: broad
      certainty: approximate
      target: ../../../events/<event-id>.md
      target_property: end
      direction: after
      offset:
        value: 2
        unit: day
      basis: "Synthetic evidence says about two days after the other event ended."
      confidence: medium
      sources:
        - source: ../../../sources/campaigns/<campaign-id>/<source-id>.md
          locator: <relative dating statement>
    - kind: relative
      property: end
      precision: unknown
      certainty: exact-at-precision
      target: chronology-segment-<campaign-slug>-<later-suffix>.md
      target_property: start
      direction: before
      basis: "Synthetic evidence establishes only that this ends before that starts."
      confidence: high
      sources:
        - source: ../../../sources/campaigns/<campaign-id>/<source-id>.md
          locator: <ordering statement>
```

## Narrative split and rejoin

At the parent segment, declare each branch separately:

```yaml
relations:
  - type: splits_into
    target: chronology-segment-<campaign-slug>-<branch-a>.md
    certainty: exact-at-precision
    basis: "Synthetic narrative moves to branch A; no fictional date implied."
    confidence: high
    sources:
      - source: ../../../sources/campaigns/<campaign-id>/<source-id>.md
        locator: <branch A transition>
  - type: splits_into
    target: chronology-segment-<campaign-slug>-<branch-b>.md
    certainty: exact-at-precision
    basis: "Synthetic narrative also follows branch B; concurrence is unknown."
    confidence: high
    sources:
      - source: ../../../sources/campaigns/<campaign-id>/<source-id>.md
        locator: <branch B transition>
```

At each branch that rejoins, record its independently evidenced edge:

```yaml
relations:
  - type: rejoins
    target: chronology-segment-<campaign-slug>-<reunion>.md
    certainty: exact-at-precision
    basis: "Synthetic branch rejoins narrative here; temporal order needs separate evidence."
    confidence: high
    sources:
      - source: ../../../sources/campaigns/<campaign-id>/<source-id>.md
        locator: <this branch's reunion passage>
```

A `continues_to` edge uses the same fields. It can lead into a retrospective. A split/rejoin graph alone establishes neither simultaneity nor temporal adjacency.

## Simultaneity and qualified overlap

```yaml
relations:
  - type: simultaneous_with
    target: chronology-segment-<campaign-slug>-<other-suffix>.md
    certainty: exact-at-precision
    basis: "Synthetic narrator explicitly places both scenes at the same time; duration is unknown."
    confidence: high
    sources:
      - source: ../../../sources/campaigns/<campaign-id>/<source-id>.md
        locator: <simultaneity statement>
  - type: probably_parallel_with
    target: chronology-segment-<campaign-slug>-<third-suffix>.md
    certainty: uncertain
    basis: "Synthetic interpretation suggests overlap but cannot prove it."
    confidence: low
    sources:
      - source: ../../../sources/campaigns/<campaign-id>/<source-id>.md
        locator: <evidence behind the hypothesis>
```

`overlaps` uses the same local fields and requires evidence of shared fictional time. Events may express these using `kind: relation`, `property: placement`, `target_property: placement`, `precision: unknown`, and `relation: simultaneous_with` (or another temporal relation), retaining certainty and local support.

## Manifest anchor and curator support

From `chronologies/<campaign-id>/chronology.md`:

```yaml
temporal:
  assertions:
    - subject: segments/chronology-segment-<campaign-slug>-<opening>.md
      kind: absolute
      property: placement
      precision: year
      certainty: exact-at-precision
      value:
        year_ap: 1032
      basis: "Synthetic curator clarification dates this segment only."
      confidence: high
      curator_clarification:
        record: ../../curation/resolved.md
        locator: <stable curation item ID with explicit decision>
```

The curator record must actually preserve that decision. It is not enough to link an unresolved question or cite conversation memory. Corrections preserve both source-stated and corrected values under the existing provenance policy.
