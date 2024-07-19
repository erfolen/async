import asyncio
import os
import pytest
from aiofiles import open as async_open

from task_2_4_2 import main, wreate_file

@pytest.fixture
def clean_up_files():
    """Удаляет созданные файлы до и после тестов"""
    file_names = [f'file_{i}' for i in range(1, 11)]
    for file_name in file_names:
        if os.path.exists(file_name):
            os.remove(file_name)
    yield
    for file_name in file_names:
        if os.path.exists(file_name):
            os.remove(file_name)

@pytest.mark.asyncio
async def test_create_file(clean_up_files):
    file_name = 'file_1'

    await wreate_file(1)

    assert os.path.exists(file_name)

    async with async_open(file_name, 'r') as f:
        content = await f.read()
    assert content == '1'


@pytest.mark.asyncio
async def test_main(clean_up_files):
    num_files = 10
    file_names = [f'file_{i}' for i in range(1, num_files + 1)]

    await main(num_files)

    for i, file_name in enumerate(file_names, start=1):
        assert os.path.exists(file_name)
        async with async_open(file_name, 'r') as f:
            content = await f.read()
        assert content == str(i)
