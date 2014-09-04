##coding=utf8

''' THIS IS THE SCRIPT TO CRAWL RITEAID STORE LOCATION AND DETAIL INFORMATION
'''
from LinearSpider.crawler import Crawler, Taskplanner
import bs4
import re
import jsontree
import itertools
from collections import deque
from pprint import pprint as ppt

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
    base_url = 'http://www.walgreens.com/'
    entrance_url = 'http://www.walgreens.com/storelocator/find.jsp?tab=store%20locator&requestType=locator'
    
    '''爬每个州url''' # 州，城市，商店三块是要一段一段注释掉运行的
#     TP.todo.setdefault(entrance_url, TP.dict_to_json({'data': None}  )  ) # 给下一步预设空间的行为,发生在当前页面爬完的情况下
#     with open('storelocator_sorted_by_state.txt', 'rb') as f:
#         html = f.read()
# #     html = spider.html(entrance_url) # 开始爬
#     
#     if html:
#         soup = bs4.BeautifulSoup(html)
#         for a in soup.findAll('a', href = re.compile(r'/storelistings/storesbycity.jsp\?requestType=locator&state=\D*')):
#             TP.todo[entrance_url].setdefault( base_url + a['href'],
#                                               TP.dict_to_json({'data': a.text.strip()}  )  )
    
    '''爬每个城市url''' # 州，城市，商店三块是要一段一段注释掉运行的
#     for state_url in TP.ignore_iter(TP.todo[entrance_url], ['data']):
#         html = spider.html(state_url)
#             
#         if html:
#             soup = bs4.BeautifulSoup(html)
#             for a in soup.findAll('a', href = re.compile(r'/storelistings/storesincity.jsp\?requestType=locator&state=[.]*')):
#                 TP.todo[entrance_url][state_url].setdefault( base_url + a['href'],
#                                                                                    TP.dict_to_json({'data': a.text.strip()}  )  )

#                 print base_url + a['href'], '---', a.text.strip()

    '''爬每个商店url''' # 州，城市，商店三块是要一段一段注释掉运行的
#     TP._load_todo('task-walgreens.txt')
#     for state_url in TP.ignore_iter(TP.todo[entrance_url], ['data']):
#         for city_url in TP.ignore_iter(TP.todo[entrance_url][state_url], ['data']):
#             if len(TP.todo[entrance_url][state_url][city_url]) == 1: # 只有data的时候，才爬
#                 html = spider.html(city_url)
#                 if html:
#                     soup = bs4.BeautifulSoup(html)
#                     for p in soup.findAll('p', attrs = {'class': 'float-left wid300 nopad'}):
#                         TP.todo[entrance_url][state_url][city_url].setdefault( base_url + p.a['href'],
#                                                                                TP.dict_to_json({ } )  )
    
    '''爬每个商店里的信息'''
    try:
        walgreens = load_jt('walgreens.txt')
    except:
        walgreens = jsontree.jsontree()
    
    pStoreID = r'(?<=id=)\d+'
    
    TP._load_todo('task-walgreens.txt')
    for state_url in TP.ignore_iter(TP.todo[entrance_url], ['data']):
        for city_url in TP.ignore_iter(TP.todo[entrance_url][state_url], ['data']):
            for store_url in TP.ignore_iter(TP.todo[entrance_url][state_url][city_url], ['data']):
                
                ID = re.findall(pStoreID, store_url)[0]
                if ID not in walgreens: # 只要没有爬过
                    html = spider.html(store_url)
                    if html:
                        soup = bs4.BeautifulSoup(html)
                        
                        street = 'None' # extract street
                        for p in soup.findAll('p', attrs = {'class': 'mrgRt10px padTop2px padBtm2px nopad',
                                                            'itemprop': 'streetAddress'}):
                            street = p.text.strip() 
                        
                        city = 'None' # extract city
                        for span in soup.findAll('span', attrs = {'itemprop': 'addressLocality'}):
                            city = span.text.strip()
                            
                        state = 'None' # extract state
                        for span in soup.findAll('span', attrs = {'itemprop': 'addressRegion'}):
                            state = span.text.strip()
                            
                        zipcode = 'None' # extract zipcode
                        for span in soup.findAll('span', attrs = {'itemprop': 'postalCode'}):
                            zipcode = span.text.strip()
                            
                        phone = 'None' # extract telephone
                        for p in soup.findAll('p', attrs = {'class': 'nopad',
                                                            'itemprop': 'telephone'}):
                            phone = p.text.strip()
                        
                        ## ====================== OFFICE HOURS ======================
                        hours = list() # extract office hours
                        for p in soup.findAll('p', attrs = {'class': 'nopad wid100 float-left'}):
                            hours.append( p.text.strip() )
                            
                        ## exam hours subcategory
                        hours_category = list()
                        for h3 in soup.findAll('h3'): # exam if there's store hours
                            for strong in h3.findAll('strong'):
                                if ('Shop' in strong.text) or ('Photo' in strong.text) or ('Store pickup' in strong.text):
                                    hours_category.append('store')
                        if len(soup.findAll('div', attrs = {'class': 'padBtm5px float-left'}) ): # exam if there's pharmacy hours
                            hours_category.append('pharmacy')
                        if len(soup.findAll('div', attrs = {'class': 'mrgTop25px padBtm5px'}) ): # exam if there's clinic hours
                            hours_category.append('clinic')
                        
                        ## process map hours to it's subcategory
                        hours_detail, hours = {}, deque(hours)
                        if 'store' in hours_category:
                            hours_detail['store'] = list()
                            hours_detail['store'].append(hours.popleft())
                            hours_detail['store'].append(hours.popleft())
                            hours_detail['store'].append(hours.popleft())
                        if 'pharmacy' in hours_category:
                            hours_detail['pharmacy'] = list()
                            hours_detail['pharmacy'].append(hours.popleft())
                            hours_detail['pharmacy'].append(hours.popleft())
                            hours_detail['pharmacy'].append(hours.popleft())
                        if 'clinic' in hours_category:
                            hours_detail['clinic'] = list(hours)
                            
                        ## ====================== SERVICE ===========================
                        services = dict() # extract service
                        
                        for div in soup.findAll('div', attrs = {'class': 'padTop5px wid220 float-left'}):
                            for li in div.findAll('li'):
                                services.setdefault('shop', list())
                                services['shop'].append( li.text.strip() )
                
                        for div in soup.findAll('div', attrs = {'class': 'wid220 float-left'}):
                            for li in div.findAll('li'):
                                services.setdefault('pharmacy', list())
                                services['pharmacy'].append( li.text.strip() )  
                                               
                        for div in soup.findAll('div', attrs = {'class': 'mrgTop10px mrgBtm20px'}):
                            for a in div.findAll('a', href = re.compile(r'http://photo.walgreens.com/walgreens/storepage/[\s\S]*')):
                                services.setdefault('photo', list())
                                services['photo'].append( a.text.strip() )  
                        
                        if validate(street, city, state, zipcode, phone, hours_detail, services, store_url ): # 说明成功了
                            walgreens.setdefault(ID, {'street': street,
                                                      'city': city,
                                                      'state': state,
                                                      'zipcode': zipcode,
                                                      'phone': phone,
                                                      'hours': hours,
                                                      'services': services})
                            print city, state, ID
        dump_jt(walgreens, 'walgreens.txt')
                        
