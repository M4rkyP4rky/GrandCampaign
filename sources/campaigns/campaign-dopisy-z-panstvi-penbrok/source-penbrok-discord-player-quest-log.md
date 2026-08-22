---
id: source-penbrok-discord-player-quest-log
record_type: source
reference_name: Panství Penbrok — Discord player quest log
raw_file: discord_player_questlog.txt
raw_file_sha256: 2918478A11B6F9097C0D441590159F171FF99A1ABA8EBAA66FB103EEF66FFD6D
campaign: ../../../campaigns/campaign-dopisy-z-panstvi-penbrok.md
document_type: player_quest_log
relationship_to_play: played_retrospective
perspective: player_maintained
epistemic_roles:
  - campaign_account
  - retrospective_campaign_notes
  - player_memory
  - player_speculation
  - quest_workflow
---

# Panství Penbrok — Discord player quest log

## Classification

This is a player-maintained quest log and retrospective set of campaign notes. It is not an in-world document, GM preparation, an objective chronology, or a session log. Declarative passages may supplement played events and character or world records, but explanations of hidden causality, history, supernatural mechanisms, and motives remain attributable to this player-side source unless independently supported elsewhere.

The export contains no visible Discord timestamps. Discord message dates, creation or edit timestamps, ordering metadata, and other platform timing information are not used to date fictional events, session order, quest-status changes, or real-world source composition. The checklist order is retained only as source structure.

Sources:

- [Preserved Discord quest log](discord_player_questlog.txt) — complete checklist structure and wording.
- Curator-supplied ingestion instructions on 2026-08-22 — classification, status semantics, timestamp prohibition, marker parsing, and handling of player-memory uncertainty.

## Status-marker semantics

The escaped Discord emoji tokens are workflow annotations, not confidence or truth markers. The raw export contains 21 check-mark occurrences, 18 question-mark occurrences, and one ongoing marker:

- `:white_check_mark:` records that an item was regarded as closed. Closure does not itself establish success; the text supplies any outcome.
- `:question:` records that an item was not marked closed when the quest log stopped being maintained. It does not establish that the fictional issue remained unresolved later and does not make factual statements within the item epistemically uncertain.
- `:arrows_counterclockwise:` records an activity, process, or situation that ran for a period. The source gives no exact start or end for the only such block, `Najímání personálu`.

Nested blockquotes retain their position under the surrounding item. The raw file remains the authoritative checklist representation; no separate quest-management schema is introduced.

Sources:

- [Preserved Discord quest log](discord_player_questlog.txt) — all status-bearing items and nested blockquotes.
- Curator-supplied ingestion instructions on 2026-08-22 — authoritative interpretation of the three workflow markers.

## Stable source locators

The following map-heading blocks are the source's practical locators. Emoji digit sequences are map-marker locators, not fictional names.

| Raw heading | Marker | Persistent identity |
| --- | --- | --- |
| `Hrad Penbrok` | `00` | [Penbrok](../../../entities/locations/location-penbrok-fortress.md) |
| `Problémy vesnice Penbrokton` | `02` | [Penbrokton](../../../entities/locations/location-penbrokton.md) |
| `Čarodějnice Neveah` | `05` | [marker-05 hut and marsh edge](../../../entities/locations/location-penbrok-map-05.md), used as a locator for [Neveah](../../../entities/beings/being-neveah.md) |
| `Morová Blata` | `06` | [Morová Blata](../../../entities/locations/location-penbrok-map-06.md) |
| `Willowburn` | `07` | [Willowburn](../../../entities/locations/location-willowburn.md) |
| `Duhové jezero u Hamsvicu` | `08` | [Duhové jezero u Hamsvicu](../../../entities/locations/location-penbrok-map-08.md) |
| `Hadí jeskyně` | `09` | [Hadí jeskyně](../../../entities/locations/location-penbrok-map-09.md) |
| `Panský dům Shelswell` | `25` | [Usedlost Shelswell](../../../entities/locations/location-shelswell-estate.md) |
| aqueduct references | `26` | [unnamed ancient aqueduct ruins](../../../entities/locations/location-penbrok-map-26.md) |
| `Vypálený klášter Hamswic` | `27` | [Hamswic](../../../entities/locations/location-hamswic.md) |
| `Problémy vesnice Old Chalford` | `50` | [Old Chalford](../../../entities/locations/location-old-chalford.md), with its separately identified [white tower](../../../entities/locations/location-old-chalford-white-tower.md) |
| `Návrší u Inglewoodu` | `72` | [gallows grove at marker 72](../../../entities/locations/location-penbrok-map-72.md), near [Inglewood](../../../entities/locations/location-inglewood.md) |
| Holt reference beside Cecily | `74` | [Holt](../../../entities/locations/location-holt.md) |

