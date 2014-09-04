##coding=utf8
import numpy as np
import pandas as pd
import faker

name = ['Albania',
'Andorra',
'Armenia',
'Austria',
'Azerbaijan',
'Belarus',
'Belgium',
'Bosnia',
'Bulgaria',
'Croatia',
'Cyprus',
'Czech Republic',
'Denmark',
'Estonia',
'Faroe Islands',
'Finland',
'France',
'Georgia Republic',
'Germany',
'Gibraltar',
'Great Britain',
'Greece',
'Hungary',
'Iceland',
'Ireland',
'Isle of Man',
'Israel',
'Italy',
'Kazakhstan',
'Kosovo (Under UNSCR 1244)',
'Kyrgyz Republic',
'Latvia',
'Liechtenstein',
'Lithuania',
'Luxembourg',
'Macedonia (FYR)',
'Malta',
'Moldova',
'Monaco',
'Montenegro',
'Netherlands',
'Norway',
'Poland',
'Portugal',
'Romania',
'Russia',
'San Marino',
'Serbia',
'Slovakia',
'Slovenia',
'Spain',
'Sweden',
'Switzerland',
'Tajikistan',
'Turkey',
'Turkmenistan',
'Ukraine',
'Uzbekistan']

p = [0.004168838,
0.00990099,
0.003126628,
0.020323085,
0.025534132,
0.013027619,
0.148514851,
0.005211047,
0.008337676,
0.007295466,
0.021365294,
0.011464304,
0.013027619,
0.004689943,
0.005211047,
0.019280875,
0.026576342,
0.007816571,
0.036477332,
0.006253257,
0.026055237,
0.027097447,
0.031266285,
0.016154247,
0.023970818,
0.008858781,
0.015112038,
0.024491923,
0.021365294,
0.002084419,
0.005211047,
0.012506514,
0.005211047,
0.017196456,
0.018238666,
0.006253257,
0.018238666,
0.005211047,
0.013548723,
0.003126628,
0.021365294,
0.007816571,
0.032829599,
0.013027619,
0.00990099,
0.051068265,
0.002084419,
0.024491923,
0.008337676,
0.010422095,
0.025013028,
0.019280875,
0.018238666,
0.003126628,
0.022928609,
0.00990099,
0.009379885,
0.011985409]

