##coding=utf-8
from toolbox_urlopener import url_to_content
import pickle
import os
import re

''' Extract the body '''
def content_to_body(content): ## Extract the body of content, delete AD, Menu, Navigator infomation
#     content = str(soup)
    pbody = re.compile(r'(?<=<!-- start pages here -->)([\s\S]*)(?=<!-- end pages here -->)')
    try:
        body = re.findall(pbody,content)[0]
        return body
    except:
        return 'None'

''' OUTPUT: 
drug_subcategory = {drugurl: {'drugname':, drugname
                              'pagelist':, [url1, url2, ... ]}
'''
def step3_main():
    ''' <1> load local file '''
    drug_subcategory = pickle.load(open('drug_subcategory.p', 'rb'))
    ''' Count how many page actually we have '''
    amount = 0
    for drug in drug_subcategory.itervalues():
        amount += len(drug['pagelist'])
    ''' <2> loop over all drugs '''
    os.chdir('data') ## set current dir.
    counter = 0
    for drug in drug_subcategory.itervalues():
        ''' <1> For one drug, create a directory '''
        drugname = drug['drugname']
        drugname = drugname.replace('/',' and ')
        drugname = drugname.replace('\t','')
        if not os.path.exists(drugname):
            print 'making directory: ', drugname
            os.makedirs(drugname)
        i = 1
        ''' <3> For one drug, loop over all pages'''
        for pageurl in drug['pagelist']:
            ''' (*) get correct file name to save '''
            if i == 1: ## if the first page, then must be durg-description.htm
                fname = drugname+'\\'+'durg-description.htm'
                i += 1
            else: ## get the subcategory from url
                fname = drugname+'\\'+ pageurl.split('/').pop() ## find the name
            ''' (*) 1. Check existence '''
            if os.path.exists(fname): ## if exist, pass
                print fname, 'Already crawlled, pass'
            else: ## if not exists, crawl it
                content = url_to_content(pageurl) ## <FUNCTION>
                ''' (*) 2. Check urlopen '''
                if content != None: ## if soup is good
                    body = content_to_body(content) ## <FUNCTION>
                    ''' (*) 3. Check body of content '''
                    if body != 'None': ## if successful to re to get the body, save it
                        with open(fname,'wb') as f:
                            f.write(body)
                        counter += 1
                        print 'success,', fname, counter, '//', + amount
                    else: ## if failed to re to get the body, 
                        print pageurl + '\t failed to extract body of content.'
                else:
                    print pageurl + '\t failed to open url.'