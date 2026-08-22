# Read and output modes

GrandCampaign has two primary modes for repository-backed answers and one diagnostic comparison mode. These modes govern what repository layers may be read; they do not change the provenance, epistemic, or temporal rules used to interpret what is read.

## FAST / MATERIALIZED

FAST answers exclusively from the materialized working world model. It may read persistent working records such as campaigns, entities, locations, organizations or polities, objects, events, snapshots, relationships, incorporated curator decisions, and the configuration and governance needed to interpret those records.

FAST must not read anything under [`sources/`](../sources/), including raw evidence, source metadata or sidecars, transcriptions, extracts, and other source-side content. It may use provenance already embedded in materialized records, but it must not follow source links or locators into source content.

FAST answers: **What does the materialized repository currently know independently of rereading its sources?**

Missing information in FAST means **not materialized**, not false. FAST must not fill gaps from model memory, earlier Codex conversations, generated outputs, or general inference.

## DEEP / SOURCE-GROUNDED

DEEP begins with the materialized working model and may then consult relevant ingested source evidence. Where practical, use provenance and source locators to retrieve only relevant material rather than loading sources indiscriminately.

DEEP may consult GM preparation, played accounts, character sheets, Discord material, maps, DOCX, XML, Markdown, and other ingested evidence under the normal provenance and epistemic rules. Source evidence may supplement, qualify, or verify materialized information, but it must not silently override curator decisions, temporal state changes, or stronger established evidence.

DEEP answers: **What can the repository establish when both its materialized model and relevant underlying evidence are consulted?**

## COMPARE

COMPARE diagnoses materialization quality for the requested subject:

1. Produce the FAST result without reading anything under `sources/`.
2. Only after the FAST result is complete, inspect relevant sources as DEEP would.
3. Report what additional, more precise, or materially different information required source access.

The comparison must clearly distinguish information already materialized, information available only from sources, and genuine discrepancy or lost nuance. Do not let information learned during the DEEP phase contaminate the FAST result.

Source-only detail is not automatically a materialization defect. The hybrid-ingestion policy intentionally permits adventure-local detail to remain source-local.

## Selection and default

**Default: FAST. Curation review or resolution: DEEP.**

If no mode is specified for a normal reconstruction, query, derived output, or fictional-generation request, use FAST. Opening, reviewing, or resolving an item from the curation queue instead uses DEEP by default: this automatically permits and expects reading relevant material under `sources/`. Where practical, inspect only sources materially relevant to the curation question. Before asking the curator or resolving the item, compare that source evidence with materialized records, curator decisions, and existing provenance; do not treat the materialized layer as sufficient evidence merely because FAST is the general default. After the curation task is complete, subsequent unspecified read and output requests revert to FAST.

An explicit user request for `FAST`, `DEEP`, or `COMPARE` overrides the applicable default where compatible with the task.

## Shared rules

All modes continue to obey repository governance for provenance, uncertainty, temporal cutoffs, prepared versus played state, character knowledge and perspective, curator information, and conflicting accounts. A mode changes the evidence layer available to the answer, not the interpretation rules.

Read and output tasks are read-only unless the user explicitly requests a repository change. Generated output never automatically becomes repository evidence or canon.

## Repository-layer boundary

The FAST boundary is defined by repository layer, not file format. A Markdown raw source is source material and forbidden in FAST; a Markdown materialized entity record is allowed. Everything under `sources/` is outside FAST regardless of whether it is DOCX, XML, Markdown, an image, metadata, a sidecar, or another format.

Requirements elsewhere in governance to preserve or record provenance do not authorize opening source content during FAST. For FAST, use only provenance already present in allowed materialized records.
