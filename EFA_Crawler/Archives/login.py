##coding=utf8
##Date  =2014-08-21
##Author=Sanhe
import Crawler

crawler = Crawler.Crawler()
url = 'http://www.archives.com/member/'
payload = {'__uid':'sanhe.hu@theeagleforce.net','__pwd':'efa2014'}
crawler._login(url, payload)
text = crawler.html(url)
with open('login_test.html', 'wb') as f:
    f.write(text)