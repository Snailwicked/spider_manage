# -*- coding=utf-8 -*-

'''
创建所需要的数据库
'''
from db.tables import *
from db.basic_db import metadata
def create_all_table():
    metadata.create_all()

if __name__ == "__main__":
    create_all_table()