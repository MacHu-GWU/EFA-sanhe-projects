##coding=utf8
import hashlib
import pickle
import os
import pprint

def is_valid_email(email):
    '''笨办法验证是否是valid_email，返回boolean
    '''
    if type(email) != str: # 是string
        print email, ', not string!'
        return False
    elif email.count('@') != 1: # 有@在中间
        print email, ', cannot find @!'
        return False
    ## 当@前的字母少于1，或@后的字符少于6
    elif (email.find('@') < 1) + (len(txt) - txt.find('@') - 1 < 5) : # '@'前面的字符少于1个，或者后面的字符少于5个
        print email, ', @ not in the middle!'
        return False
    elif email.split('.').pop() not in ['com','net','org','edu']: # 是以com, net, org, edu结尾
        print email, ', not end with com/net/org/edu!'
        return False
    else:
        print email, 'is a valid email.'
        return True
 
def sign_up(signup_table):
    ## load username list
    if os.path.exists('user_acc.p'):
        user_acc = pickle.load(open('user_acc.p', 'rb'))
    else:
        user_acc = dict()
    ## check if sign up info is valid
    if signup_table['username'] in list(user_acc.keys()): ## 检查：用户名是否已被注册
        print 'username = %s already exist' % signup_table['username']
        return None
    elif signup_table['pwd'] != signup_table['repeat_pwd']: # 检查：两次输入的密码是否匹配
        print 'pwd not match'
        return None
    elif not is_valid_email(signup_table['email']): # 检查：是否是有效的email
        print 'not a valid email'
        return None
    else:
        print 'sign up success'
        user_acc[signup_table['username']] = \
        {'pwd':hashlib.sha512(signup_table['pwd']).hexdigest(),
         'email':signup_table['email']}
        pickle.dump(user_acc, open('user_acc.p', 'wb'))
        return None
    
def display_accDB():
    '''显示密码数据库
    '''
    user_acc = pickle.load(open('user_acc.p', 'rb'))
    pprint.pprint(user_acc)


signup_table = dict()
signup_table['username'] = 'sanhe.hu'
signup_table['pwd'] = '123456'
signup_table['repeat_pwd'] = '123456'
signup_table['email'] = 'sanhe.hu@theeagleforce.net'
sign_up(signup_table)

# display_accDB()