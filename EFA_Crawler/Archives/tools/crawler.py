##coding=utf8
##Date  =2014-08-21
##Author=Sanhe

import requests
import sys
import os
import pickle

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
            
class QueryString(object):
    '''Archives.com query string generator
    '''
    def __init__(self):
        self.template = dict()
        self.template['2'] = \
        ('http://www.archives.com/member/Default.aspx?_act=VitalSearchResult'
        '&LastName=%s' # lastname
        '&Country=%s' # country
        '&State=%s' # state
        '&RecordType=%s' # recordtype
        '&DeathYear=%s' # year
        '&activityID=%s' # activityID
        '&ShowSummaryLink=1'
        '&pagesize=%s' # pagesize 
        '&pageNumber=%s' # pagenumber
        '&pagesizeAP=10&pageNumberAP=1')
    
    def string(self,
                lastname, country, state, recordtype, 
                year, activityID, pagesize, pagenumber):
        query = self.template[recordtype] % (lastname,
                                             country,
                                             state,
                                             recordtype,
                                             year,
                                             activityID,
                                             pagesize,
                                             pagenumber)
        return query

class SparseInterval(object):
    def __init__(self, lower, upper):
        self.array = [lower, upper]

    def __str__(self):
        return str( zip(self.array[::2], self.array[1::2]) )
        
    def __len__(self):
        return len(self.array) / 2
    
    def index(self, x):
        '''return the i th interval that contains x 
        index(self, x) 返回 x 所在self.array和正负无穷所形成的 2n+1
        个(离散区间有n个子区间)小区间的index序号，例如:
            index(2.3, [1,2,3,4]) = 3
        '''
        ind = 1
        for i in self.array:
            if x < i:
                return ind
            else:
                ind += 1
        return ind
    
    def __add__(self, interval):
        '''return self + interval
        '''
        x, y = interval.array
        xi, yi = self.index(x), self.index(y)
        if xi%2 == 0: # 偶数，在子区间内
            a, b = xi-2, self.array[xi-2]
        else: # 奇数，在子区间外
            a, b = xi-1, x
        if yi%2 == 0: # 偶数，在子区间内
            c, d = self.array[yi-1], yi
        else: # 奇数，在子区间外
            c, d = y, yi-1
        
        ## 去除重复的连续值
        array = list()
        i, j = -9999,-9999 # 设置一个不可能出现在self.array中的初始值
        for n in self.array[:a] + [b, c] + self.array[d:]:
            i, j = j, n # example: array = [1, 2, 2, 3]
            if i != j: # 例如是 -9999 != 1 或者是 1 != 2
                array.append(j)
            else: # 例如是 2 == 2
                array.pop() # 删除之前append的2
                j = -9999 # 下一次就会变成 -9999, 3 了
                
        ## 输出
        spsI = SparseInterval(0,1)
        spsI.array = array
        return spsI
    
    def __contains__(self, interval):
        '''return whether interval is in self
        '''
        x, y = interval.array
        for i, j in zip(self.array[::2], self.array[1::2]):
            if (i <= x) & (y <= j):
                return True
        return False

class ToDo(object):
    def __init__(self):
        from _ref_data import lastnamelist
        self.data = {lastname: {str(i) : -1 for i in range(1900, 2021)} for lastname in lastnamelist}
    
    def __getitem__(self, key):
        return self.data[key]
    
    def _dump(self, path, replace = False):
        '''dump对象到文件, replace = False时，路径若已存在则无法保存
        '''
        if replace:
            pickle.dump(self, open(path, 'wb'))
        else:
            if os.path.exists(path): # already exists, error
                print '%s already exists, change name please!' % path
            else:
                pickle.dump(self, open(path, 'wb'))
    
    def _load(self, path):
        if os.path.exists(path): # exists, then load
            todo = pickle.load(open(path, 'rb'))
            self.data = todo.data
        else:
            print '%s not exists! cannot load!' % path
            
class Finished(object):
    def __init__(self):
        from _ref_data import lastnamelist
        self.data = {lastname: {str(i) : -1 for i in range(1900, 2021)} for lastname in lastnamelist}
    
    def __getitem__(self, key):
        return self.data[key]
    
    def _dump(self, path, replace = False):
        '''dump对象到文件, replace = False时，路径若已存在则无法保存
        '''
        if replace:
            pickle.dump(self, open(path, 'wb'))
        else:
            if os.path.exists(path): # already exists, error
                print '%s already exists, change name please!' % path
            else:
                pickle.dump(self, open(path, 'wb'))
    
    def _load(self, path):
        if os.path.exists(path): # exists, then load
            finished = pickle.load(open(path, 'rb'))
            self.data = finished.data
        else:
            print '%s not exists! cannot load!' % path
            
'''UNIT TEST'''
def test_Crawler():
    '''unit test for Class - Crawler'''
    crawler = Crawler()
    url = 'http://www.archives.com/member/'
    payload = {'__uid':'sanhe.hu@theeagleforce.net','__pwd':'efa2014'}
    crawler._login(url, payload)
    text = crawler.html(url)
    with open('login_test.html', 'wb') as f:
        f.write(text)
        
def test_QueryString():
    '''unit test for class - QueryString'''
    qs = QueryString()
    lastname = 'Hanson'
    country = 'US'
    state = 'FL'
    recordtype = '2'
    year = '2010'
    activityID = '6829f573-ef51-464f-ab59-b01df1bf8828'
    pagesize = '10'
    pagenumber = '1'
    print qs.string(lastname, country, state, recordtype, year, activityID, pagesize, pagenumber)

def test_SparseInterval():
    print '\n====== Unit Test - SparseInterval ======'
    sps1 = SparseInterval(1,2)
    sps1 = sps1 + SparseInterval(3,4)
    sps1 = sps1 + SparseInterval(5,6)
    print 'sps1 = %s' % sps1
    sps2 = SparseInterval(3, 3.3) # <== 自己修改测试值
    print '%s + %s = %s' % (sps1, sps2, sps1 + sps2) 
    print '%s is in %s ? = %s' % (sps2, sps1, sps2 in sps1)

def test_ToDo():
    task = ToDo()
    print task.data
    
def test_Finished():
    history = Finished()
    print history.data
    
if __name__ == '__main__':
#     test_Crawler()
#     test_QueryString()
#     test_SparseInterval()
#     test_ToDo()
    test_Finished()
    