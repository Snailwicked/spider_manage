import asyncio
import re
import urllib.parse
from urllib.parse import urljoin

import aiohttp
import queue
from core.headers import random_headers
from lxml import etree


class Crawler():

    def __init__(self, maxtasks=100):
        super(Crawler, self).__init__()
        self.parameters = None
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
        for parameter in self.parameters:
            t = asyncio.ensure_future(self.parse_urls(parameter),
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
    def addurls(self,parameter, temp):
        for url in temp:
            if (url not in self.busy and
                    url not in self.done and
                    url not in self.todo):
                self.todo.add(url)
                yield from self.sem.acquire()
                task = asyncio.ensure_future(self.process(url,parameter), loop=self.loop)
                task.add_done_callback(lambda t: self.sem.release())
                task.add_done_callback(self.tasks.remove)
                self.tasks.add(task)

    @asyncio.coroutine
    def parse_urls(self, parameter):
        temp = []
        for item in range(1, int(parameter.get("page"))):
            tem_url = parameter.get("domain").format(item)
            temp.append(("list", tem_url))
        asyncio.ensure_future(self.addurls(parameter, temp), loop=self.loop)


    @asyncio.coroutine
    def process_urls(self ,html,parameter):
        temp = []
        for item in etree.HTML(str(html)).xpath(parameter.get("good_list")):
            temp.append(("detail",item))
            asyncio.ensure_future(self.addurls(parameter, temp), loop=self.loop)

    @asyncio.coroutine
    def process_data(self, url, html, parameter):
        title = etree.HTML(str(html)).xpath(parameter.get("personnel_age"))[0]
        print(url,title)



    @asyncio.coroutine
    def process(self, url,parameter):
        self.todo.remove(url)
        self.busy.add(url)
        try:
            import time
            import random
            pause_time = random.randint(1, 3)
            asyncio.sleep(pause_time)
            resp = yield from self.session.get(url[1],headers=random_headers)
        except:
            self.done[url] = False
        else:
            if (resp.status == 200):
                html = (yield from resp.read())
                data = html.decode('utf-8', 'replace')
                if url[0] == "list":
                    asyncio.ensure_future(self.process_urls(data,parameter), loop=self.loop)
                elif url[0] == "detail":
                    asyncio.ensure_future(self.process_data(url[1],data,parameter), loop=self.loop)
            resp.close()
            self.done[url] = True
        self.busy.remove(url)


class Crawleruning(Crawler):

    def __init__(self):
        super(Crawleruning, self).__init__()

    def main(self,loop):
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

    def set_parameters(self,parameters):
        self.parameters = parameters

if __name__ == '__main__':
    import time

    parameters = [{'personnel_sanwei': '//h1//text() ', 'page': 10, 'personnel_name': '//h1//text()',
      'attendance_time': '//h1//text()', 'good_list': "//p[@class= 't']//a//@href",
      'domain': 'http://search.360kad.com/?pageText=%E9%A2%97%E7%B2%92&pageIndex={}',
      'personnel_age': '//h1//text()', 'personnel_height': '//h1//text()', 'personnel_imgs': '//h1//text()',
      'comment': '///h1//text()', 'author': 'snail'}]

    crawler = Crawleruning()
    crawler.set_parameters(parameters)
    crawler.start()

    #
    # check = check()
    # check.chekc()

# data = "http://www.sohu.com/a/327299148_359980?scm=1002.590044.0.28b5-4ab"
    # re_Rule = "http://www.sohu.com/a/\d+_\d+"
    #
    # urls = re.findall(re_Rule, data)
    # print(urls)







