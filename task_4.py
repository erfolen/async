# Написать асинхронный код, который делает 50 get запросов к https://example.com/ . Записать все статусы ответов
# в файл и убедиться, что количество запросов соответствует заданному количеству. Необходимо учесть,
# чтобы одновременно выполнялось не больше 10 запросов. Для выполнения запросов использовать библиотеку aiohttp.
# Все значения, количество запросов, лимит одновременно выполняемых запросов и url должны передаваться как параметры.

import asyncio
import aiohttp
import aiofiles
from asyncio import Semaphore

n = 50
sem = 10
url = 'https://example.com/'


def read_file():
    with open('file_task_4.txt', 'r') as file:
        return sum(1 for line in file)


async def async_write_file(text):
    async with aiofiles.open('file_task_4.txt', 'a+') as file:
        await file.write(f'{text}\n')


async def fetch(url, sem):
    async with sem:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                await async_write_file(f'{url} : {response.status}')


async def main(n, sem, url):
    semaphore = Semaphore(sem)
    await asyncio.gather(*[fetch(url, semaphore) for _ in range(1, n + 1)])

if __name__ == '__main__':
    asyncio.run(main(n, sem, url))
    print(f'Количество строк соотвествует кол-во запросов' if read_file() == n else 'Ошибка')