These resolutions use the already-ingested regional map and curator key. No numeric pseudo-locations are created.

Sources:

- [Preserved Discord quest log](discord_player_questlog.txt) — heading blocks and inline emoji marker references.
- [Regional-map key source record](source-penbrok-regional-map-key.md#persistent-marker-handling) — persistent identity resolution for markers `00`, `02`, `05`–`09`, `25`–`27`, `50`, `72`, and `74`.

## Named-thing resolution

The complete source was checked for explicit fictional names and distinctive named variants. Existing identities absorb `Nicholas` as Nikolas; Florence; Neveah; Cecilia z Holtu as Cecily; Nathaniel; Cathrin as Katrin; Penbrok and Penbrokton; Willowburn; Egham; Barbara as Barbra; Yann du Bois; Kohouti; Lišky; Hamswic; Shelswell; Old Chalford; Holt; and Inglewood. The heading names `Morová Blata`, `Duhové jezero u Hamsvicu`, `Hadí jeskyně`, `Panský dům Shelswell`, `Vypálený klášter Hamswic`, `Bílá věž`, and `Návrší u Inglewoodu` are attached to their already established marker or associated-site identities.

Three newly encountered proper-named identities required new records: [Pierre](../../../entities/beings/being-pierre-serpents.md), [Viktor](../../../entities/beings/being-viktor-serpents.md), and the military unit [Serpents](../../../entities/organizations/organization-serpents.md). Generic descriptions such as the original lord, lady of the castle, vampire, black carriage, iron priest, paladin, unit commander, poor man, and children are not treated as new proper names. Stronger existing sources resolve the lady's and vampire narrative without turning those descriptive occurrences into duplicate identities.

Sources:

- [Preserved Discord quest log](discord_player_questlog.txt) — complete source-wide name coverage.
- Existing linked entity records and the marker-resolution table above — identity and variant resolution.

## Explicit memory uncertainty

Three passages explicitly qualify the player's memory and remain uncertain recollections rather than contradictions with stronger evidence:

- Under `Hrad Penbrok`, the player does not remember why Neveah altered or botched the curse and speculates about sympathy for the lady's relationship with a vampire.
- Under `Čarodějnice Neveah`, the player remembers almost nothing about that block.
- Under `Willowburn`, the player remembers that something bad happened to participating children but does not remember what, offering infection or possession as guesses. The independently preserved player notes report plague-like marks on the children's palms; the quest log's guesses do not overwrite that more specific account.

Sources:

- [Preserved Discord quest log](discord_player_questlog.txt) — italic memory notes under `Hrad Penbrok`, `Čarodějnice Neveah`, and `Willowburn`.
- [Player-notes source record](source-penbrok-hracske-poznamky.md#block-level-epistemic-handling) — separate handling of player hypotheses and the Willowburn consequence reported in `Sezení 4`.

## Import trace

The supplied UTF-8 text file is preserved byte-for-byte at its permanent campaign-source location. Its SHA-256 digest at successful intake and after the move is `2918478A11B6F9097C0D441590159F171FF99A1ABA8EBAA66FB103EEF66FFD6D`.

Sources:

- [Preserved Discord quest log](discord_player_questlog.txt) — exact imported bytes.
- [Source handling rules](../../README.md) — permanent campaign-source convention and inbox lifecycle.
