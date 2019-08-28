
# -*-coding:utf-8 -*-
from db.basic_db import db_session
from db.models import TaskInfo


def get_task_info():
    return [item.json() for item in db_session.query(TaskInfo).all()]