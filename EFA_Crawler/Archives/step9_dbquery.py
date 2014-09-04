##coding=utf8

import sqlite3
import time
conn = sqlite3.connect(r'C:\Users\Sanhe.Hu\Data_warehouse\Archives\archive.db')
c = conn.cursor()

# c.execute("SELECT count(*) FROM (SELECT * FROM death_records)")
# c.execute("SELECT * FROM death_records WHERE lastname = 'Johnson'")
c.execute("SELECT distinct lastname FROM death_records")
for row in c.fetchall():
    print row