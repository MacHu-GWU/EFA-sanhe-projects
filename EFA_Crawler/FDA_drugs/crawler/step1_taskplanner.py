##coding=utf-8
from toolbox_urlopener import url_to_soup
import pickle
import os
''' ============ layer1 url =========== '''
def layer1_url_generator(): ## Durg A-Z, entrance url generator
    ''' Output:
    ['http://www.rxlist.com/drugs/alpha_a.htm', 'http://www.rxlist.com/drugs/alpha_b.htm', ... ]
    '''
    head = 'http://www.rxlist.com/drugs/alpha_'
    tail = '.htm'
    layer1_urllist = list()
    for i in range(97,123): ## from ord('a') to ord('b') (97,123)
        layer1_urllist.append(head + chr(i) + tail)
    return layer1_urllist

''' ============ layer2 url =========== '''
def layer2_url_generator(url):
    ''' Output
    dict{ 'http://www.rxlist.com/a-methapred-drug.htm' : 'A-Methapred (Methylprednisolone Sodium Succinate)' }
    '''
    head = 'http://www.rxlist.com'
    layer2_drug_url_dict = dict()
    soup = url_to_soup(url, 20)
    if soup != None:
        for tag in soup.find_all('li'):
            if tag.span != None:
                if 'FDA' in tag.span.string:
                    layer2_drug_url_dict[head + tag.a['href']] = tag.a.string
        return layer2_drug_url_dict
    else:
        return layer2_drug_url_dict

''' ============ MAIN ============ '''
def step1_main():
    ''' OUTPUT: drugdict = {drugurl, drugname}, from A to Z '''
    ''' <1> load local file '''
    if os.path.exists('drugdict.p'): ## if exist, then load
        with open('drugdict.p', 'rb') as f:
            drugdict = pickle.load(f)
    else: ## if not exist, creat one
        drugdict = dict()
    print 'Already have', len(drugdict), 'drugs in our plan.' ## <FOR DEBUG>
    ''' <2> RE, get drugpage '''
    for alphaurl in layer1_url_generator():
        newdict = layer2_url_generator(alphaurl)
        drugdict.update(newdict)
        print 'downloading drug in: ', alphaurl
    ''' <3> save to local file '''
    drugdict = eval(repr(drugdict)) ## !! if don't do this, cannot dump to pickle. Don't know why.
    pickle.dump(drugdict, open('drugdict.p', 'wb'))
    print 'Complete. We got', len(drugdict), 'drugs to crawl'