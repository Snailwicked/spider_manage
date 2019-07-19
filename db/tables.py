# -*-coding:utf-8 -*-
from sqlalchemy import Table, Column, INTEGER, String
from db.basic_db import metadata



# xpath table
xpath_info = Table("xpath_info", metadata,
                   Column("id", INTEGER, primary_key=True, autoincrement=True),
                   Column("main_url", String(100), unique=True),
                   Column("xpath", String(200)),
                   Column("enable", INTEGER, default=1, server_default='1'),
                   )


__all__ = ['xpath_info']
