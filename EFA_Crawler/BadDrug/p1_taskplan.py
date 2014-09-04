##coding=utf8

from LinearSpider.crawler import Crawler, Taskplanner
import bs4
import re, os, pprint, itertools

spider = Crawler()
rule = {'drug-recall-status':'Regular',  # status 和 FDA给鉴定的标签的对应关系
        'drug-recall-status1':'Regular', 
        'drug-recall-status2':'BlackBox', 
        'drug-recall-status3':'Recalled', 
        'drug-recall-status4':'Alert'}

def valid_name(name):
    rule = ['|']
    for i in rule:
        if i in name:
            name = name.replace(i, '')
    return name

def taskplan():
    task = Taskplanner()
    try:
        task._load_todo('task.txt')
    except:
        pass
    
    html = spider.html('http://www.bad-drug.net/bad-drug-list')
    if html:
        soup = bs4.BeautifulSoup(html)
        
        for ul in soup.findAll('ul', attrs = {'class': 'drug-list'}):
            for li in ul.findAll('li'):
                try: # 找到 drugname, drugurl, drugstatus, 并存入task.todo
                    info = li.findAll('a')
                    drugname, drugurl, drugstatus =  info[1].text, info[1]['href'],  rule[ info[0]['class'][0] ]
                    task.todo.setdefault(drugurl, task.dict_to_json({'info': (drugname, drugstatus)} ) ) # drugurl is key
                except:
                    pass
        task._dump_todo('task.txt', replace = True)

def download_raw_html():
    task = Taskplanner()
    task._load_todo('task.txt')
    data_dir = r'C:\Users\Sanhe.Hu\Data_warehouse\BadDrugs\raw html' # <=== the folder used to save raw html file
    
    c = itertools.count(0)
    
    for drugurl in task.todo:
        drugname, drugstatus = task.todo[drugurl]['info']
        fname = os.path.join(data_dir, '%s-%s.html' % (valid_name(drugname), drugstatus))
        
        if not os.path.exists(fname): # 如果没有爬过
            html = spider.html(drugurl)
            if html: # 如果html良好
                with open(fname, 'wb') as f:
                    f.write(html)
                print '%s = %s-%s' % (c.next(), drugname, drugstatus)
            else:
                print '\tFAILED %s = %s-%s' % (c.next(), drugname, drugstatus)

def process_raw_html():
    '''TO BE DONE
    '''
    pass

def unit_test():
    text = 'abcdefg'
    p = re.compile(r'abc[\s\S]*')
    print re.findall(p, text)
    
if __name__ == '__main__':
#     taskplan()
#     download_raw_html()
    process_raw_html()
#     unit_test()

