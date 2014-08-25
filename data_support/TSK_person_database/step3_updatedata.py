##coding=utf8
from person import *
import numpy as np
import sqlite3
import random, itertools

def prt_all(c):
    for row in c.fetchall():
        print row

def count_number_of_row(c, tablename):
    c.execute("SELECT count(*) FROM (SELECT * FROM %s);" % tablename)
    return c.fetchall()[0][0]
    
def main():
    conn = sqlite3.connect(r'C:\Users\Sanhe.Hu\Data_warehouse\TSA\TSA_person.db')
    c = conn.cursor()
    
    print count_number_of_row(c, 'person')
    
    c.execute("SELECT id, lastname FROM person")
    counter = itertools.count(0)
    for id, lastname in c.fetchall(): # 给所有的person 更新人际关系
        ## n1 = lastname一致的关系，n2 = 其他关系
        while 1:
            n1, n2 = int( np.random.randn() * 3 + 10 ), int( np.random.randn() * 50 + 200 )
            if (n1 >= 1) & (n2 >= 3):
                break
        ## n1 对应的 id
        c.execute("""SELECT id FROM person WHERE lastname = "%s" ;""" % lastname)
        relation1 = [str(row[0]) for row in random.sample(c.fetchall(), n1)]
        ## n2 对应的 id
        c.execute("""SELECT id FROM person;""")
        relation2 = [str(row[0]) for row in random.sample(c.fetchall(), n2)]        
        SN = '&'.join(['&'.join(relation1), '&'.join(relation2)])
        ## update social_network
        c.execute("UPDATE person SET social_network = ? WHERE id = ?", (SN, id))
        print counter.next()
    conn.commit()
    conn.close()
    
if __name__ == '__main__':
    main()