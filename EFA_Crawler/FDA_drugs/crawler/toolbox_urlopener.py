## coding=utf-8

import urllib2
import bs4
def url_to_content(url, timeout = 6):
    ''' Function: given a url, return html text
    '''
    ''' === disguise as browser === '''
    req = urllib2.Request(url,headers={'User-Agent':'Magic Browser'})
    ''' === crawl it !=== '''
    try: ## can avoid to raise an error
        content = urllib2.urlopen(req, None, timeout).read() ## response is a string
        return content
    except:
        print 'time out!', url
        return None
    
def url_to_soup(url, timeout = 6):
    ''' Function: given a url, return html text
    '''
    ''' === disguise as browser === '''
    req = urllib2.Request(url,headers={'User-Agent':'Magic Browser'})
    ''' === crawl it !=== '''
    try: ## can avoid to raise an error
        content = urllib2.urlopen(req, None, timeout).read() ## response is a string
        return bs4.BeautifulSoup(content)
    except:
        print 'time out!', url
        return None
    
# url = 'http://www.rxlist.com/epzicom-drug/clinical-pharmacology.htm'
# print url_to_content(url).encode('utf-8')