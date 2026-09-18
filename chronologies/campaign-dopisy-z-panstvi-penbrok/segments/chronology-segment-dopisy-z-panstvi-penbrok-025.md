---
id: chronology-segment-dopisy-z-panstvi-penbrok-025
record_type: chronology_segment
reference_name: Cesta přes postiženou ves a Hamswic
record_sources:
  - ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
  - ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok-hracske-poznamky.md
  - ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/discord_player_questlog.txt
chronology: ../chronology.md
campaign: ../../../campaigns/campaign-dopisy-z-panstvi-penbrok.md
thread: thread-main
chronology_confidence: high
boundaries:
  - description: The afflicted-village journey and monastery intervention form one connected expedition, with the
      earlier ruin history kept separate.
    basis: The afflicted-village journey and monastery intervention form one connected expedition, with the earlier
      ruin history kept separate. This groups the identified fictional episode or narrative role; the source heading
      alone does not date it.
    confidence: high
    sources:
      - source: ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
        locator: section "Prokletý klášter", village and monastery expedition
      - source: ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok-hracske-poznamky.md
        locator: Sezení 5, Paladin z chrámu, lake, village and Chrám
      - source: ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/discord_player_questlog.txt
        locator: Vypálený klášter Hamswic, abductions, recovered victim and priest’s defeat
source_spans:
  - source: ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
    locator: section "Prokletý klášter", village and monastery expedition
  - source: ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok-hracske-poznamky.md
    locator: Sezení 5, Paladin z chrámu, lake, village and Chrám
  - source: ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/discord_player_questlog.txt
    locator: Vypálený klášter Hamswic, abductions, recovered victim and priest’s defeat
events:
  - event: ../../../events/event-cursed-monastery-expedition.md
    basis: The village rescue and monastery intervention match the existing expedition; the temple/monastery identity
      uses the already recorded curator resolution.
    confidence: high
    sources:
      - source: ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
        locator: section "Prokletý klášter", village and monastery expedition
      - source: ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok-hracske-poznamky.md
        locator: Sezení 5, Paladin z chrámu, lake, village and Chrám
      - source: ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/discord_player_questlog.txt
        locator: Vypálený klášter Hamswic, abductions, recovered victim and priest’s defeat
participants:
  - entity: ../../../entities/beings/person-yann-du-bois.md
    basis: Yann du Bois is identified in this passage in the described role. Inclusion is scoped to this episode;
      a writer, retrospective subject or staffing candidate is not thereby physically present in every narrated
      scene.
    confidence: high
    sources:
      - source: ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
        locator: section "Prokletý klášter", village and monastery expedition
      - source: ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok-hracske-poznamky.md
        locator: Sezení 5, Paladin z chrámu, lake, village and Chrám
      - source: ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/discord_player_questlog.txt
        locator: Vypálený klášter Hamswic, abductions, recovered victim and priest’s defeat
  - entity: ../../../entities/beings/person-nathaniel-hargreve.md
    basis: Nathaniel Hargreve is identified in this passage in the described role. Inclusion is scoped to this episode;
      a writer, retrospective subject or staffing candidate is not thereby physically present in every narrated
      scene.
    confidence: high
    sources:
      - source: ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
        locator: section "Prokletý klášter", village and monastery expedition
      - source: ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok-hracske-poznamky.md
        locator: Sezení 5, Paladin z chrámu, lake, village and Chrám
      - source: ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/discord_player_questlog.txt
        locator: Vypálený klášter Hamswic, abductions, recovered victim and priest’s defeat
  - entity: ../../../entities/beings/person-oswyn-waldergrave.md
    basis: Oswyn Waldegrave is identified in this passage in the described role. Inclusion is scoped to this episode;
      a writer, retrospective subject or staffing candidate is not thereby physically present in every narrated
      scene.
    confidence: high
    sources:
      - source: ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
        locator: section "Prokletý klášter", village and monastery expedition
      - source: ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok-hracske-poznamky.md
        locator: Sezení 5, Paladin z chrámu, lake, village and Chrám
      - source: ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/discord_player_questlog.txt
        locator: Vypálený klášter Hamswic, abductions, recovered victim and priest’s defeat
locations:
  - location: ../../../entities/locations/location-hamswic.md
    basis: The passage identifies the monastery episode; the existing curator resolution supplies the two-visit
      site equivalence where the account is unnamed.
    confidence: high
    sources:
      - source: ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
        locator: section "Prokletý klášter", village and monastery expedition
      - source: ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok-hracske-poznamky.md
        locator: Sezení 5, Paladin z chrámu, lake, village and Chrám
      - source: ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/discord_player_questlog.txt
        locator: Vypálený klášter Hamswic, abductions, recovered victim and priest’s defeat
    curator_clarification:
      record: ../../../curation/resolved.md
      locator: curation-penbrok-005
relations:
  - type: continues_to
    target: chronology-segment-dopisy-z-panstvi-penbrok-027.md
    certainty: exact-at-precision
    basis: The short letter reports these completed recent events. This is narrative traversal, not an independently
      dated ordering or adjacency claim.
    confidence: high
    sources:
      - source: ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
        locator: section "Prokletý klášter", letter frame, messenger warning, thanks and proposed remittance
  - type: continues_to
    target: chronology-segment-dopisy-z-panstvi-penbrok-026.md
    certainty: exact-at-precision
    basis: This callback separates earlier reported history from the current reporting scene. This is narrative
      traversal, not an independently dated ordering or adjacency claim.
    confidence: high
    sources:
      - source: ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/discord_player_questlog.txt
        locator: Vypálený klášter Hamswic, internal explosion item
  - type: precedes
    target: chronology-segment-dopisy-z-panstvi-penbrok-027.md
    certainty: exact-at-precision
    basis: The short letter describes the intervention as already accomplished.
    confidence: high
    sources:
      - source: ../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
        locator: section "Prokletý klášter", completed monastery intervention
---

# Cesta přes postiženou ves a Hamswic

## Summary

The notes recount the lake, village, Toby’s return and the armored paladin at the temple. The letter reports ending the demonic presence; the quest log reports the iron priest’s defeat and says the victim survived because the snake was already dead. No occurred snake-killing episode or precise death time is invented from that retrospective explanation.

Sources:

- [Permanent Penbrok.xml](../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml) — section "Prokletý klášter", village and monastery expedition.
- [Permanent Penbrok-hracske-poznamky.md](../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok-hracske-poznamky.md) — Sezení 5, Paladin z chrámu, lake, village and Chrám.
- [Permanent discord_player_questlog.txt](../../../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/discord_player_questlog.txt) — Vypálený klášter Hamswic, abductions, recovered victim and priest’s defeat.
