# Temporal model

## Interval-first events

Events are normally intervals. Their bounds may be precise, approximate, differently precise, or unknown. An event may cover a short game, several sessions, a campaign chapter, part of a campaign, or a longer development with subordinate events. Sessions and historical events are separate concepts.

A record may combine a human-readable description with only the structured precision supported by evidence. A schematic form is:

```yaml
time:
  description: <human-readable interval or uncertainty>
  start:
    precision: year
    year_ap: <negative before 0, zero at the epoch, positive after 0>
  end:
    precision: approximate-year
    year_ap: <negative before 0, zero at the epoch, positive after 0>
```

The `description` is always allowed. Omit unsupported bounds or components. Suitable precision vocabulary includes `exact-datetime`, `exact-date`, `day` (equivalent date granularity), `month`, `year`, `approximate-year`, `century`, `age`, `broad`, and `unknown`. This vocabulary is provisional until real material tests it.

For an exact fictional date, use supported components without implying a real-world conversion:

```yaml
time:
  description: <exact fictional date and time>
  start:
    precision: exact-datetime
    year_ap: <negative before 0, zero at the epoch, positive after 0>
    month: <calendar month number>
    day: <day of month>
    time: <time as recorded by the source>
```

Do not add an end merely to satisfy a schema. An instantaneous or unresolved event may have only one known bound and explanatory prose.

## AP epoch

Year `0 pAP` begins on day 1 of `prvenec`. This calendar boundary defines the start of year 0; it is not the instant at which Amiasovo proroctví occurred. Structured `year_ap` values are signed integers: negative before year 0, `0` within year 0, and positive after year 0. This provides one chronology without a separate system for earlier years.

Amiasovo proroctví occurred during year 0, but its exact day is not known. The year was named after the event later. These facts do not require creating an event record now, and no more precise date may be inferred.

In Czech human-facing text, write the absolute year number followed by `přPA` for a year before the epoch and `poPA` for a year after it. For example, system values `-200` and `200` are rendered as `200 přPA` and `200 poPA`. The epoch year itself is written `0 pAP`.

Year 0 corresponds approximately to year 0 AD only as an orientation aid for technological and social analogy. It is not an exact conversion rule.

## Ages

Seven broad Ages provide contextual historical periodization. Their confirmed labels and analogues are in [ages.yaml](../config/ages.yaml). No exact year boundaries are known or implied. Dates take precedence when known; an Age may be recorded or inferred only when justified and should not manufacture date precision.

## Calendar interaction

The approved fictional calendar is recorded in [calendar.yaml](../config/calendar.yaml). It has 12 months of 28 days, a 336-day year, and seven-day weeks. Weekdays use Czech names in Monday-first order: `pondělí`, `úterý`, `středa`, `čtvrtek`, `pátek`, `sobota`, and `neděle`. Every week and every month begins on `pondělí`, so each month consists of four complete Monday-to-Sunday weeks. In order, its months are `prvenec`, `druhenec`, `třetinec`, `čtvrtenec`, `pátenec`, `šestenec`, `sedmenec`, `osmenec`, `devatenec`, `desátenec`, `jedenáctenec`, and `dvanáctenec`.

Each season consists of exactly three consecutive months: `jaro` comprises `prvenec`, `druhenec`, and `třetinec`; `léto` comprises `čtvrtenec`, `pátenec`, and `šestenec`; `podzim` comprises `sedmenec`, `osmenec`, and `devatenec`; and `zima` comprises `desátenec`, `jedenáctenec`, and `dvanáctenec`.

The last Sunday, day 28, of every third month is a seasonal marker: the last Sunday of `třetinec` is the spring equinox (`jarní rovnodennost`), the last Sunday of `šestenec` is the summer solstice (`letní slunovrat`), the last Sunday of `devatenec` is the autumn equinox (`podzimní rovnodennost`), and the last Sunday of `dvanáctenec` is the winter solstice (`zimní slunovrat`). Full moon always occurs during the night of the last Sunday, day 28, of each month. These are approved calendar rules rather than provisional interpretations.

Exact dates use fictional calendar components. Approximate real-world analogy must never be converted automatically into a fictional date.

## Optional temporal assertions

Events and chronology segments may add `temporal.assertions`, a list of independent claims. Chronology manifests use the same list for anchors, with a required `subject` link identifying the event or segment each anchor constrains. These are an extension of `time`, not a migration or replacement. Neither representation overrides the other; duplicate encoding is not required. Preserve differently precise or contradictory accounts separately and report comparable contradictions instead of reconciling them silently.

Each assertion requires:

