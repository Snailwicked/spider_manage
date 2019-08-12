import aiohttp


class Request():
    """
    Request class for each request
    """
    name = 'Request'
    # Default config
    REQUEST_CONFIG = {
        'RETRIES': 3,
        'DELAY': 0,
        'TIMEOUT': 10
    }

    METHOD = ['GET', 'POST']

    def __init__(self):
        pass

    async def hi(self):
        async with aiohttp.ClientSession() as session:
            async with session.get('http://httpbin.org/get') as resp:
                print(resp.status)
                print(await resp.text())


if __name__ == '__main__':
    requests = Request()
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(requests.hi())
    finally:
        loop.close()
