import asyncio
import time

async def request(url):
    print('正在下载：', url)
    # time.sleep(2)
    await asyncio.sleep(2)
    print("下载完毕,", url)

urls = [
    'www.baidu.com',
    'www.sogou.com',
    'www.goubanjia.com'
]
start = time.time()
tasks = []

for url in urls:
    c = request(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
print(time.time() - start)