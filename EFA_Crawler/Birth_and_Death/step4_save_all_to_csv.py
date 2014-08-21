import os
import csv
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

''' ====== function 2 ====== '''
def fname_parse(fname):
    ''' Example Input Output:
        Input: data\\John_AK_1.txt
        Output:
            lastname = John
            state = AK
            startnum = 1
    '''
    fname = fname.split('\\').pop()
    lastname, state, interval = fname.split('_')
    interval = interval.replace('.txt','')
    return lastname, state, interval

def interval_to_tuple(interval):
    (a,b) = tuple(interval.split('-'))
    return (int(a),int(b))

filepathlist = get_all_file_path('smalldata')
amount = len(filepathlist)
for fname in filepathlist:
    print 'we got ', amount , ' file to process'
    amount -= 1
    lastname, state, interval = fname_parse(fname)
    with open(fname, 'r') as f:
        for line in f:
            row = line.strip().split('\t')
            with open('csv\\' + lastname + '.csv', 'a') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter='\t', lineterminator='\n')
                spamwriter.writerow(row)

print 'Complete!'

