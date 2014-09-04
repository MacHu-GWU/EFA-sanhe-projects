##coding=utf8
import numpy as np
from StringIO import StringIO
from datetime import datetime
import matplotlib.pyplot as plt

def load_data():
    def strptimelist(array, format):
        timelist = list()
        for i in array:
            timelist.append(datetime.strptime(i, format))
        return timelist
    ''' 读取数据 '''
    with open('data.txt', 'rb') as f:
        data = np.genfromtxt( StringIO(f.read()),
                              delimiter = ',',
                              dtype = 'float')
    [pID, tID, v, d] = data.transpose()
    ''' 处理数据格式 '''
    pID = pID.astype('int')
    tID = tID.astype('int')
#     v = v.astype('float')
#     d = d.astype('int')
    data = np.array([pID, tID, v, d]).transpose()
    return data

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

data = load_data()
print data
pdata = data_to_patient(1, data)

# for i in range(1):
#     i += 1
#     tdata = patient_to_mtype(float(i), pdata)
#     print tdata
#     c1, c2, dtArray = tdata.transpose()
#     dtintArray = datetime_string_converter(dtArray)
#     inttdata = np.array([c1,c2,dtintArray], dtype = 'float')
#     inttdata = inttdata.transpose()
#     inttdata = inttdata.astype('float')
#     print inttdata
#     print np.sort(inttdata.view('float,float,float'), order=['f2'], axis=0).view(np.float)
    
    
    
    
    
#     x, y = tdata.transpose()[2], tdata.transpose()[1]
#     if len(x) > 0:
#         y_mean, y_std = y.mean(), y.std()
#         ind = np.where( abs(y- y_mean) <= 2.5*y_std )
#         x, y = x[ind], y[ind]
#         plt.plot(x,y)
#         plt.plot(x,y, '.')

# plt.show()
# for i in x:
#     print i
# print y
# temp = np.array([x,y]).transpose()
# print np.sort(temp.view('int,int'), order=['f0'], axis=0)


