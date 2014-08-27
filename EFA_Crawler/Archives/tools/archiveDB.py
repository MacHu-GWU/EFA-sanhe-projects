##coding=utf8
##Date  =2014-08-21
##Author=Sanhe

import hashlib
import os
import sqlite3
import datetime, time

class ArchiveDB(object):
    def __init__(self, path):
        self.conn = sqlite3.connect(path)
        self.c = self.conn.cursor()
        
    def _initial(self):
        try:
            cmd = \
            """
            CREATE TABLE death_records
            (
            ID TEXT PRIMARY KEY NOT NULL,
            lastname TEXT NOT NULL,
            firstname TEXT NOT NULL,
            dob DATE NOT NULL,
            dod DATE NOT NULL,
            location TEXT,
            state TEXT,
            collection TEXT)
            """
            self.c.execute(cmd)
            self.conn.commit()
        except:
            print '表已存在，跳过initialization'
            
    def prt_all(self):
        for row in self.c.fetchall():
            print row
    
    def insertmany(self, tablename, records): # insert, if duplicate, then ignore
        self.c.executemany("INSERT OR IGNORE INTO %s VALUES (?,?,?,?,?,?,?,?)" % tablename, records)
    
    def commit(self):
        self.conn.commit()
    
        
def unit_test():
    adb = ArchiveDB('test.db')
    adb._initial()
    adb.c.execute("SELECT * FROM death_records")
    adb.prt_all()
     
    records = [('938fbe90afcef78f827a7cc96cb4389f', 'Smith', u'Tyrone E.', '1959-05-05', '2011-07-17', u'Henderson, Clark County, NV', u'NV', u'Nevada Death Index'),
                ('24e0e4df25af83e9871b5a01f95d07b9', 'Smith', u'Wilbur L.', '1932-12-12', '2011-07-15', u'Winnemucca, Humboldt County, NV', u'NV', u'Nevada Death Index'),
                ('8b8f85585c42866e200f24758b41e774', 'Smith', u'Dorothy', '1920-12-12', '2011-07-08', u'Las Vegas, Clark County, NV', u'NV', u'Nevada Death Index'),
                ('f8bb94ef6e61f1a1911f529847a8627e', 'Smith', u'James L.', '1946-08-08', '2011-07-16', u'Reno, Washoe County, NV', u'NV', u'Nevada Death Index'),
                ('128a3258978fba592e66e43ff7077546', 'Smith', u'Blanche', '1944-12-12', '2011-07-20', u'Henderson, Clark County, NV', u'NV', u'Nevada Death Index'),
                ('8c2439bfa5491aa005b81bb63840257e', 'Smith', u'Joni R.', '1957-01-01', '2011-07-19', u'Fernley, Lyon County, NV', u'NV', u'Nevada Death Index'),
                ('71d3facb87e8bf9427510c2a7aae28b8', 'Smith', u'Julie A.', '1964-06-06', '2011-05-12', u'Las Vegas, Clark County, NV', u'NV', u'Nevada Death Index'),
                ('7bf80542a6009345c71ad86d5bc9bf0a', 'Smith', u'Frederick M.', '1940-08-08', '2011-07-16', u'Las Vegas, Clark County, NV', u'NV', u'Nevada Death Index'),
                ('cc506d1cad3be0f2bbbbf779ff82199c', 'Smith', u'Gladys G.', '1922-11-11', '2011-07-27', u'Reno, Washoe County, NV', u'NV', u'Nevada Death Index'),
                ('859bb2458bd487da38890dd59b6c2674', 'Smith', u'Edmund C.', '1927-11-11', '2011-08-04', u'Las Vegas, Clark County, NV', u'NV', u'Nevada Death Index')]
     
    adb.insertmany('death_records', records)
    adb.c.execute("SELECT * FROM death_records")
    adb.prt_all()
    adb.commit()
    
if __name__ == '__main__':
    unit_test()