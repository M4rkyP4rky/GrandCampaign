# Open content curation items

## curation-penbrok-002 — Oswyn surname spelling

- Status: open
- Scope: [Panství Penbrok](../campaigns/campaign-dopisy-z-panstvi-penbrok.md)
- Uncertainty: Is the intended surname `Waldergrave`, `Waldegrave`, or are both spellings independently meaningful?
- Why it matters: Clarification could correct the reference name while preserving the other spelling as an attested source variant.
- Affected records: [Oswyn Waldergrave](../entities/beings/person-oswyn-waldergrave.md)
- Evidence: [Dopisy z panství Penbrok](../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml), section `Příjezd`, first gives the full form `Oswyna Waldergravea` and later uses `pan Waldegrave`.
- Current handling: `Oswyn Waldergrave` is the reference name and `Oswyn Waldegrave` is retained as an alternate source spelling.

## curation-penbrok-003 — Referents of Penbrok

- Status: open
- Scope: [Panství Penbrok](../campaigns/campaign-dopisy-z-panstvi-penbrok.md)
- Uncertainty: Which uses of `Penbrok` denote the fortified residence, the political estate, or a broader vicinity, and are any further location identities required?
- Why it matters: Conflating a physical location with a political domain would produce incorrect geography and time-dependent control data.
- Affected records: [Penbrok](../entities/locations/location-penbrok-fortress.md), [Panství Penbrok](../entities/polities/polity-penbrok-estate.md), [Penbrokton](../entities/locations/location-penbrokton.md)
- Evidence: [Dopisy z panství Penbrok](../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml), including sections `Příjezd`, `Dobytí Penbroku`, `Hladovějící z Willowburnu`, `Vrátila se snad válka?`, and `Hořkosladké vítězství`, uses `Penbrok` alongside `panství`, `tvrz`, `pevnost`, `hrad`, and `Penbrokton` without consistently fixing the referent. [Player notes](../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok-hracske-poznamky.md), especially `Sezení 1`, `Sezení 4`, and `Sezení 10`, add `hrad`, `Penbrok`, `Penbrokton`, and `panství` usages but still do not define all referents. [GM preparation](../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/000-Hrad-Penbrok.docx) explicitly uses `Hrad Penbrok` for the mapped physical fortress, confirming that referent in this source without resolving every ambiguous use in the played accounts.
- Current handling: The fortified residence and political estate have separate records; Penbrokton remains a separate settlement, and ambiguous passages are not forced into a physical hierarchy.

## curation-penbrok-004 — Extent of Darkwood

- Status: open
- Scope: [Panství Penbrok](../campaigns/campaign-dopisy-z-panstvi-penbrok.md)
- Uncertainty: Does `Darkwood` name Ruthwen's wider domain, its principal residence, or both?
- Why it matters: A confirmed distinction could require separate physical and political records and more precise event locations.
- Affected records: [Darkwood](../entities/locations/location-darkwood.md), [Útěk z Darkwoodu](../events/event-darkwood-escape.md), [Lord Ruthwen](../entities/beings/person-lord-ruthwen.md)
- Evidence: [Dopisy z panství Penbrok](../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml), sections `Upír` and `Dívky a dámy v nesnázích`, calls Darkwood a `panství` while describing a residence with underground areas and towers. [Player notes](../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok-hracske-poznamky.md), `Sezení 7` and `Sezení 8`, use `Darkwood` for the journey's destination and then describe a `hrad`, towers, underground areas, and an escape, without establishing the named extent.
- Current handling: One location record preserves the name without asserting its exact extent or physical hierarchy.

## curation-penbrok-005 — Identity of the two monasteries

- Status: open
- Scope: [Panství Penbrok](../campaigns/campaign-dopisy-z-panstvi-penbrok.md)
- Uncertainty: Is the forgotten monastery explored earlier the same place as the abandoned monastery later used in the confrontation with Ruthwen?
- Why it matters: A mistaken match would merge two locations and events; a confirmed match would justify a shared location record and links.
- Affected records: [Výprava do prokletého kláštera](../events/event-cursed-monastery-expedition.md), [Porážka Ruthwena](../events/event-defeat-of-ruthwen.md)
- Evidence: [Dopisy z panství Penbrok](../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok.xml), sections `Prokletý klášter`, `Vrátila se snad válka?`, and `Hořkosladké vítězství`, describes a forgotten monastery and later an abandoned monastery but does not establish their identity. [Player notes](../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok-hracske-poznamky.md), `Sezení 5` and `Sezení 9`–`10`, describe the earlier place under `Chrám` and the later place as a monastery with crypts, but give no equivalence statement.
- Current handling: No monastery location record or equivalence is asserted.

