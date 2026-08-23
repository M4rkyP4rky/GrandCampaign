---
id: source-rpgforum-340
record_type: source
reference_name: RPGForum — Železné přísahy
document_type: play_by_post_forum_corpus
relationship_to_play: mixed
perspective: multi_author_collaborative
source_platform: RPGForum.cz
source_url: https://rpgforum.cz/forum/viewforum.php?f=340
forum_id: 340
forum_section_title: "[PBP] Železné přísahy"
campaign_reference_name: Železné přísahy
campaign: ../../../campaigns/campaign-zelezne-prisahy.md

corpus:
  normalizer_version: 4
  topic_count: 23
  post_count: 1198
  normalized_topics: rpgforum-340-normalized/topics/
  manifest: rpgforum-340-normalized/manifest.json
  corpus_index_json: rpgforum-340-normalized/corpus-index.json
  corpus_index_csv: rpgforum-340-normalized/corpus-index.csv
  attachments: rpgforum-340-raw/attachments/
  integrity_manifest: integrity.sha256
  normalization_audit: PASS

known_participant_roles:
  - username: Orákulum
    role: game_master
    provenance: curator-supplied source interpretation on 2026-08-22
  - username: MarkyParky
    role: player
    associated_character: Myrick Lysbærer
    provenance: curator-supplied source interpretation on 2026-08-22
  - username: Jezus
    role: player
    associated_character: Beltran z Kalné vody
    provenance: curator-supplied source interpretation on 2026-08-22

epistemic_roles:
  - played_fiction
  - collaborative_authored_play
  - campaign_reference_material
  - character_definition
  - out_of_character_discussion
---

# RPGForum — Železné přísahy

## Classification and preserved representation

This source is a multi-author play-by-post corpus from the RPGForum section
`[PBP] Železné přísahy`, forum ID `340`.

For GrandCampaign, the preserved ingest representation is the audited
normalizer-v4 Markdown corpus together with the attachment binaries referenced
from those Markdown files. The upstream HTML capture was used outside
GrandCampaign to produce and verify this portable representation. It is not part
of the GrandCampaign ingest source and must not be used as an alternative source
during semantic ingestion.

The v4 production audit establishes a one-to-one correspondence between the
1,198 posts in the upstream capture, the 1,198 normalized Markdown posts, and
the 1,198 entries in the corpus index. The audit also found no missing
referenced attachments.

The normalized Markdown topic files are the primary textual evidence for
GrandCampaign derivation. `corpus-index.json`, `corpus-index.csv`, and
`manifest.json` are navigation, transformation, and validation metadata; they
must not be cited as substitutes for the actual post content.

The attachment binaries are preserved source material when a post refers to or
displays them.

Sources:

- [Normalization manifest](rpgforum-340-normalized/manifest.json) — v4 corpus counts and production audit.
- [Corpus index](rpgforum-340-normalized/corpus-index.json) — mechanical post metadata and source-file lookup.
- [Integrity manifest](integrity.sha256) — SHA-256 digests of preserved intake files.

## Authorship and play authority

`Orákulum` is the game master. `MarkyParky` is the player of Myrick
Lysbærer. `Jezus` is the player of Beltran z Kalné vody. These identifications
are curator-supplied metadata.

A posting username does not perfectly determine the authorial role of an
individual post. In particular, a post submitted under `MarkyParky` or `Jezus`
may have been written in the Oracle/game-master role rather than as
character/player narration. Determine the authorial role of each such post from
its content, surrounding play context, continuity with adjacent posts, and
apparent play function; do not classify it mechanically from username alone.

There is no need to determine which real-world participant authored an
individual post submitted under `Orákulum`.

The play-by-post game grants players authorial authority over the fiction.
Accordingly, fictional narration authored by a player as part of play establishes
the narrated fictional action, event, or state as having occurred as described,
unless the text itself marks the material as hypothetical, conditional,
proposed, uncertain, speculative, or otherwise non-actual.

Do not downgrade an asserted fictional description merely because its author is
a player rather than the game master. Conversely, do not promote embedded
character beliefs, guesses, claims, dialogue, or hypotheses into objective facts
about their referents. Such material establishes what the character believed,
said, suspected, perceived, or proposed to the extent supported by the wording.

A retrospective description can still establish an event that actually occurred.
Its retrospective nature affects chronological placement, not factuality.

The role of forum participants other than `Orákulum` must not be inferred solely
from the fact that they posted. In particular, the corpus contains meta material
and may contain comments by people who were not participating in the fiction.
Determine player participation from curator-supplied metadata or source context,
and determine the epistemic and authorial role of an individual post from its
content and context rather than mechanically from its posting username.

Source:

- Curator-supplied source interpretation on 2026-08-22 — GM identity,
  MarkyParky/Myrick and Jezus/Beltran player associations, posting-account
  caveats, player authorial authority, and interpretation of fictional
  narration.

## Cross-campaign semantic identity scope

The curator has established that Železné přísahy is very distant from Penbrok
in both fictional space and fictional time. Ordinary local beings, places,
organizations, objects, collectives, and other local referents must therefore
not be treated as plausible cross-campaign identity matches with Penbrok merely
because their names or descriptions are similar.

Cross-campaign semantic identity matching is normally relevant only for
deities, comparable cosmologically broad entities, entities whose fictional
scope can otherwise span the spatial and temporal separation, or cases with
explicit source evidence for shared identity. This restriction concerns
semantic identity matching only; persistent IDs must remain globally unique
across the complete GrandCampaign repository.

Source:

