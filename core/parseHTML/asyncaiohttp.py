import asyncio
import re
import urllib.parse
from urllib.parse import urljoin

import aiohttp
import queue
from core.parseHTML.headers import random_headers
from lxml import etree

class QueueUtil:
    def __init__(self):
        self.queue = queue.Queue()

    def put(self, data):
        self.queue.put(data)

    def get(self):
        while not self.queue.empty():
            if self.queue.qsize() < 10:
                import time
                time.sleep(5)
            yield self.queue.get()

class Crawler:
    def __init__(self, maxtasks=100):
        self.rooturl = None
        self.loop = None
        self.todo = set()
        self.busy = set()
        self.done = {}
        self.tasks = set()
        self.sem = asyncio.Semaphore(maxtasks, loop=self.loop)
        self.session = aiohttp.ClientSession(loop=self.loop)
        self.dataset = set()
        self.re_Rule = None


    @asyncio.coroutine
    def run(self):
        for url in self.rooturl:
            t = asyncio.ensure_future(self.addurls([(url, '')]),
                                  loop=self.loop)
        tas = []
        tas.append(t)
        yield from asyncio.sleep(1, loop=self.loop)
        while self.busy:
            yield from asyncio.sleep(1, loop=self.loop)
        yield from self.session.close()
        yield from tas
        self.loop.stop()

    @asyncio.coroutine
    def checkdata(self):


        pause = 1
        # while pause:
        #     import time
        #     time.sleep(5)
        #     end = len(self.dataset)
        #     temp_bit  = start/end
        #     print("----"*20,temp_bit)
        #     if 1- temp_bit<0.001:
        #         self.loop.stop()
        #         pause = 0
        #     else:
        #         start = end


    @asyncio.coroutine
    def addurls(self, urls):
        for url, parenturl in urls:
            url = urllib.parse.urljoin(parenturl, url)
            url, frag = urllib.parse.urldefrag(url)
            if (url not in self.busy and
                    url not in self.done and
                    url not in self.todo):
                self.todo.add(url)
                yield from self.sem.acquire()
                task = asyncio.ensure_future(self.process(url), loop=self.loop)
                task.add_done_callback(lambda t: self.sem.release())
                task.add_done_callback(self.tasks.remove)
                self.tasks.add(task)

    @asyncio.coroutine
    def response(self, item):
        pass

    @asyncio.coroutine
    def process(self, url):

        self.todo.remove(url)
        self.busy.add(url)
        try:
            import time
            import random
            pause_time = random.randint(1, 3)
            asyncio.sleep(pause_time)
            resp = yield from self.session.get(url,headers=random_headers)
        except:
            asyncio.ensure_future(self.addurls([(url, url)]), loop=self.loop)
            self.done[url] = False
        else:
            if (resp.status == 200):
                html = (yield from resp.read())
                data = html.decode('utf-8', 'replace')
                # urls = re.findall(r'(?i)href=["\']?([^\s"\'<>]+)', data)
                # asyncio.Task(self.addurls([(u, url) for u in urls]))
                for item in etree.HTML(str(data)).xpath("//a//@href"):
                    suburl = urljoin(url, item)
                    if suburl.startswith("http"):
                        if suburl not in self.dataset:
                            self.dataset.add(suburl)
                            asyncio.ensure_future(self.addurls([(suburl, url)]),loop=self.loop)
                        else:
                            continue
                result = re.findall(self.re_Rule, url)
                if result:
                    asyncio.ensure_future(self.response((url)), loop=self.loop)
                else:
                    pass
            resp.close()
            self.done[url] = True
        self.busy.remove(url)
        print(len(self.done), 'completed tasks,', len(self.tasks),
              'still pending, todo', len(self.todo))


class Crawleruning(Crawler):

    def __init__(self):
        super(Crawleruning, self).__init__()

    @asyncio.coroutine
    def response(self, item):
        print(item)


    def main(self,loop):
        self.rooturl = ['http://news.sohu.com/']
        self.re_Rule = "http://www.sohu.com/a/\d+_\d+"
        self.loop = loop
        tasks = asyncio.gather(  # gather() 可以将一些 future 和协程封装成一个 future
                asyncio.ensure_future(self.run(), loop=loop),
            )
        return tasks


    def start(self):
        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(self.main(loop))
        except:
            loop.close()


if __name__ == '__main__':
    import time
    start = time.time()
    crawler = Crawleruning()
    crawler.start()
    # data = "http://www.sohu.com/a/327299148_359980?scm=1002.590044.0.28b5-4ab"
    # re_Rule = "http://www.sohu.com/a/\d+_\d+"
    #
    # urls = re.findall(re_Rule, data)
    # print(urls)







