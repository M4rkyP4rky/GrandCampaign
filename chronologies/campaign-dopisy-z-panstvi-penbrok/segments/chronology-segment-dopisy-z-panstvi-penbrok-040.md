---
id: chronology-segment-dopisy-z-panstvi-penbrok-040
record_type: chronology_segment
reference_name: Dopsání darkwoodského dopisu na slunci
record_sources:
  - ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
chronology: ../chronology.md
campaign: ../../../campaigns/campaign-dopisy-z-panstvi-penbrok.md
thread: thread-main
chronology_confidence: high
boundaries:
  - description: The source explicitly resumes and finishes the unfinished letter from a new current location.
    basis: The source explicitly resumes and finishes the unfinished letter from a new current location. This groups
      the identified fictional episode or narrative role; the source heading alone does not date it.
    confidence: high
    sources:
      - source: ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
        locator: section "Dívky a dámy v nesnázích", "Dopsáno", "zakončil tento dopis", current camp and closing
          summons
source_spans:
  - source: ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
    locator: section "Dívky a dámy v nesnázích", "Dopsáno", "zakončil tento dopis", current camp and closing summons
participants:
  - entity: ../../../entities/beings/person-yann-du-bois.md
    basis: Yann du Bois is identified in this passage in the described role. Inclusion is scoped to this episode;
      a writer, retrospective subject or staffing candidate is not thereby physically present in every narrated
      scene.
    confidence: high
    sources:
      - source: ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
        locator: section "Dívky a dámy v nesnázích", "Dopsáno", "zakončil tento dopis", current camp and closing
          summons
locations:
  - location: ../../../entities/locations/location-penbrok-map-33.md
    basis: The identified source passage places this episode at this already resolved site; marker numbers are locators,
      not newly assigned fictional names.
    confidence: high
    sources:
      - source: ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
        locator: section "Dívky a dámy v nesnázích", "Dopsáno", "zakončil tento dopis", current camp and closing
          summons
relations:
  - type: continues_to
    target: chronology-segment-dopisy-z-panstvi-penbrok-041.md
    certainty: exact-at-precision
    basis: The next letter explicitly resumes the return from the camp. This is narrative traversal, not an independently
      dated ordering or adjacency claim.
    confidence: high
    sources:
      - source: ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
        locator: section "Vrátila se snad válka?", journey from camp, wolves and chapel
      - source: ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok-hracske-poznamky.md
        locator: Sezení 9, morning wolves, village 32, night watch and departure before dawn
  - type: precedes
    target: chronology-segment-dopisy-z-panstvi-penbrok-041.md
    certainty: exact-at-precision
    basis: The next letter explicitly resumes the journey from the camp from which the writer wrote last.
    confidence: high
    sources:
      - source: ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
        locator: section "Vrátila se snad válka?", "z vojenského ležení, ze kterého jsem psal posledně"
temporal:
  assertions:
    - kind: relative
      property: placement
      precision: unknown
      certainty: exact-at-precision
      target: chronology-segment-dopisy-z-panstvi-penbrok-036.md
      target_property: placement
      direction: after
      basis: The same letter resumes at the camp after the shed draft and underground escape; the change of composition
        site and fictional action support later writing without a numeric gap.
      confidence: high
      sources:
        - source: ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
          locator: section "Upír", unfinished shed draft
        - source: ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
          locator: section "Dívky a dámy v nesnázích", resumed same letter and current camp
    - kind: relative
      property: placement
      precision: unknown
      certainty: exact-at-precision
      target: chronology-segment-dopisy-z-panstvi-penbrok-039.md
      target_property: start
      direction: after
      basis: The writer is now at the refuge reached after leaving Darkwood. This follows the reunion/departure
        segment’s start, not necessarily the end of all its camp activities or its private hunger disclosure.
      confidence: high
      sources:
        - source: ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
          locator: section "Dívky a dámy v nesnázích", current camp after flight
        - source: ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok-hracske-poznamky.md
          locator: Sezení 8, reunion, departure and arrival at camp 33
---

# Dopsání darkwoodského dopisu na slunci

## Summary

Yann finishes the same Darkwood letter at the abandoned camp, in haste and sunlight. He retrospectively describes the underground escape and expresses concern about Kirsten among the mercenaries; Nathaniel calls him to confer. The writing location differs from the earlier shed, with no stated numeric gap.

Sources:

- [Permanent Penbrok.xml](../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml) — section "Dívky a dámy v nesnázích", "Dopsáno", "zakončil tento dopis", current camp and closing summons.