#                     print len(hours), len(services),  store_url

#     TP._load_todo('task-walgreens.txt')   
#     TP._dump_todo('task-walgreens.txt', replace = True)



def validate(street, city, state, zipcode, phone, hours, services, store_url ):
#     pprint.pprint((street, city, state, zipcode, phone, hours, services ))
    if (street == 'None') or (city == 'None') or (state == 'None') or (len(zipcode) != 5):
#         print 'address ERROR: %s-%s-%s-%s!' % (street, city, state, zipcode)
        print '\taddress ERROR: %s %s' % (store_url, street+ city+ state+ zipcode)
        return False
    if len(hours) == 3:
        print '\tSERVICE ERROR: %s %s' % (store_url, hours)
        return False
    if len(services) == 3:
#         print 'SERVICE ERROR: %s' % services
        print '\tSERVICE ERROR: %s %s' % (store_url, services)
        return False
    return True

def unit_test():
    spider = Crawler()
    url = 'http://www.walgreens.com/locator/walgreens-424+sycolin+rd+se-leesburg-va-20175/id=15085'
#     url = 'http://www.walgreens.com//locator/walgreens-900+illinois+ave.-stevens+point-wi-54481/id=13074'
    html = spider.html(url)
    if html:
        soup = bs4.BeautifulSoup(html)
        services = dict() # extract service
        
        for div in soup.findAll('div', attrs = {'class': 'padTop5px wid220 float-left'}):
            for li in div.findAll('li'):
                services.setdefault('shop', list())
                services['shop'].append( li.text.strip() )

        for div in soup.findAll('div', attrs = {'class': 'wid220 float-left'}):
            for li in div.findAll('li'):
                services.setdefault('pharmacy', list())
                services['pharmacy'].append( li.text.strip() )  
                               
        for div in soup.findAll('div', attrs = {'class': 'mrgTop10px mrgBtm20px'}):
            for a in div.findAll('a', href = re.compile(r'http://photo.walgreens.com/walgreens/storepage/[\s\S]*')):
                services.setdefault('photo', list())
                services['photo'].append( a.text.strip() )        
        
        ppt( services )
    pass
            

if __name__ == '__main__':
#     step1_taskplan() # 先执行taskplan
    unit_test()

