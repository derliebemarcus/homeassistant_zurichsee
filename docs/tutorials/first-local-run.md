# First local run

## Goal

Create a verified local or test execution of Zürichsee Wetterstationen Home Assistant Integration.

## Prerequisites

- A checkout of `homeassistant_zurichsee`
- Tooling compatible with Python, Home Assistant, tecdottir HTTP API, HACS
- No production secrets in the repository working tree

## Procedure

1. Install through HACS as a custom Integration repository and restart Home Assistant.
2. For a manual installation, copy `custom_components/zurichsee_ha` into the Home Assistant `custom_components` directory.
3. Add the integration and select stations and the update interval.

## Verification

```bash
python3 -m pytest tests/unit tests/ha
ruff check .
ruff format --check .
mypy .
```
