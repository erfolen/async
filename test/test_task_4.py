import os
import asyncio
import pytest
import aiofiles
import aresponses
import aiohttp
from task_4 import async_write_file, fetch, main

url = 'https://example.com/'
n = 50
sem = 10
file_path = 'file_task_4.txt'


@pytest.fixture(autouse=True)
def clean_up_file():
    """Удаляет созданный файл до и после тестов"""
    if os.path.exists(file_path):
        os.remove(file_path)
    yield
    if os.path.exists(file_path):
        os.remove(file_path)


@pytest.mark.asyncio
async def test_async_write_file():
    text = "test text"
    await async_write_file(text)

    async with aiofiles.open(file_path, 'r') as file:
        content = await file.read()

    assert text in content


@pytest.mark.asyncio
async def test_fetch():
    async with aresponses.ResponsesMockServer() as mock_server:
        mock_server.add("example.com", "/", "GET", aresponses.Response(text="Example Domain", status=200))

        semaphore = asyncio.Semaphore(sem)
        await fetch(url, semaphore)

    async with aiofiles.open(file_path, 'r') as file:
        content = await file.read()

    assert f'{url} : 200' in content


@pytest.mark.asyncio
async def test_main():
    async with aresponses.ResponsesMockServer() as mock_server:
        mock_server.add("example.com", "/", "GET", aresponses.Response(text="Example Domain", status=200))

        await main(n, sem, url)

    async with aiofiles.open(file_path, 'r') as file:
        lines = await file.readlines()

    assert len(lines) == n
