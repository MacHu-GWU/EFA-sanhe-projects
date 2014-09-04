##coding=utf8

import re
import bs4
from LinearSpider.crawler import Crawler, Taskplanner


p = re.compile(r'/storelistings/storesincity.jsp\?requestType=locator&state=[.]*')
html = '<a title="ALABASTER, AL" class="no_underline" href="/storelistings/storesincity.jsp?requestType=locator&state=AL&city=ALABASTER">ALABASTER, AL</a>'

# soup = bs4.BeautifulSoup(text)
# print soup.findAll(href = p)

# entrance_url = 'http://www.walgreens.com/storelistings/storesbycity.jsp?requestType=locator&state=AL'
# spider = Crawler()
# html = spider.html(entrance_url)

# with open('walgreens.html', 'rb') as f:
#     html = f.read()
soup = bs4.BeautifulSoup(html)
for a in soup.findAll('a', href = re.compile(r'/storelistings/storesincity.jsp\?requestType=locator&state=[.]*')):
    print a