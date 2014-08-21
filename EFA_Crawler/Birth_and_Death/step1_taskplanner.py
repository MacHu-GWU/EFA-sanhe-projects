import urllib2
import urllib
import cookielib ## cookies
import re ## regular expression

''' query string generate '''
def DR_url_gen(lastname, state, activityID, pagesize, pagenumber):
    '''
        DR_url_gen = DeathRecord_url_generator
    '''
    body1 = 'http://www.archives.com/member/Default.aspx?_act=VitalSearchResult&LastName='
    body2 = '&Country=US&State='
#     body3 = '&RecordType=2&DeathYear=2004&DeathYearSpan=10&activityID='
    body3 = '&RecordType=1&BirthYear=2004&BirthYearSpan=10&activityID='
    body4 = '&pagesize='
    body5 = '&pageNumber='
    body6 = '&pagesizeAP=10&pageNumberAP=1'
    url = body1 + lastname + body2 + state + body3 + activityID + body4 + str(pagesize) + body5 + str(pagenumber) + body6
    return url

statelist = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'HI', 'ID', 'IL', 'IA', 'KS', 'KY', 
             'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 
             'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']

''' urllib '''
def url_to_content(url, timeout = 10):
    ''' Function: given a url, return html text
    '''
    ''' === disguise as browser === '''
    req = urllib2.Request(url,headers={'User-Agent':'Magic Browser'})
    ''' === crawl it !=== '''
    try: ## can avoid to raise an error
        content = urllib2.urlopen(req, None, timeout).read() ## response is a string
        print 'successfully read html\n'
    except:
        print 'time out!', url
        return 'NA'
    return content

def find_amount_of_record_by_content(content):
    try:
        s1 = re.findall(r'(?<=>Showing).{1,30}(?=</span>)', content)[0]
    except:
        print ''        
    try:
        s2 = s1.split().pop()
    except:
        print ''
    s3 = ''
    for c in s2:
        if c.isdigit():
            s3 = s3 + c
    return int(s3)
''' ====================== TEST ====================== '''
''' === Login === '''
login_url = 'http://www.archives.com/member/'
acc_pwd = {'__uid':'sanhe.hu@theeagleforce.net','__pwd':'diablo1987'}
cj = cookielib.CookieJar() ## add cookies
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj)) ## build opener
opener.addheaders = [('User-agent','Mozilla/5.0 \
                    (compatible; MSIE 6.0; Windows NT 5.1)')] ## browser header
data = urllib.urlencode(acc_pwd) ## encode login acc and pwd
try: ## handle login connection time out
    opener.open(login_url,data,10)
    print 'log in - success!'
except:
    print 'log in - times out!', login_url

''' === start crawl === '''
with open('lastnamelist.txt', 'r') as f:
    lastnamelist = f.read().strip().split('\n')
    
state = ''
activityID = '3a65528f-fbd4-4161-9217-957cc8c51187'
pagesize = 10
pagenumber = 1

fname = 'taskplan.txt'

f = open(fname, 'r')
tasklist = f.read()
f.close()

for lastname in lastnamelist:
    for state in statelist:
        url = DR_url_gen(lastname, state, activityID, pagesize, pagenumber)
        print url
        if (lastname + '\t' + state) not in tasklist:
            try: ## handle open url connection time out
                content = opener.open(url, data, 10).read()
            except: ## if time out, return NA
                print 'open url - times out', url
                content = 'NA'
            if content != 'NA': ## if NA skip
                record_amount = find_amount_of_record_by_content(content)
                ''' append one lastname, state pair '''
                with open(fname, 'a') as f:
                    f.write(lastname + '\t' + state + '\t' + str(record_amount) + '\n')
                    print 'finishing: ', lastname + '\t' + state + '\t' + str(record_amount), url
        else:
            pass
#             print lastname, state, ' is already in the task plan'

f.close()
print ' ============== Task Planner Complete! ============== '