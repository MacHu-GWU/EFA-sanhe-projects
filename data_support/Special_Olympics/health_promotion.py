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
    health_promotion = pd.DataFrame(index = range(noa))
    health_promotion['country'] = np.random.choice(a = name, size = noa, p=p)
    health_promotion['gender'] = np.random.choice(a = ['male', 'female'], size = noa, p=[0.689, 0.311])
    health_promotion['age'] = np.fix(np.random.randn(noa) * 7 + np.ones(noa) * 30)
    

    ## Weight
    health_promotion['adults_aged_20_or_over'] =  np.random.choice( a=['Underweight','Healthy_weight','Overweight','Obese'],
                                                                    size=noa, p=[0.045,0.46,0.341,0.154])
    health_promotion['children_and_adolescents_under_age_20'] =  np.random.choice( a=['Underweight','Healthy_weight','Overweight','Obese'],
                                                                                   size=noa, p=[0.06,0.727,0.104,0.109])
    health_promotion['at_risk_for_Osteopenia'] =  np.random.choice( a=[1,0], size=noa, p=[0.208,0.792])
    health_promotion['at_risk_for_Osteoporosis'] =  np.random.choice( a=[1,0], size=noa, p=[0.014,0.986])
    health_promotion['blood_pressure(Adults(aged_20_or_over))'] =  \
                    np.random.choice( a=['Hypotension','Normal','Hypertension Stage 1','Hypertension Stage 2',
                                         'Hypertension Stage 3','Hypertension Stage 4'], size=noa, p=[0.089,0.757,0.134,0.014,0.004,0.002])
    health_promotion['blood_pressure(Children_and_adolescents_under_age_20)'] =  \
                    np.random.choice( a=['Hypotension','Normal','Hypertension Stage 1','Hypertension Stage 2',
                                         'Hypertension Stage 3','Hypertension Stage 4'], size=noa, p=[0.141,0.759,0.092,0.008,0,0])
    ## Smoke
    health_promotion['smoker'] =  np.random.choice( a=[1,0], size=noa, p=[0.055,0.945])
    health_promotion['what_do_athletes_do_if_someone_smokes_around_them'] =  \
                    np.random.choice( a=['Asks smoker to stop','Leaves the room','Smoke','Do not do anything','Other'], 
                                      size=noa, p=[0.323,0.254,0.047,0.351,0.025])
                    
    health_promotion['reported_beverage_when_thirsty(Water)'] =  np.random.choice( a=[1,0], size=noa, p=[0.828,0.172])
    health_promotion['reported_beverage_when_thirsty(Fruit_juice)'] =  np.random.choice( a=[1,0], size=noa, p=[0.33,0.67])
    health_promotion['reported_beverage_when_thirsty(Soft_drink)'] =  np.random.choice( a=[1,0], size=noa, p=[0.222,0.778])
    health_promotion['reported_beverage_when_thirsty(Milk_product)'] =  np.random.choice( a=[1,0], size=noa, p=[0.3,0.7])
    health_promotion['reported_beverage_when_thirsty(Energy_Drink)'] =  np.random.choice( a=[1,0], size=noa, p=[0.007,0.993])
    
    health_promotion['sources_of_calcium'] =  np.random.choice( a=['Less than 1 serving per day','1-2 servings per day','3-5 servings per day','More than 5 servings per day',
                                                                   'Never'], size=noa, p=[0.166,0.554,0.234,0.021,0.025])
    health_promotion['fruits_and_vegetables'] =  np.random.choice( a=['Less than 1 serving per day','1-2 servings per day','3-5 servings per day','More than 5 servings per day',
                                                                   'Never'], size=noa, p=[0.151,0.461,0.315,0.033,0.04])
    health_promotion['snack_foods'] =  np.random.choice( a=['Daily','Weekly','Monthly','Never'], size=noa, p=[0.526,0.35,0.071,0.053])
    health_promotion['sweetened_beverages'] =  np.random.choice( a=['Daily','Weekly','Monthly','Never'], size=noa, p=[0.352,0.435,0.116,0.097])
    health_promotion['fast_foods'] =  np.random.choice( a=['Daily','Weekly','Monthly','Never'], size=noa, p=[0.075,0.376,0.317,0.232])

    return health_promotion

def hist_dict(array):
    res = dict()
    for i in array:
        if i in res:
            res[i] += 1
        else:
            res[i] = 1
    return res

health_promotion = numeric_data()

''' group by country '''
summary = dict()

for columnname in health_promotion: ## 对每一列进行统计
    summary[columnname] = pd.DataFrame(index = name)
     
    for country in name: ## group by 每一个国家
        ind = np.where(health_promotion['country'].values == country)
        tempdata = health_promotion.loc[ind[0], columnname]
        for k,v in hist_dict(tempdata.values).iteritems(): ## 对每个国家/列数据进行hist频率统计
            summary[columnname].loc[country, k] = v
    
writer = pd.ExcelWriter('health_promotion.xlsx')
health_promotion.to_excel(writer, 'data')

for k, v in summary.iteritems():
    if len(k) > 31: ## 长于31位的字符串不能作为sheetname
        k = k[0:31]
    v.to_excel(writer, k)
writer.save()


