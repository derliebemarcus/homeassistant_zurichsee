"""Fixtures for Zurichsee Wetterstationen tests."""

from collections.abc import Generator
from unittest.mock import AsyncMock, patch

import pytest


@pytest.fixture
def mock_setup_entry() -> Generator[AsyncMock]:
    """Override setup_entry."""
    with patch(
        "custom_components.zurichsee_ha.async_setup_entry", return_value=True
    ) as mock_setup_entry:
        yield mock_setup_entry


@pytest.fixture
def mock_api_client() -> Generator[AsyncMock]:
    """Mock API client."""
    with patch("custom_components.zurichsee_ha.api.ZurichseeApiClient", autospec=True) as mock_api:
        instance = mock_api.return_value
        instance.async_get_measurements.return_value = None
        yield instance
