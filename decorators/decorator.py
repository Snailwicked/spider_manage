# -*-coding:utf-8 -*-
from functools import wraps
from traceback import format_tb
from db.basic_db import db_session


# timeout decorator
def timeout_decorator(func):
    @wraps(func)
    def time_limit(*args, **kargs):
        try:
            return func(*args, **kargs)
        except Exception as e:
            return ''

    return time_limit


def db_commit_decorator(func):
    @wraps(func)
    def session_commit(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print("入库失败")
            db_session.rollback()
    return session_commit


