##coding=utf8
##Date  =2014-08-21
##Author=Sanhe

import requests
import sys
reload(sys);
eval('sys.setdefaultencoding("utf-8")')

class Crawler(object):
    def __init__(self):
        self.headers = {'User-Agent': ('Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11, '
                                       '(KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),
                        'Accept':'text/html;q=0.9,*/*;q=0.8',
                        'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                        'Accept-Encoding':'gzip',
                        'Connection':'close',
                        'Referer':None}
        self.auth = None # initialize the self.auth. Then if there's no login, Crawler.html can work in regular mode
        
    def _login(self, url, payload):
        '''
        url = login_page_url
        payload = {key1: acc, key2: password}
        '''
        self.auth = requests.Session()
        self.auth.post(url, data=payload)
        
    def html(self, url, timeout = 6):
        if not self.auth: # if no login needed, then self.c = None, then not self.c = True
            ## regular get html, use requests.get
            try:
                r = requests.get(url, headers = self.headers, timeout = timeout)
                return r.text # if success, return html
            except:
                print '%s time out!' % url
                return None # if failed, return none
        else: ## if login needed, use self.auth.get
            try:
                r = self.auth.get(url, headers = self.headers, timeout = timeout)
                return r.text # if success, return html
            except:
                print '%s time out!' % url
                return None # if failed, return none

if __name__ == '__main__':
#     import sys
#     reload(sys);
#     eval('sys.setdefaultencoding("utf-8")')
    
    crawler = Crawler()
    url = 'http://www.archives.com/member/'
    payload = {'__uid':'sanhe.hu@theeagleforce.net','__pwd':'efa2014'}
    crawler._login(url, payload)
    text = crawler.html(url)
    with open('login_test.html', 'wb') as f:
        f.write(text)