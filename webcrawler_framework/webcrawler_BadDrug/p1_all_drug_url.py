##coding=utf8
# 从http://www.mayoclinic.org/diseases-conditions/index?letter=A 这个网站，其中letter=A-Z循环一遍
# 然后取得所有疾病的名字和url链接，并且存成名为disease_to_url (是一个dict)的pickle文件
import requests, re, os, itertools, sys
def urlhtml(url, timeout = 6):
    headers = {'User-Agent':'''Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) 
                 Chrome/23.0.1271.64 Safari/537.11''',
                 'Accept':'text/html;q=0.9,*/*;q=0.8',
                 'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                 'Accept-Encoding':'gzip',
                 'Connection':'close',
                 'Referer':None}
    r = requests.get(url, headers = headers, timeout = timeout)
    return r.text

rule = {'drug-recall-status nolist':'Regular', 
        'drug-recall-status1 nolist':'BlackBox', 
        'drug-recall-status2 nolist':'Recalled', 
        'drug-recall-status4 nolist':'Alert', 
        'drug-recall-status3 nolist':'Recalled'}
with open('name_url.txt', 'rb') as f: ## download from: http://www.bad-drug.net/bad-drug-list#
    rowlist = f.read().split('\n')
# <a href=http://www.bad-drug.net/bad-drug/zoloft" class="drug-recall-status1 nolist"></a>
p1= re.compile(r'(?<=<a href=)([\s\S]{1,100})(?=" class=")') ## url
p2= re.compile(r'(?<=class=")([\s\S]{1,100})(?="></a>)')
c = itertools.count(1,1)
baddrug = dict()
for row in rowlist:
    if 'drug-recall-status' in row: ## 1421, 667, 754
        url = re.findall(p1, row)[0]
        name = url.replace('http://www.bad-drug.net/bad-drug/', '')
        status = rule[re.findall(p2, row)[0]]
        baddrug.setdefault(name, (url, status))
## 保存所有的数据
os.chdir('BadDrugs')
for name, tp in baddrug.iteritems():
    url, status = tp
    fname = name + ' - ' + status + '.html'
    if not os.path.exists(fname):
        try:
            content = urlhtml(url)
            x= re.compile(r'(?<=<h1 itemprop="aspect">)([\s\S]*)(?=</h2>)')
            fullhtml = re.findall(x, content)[0]
            fullhtml = fullhtml.replace('style="display: none;"', '')
            with open(fname, 'wb') as f:
                f.write('<h1 itemprop="aspect">' + fullhtml + '</h2>')
        except:
            print fname, sys.exc_info()[0]