def tuple_to_range(t):
    return range(t[0],t[1]+1)

class Discrete_Interval(object):
    def __init__(self, intervallist):
        flag = 1
        for interval in intervallist:
            tempflag = 1
            if type(interval) != tuple: ## if not tuple
                tempflag = 0
            if len(interval) != 2: ## if tuple len != 2
                tempflag = 0
            if (interval[0]==int) != 2: ## if tuple element not int
                tempflag = 0
            if interval[0] > interval [1]: ## if lower bound > upper bound
                tempflag = 0
            flag = flag & tempflag
        self.intervallist = intervallist
        
    def __str__(self):
        res = list()
        for interval in self.intervallist:
            res.append(str(interval[0]) + ' - ' + str(interval[1]))
        return ' , '.join(res)
     
    def __name__(self):
        return 'Discrete_Interval'
    
    def overlap(self, other):
        if other.__name__() != 'Discrete_Interval':
            print 'argument is not a Discrete_Interval'
            return None
        for t in self.intervallist:
            for i in tuple_to_range(t):
                for tother in other.intervallist:
                    if i in tuple_to_range(tother):
                        return True
        return False

''' ====== Test ====== '''
   
# qj1 = Discrete_Interval([(1,4),(8,12)])
# qj2 = Discrete_Interval([(5,7),(-100,1)])
# print qj2.overlap(qj1)
