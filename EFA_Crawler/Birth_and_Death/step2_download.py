import urllib2
import urllib
import cookielib ## cookies
import os
import random
from Discrete_Interval import *
''' history generator '''
##############################################
def get_all_file_path(path): ## Don't forget to import os
    '''
        return all file's path under a folder
    '''
    filepathlist = list()
    for folder in os.walk(path):
        for fname in folder[2]:
            fpath = folder[0]+'\\'+fname
            filepathlist.append(os.path.abspath(fpath))
    return filepathlist

def fname_parse(fname):
    ''' Example Input Output:
        Input: data\\John_AK_1.txt
        Output:
            lastname = John
            state = AK
            startnum = 1
    '''
    fname = fname.split('\\').pop()
    lastname, state, startnum = fname.split('_')
    startnum = startnum.replace('.txt','')
    return lastname, state, startnum
##############################################
def interval_to_tuple(interval):
    (a,b) = tuple(interval.split('-'))
    return (int(a),int(b))

def generate_history(path): 
    '''
        given a path, generate history, it's a dict
        keys = lastname + '-' + state
        value = Discrete_Interval
    '''
    filepathlist = get_all_file_path(path)
    history = dict()
    for fname in filepathlist:
        lastname, state, interval = fname_parse(fname)
        if lastname+'_'+state in history:
            history[lastname+'_'+state].append(interval_to_tuple(interval))
        else:
            history[lastname+'_'+state] = [interval_to_tuple(interval)]
    for key in history:
        history[key] = Discrete_Interval(history[key])
    return history

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
    except:
        print 'time out!', url
        return 'NA'
    return content

''' ====== test ====== '''
''' === Login === '''
login_url = 'http://www.archives.com/member/'
acc_pwd = {'__uid':'sanhe.hu@theeagleforce.net','__pwd':'diablo1987'}
cj = cookielib.CookieJar() ## add cookies
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj)) ## build opener
opener.addheaders = [('User-agent','Mozilla/5.0 \
                    (compatible; MSIE 6.0; Windows NT 5.1)')] ## browser header
data = urllib.urlencode(acc_pwd) ## encode login acc and pwd
try: ## handle login connection time out
    opener.open(login_url,data, 10)
    print 'log in - success!'
except:
    print 'log in - times out!', login_url
''' === start crawling === '''
history = generate_history('data') ## history
fname = 'taskplan.txt'
f = open(fname, 'rb') ## <open>
planlist = f.read().strip().split('\n')
f.close() ## <close>
random.shuffle(planlist)

f = open('taskplan_failed.txt', 'rb') ## <open>
failedlist = f.read().strip().split('\n')
f.close() ## <close>


activityIDlist = ['f25ae3eb-db4e-4aad-89ec-ae9f2c314020',
                  'a3917be7-2750-4e39-ad26-8ff82d55d732',
                  '3e5da5c0-7d1b-479a-8530-a13d4b1d5a36',
                  '3a65528f-fbd4-4161-9217-957cc8c51187'
                  ]
for plan in planlist:
    lastname, state, amount = plan.split('\t')
    lastname = lastname.lower()
    lastname = lastname[0].upper() + lastname[1:]
    pagesize = 250
    amount = int(amount)/pagesize + 1
    for i in range(int(amount)):
        random.shuffle(activityIDlist)
        activityID = activityIDlist[0]
        url = DR_url_gen(lastname, state, activityID, pagesize, i+1)
        fname = 'data\\' + lastname + '_' + state + '_' + str(i*pagesize+1)+'-'+str((i+1)*pagesize) + '.txt'
        qujian = Discrete_Interval([(i*pagesize+1,(i+1)*pagesize)])
        ### urlopen or not logic check
        flagflag = 1
        if (lastname+'_'+state) in history: ## if already in, continue checking
            if qujian.overlap(history[lastname+'_'+state]): ## if overlap
                flagflag = 0
        if fname in failedlist:
            flagflag = -1
        
        if flagflag: ## if not overlap
            try: ## handle open url connection time out
                content = opener.open(url, None, 20).read()
                flag = 1
            except: ## if time out, return NA
                print 'open url - times out', url
                with open('taskplan_failed.txt', 'a') as f:
                    f.write(fname + '\n')
                flag = 0
            if flag == 1:
                with open(fname, 'wb') as f:
                    f.write(content)
                if os.path.getsize(fname) >= 200000:
                    print fname, ' is complete!', url
                else:
                    os.remove(fname)
                    print fname, ' is a bad file', url
        elif flagflag == 0: ## if already exist, skip
            print fname, 'already exist, skip'
        else:
            print fname, 'already failed, skip'

print 'Download source date complete!'
