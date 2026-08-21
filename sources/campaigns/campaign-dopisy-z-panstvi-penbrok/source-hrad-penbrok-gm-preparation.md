---
id: source-hrad-penbrok-gm-preparation
record_type: source
reference_name: Hrad Penbrok — GM preparation
raw_file: 000-Hrad-Penbrok.docx
raw_file_sha256: 24DF7D73FB5A492D37E80618082EACA3C9A83234DB21E49A89682849EDBF75D1
campaign: ../../../campaigns/campaign-dopisy-z-panstvi-penbrok.md
document_type: gm_preparation
relationship_to_play: pre_play
perspective: gm
epistemic_roles:
  - prepared_baseline
  - hidden_gm_information
  - established_backstory
  - npc_knowledge_and_motivation
  - planned_contingency
  - game_procedure
  - random_possibility
  - draft_incomplete
  - keyed_location_reference
  - map_reference
docx_package_metadata:
  creator: Filip Dvořák
  last_modified_by: Filip Dvořák
  created_utc: "2022-11-29T18:27:00Z"
  modified_utc: "2022-11-29T18:29:00Z"
  revision: 3
  pages_reported: 2
  words_reported: 620
curator_corrections:
  - field: composed_map_marker_position
    locator: text key 16 "Čapí hnízdo" and final map page
    source_value: marker 16 omitted from the drawing layer
    corrected_value: marker 16 belongs in the tower above markers 11 and 15
    provenance: curator-supplied correction during curation review on 2026-08-21
---

# Hrad Penbrok — GM preparation

## Classification and document metadata

This is pre-play GM preparation for `Hrad Penbrok` in the campaign `Panství Penbrok`. It supplies a prepared starting state, hidden backstory and mechanisms, NPC knowledge and motivations, encounter procedures, contingencies, draft fragments, keyed location descriptions, and a composed castle map. It is evidence for what was prepared, not by itself evidence that a possible action or outcome occurred in play.

The DOCX package names `Filip Dvořák` as its creator and last modifier. Those fields are preserved as document-package provenance only; no curator-supplied real-world authorship was provided, so the package metadata is not promoted to an authoritative real-world author claim. The creation and modification timestamps are real-world document metadata, not fictional dates or session dates.

Provenance:

- Curator instructions accompanying the ingestion request on 2026-08-21 — campaign association, pre-play classification, and interpretation rules.
- [Preserved GM preparation](000-Hrad-Penbrok.docx) — document content, package properties, keyed headings, and composed visual material.

## Epistemic handling

| Source material | Archive treatment |
| --- | --- |
| Opening description and declarative hidden-background passages under `Panoš a koně`, `Ohnivec`, and `Žaba na prameni` | Prepared fictional baseline or established backstory. It may support a GM/world-state reconstruction while remaining distinct from character knowledge and from later played changes. |
| Statements about what Lawrence, Nicholas, the bandits, Cecily, or Kirsten know, believe, want, or intend | Prepared NPC knowledge, motivation, or intention. An intention is not an event that occurred. |
| Conditional language such as `Pokud se to nezmění` | Planned or contingent future development. It is not materialized as a played event. |
| Dice chances such as `2z6`, `4z6`, and `1z6`, plus tactical reactions and attack options | Game procedure or random possibility, not fictional history. |
| `Jjkk` and the unfinished sentence under `Pozvánky` | Draft or incomplete source material. No missing completion is invented. |
| Numbered headings and the composed final map | Adventure-local keyed reference material. Significant location state is materialized selectively; ordinary room and tactical detail remains addressable in this source. |

Source:

- [Preserved GM preparation](000-Hrad-Penbrok.docx) — the cited headings and internal wording.

## Keyed textual locators

The DOCX's `Heading 1` style is automatically numbered. These source-native headings are sufficient locators without creating room records:

| Key | Heading | Material type |
| --- | --- | --- |
| 1 | `Padací most` | Structural condition. |
| 2 | `Dřevěné lávky` | Structural and tactical reference. |
| 3 | `Hlídající bandita` | NPC placement, procedure, and tactics. |
| 4 | `Panoš a koně` | NPC state plus hidden curse backstory and mechanism. |
| 5 | `Bandité` | Encounter composition, random condition, knowledge, and plans. |
| 6 | `Loupeživý rytíř` | Nicholas's prepared state, knowledge, and contingent plans. |
| 7 | `Rukujmí` | Cecily's prepared state and motivation. |
| 8 | `Brána` | Architectural feature and inscription. |
| 9 | `Prevet` | Adventure-local route detail. |
| 10 | `Pozvánky` | Significant curse-related objects plus an incomplete draft sentence. |
| 11 | `Ohnivec` | Hidden backstory and prepared supernatural state. |
| 12 | `Úniková chodba` | Adventure-local route detail. |
| 13 | `Žaba na prameni` | Hidden creature and water-contamination mechanism. |
| 14 | `Tenká příčka` | Adventure-local structural detail. |
| 15 | `Tekutý poklad` | Ordinary room contents. |
| 16 | `Čapí hnízdo` | Adventure-local encounter detail. Marker 16 is omitted from the raw drawing layer; the curator placed it in the tower above markers 11 and 15. |
| 17 | Final map paragraph | Not an independent textual key. The composed drawing paragraph is styled `Heading 1`, so Word's automatic numbering assigns it 17; `Žába na pramen` is one of the drawing-layer labels within that paragraph. |

