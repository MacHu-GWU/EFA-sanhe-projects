import numpy as np



y = np.array([7,58,36,74,44,32,54,16,103,98,77,56])
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

e = 2.5
def clean_outlier(x, y, e = 3):
    while 1:
        m = y.mean()
        std = y.std()
        ind = np.where( abs(y - m) <= (std * e) )
        if len(ind[0]) == len(y):
            break
        else:
            y = y[ind]
            x = x[ind]
    return x,y
