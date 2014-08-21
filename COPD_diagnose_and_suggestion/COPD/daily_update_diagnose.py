##coding=utf8
from sklearn import tree
from sklearn.neighbors import NearestNeighbors
from sklearn import preprocessing
import numpy as np

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

def dt_train(train_fname):
    train_data = list()
    train_label = list()
    with open(train_fname, 'rb') as f:
        for row in f.xreadlines():
            nr = row.strip().split(',') 
            ## nr looks like: ['76', '1', '56', '5', '0.58', '0.66', '0.9', '1.37', '2']
            finalrow = [int(nr[0]),
                        int(nr[1]),
                        int(nr[2]),
                        int(nr[3]),
                        float(nr[4]),
                        float(nr[5]),
                        float(nr[6]),
                        float(nr[7])]
            train_data.append(finalrow)
            train_label.append(int(nr[8]))
    clf = tree.DecisionTreeClassifier() ## create new decisiontree classifier
    clf = clf.fit(train_data, train_label) ## train
    return clf

def predict_one(data):
    newdata =  [int(data[0]),
                int(data[1]),
                int(data[2]),
                int(data[3]),
                float(data[4]),
                float(data[5]),
                float(data[6]),
                float(data[7])]
    clf = dt_train('copd_1100_train.txt')
    return clf.predict(newdata)[0]

def daily_update(data):
    msg = list()
    diagnose = predict_one(data) ## <=== diagnose patient current COPD level
    msg.append('================ Diagnose ================')
    msg.append('You are diagnosed as COPD level: %s' % diagnose)
    
    ''' setup a COPD recovery goal based on patient's current COPD level '''
    mapping = {4:3,3:2,2:1,1:0}
    if diagnose == 0:
        goal = 0
    else:
        goal = 0
    #     goal = mapping[diagnose] ## <=== the goal that patient going to approach
    
    train_data, train_label = load_train('copd_1100_train.txt') ## 1. load train data
    train_data.append(data) ## 2. append the patient data
    train_data = np.array(train_data, dtype = 'f') ## 3. transform to numpy object
    train_label = np.array(train_label, dtype = 'int')
    std_train_data = preprocessing.scale(train_data) ## 4. standardize data, for KNN
    (m,n) = std_train_data.shape ## 5. return the data-set size
    
    index = np.where(train_label == goal)[0] ## index是在std_train_data中的index, goal是想要达到的目标
    target_data = std_train_data[index] ## idol data set
    nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(target_data) ## 训练KNN
    distances, indices = nbrs.kneighbors(std_train_data[-1])## KNN search
                                                            ## indices是在target_data中的index
    
    nn = train_data[  index[indices[0]  ]  ]
    nn = np.transpose(nn)
    
    if data[3] == 0: ## if he is not smoking
        cpd_goal = 0 ## keep not smoking :)
    else: ## if smoking, find the guy smoke least in the idol data set
        minimum = 999
        for i in nn[3]:
            if i != 0:
                if minimum > i:
                    minimum = i
        if minimum == 999: ## if idol are all not smoking...
            minimum = data[3]
        cpd_goal = int(minimum * 0.7) 
    walk_goal = nn[7].max() * 1.1
    msg.append('=============== Suggestion ===============')
    if cpd_goal:
        msg.append('Reduce your Cigarette per day to %s.' % cpd_goal)
    else:
        msg.append('Keep on no smoking.')
    
    if data[7] >= walk_goal:
        msg.append('You do practice a lot! Keep doing that. And make sure at least walk %4.2f miles per day.' % walk_goal)
    else:
        msg.append('you should walk at least %4.2f miles per day to getting better.' % walk_goal)
    return '\n'.join(msg)

def parser_3(survey_string, dailyupdate_string):
    FEV_map = {'0':0.92,'1':0.87,'2':0.7,'3':0.43,'4':0.2}
    a,b,c,d,e = survey_string.strip().split(',')
    f,g,h = dailyupdate_string.strip().split(',')
    return (int(a), int(b), int(c), int(d), FEV_map[e], float(f), float(g), float(h))


data = [85, ## age                            70-100
        1, ## gender                          0/1
        25, ## years of smoking               0=non smoker 40-90=smoker
        10, ## cigarette per day              0-20
        0.60, ## FEV% AVG                     0.1-1
        0.589876, ## FEV% today               0.1-1
        0.94, ## OX2% today                   0.8-0.99
        4.538643668] ## walking miles today
 
data = parser_3('85,1,25,10,2', '0.589876,0.94,4.538643668')
print daily_update(data)