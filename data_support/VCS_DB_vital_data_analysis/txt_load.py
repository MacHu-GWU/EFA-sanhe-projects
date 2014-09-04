##coding=utf8
##By. Sanhe 2014-06-09
##[标题] 如何从txt文件中读取数据

import numpy as np
from StringIO import StringIO

fname1 = 'data1.txt' ## 如果要从csv文件中读取，只需要改变扩展名为csv即可
fname2 = 'data2.txt' ## 如果要从csv文件中读取，只需要改变扩展名为csv即可
''' 本例中，数字被读成了字符串，所以会有'4'这样的东西出现 '''
with open(fname1, 'rb') as text:
    data = np.genfromtxt(   StringIO(text.read()), 
                            delimiter=",", ## 定义分隔符
                            dtype = 'str', ## 定义数据类型
                            skiprows = 1, ## 从头跳过若干行
                            skip_header = 0, ## 跳过第一行标题
                            skip_footer = 0) ## 跳过最后一行注脚
    print data
''' 本例中，字符串被强制转化成了float，所以最后数据中会有 nan '''
with open(fname2, 'rb') as text:
    data = np.genfromtxt(   StringIO(text.read()), 
                            delimiter=",", ## 定义分隔符
                            dtype = 'float', ## 定义数据类型
                            skiprows = 1, ## 从头跳过若干行
                            skip_header = 0, ## 跳过第一行标题
                            skip_footer = 0) ## 跳过最后一行注脚
    print data
    
# 更多参考资料请参考：
# numpy.genfromtxt定义: http://docs.scipy.org/doc/numpy/reference/generated/numpy.genfromtxt.html
# numpy.genfromtxt技巧: http://docs.scipy.org/doc/numpy/user/basics.io.genfromtxt.html