##coding=utf8
import os
import bs4
def index1_disease_to_drug(disease_name):     
    root = 'data'
    os.chdir(root)
    counter = 0
    res = dict()
    for name in os.listdir(os.getcwd()):
        for fname in os.listdir(name):
            if fname == 'consumer-uses.htm': ## search in c
                counter += 1
                dst = os.path.join(name, fname) ## directory that contain usage information
                with open(dst, 'rb') as f:
                    content = f.read()
                    soup = bs4.BeautifulSoup(content)
                    text = soup.text.lower()
                    lines = text.split('\n')
                    for line in lines:
                        if 'uses:' in line:
                            if disease_name in line:
                                res[name] = line
    return res


# for k, v in index1_disease_to_drug('copd').iteritems():
#     print '%s\n\t%s\n' % (k,v)
import pickle

root = 'data'
os.chdir(root)
counter = 0
res = dict()
for name in os.listdir(os.getcwd()):
    for fname in os.listdir(name):
        if fname == 'consumer-uses.htm': ## search in c
            counter += 1
            dst = os.path.join(name, fname) ## directory that contain usage information
            with open(dst, 'rb') as f:
                content = f.read()
                soup = bs4.BeautifulSoup(content)
                text = soup.text.lower()
                lines = text.split('\n')
                for line in lines:
                    if 'uses:' in line:
                        res[line] = name

print len(res)
pickle.dump(res, open('uses_data.p', 'wb'))