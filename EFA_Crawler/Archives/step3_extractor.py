##coding=utf8
import re
import bs4
import os
import hashlib
from datetime import datetime, date

def process_fullname(fullname, lastname):
    '''split lastname and firstname
    Input: fullname = Johnnie L. John II, lastname = John
    Output: firstname = Johnnie L.
    '''
    namepiece = fullname.split(lastname)
    namepiece.pop()
    firstname = lastname.join(namepiece).strip()
    return firstname
    
def process_date(datestring):
    '''change the date format from "Jan 3, 2012" to "2012-01-03"
    '''
    return datetime.strftime(datetime.strptime(datestring, '%b %d, %Y'), '%Y-%m-%d')

def process_location(location):
    '''split location and state
    '''
    locpiece = location.split(',')
    state = locpiece.pop().strip()
    return location, state
    
def records_generator(text, lastname):
    '''Given a text, iterately generate:
             #lastname, #firstname, #bod, #dod, #location, #state, #source
    '''
    for line in text.split('\n'):
        if '<div class="searchColRight">' in line:
            line = line.strip().replace('</script></div>', '')
            soup = bs4.BeautifulSoup(line)

    for entry in soup.findAll('div', attrs = {'class': 'resultsRow vital-record-row clearfix'}):
        
        row = list() 
        for field in entry.findAll('div', attrs = {'class': 'fieldValue'}):
            row.append(field.text)
            
        try: # pre process data format
            fullname, bod, dod, location, source, = row[0], row[1], row[2], row[3], row[4] # !! sometime it raise error.
            firstname = process_fullname(fullname, lastname) # split lastname and firstname !! sometime it raise error.
            bod, dod = process_date(bod), process_date(dod) # change format of date !! sometime it raise error.
            location, state = process_location(location) # split location and state !! sometime it raise error.
            if bod <= dod:
                yield firstname, bod, dod, location, state, source
        except:
            pass

def main():
    fname = '2014y-08m-26d 10h_05m_48s.html'
    with open(fname, 'rb') as f:
        text = f.read()
    
    lastname = 'Smith'
    for firstname, bod, dod, location, state, source in records_generator(text, lastname):
        id = hashlib.md5(','.join((lastname, firstname, bod, dod, location, state, source)) ).hexdigest()
        print (id, lastname, firstname, bod, dod, location, state, source)
        
if __name__ == '__main__':
    main()
