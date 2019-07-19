# coding:utf-8
import time

from logger import log
from core import xpathtexts
from tasks.workers import app
from db import xpath_info

@app.task(ignore_result=True)
def spider_task(main_url, xpath):
    xpathtexts.get_content(main_url,xpath)


# There should be login interval, if too many accounts login at the same time from the same ip, all the
# accounts can be banned by weibo's anti-cheating system
@app.task(ignore_result=True)
def excute_xpath_task():
    infos = xpath_info.get_xpath_info()
    # Clear all stacked login tasks before each time for login
    log.crawler.info('The login task is starting...')
    for info in infos:
        app.send_task('tasks.xpath.spider_task', args=(info.main_url, info.xpath), queue='xpath_queue',
                      routing_key='for_xpath')
        time.sleep(10)
