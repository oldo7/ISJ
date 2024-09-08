async def get_urls(urlList):
    import asyncio
    import aiohttp

    async def download_url(url, list):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(str(url)) as response:
                    list.append((response.status,url))
            except aiohttp.ClientConnectionError as e:
                list.append(('aiohttp.ClientConnectorError',url))

    listA = []
    tlist = []
    for url in urlList:
        task1 = asyncio.create_task(download_url(url, listA))
        tlist.append(task1)

    for task in tlist:
        await task
        
    return listA
        
'''
import asyncio

if __name__ == '__main__':

    urls = ['https://www.fit.vutbr.cz', 'https://www.szn.cz', 'https://office.com']

    # for MS Windows

    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    res = asyncio.run(get_urls(urls))

    print(res)

'''
