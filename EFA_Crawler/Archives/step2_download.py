##coding=utf8
from tools.crawler import Crawler, QueryString, SparseInterval, ToDo, Finished
from tools._ref_data import lastnamelist
from tools.archiveDB import ArchiveDB
from datetime import datetime
import pprint
import re
import os, shutil
import math
import bs4
import hashlib
import itertools

def unit_task_generator(task, size = 100):
    '''iterately generate the following from task plan
        lastname, year, lower, upper, pagesize, pagenumber, queryurl
    '''
    import random
    activityIDlist = ['2cec1360-a5cb-4ce4-bd22-7a15303c4c37',
                      'e218f069-fab8-4284-ace8-eceedb304176',
                      'f689eade-604c-4cbb-ba22-7f0b9a3c5af4',
                      '68f49228-6e68-4076-b738-5bc4e8981be7']
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

def process_fullname(fullname, lastname):
    '''split lastname and firstname
    Input: fullname = Johnnie L. John II, lastname = John
    Output: firstname = Johnnie L.
    '''
    namepiece = fullname.split(lastname)
    namepiece.pop()
    firstname = lastname.join(namepiece).strip()
    return firstname
    
def process_date(datestring):
    '''change the date format from "Jan 3, 2012" to "2012-01-03"
    '''
    return datetime.strftime(datetime.strptime(datestring, '%b %d, %Y'), '%Y-%m-%d')

def process_location(location):
    '''split location and state
    '''
    locpiece = location.split(',')
    state = locpiece.pop().strip()
    return location, state
    
def records_generator(text, lastname):
    '''Given a text, iterately generate:
             #lastname, #firstname, #bod, #dod, #location, #state, #source
    '''
    for line in text.split('\n'):
        if '<div class="searchColRight">' in line: # 这一行包含了所有的数据
            line = line.strip().replace('</script></div>', '')
            soup = bs4.BeautifulSoup(line)
            
            amount = 0
            for entry in soup.findAll('div', attrs = {'class': 'resultsRow vital-record-row clearfix'}):
                amount += 1
                row = list() 
                for field in entry.findAll('div', attrs = {'class': 'fieldValue'}):
                    row.append(field.text)
                    
                try: # pre process data format
                    fullname, bod, dod, location, source, = row[0], row[1], row[2], row[3], row[4] # !! sometime it raise error.
                    firstname = process_fullname(fullname, lastname) # split lastname and firstname !! sometime it raise error.
                    bod, dod = process_date(bod), process_date(dod) # change format of date !! sometime it raise error.
                    location, state = process_location(location) # split location and state !! sometime it raise error.
                    if bod <= dod:
                        yield firstname, bod, dod, location, state, source, amount
                except:
                    pass

def backup():
    '''finished.p 和 archive.db
    '''
    shutil.copy(r'C:\Users\Sanhe.Hu\Data_warehouse\Archives\finished.p', 
                r'C:\Users\Sanhe.Hu\Data_warehouse\Archives\backup\history_and_db\finished_%s.p' % datetime.strftime( datetime.now(),
                                                                                                            '%Yy-%mm-%dd %Hh_%Mm_%Ss' ) )
    shutil.copy(r'C:\Users\Sanhe.Hu\Data_warehouse\Archives\archive.db', 
                r'C:\Users\Sanhe.Hu\Data_warehouse\Archives\backup\history_and_db\archive_%s.db' % datetime.strftime( datetime.now(),
                                                                                                            '%Yy-%mm-%dd %Hh_%Mm_%Ss' ) )
def main():
    task = ToDo() # load task
    task._load(r'C:\Users\Sanhe.Hu\Data_warehouse\Archives\todo.p')
    history = Finished() # load history
    history._load(r'C:\Users\Sanhe.Hu\Data_warehouse\Archives\finished.p')
    
    adb = ArchiveDB(r'C:\Users\Sanhe.Hu\Data_warehouse\Archives\archive.db') # 初始化
    adb._initial() # 初始化表格
    
    spider = Crawler() # create crawler
    spider._login(url = 'http://www.archives.com/member/', # 尝试登录
                  payload = {'__uid':'sanhe.hu@theeagleforce.net','__pwd':'efa2014'})
     
    backup_counter = itertools.cycle(xrange(150)) # 备份循环计数器
    progress_counter = itertools.count(0)
    for lastname, year, lower, upper, pagesize, pagenumber, queryurl in unit_task_generator(task, size = 250):
        
        history[lastname].setdefault(year, SparseInterval(0,0)) # try to initialize history[lastname][year] = SparseInterval(0, 0)
        if SparseInterval(lower, upper) not in history[lastname][year]: # 如果没有爬过
            print 'Crawling %s (%s %s %s %s) \nurl = %s' % (progress_counter.next(), lastname, year, lower, upper, queryurl)
            html = spider.html(queryurl, 30) # crawler the query result webpage
    
            if html: # if http request success
                ## generate pagesize of records from single HTML
                records = list()
                total = 0.1 # 初始化total, 因为如果records_generator一个好结果都声称不出来的话，后面total就不会被定义
                for firstname, bod, dod, location, state, source, total in records_generator(html, lastname):
                    ID = hashlib.md5(','.join((lastname, firstname, bod, dod, location, state, source)) ).hexdigest()
                    records.append( (ID, lastname, firstname, bod, dod, location, state, source) )
                    
                amount = len(records) # how many records have been inserted
                adb.insertmany('death_records', records) # insert into database
                adb.commit()
                print '\tSuccess: %s records have been inserted. %s (%s, %s)' % (amount, lastname, lower, upper)

                if (amount + 0.001)/total >= 0.8: # <=== 当有50%的条目是正确条目时,更新history
                    history[lastname][year] += SparseInterval(lower, upper)
 
                if backup_counter.next() == 149: # 定时备份
                    history._dump(r'C:\Users\Sanhe.Hu\Data_warehouse\Archives\finished.p', replace = True)
                    print '===BACKUP finished.p and archive.db...==='
                    backup()
                    print '===BACKUP FINISHED !!! ==='

            else:
                print '\tFailed!'
        
def unit_test_ToDo_and_Finished():
    task = ToDo()
    task._load(r'C:\Users\Sanhe.Hu\Data_warehouse\Archives\todo.p')
    print task['Johnson']
#     print task.data.keys()
#     task._info()

#     history = Finished()
#     history._dump(r'C:\Users\Sanhe.Hu\Data_warehouse\Archives\finished.p')
#     history._load(r'C:\Users\Sanhe.Hu\Data_warehouse\Archives\finished.p')
#     print history['Smith']['2011']
#     print history['Smith'].setdefault('2013', SparseInterval(0, 0))
    
def unit_test_archiveDB():
    import sqlite3
    from tools.sqlite3_schema import Database_schema
    db = Database_schema(r'C:\Users\Sanhe.Hu\Data_warehouse\Archives\archive.db') # print schema
    print db
    print db.death_records
    conn = sqlite3.connect(r'C:\Users\Sanhe.Hu\Data_warehouse\Archives\archive.db') # print data in table death_records
    c = conn.cursor()
    c.execute("SELECT * FROM death_records")
    for row in c.fetchall():
        print row

if __name__ == '__main__':
    for i in xrange(100):
        main()
#         try:
#             main()
#         except:
#             pass
#     unit_test_ToDo_and_Finished()
#     unit_test_archiveDB()