##coding=utf8

import jsontree

def prt_jt(jt):
    return jsontree.dumps(jt, sort_keys=True,indent=4,separators=(',' , ': '))

def dump_jt(jt, fname):
    with open(fname, 'wb') as f:
        f.write(prt_jt(jt))

def load_jt(fname):
    with open(fname, 'rb') as f:
        return jsontree.loads(f.read())

def ignore_iter(dictionary, ignore):
    for key in dictionary:
        if key not in ignore:
            yield key
def main():
    task = load_jt('taskdata.py')
    
    for state in ignore_iter(task, ['url']):
        for city in ignore_iter(task[state], ['url']):
            for store in ignore_iter(task[state][city], ['url']):
                task[state][city][store]['hour'], task[state][city][store]['service'] = list(), list()
    
    dump_jt(task, 'taskdata.py')
        
main()