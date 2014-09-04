##coding=utf8

from tools.crawler import Crawler
import bs4
import jsontree
import itertools
import re

fname = 'taskdata.py'
spider = Crawler()
homepage = 'http://www.cvs.com'

def prt_jt(jt):
    return jsontree.dumps(jt, sort_keys=True,indent=4,separators=(',' , ': '))

def dump_jt(jt, fname):
    with open(fname, 'wb') as f:
        f.write(prt_jt(jt))

def load_jt(fname):
    with open(fname, 'rb') as f:
        return jsontree.loads(f.read())
    
def process_hour_string(text):
    res = list()
    for line in text.split('\n'):
        if line.strip() != '':
            res.append( line.strip() )
    result = list()
    for piece in ' '.join(res).split():
        if piece.strip() != '':
            result.append( piece.strip() )
    return ' '.join(result)

def s1_state_layer():
    try:
        task = load_jt(fname)
    except:
        task = jsontree.jsontree()
    
    entrance_url = 'http://www.cvs.com/stores/cvs-pharmacy-locations'
    
    html = spider.html(entrance_url, timeout = 10)
    if html:
        for line in html.split('\n'):
            if '<a href="/stores/cvs-pharmacy-locations' in line:
                soup = bs4.BeautifulSoup(line.strip())
                href = soup.find('a')['href']
                state = href.split(r'/').pop()
                task[state] = {'url': homepage + href}
    dump_jt(task, fname)
    
def s2_city_layer():
    task = load_jt(fname)
    for state in task:
        url = task[state]['url']
        
        if task[state].get('DONE', 0) == 0: # 没有爬过的时候才爬 
            html = spider.html(url, timeout = 10)
            if html:
                for line in html.split('\n'):
                    if '<a href="/stores/cvs-pharmacy-locations/%s' % state in line:
                        soup = bs4.BeautifulSoup(line.strip())
                        href = soup.find('a')['href'] 
                        city = href.split(r'/').pop()
                        task[state][city] = {'url': homepage + href}
            else:
                print '%s - %s FailED' % (state, city)       
            dump_jt(task, fname)
        print state

def s3_store_layer():
    task = load_jt(fname)
    for state in task:
        for city in task[state]:
            
            if city != 'url': # 不要被url干扰了
                if len(task[state][city].keys()) == 1: # 只有url一个key 说明没爬过
                    url = task[state][city]['url']
                    print state, city, url
                    html = spider.html(url, timeout = 10)
                    if html:
                        soup = bs4.BeautifulSoup(html)
                        c = itertools.cycle(xrange(4)) # 循环器
                        for tr in soup.findAll('tr')[1:]: # 除了第一个tr不是，其他都是， 每次输出一个药店的记录
                            
                            for td in tr.findAll('td'): # 每次输出一个tag
                                flag = c.next()
                                
                                if flag == 0:
                                    storeID = td.text.strip()
                                    task[state][city].setdefault(storeID, jsontree.jsontree() )
                            
                                elif flag == 1:
                                    task[state][city][storeID].setdefault('addr', td.text.strip())
                                    
                                elif flag == 2:
                                    task[state][city][storeID].setdefault('tel', td.text.strip())
                                
                                else:
                                    task[state][city][storeID].setdefault('url', homepage + td.a['href'] )
                            dump_jt(task, fname)
                    
def s4_store_hour_layer():
    task = load_jt(fname)

    
    for state in task:
        for city in task[state]:
            if city != 'url':
                for store in task[state][city]:
                    if store != 'url':
                        if len(task[state][city][store].keys()) == 5: ## 只有addr, tel, url 3个key说明没爬过
                            ## 真正开始爬
                            url = task[state][city][store]['url']
                            print state, city, store
                            html = spider.html(url)
                            if html:
                                soup = bs4.BeautifulSoup(html)
                                ## 解析 hours
                                hour = list()
                                for div in soup.findAll('div', attrs = {'class': 'hours'}):
                                    for ul in div.findAll('ul'):
                                        for li in ul.findAll('li'):
                                            raw_text = li.text.strip()
                                            hour.append( process_hour_string(raw_text) )
                                
                                ## 解析 service
                                service = list()
                                for p in soup.findAll('p', attrs = {'class': 'nomargin'}):
                                    service.append(p.text.strip())
                                
                                ## 插入数据
#                                 for i in hour:
#                                     if i not in task[state][city][store]['hour']:
#                                         task[state][city][store]['hour'].append(i)
#                                 
#                                 task[state][city][store]['service'] = service
#                                 for j in service:
#                                     if j not in task[state][city][store]['service']:
#                                         task[state][city][store]['service'].append(j)
                                if (len(hour) != 0) & (len(service) != 0):
                                    task[state][city][store]['hour'] = hour # 添加hour
                                    task[state][city][store]['service'] = service
        dump_jt(task, fname)
    
if __name__ == '__main__':
#     s1_state_layer()
#     s2_city_layer()
#     for x in xrange(10):
#         try:
#             s3_store_layer()
#         except:
#             pass
    for x in xrange(10):
        try:
            s4_store_hour_layer()
        except:
            pass