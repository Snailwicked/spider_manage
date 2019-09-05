# spider: 爬虫管理系统

    
## 项目介绍

        爬虫管理系统是一套对服务器资源进行合理分配的分布式数据采集WEB系统,其中包含网页管理、爬虫管理、数据监控等模块，各
    
    模块间相互关联，组建一个多服务器相互协作的系统，让你仅通过简单的配置信息就能够搭建一个属于自己的数据采集系统。
        
       
## celery

        在运行项目之前，需启动任务队列，启动代码如下：
        celery -A tasks.workers.app worker -l info -P eventlet
        
## 项目展示
### 网站列表
        在网址列表中你可以添加一个需要采集的的目标网站，系统会为你自动生成一系列的默认配置信息，在新闻数据采集中，内部包含一套算法采集，
    让你不需要配置任何信息便可获取目标新闻数据，但采集精度有限，如果需要精确数据可在采集字段中设置xpath路径，css路径或正则表达式。
    
        在配置信息你可以设置此网站要采集的深度（默认深度为1，默认采集当前网址数据），也可以根据网址的正则进行过滤网址，获取目标网址。
        
        在设置了配置信息之后，你可以点击监测按钮，查看配置信息是否生效，系统会默认先读取输入的选择器信息
![Image text](https://raw.githubusercontent.com/Snailwicked/spider_manage/master/images/weblist.png)

配置信息
![Image text](https://raw.githubusercontent.com/Snailwicked/spider_manage/master/images/config.png)


数据采集引擎
![Image text](https://raw.githubusercontent.com/Snailwicked/spider_manage/master/images/spider_engine.png)


网站导入数据采集引擎
![Image text](https://raw.githubusercontent.com/Snailwicked/spider_manage/master/images/import.png)

系统监控图
![Image text](https://raw.githubusercontent.com/Snailwicked/spider_manage/master/images/monitor.png)


数据展示列表
![Image text](https://raw.githubusercontent.com/Snailwicked/spider_manage/master/images/newslist.png)

详情数据图
![Image text](https://raw.githubusercontent.com/Snailwicked/spider_manage/master/images/detailed.png)
## 相关技术

- flask
- mysql
- redis
- celey
