##coding=utf8
from sklearn.neighbors import NearestNeighbors
from sklearn import preprocessing
import numpy as np

def knn_train(train_fname):
    train_data = list()
    with open(train_fname, 'rb') as f:
        for row in f.xreadlines():
            nr = row.strip().split(',') 
            ## nr looks like: ['76', '1', '56', '5', '0.58', '0.66', '0.9', '1.37', '2']
            finalrow = [float(nr[3]),
                        float(nr[4]),
                        float(nr[5]),
                        float(nr[6]),
                        float(nr[7])]
            train_data.append(finalrow)
    nbrs = NearestNeighbors(n_neighbors=4, algorithm='ball_tree').fit(train_data)
    return nbrs

def load_train(train_fname):
    train_data = list()
    train_label = list()
    with open(train_fname, 'rb') as f:
        for row in f.xreadlines():
            nr = row.strip().split(',') 
            ## nr looks like: ['76', '1', '56', '5', '0.58', '0.66', '0.9', '1.37', '2']
            finalrow = [float(nr[0]),
                        float(nr[1]),
                        float(nr[2]),
                        float(nr[3]),
                        float(nr[4]),
                        float(nr[5]),
                        float(nr[6]),
                        float(nr[7])]
            train_data.append(finalrow)
            train_label.append(int(nr[8]))
    return train_data, train_label




data = [77, ## age
        1, ## gender
        50, ## years of smoking
        4, ## cigarette per day
        0.656288924, ## FEV% AVG
        0.641185257, ## FEV% today
        0.895300599, ## OX2% today
        1.238643668] ## walking miles today
train_data, train_label = load_train('copd_1100_train.txt') ## 1. 读数据
# nbrs = NearestNeighbors(n_neighbors=4, algorithm='ball_tree').fit(train_data) ## 2. 训练KNN
train_data.append(data) ## 3. 增加新用户数据
train_data = np.array(train_data, dtype = 'f') ## 4. 转化为numpy数组
std_train_data = preprocessing.scale(train_data) ## 5. 标准化数据
(m,n) = std_train_data.shape

train_label = np.array(train_label, dtype = 'int')
print np.where(train_label == 1)[0]



# nbrs = NearestNeighbors(n_neighbors=4, algorithm='ball_tree').fit(std_train_data[0:m-1])
# distances, indices = nbrs.kneighbors(std_train_data[-1])
# 
# for index in indices[0]:
#     print train_data[index], index
# print distances