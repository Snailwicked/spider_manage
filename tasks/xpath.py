# coding:utf-8

from logger import log
from utils.base_utils import xpathtexts
from tasks.workers import app
from db import xpath_info

@app.task(ignore_result=True)
def spider_task(main_url, xpath):
    xpathtexts.get_content(main_url, xpath)


@app.task(ignore_result=True)
def excute_xpath_task():
    infos = xpath_info.get_xpath_info()
    log.crawler.info('The xpath task is starting...')
    for info in infos:
        print(info.main_url)
        app.send_task('tasks.xpath.spider_task', args=(info.main_url, info.xpath), queue='xpath_queue',
                      routing_key='for_xpath')
