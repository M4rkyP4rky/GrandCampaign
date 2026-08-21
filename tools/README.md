# Internal tools boundary

No tools are implemented during bootstrap.

Small utilities that validate or transform the internal GrandCampaign data model may eventually live here, such as:

- a metadata validator;
- a broken-link checker;
- a timeline generator;
- an orphan-asset checker.

External service-specific collectors and importers should normally be separate projects or repositories. For example, a Discord exporter should produce raw, portable input files for this repository rather than making GrandCampaign depend on the Discord API.
