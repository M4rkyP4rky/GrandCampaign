# Temporal model

## Interval-first events

Events are normally intervals. Their bounds may be precise, approximate, differently precise, or unknown. An event may cover a short game, several sessions, a campaign chapter, part of a campaign, or a longer development with subordinate events. Sessions and historical events are separate concepts.

A record may combine a human-readable description with only the structured precision supported by evidence. A schematic form is:

```yaml
time:
  description: <human-readable interval or uncertainty>
  start:
    precision: year
    year_ap: <signed integer>
  end:
    precision: approximate-year
    year_ap: <signed integer>
```

The `description` is always allowed. Omit unsupported bounds or components. Suitable precision vocabulary includes `exact-datetime`, `exact-date`, `year`, `approximate-year`, `century`, `age`, `broad`, and `unknown`. This vocabulary is provisional until real material tests it.

For an exact fictional date, use supported components without implying a real-world conversion:

```yaml
time:
  description: <exact fictional date and time>
  start:
    precision: exact-datetime
    year_ap: <signed integer>
    month: <calendar month number>
    day: <day of month>
    time: <time as recorded by the source>
```

Do not add an end merely to satisfy a schema. An instantaneous or unresolved event may have only one known bound and explanatory prose.

## AP epoch

Year `0 AP` is defined by the event named “Amiasovo proroctví” / “Amias's Prophecy.” This epoch fact does not create an event record during bootstrap. Years before it can use negative signed `year_ap` values, avoiding a second incompatible chronology.

The epoch corresponds approximately to year 0 AD only as an orientation aid for technological and social analogy. It is not an exact conversion rule.

## Ages

Seven broad Ages provide contextual historical periodization. Their confirmed labels and analogues are in [ages.yaml](../config/ages.yaml). No exact year boundaries are known or implied. Dates take precedence when known; an Age may be recorded or inferred only when justified and should not manufacture date precision.

## Calendar interaction

Confirmed calendar facts are recorded in the explicitly provisional [calendar.yaml](../config/calendar.yaml). Exact dates use fictional calendar components. Approximate real-world analogy must never be converted automatically into a fictional date.

Unresolved astronomical, naming, alignment, and intercalation questions are listed in [open questions](open-questions.md). Until settled, retain source wording rather than calculating unsupported dates, weekdays, seasons, or lunar phases.
