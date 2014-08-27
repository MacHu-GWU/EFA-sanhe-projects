##coding=utf8

from tools.crawler import Crawler
import bs4
import jsontree
import itertools


def process(text):
    res = list()
    for line in text.split('\n'):
        if line.strip() != '':
            res.append( line.strip() )
    result = list()
    for piece in ' '.join(res).split():
        if piece.strip() != '':
            result.append( piece.strip() )
    return ' '.join(result)
    
def main():
    url = 'http://www.cvs.com/stores/cvs-pharmacy-address/11022+Highway+49-Gulfport-MS-39503/storeid=5908'
    spider = Crawler()
    html = spider.html(url)
    
    soup = bs4.BeautifulSoup(html)
    for div in soup.findAll('div', attrs = {'class': 'hours'}):
        for ul in div.findAll('ul'):
            for li in ul.findAll('li'):
                print '============'
                raw_text = li.text.strip()
                print process(raw_text)
                
            
main()