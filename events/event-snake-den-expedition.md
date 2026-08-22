---
id: event-snake-den-expedition
record_type: event
reference_name: Výprava do hadího doupěte
time:
  description: Fictional date and duration are not recorded; Yann presents the expedition after the group's establishment at Penbrok and before its journey to Willowburn.
  sources:
    - ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
locations:
  - location: ../entities/locations/location-penbrok-map-09.md
    sources:
      - ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok-hracske-poznamky.md
      - ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/discord_player_questlog.txt
entities:
  - entity: ../entities/beings/person-yann-du-bois.md
    sources:
      - ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
  - entity: ../entities/beings/person-nathaniel-hargreve.md
    sources:
      - ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
  - entity: ../entities/beings/person-oswyn-waldergrave.md
    sources:
      - ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
  - entity: ../entities/beings/being-pierre-serpents.md
    sources:
      - ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/discord_player_questlog.txt
  - entity: ../entities/beings/being-viktor-serpents.md
    sources:
      - ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/discord_player_questlog.txt
  - entity: ../entities/organizations/organization-serpents.md
    sources:
      - ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/discord_player_questlog.txt
accounts:
  - kind: campaign-account
    source: ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
    locator: section "Hadí doupě"
    summary: In Hadí doupě, Yann reports an expedition to caves associated with stories of a giant snake, an encounter with Imperial soldiers, and no encounter with the snake itself.
  - kind: player-notes
    source: ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok-hracske-poznamky.md
    locator: section "Sezení 3"
    summary: The notes report the cave expedition, soldiers, sacrifices, and two recruited survivors while explicitly marking several conclusions about the cult, armor-making, and causation as appearances or probabilities.
  - kind: player-retrospective
    source: ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/discord_player_questlog.txt
    locator: marker `09`, `Hadí jeskyně`
    summary: The quest log says the group obtained snake skin, dispersed the Serpents soldiers who used human sacrifice and alchemy to make equipment, and defeated the iron priest who brought victims.
---

# Výprava do hadího doupěte

## Description

Yann reports that Nathaniel responded to local stories of a giant snake by leading an expedition into caves. He says the group incapacitated Imperial soldiers whom he believed were under dark magical influence and recruited two survivors, while the alleged giant snake was not encountered. The quest log names the soldiers' unit [Serpents](../entities/organizations/organization-serpents.md), names the two later-serving soldiers Pierre and Viktor, confirms acquisition of shed snake skin, and reports the defeat of the unnamed iron priest. The claimed magic, sacrifices, alchemical purpose, and causal explanation remain player-side accounts.

Sources:

- [Raw correspondence](../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml) — section `Hadí doupě`.
- [Player notes](../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok-hracske-poznamky.md) — `Sezení 3`, preserving the account's observations and hypotheses separately.
- [Discord player quest log](../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/discord_player_questlog.txt) — marker `09`, closed snake-cave items.
