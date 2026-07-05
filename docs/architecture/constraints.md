# Architectural constraints

- The integration depends on availability and schema stability of the public API.
- Polling must remain within reasonable intervals.
- Home Assistant async I/O requirements prohibit blocking runtime operations.
- Station-specific missing measurements must not break the integration.
