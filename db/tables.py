# -*-coding:utf-8 -*-
from sqlalchemy import Table, Column, INTEGER, String
from db.basic_db import metadata



# xpath table
xpath_info = Table("xpath_info", metadata,
                   Column("id", INTEGER, primary_key=True, autoincrement=True),
                   Column("domain",  String(100) ,default='', server_default=''),
                   Column("author", String(100), default='', server_default=''),
                   Column("page", INTEGER, default=10, server_default='10'),
                   Column("good_list",  String(100) ,default='', server_default=''),
                   Column("personnel_imgs", String(100), default='', server_default=''),
                   Column("personnel_age", String(100), default='', server_default=''),
                   Column("personnel_name", String(100), default='', server_default=''),
                   Column("comment", String(100), default='', server_default=''),
                   Column("personnel_height", String(100), default='', server_default=''),
                   Column("attendance_time", String(100), default='', server_default=''),
                   Column("personnel_sanwei", String(100), default='', server_default=''),
            )


task_info = Table("task_info", metadata,
                   Column("id", INTEGER, primary_key=True, autoincrement=True),
                   Column("domain",  String(100) ,default='', server_default=''),
                   Column("author", String(100), default='', server_default=''),
                   Column("page", INTEGER, default=10, server_default='10'),
                   Column("good_list",  String(100) ,default='', server_default=''),
                   Column("personnel_imgs", String(100), default='', server_default=''),
                   Column("personnel_age", String(100), default='', server_default=''),
                   Column("personnel_name", String(100), default='', server_default=''),
                   Column("comment", String(100), default='', server_default=''),
                   Column("personnel_height", String(100), default='', server_default=''),
                   Column("attendance_time", String(100), default='', server_default=''),
                   Column("personnel_sanwei", String(100), default='', server_default=''),
            )


# {
#     "author":"自己的名字，用于标识此网站是谁做的,以便后期结算",
#     "domain":"需要采集的网站地址,此地址只需要改变参数便可做到分页效果",
#     "page":"采集的总页数(整数型)",
#     "good_list":"数据列表xpath路径",
#     "personnel_imgs":"图片链接的xpath路径",
#     "personnel_name":"人员名称的xpath路径",
#     "personnel_age":"人员年龄的xpath路径",
#     "personnel_height":"人员身高的xpath路径",
#     "personnel_sanwei":"人员三围的xpath路径 ",
#     "attendance_time":"出勤时间的xpath路径",
#     "comment":"评论的xpath路径"
# }
__all__ = ['xpath_info','task_info']
