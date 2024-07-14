# Реализуйте асинхронный метод, который будет отправлять запросы в http://google.com по http
# с ограничением не более 10 запросов в единицу времени.
import asyncio
import aiohttp

url = 'http://google.com'


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main(n):
    await asyncio.gather(*[fetch(url) for _ in range(1, n + 1)])


if __name__ == '__main__':
    asyncio.run(main(10))
