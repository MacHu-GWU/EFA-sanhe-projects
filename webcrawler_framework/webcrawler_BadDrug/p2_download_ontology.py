##coding=utf8
# 为所有的药建立一个文件夹，每个文件夹下有多个subcategory文件，
# 存放了原始页面的纯HTML。而下一步是摘除其他广告信息以及无关信息
import requests
import bs4
import re
import os

content = '<a href="http://www.bad-drug.net/bad-drug/zyvox" title="More Information on Zyvox">Zyvox</a>'
soup = bs4.BeautifulSoup(content)

for tag in soup.find_all('a'):
    print tag