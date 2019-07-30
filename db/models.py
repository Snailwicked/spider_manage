# -*-coding:utf-8 -*-
from db.basic_db import Base
from db.tables import *



class XpathInfo(Base):
    __table__ = xpath_info
    def json(self):
        return {"author":self.author,"domain":self.domain,"page":self.page,"good_list":self.good_list,
                    "personnel_imgs":self.personnel_imgs,"personnel_name":self.personnel_name,"personnel_age":self.personnel_age,
                        "personnel_height":self.personnel_height,"personnel_sanwei":self.personnel_sanwei,"attendance_time":self.attendance_time,"comment":self.comment}


class TaskInfo(Base):
    __table__ = task_info
    def json(self):
        return {"author":self.author,"domain":self.domain,"page":self.page,"good_list":self.good_list,
                    "personnel_imgs":self.personnel_imgs,"personnel_name":self.personnel_name,"personnel_age":self.personnel_age,
                        "personnel_height":self.personnel_height,"personnel_sanwei":self.personnel_sanwei,"attendance_time":self.attendance_time,"comment":self.comment}
'''
{
    "author":"自己的名字，用于标识此网站是谁做的,以便后期结算",
    "domain":"需要采集的网站地址,此地址只需要改变参数便可做到分页效果",
    "page":"采集的总页数(整数型)",
    "good_list":"数据列表xpath路径",
    "personnel_imgs":"图片链接的xpath路径",
    "personnel_name":"人员名称的xpath路径",
    "personnel_age":"人员年龄的xpath路径",
    "personnel_height":"人员身高的xpath路径",
    "personnel_sanwei":"人员三围的xpath路径 ",
    "attendance_time":"出勤时间的xpath路径",
    "comment":"评论的xpath路径"
}

'''

class WebData():

    def __int__(self):
        self.url = ""
        self.personnel_imgs = []
        self.personnel_name = ""
        self.personnel_age = ""
        self.personnel_height = ""
        self.personnel_sanwei = ""
        self.attendance_time = ""
        self.comment = ""


    def get_json(self):
        return {"url":self.url,"personnel_imgs":self.personnel_imgs,"personnel_name":self.personnel_name,"personnel_age":self.personnel_age,
                    "personnel_height":self.personnel_height,"personnel_sanwei":self.personnel_sanwei,"attendance_time":self.attendance_time,"comment":self.comment}