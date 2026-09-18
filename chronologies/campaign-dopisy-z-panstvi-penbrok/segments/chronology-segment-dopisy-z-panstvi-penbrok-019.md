---
id: chronology-segment-dopisy-z-panstvi-penbrok-019
record_type: chronology_segment
reference_name: Třetí psaní s obráceným vyprávěním
record_sources:
  - ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
chronology: ../chronology.md
campaign: ../../../campaigns/campaign-dopisy-z-panstvi-penbrok.md
thread: thread-main
chronology_confidence: high
boundaries:
  - description: The explicit backward narration is preserved in its own composition frame instead of treating the
      opening paragraph as the first fictional event.
    basis: The explicit backward narration is preserved in its own composition frame instead of treating the opening
      paragraph as the first fictional event. This groups the identified fictional episode or narrative role; the
      source heading alone does not date it.
    confidence: high
    sources:
      - source: ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
        locator: section "Hladovějící z Willowburnu", letter label, opening and previous-day carving through funding
          request
source_spans:
  - source: ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
    locator: section "Hladovějící z Willowburnu", letter label, opening and previous-day carving through funding
      request
participants:
  - entity: ../../../entities/beings/person-yann-du-bois.md
    basis: Yann du Bois is identified in this passage in the described role. Inclusion is scoped to this episode;
      a writer, retrospective subject or staffing candidate is not thereby physically present in every narrated
      scene.
    confidence: high
    sources:
      - source: ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
        locator: section "Hladovějící z Willowburnu", letter label, opening and previous-day carving through funding
          request
relations:
  - type: continues_to
    target: chronology-segment-dopisy-z-panstvi-penbrok-023.md
    certainty: exact-at-precision
    basis: The following letter acknowledges funds and the completed marriage. This is narrative traversal, not
      an independently dated ordering or adjacency claim.
    confidence: high
    sources:
      - source: ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
        locator: section "Prokletý klášter", thanks for funds, accountant’s first days and completed wedding
      - source: ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok-hracske-poznamky.md
        locator: Sezení 5, Barbra and Maxmilián
      - source: ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/discord_player_questlog.txt
        locator: Problémy vesnice Penbrokton, Barbara si vzala Yanna du Bois
temporal:
  assertions:
    - kind: relative
      property: placement
      precision: day
      certainty: exact-at-precision
      target: chronology-segment-dopisy-z-panstvi-penbrok-016.md
      target_property: placement
      direction: after
      basis: The new carving decorates Willowburn after yesterday. This is a previous-day composition relation for
        the carving only, not a timestamp for the whole Willowburn adventure.
      confidence: high
      sources:
        - source: ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
          locator: section "Hladovějící z Willowburnu", "po včerejšku" new carving
      offset:
        value: 1
        unit: day
---

# Třetí psaní s obráceným vyprávěním

## Summary

Yann writes again sooner than expected about the past days. He explicitly begins at the end, then returns to Willowburn, and asks for marriage funding. The previous-day carving cue dates only that outcome relative to composition. The tower outcome, earlier Willowburn episode and earlier plague story are distinct temporal layers.

Sources:

- [Permanent Penbrok.xml](../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml) — section "Hladovějící z Willowburnu", letter label, opening and previous-day carving through funding request.
