import asyncio
import pytest
import aresponses
from unittest.mock import patch, AsyncMock

from task_3 import fetch, main


url = 'http://google.com'
semaphore = asyncio.Semaphore(10)


@pytest.fixture
def setup_semaphore():
    """Фикстура для создания семафора"""
    return asyncio.Semaphore(10)

@pytest.mark.asyncio
async def test_fetch_success(setup_semaphore):
    async with aresponses.ResponsesMockServer() as mock_server:
        mock_server.add("google.com", "/", "GET", aresponses.Response(text="Google Home", status=200))
        response = await fetch(url, setup_semaphore)
        assert "Google Home" in response


@pytest.mark.asyncio
async def test_fetch_error(setup_semaphore):
    async with aresponses.ResponsesMockServer() as mock_server:
        mock_server.add("google.com", "/", "GET", aresponses.Response(text="Not Found", status=404))
        response = await fetch(url, setup_semaphore)
        assert "Not Found" in response

@pytest.mark.asyncio
@patch("task_3.fetch", new_callable=AsyncMock)
async def test_main(mock_fetch):
    mock_fetch.return_value = "mocked response"
    await main(10)
    assert mock_fetch.call_count == 10