- Curator-supplied cross-campaign context on 2026-08-22.

## Curator-resolved named identities

The earlier raider `Fanir z Rudoskal` and the later miner named `Fanir` from
Údolí kleče are two distinct people. Their shared personal name does not
indicate identity and they must not be merged.

`Nisus` is one person. The source's use of “brother” describes a familial
relationship: Nisus is a brother or family member of Cadigan. It does not name
Cadigan's brothers collectively or a kin group.

`S.M.J.` remains intentionally unresolved. The available source and curator
metadata do not establish whether the initials identify a person, an
organization, or another kind of signatory.

Source:

- Curator-supplied identity clarifications on 2026-08-23.

## Topic and block semantics

The forum section contains multiple kinds of threads, including played-fiction,
character, location/NPC, information, and meta threads. Topic labels are useful
source structure but must not by themselves determine the epistemic role of
every statement inside the topic.

In particular, do not mechanically convert every post or every topic into a
fictional event. Declarative character or world-reference material may establish
character or world state without describing an event, while meta or
out-of-character discussion may establish no fictional fact at all.

Played-fiction passages are interpreted according to the authorial rules above.

Source:

- [Normalized topic corpus](rpgforum-340-normalized/topics/) — complete
  source-native topic and post structure.
- Curator-supplied source interpretation on 2026-08-22 — play-authority rules.

## Cross-thread chronology

Forum topics are organizational chapters or subchapters, not independent
chronological units. Characters and players may leave one thread, continue in
another thread or subchapter, and later return to an earlier thread. Different
fictional streams may therefore interleave across multiple topics.

The original forum `posted_at` timestamps are a strong default scaffold for
reconstructing relative play order across threads. Start cross-thread chronology
from the global timestamp order of posts rather than from topic order.

Forum timestamp order is not an absolute fictional chronology. Explicit
in-fiction temporal information, retrospectives, flashbacks, stated
simultaneity, explicit continuation relationships, or other stronger temporal
evidence override or qualify the timestamp-derived ordering.

A retrospective post remains evidence of the narrated fictional events, but its
`posted_at` timestamp indicates when the retrospective was posted, not when its
fictional events occurred.

Where the source does not support a total ordering, preserve parallel,
partially ordered, or uncertain fictional streams rather than manufacturing a
precise sequence.

Sources:

- [Corpus index](rpgforum-340-normalized/corpus-index.json) — original
  `posted_at`, topic ID, post ID, author, and source-file metadata for all
  1,198 posts.
- Curator-supplied source interpretation on 2026-08-22 — cross-thread play
  structure and use of forum timestamps as the default ordering aid.

## Curator-supplied corrections and chronology anchors

The following clarifications were supplied by the curator/GM on 2026-08-22.
They are interpretation and chronology metadata; they do not alter the
preserved normalized source text.

### Correction of source interpretation

At `topic 17686, post 689891`, the source text names `Bjorn`, but the player of
Myrick wrote that name in error. The intended character is `Tristan`. Interpret
the reference as Tristan. This post must not be used as evidence that Bjorn
returned to or was present in Bouřný Les at that point.

Correction metadata:

- field: character reference in played narration;
- locator: `topic 17686, post 689891`;
- source value: `Bjorn`;
- corrected interpretation: `Tristan`;
- provenance: curator/GM clarification supplied on 2026-08-22.

### Curator-supplied chronology relation

The fictional action beginning at `topic 17460, post 700043` immediately
follows the Jeskyně Zrady sequence. There is no substantial unrepresented
fictional interval between those passages.

Relation metadata:

- locator: `topic 17460, post 700043`;
- relation: immediately follows the preceding Jeskyně Zrady sequence;
- provenance: curator/GM clarification supplied on 2026-08-22.

### GM-supplied fictional chronology anchor

The played story begins in **1032 poPA**. This establishes year precision only.
It does not establish a month, day, season boundary, or a date equivalent to
`1032-01-01`. The anchor applies to the campaign opening; later material must
not be assigned to 1032 poPA merely from this anchor where the reconstructed
relative chronology does not establish that it remains within the same year.

Anchor metadata:

- applies to: campaign opening (`topic 17203, post 650283`);
- year: `1032 poPA`;
- precision: year;
- provenance: GM-supplied fictional chronology clarification on 2026-08-22.

## Stable source locators

The stable locator for an individual forum contribution is:

`topic <topic_id>, post <post_id>`

For example:

`topic 17203, post 697240`

The corresponding primary source is the normalized topic Markdown file:

`rpgforum-340-normalized/topics/<topic_id>.md`

whose post heading is:

`## Post <post_id>`

Derived factual content should link to the appropriate normalized topic Markdown
file and include the topic/post locator when a whole-topic link would be
ambiguous.

When visual attachment content itself supports a derived fact, extend the
locator with the attachment ID or preserved filename where useful.

The corpus index is a lookup aid for finding the relevant topic file, author,
timestamp, and post ID. It is not itself fictional evidence and its physical row
order is not fictional chronology.

## Intake integrity

All files listed by `integrity.sha256` were preserved at intake without content
changes. The normalized Markdown files retain the exact v4 production output.
The attachment binaries retain the exact archived files referenced by the
normalized corpus.

The upstream raw HTML pages are intentionally not part of this GrandCampaign
source package. GrandCampaign semantic ingestion uses the verified portable
Markdown representation described above.

Sources:

- [Integrity manifest](integrity.sha256) — intake file digests.
- [Normalization manifest](rpgforum-340-normalized/manifest.json) — v4
  transformation and audit metadata.
