##coding=utf8
##By. Sanhe 2014-06-09
##[标题] 如何把数据保存为txt或csv文件

import numpy as np

fname1 = 'dump_data1.txt' ## 如果要存成csv，只需要改变扩展名为csv即可
fname2 = 'dump_data2.txt' ## 如果要存成csv，只需要改变扩展名为csv即可

''' 本例中，数字的精度被改变成小数点后保留2位'''
data1 = np.array([[1.111,2.222,3.333],
                 [4.444,5.555,6.666],
                 [7.777,8.888,9.999]])
np.savetxt(fname1, ## 文件名
           data1,  ## 数据
           fmt='%.2f', ## 定义格式， fmt = format  %.2f = 小数点后保留2位
           delimiter = ',', ## 定义分隔符
           header = 'one, two, three') ## 定义表头

''' 本例中，数字都被当成字符串储存了 '''
data2 = np.array([[1.111,2.222,'three'],
                 [4.444,5.555,'six'],
                 [7.777,8.888,'nine']])
np.savetxt(fname2, data2, fmt = '%s', delimiter = ',') ## %s 保存为字符串

# 更多资料请参考
# numpy.savetxt介绍: http://docs.scipy.org/doc/numpy/reference/generated/numpy.savetxt.html