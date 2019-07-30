
# -*-coding:utf-8 -*-
from sqlalchemy import text
from db.basic_db import db_session
from db.models import TaskInfo
from decorators.decorator import db_commit_decorator



def get_task_info():
    return [item.json() for item in db_session.query(TaskInfo).all()]