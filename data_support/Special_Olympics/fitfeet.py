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
    fitfeet = pd.DataFrame(index = range(noa))
    fitfeet['country'] = np.random.choice(a = name, size = noa, p=p)
    fitfeet['gender'] = np.random.choice(a = ['male', 'female'], size = noa, p=[0.689, 0.311])
    fitfeet['age'] = np.fix(np.random.randn(noa) * 5 + np.ones(noa) * 25)
    
    fitfeet['Current_Shoe_Type'] =  np.random.choice( a=['Sport', 'Casual', 'Boots', 'Sandal', 'Custom_made'], size=noa, p=[0.892,0.014,0.04,0.001,0.053])
    fitfeet['Current_Sock_Type'] =  np.random.choice( a=['Acrylic', 'Cotton', 'Nylon', 'Wool', 'Other', 'No Sock'], size=noa, p=[0.921,0.02,0.011,0.02,0,0.028])
    
    fitfeet['Left_Joint_Range_of_Motion_Ankle'] =  np.random.choice(a = ['normal', 'restricted', 'Hypermobile', 'NA'], size = noa, p=[0.815, 0.114, 0.056, 0.015])
    fitfeet['Left_Joint_Range_of_Motion_MTP'] =  np.random.choice(a = ['normal', 'restricted', 'Hypermobile', 'NA'], size = noa, p=[0.873, 0.059, 0.052, 0.016])
    fitfeet['Left_Joint_Range_of_Motion_Subtalar'] =  np.random.choice(a = ['normal', 'restricted', 'Hypermobile', 'NA'], size = noa, p=[0.884, 0.041, 0.057, 0.018])
    fitfeet['Left_Joint_Range_of_Motion_Midtarsal'] =  np.random.choice(a = ['normal', 'restricted', 'Hypermobile', 'NA'], size = noa, p=[0.889, 0.033, 0.053, 0.025])
    fitfeet['Left_Joint_Range_of_Motion_Knee'] =  np.random.choice(a = ['Valgus (outward angulation)', 'Normal', 'Varus (inward angulation)', 'Recurvatum (knee bend)', 'Flexum (knee bend)', 'NA'], size = noa, p=[0.041, 0.835, 0.013, 0.03, 0.008, 0.073])
    fitfeet['Right_Joint_Range_of_Motion_Ankle'] =  np.random.choice(a = ['normal', 'restricted', 'Hypermobile', 'NA'], size = noa, p=[0.806, 0.114, 0.056, 0.024])
    fitfeet['Right_Joint_Range_of_Motion_MTP'] =  np.random.choice(a = ['normal', 'restricted', 'Hypermobile', 'NA'], size = noa, p=[0.868, 0.054, 0.053, 0.025])
    fitfeet['Right_Joint_Range_of_Motion_Subtalar'] =  np.random.choice(a = ['normal', 'restricted', 'Hypermobile', 'NA'], size = noa, p=[0.875, 0.038, 0.056, 0.031])
    fitfeet['Right_Joint_Range_of_Motion_Midtarsal'] =  np.random.choice(a = ['normal', 'restricted', 'Hypermobile', 'NA'], size = noa, p=[0.881, 0.035, 0.049, 0.035])
    fitfeet['Right_Joint_Range_of_Motion_Knee'] =  np.random.choice(a = ['Valgus (outward angulation)', 'Normal', 'Varus (inward angulation)', 'Recurvatum (knee bend)', 'Flexum (knee bend)', 'NA'], size = noa, p=[0.042, 0.835, 0.011, 0.031, 0.008, 0.073])
    
    fitfeet['Left_Foot_Structure'] =  np.random.choice( a=['Pes Cavus (high arch)','Pes Planus (flat foot)','Metatarsus Adductus (foot turned inward)',
                                                           'Tibial Varum (bow leg)','NA'], size=noa, p=[0.069,0.344,0.018,0.021,0.548])
    fitfeet['Left_Foot_Structure_Calcaneus_(heel_bone)'] =  np.random.choice( a=['Valgus (outward angulation)','Normal','Varus (inward angulation)', 'NA'], 
                                                                              size=noa, p=[0.236,0.632,0.061,0.071])
    fitfeet['Right_Foot_Structure'] =  np.random.choice( a=['Pes Cavus (high arch)','Pes Planus (flat foot)','Metatarsus Adductus (foot turned inward)',
                                                            'Tibial Varum (bow leg)','NA'], size=noa, p=[0.065,0.347,0.02,0.025,0.543])
    fitfeet['Right_Foot_Structure_Calcaneus_(heel_bone)'] =  np.random.choice( a=['Valgus (outward angulation)','Normal','Varus (inward angulation)', 'NA'],
                                                                               size=noa, p=[0.217,0.642,0.063,0.078])
     
    fitfeet['Left_Basic_Gait_Analysis(Normal)'] =  np.random.choice( a=[1,0], size=noa, p=[0.599,0.401])
    fitfeet['Left_Basic_Gait_Analysis(Excessive_Pronation)'] =  np.random.choice( a=[1,0], size=noa, p=[0.198,0.802])
    fitfeet['Left_Basic_Gait_Analysis(Excessive_Supination)'] =  np.random.choice( a=[1,0], size=noa, p=[0.047,0.953])
    fitfeet['Left_Basic_Gait_Analysis(Forefoot_Abduction)'] =  np.random.choice( a=[1,0], size=noa, p=[0.148,0.852])
    fitfeet['Left_Basic_Gait_Analysis(Forefoot_Adduction)'] =  np.random.choice( a=[1,0], size=noa, p=[0.031,0.969])
    fitfeet['Left_Basic_Gait_Analysis(Early_Heel)'] =  np.random.choice( a=[1,0], size=noa, p=[0.022,0.978])
 
    fitfeet['Right_Basic_Gait_Analysis(Normal)'] =  np.random.choice( a=[1,0], size=noa, p=[0.606,0.394])
    fitfeet['Right_Basic_Gait_Analysis(Excessive_Pronation)'] =  np.random.choice( a=[1,0], size=noa, p=[0.197,0.803])
    fitfeet['Right_Basic_Gait_Analysis(Excessive_Supination)'] =  np.random.choice( a=[1,0], size=noa, p=[0.046,0.954])
    fitfeet['Right_Basic_Gait_Analysis(Forefoot_Abduction)'] =  np.random.choice( a=[1,0], size=noa, p=[0.148,0.852])
    fitfeet['Right_Basic_Gait_Analysis(Forefoot_Adduction)'] =  np.random.choice( a=[1,0], size=noa, p=[0.034,0.966])
    fitfeet['Right_Basic_Gait_Analysis(Early_Heel)'] =  np.random.choice( a=[1,0], size=noa, p=[0.024,0.976])
 
    fitfeet['Nail(Normal)'] =  np.random.choice( a=[1,0], size=noa, p=[0.575,0.425])
    fitfeet['Nail(Wrong nail cut)'] =  np.random.choice( a=[1,0], size=noa, p=[0.232,0.768])
    fitfeet['Nail(Hematoma (bruise))'] =  np.random.choice( a=[1,0], size=noa, p=[0.013,0.987])
    fitfeet['Nail(Lesion)'] =  np.random.choice( a=[1,0], size=noa, p=[0.023,0.977])
    fitfeet['Nail(Discoloration)'] =  np.random.choice( a=[1,0], size=noa, p=[0.097,0.903])
    fitfeet['Nail(Split_and_laceration)'] =  np.random.choice( a=[1,0], size=noa, p=[0.036,0.964])
    fitfeet['Nail(Thick)'] =  np.random.choice( a=[1,0], size=noa, p=[0.059,0.941])
    fitfeet['Nail(Yellow)'] =  np.random.choice( a=[1,0], size=noa, p=[0.071,0.929])
    fitfeet['Nail(Black)'] =  np.random.choice( a=[1,0], size=noa, p=[0.033,0.967])
    fitfeet['Nail(White)'] =  np.random.choice( a=[1,0], size=noa, p=[0.025,0.975])
    fitfeet['Nail(Blister)'] =  np.random.choice( a=[1,0], size=noa, p=[0.001,0.999])
    fitfeet['Nail(Crumbly)'] =  np.random.choice( a=[1,0], size=noa, p=[0.029,0.971])
    fitfeet['Nail(Ingrown)'] =  np.random.choice( a=[1,0], size=noa, p=[0.07,0.93])
     
    fitfeet['Skin(Normal)'] =  np.random.choice( a=[1,0], size=noa, p=[0.556,0.444])
    fitfeet['Skin(Calluses)'] =  np.random.choice( a=[1,0], size=noa, p=[0.141,0.859])
    fitfeet['Skin(Warts)'] =  np.random.choice( a=[1,0], size=noa, p=[0.007,0.993])
    fitfeet['Skin(Blisters)'] =  np.random.choice( a=[1,0], size=noa, p=[0.025,0.975])
    fitfeet['Skin(Maceration)'] =  np.random.choice( a=[1,0], size=noa, p=[0.042,0.958])
    fitfeet['Skin(Split_or_cracks)'] =  np.random.choice( a=[1,0], size=noa, p=[0.054,0.946])
    fitfeet['Skin(Redness)'] =  np.random.choice( a=[1,0], size=noa, p=[0.043,0.957])
    fitfeet['Skin(Moist)'] =  np.random.choice( a=[1,0], size=noa, p=[0.07,0.93])
    fitfeet['Skin(Dry)'] =  np.random.choice( a=[1,0], size=noa, p=[0.09,0.91])
    fitfeet['Skin(Odor)'] =  np.random.choice( a=[1,0], size=noa, p=[0.023,0.977])
    fitfeet['Skin(Ulcers)'] =  np.random.choice( a=[1,0], size=noa, p=[0.003,0.997])
    fitfeet['Skin(Papules_(bumps))'] =  np.random.choice( a=[1,0], size=noa, p=[0.016,0.984])
    fitfeet['Skin(Nevus_(birthmark))'] =  np.random.choice( a=[1,0], size=noa, p=[0.034,0.966])
    fitfeet['Skin(Rash)'] =  np.random.choice( a=[1,0], size=noa, p=[0.012,0.988])
    fitfeet['Skin(Soft_tissue_mass)'] =  np.random.choice( a=[1,0], size=noa, p=[0.004,0.996])
    fitfeet['Skin(Corns)'] =  np.random.choice( a=[1,0], size=noa, p=[0.058,0.942])
 
    fitfeet['Foot_and_Bone(Normal)'] =  np.random.choice( a=[1,0], size=noa, p=[0.722,0.278])
    fitfeet['Foot_and_Bone(Crossover_toe)'] =  np.random.choice( a=[1,0], size=noa, p=[0.046,0.954])
    fitfeet['Foot_and_Bone(Clawtoes)'] =  np.random.choice( a=[1,0], size=noa, p=[0.037,0.963])
    fitfeet['Foot_and_Bone(Brachymetarsia(Short_toe))'] =  np.random.choice( a=[1,0], size=noa, p=[0.022,0.978])
    fitfeet['Foot_and_Bone(Bunions)'] =  np.random.choice( a=[1,0], size=noa, p=[0.066,0.934])
    fitfeet['Foot_and_Bone(Tailors_Bunion)'] =  np.random.choice( a=[1,0], size=noa, p=[0.008,0.992])
    fitfeet['Foot_and_Bone(Hallux_rigidus_or_limitus(Stiff_big_toe))'] =  np.random.choice( a=[1,0], size=noa, p=[0.044,0.956])
    fitfeet['Foot_and_Bone(Neuralgia(pinched_nerve))'] =  np.random.choice( a=[1,0], size=noa, p=[0.001,0.999])
    fitfeet['Foot_and_Bone(Haglunds(bone_deformity_on_back_of_heel))'] =  np.random.choice( a=[1,0], size=noa, p=[0.003,0.997])
    fitfeet['Foot_and_Bone(Exostosis(formation_of_new_bone))'] =  np.random.choice( a=[1,0], size=noa, p=[0.009,0.991])
    fitfeet['Foot_and_Bone(Hammertoes)'] =  np.random.choice( a=[1,0], size=noa, p=[0.027,0.973])

    return fitfeet

def hist_dict(array):
    res = dict()
    for i in array:
        if i in res:
            res[i] += 1
        else:
            res[i] = 1
    return res

fitfeet = numeric_data()

''' group by country '''
summary = dict()

for columnname in fitfeet: ## 对每一列进行统计
    summary[columnname] = pd.DataFrame(index = name)
     
    for country in name: ## group by 每一个国家
        ind = np.where(fitfeet['country'].values == country)
        tempdata = fitfeet.loc[ind[0], columnname]
        for k,v in hist_dict(tempdata.values).iteritems(): ## 对每个国家/列数据进行hist频率统计
            summary[columnname].loc[country, k] = v
    
writer = pd.ExcelWriter('fitfeet.xlsx')
fitfeet.to_excel(writer, 'data')

for k, v in summary.iteritems():
    if len(k) > 31: ## 长于31位的字符串不能作为sheetname
        k = k[0:31]
    v.to_excel(writer, k)
writer.save()