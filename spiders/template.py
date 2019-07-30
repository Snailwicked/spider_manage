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
xpath = xPathTexts()
webdata = WebData()
class spider_test():

    def set_parameter(self,parameter):
        self.parameter = parameter

    #获取所有分页链接
    def get_urls(self):
        for url in range(1,int(self.parameter.get("page"))):
            tem_url = self.parameter.get("domain").format(url)
            print("正在采集第{}页".format(url),tem_url)
            xpath.set_parameter(url= tem_url)
            print(xpath.getHtml())
            # for item in xpath.get_contents(self.parameter.get("good_list")):
            #     yield item

    def get_data(self):
        for url in self.get_urls():
            xpath.set_parameter(url=url)
            print(url)




if __name__ == '__main__':
    parameter ={
                        "author":"snail",
                        "domain":"http://fund.eastmoney.com/data/FundDataPortfolio_Interface.aspx?dt=1&t=2019_2&hydm=C&pi={}&pn=50&mc=returnJson&st=desc&sc=SZ",
                        "page":10,
                        "good_list":"//p[@class= 't']//a//@href",
                        "personnel_imgs":"//h1//text()",
                        "personnel_name":"//h1//text()",
                        "personnel_age":"//h1//text()",
                        "personnel_height":"//h1//text()",
                        "personnel_sanwei":"//h1//text() ",
                        "attendance_time":"//h1//text()",
                        "comment":"///h1//text()"
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