---
id: event-yann-barbra-marriage
record_type: event
reference_name: Sňatek Yanna a Barbry
time:
  description: The marriage occurred during podzim 1652 poPA; its exact month and day are not recorded. Played sources place it after the Willowburn engagement and before the expedition to Hamswic.
  start:
    precision: broad
    year_ap: 1652
    season: podzim
  end:
    precision: broad
    year_ap: 1652
    season: podzim
  sources:
    - Curator-supplied campaign chronology on 2026-08-22
    - ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
    - ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok-hracske-poznamky.md
    - ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/discord_player_questlog.txt
entities:
  - entity: ../entities/beings/person-yann-du-bois.md
    sources:
      - ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
      - ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok-hracske-poznamky.md
      - ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/discord_player_questlog.txt
  - entity: ../entities/beings/person-barbra.md
    sources:
      - ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
      - ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok-hracske-poznamky.md
      - ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/discord_player_questlog.txt
accounts:
  - kind: campaign-account
    source: ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
    locator: section "Prokletý klášter"
    summary: Yann reports that he married Barbra.
  - kind: player-notes
    source: ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok-hracske-poznamky.md
    locator: section "Sezení 5"
    summary: The notes treat Barbra as Yann's wife during the subsequent play.
  - kind: player-retrospective
    source: ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/discord_player_questlog.txt
    locator: marker `02`, closed item `Barbara si vzala Yanna du Bois`
    summary: The closed quest-log item directly records the marriage; its wording, not the check mark alone, supports the outcome.
---

# Sňatek Yanna a Barbry

## Description

Three player-side sources support that Yann and Barbra married. The quest log spells her name `Barbara`; the continuous relationship and existing source variants resolve this to [Barbra](../entities/beings/person-barbra.md), not a new being. No exact fictional date is inferred.

Sources:

- [Raw correspondence](../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml) — section `Prokletý klášter`.
- [Player notes](../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok-hracske-poznamky.md) — `Sezení 5`.
- [Discord player quest log](../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/discord_player_questlog.txt) — marker `02`, closed marriage item.
