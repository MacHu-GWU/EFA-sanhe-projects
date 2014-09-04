##coding=utf8
import numpy as np
from StringIO import StringIO
from datetime import datetime
import matplotlib.pyplot as plt
from sklearn import preprocessing

# a = np.array([1,2,3,4])
# print np.diff(a)
# 
# fig = plt.figure(1)
# ax  = fig.add_subplot(111)
# plt.plot(a)
# plt.show()

def data_to_patient(pID, data):
    res = list()
    for row in data:
        if row[0] == pID:
            res.append(row[1:])
    return np.array(res)

def patient_to_mtype(tID,pdata):
    ind = np.where(pdata.transpose()[0] == tID)
    return pdata[ind]

def datetime_string_converter(array):
    import datetime, time
    res = list()
    if type(array[0]) == type(datetime.datetime(2000,1,1)): ## datetime to int
        for i in array:
            res.append( time.mktime(i.timetuple()) )
    else: ## int to datetime
        for i in array:
            res.append( datetime.datetime.fromtimestamp(i) )
    return res

with open('data_IntDate_sorted.txt', 'rb') as f:
    data = np.genfromtxt( StringIO(f.read()),
                          delimiter = ',',
                          dtype = 'float')
[pID, tID, v, d] = data.transpose()
pID = pID.astype('int')
tID = tID.astype('int')
newdata = np.array([pID, tID, v, d]).transpose()

tID = 1
ind = np.where(newdata.transpose()[1] == tID)
tdata = newdata[ind]

for pID in range(1,49):
    ind = np.where(tdata.transpose()[0] == pID)
    pdata = tdata[ind]
    x, y = pdata.transpose()[3], pdata.transpose()[2]
    if len(x) != 0:
        x = np.array(datetime_string_converter(x))
        if tID == 7: ## 如果是体重，直接去除奇怪的数字
            ind = np.where(y >= 80 )[0]
            x, y = x[ind], y[ind]
        y_mean, y_std = y.mean(), y.std() ## 去除outlier
        ind = np.where( abs(y- y_mean) <= (2.5 * y_std) )[0]
        x, y = x[ind], y[ind]
        plt.plot(x,y)
        
    
plt.show()

