##coding=utf8

from tools.crawler import Crawler, QueryString, SparseInterval, ToDo, Finished
from tools._ref_data import lastnamelist
from datetime import datetime
import pprint
import re
import os, shutil
import faker
import hashlib

def unit_test():
    '''测试hash的重复性
    '''
    res = list()
    for i in xrange(50000):
        fake = faker.Factory.create()
        firstname = fake.first_name()
        lastname = fake.last_name()
        dob = fake.date()
        dod = fake.date()
        location = fake.address()
        org = fake.company()
        
#         res.append( hash( (firstname, lastname, dob, dod, location, org) ) )
        h = hashlib.new('md5', '%s%s%s%s%s%s' % (firstname, lastname, dob, dod, location, org)) ## hashlib.new(algorithm, string)
        hashvalue = h.hexdigest()
        print type(hashvalue)
        
        
        
    print len(res)
    print len(set(res))
    
if __name__ == '__main__':
    unit_test()


# url = 'http://www.archives.com/member/Default.aspx?_act=VitalSearchResult&LastName=Smith&Country=US&State=AK&RecordType=2&DeathYear=2013&activityID=3a65528f-fbd4-4161-9217-957cc8c51187&ShowSummaryLink=1&pagesize=10&pageNumber=1&pagesizeAP=10&pageNumberAP=1'
# html = spider.html(url, 10)
# print find_amount_of_record_by_html(html), url

print 'COMPLETE at %s' % datetime.now()