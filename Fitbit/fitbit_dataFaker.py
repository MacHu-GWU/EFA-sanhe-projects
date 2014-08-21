## coding=utf8
'''本程序用来生成人造fitbit数据
'''
import datetime
import numpy as np
import jsontree
import pprint as ppt

def normal( info ):
    return np.random.randn() * info[1] + info[0]

def daterange_gen(start,end):
    '''时间序列生成器
    Output: datetime.datetime object from start date to end date
    '''
    st_date = datetime.datetime.strptime(start, '%Y-%m-%d')
    et_date = datetime.datetime.strptime(end, '%Y-%m-%d')
    n = (et_date - st_date).days + 1
    delta = datetime.timedelta(days = 1)
    for i in range(n):
        yield st_date + i * delta

def strdt(dt):
    ''' stringlize date time in %Y-%m-%d '''
    return datetime.datetime.strftime(dt,'%Y-%m-%d')

''' step1 初始化数据 '''
uv_step = np.array([[2000,300], ## Monday
                    [5000,500], ## Tuesday
                    [2000,300], ## Wedsday
                    [6000,500], ## Thursday
                    [3000,400], ## Friday
                    [7500,1500], ## Saturday
                    [3000,400]]) ## Sunday

uv_cal = np.array([[0,1], ## Monday
                   [0,1], ## Tuesday
                   [0,1], ## Wedsday
                   [0,1], ## Thursday
                   [0,1], ## Friday
                   [0,1], ## Saturday
                   [0,1]]) ## Sunday

uv_mile = np.array([[0,1], ## Monday
                    [0,1], ## Tuesday
                    [0,1], ## Wedsday
                    [0,1], ## Thursday
                    [0,1], ## Friday
                    [0,1], ## Saturday
                    [0,1]]) ## Sunday

uv_vam = np.array([[0,1], ## Monday
                   [0,1], ## Tuesday
                   [0,1], ## Wedsday
                   [0,1], ## Thursday
                   [0,1], ## Friday
                   [0,1], ## Saturday
                   [0,1]]) ## Sunday

uv_step1, uv_cal1, uv_mile1, uv_vam1 = uv_step, uv_cal, uv_mile, uv_vam
step, cal, mile, vam = dict(), dict(), dict(), dict()

''' Step2 按照step的设置，生成正态分布数据 '''
pr = 0.1 ## 以 10% 的概率，打乱当周的作息规律
st, et = '2014-01-01', '2014-12-31'
keys = list()
for dt in daterange_gen(st, et):
    keys.append(strdt(dt))
    if np.random.rand() <= pr: ## shuffle 每周作息时间
        np.random.shuffle(uv_step1)
        step_value = normal(uv_step1[dt.weekday()])
        step[strdt(dt)] = step_value
    else: ## 按照标准作息时间来
        step_value = normal(uv_step[dt.weekday()])
        step[strdt(dt)] = step_value

''' Step3 随机选择部分日子，偷懒或者努力 '''
np.random.permutation(keys)
lazydays, workoutdays = keys[0:29], keys[30:44] ## 随机取30天作为lazyday, 15天作为workoutday

for i in lazydays: ## 这些天会偷懒
    step[i] = normal( [np.random.randint(1750, 2250), 300] )
for i in workoutdays: ## 这些天会努力
    step[i] = normal( [np.random.randint(7000, 9000), 1500] )

''' Step4 把step转换为cal和mile, 转换系数在小范围内服从正太分布 '''    
for k, v in step.iteritems():
    mile[k] = v/( normal( (2100, 50) ) )
    cal[k] = v/( normal( (22, 1) ) )   

#     vam.append( (dt, normal(uv_vam[dt.weekday()]) ) )

# ppt.pprint(step)

''' Step5 保存数据到本地文件 '''
data = {'step': step,
        'mile': mile,
        'calories': cal}
 
sdata = jsontree.dumps(data, sort_keys=True,indent=4,separators=(',' , ': '))
with open('fitbit2014.json', 'wb') as f:
    f.write(sdata)

