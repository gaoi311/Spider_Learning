import aiohttp
import asyncio
urls = [
    'http://www.baidu.com',
    'http://www.sogou.com',
    'http://www.taobao.com',
]

async def get_page(url):
    async with aiohttp.ClientSession() as session:
        async with await session.get(url) as response:
            page_text = await response.text()
            print(page_text)

tasks = []

for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
