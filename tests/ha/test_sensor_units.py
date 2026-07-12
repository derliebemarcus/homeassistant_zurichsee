"""Test Zurichsee sensor unit metadata."""

from homeassistant.const import UnitOfRatio

from custom_components.zurichsee_ha.sensor import SENSOR_DESCRIPTIONS


def test_humidity_uses_unit_of_ratio_percentage() -> None:
    """Test the humidity sensor uses the supported Home Assistant percentage unit."""
    humidity = next(description for description in SENSOR_DESCRIPTIONS if description.key == "humidity")

    assert humidity.native_unit_of_measurement is UnitOfRatio.PERCENTAGE
