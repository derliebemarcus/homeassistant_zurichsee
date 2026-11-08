"""Assert that the supported Home Assistant CI baseline is installed."""

from importlib.metadata import version


def test_home_assistant_2026_11_baseline() -> None:
    """Prevent an accidental regression to an older HA or fixture release."""
    assert version("homeassistant") == "2026.11.0"
    assert version("pytest-homeassistant") == "2026.11.0"
