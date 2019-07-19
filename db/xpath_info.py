# -*-coding:utf-8 -*-
from sqlalchemy import text
from db.basic_db import db_session
from db.models import XpathInfo


def get_login_info():
    return db_session.query(XpathInfo.main_url, XpathInfo.xpath, XpathInfo.enable).\
        filter(text('enable=1')).all()

if __name__ == '__main__':
    # xpt = XpathInfo()
    # xpt.main_url = "http://world.people.com.cn/n1/2019/0716/c1002-31235646.html"
    # xpt.xpath = "//a//@href"
    # db_session.add(xpt)
    # db_session.commit()
    print(get_login_info())