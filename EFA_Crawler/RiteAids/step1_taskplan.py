##coding=utf8

from LinearSpider.crawler import Crawler, Taskplanner
import bs4
import re, pprint
import jsontree
import itertools
'''
第一级，入口页面，内容是所有的rite aid的商店的url
    https://www.riteaid.com/store-site-map
    
第二季，rite aid商店，内容是具体信息
    https://www.riteaid.com/store-details?storeNumber=01140
'''

def prt_jt(jt):
    print jsontree.dumps(jt, sort_keys=True,indent=4,separators=(',' , ': '))

def dump_jt(jt, fname):
    with open(fname, 'wb') as f:
        f.write(jsontree.dumps(jt, sort_keys=True,indent=4,separators=(',' , ': ')))

def load_jt(fname):
    with open(fname, 'rb') as f:
        return jsontree.loads(f.read())
    
def step1_taskplan():
    '''设定函数内常量'''
    spider = Crawler()
    TP = Taskplanner()
    base_url = 'https://www.riteaid.com'
    entrance_url = 'https://www.riteaid.com/store-site-map'
    
    TP.todo.setdefault(entrance_url, TP.dict_to_json({'data': None}  )  ) # 给下一步预设空间的行为发生在当前页面爬完的情况下
    
    html = spider.html(entrance_url) # 开始爬
    if html:
        soup = bs4.BeautifulSoup(html)
        for a in soup.findAll(href = re.compile(r'https://www.riteaid.com/store-details\?storeNumber=\d*')):
            TP.todo[entrance_url].setdefault( a['href'],
                                              TP.dict_to_json({'data': a.text}  )  )

    TP._dump_todo('task.txt')


def validate(phone, hours, additional_info, detail):
    if (len(phone) == 14) & (len(hours) == 4) & (len(additional_info) == 2):
        print "CORRECT"
        return True
    else:
        print "ERROR!", (phone, hours, additional_info, detail)
        return False
    
def step2_download():
    spider = Crawler()
    TP = Taskplanner()
    TP._load_todo('task.txt')
    base_url = 'https://www.riteaid.com'
    entrance_url = 'https://www.riteaid.com/store-site-map'
    
    try:
        riteaid = load_jt('riteaid.txt')
    except:
        riteaid = jsontree.jsontree()
        
    counter = itertools.count(0)
    for store_url in TP.ignore_iter(TP.todo[entrance_url], ['data']):
        text = TP.todo[entrance_url][store_url]['data']
        storeID, address = text.split(',', 1)
        storeID, address = storeID.strip(), address.strip()
        ## 每页的 html 页面
        if storeID not in riteaid:
            html = spider.html(store_url)
            if html:
                soup = bs4.BeautifulSoup(html)
                ''' phone number '''
                for p in soup.findAll('p', attrs = {'class', 'padding-phone'}):
                    phone = p.text.replace(p.strong.text, '').strip().replace(' ', '-') # 处理电话号码
                    
                ''' hour '''
                hours = list()
                for ul in soup.findAll('ul', attrs = {'class', 'days'}):
                    hours.append( ul.text.split() )
                
                ''' additional information '''
                additional_info = list()
                for div in soup.findAll('div', attrs = {'id': 'eventListId'}):
                    for li in div.findAll('li'):
                        additional_info.append( li.text )
                
                ''' store detail '''
                detail = {}
                for div in soup.findAll('div', attrs = {'class': 'storeDetailsAttributeCategory'}):
                    storeDetailsAttributeCategory = div.strong.text.strip()
                    detail.setdefault(storeDetailsAttributeCategory, list())
                    for subdiv in div.findAll('div', attrs = {'class': 'storeDetailsAttribute'}):
                        detail[storeDetailsAttributeCategory].append(subdiv.text.strip())
            
            if validate(phone, hours, additional_info, detail):
                riteaid.setdefault(storeID, (address, phone, hours, additional_info, detail) )
                dump_jt(riteaid, 'riteaid.txt')
                print storeID, counter.next()
            
def unit_test():
    
    url = 'https://www.riteaid.com/store-details?storeNumber=01140'
    spider = Crawler()
    html = spider.html(url)
    if html:
        soup = bs4.BeautifulSoup(html)
        ''' phone number '''
        for p in soup.findAll('p', attrs = {'class', 'padding-phone'}):
            phone = p.text.replace(p.strong.text, '').strip().replace(' ', '-') # 处理电话号码
            
        ''' hour '''
        hours = list()
        for ul in soup.findAll('ul', attrs = {'class', 'days'}):
            hours.append( ul.text.split() )
        
        ''' additional information '''
        additional_info = list()
        for div in soup.findAll('div', attrs = {'id': 'eventListId'}):
            for li in div.findAll('li'):
                additional_info.append( li.text )
        
        ''' store detail '''
        detail = {}
        for div in soup.findAll('div', attrs = {'class': 'storeDetailsAttributeCategory'}):
            storeDetailsAttributeCategory = div.strong.text.strip()
            detail.setdefault(storeDetailsAttributeCategory, list())
            for subdiv in div.findAll('div', attrs = {'class': 'storeDetailsAttribute'}):
                detail[storeDetailsAttributeCategory].append(subdiv.text.strip())
                
        print phone, hours, additional_info, detail
            
    
    
    
    
    
if __name__ == '__main__':
#     step1_taskplan()
    for i in xrange(100):
        try:
            step2_download()
        except:
            pass
#     unit_test()

