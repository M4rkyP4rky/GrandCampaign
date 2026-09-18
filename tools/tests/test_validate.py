"""Synthetic governance regressions; no campaign data is materialized."""
import copy
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from validate import Validator


class ChronologyValidation(unittest.TestCase):
    def setUp(self):
        self.work = tempfile.TemporaryDirectory()
        self.addCleanup(self.work.cleanup)
        self.root = Path(self.work.name).resolve()
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        self.campaign = "campaigns/campaign-demo.md"
        self.manifest = "chronologies/campaign-demo/chronology.md"
        self.a = "chronologies/campaign-demo/segments/chronology-segment-demo-a.md"
        self.b = "chronologies/campaign-demo/segments/chronology-segment-demo-b.md"
        self.event = "events/event-demo.md"
        self.write(self.campaign, {"id": "campaign-demo", "record_type": "campaign", "reference_name": "Demo campaign"})
        self.write(self.event, {"id": "event-demo", "record_type": "event", "reference_name": "Demo event"})
        source = self.root / "sources/evidence.md"
        source.parent.mkdir()
        source.write_text("# Synthetic evidence\n", encoding="utf-8")

    def write(self, name, data):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("---\n" + yaml.safe_dump(data, sort_keys=False) + "---\n\n# " + data["reference_name"] + "\n", encoding="utf-8")

    def support(self):
        return {"basis": "Synthetic evidence", "confidence": "high", "sources": ["../../../sources/evidence.md"]}

    def seed(self):
        manifest = {"id": "chronology-demo", "record_type": "chronology", "reference_name": "Demo chronology", "campaign": "../../" + self.campaign, "status": "draft", "record_sources": ["../../sources/evidence.md"], "threads": [{"id": "thread-main", "label": "Main"}], "segments": ["segments/" + Path(self.a).name, "segments/" + Path(self.b).name]}
        self.write(self.manifest, manifest)
        data = {"id": Path(self.a).stem, "record_type": "chronology_segment", "reference_name": "Demo A", "record_sources": ["../../../sources/evidence.md"], "chronology": "../chronology.md", "campaign": "../../../" + self.campaign, "thread": "thread-main", "chronology_confidence": "high", "boundaries": [{"description": "Synthetic grouping", **self.support()}]}
        self.write(self.a, data)
        other = copy.deepcopy(data)
        other.update(id=Path(self.b).stem, reference_name="Demo B")
        self.write(self.b, other)
        return data, other

    def relation(self, kind, target, certainty="exact-at-precision"):
        return {"type": kind, "target": Path(target).name, "certainty": certainty, **self.support()}

    def absolute(self, year=1032, prop="placement"):
        return {"kind": "absolute", "property": prop, "precision": "year", "certainty": "exact-at-precision", "value": {"year_ap": year}, **self.support()}

    def check(self):
        return Validator(self.root).run()

    def read(self, name):
        return yaml.safe_load((self.root / name).read_text(encoding="utf-8").split("---")[1])

    def cli(self):
        return subprocess.run([sys.executable, "-B", str(Path(__file__).resolve().parents[1] / "validate.py"), str(self.root)], capture_output=True, text=True, encoding="utf-8")

    def test_existing_records_need_no_chronology(self):
        result = self.check()
        self.assertEqual((result.errors, result.conflicts), ([], []))

    def test_zero_event_segment_year_only_negative_epoch(self):
        a, _ = self.seed()
        for year in (-20, 0, 1032):
            a["temporal"] = {"assertions": [self.absolute(year)]}
            self.write(self.a, a)
            result = self.check()
            self.assertEqual((result.errors, result.conflicts), ([], []))

    def test_narrative_cycle_is_not_temporal_cycle(self):
        a, b = self.seed()
        a["relations"] = [self.relation("splits_into", self.b)]
        b["relations"] = [self.relation("rejoins", self.a)]
        self.write(self.a, a)
        self.write(self.b, b)
        self.assertEqual(self.check().conflicts, [])
        a["relations"].append(self.relation("precedes", self.b))
        b["relations"].append(self.relation("immediately_precedes", self.a))
        self.write(self.a, a)
        self.write(self.b, b)
        result = self.check()
        self.assertEqual(result.errors, [])
        self.assertTrue(any("cycle" in x for x in result.conflicts))

    def test_qualified_edge_not_hardened(self):
        a, b = self.seed()
        a["relations"] = [self.relation("precedes", self.b)]
        b["relations"] = [self.relation("precedes", self.a, "uncertain")]
        self.write(self.a, a)
        self.write(self.b, b)
        self.assertEqual(self.check().conflicts, [])

    def test_aggregate_provenance_cannot_replace_local_support(self):
        a, _ = self.seed()
        a["relations"] = [self.relation("continues_to", self.b)]
        del a["relations"][0]["sources"]
        self.write(self.a, a)
        self.assertTrue(any("local sources" in x for x in self.check().errors))

    def test_bad_thread_and_broken_target(self):
        a, _ = self.seed()
        a["thread"] = "thread-undeclared"
        a["relations"] = [self.relation("precedes", "missing.md")]
        self.write(self.a, a)
        errors = self.check().errors
        self.assertTrue(any("thread" in x for x in errors))
        self.assertTrue(any("broken" in x for x in errors))

    def test_fake_calendar_date_and_fabricated_precision(self):
        a, _ = self.seed()
        value = self.absolute()
        value["value"].update(calendar="poPA", month=13, day=29)
        a["temporal"] = {"assertions": [value]}
        self.write(self.a, a)
        errors = self.check().errors
        for phrase in ("calendar", "invalid month", "invalid day", "finer components"):
            self.assertTrue(any(phrase in x for x in errors), errors)

    def test_conflicting_claims_and_legacy_time(self):
        a, _ = self.seed()
        a["temporal"] = {"assertions": [self.absolute(1032, "start")]}
        a["time"] = {"start": {"precision": "year", "year_ap": 1040}}
        self.write(self.a, a)
        self.assertTrue(self.check().conflicts)

    def test_bounds_constrain_property_not_duration(self):
        a, _ = self.seed()
        bounded = {"kind": "bounded", "property": "start", "precision": "broad", "certainty": "bounded", "earliest": {"precision": "year", "year_ap": 1031}, "latest": {"precision": "exact-date", "year_ap": 1033, "month": 2, "day": 7}, **self.support()}
        a["temporal"] = {"assertions": [bounded, self.absolute(1040, "end")]}
        self.write(self.a, a)
        result = self.check()
        self.assertEqual((result.errors, result.conflicts), ([], []))
        bounded["earliest"]["year_ap"] = 1040
        self.write(self.a, a)
        self.assertTrue(any("earliest exceeds latest" in x for x in self.check().conflicts))

    def test_simultaneity_conflicts_with_order(self):
        a, _ = self.seed()
        a["relations"] = [self.relation("precedes", self.b), self.relation("simultaneous_with", self.b)]
        self.write(self.a, a)
        self.assertTrue(any("concurrency" in x for x in self.check().conflicts))

    def test_identity_envelope_and_self_relation(self):
        a, _ = self.seed()
        a["relations"] = [self.relation("precedes", self.a)]
        a["id"] = "chronology-demo"
        self.write(self.a, a)
        errors = self.check().errors
        for phrase in ("duplicate ID", "filename", "self relation"):
            self.assertTrue(any(phrase in x for x in errors), errors)

    def test_curator_support_optional_event_navigation(self):
        self.seed()
        decision = self.root / "curation/resolved.md"
        decision.parent.mkdir()
        decision.write_text("# Resolved\n\n## curation-demo-001\n\nSynthetic decision.\n", encoding="utf-8")
        self.write(self.event, {"id": "event-demo", "record_type": "event", "reference_name": "Demo event", "chronology_segments": [{"segment": "../" + self.a, "basis": "Synthetic decision", "confidence": "high", "curator_clarification": {"record": "../curation/resolved.md", "locator": "curation-demo-001"}}]})
        result = self.check()
        self.assertEqual((result.errors, result.conflicts), ([], []))

    def test_manifest_anchor_and_cross_scope_thread(self):
        a, _ = self.seed()
        path = self.root / self.manifest
        manifest = yaml.safe_load(path.read_text(encoding="utf-8").split("---")[1])
        claim = self.absolute()
        claim.update(subject="segments/" + Path(self.a).name, sources=["../../sources/evidence.md"])
        manifest["temporal"] = {"assertions": [claim]}
        self.write(self.manifest, manifest)
        self.assertEqual(self.check().errors, [])
        a["chronology"] = "../../../campaigns/campaign-demo.md"
        self.write(self.a, a)
        self.assertTrue(self.check().errors)

    def test_misplaced_chronology_record_is_reported(self):
        self.seed()
        (self.root / "chronologies/campaign-demo/misplaced.md").write_text("---\n{}\n---\n# Misplaced record\n", encoding="utf-8")
        self.assertTrue(any("unsupported chronology record path" in x for x in self.check().errors))

    def test_relative_assertions_and_required_fields(self):
        a, b = self.seed()
        claim = {"kind": "relative", "property": "placement", "precision": "unknown", "certainty": "exact-at-precision", "target": Path(self.b).name, "target_property": "placement", "direction": "before", **self.support()}
        a["temporal"] = {"assertions": [claim]}
        b["relations"] = [self.relation("precedes", self.a)]
        self.write(self.a, a)
        self.write(self.b, b)
        self.assertTrue(self.check().conflicts)
        del claim["target_property"]
        self.write(self.a, a)
        self.assertTrue(any("target_property" in x for x in self.check().errors))

    def test_all_derived_associations_need_local_evidence(self):
        a, _ = self.seed()
        a["events"] = [{"event": "../../../" + self.event}]
        self.write(self.a, a)
        errors = self.check().errors
        for phrase in ("local basis", "local confidence", "local sources"):
            self.assertTrue(any(phrase in x for x in errors), errors)

    def test_template_envelopes_and_example_yaml_parse(self):
        repo = Path(__file__).resolve().parents[2]
        for name in ("chronology.md", "chronology-segment.md"):
            text = (repo / "templates" / name).read_text(encoding="utf-8")
            data = yaml.safe_load(text.split("---")[1])
            for field in ("id", "record_type", "reference_name", "record_sources"):
                self.assertIn(field, data)
            self.assertIn("# " + data["reference_name"], text)
        import re
        text = (repo / "docs/chronology-examples.md").read_text(encoding="utf-8")
        for block in re.findall(r"```yaml\n(.*?)```", text, re.S):
            self.assertIsInstance(yaml.safe_load(block), dict)

    def test_unsupported_calendar_and_approximate_year_scope(self):
        a, _ = self.seed()
        claim = self.absolute(-20)
        claim.update(precision="approximate-year", certainty="approximate")
        a["temporal"] = {"assertions": [claim]}
        a["time"] = {"start": {"precision": "approximate-year", "year_ap": -30}}
        self.write(self.a, a)
        result = self.check()
        self.assertEqual((result.errors, result.conflicts), ([], []))
        claim["value"]["calendar"] = "unsupported-calendar"
        self.write(self.a, a)
        self.assertTrue(any("calendar" in x for x in self.check().errors))

    def test_manifest_anchor_compares_legacy_only_event(self):
        self.seed()
        event = self.read(self.event)
        event["time"] = {"start": {"precision": "year", "year_ap": 1040}, "sources": ["../sources/evidence.md"]}
        self.write(self.event, event)
        manifest = self.read(self.manifest)
        claim = self.absolute(1032, "start")
        claim.update(subject="../../" + self.event, sources=["../../sources/evidence.md"])
        manifest["temporal"] = {"assertions": [claim]}
        self.write(self.manifest, manifest)
        before = {p: p.read_bytes() for p in self.root.rglob("*.md")}
        result = self.check()
        self.assertEqual(result.errors, [])
        diagnostic = "\n".join(result.conflicts)
        for value in ("incompatible start", "event-demo", "chronology-demo", "1040", "1032", "time.start", "sources/evidence.md"):
            self.assertIn(value, diagnostic)
        self.assertEqual(before, {p: p.read_bytes() for p in before})
        run = self.cli()
        self.assertEqual(run.returncode, 2, run.stdout + run.stderr)
        self.assertIn("CONTRADICTION:", run.stdout)
        self.assertNotIn("Traceback", run.stderr)
        # A different property is not a conflict, nor is an approximate year.
        claim["property"] = "end"
        self.write(self.manifest, manifest)
        self.assertEqual(self.check().conflicts, [])
        claim.update(property="start", certainty="approximate")
        self.write(self.manifest, manifest)
        self.assertEqual(self.check().conflicts, [])

    def test_exact_concurrence_disjoint_placements(self):
        a, b = self.seed()
        a["temporal"] = {"assertions": [self.absolute(1032)]}
        b["temporal"] = {"assertions": [self.absolute(1040)]}
        self.write(self.b, b)
        for relation in ("simultaneous_with", "overlaps"):
            with self.subTest(relation=relation):
                a["relations"] = [self.relation(relation, self.b)]
                self.write(self.a, a)
                result = self.check()
                self.assertEqual(result.errors, [])
                diagnostic = "\n".join(result.conflicts)
                for value in (relation, "1032", "1040", Path(self.a).stem, Path(self.b).stem, "sources/evidence.md"):
                    self.assertIn(value, diagnostic)

    def test_narrative_and_probable_relations_do_not_equal_dates(self):
        a, b = self.seed()
        a["temporal"] = {"assertions": [self.absolute(1032)]}
        b["temporal"] = {"assertions": [self.absolute(1040)]}
        self.write(self.b, b)
        for relation in ("continues_to", "splits_into", "rejoins", "probably_parallel_with", "simultaneous_with"):
            certainty = "uncertain" if relation in ("probably_parallel_with", "simultaneous_with") else "exact-at-precision"
            with self.subTest(relation=relation):
                a["relations"] = [self.relation(relation, self.b, certainty)]
                self.write(self.a, a)
                result = self.check()
                self.assertEqual((result.errors, result.conflicts), ([], []))

    def test_concurrence_preserves_approximation_scope_and_precision(self):
        a, b = self.seed()
        a["relations"] = [self.relation("simultaneous_with", self.b)]
        a["temporal"] = {"assertions": [self.absolute(1032)]}
        variants = [self.absolute(1040, "start"), self.absolute(1040)]
        variants[1]["certainty"] = "approximate"
        day = self.absolute(1032)
        day.update(precision="exact-date", value={"year_ap": 1032, "month": 3, "day": 12})
        variants.append(day)
        variants.append({"kind": "bounded", "property": "placement", "precision": "broad", "certainty": "bounded", "earliest": {"precision": "year", "year_ap": 1031}, "latest": {"precision": "exact-date", "year_ap": 1033, "month": 2, "day": 7}, **self.support()})
        self.write(self.a, a)
        for claim in variants:
            with self.subTest(claim=claim):
                b["temporal"] = {"assertions": [claim]}
                self.write(self.b, b)
                result = self.check()
                self.assertEqual((result.errors, result.conflicts), ([], []))

    def test_overlap_start_dates_are_not_equated(self):
        a, b = self.seed()
        a["temporal"] = {"assertions": [self.absolute(1032, "start"), {"kind": "relation", "property": "start", "precision": "year", "certainty": "exact-at-precision", "relation": "overlaps", "target": Path(self.b).name, "target_property": "start", **self.support()}]}
        b["temporal"] = {"assertions": [self.absolute(1040, "start")]}
        self.write(self.a, a)
        self.write(self.b, b)
        self.assertEqual(self.check().conflicts, [])

    def temporal_relation(self, relation, prop="placement", target_prop="placement", precision="year"):
        return {"kind": "relation", "property": prop, "target_property": target_prop,
                "target": Path(self.b).name, "relation": relation, "precision": precision,
                "certainty": "exact-at-precision", **self.support()}

    def dated(self, year=1032, month=3, day=1, time=None):
        claim = self.absolute(year)
        claim.update(precision="exact-date", value={"year_ap": year, "month": month, "day": day})
        if time is not None:
            claim["precision"] = "exact-datetime"
            claim["value"]["time"] = time
        return claim

    def simultaneity_case(self, left, right, precision, conflict):
        # Exercise both schema entry points, preserving fixtures across read-only checks.
        for segment_edge in (False, True):
            with self.subTest(precision=precision, segment_edge=segment_edge):
                a, b = self.seed()
                a["temporal"] = {"assertions": [left]}
                b["temporal"] = {"assertions": [right]}
                if segment_edge:
                    a["relations"] = [{**self.relation("simultaneous_with", self.b), "precision": precision}]
                else:
                    a["temporal"]["assertions"].append(self.temporal_relation("simultaneous_with", precision=precision))
                self.write(self.a, a)
                self.write(self.b, b)
                before = {p: p.read_bytes() for p in self.root.rglob("*.md")}
                result = self.check()
                self.assertEqual(result.errors, [])
                self.assertEqual(bool(result.conflicts), conflict, result.conflicts)
                self.assertEqual(before, {p: p.read_bytes() for p in self.root.rglob("*.md")})
                if conflict:
                    diagnostic = "\n".join(result.conflicts)
                    for token in (Path(self.a).stem, Path(self.b).stem, "simultaneous_with", "placement", precision, "sources", "year_ap"):
                        self.assertIn(token, diagnostic)

    def test_overlap_with_ordered_starts_or_ends(self):
        for prop in ("start", "end"):
            for reverse in (False, True):
                with self.subTest(prop=prop, reverse=reverse):
                    a, b = self.seed()
                    order = self.temporal_relation("precedes", prop, prop)
                    a["temporal"] = {"assertions": [self.temporal_relation("overlaps", prop, prop)]}
                    if reverse:
                        order["target"] = Path(self.a).name
                        b["temporal"] = {"assertions": [order]}
                    else:
                        a["temporal"]["assertions"].append(order)
                    self.write(self.a, a)
                    self.write(self.b, b)
                    result = self.check()
                    self.assertEqual((result.errors, result.conflicts), ([], []))

    def test_overlap_with_proven_interval_separation(self):
        for reverse in (False, True):
            for whole in (False, True):
                with self.subTest(reverse=reverse, whole=whole):
                    a, b = self.seed()
                    a["relations"] = [self.relation("overlaps", self.b)]
                    order = self.temporal_relation("precedes", "placement" if whole else "end", "placement" if whole else "start")
                    if reverse:
                        order["target"] = Path(self.a).name
                    (b if reverse else a)["temporal"] = {"assertions": [order]}
                    self.write(self.a, a)
                    self.write(self.b, b)
                    result = self.check()
                    self.assertEqual(result.errors, [])
                    self.assertTrue(any("overlaps conflicts with interval separation" in x for x in result.conflicts))

    def test_simultaneous_year_precision(self):
        self.simultaneity_case(self.dated(month=1), self.dated(month=2), "year", False)

    def test_simultaneous_month_precision(self):
        self.simultaneity_case(self.dated(day=1), self.dated(day=20), "month", False)

    def test_simultaneous_day_precision_contradiction(self):
        self.simultaneity_case(self.dated(day=1), self.dated(day=2), "day", True)

    def test_simultaneous_same_day_different_times(self):
        self.simultaneity_case(self.dated(time="morning"), self.dated(time="evening"), "day", False)

    def test_simultaneous_different_years(self):
        self.simultaneity_case(self.absolute(1032), self.absolute(1040), "year", True)

    def test_simultaneous_insufficient_endpoint_precision(self):
        self.simultaneity_case(self.absolute(1032), self.dated(), "day", False)
        self.simultaneity_case(self.absolute(1032), self.dated(year=1040), "day", True)

    def test_simultaneous_coarse_precision_allows_order_inside_bucket(self):
        a, b = self.seed()
        a["temporal"] = {"assertions": [self.dated(day=1), self.temporal_relation("precedes"), self.temporal_relation("simultaneous_with", precision="month")]}
        b["temporal"] = {"assertions": [self.dated(day=20)]}
        self.write(self.a, a)
        self.write(self.b, b)
        result = self.check()
        self.assertEqual((result.errors, result.conflicts), ([], []))

    def test_overlap_end_start_dates_and_touching_days(self):
        for year, conflict in ((1032, False), (1040, True)):
            a, b = self.seed()
            a["relations"] = [self.relation("overlaps", self.b)]
            a["temporal"] = {"assertions": [self.absolute(1032, "end")]}
            b["temporal"] = {"assertions": [self.absolute(year, "start")]}
            self.write(self.a, a)
            self.write(self.b, b)
            result = self.check()
            self.assertEqual(result.errors, [])
            self.assertEqual(bool(result.conflicts), conflict)

    def test_month_day_components_and_relation_precision_types(self):
        a, _ = self.seed()
        for precision, value, valid in (("month", {"year_ap": 0, "month": 12}, True), ("day", {"year_ap": -1, "month": 12, "day": 28}, True), ("month", {"year_ap": 0}, False), ("month", {"year_ap": 0, "month": 1, "day": 1}, False), ("day", {"year_ap": 0, "month": 1}, False)):
            claim = self.absolute()
            claim.update(precision=precision, value=value)
            a["temporal"] = {"assertions": [claim]}
            self.write(self.a, a)
            self.assertEqual(not self.check().errors, valid)
        a.pop("temporal")
        for precision in ([], {}, 1):
            a["relations"] = [{**self.relation("simultaneous_with", self.b), "precision": precision}]
            self.write(self.a, a)
            self.assertTrue(self.check().errors)

    def test_chronology_envelopes_cannot_bypass_discovery(self):
        self.seed()
        for name in (self.manifest, self.a):
            original = (self.root / name).read_text(encoding="utf-8")
            data = self.read(name)
            variants = ["# Missing frontmatter\n", "---\n{}\n---\n# Empty\n", "---\n[]\n---\n# Non-mapping\n"]
            for field in ("record_type", "id", "reference_name", "record_sources", "campaign"):
                changed = copy.deepcopy(data)
                del changed[field]
                variants.append("---\n" + yaml.safe_dump(changed) + "---\n# " + data["reference_name"] + "\n")
            variants += [original.replace("record_type: " + data["record_type"], "record_type: event"), original.replace("# " + data["reference_name"], "# Wrong H1")]
            for index, content in enumerate(variants):
                with self.subTest(record=name, variant=index):
                    (self.root / name).write_text(content, encoding="utf-8")
                    self.assertTrue(self.check().errors)
            (self.root / name).write_text(original, encoding="utf-8")
        self.assertEqual(self.check().errors, [])

    def test_source_resource_file_directory_missing_and_url_encoding(self):
        a, _ = self.seed()
        encoded = self.root / "sources/evidence with spaces.md"
        encoded.write_text("# Synthetic evidence\n", encoding="utf-8")
        for link, valid in (("../../../sources/", False), ("../../../sources/missing.md", False), ("../../../sources/evidence.md", True), ("../../../sources/evidence%20with%20spaces.md", True)):
            with self.subTest(link=link):
                a["boundaries"][0]["sources"] = [link]
                self.write(self.a, a)
                self.assertEqual(not self.check().errors, valid)

    def test_directory_support_rejected_for_each_local_claim(self):
        a, _ = self.seed()
        base = copy.deepcopy(a)
        unsupported = {**self.support(), "sources": ["../../../sources/"]}
        claims = {
            "boundaries": [{"description": "Synthetic boundary", **unsupported}],
            "participants": [{"entity": "../../../entities/beings/being-demo.md", **unsupported}],
            "locations": [{"location": "../../../entities/locations/location-demo.md", **unsupported}],
            "events": [{"event": "../../../" + self.event, **unsupported}],
            "relations": [{**self.relation("continues_to", self.b), **unsupported}],
            "temporal": {"assertions": [{**self.absolute(), **unsupported}]},
        }
        self.write("entities/beings/being-demo.md", {"id": "being-demo", "record_type": "being", "reference_name": "Synthetic being"})
        self.write("entities/locations/location-demo.md", {"id": "location-demo", "record_type": "location", "reference_name": "Synthetic location"})
        for field, value in claims.items():
            with self.subTest(field=field):
                a = {**base, field: value}
                self.write(self.a, a)
                self.assertTrue(any("concrete file" in x for x in self.check().errors))
        self.write(self.a, base)
        manifest = self.read(self.manifest)
        manifest["temporal"] = {"assertions": [{**self.absolute(), "subject": "segments/" + Path(self.a).name, "sources": ["../../sources/"]}]}
        self.write(self.manifest, manifest)
        self.assertTrue(any("concrete file" in x for x in self.check().errors))
        event = self.read(self.event)
        event["chronology_segments"] = [{"segment": "../" + self.a, "basis": "Synthetic link", "confidence": "high", "sources": ["../sources/"]}]
        self.write(self.event, event)
        self.assertTrue(any("events" in x and "concrete file" in x for x in self.check().errors))

    def test_curator_item_must_exist_in_concrete_queue_file(self):
        a, _ = self.seed()
        queue = self.root / "curation/resolved.md"
        queue.parent.mkdir()
        queue.write_text("# Resolved\n\n## curation-demo-001 — Synthetic decision\n\nDecision recorded.\n", encoding="utf-8")
        entry = a["boundaries"][0]
        del entry["sources"]
        for record, locator, valid in (("../../../curation/resolved.md", "curation-demo-001", True), ("../../../curation/resolved.md", "curation-demo-999", False), ("../../../curation/missing.md", "curation-demo-001", False), ("../../../curation/", "curation-demo-001", False), ("../../../curation/resolved.md", "", False)):
            with self.subTest(record=record, locator=locator):
                entry["curator_clarification"] = {"record": record, "locator": locator}
                self.write(self.a, a)
                self.assertEqual(not self.check().errors, valid)

    def test_malformed_enum_types_report_diagnostics(self):
        a, _ = self.seed()
        for value in ([], {}, 1):
            for field in ("confidence", "kind", "property", "precision", "certainty", "relation", "target_property", "direction"):
                with self.subTest(field=field, value=value):
                    claim = self.absolute()
                    if field in ("relation", "target_property", "direction"):
                        claim = {"kind": "relative" if field == "direction" else "relation", "property": "placement", "precision": "unknown", "certainty": "exact-at-precision", "target": Path(self.b).name, "target_property": "placement", **self.support()}
                        claim["direction" if field == "direction" else "relation"] = "before" if field == "direction" else "precedes"
                    claim[field] = value
                    a["temporal"] = {"assertions": [claim]}
                    self.write(self.a, a)
                    self.assertTrue(self.check().errors)
            for field in ("type", "certainty", "confidence"):
                with self.subTest(relation_field=field, value=value):
                    a.pop("temporal", None)
                    relation = self.relation("precedes", self.b)
                    relation[field] = value
                    a["relations"] = [relation]
                    self.write(self.a, a)
                    self.assertTrue(self.check().errors)
            a.pop("relations", None)
            original = copy.deepcopy(a)
            for field in ("record_type", "chronology_confidence", "thread"):
                with self.subTest(record_field=field, value=value):
                    self.write(self.a, {**original, field: value})
                    self.assertTrue(self.check().errors)
            self.write(self.a, original)
        a["boundaries"][0]["confidence"] = []
        self.write(self.a, a)
        event = self.read(self.event)
        event["record_type"] = {}
        self.write(self.event, event)
        run = self.cli()
        self.assertEqual(run.returncode, 1, run.stdout + run.stderr)
        self.assertIn("local confidence", run.stdout)
        self.assertIn("record_type", run.stdout)
        self.assertNotIn("Traceback", run.stdout + run.stderr)

    def test_malformed_adjacent_fields_continue_validation(self):
        a, _ = self.seed()
        manifest = self.read(self.manifest)
        for field in ("status", "threads", "segments", "curator_corrections"):
            with self.subTest(field=field):
                self.write(self.manifest, {**manifest, field: {}})
                self.assertTrue(self.check().errors)
        self.write(self.manifest, manifest)
        for claim in (
            {"kind": "bounded", "property": "start", "precision": "broad", "certainty": "bounded", "earliest": {"precision": {}, "year_ap": 1032}, **self.support()},
            {"kind": "relative", "property": "start", "precision": "broad", "certainty": "exact-at-precision", "target": Path(self.b).name, "target_property": "end", "direction": "after", "offset": {"value": 2, "unit": []}, **self.support()},
        ):
            a["temporal"] = {"assertions": [claim]}
            self.write(self.a, a)
            self.assertTrue(self.check().errors)


if __name__ == "__main__":
    unittest.main()
