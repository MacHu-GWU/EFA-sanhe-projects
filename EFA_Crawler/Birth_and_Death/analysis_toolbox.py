import bs4
import os
import re
import csv
from datetime import datetime

''' Pre Analysis Module '''
def print_all_possible_field():
    '''
        find all possible useful field name
        currently they are: [ 'Name:', 'Birth Date:', 'Death Date:','Location:','Collection:']
    '''
    fieldset = set() 
    os.chdir('data')
    path = os.getcwd()
    for fname in os.listdir(path):
        with open(fname, 'r') as f:
            soup = bs4.BeautifulSoup(f.read())
        ''' ================== '''
        for tag in soup.find_all('div'):
            if 'class' in tag.attrs: ## <div class="position"> or <div class="fieldValue">
                if 'field' == tag['class'][0]:
                    fieldset.add(tag.string.strip())
    print fieldset
    return None

# print_all_possible_field()
