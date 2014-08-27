##coding=utf8
##Date  =2014-08-21
##Author=Sanhe

import requests
import sys
import os
import jsontree

reload(sys); # change the system default encoding = utf-8
eval('sys.setdefaultencoding("utf-8")')

class Crawler(object):
    '''Simple http Crawler class
    '''
    def __init__(self):
        self.headers = {'User-Agent': ('Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11, '
                                       '(KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),
                        'Accept':'text/html;q=0.9,*/*;q=0.8',
                        'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                        'Accept-Encoding':'gzip',
                        'Connection':'close',
                        'Referer':None}
        self.auth = None # initialize the self.auth. Then if there's no login, Crawler.html can work in regular mode
        
    def _login(self, url, payload, timeout = 6):
        '''website log in
        url = login_page_url
        payload = {key1: acc, key2: password}
        '''
        self.auth = requests.Session()
        try:
            self.auth.post(url, data=payload, timeout = timeout)
            print 'successfully loged in to %s' % url
            return True
        except:
            return False
        
    def html(self, url, timeout = 6):
        '''return the html for the url
        '''
        if not self.auth: # if no login needed, then self.c = None, then not self.c = True
            ## regular get html, use requests.get
            try:
                r = requests.get(url, headers = self.headers, timeout = timeout)
                return r.text # if success, return html
            except:
#                 print '%s time out!' % url # <=== 测试时才用
                return None # if failed, return none
        else: # if login needed, use self.auth.get
            try:
                r = self.auth.get(url, headers = self.headers, timeout = timeout)
                return r.text # if success, return html
            except:
#                 print '%s time out!' % url <=== 测试时才用
                return None # if failed, return none
            
class Taskplanner(object):
    def __init__(self):
        self.todo = jsontree.jsontree()
        self.finished = jsontree.jsontree()
        
    def prt_jt(self, jt):
        print jsontree.dumps(jt, sort_keys=True,indent=4,separators=(',' , ': '))
    
    def _dump_todo(self, path, replace = False):
        '''dump taskplanner.todo to local file.
        When replace = False, existing local file will not be overwrite. For safety
        '''
        if replace:
            with open(path, 'wb') as f:
                f.write( jsontree.dumps(self.todo, sort_keys=True,indent=4,separators=(',' , ': ')) )
        else:
            if os.path.exists(path): # already exists, error
                print '%s already exists, change name please!' % path
            else:
                with open(path, 'wb') as f:
                    f.write( jsontree.dumps(self.todo, sort_keys=True,indent=4,separators=(',' , ': ')) )

    def _dump_finished(self, path, replace = False):
        '''dump taskplanner.finished to local file.
        When replace = False, existing local file will not be overwrite. For safety
        '''
        if replace:
            with open(path, 'wb') as f:
                f.write( jsontree.dumps(self.finished, sort_keys=True,indent=4,separators=(',' , ': ')) )
        else:
            if os.path.exists(path): # already exists, error
                print '%s already exists, change name please!' % path
            else:
                with open(path, 'wb') as f:
                    f.write( jsontree.dumps(self.finished, sort_keys=True,indent=4,separators=(',' , ': ')) )

    def _load_todo(self, path):
        '''load taskplanner.todo data from local file
        '''
        if os.path.exists(path): # exists, then load
            with open(path, 'rb') as f:
                self.todo = jsontree.loads(f.read())
        else:
            print '%s not exists! cannot load!' % path

    def _load_finished(self, path):
        '''load taskplanner.fished data from local file
        '''
        if os.path.exists(path): # exists, then load
            with open(path, 'rb') as f:
                self.finished = jsontree.loads(f.read())
        else:
            print '%s not exists! cannot load!' % path
    
    def ignore_iter(self, dictionary, ignore):
        for key in dictionary:
            if key not in ignore:
                yield key

    def dict_to_json(self, dictionary):
        return jsontree.loads(jsontree.dumps(dictionary))
    
def unit_test():
    task = Taskplanner()
    data = {'a': 
                {
                 'info': [1],
                 'a1': 
                    {
                     'info': [1,1]
                     },
                 'a2': 
                    {
                     'info': [2,2]
                     }
                 }
            }
    task.todo = task.dict_to_json(data)
#     task.prt_jt( task.todo )

    task1 = Taskplanner()
    task1.todo.setdefault('a', task1.dict_to_json({'b':'c'}) )
#     task1.todo['a'] = {'b':'c'})
    print task1.todo
    print task1.todo.a.b
if __name__ == '__main__':
    unit_test()