##coding=utf8
import numpy as np
from StringIO import StringIO
import matplotlib.pyplot as plt

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


labeldict = {1: 'Blood Glucose',
             2: 'Diastolic',
             3: 'Heartrate',
             4: 'Oxygen',
             5: 'Systolic',
             6: 'Temperature',
             7: 'Weight',}

for pID in range(1,49):
    pdata = data_to_patient(pID, data) ## 选择病人
    fig = plt.figure(1)
    ax  = fig.add_subplot(111)
    ax.set_position([0.1,0.1,0.6,0.8])
    label = list()
    for i in range(7):
        i += 1
        tdata = patient_to_mtype(i, pdata)
        x, y = tdata.transpose()[2], tdata.transpose()[1]
        if len(x) > 0:
            x = np.array(datetime_string_converter(x))
            if i == 7: ## 如果是体重，直接去除奇怪的数字
                ind = np.where(y >= 80 )[0]
                x, y = x[ind], y[ind]
            y_mean, y_std = y.mean(), y.std() ## 去除outlier
            ind = np.where( abs(y- y_mean) <= (2.5 * y_std) )[0]
            x, y = x[ind], y[ind]
            plt.plot(x,y, '-o', linewidth = 2, )
            label.append(labeldict[i])
    plt.xlabel('date')
    plt.ylabel('vital sign value')
    leg = ax.legend(label,
                     loc = 'center left',
                     bbox_to_anchor = (1.0, 0.8))
    ax.tick_params(axis='both', which='major', labelsize=6)
#     ax.tick_params(axis='y', which='minor', labelsize=6)
    
#     plt.show()
    fig.savefig(str(pID).zfill(2) + '.png')
    plt.clf()
