# # coding:utf-8
import os
#
from celery import Celery, platforms
from config.conf import get_broker_and_backend
platforms.C_FORCE_ROOT = True
broker, backend = get_broker_and_backend()
#
tasks = ['tasks.xpath',"tasks.gethtml"]

app = Celery('spider_task', include=tasks, broker=broker, backend=backend)

app.conf.update(
    CELERY_TIMEZONE='Asia/Shanghai',
    CELERY_ENABLE_UTC=True,
    CELERY_ACCEPT_CONTENT=['json'],
    CELERY_TASK_SERIALIZER='json',
    CELERY_RESULT_SERIALIZER='json',
    CELERY_ROUTES={
        'tasks.xpath.excute_xpath_task':
            {
                'queue': 'xpath_queue',
                'routing_key': 'xpath_queue'
            },

        'tasks.gethtml.excute_xpath_task':
            {
                'queue': 'gethtml_queue',
                'routing_key': 'gethtml_queue'
            },


    },

    CELERY_QUEUES={
        "gethtml_queue": {
            "exchange": "gethtml_queue",
            "exchange_type": "direct",
            "routing_key": "gethtml_queue"
        }
    }

)