def numeric_data():
    noa = 2000
    opening_eyes = pd.DataFrame(index = range(noa))
    opening_eyes['country'] = np.random.choice(a = name, size = noa, p=p)
    opening_eyes['gender'] = np.random.choice(a = ['male', 'female'], size = noa, p=[0.691, 0.309])
    opening_eyes['age'] = np.fix(np.random.randn(noa) * 7 + np.ones(noa) * 30)
    
    opening_eyes['last_eye_exam'] =  np.random.choice( a=['Less than 1 year','1-3 years','More than 3 years','Never','NA'], size=noa, p=[0.319,0.156,0.114,0.168,0.243])
    opening_eyes['Glass_type'] =  np.random.choice( a=['Standard Glasses','Sports Glasses','Contact lenses','No','NA'], size=noa, p=[0.248,0.005,0.007,0.708,0.032])
    opening_eyes['Following'] =  np.random.choice( a=['Difficulty seeing','Headaches','Sensitivity to light','Double vision','NA'], size=noa, p=[0.295,0.084,0.065,0.009,0.547])
    opening_eyes['Screening_test'] =  np.random.choice( a=['Without Glasses','With Glasses','With contact lenses','NA'], size=noa, p=[0.808,0.166,0.005,0.021])
    opening_eyes['Visual_acuity_Far'] =  np.random.choice( a=['Pass','Fail','not tested'], size=noa, p=[0.543,0.41,0.047])
    opening_eyes['Visual_acuity_Near'] =  np.random.choice( a=['Pass','Fail','not tested'], size=noa, p=[0.809,0.146,0.045])
    opening_eyes['Color_vision'] =  np.random.choice( a=['Pass (Trial 1 8 or 9)','No Pass (Trial 2 less than 9)','Inconclusive','not tested'],
                                                      size=noa, p=[0.886,0.07,0.014,0.03])
    opening_eyes['Stereopsis'] =  np.random.choice( a=['Normal (5 or 6)','Abnormal (less than 5)','not tested'], size=noa, p=[0.728,0.182,0.09])
    opening_eyes['Eye_Health_external_Normal'] =  np.random.choice( a=[1,0], size=noa, p=[0.922,0.078])
    opening_eyes['Eye_Health_external_Lid anomaly'] =  np.random.choice( a=[1,0], size=noa, p=[0.008,0.992])
    opening_eyes['Eye_Health_external_Blepharitis'] =  np.random.choice( a=[1,0], size=noa, p=[0.003,0.997])
    opening_eyes['Eye_Health_external_Conjunctivitis'] =  np.random.choice( a=[1,0], size=noa, p=[0.006,0.994])
    opening_eyes['Eye_Health_external_Pterigium_or_pinguecula'] =  np.random.choice( a=[1,0], size=noa, p=[0.009,0.991])
    opening_eyes['Eye_Health_external_Corneal_anomaly'] =  np.random.choice( a=[1,0], size=noa, p=[0.018,0.982])
    opening_eyes['Eye_Health_external_Ptosis'] =  np.random.choice( a=[1,0], size=noa, p=[0.002,0.998])
    opening_eyes['Eye_Health_external_Iris_anomaly'] =  np.random.choice( a=[1,0], size=noa, p=[0.003,0.997])
    
    opening_eyes['Eye_Health_internal_Normal'] =  np.random.choice( a=[1,0], size=noa, p=[0.872,0.128])
    opening_eyes['Eye_Health_internal_Cataracts'] =  np.random.choice( a=[1,0], size=noa, p=[0.047,0.953])
    opening_eyes['Eye_Health_internal_Coloboma'] =  np.random.choice( a=[1,0], size=noa, p=[0.001,0.999])
    opening_eyes['Eye_Health_internal_Retinal_anomaly'] =  np.random.choice( a=[1,0], size=noa, p=[0.009,0.991])
    opening_eyes['Eye_Health_internal_Optic_nerve_anomaly'] =  np.random.choice( a=[1,0], size=noa, p=[0.005,0.995])
    opening_eyes['Eye_Health_internal_Glaucoma_suspect'] =  np.random.choice( a=[1,0], size=noa, p=[0.005,0.995])
    
    opening_eyes['Pupils'] =  np.random.choice( a=['Normal','Abnormal','NA'], size=noa, p=[0.924,0.006,0.07])
    
    opening_eyes['Recommend'] =  np.random.choice( a=['New glasses','No new Glasses','Sunglasses'], size=noa, p=[0.335,0.663,0.002])    
    return opening_eyes

def hist_dict(array):
    res = dict()
    for i in array:
        if i in res:
            res[i] += 1
        else:
            res[i] = 1
    return res

opening_eyes = numeric_data()

''' group by country '''
summary = dict()
for columnname in opening_eyes: ## 对每一列进行统计
    summary[columnname] = pd.DataFrame(index = name)
    
    for country in name: ## group by 每一个国家
        ind = np.where(opening_eyes['country'].values == country)
        tempdata = opening_eyes.loc[ind[0], columnname]
         
        for k,v in hist_dict(tempdata.values).iteritems(): ## 对每个国家/列数据进行hist频率统计
            summary[columnname].loc[country, k] = v
    
writer = pd.ExcelWriter('opening_eyes.xlsx')
opening_eyes.to_excel(writer, 'data')

for k, v in summary.iteritems():
    if len(k) > 31: ## 长于31位的字符串不能作为sheetname
        k = k[0:31]
    v.to_excel(writer, k)
writer.save()
