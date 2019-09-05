# spider: 爬虫管理系统

## 临时通知
        项目因缺少前端工作人员，在js功能研发上存在严重滞后，现发起征贤启示，希望有志者参与指导开发，万分感谢。
    
## 项目介绍

        爬虫管理系统旨在数据采集的基础之上建立一套网页管理模式，通过输入xpath路径、正则等定位目标数据，进而进行数据采集及
    
    导出工作。本项目完全开源，代码参考github中其他对外开放项目，如有侵权，请联系开发团队，同时也欢迎大家参与本项目的开发及
    
    维护工作。
    
    qq群：796732027


## celery

        在运行项目之前，需启动任务队列，目前只有一个xpath解析a标签的任务，启动代码如下：
        celery -A tasks.workers.app worker -l info -P eventlet
        
## 项目展示
网站列表
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