- `kind`: `absolute`, `bounded`, `relative`, or `relation`;
- `property`: `start`, `end`, or `placement` (the event/segment as a whole);
- `precision`: supported granularity, including the existing provisional values;
- `certainty`: `exact-at-precision`, `approximate`, `bounded`, or `uncertain`;
- `confidence`, `basis`, and local `sources` or identifiable `curator_clarification`, following the [chronology provenance contract](../chronologies/README.md#local-evidence-shape).

Precision describes how fine a time is stated, certainty describes whether that value is exact at that precision, and confidence describes the strength of the interpretation/evidence. A low-confidence year claim can still be exact at year precision. Existing `approximate-year` remains valid; in new assertions use it with `certainty: approximate` (or use `precision: year` with that certainty). Existing `time` needs no added certainty/confidence fields.

### Assertion payloads

| Kind | Payload |
| --- | --- |
| `absolute` | `value` containing only attested components. |
| `bounded` | `earliest` and/or `latest`, each with its own `precision` and components; `certainty: bounded`. |
| `relative` | `target`, `target_property` (`start`, `end`, `placement`), `direction` (`before`, `after`), optional `offset: {value, unit}`. |
| `relation` | `target`, `target_property`, `relation` (`precedes`, `immediately_precedes`, `simultaneous_with`, `overlaps`, `probably_parallel_with`). No numeric date required. |

Relative/relation targets are event or chronology-segment links. A segment-to-segment target stays within its chronology. `offset.value` is a nonnegative number; `unit` is `day`, `week`, `month`, or `year` under the approved calendar, without automatic conversion or timeline solving. An offset-free relative assertion expresses ordering only. Relation/relative precision may be `unknown`; prose and `basis` must describe any limits. `probably_parallel_with` uses `certainty: uncertain`.

`earliest`/`latest` constrain the selected property; **they are not automatically the event's actual duration endpoints**. For example, bounds on `start` describe the window in which it began. Bounds on `placement` locate the whole occurrence without asserting when it started or finished. Use separate start/end assertions when duration endpoints are evidenced. The outer precision describes the overall claim; each bound retains its own precision, including differently precise bounds.

For comparable whole-unit relations, `precedes`/`immediately_precedes` mean the subject ends before the target starts. With explicit start/end properties, they order those properties. Overlap describes intervals; simultaneity at a stated precision does not establish identical duration. Do not treat qualified hypotheses as hard constraints or collapse incompatible claims.

### Component rules

AP values use signed integer `year_ap`, including zero and negative years. `poPA` is a human-readable era suffix, **not a calendar ID**. No `calendar` identifier is introduced here; future identifiers require explicit documentation and approval. The default is the existing approved fictional calendar.

Generic named calendars are explicitly **out of scope for the current approved schema**. Arbitrary `calendar:` fields are unsupported and rejected by validation. This is an intentional scope limit, not an incomplete registry: no named-calendar objects, registry, or conversion logic are required. Broader fictional calendar support is a future model extension; prose era notation alone never authorizes a calendar identifier.

`month` is an integer 1–12 and requires `year_ap`; `day` is an integer 1–28 and requires month/year; `time` is a quoted source-attested string and requires day/month/year. `exact-date` requires year/month/day; `exact-datetime` additionally requires time. `year` and `approximate-year` require only `year_ap` and must not carry fabricated month/day/time. `century`, `age`, `broad`, and `unknown` may retain supported descriptions and contextual components without invented boundaries. Never turn `year_ap: 1032` at `precision: year` into `1032-01-01`.

`month` precision requires year/month and excludes finer day/time components. `day` precision has the same component rules as `exact-date`: year/month/day without a time component. These granularities use the existing AP calendar; no calendar identifier or conversion is added.

See [generic examples](chronology-examples.md) for exact dates, year-only claims, approximate and bounded claims, before/after relations, narrative branches, and simultaneity.

### Direct contradiction checks

The [canonical validator](../tools/README.md) loads legacy event/segment `time` independently of `temporal.assertions`, including when an assertion about that subject is in a chronology manifest. Directly disjoint comparable AP-year/date claims about the same property are reported with their subject/record IDs, values, and available local support. Neither encoding wins and neither must duplicate the other.

Exact `simultaneous_with` compares the selected subject/target properties at the relation/assertion's stated precision, never at a finer granularity than both endpoints support. Different days in one month are compatible at month precision; different months in one year are compatible at year precision. A year-only endpoint and a date within that year are compatible even when the relation claims day precision. Missing precision is insufficient evidence, not contradiction. Time-of-day strings are not ordered or equated by the validator; their attested date can still support day/month/year comparison. Broad/unknown/approximate relation precision has no exact comparison bucket.

Segment relations may supply `precision` explicitly. Existing edges that omit it retain direct simultaneity checks against strict order and disjoint supported placement windows; omission never manufactures date components. For an equality claim limited to a year, month, or day, state that precision. Strict ordering within the same stated bucket is compatible with simultaneity at that granularity.

`overlaps` uses a separate interval-intersection check. Ordered starts or ordered ends alone are compatible with overlap. A contradiction requires a supported strict path from one end to the other start, strict whole-unit precedence, safely disjoint whole-unit placement windows, or comparable end/start dates proving separation. Equal or unresolved endpoint windows do not prove separation. Overlap never implies equal starts or equal ends.

Compatible differently precise claims and bounded windows are valid; precision differences alone do not establish contradiction. Approximate claims are not converted into exact bounds. Start, end, and placement remain distinct. Narrative edges and probable parallelism do not imply temporal equivalence or enter the strict ordering graph. Reporting is read-only, preserves all claims, and does not perform general constraint solving.

## Source time and fictional time

Forum `posted_at`, document order, letter order/date, session number/date, chat timestamps, transcript order, and file creation time are source/document metadata. They may scaffold reconstruction but establish fictional chronology only when the source semantics support the inference, recorded with local provenance.

For letters distinguish document order, fictional writing time, and time of narrated events. For session logs distinguish real session order/date, fictional time, and flashbacks/retrospectives. Do not date narrated events merely from a document's writing or posting date.
