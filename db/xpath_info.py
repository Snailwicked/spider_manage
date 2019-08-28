# -*-coding:utf-8 -*-
from db.basic_db import db_session
from db.models import XpathInfo
from utils.decorator import db_commit_decorator


def get_xpath_info():
    return [item.json() for item in db_session.query(XpathInfo).all()]


@db_commit_decorator
def data_commit(data):
    """
    :param name: login account
    :param rs: 0 stands for banned，1 stands for normal，2 stands for name or password is invalid
    :return:
    """
    db_session.add(data)
    db_session.commit()


def commit_data(parameter):
    from db.models import XpathInfo
    xpath_data = XpathInfo()
    xpath_data.author = str(parameter.get("author"))
    xpath_data.domain = str(parameter.get("domain"))
    xpath_data.page = str(parameter.get("page"))
    xpath_data.good_list = str(parameter.get("good_list"))
    xpath_data.personnel_imgs = str(parameter.get("personnel_imgs"))
    xpath_data.personnel_name = str(parameter.get("personnel_name"))
    xpath_data.personnel_age = str(parameter.get("personnel_age"))
    xpath_data.personnel_height = str(parameter.get("personnel_height"))
    xpath_data.personnel_sanwei = str(parameter.get("personnel_sanwei"))
    xpath_data.attendance_time = str(parameter.get("attendance_time"))
    xpath_data.comment = str(parameter.get("comment"))
    data_commit(xpath_data)
    return "入库成功"



if __name__ == '__main__':
    # parameter = {
    #     "author": "自己的名字，用于标识此网站是谁做的,以便后期结算",
    #     "domain": "需要采集的网站地址,此地址只需要改变参数便可做到分页效果",
    #     "page": "1",
    #     "good_list": "数据列表xpath路径",
    #     "personnel_imgs": "图片链接的xpath路径",
    #     "personnel_name": "人员名称的xpath路径",
    #     "personnel_age": "人员年龄的xpath路径",
    #     "personnel_height": "人员身高的xpath路径",
    #     "personnel_sanwei": "人员三围的xpath路径 ",
    #     "attendance_time": "出勤时间的xpath路径",
    #     "comment": "评论的xpath路径"
    # }
    # xpath_data = XpathInfo()
    # xpath_data.author = str(parameter.get("author"))
    # xpath_data.domain = str(parameter.get("domain"))
    # xpath_data.page = str(parameter.get("page"))
    # xpath_data.good_list = str(parameter.get("good_list"))
    # xpath_data.personnel_imgs = str(parameter.get("personnel_imgs"))
    # xpath_data.personnel_name = str(parameter.get("personnel_name"))
    # xpath_data.personnel_age = str(parameter.get("personnel_age"))
    # xpath_data.personnel_height = str(parameter.get("personnel_height"))
    # xpath_data.personnel_sanwei = str(parameter.get("personnel_sanwei"))
    # xpath_data.attendance_time = str(parameter.get("attendance_time"))
    # xpath_data.comment = str(parameter.get("comment"))
    #
    #
    # # xpt = XpathInfo()
    # # xpt.author = "http://world.people.com.cn/n1/2019/0716/c1002-31235646.html"
    # # xpt.comment = "//a//@href"
    # data_commit(xpath_data)
    print(get_xpath_info())