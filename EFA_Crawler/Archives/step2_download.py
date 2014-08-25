##coding=utf8
from tools.crawler import Crawler, QueryString, SparseInterval, ToDo, Finished
from tools._ref_data import lastnamelist
from datetime import datetime
import pprint
import re
import os, shutil
import math

def unit_test():
    task = ToDo()
    task._load(r'taskplan\todo.p')
    for k, v in task.data['Smith'].iteritems():
        print k, v
        
task = ToDo()
task._load(r'taskplan\todo.p')
# for k, v in task.data['Smith'].iteritems():
#     print k, v

#     lastname, country, state, recordtype,
#     year, activityID, pagesize, pagenumber

def unit_task_generator(task, size = 100):
    import random
    activityIDlist = ['3a65528f-fbd4-4161-9217-957cc8c51187',
                      'e8bbfb30-c4ed-468c-8cf7-a16dd403b22b']
    qs = QueryString()
    for lastname in lastnamelist:
        plan = task.data.get(lastname, {})
        for year, amount in plan.iteritems():
            for i in range( int(math.floor(float(amount)/size)) ):
                lower, upper, pagesize, pagenumber = 1 + i * size, (i+1)* size, size, i+1
                queryurl = qs.string(lastname = lastname,
                                     country = 'US',
                                     state = '',
                                     recordtype = '2',
                                     year = year,
                                     activityID = random.choice(activityIDlist),
                                     pagesize = pagesize,
                                     pagenumber = pagenumber )
                yield lastname, year, lower, upper, pagesize, pagenumber, queryurl

spider = Crawler()
spider._login(url = 'http://www.archives.com/member/', # 登录
              payload = {'__uid':'sanhe.hu@theeagleforce.net','__pwd':'efa2014'})

       
for lastname, year, lower, upper, pagesize, pagenumber, queryurl in unit_task_generator(task):
    html = spider.html(url, 10) ##
    