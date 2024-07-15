# Реализуйте асинхронный метод, который будет отправлять запросы в http://google.com по http
# с ограничением не более 10 запросов в единицу времени.
import asyncio
from asyncio import Semaphore
import aiohttp

url = 'http://google.com'
semaphore = Semaphore(10)  # Ограничение на 10 запросов одновременно


async def fetch(url, sem):
    async with sem:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                print(response.status)
                return await response.text()


async def main(n):
    await asyncio.gather(*[fetch(url, semaphore) for _ in range(1, n + 1)])


if __name__ == '__main__':
    asyncio.run(main(10))
