##coding=utf8
import os
import numpy as np
from StringIO import StringIO

    
root = 'coef_data'
os.chdir(root)


i = 1
j = 2
def coef_ana(i,j):
    coeflist = list()
    for fname in os.listdir(os.getcwd()):
        with open(fname, 'rb') as f:
            data = np.genfromtxt( StringIO(f.read()),
                                  delimiter = ',',
                                  dtype = 'float',
                                  skip_header = 1)
            if data[i][j] >= -900:
                coeflist.append(data[i][j])
    coeflist = np.array(coeflist)
    print coeflist
    return coeflist.mean(), len(coeflist)

n = 7
res_m = np.zeros((n,n),dtype = 'float')
res_s = np.zeros((n,n),dtype = 'int')

for i in range(n):
    for j in range(n):
        m, s = coef_ana(i,j)
        res_m[i][j] = m
        res_s[i][j] = s
print res_m
print res_s

np.savetxt('1.csv', ## 文件名
           res_m,  ## 数据
           fmt='%s', ## 定义格式， fmt = format  %.2f = 小数点后保留2位
           delimiter = ',')
np.savetxt('2.csv', ## 文件名
           res_s,  ## 数据
           fmt='%s', ## 定义格式， fmt = format  %.2f = 小数点后保留2位
           delimiter = ',') 