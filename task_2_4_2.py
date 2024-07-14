# Напишите скрипт который создаст параллельно 10 файлов с именем `file_ {index} .txt' и записывает их номер внутрь
# файла.

import asyncio
import aiofiles


async def wreate_file(n):
    """Создание n файлов и запись в них индекс"""
    async with aiofiles.open(f'file_{n}', 'w') as file:
        await file.write(str(n))


async def main(n):
    await asyncio.gather(*[wreate_file(n) for n in range(1, n+1)])


if __name__ == '__main__':
    asyncio.run(main(10))
