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

The `description` is always allowed. Omit unsupported bounds or components. Suitable precision vocabulary includes `exact-datetime`, `exact-date`, `year`, `approximate-year`, `century`, `age`, `broad`, and `unknown`. This vocabulary is provisional until real material tests it.

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

Year `0 AP` is defined by the event named “Amiasovo proroctví” / “Amias's Prophecy.” This epoch fact does not create an event record during bootstrap. Structured `year_ap` values are signed integers: negative before the epoch, `0` at the epoch, and positive after the epoch. This provides one chronology without a separate system for years before 0.

In Czech human-facing text, write the absolute year number followed by `přPA` for a year before the epoch and `poPA` for a year after it. For example, system values `-200` and `200` are rendered as `200 přPA` and `200 poPA`. The epoch itself remains `0 AP`.

The epoch corresponds approximately to year 0 AD only as an orientation aid for technological and social analogy. It is not an exact conversion rule.

## Ages

Seven broad Ages provide contextual historical periodization. Their confirmed labels and analogues are in [ages.yaml](../config/ages.yaml). No exact year boundaries are known or implied. Dates take precedence when known; an Age may be recorded or inferred only when justified and should not manufacture date precision.

## Calendar interaction

The approved fictional calendar is recorded in [calendar.yaml](../config/calendar.yaml). It has 12 months of 28 days, a 336-day year, and seven-day weeks. Weekdays use Czech names in Monday-first order: `pondělí`, `úterý`, `středa`, `čtvrtek`, `pátek`, `sobota`, and `neděle`. Every week and every month begins on `pondělí`, so each month consists of four complete Monday-to-Sunday weeks. In order, its months are `prvenec`, `druhenec`, `třetinec`, `čtvrtenec`, `pátenec`, `šestenec`, `sedmenec`, `osmenec`, `devatenec`, `desátenec`, `jedenáctenec`, and `dvanáctenec`.

Each season consists of exactly three consecutive months: `jaro` comprises `prvenec`, `druhenec`, and `třetinec`; `léto` comprises `čtvrtenec`, `pátenec`, and `šestenec`; `podzim` comprises `sedmenec`, `osmenec`, and `devatenec`; and `zima` comprises `desátenec`, `jedenáctenec`, and `dvanáctenec`.

The last Sunday, day 28, of every third month is a seasonal marker: the last Sunday of `třetinec` is the spring equinox (`jarní rovnodennost`), the last Sunday of `šestenec` is the summer solstice (`letní slunovrat`), the last Sunday of `devatenec` is the autumn equinox (`podzimní rovnodennost`), and the last Sunday of `dvanáctenec` is the winter solstice (`zimní slunovrat`). Full moon always occurs during the night of the last Sunday, day 28, of each month. These are approved calendar rules rather than provisional interpretations.

Exact dates use fictional calendar components. Approximate real-world analogy must never be converted automatically into a fictional date.
