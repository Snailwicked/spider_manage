# coding:utf-8
import os
from datetime import timedelta

from celery import Celery, platforms
from kombu import Exchange, Queue

from config.conf import get_broker_and_backend
# allow celery worker started by root
platforms.C_FORCE_ROOT = True

worker_log_path = os.path.join(os.path.dirname(os.path.dirname(__file__)) + './logs', 'celery.log')
beat_log_path = os.path.join(os.path.dirname(os.path.dirname(__file__)) + './logs', 'beat.log')
broker, backend = get_broker_and_backend()

tasks = ['tasks.xpath']

app = Celery('spider_task', include=tasks, broker=broker, backend=backend)

app.conf.update(
    CELERY_TIMEZONE='Asia/Shanghai',
    CELERY_ENABLE_UTC=True,
    CELERYD_LOG_FILE=worker_log_path,
    CELERYBEAT_LOG_FILE=beat_log_path,
    CELERY_ACCEPT_CONTENT=['json'],
    CELERY_TASK_SERIALIZER='json',
    CELERY_RESULT_SERIALIZER='json',
    CELERYBEAT_SCHEDULE={
        'xpath_task': {
            'task': 'tasks.xpath.excute_xpath_task',
            'schedule': timedelta(hours=1),
            'options': {'queue': 'xpath_queue', 'routing_key': 'for_xpath'}
        },
    },
    CELERY_QUEUES=(
        Queue('xpath_queue', exchange=Exchange('xpath_queue', type='direct'), routing_key='for_xpath')
    ),

)
