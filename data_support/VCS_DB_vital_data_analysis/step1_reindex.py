##coding=utf8
import numpy as np
from StringIO import StringIO

def reindex(array,sortflag = 0):
    array = np.array(array)
    uni = np.unique(array)
    if sortflag:
        uni.sort()
    oldnewdict = dict()
    mapzip = zip(uni, range(1,len(uni)+1))
    for i,j in mapzip:
        oldnewdict[i] = j
        print i,j
    def mapindex(ind):
        return oldnewdict[ind]
    return map(mapindex, array), mapzip

with open('data_original.csv', 'rb') as f:
    data = np.genfromtxt( StringIO(f.read()),
                          delimiter = ',',
                          dtype = 'str',
                          skip_header = 1)

[pID, tID, v, d] = data.transpose()

pID, pIDzip = reindex(pID, 1)
tID, tIDzip = reindex(tID, 1)
newdata = np.array([pID, tID, v, d]).transpose()
'''
[('Blood Glucose', 1), 
('Diastolic Blood Pressure', 2), 
('Heart Rate', 3), 
('Oxygen Saturation Percentage', 4), 
('Systolic Blood Pressure', 5), 
('Temperature', 6), 
('Weight', 7)]
'''
print pIDzip
print tIDzip
# np.savetxt('data.txt', ## 文件名
#            newdata,  ## 数据
#            fmt='%s', ## 定义格式， fmt = format  %.2f = 小数点后保留2位
#            delimiter = ',')
# np.savetxt('data1.csv', ## 文件名
#            newdata,  ## 数据
#            fmt='%s', ## 定义格式， fmt = format  %.2f = 小数点后保留2位
#            delimiter = ',',
#            header = 'pID, tID, Value, datetime')

    