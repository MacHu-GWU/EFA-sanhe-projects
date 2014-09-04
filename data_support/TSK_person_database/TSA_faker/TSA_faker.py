##coding=utf8
import numpy as np
import pandas as pd
import faker

        
num = 1000
people = pd.DataFrame(index = range(1,num+1))
'''Initial the setting'''
people['International Terrorist Watch List'] =np.random.choice( a=[1,0], size=num, p=[0.03,0.97])
people['National Terrorist Watch List'] =np.random.choice( a=[1,0], size=num, p=[0.05,0.95])
people['National Law Enforcement'] =np.random.choice( a=[1,0], size=num, p=[0.07,0.93])
people['Local Law Enforcement'] =np.random.choice( a=[1,0], size=num, p=[0.15,0.85])
people['IRS or other Federal Finance Company'] =np.random.choice( a=[1,0], size=num, p=[0.23,0.77])
'''Biometrics'''
people['Face Match with Picture DB'] =np.random.choice( a=[1,0], size=num, p=[0.1,0.9])
'''Ticket Purchase'''
people['Cash Payment Same Day'] =np.random.choice( a=[2,1,0], size=num, p=[0.1,0.2,0.7])
'''Link Analysis'''
people['Immediate Family'] =np.random.choice( a=[1,0], size=num, p=[0.05,0.95])
people['Extented Family'] =np.random.choice( a=[1,0], size=num, p=[0.08,0.92])
people['Place of Worship'] =np.random.choice( a=[1,0], size=num, p=[0.11,0.89])

people.to_csv('people.csv')

rules = {'International Terrorist Watch List':67,
         'National Terrorist Watch List':51,
         'National Law Enforcement':34,
         'Local Law Enforcement':21,
         'IRS or other Federal Finance Company':20,
         'Face Match with Picture DB':100,
         'Immediate Family':60,
         'Extented Family':40,
         'Place of Worship':20,}
people_value = people

res = list()
for i in people_value['Cash Payment Same Day'].values:
    if i == 2:
        res.append(100)
    elif i == 1:
        res.append(75)
    else:
        res.append(0)

people_value['Cash Payment Same Day'] = res

for k in people_value:
    if k != 'Cash Payment Same Day':
        people_value[k] = people_value[k] * rules[k]

def clear100(array):
    res = list()
    for i in array:
        while i > 100:
            i = i * 0.9
        res.append(i)
    return res

TSK_feature = pd.DataFrame(index = range(1,num+1))
TSK_feature['WatchList'] = np.sum(people_value.loc[:,'International Terrorist Watch List':'IRS or other Federal Finance Company'].values,axis = 1)
TSK_feature['WatchList'] = clear100(TSK_feature['WatchList'].values)

TSK_feature['Biometrics'] = people_value.loc[:,'Face Match with Picture DB'].values
TSK_feature['Ticket Purchase'] = people_value.loc[:,'Cash Payment Same Day'].values
TSK_feature['Link Analysis'] = np.sum(people_value.loc[:,'Immediate Family':'Place of Worship'].values,axis = 1)
TSK_feature['Link Analysis'] = clear100(TSK_feature['Link Analysis'].values)

TSK_feature['Total'] = np.dot(TSK_feature.values, np.array([[0.45,0.3,0.25,0.2]]).transpose()   )
TSK_feature.to_csv('TSK_feature.csv')
