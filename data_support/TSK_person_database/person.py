##coding=utf8
import numpy as np
base_weight = {'International_Terrorist_Watch_List': {1: 35, 0: 0, -1: 0.4}, # Basescore = 0.4, 0.3, 0.1, 0.2
               'National_Terrorist_Watch_List': {1: 25, 0: 0, -1: 0.4},
               'National_Law_Enforcement': {1: 17, 0: 0, -1: 0.4},
               'Local_Law_Enforcement': {1: 13, 0: 0, -1: 0.4},
               'IRS_or_other_Federal_Finance_Company': {1: 10, 0: 0, -1: 0.4},
               
               'Face_Match_with_Picture_DB': {1: 100, 0: 0, -1: 0.3},
               
               'Cash_Payment_Same_Day':  {2: 100, 1:50, 0: 0, -1: 0.1},
               
               'Immediate_Family': {1: 50, 0: 0, -1: 0.2},
               'Extented_Family': {1: 34, 0: 0, -1: 0.2},
               'Place_of_Worship': {1: 16, 0: 0, -1: 0.2},}

joint_watchlist_rules = \
{0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 30,
 8: 0, 9: 0, 10: 0, 11: 40, 12: 20, 13: 40, 14: 40, 15: 50,
 16: 0, 17: 0, 18: 0, 19: 60, 20: 0, 21: 60, 22: 60, 23: 60,
 24: 70, 25: 70, 26: 70, 27: 100, 28: 80, 29: 100, 30: 100, 31: 100}

def person_generator(n):
    '''
    n = how many person you want to generate
    '''
    for i in xrange(n):
        person_info = {'International_Terrorist_Watch_List':   np.random.choice(a=[1,0], p=[0.03,0.97]),
                       'National_Terrorist_Watch_List':        np.random.choice(a=[1,0], p=[0.05,0.95]),
                       'National_Law_Enforcement':             np.random.choice(a=[1,0], p=[0.07,0.93]),
                       'Local_Law_Enforcement':                np.random.choice(a=[1,0], p=[0.15,0.85]),
                       'IRS_or_other_Federal_Finance_Company': np.random.choice(a=[1,0], p=[0.23,0.77]),
                        
                       'Face_Match_with_Picture_DB':           np.random.choice(a=[1,0], p=[0.1,0.9]),
                       
                       'Cash_Payment_Same_Day':                np.random.choice(a=[2,1,0], p=[0.1,0.2,0.7]), # 2 = one way, 1 = round trip
                       'Immediate_Family':                     np.random.choice(a=[1,0], p=[0.05,0.95]),
                       'Extented_Family':                      np.random.choice(a=[1,0], p=[0.08,0.92]),
                       'Place_of_Worship':                     np.random.choice(a=[1,0], p=[0.11,0.89])}
        yield person_info

def score1_base(person):
    total = 0
    for key, v in person.iteritems():
        total += base_weight[key][v] * base_weight[key][-1]
    return total

def score2_dependent_bonus(person):
    joint_watchlist_score = person['International_Terrorist_Watch_List'] * 16 + \
                            person['National_Terrorist_Watch_List'] * 8 + \
                            person['National_Law_Enforcement'] * 4 + \
                            person['Local_Law_Enforcement'] * 2 + \
                            person['IRS_or_other_Federal_Finance_Company'] * 1
    bonus = joint_watchlist_rules[joint_watchlist_score]
    return bonus

def score3_watchlist_relationship_bounus(person):
    counter = person['International_Terrorist_Watch_List'] + \
              person['National_Terrorist_Watch_List'] + \
              person['Face_Match_with_Picture_DB'] + \
              person['Immediate_Family'] + \
              person['Extented_Family'] + \
              person['Place_of_Worship']
    rule = {4:33, 5:66, 6:100}
    return rule.get(counter, 0)


# def evaluate(person):
#     score = score1_base(person) + score2_dependent_bonus(person)*0.18 + score3_watchlist_relationship_bounus(person)*0.12
#     return score


''' INSERT DATA '''

    
# print len(res)
# print len(set(res))
#     res.append(fake)
#     res.append()

'''DB schema'''
