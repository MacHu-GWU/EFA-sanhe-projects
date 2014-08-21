##coding=utf8
##rei
import requests

def url_html(url, timeout = 6):
    '''返回url的HTML内容
    '''
    headers = {'User-Agent': ('Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11, '
                              '(KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),
               'Accept':'text/html;q=0.9,*/*;q=0.8',
               'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding':'gzip',
               'Connection':'close',
               'Referer':None}
    r = requests.get(url, headers = headers, timeout = timeout)
    return r.text
    
def url_download(url, save_as, timeout = 10):
    '''把url的文件下载到save_as的位置下
    '''
    headers = {'User-Agent': ('Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11, '
                              '(KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),
               'Accept':'text/html;q=0.9,*/*;q=0.8',
               'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding':'gzip',
               'Connection':'close',
               'Referer':None}
    response = requests.get(url, headers = headers, timeout = timeout, stream=True)
    with open(save_as, 'wb') as f:
        for block in response.iter_content(1024):
            if not block:
                break
            f.write(block)

if __name__ == '__main__':
    url = 'http://norvig.com/spell.py'  
    print url_html(url)
    url_download(url, 'nice.py')