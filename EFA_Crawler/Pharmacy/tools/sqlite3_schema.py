##coding=utf8
import sqlite3
import os
from datetime import date

class Table(object):
    def __init__(self, name):
        self.name = name
        self.columns = list()
        self.amount = 0
        
    def __str__(self):
        tableinfo = 'table name = %s, column number = %s, entry number = %s\n' \
                    % (self.name, len(self.columns), self.amount)
        columnsinfo = ['{0[0]:<10}{0[1]:<20}{0[2]:<10}{0[3]:<10}{0[4]:<20}{0[5]:<10}'.format(('cID', ##字符美化输出
                                                                                             'COLUMN NAME',
                                                                                             'TYPE',
                                                                                             'NOT NULL',
                                                                                             'dflt_value',
                                                                                             'IS PRIMARY KEY'))]
        for column in self.columns:
            columnsinfo.append('{0[0]:<10}{0[1]:<20}{0[2]:<10}{0[3]:<10}{0[4]:<20}{0[5]:<10}'.format(column))
        return '=========================== TABLE info ============================\n' + \
            tableinfo + '\n'.join(columnsinfo)
            
class Database_schema(object): # sqlite3 database schema object
    def __init__(self, dbpath):
        name, _ = os.path.splitext(os.path.basename(dbpath) ) ## 拆分文件名，得到数据库名
        self.name = name 
        self.tables = dict()
        
        conn = sqlite3.connect(dbpath) ## 连接数据库
        crs = conn.cursor() ## 创建游标
        ## >> 获得数据中所有表的名字 << ##
        crs.execute("SELECT name FROM sqlite_master WHERE type='table';")
        for tablename in crs.fetchall(): ## 给db信息中添加table的信息
            table = Table(tablename[0]) ## 根据表名称，创建表对象
            ## >> 不经过SELECT *, 得到表中所有列的属性细节 << ##
            crs.execute("PRAGMA table_info(%s)" % tablename[0] ) ## 取得列信息
            for info in crs.fetchall(): ## 填写 table.columns
                table.columns.append((str(info[0]), 
                                      str(info[1]), 
                                      str(info[2]), 
                                      str(info[3]), 
                                      str(info[4]), 
                                      str(info[5]))  )
            crs.execute("SELECT count(*) FROM (SELECT * FROM %s);" % tablename[0] ) ## 快速得到表中数据条数
            table.amount = crs.fetchone()[0] ## 填写 table.amount
            self.tables[tablename[0]] = table
        
    def __str__(self):
        return '========================== DATABASE info ==========================\ndatabase name = "' \
        + self.name + '"\n=== list of table name ===\n' + '\n'.join(self.tables)

    def __getattr__(self, item):
        if item not in ['name', 'tables']:
            return self.tables[item]

def unit_test():
    try:
        conn = sqlite3.connect("records.db")
        c = conn.cursor()
        c.execute("CREATE TABLE test (id INTEGER PRIMARY KEY NOT NULL, name TEXT, enroll_date DATE)")
        c.execute("INSERT INTO test (id, name, enroll_date) VALUES (?, ?, ?)", (1, "Jack", date(2014,8,15)))
        conn.commit()
        conn.close()
    except:
        print 'DB already created, no need to create again'
    
    db_schema = Database_schema("records.db")
    print db_schema
    print db_schema.test
    
if __name__ == "__main__":
    unit_test()