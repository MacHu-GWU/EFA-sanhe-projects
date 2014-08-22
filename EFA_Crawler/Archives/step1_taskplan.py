##coding=utf8

from tools.crawler import Crawler, QueryString, SparseInterval, ToDo, Finished
from tools._ref_data import lastnamelist
from datetime import datetime
import pprint
import re
import os, shutil
import itertools

def querystring_generator():
    '''Generate querystring by using the following field
    lastname, country, state, recordtype,
    year, activityID, pagesize, pagenumber
    '''
    import random
    activityIDlist = ['3a65528f-fbd4-4161-9217-957cc8c51187',
                      'e8bbfb30-c4ed-468c-8cf7-a16dd403b22b']
    qs = QueryString()
    country, state, recordtype, pagesize, pagenumber = 'US', '', '2', '10', '1' # deathrecord
    for lastname in lastnamelist:
        for year in [str(i) for i in range(2011, 2014)][::-1]: # 从2013 - 1900 逆序输出
            activityID = random.choice(activityIDlist)
            yield qs.string(lastname = lastname,
                            country = country,
                            state = state,
                            recordtype = recordtype,
                            year = year,
                            activityID = activityID,
                            pagesize = pagesize,
                            pagenumber = pagenumber ) , lastname, year
            
def find_amount_of_record_by_html(html):
    '''给定一个搜索结果的页面，找到该搜索串返回的结果的总数
    http://www.archives.com/member/Default.aspx?_act=VitalSearchResult&LastName=Smith&Country=US&State=AK&RecordType=2&DeathYear=2013&activityID=3a65528f-fbd4-4161-9217-957cc8c51187&ShowSummaryLink=1&pagesize=10&pageNumber=1&pagesizeAP=10&pageNumberAP=1'
    '''
    try:
        s = re.findall(r'(?<=>Showing 1-10 of ).{1,10}(?=</span>)', html)[0]
        s = s.replace(',', '')
        return int(s)
    except: # 通常是http.request失败，返回的html = None，导致了正则失败
        return -1

def backup():
    '''备份todo.p
    '''
    shutil.copy(r'taskplan\todo.p', 
                r'C:\Users\Sanhe.Hu\Data_warehouse\Archives\backup\taskplan\todo_%s.p' % datetime.strftime( datetime.now(),
                                                                                                            '%Yy-%mm-%dd %Hh_%Mm_%Ss' ) )
def main():
    spider = Crawler()
    if spider._login(url = 'http://www.archives.com/member/', # 登录
                     payload = {'__uid':'sanhe.hu@theeagleforce.net','__pwd':'efa2014'}):

        task = ToDo()
        task._load(r'taskplan\todo.p') # 可用来查找r'taskplan\tp_%s.p' % datetime.strftime(datetime.now(), '%Yy-%mm-%dd %Hh_%Mm_%Ss')
        
        c = itertools.cycle(xrange(20)) #
        for queryurl, lastname, year in querystring_generator():
    
            if task[lastname][year] == -1: # 如果没有规划过(task[lastname][year] == -1)，访问queryurl
                html = spider.html(queryurl, 10)
                amount = find_amount_of_record_by_html(html)
                
                if amount == -1: # 说明 queryurl 访问失败
                    print '\tquery失败, url = %s' % queryurl
                    
                else:
                    task[lastname][year] = amount
                    task._dump(r'taskplan\todo.p', replace = True)
                    print '\t\t被更新为: %s in %s = %s' % (lastname, year, task[lastname][year])
                    
                    if c.next() == 19: # backup every time visit n url
                        backup()
                    
            else: # 已经规划过了
                print '\t已规划过: %s in %s = %s' % (lastname, year, task[lastname][year])
    
    else:
        print '登录失败！！'
        
def unit_test():
    task = ToDo()
    task._load(r'taskplan\todo.p')
    print task.data
    
if __name__ == '__main__':
    for i in range(100):
        main()
#     unit_test()


# url = 'http://www.archives.com/member/Default.aspx?_act=VitalSearchResult&LastName=Smith&Country=US&State=AK&RecordType=2&DeathYear=2013&activityID=3a65528f-fbd4-4161-9217-957cc8c51187&ShowSummaryLink=1&pagesize=10&pageNumber=1&pagesizeAP=10&pageNumberAP=1'
# html = spider.html(url, 10)
# print find_amount_of_record_by_html(html), url

print 'COMPLETE at %s' % datetime.now()