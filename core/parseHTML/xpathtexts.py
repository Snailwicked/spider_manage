# -*- coding: utf-8 -*-
import requests,re
from lxml import etree
from urllib.parse import urljoin
from core.parseHTML.headers import random_headers

class xPathTexts(object):
    def __init__(self, *args,**kwargs):
        self.html = None

    def getHtml(self,url = None,headers= None,cookies = None):
        '''
        获取self.url 的 html
        :return: html
        '''
        if headers== None:
            headers = random_headers
        try:
            resp = requests.get(url=url, headers=headers, cookies=cookies, timeout=30)
            reg = '<meta .*(http-equiv="?Content-Type"?.*)?charset="?([a-zA-Z0-9_-]+)"?'
            charset = re.findall(reg, resp.text)[0][1]
            charset = charset.lower()
            resp.encoding = charset
            return resp.text
        except Exception as e:
            print(e)

    def get_contents(self,html=None,url= None,headers=None,X_path= None,cookies = None):
        if html != None:
            self.html = html
        else:
            self.html = self.getHtml(url,headers,cookies)

        contens = []
        print(X_path)
        for item in etree.HTML(str(self.html)).xpath(X_path):
            contens.append(str(item).strip())
        return contens


class xpathUrl(xPathTexts):
    def __init__(self):
        super(xpathUrl, self).__init__()
        self.urls = None

    def getUrls(self,url =None,html = None,headers=None):
        X_path = "//a//@href"
        data = set()
        if html!= None:
            self.urls = self.get_contents(X_path=X_path, html=html, headers=headers)
        else:
            self.urls = self.get_contents(url=url, X_path=X_path, headers=headers)

        for item in self.urls:
            url = urljoin(url, item)
            if "http" in url:
                if url not in data:
                    yield url
                    data.add(url)
                else:
                    continue

if __name__ == "__main__":
    url = "http://world.people.com.cn/n1/2019/0716/c1002-31235646.html"
    xpt = xpathUrl()
    xpt.get_contents()
    hrefs = xpt.getUrls(url=url)
    # import requests
    for href in hrefs:
        print(href)