##coding=utf8
# -Map from Disease to Drug-
# -Time to take effect
# -Warnings
# -Interactions with other drugs
# -Dosages
# -Side Effects
import os
import re
import bs4
def step1():
    root = 'data'
    os.chdir(root)
    drugnamelist = list()
    brandnamelist = list()
    for name in os.listdir(os.getcwd()):
        if ('(' in name) & (')' in name):
            drugname, brandname = name.split('(',1)
            drugname = drugname.strip()
            brandname = brandname.strip()
            brandname = brandname[:-1]
            brandname = brandname.strip()
            print drugname, brandname
        else:
            drugname = name.strip()
            brandname = ''
        drugnamelist.append(drugname)
        brandnamelist.append(brandname)
    
def step2():
    root = 'C:\Users\Sanhe Hu\workspace\EagleForce\WebCrawler_FDAdrug\data\Albenza (Albendazole)'
    os.chdir(root)
    for fname in os.listdir(os.getcwd()):
        with open(fname, 'rb') as f:
            content = f.read()
            soup = bs4.BeautifulSoup(content)
            for tag in soup.find_all('h3'):
                print tag
    
    fname = r'C:\Users\Sanhe Hu\workspace\EagleForce\WebCrawler_FDAdrug\data\Albenza (Albendazole)\clinical-pharmacology.htm'
    with open(fname, 'rb') as f:
        content = f.read()
        soup = bs4.BeautifulSoup(content)
        for tag in soup.find_all('h5'):
            print tag.text

def index1_disease_to_drug():     
    root = r'C:\Users\Sanhe.Hu\Data_warehouse\FDA_drugs\data'
    os.chdir(root)
    counter = 0
    for name in os.listdir(os.getcwd()):
        for fname in os.listdir(name):
            if fname == 'consumer-uses.htm': ## search in c
                counter += 1
                dst = os.path.join(name, fname)
                with open(dst, 'rb') as f:
                    content = f.read()
                    soup = bs4.BeautifulSoup(content)
                    text = soup.text.lower()
                    lines = text.split('\n')
                    for line in lines:
#                         if 'pleural effusion' in line:
#                             print dst, line
                        if 'uses:' in line:
                            if 'multiple sclerosis' in line:
                                print dst, line

index1_disease_to_drug()
                                
def index2_dosage():
    root = 'C:\Users\Sanhe.Hu\Data_warehouse\FDA_drugs'
    os.chdir(root)
    counter1 = 0
    counter2 = 0
    for name in os.listdir(os.getcwd()):
        for fname in os.listdir(name):
            if fname == 'indications-dosage.htm': ## search in c
                dst = os.path.join(name, fname)
                with open(dst, 'rb') as f:
                    content = f.read()
                    soup = bs4.BeautifulSoup(content)
                    text = soup.text.lower()
                    if 'DOSAGE AND ADMINISTRATION'.lower() in text:
                        if 'HOW SUPPLIED'.lower() in text:
                            counter1 += 1
                        else:
                            counter2 += 1
                            print dst
    print counter1, counter2
    
index2_dosage()

# 'albuminar (albumin (human))'