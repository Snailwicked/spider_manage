import aiohttp
import asyncio
import chardet
from ascio.aspider.utils import get_logger
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

    def __init__(self, url, *,
                 method: str = 'GET',
                 request_config: dict = None,
                 request_session=None,
                 callback=None,
                 extra_value: dict = None,
                 res_type: str = 'text',
                 **kwargs):

        self.url = url
        self.method = method.upper()
        if self.method not in self.METHOD:
            raise ValueError('%s method is not supported' % self.method)
        if request_config is None:
            self.request_config = self.REQUEST_CONFIG
        else:
            self.request_config = request_config
        self.request_session = request_session
        self.callback = callback
        self.extra_value = extra_value if extra_value is not None else {}
        self.res_type = res_type
        self.close_request_session = False
        self.kwargs = kwargs
        self.logger = get_logger(name=self.name)

    @property
    def current_request_func(self):
        self.logger.info(f"<{self.method}: {self.url}>")
        if self.method == 'GET':
            request_func = self.current_request_session.get(self.url, **self.kwargs)
        else:
            request_func = self.current_request_session.post(self.url, **self.kwargs)
        return request_func


    @property
    def current_request_session(self):
        if self.request_session is None:
            self.request_session = aiohttp.ClientSession()
            self.close_request_session = True
        return self.request_session



    async def fetch(self):
        if self.request_config.get('DELAY', 0) > 0:
            await asyncio.sleep(self.request_config['DELAY'])

        async with self.current_request_func as resp:
            if resp.status in [200, 201]:
                if self.res_type == 'bytes':
                    data = await resp.read()
                elif self.res_type == 'json':
                    data = await resp.json()
                else:
                    content = await resp.read()
                    charset = chardet.detect(content)
                    data = content.decode(charset['encoding'])
            else:
                self.logger.error(f"<Error: {self.url} {resp.status}>")
                data = None

        if self.close_request_session:
            await self.request_session.close()

        return type('Response', (),
                    {'html': data, 'url': self.url, 'extra_value': self.extra_value})

    def __str__(self):
        return "<%s %s>" % (self.method, self.url)
if __name__ == '__main__':
    requests = Request()
    import asyncio
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(requests.hi())
    finally:
        loop.close()
