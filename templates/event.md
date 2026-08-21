---
id: <event-stable-id>
record_type: event
reference_name: <event title>
time:
  description: <human-readable interval or uncertainty>
  start:
    precision: <exact-datetime | exact-date | year | approximate-year | century | age | broad | unknown>
    year_ap: <negative before 0, zero at the epoch, positive after 0>
  end:
    precision: <precision supported for the end>
    year_ap: <negative before 0, zero at the epoch, positive after 0>
  sources:
    - <relative link supporting this time block>
locations:
  - location: <relative link to relevant location>
    sources:
      - <relative link supporting this relationship>
entities:
  - entity: <relative link to relevant entity>
    sources:
      - <relative link supporting this relationship>
accounts:
  - kind: <campaign-account | legend | gm-reconstruction>
    source: <relative link to source or account>
    summary: <what this perspective reports>
---

# <event title>

## Description

<Description that preserves disagreement and does not promote one account to objective truth.>

Sources:

- [<source label>](<relative path>) — <what this source supports in this section>