## Map and visual addressability

The DOCX package reports two pages. Its final drawing paragraph forms the map page: a base castle elevation and multi-level floor-plan JPEG (`word/media/image3.jpeg`) is combined with Word drawing-layer objects. The drawing layer supplies key markers 1–15, stairs and route marks, and labels including `Vyhořelá laboratoř`, `Vyhořelá ložnice`, `Panská ložnice`, `Brána`, `Zbrojnice`, `Cisterna`, `Sklepní skladiště`, `Vinný sklep`, `Ubikace`, `Hostinské pokoje`, `Kuchyně`, `Spíže`, `Sál`, and `Stáje`.

The base JPEG alone is not exported as the archive map because it omits the Word overlay layer. The preserved DOCX is therefore the authoritative composed visual source. Retrieve it by the final map page together with textual keys 1–16 above. The raw map contains markers 1–15 but no marker 16. The curator supplied the omitted intended position: marker 16 belongs in the tower above markers 11 and 15. This correction is recorded in metadata and is not drawn into the preserved source. The apparent key 17 is an automatic number applied to the final map paragraph because that paragraph uses the heading style; it is not a second `Žába na pramen` textual entry.

During ingestion, the embedded base JPEG was visually inspected and the complete drawing layer was structurally enumerated from the DOCX package. A full-page raster render could not be produced because LibreOffice is not installed in the available document runtime; therefore the composed page was not falsely claimed to have passed raster-layout QA. The original DOCX retains the complete composition.

Source:

- [Preserved GM preparation](000-Hrad-Penbrok.docx) — final map page, embedded image, drawing labels, arrows, and numbered key markers.
- Curator-supplied correction during curation review on 2026-08-21 — intended position of omitted marker 16.

## Prepared baseline and later play

The source prepares Nicholas and his bandits as occupying Penbrok, with Lawrence serving him and Cecily held hostage. Played sources later report Nicholas's defeat and Nathaniel's group taking the fortress. This is treated as a state transition from prepared baseline to played outcome, not as contradictory evidence.

The prepared source identifies the tower being as an `ohnivec` trapped by Florence's unfinished ritual. Yann's played account interprets it as a manifestation of the Sluneční panna. The archive retains both the prepared GM identification and Yann's religious interpretation; it does not rewrite one into the other.

The prepared explanation of the invitation-and-sleep curse closely matches the gossip explanation in the player notes. It independently establishes the hidden GM baseline; the curator clarified that Yann learned the shorter, not-entirely-true version as gossip during `Sezení 2`.

The vampire in the hidden background under `Panoš a koně` is unnamed in the DOCX. The curator identified that being as Lord Ruthwen. This identity decision links Ruthwen to Kirsten's earlier invitation and Edward's attempt to exclude him without altering the source's unnamed wording or implying that the player characters knew the identity at that time.

Sources:

- [Preserved GM preparation](000-Hrad-Penbrok.docx) — prepared occupation and headings `Panoš a koně`, `Loupeživý rytíř`, `Rukujmí`, and `Ohnivec`.
- [Raw correspondence](Penbrok.xml) — sections `Dobytí Penbroku` and `Hladovějící z Willowburnu`, for later played outcomes and Yann's interpretation.
- [Player notes](Penbrok-hracske-poznamky.md) — `Sezení 2` and `Sezení 4`, for Yann's gossip account and played handling of the tower being.
- [Ruthwen identity resolution](../../../curation/resolved.md#curation-penbrok-009--identity-of-the-vampire-in-the-prepared-curse-backstory) — curator-supplied identity of the unnamed prepared vampire.

## Deliberately source-local material

The archive does not create independent records for every keyed room, ordinary architectural feature, mundane item, bandit, horse, tactical option, dice probability, route hazard, or random encounter condition. Nicholas's possible future sale of Cecily is retained only as a contingency in key 6 and is not recorded as an event. The incomplete invitation sentence and `Jjkk` fragment remain incomplete.

Source:

- [Preserved GM preparation](000-Hrad-Penbrok.docx) — textual keys 1–16 and the auto-numbered final map paragraph.

## Import trace

The original DOCX is preserved unchanged beside this metadata record. Its SHA-256 digest at intake and after the move is `24DF7D73FB5A492D37E80618082EACA3C9A83234DB21E49A89682849EDBF75D1`.

Sources:

- [Preserved GM preparation](000-Hrad-Penbrok.docx) — exact imported bytes.
- [Source handling rules](../../README.md) — permanent campaign-source convention and inbox lifecycle.
