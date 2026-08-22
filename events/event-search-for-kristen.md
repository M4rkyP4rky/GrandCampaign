---
id: event-search-for-kristen
record_type: event
reference_name: Pátrání po Kristen
time:
  description: Fictional dates and total duration are not recorded; Yann presents a search beginning after the group's arrival at Penbrok and ending when Kristen is found at Darkwood.
  sources:
    - ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
locations:
  - location: ../entities/locations/location-penbrok-fortress.md
    sources:
      - ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
  - location: ../entities/locations/location-rumcombe.md
    sources:
      - ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
  - location: ../entities/locations/location-forgotton.md
    sources:
      - ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok-hracske-poznamky.md
  - location: ../entities/locations/location-darkwood.md
    sources:
      - ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
      - ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/source-penbrok-hracske-poznamky.md
entities:
  - entity: ../entities/beings/person-kristen-penbrok.md
    sources:
      - ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
  - entity: ../entities/beings/person-nathaniel-hargreve.md
    sources:
      - ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
  - entity: ../entities/beings/person-oswyn-waldergrave.md
    sources:
      - ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
  - entity: ../entities/beings/person-yann-du-bois.md
    sources:
      - ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
  - entity: ../entities/beings/being-pani-vran.md
    sources:
      - ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
      - ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok-hracske-poznamky.md
  - entity: ../entities/beings/being-sir-desmond.md
    sources:
      - ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
      - ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok-hracske-poznamky.md
accounts:
  - kind: campaign-account
    source: ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml
    locator: sections "Dobytí Penbroku", "Hladovějící z Willowburnu", "Prokletý klášter", "Paní vran", and "Upír"
    summary: Across several letters, Yann reports clues at Penbrok, information obtained through Neveah, encounters during a search through Rumcombe and an unnamed village, Desmond's lead, and finally finding Kristen at Darkwood.
  - kind: player-notes
    source: ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok-hracske-poznamky.md
    locator: sections "Sezení 3" through "Sezení 7"
    summary: The notes preserve developing clues, player hypotheses, Neveah's reported explanation, the search through Rumcombe and Forgotton, Desmond's lead, and finding Kristen at Darkwood. The explicit "Co postavy neví" block in Sezení 4 remains GM/meta information outside Yann's knowledge.
  - kind: player-retrospective
    source: ../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/discord_player_questlog.txt
    locator: marker `00`, open curse block, nested item beginning `Po smrti pána`
    summary: The quest log says the lady of Penbrok tried for a time to break the curse with Florence, gave up, and was taken away by a black carriage; the item was not marked closed, but the source's later maintenance gap does not establish permanent non-resolution.
---

# Pátrání po Kristen

## Description

Yann's letters gradually report a search for the missing Kristen. He withholds or labels some early conclusions as speculation, later says the witch Neveah provided sensitive information he would not disclose, and describes encounters with [Paní Vran](../entities/beings/being-pani-vran.md) and a lead from [Sir Desmond](../entities/beings/being-sir-desmond.md) before claiming the group found Kristen at Darkwood. The player notes name the memory-affecting village [Forgotton](../entities/locations/location-forgotton.md). The player notes and curator clarification establish that Yann learned of Kirsten's involvement with a vampire during the `Sezení 5` visit to Neveah; they do not thereby establish every hidden detail or the vampire's identity. The record preserves the remaining omissions, uncertainty, and attributions rather than reconstructing missing chronology.

The quest log contributes an open-item retrospective that she tried to break the curse with Florence and was later taken away in a black carriage. Its open status is not treated as evidence that the search stayed unresolved, since stronger played sources record that Kristen was found.

Sources:

- [Raw correspondence](../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml) — sections `Dobytí Penbroku`, `Hladovějící z Willowburnu`, `Prokletý klášter`, `Paní vran`, and `Upír`.
- [Player notes](../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok-hracske-poznamky.md) — `Sezení 3` through `Sezení 7`, with hypotheses and GM/meta knowledge kept distinct from the played account.
- [Player-notes source metadata](../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/source-penbrok-hracske-poznamky.md#curator-corrections) — curator-supplied clarification that the Darkwood destination is the castle.
- Curator-supplied character-knowledge clarification during curation review on 2026-08-21 — Yann learned about Kirsten and a vampire during the `Sezení 5` visit to Neveah.
- [Discord player quest log](../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/discord_player_questlog.txt) — marker `00`, nested open item about the lady's departure.
