---
id: <event-stable-id>
record_type: event
reference_name: <event title>
# Optional temporal.assertions and chronology_segments: see instructions below.
time:
  description: <human-readable interval or uncertainty>
  start:
    precision: <exact-datetime | exact-date | year | approximate-year | century | age | broad | unknown>
    year_ap: <negative before 0, zero at the epoch, positive after 0>
  end:
    precision: <precision supported for the end>
    year_ap: <negative before 0, zero at the epoch, positive after 0>
  sources:
    - <relative link supporting this time block>
locations:
  - location: <relative link to relevant location>
    sources:
      - <relative link supporting this relationship>
entities:
  - entity: <relative link to relevant entity>
    sources:
      - <relative link supporting this relationship>
accounts:
  - kind: <campaign-account | legend | gm-reconstruction>
    source: <relative link to source or account>
    locator: <optional human-readable section or block locator>
    summary: <what this perspective reports>
---

# <event title>

## Description

<Description that preserves disagreement and does not promote one account to objective truth.>

Sources:

- [<source label>](<relative path>) — <what this source supports in this section>

## Template instructions: optional chronology and assertions

<Omit unsupported optional fields. Existing time remains valid without temporal.assertions; neither overrides the other and duplication is unnecessary. Consult docs/temporal-model.md and docs/chronology-examples.md before adding assertions. Remove these instructions from a persistent record.>

```yaml
temporal:
  assertions:
    - kind: absolute
      property: placement
      precision: year
      certainty: exact-at-precision
      value:
        year_ap: <signed attested AP year; no default month/day>
      basis: <what establishes this time>
      confidence: <high | medium | low>
      sources:
        - source: ../sources/campaigns/<campaign-id>/<source-id>.md
          locator: <supporting passage>
chronology_segments:
  - segment: ../chronologies/<campaign-id>/segments/<chronology-segment-id>.md
    basis: <why this event belongs in the segment>
    confidence: <high | medium | low>
    sources:
      - source: ../sources/campaigns/<campaign-id>/<source-id>.md
        locator: <supporting passage>
```