## curation-penbrok-007 — Map keys 16–17 in Hrad Penbrok

- Status: open
- Scope: [Hrad Penbrok GM preparation](../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/source-hrad-penbrok-gm-preparation.md)
- Uncertainty: Where, if anywhere, should text key 16 `Čapí hnízdo` and the trailing key 17 `Žába na pramen` appear on the composed castle map, and is key 17 an accidental duplicate of key 13 `Žaba na prameni`?
- Why it matters: Inventing positions would corrupt map addressability; silently merging key 17 with key 13 would rewrite a draft ambiguity in the source.
- Affected records: [GM-preparation source metadata](../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/source-hrad-penbrok-gm-preparation.md), especially the keyed-locator and map sections.
- Evidence: [GM preparation](../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/000-Hrad-Penbrok.docx) automatically numbers the textual headings 1–17, while the final drawing layer contains map markers only for keys 1–15. The final drawing paragraph carries the duplicate-like heading `Žába na pramen`.
- Current handling: Keys 1–15 remain addressable between text and map. Keys 16 and 17 remain text locators without inferred map positions or equivalence.

## curation-penbrok-008 — Character knowledge of the curse explanation

- Status: open
- Scope: [Penbrok player notes](../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/source-penbrok-hracske-poznamky.md)
- Replaces: [curation-penbrok-006](resolved.md#curation-penbrok-006--epistemic-status-of-the-fortress-curse-explanation)
- Uncertainty: When and how did the prepared GM explanation of the Penbrok curse enter the player notes, and did Yann know it during `Sezení 2`, learn it later, or never possess it as character knowledge?
- Why it matters: The GM preparation establishes the hidden baseline explanation but does not establish the player-character knowledge boundary or the time at which any discovery occurred.
- Affected records: [Player-notes source metadata](../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/source-penbrok-hracske-poznamky.md), [prepared Penbrok snapshot](../snapshots/locations/snapshot-location-penbrok-preplay-baseline.md), and any future character-knowledge output about the curse.
- Evidence: [Player notes](../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/Penbrok-hracske-poznamky.md), `Sezení 2`, contains an unlabelled explanation closely matching hidden material under key 4 `Panoš a koně` in the [GM preparation](../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/000-Hrad-Penbrok.docx). Neither source states how that explanation entered the player notes.
- Current handling: The explanation may support the prepared GM baseline but is not attributed to Yann's knowledge at `Sezení 2` or any other time without further evidence.

## curation-penbrok-009 — Identity of the vampire in the prepared curse backstory

- Status: open
- Scope: [Panství Penbrok](../campaigns/campaign-dopisy-z-panstvi-penbrok.md)
- Uncertainty: Is the unnamed vampire whom Kirsten invited to Penbrok in the GM preparation the same being as [Lord Ruthwen](../entities/beings/person-lord-ruthwen.md)?
- Why it matters: A confirmed match would establish Ruthwen's earlier relationship with Kirsten and his role in the origin of the fortress curse; a wrong match would attach hidden backstory to the wrong being.
- Affected records: [Kristen](../entities/beings/person-kristen-penbrok.md), [Edward z Penbroku](../entities/beings/being-edward-of-penbrok.md), [Lord Ruthwen](../entities/beings/person-lord-ruthwen.md), and [prepared Penbrok snapshot](../snapshots/locations/snapshot-location-penbrok-preplay-baseline.md).
- Evidence: [GM preparation](../sources/campaigns/campaign-dopisy-z-panstvi-penbrok/000-Hrad-Penbrok.docx), hidden background under key 4 `Panoš a koně`, describes an unnamed vampire visiting Kirsten. Played sources later identify Ruthwen as a vampire connected to Kirsten's disappearance and condition, but the GM preparation does not name him in the earlier backstory.
- Current handling: The prepared vampire remains unnamed and is not linked to Ruthwen in derived backstory or snapshot records.
