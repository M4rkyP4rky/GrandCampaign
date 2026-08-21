# Geography model

## Physical foundation

Stable physical geography is the primary location hierarchy. A conceptual chain may be:

```text
world
→ continent
→ subcontinent or macroregion
→ region
→ smaller physical region
→ settlement or other location
```

Levels may be skipped. A location has at most the supported `physical_parent` relationship; do not invent missing levels. Spatial relationships can remain prose unless later evidence justifies a small structured vocabulary.

Do not store geographic coordinates and do not introduce a coordinate system.

## Political geography

Kingdoms, empires, republics, duchies, and similar political bodies are separate polity entities, not physical parents. Their existence, jurisdiction, claims, and control may change over time. Represent a location's political relationship in a dated or uncertain snapshot or supported event, not as timeless geography.

## Names and identity

A changed, translated, or historical place name does not by itself create a new location. Keep the stable location ID and record supported names with language, cultural context, and temporal validity when known. Preserve uncertainty when sources do not establish whether two names refer to one place.

## Location snapshots

There is no universal current state for a historical location. A record under [`snapshots/locations/`](../snapshots/locations/) describes a particular location at a particular exact or uncertain time. It has:

- its own stable snapshot ID;
- a link to the target location identity;
- a time description with only supported precision;
- a state description;
- provenance for that description.

Snapshots may link time-bounded political relationships, inhabitants, condition, usage, or other supported state. They do not replace the location identity record, and no snapshots are created during bootstrap.
