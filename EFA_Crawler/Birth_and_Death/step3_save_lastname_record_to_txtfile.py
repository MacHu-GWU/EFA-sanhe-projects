import bs4
import os
from datetime import datetime
''' ====== function 1 ====== '''
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

''' ====== function 2 ====== '''
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

def interval_to_tuple(interval):
    (a,b) = tuple(interval.split('-'))
    return (int(a),int(b))

''' ====== function 3 ====== '''
def soup_generator(filepathlist):
    for fname in filepathlist:
        lastname, state, interval = fname_parse(fname)
        (a,b) = interval_to_tuple(interval)
        ''' load one file, find the target line '''
        with open(fname, 'rb') as f:
            for line in f:
                if ('<div class="position">' + str(a) + '</div>') in line:
                    target = line ## !! Got the right line
                    soup = bs4.BeautifulSoup(target)
                    yield (lastname, state, interval, soup)

''' ====== function 4 ====== '''
def record_generator(state, soup):
    ''' 
    Example Output:
        {u'Location:': u'Venetie, AK', u'Death Date:': u'Sep 15, 1994', u'Name:': u'Silas John', 
        u'Collection:': u'Social Security Death Index', u'Birth Date:': u'Dec 25, 1903'}
    '''
    tmprecord = {'state': state}
    record = tmprecord ## initialization
    for tag in soup.find_all('div'):
        if 'class' in tag.attrs: ## <div class="position"> or <div class="fieldValue">
            if 'position' == tag['class'][0]: ## Ready to get one people record
                if len(record) > 1: # if record not empty, yield
                    yield record ## @@@@ GENERATE !!!!
                    record = tmprecord
#                     print record
            if 'field' == tag['class'][0]:
                key = tag.string.strip()
                if key != '':
                    flag = 1
            if 'fieldValue' == tag['class'][0]:
                if flag == 1:
                    try:
                        record[key] = tag.string.strip() ## sometime there's a subtag <a>
                        flag = 0
                    except:
                        flag = 0
                    try:
                        record[key] = tag.a.string.strip()
                        flag = 0
                    except:
                        flag = 0

''' ====== function 5 ====== '''              
def splitname(fullname):
    ''' Example Input Output
        Input: Johnnie L. John
        Output: lastname = Johnnie L.    firstname = John
    '''
    namepiece = fullname.split()
    lastname = namepiece.pop()
    firstname = ''.join(namepiece)
    return lastname, firstname

''' ====== function 6 ====== '''               
def record_parse(record):
    ''' === Get rid of bad data, and reformat good data === 
        if it have:
            1. Valid lastname and firstname
            2. Valid date of birth
            3. Valid date of death
        Then output formated record
    '''
    fullname = record.get('Name:')
    dob = record.get('Birth Date:')
    dod = record.get('Death Date:')
    location = record.get('Location:')
    collection = record.get('Collection:')
#     print fullname , dob, dod, location, collection ## %%% for test
    try: ## get name =============================================
        lastname, firstname = splitname(fullname)
        flagname = 1
    except:
        flagname = 0
    try: ## get dob ==============================================
        dob = datetime.strptime(dob, '%b %d, %Y')
        flagdob = 1
    except:
        try:
            dob = datetime.strptime(dob, '%Y')
            flagdob = 1
        except:
            flagdob = 0
    try: ## get dod ===============================================
        dod = datetime.strptime(dod, '%b %d, %Y')
        flagdod = 1
    except:
        try:
            dod = datetime.strptime(dod, '%Y')
            flagdod = 1
        except:
            flagdod = 0
    if location == None: ## get death location ====================    
        location = record['state'] ## if death location not known, assign the state to it
    if collection == None: ## get data source info ================
        collection = 'Unknown'
#             print flagname,flagdob,flagdod ## %%% for test
    if (flagname & flagdob & flagdod) == 1: ## caculate age =======
        y, d = divmod((dod-dob).days, 365)
        age = str(y) + ' years ' + str(d) + ' days' ## final age
        row = [lastname, firstname, str(dob.date()), str(dod.date()), age, location, collection]
        return row
    return None

''' ====== MAIN function ====== '''
path = 'data'
filepathlist = get_all_file_path(path)
for souptuple in soup_generator(filepathlist): ## generator
    (lastname, state, interval, soup) = souptuple
    for record in record_generator(state, soup): ## generator
        row = record_parse(record)
        if row != None:
            with open('smalldata\\' + lastname + '_' + state + '_' + interval + '.txt', 'a') as f:
                f.write('\t'.join(row)+'\n')
    with open('data\\' + lastname + '_' + state + '_' + interval + '.txt', 'wb') as f:
        pass
    print lastname, state, ' records complete!'
            
print 'COMPLETE!'