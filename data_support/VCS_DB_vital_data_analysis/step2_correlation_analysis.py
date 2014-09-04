##coding=utf8
import numpy as np
from StringIO import StringIO
from datetime import datetime

def strptimelist(array, format):
    timelist = list()
    for i in array:
        timelist.append(datetime.strptime(i, format))
    return timelist
''' 读取数据 '''
with open('data.txt', 'rb') as f:
    data = np.genfromtxt( StringIO(f.read()),
                          delimiter = ',',
                          dtype = 'str')
[pID, tID, v, d] = data.transpose()
''' 处理数据格式 '''
pID = pID.astype('int')
tID = tID.astype('int')
v = v.astype('int')
d = strptimelist(d, '%m/%d/%Y %H:%M')
data = np.array([pID, tID, v, d]).transpose()
# print data
''' 分析数据 '''
''' 对7个测量值，两两配对进行关联性分析 '''
## 1. 根据时间获取共同的数据
def corrcoef_analysis(data, pID, tID1, tID2): 
    ## 因为coef需要向量长度一致，也就是每天必须同时对这两个变量有测量
    set1, set2 = set(), set()
    for row in data:
        if row[0] == pID: ## 如果是某个病人，才可以
            if row[1] == tID1:
                set1.add(row[3].date())
            elif row[1] == tID2:
                set2.add(row[3].date())
    greatest = set.intersection(set1, set2)
    ## 求各天的样本值向量
    co = [dict(), dict()]
    for row in data:
        if (row[0] == pID) & (row[1] in {tID1, tID2}) & (row[3].date() in greatest): ## 符合病人ID，并且时间互相匹配
            if row[1] == tID1:
                co[0][row[3].date()] = row[2]
            else:
                co[1][row[3].date()] = row[2]
    smp1 = co[0].values()
    smp2 = co[1].values()
#     print len(smp1)
    if len(smp1) == 0:
        return '-999'
    else:##同时把 相关系数 和 样本数储存起来
        coef = '%.2f' % np.corrcoef(np.array(smp1), np.array(smp2))[0][1]
#         coef = coef + '_%s' % len(smp1)
        return coef

# print corrcoef_analysis(data, 1, 1, 3)

for pID in range(48):
    pID = pID + 1
    print pID
    n = 7
    coe_matrix = np.zeros((n,n)).astype('str')
    for i in range(n):
        for j in range(n):
            aaa =  corrcoef_analysis(data, pID, i+1, j+1)
            coe_matrix[i][j] = aaa
    print coe_matrix
    np.savetxt('corrcoef' + str(pID).zfill(2) + '.csv', ## 文件名
               coe_matrix,  ## 数据
               fmt='%s', ## 定义格式， fmt = format  %.2f = 小数点后保留2位
               delimiter = ',',
               header = 'Blood Glucose, Diastolic, Heart Rate, Oxygen, Systolic, Temp, Weight') ## 定义分隔符