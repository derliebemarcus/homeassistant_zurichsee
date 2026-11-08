# Compatibility

- CI acceptance baseline: Home Assistant Core 2026.11.0 with `pytest-homeassistant==2026.11.0`
- Python 3.14 in CI
- tecdottir API availability
- HACS custom integration installation

Breaking compatibility changes require an explicit major release or migration note.

Security waivers in `tools/pip-audit-ignore.txt` and `osv-scanner.toml` are temporary. Each identifier must be reconciled against the fully resolved 2026.11.0 dependency graph before approval; only unfixable upstream-pinned advisories may remain, with an explicit removal trigger.
