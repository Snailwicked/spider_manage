# -*-coding:utf-8 -*-

'''
所的网站采集均以json数据进行交互
目前只是简单的静态页面数据采集，其他类型暂且跳过
遇到问题暂且备注，发到群里进行统一处理


json 数据暂且自行保存
'''


"""
json 数据格式

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
"""

from core.xpathtexts import xPathTexts
from db.models import WebData

class spider_test():

    def __int__(self,parameter):
        self.webdata = WebData()
        self.xpath = xPathTexts()

    def set_parameter(self,parameter):
        self.parameter = parameter

    #获取所有分页链接
    def get_urls(self):
        for url in range(1,int(self.parameter.get("page"))):
            self.xpath.set_parameter(url=url)
            for item in self.xpath.get_contents(self.parameter.get("good_list")):
                yield item

    def get_data(self):
        for url in self.get_urls():
            self.xpath.set_parameter(url=url)
            self.webdata.url = url
            self.webdata.personnel_name = self.xpath.get_contents(self.parameter.get("personnel_name"))
            self.webdata.personnel_age = self.xpath.get_contents(self.parameter.get("personnel_age"))
            self.webdata.personnel_height = self.xpath.get_contents(self.parameter.get("personnel_height"))
            self.webdata.personnel_sanwei = self.xpath.get_contents(self.parameter.get("personnel_sanwei"))
            self.webdata.attendance_time = self.xpath.get_contents(self.parameter.get("attendance_time"))
            self.webdata.comment = self.xpath.get_contents(self.parameter.get("comment"))
            print(self.webdata.get_json())
            return self.webdata.get_json()



if __name__ == '__main__':
    parameter ={
                        "author":"自己的名字，用于标识此网站是谁做的,以便后期结算",
                        "domain":"http://search.360kad.com/?pageText=%E5%96%B7%E9%9B%BE%E5%89%82&pageIndex={}",
                        "page":"10",
                        "good_list":"//div[@class= 'plist_li']//div//p[@class='t']//a//@herf",
                        "personnel_imgs":"图片链接的xpath路径",
                        "personnel_name":"人员名称的xpath路径",
                        "personnel_age":"人员年龄的xpath路径",
                        "personnel_height":"人员身高的xpath路径",
                        "personnel_sanwei":"人员三围的xpath路径 ",
                        "attendance_time":"出勤时间的xpath路径",
                        "comment":"评论的xpath路径"
                    }
    spider = spider_test()
    spider.set_parameter(parameter)
    spider.get_data()

    '''
    如果可以获取所需要的数据，请将参数提交到数据库
    提交方法如下，没写验证，请勿重复提交
    '''
    # from db import xpath_info
    # print(xpath_info.commit_data(parameter))