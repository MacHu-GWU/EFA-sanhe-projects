##coding=utf8
from sklearn import tree
def dt_train(train_fname):
    train_data = list()
    train_label = list()
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
            train_label.append(int(nr[8]))
    clf = tree.DecisionTreeClassifier() ## create new decisiontree classifier
    clf = clf.fit(train_data, train_label) ## train
    return clf

clf = dt_train('copd_1000_train.txt')
''' TEST on test data '''
test_data = list()
with open('copd_1000_test.txt', 'rb') as f:
    for row in f.xreadlines():
        nr = row.strip().split(',') ## nr
        finalrow = [float(nr[3]),
                    float(nr[4]),
                    float(nr[5]),
                    float(nr[6]),
                    float(nr[7])]
        test_data.append(finalrow)
''' TEST on test data '''
res = clf.predict(test_data)
counter = 1
for i in res:
    print '%s ------ %s' % (counter, i)
    counter += 1

''' TEST on train data '''
# res = clf.predict(train_data)
# counter = 0
# for i in range(1000):
#     if res[i] == train_label[i]:
#         counter += 1
# print counter

