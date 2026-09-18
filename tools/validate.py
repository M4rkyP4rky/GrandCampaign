"""Read-only record/link and optional chronology checks; no inference or repair."""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote

import yaml


CONFIDENCE = {"high", "medium", "low"}
CERTAINTY = {"exact-at-precision", "approximate", "bounded", "uncertain"}
PRECISION = {"exact-datetime", "exact-date", "day", "month", "year", "approximate-year", "century", "age", "broad", "unknown"}
PROPERTIES = {"start", "end", "placement"}
NARRATIVE = {"continues_to", "splits_into", "rejoins"}
ORDER = {"precedes", "immediately_precedes"}
CONCURRENT = {"simultaneous_with", "overlaps", "probably_parallel_with"}
ID = re.compile(r"[a-z][a-z0-9]*(?:-[a-z0-9]+)+\Z")


def member(value, choices):
    """Reject malformed enum types before any hash-based membership check."""
    return isinstance(value, str) and value in choices


class UniqueLoader(yaml.SafeLoader):
    pass


def unique_mapping(loader, node):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node)
        if key in result:
            raise ValueError(f"duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


class Validator:
    def __init__(self, root):
        self.root = Path(root).resolve()
        self.records = {}
        self.errors = []
        self.conflicts = []
        self.edges = []
        self.concurrent = []
        self.dates = {}

    def error(self, path, message):
        self.errors.append(f"{path.relative_to(self.root)}: {message}")

    def require(self, path, value, message):
        if not value:
            self.error(path, message)
        return bool(value)

    def link(self, path, value, types=None):
        if not isinstance(value, str) or not value.strip():
            self.error(path, "missing/non-string relative link")
            return None
        if re.match(r"^[a-zA-Z][\w+.-]*:", value) or value.startswith(("/", "\\")):
            self.error(path, f"not a repository-relative link: {value}")
            return None
        target = (path.parent / unquote(value.split("#", 1)[0])).resolve()
        if not target.is_relative_to(self.root) or not target.exists():
            self.error(path, f"broken/outside-repository link: {value}")
            return None
        if types and not member(self.records.get(target, {}).get("record_type"), types):
            self.error(path, f"wrong record type for link: {value}; expected {sorted(types)}")
        return target

    def resource(self, path, value):
        target = self.link(path, value)
        if target and not target.is_file():
            self.error(path, f"provenance must identify a concrete file: {value}")
            return None
        return target

    def describe(self, path, claim, label):
        rid = self.records.get(path, {}).get("id", path.stem)
        return f"{rid} [{path.relative_to(self.root)}] {label}: {claim!r}"

    def items(self, path, value, label):
        if not isinstance(value, list):
            self.error(path, f"{label} must be a list")
            return []
        return value

    def mapping(self, path, value, label):
        if not isinstance(value, dict):
            self.error(path, f"{label} must be a mapping")
            return {}
        return value

    def support(self, path, item):
        self.require(path, isinstance(item.get("basis"), str) and item["basis"].strip(), "local basis required")
        self.require(path, member(item.get("confidence"), CONFIDENCE), "local confidence must be high/medium/low")
        self.require(path, item.get("sources") or item.get("curator_clarification"), "local sources or curator_clarification required")
        for source in self.items(path, item.get("sources", []), "sources"):
            value = source.get("source") if isinstance(source, dict) else source
            target = self.resource(path, value)
            if target:
                self.require(path, target.is_relative_to(self.root / "sources"), "local sources must cite preserved sources; use curator_clarification for decisions")
        if "curator_clarification" in item:
            clarification = self.mapping(path, item["curator_clarification"], "curator_clarification")
            target = self.resource(path, clarification.get("record"))
            locator = clarification.get("locator")
            valid_locator = self.require(path, isinstance(locator, str) and locator.strip(), "curator clarification needs a locator")
            if target:
                self.require(path, target.is_relative_to(self.root / "curation") or target.is_relative_to(self.root / "sources"), "clarification must identify durable curation/source metadata")
                if target.is_relative_to(self.root / "curation"):
                    self.require(path, target in {self.root / "curation/open.md", self.root / "curation/resolved.md"}, "curator item must use the existing open/resolved queue")
                    if valid_locator:
                        ids = re.findall(r"^#{1,6}\s+(curation-[a-z0-9-]+)(?=\s|$)", target.read_text(encoding="utf-8-sig"), re.M)
                        self.require(path, any(re.search(r"(?<![a-z0-9-])" + re.escape(cid) + r"(?![a-z0-9-])", locator) for cid in ids), "curator locator must identify an existing curation item")
                elif target.is_relative_to(self.root / "sources"):
                    self.require(path, self.records.get(target, {}).get("record_type") == "source", "curator clarification must identify source metadata, not raw evidence")

    def date(self, path, point, precision):
        before = len(self.errors)
        point = self.mapping(path, point, "time value/bound")
        valid_precision = self.require(path, member(precision, PRECISION), "unsupported temporal precision")
        self.require(path, "calendar" not in point, "no calendar ID is currently defined; use signed year_ap")
        for key, low, high in (("year_ap", None, None), ("month", 1, 12), ("day", 1, 28)):
            if key in point:
                value = point[key]
                self.require(path, type(value) is int and (low is None or low <= value <= high), f"invalid {key}")
        if "month" in point:
            self.require(path, "year_ap" in point, "month requires year_ap")
        if "day" in point:
            self.require(path, "month" in point and "year_ap" in point, "day requires month/year_ap")
        if "time" in point:
            self.require(path, all(k in point for k in ("year_ap", "month", "day")) and isinstance(point["time"], str), "time requires date and quoted source string")
        needed = {"year": ("year_ap",), "approximate-year": ("year_ap",), "month": ("year_ap", "month"), "day": ("year_ap", "month", "day"), "exact-date": ("year_ap", "month", "day"), "exact-datetime": ("year_ap", "month", "day", "time")}
        self.require(path, all(k in point for k in (needed.get(precision, ()) if valid_precision else ())), "missing components for precision")
        if member(precision, {"year", "approximate-year"}):
            self.require(path, not any(k in point for k in ("month", "day", "time")), "year precision cannot contain finer components")
        if precision == "month":
            self.require(path, not any(k in point for k in ("day", "time")), "month precision cannot contain finer components")
        if member(precision, {"exact-date", "day"}):
            self.require(path, "time" not in point, "exact-date cannot contain a finer time component")
        # Ranges are used only for disjointness checks, never stored as inferred dates.
        if len(self.errors) == before and type(point.get("year_ap")) is int and member(precision, {"year", "month", "day", "exact-date", "exact-datetime"}):
            year = point["year_ap"] * 336
            if precision == "year":
                return year, year + 335
            if precision == "month":
                month = year + (point["month"] - 1) * 28
                return month, month + 27
            if all(type(point.get(k)) is int for k in ("month", "day")):
                day = year + (point["month"] - 1) * 28 + point["day"] - 1
                return day, day
        return None

    def scoped_target(self, path, subject, target):
        a, b = self.records.get(subject, {}), self.records.get(target, {})
        if a.get("record_type") == b.get("record_type") == "chronology_segment":
            left, right = a.get("chronology"), b.get("chronology")
            if isinstance(left, str) and isinstance(right, str):
                self.require(path, (subject.parent / left).resolve() == (target.parent / right).resolve(), "segment target crosses chronology scope")
            else:
                self.error(path, "segment chronology links must be strings")

    def assertion(self, path, value, manifest=False):
        item = self.mapping(path, value, "assertion")
        self.support(path, item)
        kind, prop, precision = item.get("kind"), item.get("property"), item.get("precision")
        valid_kind = self.require(path, member(kind, {"absolute", "bounded", "relative", "relation"}), "invalid assertion kind")
        valid_prop = self.require(path, member(prop, PROPERTIES), "assertion property must be start/end/placement")
        self.require(path, member(precision, PRECISION), "assertion precision required")
        self.require(path, member(item.get("certainty"), CERTAINTY), "assertion certainty required")
        self.require(path, "calendar" not in item, "no calendar ID currently defined")
        payloads = {"absolute": {"value"}, "bounded": {"earliest", "latest"}, "relative": {"target", "target_property", "direction", "offset"}, "relation": {"target", "target_property", "relation"}}
        payload_fields = set().union(*payloads.values())
        if isinstance(kind, str) and kind in payloads:
            self.require(path, not (set(item) & payload_fields) - payloads[kind], "payload fields do not match assertion kind")
        subject = self.link(path, item.get("subject"), {"event", "chronology_segment"}) if manifest else path
        if manifest and subject and self.records.get(subject, {}).get("record_type") == "chronology_segment":
            owner = self.link(subject, self.records[subject].get("chronology"), {"chronology"})
            self.require(path, owner == path, "anchor subject belongs to another chronology")
        if not valid_kind or not valid_prop or subject is None:
            return
        detail = self.describe(path, item, "temporal assertion")
        if kind == "absolute":
            span = self.date(path, item.get("value"), precision)
            if precision == "approximate-year":
                self.require(path, item.get("certainty") == "approximate", "approximate-year requires approximate certainty")
            if span and item.get("certainty") == "exact-at-precision":
                self.dates.setdefault((subject, prop), []).append((span, detail))
        elif kind == "bounded":
            self.require(path, item.get("certainty") == "bounded", "bounded assertion requires bounded certainty")
            self.require(path, "earliest" in item or "latest" in item, "bounded assertion needs a bound")
            bounds = {}
            for key in ("earliest", "latest"):
                if key in item:
                    bound = self.mapping(path, item[key], key)
                    bounds[key] = self.date(path, bound, bound.get("precision"))
            lower, upper = bounds.get("earliest"), bounds.get("latest")
            if lower and upper and lower[0] > upper[1]:
                self.conflicts.append(f"earliest exceeds latest for {prop}; {detail}")
            if lower or upper:
                self.dates.setdefault((subject, prop), []).append(((lower[0] if lower else float('-inf'), upper[1] if upper else float('inf')), detail))
        elif kind in {"relative", "relation"}:
            target = self.link(path, item.get("target"), {"event", "chronology_segment"})
            self.scoped_target(path, subject, target)
            target_prop = item.get("target_property")
            valid_target_prop = self.require(path, member(target_prop, PROPERTIES), "target_property required")
            relation = item.get("relation")
            if kind == "relative":
                self.require(path, member(item.get("direction"), {"before", "after"}), "relative direction must be before/after")
                relation = "precedes"
                if "offset" in item:
                    offset = self.mapping(path, item["offset"], "offset")
                    self.require(path, type(offset.get("value")) in (int, float) and offset["value"] >= 0 and member(offset.get("unit"), {"day", "week", "month", "year"}), "invalid relative offset")
            else:
                self.require(path, member(relation, ORDER | CONCURRENT), "invalid temporal relation")
            if relation == "probably_parallel_with":
                self.require(path, item.get("certainty") == "uncertain", "probably_parallel_with must be uncertain")
            if target and subject and valid_target_prop:
                self.require(path, subject != target, "self temporal relation not allowed")
                if item.get("certainty") == "exact-at-precision" and member(relation, ORDER):
                    left, right = (subject, prop), (target, target_prop)
                    if kind == "relative" and item.get("direction") == "after":
                        left, right = right, left
                    self.edges.append((left, right, detail))
                elif item.get("certainty") == "exact-at-precision" and member(relation, CONCURRENT):
                    self.concurrent.append(((subject, prop), (target, target_prop), relation, precision, detail))

    def chronology(self, path, data, kind):
        campaign = self.link(path, data.get("campaign"), {"campaign"})
        self.require(path, isinstance(data.get("record_sources"), list) and data["record_sources"], "record_sources overview required")
        for source in self.items(path, data.get("record_sources", []), "record_sources"):
            self.link(path, source.get("source") if isinstance(source, dict) else source)
        if kind == "chronology":
            self.require(path, path.name == "chronology.md" and path.parent.parent == self.root / "chronologies", "invalid manifest path")
            if campaign:
                self.require(path, path.parent.name == self.records.get(campaign, {}).get("id"), "manifest directory must equal campaign ID")
            self.require(path, member(data.get("status"), {"draft", "reviewed", "disputed"}), "invalid chronology status")
            threads = self.items(path, data.get("threads"), "threads")
            seen = set()
            for value in threads:
                thread = self.mapping(path, value, "thread")
                tid = thread.get("id")
                if self.require(path, isinstance(tid, str) and ID.fullmatch(tid) and tid.startswith("thread-"), "invalid thread ID"):
                    self.require(path, tid not in seen, "duplicate chronology-scoped thread ID")
                    seen.add(tid)
                self.require(path, isinstance(thread.get("label"), str) and thread["label"].strip(), "thread label required")
            for value in self.items(path, data.get("segments"), "segments"):
                target = self.link(path, value, {"chronology_segment"})
                if target and target in self.records:
                    self.require(path, self.link(target, self.records[target].get("chronology"), {"chronology"}) == path, "manifest segment belongs elsewhere")
            for value in self.items(path, data.get("curation", []), "curation"):
                target = self.link(path, value)
                if target:
                    self.require(path, target.is_relative_to(self.root / "curation"), "curation link must use existing queue")
            for value in self.items(path, data.get("curator_corrections", []), "curator_corrections"):
                item = self.mapping(path, value, "correction")
                self.support(path, item)
                self.require(path, "source_value" in item and "corrected_value" in item, "correction must retain both values")
        else:
            owner = self.link(path, data.get("chronology"), {"chronology"})
            self.require(path, member(data.get("chronology_confidence"), CONFIDENCE), "chronology_confidence required")
            if owner and owner in self.records:
                manifest = self.records[owner]
                self.require(path, path.parent == owner.parent / "segments", "segment must live in its manifest's segments directory")
                self.require(path, campaign == self.link(owner, manifest.get("campaign"), {"campaign"}), "segment/manifest campaign mismatch")
                tids = [x.get("id") for x in manifest.get("threads", []) if isinstance(x, dict)] if isinstance(manifest.get("threads"), list) else []
                self.require(path, member(data.get("thread"), tids), "undeclared or wrong-scope thread")
                navigation = manifest.get("segments", [])
                self.require(path, isinstance(navigation, list) and any(isinstance(x, str) and (owner.parent / x).resolve() == path for x in navigation), "segment missing from manifest navigation")
            self.require(path, data.get("boundaries"), "segment boundaries required")
            for field, key, types in (("boundaries", None, None), ("participants", "entity", {"being", "organization", "polity", "object", "affliction", "location"}), ("locations", "location", {"location"}), ("events", "event", {"event"})):
                for value in self.items(path, data.get(field, []), field):
                    item = self.mapping(path, value, field)
                    self.support(path, item)
                    if key:
                        self.link(path, item.get(key), types)
                    else:
                        self.require(path, isinstance(item.get("description"), str) and item["description"].strip(), "boundary description required")
            for value in self.items(path, data.get("source_spans", []), "source_spans"):
                item = self.mapping(path, value, "source span")
                self.resource(path, item.get("source"))
                self.require(path, item.get("locator"), "source span locator required")
            for value in self.items(path, data.get("relations", []), "relations"):
                item = self.mapping(path, value, "relation")
                self.support(path, item)
                relation = item.get("type")
                self.require(path, member(relation, NARRATIVE | ORDER | CONCURRENT), "invalid relation type")
                self.require(path, member(item.get("certainty"), CERTAINTY), "relation certainty required")
                if "precision" in item:
                    self.require(path, member(item["precision"], PRECISION), "unsupported relation precision")
                target = self.link(path, item.get("target"), {"chronology_segment"})
                self.require(path, target != path, "self relation not allowed")
                self.scoped_target(path, path, target)
                if relation == "probably_parallel_with":
                    self.require(path, item.get("certainty") == "uncertain", "probably_parallel_with must be uncertain")
                if target and item.get("certainty") == "exact-at-precision":
                    detail = self.describe(path, item, "segment relation")
                    if member(relation, ORDER):
                        self.edges.append(((path, "placement"), (target, "placement"), detail))
                    elif member(relation, CONCURRENT):
                        self.concurrent.append(((path, "placement"), (target, "placement"), relation, item.get("precision"), detail))

    def contradictions(self):
        for (subject, prop), claims in self.dates.items():
            for i, (a, origin) in enumerate(claims):
                for b, other in claims[i + 1:]:
                    if a[0] > b[1] or b[0] > a[1]:
                        self.conflicts.append(f"incompatible {prop} dates for {self.records.get(subject, {}).get('id', subject.stem)}; {origin}; versus {other}")
        graph = {}
        for a, b, detail in self.edges:
            graph.setdefault(a, set()).add(b)
            for left, origin in self.dates.get(a, []):
                for right, other in self.dates.get(b, []):
                    if left[0] > right[1]:
                        self.conflicts.append(f"ordering contradicts comparable dates; {detail}; {origin}; versus {other}")
        def reaches(start, end):
            pending, visited = list(graph.get(start, ())), set()
            while pending:
                node = pending.pop()
                if node == end:
                    return True
                if node not in visited:
                    visited.add(node)
                    pending.extend(graph.get(node, ()))
            return False
        for node in graph:
            if reaches(node, node):
                witnesses = [detail for a, b, detail in self.edges if (a == node or reaches(node, a)) and (b == node or reaches(b, node))]
                self.conflicts.append(f"strict temporal cycle at {node[0].stem}:{node[1]}; preserve evidence and review curation; " + "; ".join(witnesses))
        def order_witnesses(start, end):
            return [edge for x, y, edge in self.edges if (x == start or reaches(start, x)) and (y == end or reaches(y, end))]

        for a, b, relation, precision, detail in self.concurrent:
            if relation == "overlaps":
                # Ordered starts or ordered ends alone never prove disjoint intervals.
                for first, second in ((a[0], b[0]), (b[0], a[0])):
                    for left, right in (((first, "end"), (second, "start")), ((first, "placement"), (second, "placement"))):
                        if reaches(left, right):
                            self.conflicts.append(f"overlaps conflicts with interval separation; {detail}; " + "; ".join(order_witnesses(left, right)))
                    for end, origin in self.dates.get((first, "end"), []):
                        for start, other in self.dates.get((second, "start"), []):
                            if end[1] < start[0]:
                                self.conflicts.append(f"overlaps conflicts with end before start; {detail}; {origin}; versus {other}")
                for left, origin in self.dates.get((a[0], "placement"), []):
                    for right, other in self.dates.get((b[0], "placement"), []):
                        if left[0] > right[1] or right[0] > left[1]:
                            self.conflicts.append(f"overlaps conflicts with disjoint placement dates; {detail}; {origin}; versus {other}")
            elif relation == "simultaneous_with":
                # Legacy edges without precision assert direct simultaneity. An
                # explicitly coarse bucket can contain strictly ordered instants.
                if precision is None and (reaches(a, b) or reaches(b, a)):
                    witnesses = order_witnesses(a, b) + order_witnesses(b, a)
                    self.conflicts.append(f"simultaneous_with concurrency conflicts with strict order; {detail}; " + "; ".join(witnesses))
                widths = {"year": 336, "month": 28, "day": 1, "exact-date": 1, "exact-datetime": 1}
                width = widths.get(precision) if isinstance(precision, str) else 1 if precision is None else None
                if width is None:
                    continue  # Broad/unknown/approximate precision has no exact bucket.
                def bucket(value):
                    return value // width if isinstance(value, int) else value  # preserve unbounded endpoints
                for left, origin in self.dates.get(a, []):
                    for right, other in self.dates.get(b, []):
                        if bucket(left[0]) > bucket(right[1]) or bucket(right[0]) > bucket(left[1]):
                            self.conflicts.append(f"simultaneous_with conflicts with disjoint {a[1]}/{b[1]} dates at precision {precision or 'unspecified'}; {detail}; {origin}; versus {other}")

    def run(self):
        names = subprocess.check_output(["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"], cwd=self.root).decode().split("\0")
        ids, texts, expected_types = {}, {}, {}
        for name in sorted(set(names)):
            path = self.root / name
            if not name.endswith(".md") or not path.is_file() or name.startswith(("tmp/", "temp/", ".")):
                continue
            text = path.read_text(encoding="utf-8-sig")
            texts[path] = text
            if name.startswith("templates/"):
                continue
            parts = Path(name).parts
            expected = None
            if len(parts) == 3 and parts[0] == "chronologies" and parts[2] == "chronology.md":
                expected = "chronology"
            elif len(parts) == 4 and parts[0] == "chronologies" and parts[2] == "segments":
                expected = "chronology_segment"
            if expected:
                expected_types[path] = expected
            elif parts[0] == "chronologies" and path.name != "README.md":
                self.error(path, "unsupported chronology record path; use campaign chronology.md or segments/*.md")
            match = re.match(r"^---\n(.*?)\n---(?:\n|$)", text, re.S)
            if not match:
                if expected or (name.startswith("chronologies/") and path.name != "README.md"):
                    self.error(path, "chronology record frontmatter required")
                continue
            try:
                data = yaml.load(match[1], Loader=UniqueLoader)
                if not isinstance(data, dict):
                    raise ValueError("frontmatter must be a mapping")
            except (yaml.YAMLError, ValueError, TypeError) as error:
                self.error(path, f"invalid YAML: {error}")
                continue
            if not expected and "id" not in data and "record_type" not in data:
                continue
            if expected:
                self.require(path, data.get("record_type") == expected, f"record_type must be {expected} at this path")
            self.records[path] = data
            rid = data.get("id")
            if self.require(path, isinstance(rid, str) and ID.fullmatch(rid), "invalid stable ASCII record ID"):
                self.require(path, rid not in ids, f"duplicate ID {rid}")
                ids[rid] = path
                if expected != "chronology" and data.get("record_type") != "chronology":
                    self.require(path, path.stem == rid, "record filename must equal ID")
            self.require(path, isinstance(data.get("record_type"), str) and data["record_type"].strip(), "record_type must be a nonempty string")
            headings = re.findall(r"^# (.+)$", text, re.M)
            self.require(path, headings == [str(data.get("reference_name", data.get("title")))], "one H1 matching reference_name/title required")
        for path, text in texts.items():
            if path.is_relative_to(self.root / "sources") and path not in self.records and path.name != "README.md":
                continue  # Raw evidence can contain source-native bracket syntax.
            # Prose links only; fenced code/placeholder examples are intentionally schematic.
            prose = re.sub(r"```.*?```", "", text, flags=re.S)
            for value in re.findall(r"\[[^\]]*\]\(([^)]+)\)", prose):
                if not any(x in value for x in ("<", ">")) and not value.startswith(("https://", "http://", "mailto:")):
                    self.link(path, value)
        for path, data in self.records.items():
            kind = data.get("record_type")
            chronology_kind = expected_types.get(path, kind)
            if member(chronology_kind, {"chronology", "chronology_segment"}):
                self.require(path, isinstance(data.get("reference_name"), str) and data["reference_name"].strip(), "chronology reference_name required")
                prefix = "chronology-segment-" if chronology_kind == "chronology_segment" else "chronology-"
                self.require(path, isinstance(data.get("id"), str) and data["id"].startswith(prefix), "wrong chronology ID prefix")
                self.chronology(path, data, chronology_kind)
            if kind == "campaign" and "chronology" in data:
                target = self.link(path, data["chronology"], {"chronology"})
                if target in self.records:
                    self.require(path, self.link(target, self.records[target].get("campaign"), {"campaign"}) == path, "campaign chronology points to another campaign")
            if kind == "event":
                for value in self.items(path, data.get("chronology_segments", []), "chronology_segments"):
                    item = self.mapping(path, value, "event segment link")
                    self.support(path, item)
                    self.link(path, item.get("segment"), {"chronology_segment"})
            if member(kind, {"event", "chronology_segment", "chronology"}) and "temporal" in data:
                temporal = self.mapping(path, data["temporal"], "temporal")
                for item in self.items(path, temporal.get("assertions"), "temporal.assertions"):
                    self.assertion(path, item, kind == "chronology")
            # A manifest anchor can refer to a legacy-only event. The presence of
            # an extension on this record must not gate legacy comparison.
            if member(kind, {"event", "chronology_segment"}) and "time" in data:
                legacy = self.mapping(path, data["time"], "time")
                for prop in ("start", "end"):
                    if prop in legacy:
                        point = self.mapping(path, legacy[prop], f"time.{prop}")
                        span = self.date(path, point, point.get("precision"))
                        if span:
                            detail = self.describe(path, {"value": point, "sources": legacy.get("sources", [])}, f"time.{prop}")
                            self.dates.setdefault((path, prop), []).append((span, detail))
        self.contradictions()
        return self


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    result = Validator(args.root).run()
    for error in result.errors:
        print(f"ERROR: {error}")
    for conflict in sorted(set(result.conflicts)):
        print(f"CONTRADICTION: {conflict}")
    print(f"records={len(result.records)} errors={len(result.errors)} contradictions={len(set(result.conflicts))}")
    return 1 if result.errors else 2 if result.conflicts else 0


if __name__ == "__main__":
    raise SystemExit(main())
