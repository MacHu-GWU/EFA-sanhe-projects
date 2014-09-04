##coding=utf-8
from toolbox_urlopener import url_to_soup
import pickle
import os
''' ============ layer3 url =========== '''
def layer3_url_generator(url):
    ''' Output
    ['http://www.rxlist.com/a-methapred-drug.htm', 'http://www.rxlist.com/a-methapred-drug/indications-dosage.htm', ... ]
    '''
    head = 'http://www.rxlist.com'
    pageurllist = list()
    soup = url_to_soup(url) ## <FUNCTION>
    if soup != None:
        for tag in soup.find_all('li'):
            if 'id' in tag.attrs:
                if 'pagination_top_' in tag['id']:
                    pageurllist.append(head+tag.a['href'])
        pageurllist = pageurllist[:len(pageurllist)/2]
    return pageurllist

''' ============ MAIN ============ '''
def step2_main():
    ''' OUTPUT: 
    drug_subcategory = {drugurl: {'drugname':, drugname
                                  'pagelist':, [url1, url2, ... ]}
    '''
    ''' <1> load local file '''
    if os.path.exists('drug_subcategory.p'):
        with open('drug_subcategory.p', 'rb') as f:
            drug_subcategory = pickle.load(f)
    else:
        drug_subcategory = dict()
    ''' <2> RE, get drugpage '''
    drugdict = pickle.load(open('drugdict.p', 'rb')) ## load drugdict = {drugurl, drugname}
    n = len(drugdict)
    for drugurl in drugdict:
        if drugurl not in drug_subcategory: ## if didn't crawled before
            pageurllist = layer3_url_generator(drugurl) ## <FUNCTION>
            if pageurllist != None: ## if urlopen failed, do nothing
                ''' <3> save to local file '''
                drug_subcategory[drugurl] = {'drugname':drugdict[drugurl], 
                                             'pagelist':pageurllist}
                pickle.dump(drug_subcategory, open('drug_subcategory.p', 'wb'))
            else:
                print drugurl, ' failed to crawl.'
        n -= 1
        print 'Still have', n, 'drug page to crawl.', drugurl
    print 'Complete. We suppose to get', len(drugdict), '. Now we get', len(drug_subcategory)