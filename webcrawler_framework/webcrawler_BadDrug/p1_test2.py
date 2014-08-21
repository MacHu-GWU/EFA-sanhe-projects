##coding=utf8
# 从http://www.mayoclinic.org/diseases-conditions/index?letter=A 这个网站，其中letter=A-Z循环一遍
# 然后取得所有疾病的名字和url链接，并且存成名为disease_to_url (是一个dict)的pickle文件
import requests, bs4, re, os
def urlhtml(url):
    user_agent = {'User-agent': 'Mozilla/5.0'}
    r = requests.get(url, headers = user_agent, timeout = 10)
    return r.text

with open('main.txt', 'rb') as f:
    content = f.read()
    
p= re.compile(r'(?<=<a href=")([\s\S]{1,100})(?=</a>)')
res = re.findall(p,content)
taglist = list()
for i in res:
    taglist.append('<a href=' + i + '</a>')
with open('name_url.txt', 'wb') as f:
    f.write('\n'.join(taglist))