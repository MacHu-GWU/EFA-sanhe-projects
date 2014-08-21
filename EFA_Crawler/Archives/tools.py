##coding=utf8
def querystring(lastname, country, state, recordtype, year, activityID, pagesize, pagenumber):
    template = dict()
    template['2'] = \
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
    query = template[recordtype] % (lastname,
                                    country,
                                    state,
                                    recordtype,
                                    year,
                                    activityID,
                                    pagesize,
                                    pagenumber)
    return query

if __name__ == '__main__':
    lastname = 'Hanson'
    country = 'US'
    state = 'FL'
    recordtype = '2'
    year = '2010'
    activityID = '6829f573-ef51-464f-ab59-b01df1bf8828'
    pagesize = '10'
    pagenumber = '1'
    
    print querystring(lastname, country, state, recordtype, year, activityID, pagesize, pagenumber)
