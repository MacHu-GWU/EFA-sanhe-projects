import os
def get_all_file_path(path): ## Don't forget to import os
    '''
        return all file's path under a folder
    '''
    filepathlist = list()
    for folder in os.walk(path):
        for fname in folder[2]:
            fpath = folder[0]+'\\'+fname
            filepathlist.append(os.path.abspath(fpath))
    return filepathlist

def fname_parse(fname):
    ''' Example Input Output:
        Input: data\\John_AK_1.txt
        Output:
            lastname = John
            state = AK
            startnum = 1
    '''
    fname = fname.split('\\').pop()
    lastname, state, startnum = fname.split('_')
    startnum = startnum.replace('.txt','')
    return lastname, state, startnum

'Smith_AL_1'
def rename(path):
    filepathlist = get_all_file_path(path)
    os.chdir(path)
    for fname in filepathlist:
        lastname, state, startnum = fname_parse(fname)
        interval = str(int(startnum)*1000-999)+'-'+str(int(startnum)*1000)
        newname = lastname + '_' + state + '_' + interval + '.txt'
        os.rename(fname, newname)

rename('data')
from Discrete_Interval import *
def generate_history(path): 
    '''
        given a path, generate history, it's a dict
        keys = lastname + '-' + state
        value = Discrete_Interval
    '''
    def interval_to_tuple(interval):
        (a,b) = tuple(interval.split('-'))
        return (int(a),int(b))
    
    filepathlist = get_all_file_path(path)
    history = dict()
    for fname in filepathlist:
        lastname, state, interval = fname_parse(fname)
        if lastname+'_'+state in history:
            history[lastname+'_'+state].append(interval_to_tuple(interval))
        else:
            history[lastname+'_'+state] = [interval_to_tuple(interval)]
    for key in history:
        history[key] = Discrete_Interval(history[key])
    return history

# print generate_history('data')['Smith_AL']

# qj1 = Discrete_Interval([(1,4),(8,12)])
# qj2 = Discrete_Interval([(5,7),(-100,1)])
# print qj2.overlap(qj1)
