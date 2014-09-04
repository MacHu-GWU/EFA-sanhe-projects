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
    fun_fitness = pd.DataFrame(index = range(noa))
    fun_fitness['country'] = np.random.choice(a = name, size = noa, p=p)
    fun_fitness['gender'] = np.random.choice(a = ['male', 'female'], size = noa, p=[0.69, 0.31])
    fun_fitness['age'] = np.fix(np.random.randn(noa) * 7 + np.ones(noa) * 30)
    
    fun_fitness['current_diseases'] =  np.random.choice( a=['breathing or lung','heart','circulation','NA'], 
                                                         size=noa, p=[0.026,0.015,0.007,0.952])
    fun_fitness['pain'] =  np.random.choice( a=['Lower extremity','Upper extremity','Back','Neck','Head','NA'], 
                                             size=noa, p=[0.029,0.013,0.015,0.005,0.006,0.932])
    fun_fitness['sprain'] =  np.random.choice( a=['Foot or ankle','Knee','Hip','Hand or wrist','Elbow','Shoulder','Back','Neck','NA'], 
                                               size=noa, p=[0.016,0.014,0.001,0.009,0.011,0.008,0.004,0.002,0.935])
    fun_fitness['strain'] =  np.random.choice( a=['Foot','Leg','Back or pelvis','Hand','Arm','Shoulder or scapula','Neck','NA'],
                                               size=noa, p=[0.004,0.015,0.01,0.001,0.002,0.001,0,0.967])
    
    fun_fitness['has_skin_problems'] =  np.random.choice( a=[1,0], size=noa, p=[0.008,0.992])
    fun_fitness['has_fever_illness_or_infection'] =  np.random.choice( a=[1,0], size=noa, p=[0.006,0.994])
    fun_fitness['fallen_in_your_home_in_the_past_year'] =  np.random.choice( a=[1,0,'NA'], size=noa, p=[0.059,0.876,0.065])
    ## Flexibility
    fun_fitness['do_you_stretch_routinely'] =  np.random.choice( a=['Several times each day','Once each day','Occasionally, but not every day',
                                                                    'No regular stretching','Could not elicit response to question','NA'], 
                                                                 size=noa, p=[0.091,0.306,0.345,0.227,0.002,0.029])
    ## Functional strength
    fun_fitness['physical_activity_for_strength'] =  np.random.choice( a=['No_days','1-2 days','3-6 days','Every Day','NA'],
                                                                       size=noa, p=[0.364,0.286,0.175,0.143,0.032])
    fun_fitness['special_olympics_training'] =  np.random.choice( a=['None','Some','Most','All','NA'], size=noa, p=[0.093,0.233,0.121,0.054,0.499])
    
    ## Physical Activity Habits
    fun_fitness['how_many_days_per_week_do_you_exercise'] =  np.random.choice( a=['every day','3-6 days','1-2 days','no regular program'],
                                                                               size=noa, p=[0.232,0.3,0.343,0.125])
    fun_fitness['activity_at_a_moderate_level'] =  np.random.choice( a=['every day','3-6 days','1-2 days','no regular program'],
                                                                     size=noa, p=[0.232,0.274,0.386,0.108])
    fun_fitness['how_much_is_related_to_Special_Olympics_training'] =  np.random.choice( a=['None','Some','Most','All','NA'],
                                                                                         size=noa, p=[0.027,0.115,0.054,0.062,0.742])
    
    ## Recommended
    fun_fitness['physical_therapist_referral_recommended'] =  np.random.choice( a=[1,0], size=noa, p=[0.427,0.573])
    fun_fitness['reason_for_PT_referral(Flexibility)'] =  np.random.choice( a=[1,0], size=noa, p=[0.846,0.154])
    fun_fitness['reason_for_PT_referral(Strength)'] =  np.random.choice( a=[1,0], size=noa, p=[0.485,0.515])
    fun_fitness['reason_for_PT_referral(Balance)'] =  np.random.choice( a=[1,0], size=noa, p=[0.633,0.367])
    fun_fitness['reason_for_PT_referral(Aerobic Fitness)'] =  np.random.choice( a=[1,0], size=noa, p=[0.217,0.783])
    fun_fitness['primary_care_physician_referral_recommended'] =  np.random.choice( a=[1,0], size=noa, p=[0.084,0.916])
    
#     fun_fitness[''] =  np.random.choice( a=[], size=noa, p=[])
    return fun_fitness

def hist_dict(array):
    res = dict()
    for i in array:
        if i in res:
            res[i] += 1
        else:
            res[i] = 1
    return res

fun_fitness = numeric_data()
''' group by country '''
summary = dict()

for columnname in fun_fitness: ## 对每一列进行统计
    summary[columnname] = pd.DataFrame(index = name)
     
    for country in name: ## group by 每一个国家
        ind = np.where(fun_fitness['country'].values == country)
        tempdata = fun_fitness.loc[ind[0], columnname]
        for k,v in hist_dict(tempdata.values).iteritems(): ## 对每个国家/列数据进行hist频率统计
            summary[columnname].loc[country, k] = v
    
writer = pd.ExcelWriter('fun_fitness.xlsx')
fun_fitness.to_excel(writer, 'data')

for k, v in summary.iteritems():
    if len(k) > 31: ## 长于31位的字符串不能作为sheetname
        k = k[0:31]
    v.to_excel(writer, k)
writer.save()