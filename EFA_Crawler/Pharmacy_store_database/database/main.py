##coding=utf8
import sqlite3
from sqlite3_schema import Database_schema



def prt_all(c):
    for row in c.fetchall():
        print row
    

conn = sqlite3.connect('test.db')
c = conn.cursor()
cmd = \
'''
CREATE TABLE test
(name TEXT)
'''
# c.execute(cmd)

c.execute("INSERT INTO test VALUES (?)", ("ABC'D",))
c.execute("SELECT * FROM test")
prt_all(c)













# if __name__ == '__main__':
#     initial()