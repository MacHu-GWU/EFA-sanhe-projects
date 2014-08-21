import urllib2
import urllib
import cookielib ## cookies


# login_url = 'http://www.archives.com/member/'
# acc_pwd = {'__uid':'sanhe.hu@theeagleforce.net','__pwd':'diablo1987'}
# cj = cookielib.CookieJar() ## add cookies
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj)) ## build opener
# opener.addheaders = [('User-agent','Mozilla/5.0 \
#                     (compatible; MSIE 6.0; Windows NT 5.1)')] ## browser header
# data = urllib.urlencode(acc_pwd) ## encode login acc and pwd
# try: ## handle login connection time out
#     opener.open(login_url,data,10)
#     print 'log in - success!'
# except:
#     print 'log in - times out!', login_url
# 
# url = 'http://www.archives.com/member/Default.aspx?_act=VitalSearchResult&LastName=SMITH&Country=US&State=AK&RecordType=2&DeathYear=2004&DeathYearSpan=10&activityID=e795018f-27e0-4851-a80a-fb0c0e1ed5cb&pagesize=10&pageNumber=1&pagesizeAP=10&pageNumberAP=1'
# page = opener.open(url, data, 30)
# print page.read()

import os
print os.path.getsize('data\White_MS_3001-4000.txt')
print os.path.getsize('New Text Document.txt')
os.remove('New Text Document.txt')