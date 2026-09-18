---
id: chronology-segment-<campaign-slug>-<stable-suffix>
record_type: chronology_segment
reference_name: <segment label>
record_sources:
  - ../../../sources/campaigns/<campaign-id>/<source-id>.md
chronology: ../chronology.md
campaign: ../../../campaigns/<campaign-id>.md
thread: thread-<stable-suffix>
chronology_confidence: <high | medium | low>
boundaries:
  - description: <why this material is grouped as one segment>
    basis: <evidenced boundary or explicit mechanical grouping>
    confidence: <high | medium | low>
    sources:
      - source: ../../../sources/campaigns/<campaign-id>/<source-id>.md
        locator: <source-native span>
source_spans:
  - source: ../../../sources/campaigns/<campaign-id>/<source-id>.md
    locator: <coverage; not a substitute for local support>
participants:
  - entity: ../../../entities/beings/<being-id>.md
    basis: <why this resolved identity participates>
    confidence: <high | medium | low>
    sources:
      - source: ../../../sources/campaigns/<campaign-id>/<source-id>.md
        locator: <supporting passage>
locations:
  - location: ../../../entities/locations/<location-id>.md
    basis: <why this location applies>
    confidence: <high | medium | low>
    sources:
      - source: ../../../sources/campaigns/<campaign-id>/<source-id>.md
        locator: <supporting passage>
events:
  - event: ../../../events/<event-id>.md
    basis: <why the event belongs in this segment>
    confidence: <high | medium | low>
    sources:
      - source: ../../../sources/campaigns/<campaign-id>/<source-id>.md
        locator: <supporting passage>
relations:
  - type: continues_to
    target: chronology-segment-<campaign-slug>-<other-suffix>.md
    certainty: exact-at-precision
    basis: <narrative continuity only; no temporal order implied>
    confidence: <high | medium | low>
    sources:
      - source: ../../../sources/campaigns/<campaign-id>/<source-id>.md
        locator: <support for this individual edge>
---

# <segment label>

## Summary

<Concise derived summary; zero, one, or multiple events may be linked.>

Sources:

- [<source label>](../../../sources/campaigns/<campaign-id>/<source-id>.md) — <specific supporting span>

## Temporal evidence and notes

<Optional temporal.assertions uses the shared temporal model. Preserve exact wording and locators when useful; do not promote source timestamps into fictional dates. Support every factual block locally.>

## Template instructions

<Save beneath chronologies/<campaign-id>/segments/ using the stable ID filename. All paths above are destination-relative. Remove unsupported optional lists, including events; remove these instructions.>
