---
id: event-cursed-monastery-expedition
record_type: event
reference_name: Výprava do prokletého kláštera
time:
  description: The event occurred during podzim 1652 poPA; its exact month, day, and duration are not recorded. Yann presents the expedition after his marriage and after Maxmillian de Juive's arrival at Penbrok.
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
locations:
  - location: ../entities/locations/location-hamswic.md
    sources:
      - ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
      - ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok-hracske-poznamky.md
      - ../curation/resolved.md#curation-penbrok-005--identity-of-the-two-monasteries
entities:
  - entity: ../entities/beings/being-maxmillian-de-juive.md
    sources:
      - ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
      - ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok-hracske-poznamky.md
  - entity: ../entities/beings/person-yann-du-bois.md
    sources:
      - ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
  - entity: ../entities/beings/person-nathaniel-hargreve.md
    sources:
      - ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
  - entity: ../entities/beings/person-oswyn-waldergrave.md
    sources:
      - ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
accounts:
  - kind: campaign-account
    source: ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
    locator: section "Prokletý klášter"
    summary: In Prokletý klášter, Yann reports that the group explored a forgotten monastery near an unnamed afflicted village and dispersed what he calls a demon's presence.
  - kind: player-notes
    source: ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok-hracske-poznamky.md
    locator: section "Sezení 5"
    summary: The notes describe the afflicted village, crystalline mud and small gems, numbered graves, and an armored paladin in a place headed "Chrám"; they do not name the village, establish a fictional date, or themselves identify this place with the later monastery.
  - kind: player-retrospective
    source: ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/discord_player_questlog.txt
    locator: marker `27`, `Vypálený klášter Hamswic`
    summary: The quest log names the place Hamswic, describes its cemetery and pipe system, reports disappearances in a nearby settlement, and says the abducted poor man survived before the group defeated the iron priest.
---

# Výprava do prokletého kláštera

## Description

Yann says the group visited an unnamed village troubled by a curse, apparitions, disappearances, and disability, then explored the monastery Hamswic and ended a demonic presence. The earlier correspondence and player notes do not name the village or monastery, supply a fictional date, or establish identity with the later site; the quest log now independently uses `Hamswic` for marker `27` but does not itself establish the two-visit equivalence. The earlier curator resolution remains the basis for that equivalence.

The quest log clarifies that the abducted poor man was found frightened but unharmed and that the iron priest was defeated. It attributes the victim's survival to the snake already being dead. The open or closed workflow states of the surrounding items do not change the epistemic status of those player-retrospective claims.

Sources:

- [Raw correspondence](../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml) — section `Prokletý klášter`.
- [Player notes](../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok-hracske-poznamky.md) — `Sezení 5`, a more detailed but still perspective-bound player account.
- [Curation resolution](../curation/resolved.md#curation-penbrok-005--identity-of-the-two-monasteries) — curator-supplied monastery name and equivalence with the later site.
- [Discord player quest log](../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/discord_player_questlog.txt) — marker `27`, Hamswic structures, disappearances, rescue, and iron-priest outcome.
