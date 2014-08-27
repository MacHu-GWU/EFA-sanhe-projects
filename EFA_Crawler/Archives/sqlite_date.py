import sqlite3
import datetime

def prt_all(c):
    for row in c.fetchall():
        print row

this_year = (datetime.date(datetime.date.today().isocalendar()[0], 1, 1))
print this_year, type(this_year)

con = sqlite3.connect("database.db")
c = con.cursor()
# c.execute("create table test(id Integer,d date)")
c.execute("insert into test(id, d) values (?, ?)", (1, '2010-01-15'))
c.execute("insert into test(id, d) values (?, ?)", (1, '2010-01-20'))
c.execute("SELECT * FROM test WHERE d >= ? AND d <= ?", ( datetime.date(2010,01,17), datetime.date(2010,01,19)) )
prt_all(c)


# con = sqlite3.connect("database.db", detect_types=sqlite3 .PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
# c = con.cursor()

# c.execute("create table test(id Integer,d date)")


# c.execute("insert into test(id, d) values (?, ?)", (1, datetime.date(2010, 1, 15)))
# c.execute("SELECT * FROM test WHERE d = datetime.date(2010, 1, 15)")
# prt_all(c)



# today = datetime.date.today()
# now = datetime.datetime.now()
# 
# cur.execute("insert into test(d, ts) values (?, ?)", (today, now))
# cur.execute("select d, ts from test")
# row = cur.fetchone()
# print today, "=>", row[0], type(row[0])
# print now, "=>", row[1], type(row[1])
# 
# cur.execute('select current_date as "d [date]", current_timestamp as "ts [timestamp]"')
# row = cur.fetchone()
# print "current_date", row[0], type(row[0])
# print "current_timestamp", row[1], type(row[1])
# 
# cur.execute("SELECT * FROM test")
# for row in cur.fetchall():
#     print row