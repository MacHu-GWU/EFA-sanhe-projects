##coding=utf8
'''sparseInterval类，简称spsI
普通的区间（本文中区间主要是指闭区间）是由一个lower和upper组成的，例如: [1,3]
而sparseInterval是由多个[lower,upper]对组成的，其中所有的子区间互不交叠。
这样就形成了一个离散的区间的集合，称之为"离散区间" - sparseInterval

这个类主要实现两种操作:
1. 包含有多个子区间的spsI 与 一个普通区间 做加法，也就是求交集
    例如:
        [(1, 2), (3, 4)] + (1.5, 3.5) = [(1, 4)]
        [(1, 2), (3, 4)] + (1.5, 2.5) = [(1, 2.5), (3, 4)]
        [(1, 2), (3, 4)] + (0.5, 3.2) = [(0.5, 4)]
        [(1, 2), (3, 4)] + (2.5, 2.8) = [(1, 2), (2.5, 2.8), (3, 4)]
    注,当有头尾刚好相等时:
        [(1, 2), (3, 4)] + (2, 2.5) = [(1, 2.5), (3, 4)]

2. 判断一个普通区间是否是spsI的子集
    功用: 爬虫程序中，spsI用于保存已经爬过的编号区间，该操作可以
    用于检测一个普通区间是否已被完全爬过

1. 离散区间 与 普通区间 加法的实现算法:
    我们把普通区间的上下限记做(lower, upper)
    我们定义:
        给定一个数x，对于离散区间中的每一个普通区间，如果有任意一个普通区间
        (lower, upper)使得 lower <= x < upper (注意开闭符号)，那么
        我们就称 x 在 离散区间"内"，反之称在 离散区间"外"
    
    我们发现，如果把离散区间的所有子区间从小到大排序，形成一个列表array，我们
    定义一个方法 index(x, array) 返回 x 所在array和正负无穷所形成的 2n+1
    个(离散区间有n个子区间)小区间的index序号，例如:
        index(2.3, [1,2,3,4]) = 3 因为 [-无穷, 1), [1, 2), [2, 3)
        注：之所以这里左边是闭区间，右边是开区间，是因为比如当x恰好等于2时，
            我们想要返回唯一的index，不希望存在歧义。
        
    我们可以证明：
        当index是奇数时，表示x落在离散区间外
        当index是偶数时，表示x落在离散区间内
        
    然后我们可以继续证明，离散区间 + 普通区间 = :
    例如：spsI = [(1, 2), (3, 4), (5, 6)]
        lower内，upper内，result =
            [:lower的前前一个] + [lower的前一个 - upper的后一个] + [upper的后后一个:]
        
        lower内，upper外，result =
            [:lower的前前一个] + [lower的前一个 - upper本身] + [upper的后一个]
        
        lower外，upper内，result =
            [:lower的前一个] + [lower本身 - upper的后一个] + [upper的后后一个:]
        
        lower外，upper外，result =
            [:lower的前一个] + [lower本身 - upper本身] + [upper的后一个]
    但是 [(1, 2), (3, 4), (5, 6)] + [2, 2.5] = [(1, 2), (2, 2.5), (3, 4), (5, 6)]
    有时候会因为闭区间而造成的交叠。所以在最后我们要扫描一次array列表，两两删除连续的重复数字
'''

'''start from negative infinity, the i th interval obey:
a <= x < b
当counter是奇数时，表示落在所有子区间外
当counter是偶数时，表示落在某个子区间内
'''
class SparseInterval(object):
    def __init__(self, lower, upper):
        self.array = [lower, upper]

    def __str__(self):
        return str( zip(self.array[::2], self.array[1::2]) )
        
    def __len__(self):
        return len(self.array) / 2
    
    def index(self, x):
        '''return the i th interval that contains x 
        index(self, x) 返回 x 所在self.array和正负无穷所形成的 2n+1
        个(离散区间有n个子区间)小区间的index序号，例如:
            index(2.3, [1,2,3,4]) = 3
        '''
        ind = 1
        for i in self.array:
            if x < i:
                return ind
            else:
                ind += 1
        return ind
    
    def __add__(self, interval):
        '''return self + interval
        '''
        x, y = interval.array
        xi, yi = self.index(x), self.index(y)
        if xi%2 == 0: # 偶数，在子区间内
            a, b = xi-2, self.array[xi-2]
        else: # 奇数，在子区间外
            a, b = xi-1, x
        if yi%2 == 0: # 偶数，在子区间内
            c, d = self.array[yi-1], yi
        else: # 奇数，在子区间外
            c, d = y, yi-1
        
        ## 去除重复的连续值
        array = list()
        i, j = -9999,-9999 # 设置一个不可能出现在self.array中的初始值
        for n in self.array[:a] + [b, c] + self.array[d:]:
            i, j = j, n # example: array = [1, 2, 2, 3]
            if i != j: # 例如是 -9999 != 1 或者是 1 != 2
                array.append(j)
            else: # 例如是 2 == 2
                array.pop() # 删除之前append的2
                j = -9999 # 下一次就会变成 -9999, 3 了
                
        ## 输出
        spsI = SparseInterval(0,1)
        spsI.array = array
        return spsI
    
    def __contains__(self, interval):
        '''return whether interval is in self
        '''
        x, y = interval.array
        for i, j in zip(self.array[::2], self.array[1::2]):
            if (i <= x) & (y <= j):
                return True
        return False
            
def algorithm_demo():
    def index(x, array):
        ind = 1
        for i in array:
            if x < i:
                return ind
            else:
                ind += 1
        return ind
    array = [1,2,3,4,5,6]
    x, y = 1.5, 3.5 # <== 自己修改测试值
    xi, yi = index(x, array), index(y, array)
    print 'array = %s' % zip(array[::2], array[1::2])
    print 'x = %s, y = %s' % (x, y)
    print 'x_index = %s, y_index = %s' % (xi, yi)
    '''lower内，upper内: [:lower的前前一个] + [lower的前一个 - upper的后一个] + [upper的后后一个:]'''
    print array[:xi-2]
    print [array[xi-2], array[yi-1]] 
    print array[yi:]
    '''lower内，upper外: [:lower的前前一个] + [lower的前一个 - upper本身] + [upper的后一个]'''
    # print array[:xi-2]
    # print [array[xi-2], y]
    # print array[yi-1:]
    '''lower外，upper内: [:lower的前一个] + [lower本身 - upper的后一个] + [upper的后后一个:]'''
    # print array[:xi-1]
    # print [x, array[yi-1]]
    # print array[yi:]
    '''lower外，upper外: [:lower的前一个] + [lower本身 - upper本身] + [upper的后一个]'''
    # print array[:xi-1]
    # print [x, y]
    # print array[yi-1:]

def unit_test():
    sps1 = SparseInterval(1,2)
    sps1 = sps1 + SparseInterval(3,4)
    sps1 = sps1 + SparseInterval(5,6)
    print 'sps1 = %s' % sps1
    sps2 = SparseInterval(3, 3.3) # <== 自己修改测试值
    print '%s + %s = %s' % (sps1, sps2, sps1 + sps2) 
    print '%s is in %s ? = %s' % (sps2, sps1, sps2 in sps1)
    
if __name__ == '__main__':
    algorithm_demo()
#     unit_test()