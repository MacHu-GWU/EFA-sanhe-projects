##CODING=utf8
'''
INPUT
1. Age                                   mandatory
2. Gender                                mandatory
3. Years of Smoking                      mandatory
4. Cigarette per day(CPD)                mandatory
5. COPD level(0/1/2/3/4)                 mandatory
possible OUTPUT
1. you have to reduce your CPD to...
2. you have to quit smoking...
3. you have to walk at least X miles per day.
'''
def first_login_suggest(form):
    age, gender, yos, cpd, copd = form
    quit_smoking = 0
    reduce_cpd = 0
    msg_quit_smoking = ""
    msg_reduce_cpd = ""
    msg_walking = ""
    ''' QUIT SMOKING '''
    if copd >= 3: ## if he is level 3 or 4
        if yos > 0: ## if he smoke
            quit_smoking = 1
            msg_quit_smoking = "1. You have been diagnosed with a very severe case of COPD. Please consider quitting smoking, exercising more, and living a healthier lifestyle."
    ''' reduce_cpd '''
    if copd >= 1: ## if he is level 1 or 2
        if yos > 0: ## if he smoke
            if cpd >= 10: ## if he smoke a lot
                reduce_cpd = 1
                msg_reduce_cpd = "1. It would be smart to consider quitting smoking; starting with a reduction of about 5, to 7, cigarettes a day."
            elif cpd >= 6: ## if he smoke not too much
                reduce_cpd = 1
                msg_reduce_cpd = "1. It would be smart to consider quitting smoking; starting with a reduction of about 3, to 5, cigarettes a day."
            else: ## if he smoke only a little: 1 ~ 5
                reduce_cpd = 1
                msg_reduce_cpd = "1. It would be smart to consider quitting smoking; starting with a reduction of 1, to 3, cigarettes a day."
    if copd == 0:
        if yos > 0:
            reduce_cpd = 1
            msg_reduce_cpd = "Your symptoms indicate that you are close to a COPD diagnosis. It would be smart to consider quitting or at least reducing your tobacco intake." 
    ''' walking '''
    if copd == 0:
        msg_walking = "2. It would be smart to keep exercising, maybe even consider walking up to 1000 more steps a day (if possible)."
    if copd == 1:
        msg_walking = "2. Because of your diagnosis; you should consider exercising more frequently."
    if copd == 2:
        msg_walking = "2. Because of your diagnosis; it would be smart to set up a workout plan, and try to exercise every day."
    if copd == 3:
        msg_walking = "2. Your diagnosis suggests that you workout more frequently, and try to walk about 1000 more steps a day (if possible)."
    if copd == 4:
        msg_walking = "2. Your diagnosis suggests that you need more exercise. If possible you should consider a workout plan, and attempt to stretch, walk, or run more frequently."
    ''' Generate MSG '''
    msg = ['=============== Suggestion ===============']
    if quit_smoking:
        msg.append(msg_quit_smoking)
    elif reduce_cpd:
        msg.append(msg_reduce_cpd)
    msg.append(msg_walking)
    return '\n'.join(msg)

def parser_5(survey_string):
    a,b,c,d,e = survey_string.strip().split(',')
    return (int(a), int(b), int(c), int(d), int(e))
    
if __name__ == '__main__':
    age = 85 ## age 70-100
    gender = 1 ## gender 0/1
    yos = 25 ## years of smoking >=0
    cpd = 10 ## cigarette per day >=0
    copd = 2 ## COPD level 0/1/2/3/4
    print first_login_suggest(parser_5('85,1,25,10,2'))
#     print first_login_suggest(age, gender, yos, cpd, copd)

