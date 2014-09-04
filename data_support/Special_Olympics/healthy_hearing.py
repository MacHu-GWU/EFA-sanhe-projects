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
    healthy_hearing = pd.DataFrame(index = range(noa))
    healthy_hearing['country'] = np.random.choice(a = name, size = noa, p=p)
    healthy_hearing['gender'] = np.random.choice(a = ['male', 'female'], size = noa, p=[0.696, 0.304])
    healthy_hearing['age'] = np.fix(np.random.randn(noa) * 7 + np.ones(noa) * 30)

    healthy_hearing['Ear_Block'] =  np.random.choice( a=['Clear','Partically Blocked','Blocked'], size=noa, p=[0.682,0.147,0.171])
    healthy_hearing['Otoacoustic_Emissions'] =  np.random.choice( a=['Pass (both ear)','No Pass','NA'], size=noa, p=[0.525,0.469,0.006])
    healthy_hearing['Tympanometry'] =  np.random.choice( a=['Pass (both ear)','No Pass','NA'], size=noa, p=[0.34,0.112,0.548])
    healthy_hearing['Pure_Tone_Screen_Hearing_ Level_(2000Hz)'] =  np.random.choice( a=['Pass (both ear)','No Pass','NA'], size=noa, p=[0.312,0.139,0.549])
    healthy_hearing['Pure_Tone_Screen_Hearing_ Level_(4000Hz)'] =  np.random.choice( a=['Pass (both ear)','No Pass','NA'], size=noa, p=[0.273,0.178,0.549])
    '''Services_Provided_at_the_Event'''
    healthy_hearing['Ear_Canal_Inspection'] =  np.random.choice( a=[1,0], size=noa, p=[0.098,0.902])
    healthy_hearing['Hearing_Screening'] =  np.random.choice( a=[1,0], size=noa, p=[0.098,0.902])
    healthy_hearing['Middle_Ear_Screening'] =  np.random.choice( a=[1,0], size=noa, p=[0.046,0.954])
    healthy_hearing['Hearing_Threshold_Testing'] =  np.random.choice( a=[1,0], size=noa, p=[0.019,0.981])
    healthy_hearing['Hearing_Aid_Repair_or_Maintenance'] =  np.random.choice( a=[1,0], size=noa, p=[0.004,0.996])
    healthy_hearing['Ear_Mold_for_Hearing_Aid'] =  np.random.choice( a=[1,0], size=noa, p=[0.003,0.997])
    healthy_hearing['Hearing_Aid'] =  np.random.choice( a=[1,0], size=noa, p=[0.002,0.998])
    healthy_hearing['Counseling_Athlete_or_Coach_or_Other'] =  np.random.choice( a=[1,0], size=noa, p=[0.084,0.916])
    healthy_hearing['Report_to_Athlete_or_Coach_or_Other'] =  np.random.choice( a=[1,0], size=noa, p=[0.085,0.915])
    '''Recommended Follow-up Care'''
    healthy_hearing['Cerumen Removal'] =  np.random.choice( a=[1,0], size=noa, p=[0.314,0.686])
    healthy_hearing['Medical evaluation of ears'] =  np.random.choice( a=[1,0], size=noa, p=[0.107,0.893])
    healthy_hearing['Audiological evaluation of hearing'] =  np.random.choice( a=[1,0], size=noa, p=[0.166,0.834])
    healthy_hearing['Ear molds for hearing aid use'] =  np.random.choice( a=[1,0], size=noa, p=[0.039,0.961])
    healthy_hearing['Hearing aid evaluation and fitting'] =  np.random.choice( a=[1,0], size=noa, p=[0.043,0.957])

    
#     healthy_hearing[''] =  np.random.choice( a=[], size=noa, p=[])
#     healthy_hearing[''] =  np.random.choice( a=[], size=noa, p=[])
#     healthy_hearing[''] =  np.random.choice( a=[], size=noa, p=[])

    return healthy_hearing

def hist_dict(array):
    res = dict()
    for i in array:
        if i in res:
            res[i] += 1
        else:
            res[i] = 1
    return res

healthy_hearing = numeric_data()

''' group by country '''
summary = dict()

for columnname in healthy_hearing: ## 对每一列进行统计
    summary[columnname] = pd.DataFrame(index = name)
     
    for country in name: ## group by 每一个国家
        ind = np.where(healthy_hearing['country'].values == country)
        tempdata = healthy_hearing.loc[ind[0], columnname]
        for k,v in hist_dict(tempdata.values).iteritems(): ## 对每个国家/列数据进行hist频率统计
            summary[columnname].loc[country, k] = v
    
writer = pd.ExcelWriter('healthy_hearing.xlsx')
healthy_hearing.to_excel(writer, 'data')

for k, v in summary.iteritems():
    if len(k) > 31: ## 长于31位的字符串不能作为sheetname
        k = k[0:31]
    v.to_excel(writer, k)
writer.save()