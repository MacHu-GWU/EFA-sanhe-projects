##coding=utf8

import faker
import sqlite3
from _tool_schema import get_schema
        
conn = sqlite3.connect(r'C:\Users\Sanhe.Hu\Data_warehouse\TSA\TSA_person.db')
c = conn.cursor()
''' CREATE TABLE '''
try:
    cmd = \
    """
    CREATE TABLE person
    (id INTEGER PRIMARY KEY NOT NULL,
    lastname TEXT,
    firstname TEXT,
    social_network TEXT,
    International_Terrorist_Watch_List INTEGER,
    National_Terrorist_Watch_List INTEGER,
    National_Law_Enforcement INTEGER,
    Local_Law_Enforcement INTEGER,
    IRS_or_other_Federal_Finance_Company INTEGER,
    Face_Match_with_Picture_DB INTEGER,
    Cash_Payment_Same_Day INTEGER,
    Immediate_Family INTEGER,
    Extented_Family INTEGER,
    Place_of_Worship INTEGER,
    basic_score REAL,
    bonus_score REAL,
    score INTEGER)
    """
 
    c.execute(cmd)
    conn.commit()
    conn.close()
except:
    print 'cannot create table!'
    
db = get_schema(r'C:\Users\Sanhe.Hu\Data_warehouse\TSA\TSA_person.db')
print db
print db.person