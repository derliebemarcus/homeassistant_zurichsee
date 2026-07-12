"""Tests for Zurichsee API client."""

import json
from typing import Any
from unittest.mock import AsyncMock, MagicMock

import aiohttp
import pytest

from custom_components.zurichsee_ha.api import ZurichseeApiClient
from custom_components.zurichsee_ha.exceptions import ZurichseeApiError


def _mock_session(
    *,
    status: int = 200,
    payload: dict[str, Any] | None = None,
    exception: BaseException | None = None,
) -> MagicMock:
    """Create a mocked aiohttp session and response context manager."""
    session = MagicMock(spec=aiohttp.ClientSession)

    if exception is not None:
        session.get.side_effect = exception
        return session

    response = MagicMock()
    response.status = status
    response.json = AsyncMock(return_value=payload)

    response_context = MagicMock()
    response_context.__aenter__ = AsyncMock(return_value=response)
    response_context.__aexit__ = AsyncMock(return_value=None)
    session.get.return_value = response_context
    return session


@pytest.mark.asyncio
async def test_async_get_measurements_success() -> None:
    """Test successful data retrieval."""
    with open("tests/fixtures/mythenquai.json") as fixture:
        mock_data = json.load(fixture)

    client = ZurichseeApiClient(_mock_session(payload=mock_data))
    result = await client.async_get_measurements("mythenquai")

    assert result is not None
    assert result.air_temperature == 12.5
    assert result.water_temperature == 11.2
    assert result.wind_direction == 240


@pytest.mark.asyncio
async def test_async_get_measurements_error() -> None:
    """Test API error handling."""
    client = ZurichseeApiClient(_mock_session(status=500))

    with pytest.raises(ZurichseeApiError):
        await client.async_get_measurements("mythenquai")


@pytest.mark.asyncio
async def test_async_validate_connection() -> None:
    """Test connection validation."""
    with open("tests/fixtures/mythenquai.json") as fixture:
        mock_data = json.load(fixture)

    client = ZurichseeApiClient(_mock_session(payload=mock_data))
    await client.async_validate_connection()


@pytest.mark.asyncio
async def test_async_get_measurements_empty_result() -> None:
    """Test handling of empty results."""
    client = ZurichseeApiClient(_mock_session(payload={"result": []}))
    result = await client.async_get_measurements("mythenquai")

    assert result is None


@pytest.mark.asyncio
async def test_async_get_measurements_missing_keys() -> None:
    """Test handling of missing keys in values."""
    mock_data = {
        "result": [
            {
                "station": "mythenquai",
                "timestamp": "2026-04-29T10:00:00Z",
                "values": {"air_temperature": {"value": 15.0, "unit": "°C"}},
            }
        ]
    }
    client = ZurichseeApiClient(_mock_session(payload=mock_data))
    result = await client.async_get_measurements("mythenquai")

    assert result is not None
    assert result.air_temperature == 15.0
    assert result.water_temperature is None


@pytest.mark.asyncio
async def test_async_get_measurements_timeout() -> None:
    """Test timeout handling."""
    client = ZurichseeApiClient(_mock_session(exception=TimeoutError()))

    with pytest.raises(ZurichseeApiError, match="Timeout"):
        await client.async_get_measurements("mythenquai")


@pytest.mark.asyncio
async def test_async_get_measurements_network_error() -> None:
    """Test network error handling."""
    client = ZurichseeApiClient(_mock_session(exception=aiohttp.ClientError()))

    with pytest.raises(ZurichseeApiError, match="Network error"):
        await client.async_get_measurements("mythenquai")
