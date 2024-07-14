# Напишите скрипт который создаст параллельно 10 файлов с именем `file_ {index} .txt' и записывает их номер внутрь
# файла.

import asyncio
import asyncfile


async def create_file(n):
    """Создание n файлов и запись в них индекс"""
    custom_loop = asyncio.get_event_loop()
    async with asyncfile.open(f'file_{n}', 'w', loop=custom_loop) as f:
        await f.write(str(n))


async def main(n):
    await asyncio.gather(*[create_file(n) for n in range(1, n+1)])


if __name__ == '__main__':
    asyncio.run(main(10))
