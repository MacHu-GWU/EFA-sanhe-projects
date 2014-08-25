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
    
def evaluate(id):
    conn = sqlite3.connect(r'C:\Users\Sanhe.Hu\Data_warehouse\TSA\TSA_person.db')
    c = conn.cursor()
    
    print count_number_of_row(c, 'person')
    
    c.execute("SELECT lastname FROM person WHERE id = %s" % id)
    lastname = c.fetchone()[0]

    while 1:
        n1, n2 = int( np.random.randn() * 3 + 10 ), int( np.random.randn() * 50 + 200 )
        if (n1 >= 1) & (n2 >= 3):
            break
    ## n1 对应的 id
    c.execute("""SELECT id FROM person WHERE lastname = "%s" ;""" % lastname)
    relation1 = [row[0] for row in random.sample(c.fetchall(), n1)]
    ## n2 对应的 id
    c.execute("""SELECT id FROM person;""")
    relation2 = [row[0] for row in random.sample(c.fetchall(), n2)]
    relation = relation1 + relation2
    
    num_of_danger_relations = 0 
    for ii in relation:
        c.execute("SELECT basic_score FROM person WHERE id = %s" % ii)
        basic_score = c.fetchone()[0]
        if basic_score >= 60:
            num_of_danger_relations += 1
    print num_of_danger_relations, len(relation)
    
        ## update social_network
#         c.execute("UPDATE person SET social_network = ? WHERE id = ?", (SN, id))
#         print counter.next()
#     conn.commit()
#     conn.close()

def query(lastname = '', firstname = ''):
    conn = sqlite3.connect(r'C:\Users\Sanhe.Hu\Data_warehouse\TSA\TSA_person.db')
    c = conn.cursor()
    if firstname == '':
        c.execute("""SELECT * FROM person WHERE lastname = "%s" """ % lastname)
    else:
        c.execute("""SELECT * FROM person WHERE lastname = "%s", firstname = "firstname" """ % (lastname, firstname))
    prt_all(c)
    
if __name__ == '__main__':
    evaluate(1)
#     query('Smith')
#     conn = sqlite3.connect(r'C:\Users\Sanhe.Hu\Data_warehouse\TSA\TSA_person.db')
#     c = conn.cursor()
#     c.execute("SELECT * FROM person")
#     prt_all(c)