# coding=utf8
# fitbit 测试账号信息
# acc = 'variganti@gmail.com'
# pwd = 'Test23'

import pprint as ppt
import json
import fitbit

authd_client = fitbit.Fitbit('94a2b2a7da56414ab73b8fb8b85c1e64', 
                             '116e8f7682654b39bc75fd1004a6072d', 
                             resource_owner_key = '08dbe24aba7ba824b60ffabf2c0f219a', ## resource_owner_key 和 resource_owner_secret
                             resource_owner_secret = '218d3283ae8bf531a3729d40f6142526') ## 需要运行 gather_info.py 才能获取
'''
FOOD
foods/log/caloriesIn    
foods/log/water

ACTIVITY
activities/calories
activities/caloriesBMR
activities/steps
activities/distance
activities/floors
activities/elevation
activities/minutesSedentary
activities/minutesLightlyActive    
activities/minutesFairlyActive
activities/minutesVeryActive
activities/activityCalories

activities/tracker/calories
activities/tracker/steps
activities/tracker/distance
activities/tracker/floors
activities/tracker/elevation
activities/tracker/minutesSedentary
activities/tracker/minutesLightlyActive    
activities/tracker/minutesFairlyActive
activities/tracker/minutesVeryActive
activities/tracker/activityCalories   

SLEEP
sleep/startTime
sleep/timeInBed
sleep/minutesAsleep
sleep/awakeningsCount    
sleep/minutesAwake
sleep/minutesToFallAsleep
sleep/minutesAfterWakeup
sleep/efficiency

BODY
body/weight    
body/bmi
body/fat
'''

data = authd_client.time_series('activities/tracker/steps', user_id = '2Q9QDM', base_date = '2014-06-07', period = '7d')
ppt.pprint(data)
