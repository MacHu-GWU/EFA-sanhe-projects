##coding=utf8
import os
import bs4

def index1_disease_to_drug(diseasename):
    root = 'C:\Users\Sanhe Hu\workspace\EagleForce\WebCrawler_FDAdrug\data'
    os.chdir(root)
    for name in os.listdir(os.getcwd()):
        for fname in os.listdir(name):
            if fname == 'consumer-uses.htm': ## search in uses
                dst = os.path.join(name, fname)
                drugname = dst.split('\\')[0]
                with open(dst, 'rb') as f:
                    content = f.read()
                    soup = bs4.BeautifulSoup(content)
                    text = soup.text
                    lines = text.split('\n')
                    flag = 0
                    msg = list()
                    ## Content Analysis
                    for line in lines:
                        if flag:
                            if line[0:3] == line[0:3].upper():
                                print '\n', drugname ## print drugname
                                for l in msg: ## print USAGE info
                                    print '\t', l                                
                                break ## prepare to output
                            else:
                                msg.append(line)
                        if line.startswith('USES:'):
                            if diseasename.lower() in line.lower():
                                msg.append(line)
                                flag = 1
                            
index1_disease_to_drug('copd')
