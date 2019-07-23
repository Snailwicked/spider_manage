from tasks.workers import app
from core.asyncaiohttp import Crawleruning
from db import xpath_info
from db import task_info


@app.task(ignore_result=True)
def parameter_task(task_name):
    parameter =  task_info.get_xpath_info(task_name)
    crawler = Crawleruning()
    crawler.set_parameters(parameter)
    crawler.start()


@app.task(ignore_result=True)
def excute_xpath_task():
    infos = task_info.get_task_info()
    for info in infos:
        print(info.task_name)
        app.send_task('tasks.gethtml.parameter_task', args=(info.task_name), queue='task_queue',
                      routing_key='for_task')

