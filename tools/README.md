# Internal validation tools

`validate.py` is a read-only check of persistent record envelopes, links, and the optional [chronology model](../chronologies/README.md). It never repairs records, deletes conflicting edges, infers dates, solves a timeline, or requires backfill.

## Canonical status

`tools/validate.py` and `tools/tests/` are the single supported validation path. Use the commands below for repository checks and regression tests. The ignored, untracked `temp/shelswell-inspection/validate_records.py` is an obsolete inspection helper, not a supported validator or acceptance gate. It does not decode URL-escaped filenames and can report 73 false broken links in existing records; the canonical validator decodes these links and has a regression test for them. The helper is retained unchanged as temporary inspection history; no cleanup or duplicate-tool redesign is required. Its exit status is not part of canonical validation results.

## Run

Requires Python 3.10+ and PyYAML (pinned in `requirements.txt`):

```text
python -m pip install -r tools/requirements.txt
python tools/validate.py
python -m unittest discover -s tools/tests -v
git diff --check
```

An optional root argument permits isolated fixture repositories. Files are selected with `git ls-files --cached --others --exclude-standard`; ignored tmp/temp workspaces are excluded. Templates are schematic, not persistent records. Raw evidence bodies are not treated as archive Markdown links. Source metadata is read to check record identities; this is a validation operation, not a FAST repository answer.

Exit status: `0` clean, `1` structural/link errors, `2` temporal contradictions with otherwise valid structure. Contradictions are preserved evidence requiring interpretation, not instructions to erase claims. Disputed status or curation links do not suppress reports.

## Coverage

- Repository-wide unique ASCII IDs, ID filenames (with the manifest exception), record type presence, duplicate YAML keys, and one matching H1.
- Prose Markdown file/directory links in governance and records, and structured links introduced by chronology; paths must be repository-relative and resolve.
- Chronology/segment envelopes expected from their storage paths, even when frontmatter is empty or record-discovery fields are missing/wrong; directory convention, campaign membership, manifest navigation, thread declarations/scope, relation targets, and no self-relations.
- Local basis/confidence/support for relations, assertions, boundaries, participants, locations, corrections, and event/segment associations; source support must be a concrete file. Curator support requires source metadata or a concrete queue file and existing curation item ID. Aggregate provenance does not suffice.
- Optional event assertions and campaign/event navigation; existing records without these fields remain valid.
- Signed AP components, approved month/day ranges, precision/component shape, independent bound precisions, relative offsets, and rejection of invented calendar identifiers.
- Disjoint comparable exact year/date or bounded claims about the same property, with legacy `time` and new assertions loaded independently, including manifest anchors on legacy-only events; reversed bounds; strict temporal cycles; exact concurrence versus strict ordering paths or disjoint compatible dates; date/order contradictions when dates are sufficiently distinct.
- Invalid enum types are diagnosed before membership checks, so malformed confidence, record/relation/assertion types, property, precision, certainty, and adjacent enums do not raise unhandled type errors. Other records continue to be checked.

Contradiction diagnostics retain participating record IDs, claim/relation types, original values, and available local provenance. They do not mutate or suppress claims. Only directly comparable scopes are checked; interval overlap does not imply equal start/end dates.

Narrative edges never enter the strict temporal graph. Approximate/uncertain constraints and probable parallelism remain qualified, not hardened into temporal order.

## Deliberate limits and review obligations

This is a focused validator, not a complete schema or inference engine. It does not validate source truth, quotation accuracy, general human-readable source locators or Markdown fragments, arbitrary legacy structured-link fields, every fantasy time descriptor, cross-property interval algebra, numeric offsets against dates, time-of-day ordering, or all combinations of qualified constraints. The targeted curation check verifies that an item ID exists, not whether its contents actually establish a decision. Broad/age/century and differently qualified claims may require human comparison. Generic calendar identifiers are explicitly unsupported. Existing `time` does not gain mandatory new fields. Further incompatible constraints must be reported during review without assigning a winning authority.

Inspect destination-relative template examples manually; placeholders and code fences are intentionally excluded from ordinary link checks. Keep this coverage list accurate as checks evolve. No campaign requires chronology and no event requires temporal assertions. No automated ingestion, timeline generation, or database is introduced.

External service-specific collectors and importers should normally be separate projects or repositories. For example, a Discord exporter should produce raw, portable input files for this repository rather than making GrandCampaign depend on the Discord API.
