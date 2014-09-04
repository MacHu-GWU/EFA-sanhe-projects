##coding=utf8
import numpy as np
from StringIO import StringIO
from datetime import datetime
import matplotlib.pyplot as plt
from sklearn import preprocessing

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

def clean_outlier(y, e = 3):
    while 1:
        m = y.mean()
        std = y.std()
        ind = np.where( abs(y - m) <= (std * e) )
        if len(ind[0]) == len(y):
            break
        else:
            y = y[ind]
    return y

with open('data_IntDate_sorted.txt', 'rb') as f:
    data = np.genfromtxt( StringIO(f.read()),
                          delimiter = ',',
                          dtype = 'float')
[pID, tID, v, d] = data.transpose()
pID = pID.astype('int')
tID = tID.astype('int')
newdata = np.array([pID, tID, v, d]).transpose()

tID = 1 ## !!
ind = np.where(newdata.transpose()[1] == tID)
tdata = newdata[ind]
## BLOOD GLUCOSE normal range (70-100)

res = list()
for pID in range(1,49):
    ind = np.where(tdata.transpose()[0] == pID)
    pdata = tdata[ind]
    array = pdata.transpose()[2] ##
#     print array
    if len(array) != 0: ## 如果数据这个病人就没有这个数据就算了
        if tID == 7: ## 如果是体重，直接去除奇怪的数字
            ind = np.where(array >= 80 )[0]
            array = array[ind]
        array = clean_outlier(array)
        res.append(np.array(array).mean())
    print '%s of patients have %s type measurement' % (len(res), tID)
x = np.arange(1, len(res)+1)
plt.plot(x, res, 'o')
plt.xlabel('patients_ID')
plt.ylabel('Weight mean value')
# labeldict = {1: 'Blood Glucose',
#              2: 'Diastolic',
#              3: 'Heartrate',
#              4: 'Oxygen',
#              5: 'Systolic',
#              6: 'Temperature',
#              7: 'Weight',}
plt.show()