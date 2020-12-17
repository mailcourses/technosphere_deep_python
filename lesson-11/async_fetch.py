import asyncio
import aiohttp
import time


URL = 'https://loremflickr.com/320/240'


async def fetch(url, session):
    async with session.get(url, allow_redirects=True) as resp:
        data = await resp.read()
        with open(f'photo_{time.time()}', 'wb') as f:
            f.write(data)


async def main():
    tasks = []
    async with aiohttp.ClientSession() as session:
        for _ in range(10):
            tasks.append(asyncio.create_task(fetch(URL, session)))

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(main())
    t2 = time.time()
    print('T', t2 - t1)