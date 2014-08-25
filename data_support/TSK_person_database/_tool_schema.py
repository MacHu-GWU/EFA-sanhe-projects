##coding=utf8
import sqlite3
import os

class Database(object):
    def __init__(self, name):
        self.name = name
        self.tables = dict()
        
    def __str__(self):
        return '========================== DATABASE info ==========================\ndatabase name = "' \
        + self.name + '"\n=== list of table name ===\n' + '\n'.join(self.tables)

    def __getattr__(self, item):
        if item not in ['name', 'tables']:
            return self.tables[item]
    
class Table(object):
    def __init__(self, name):
        self.name = name
        self.columns = list()
        self.amount = 0
        
    def __str__(self):
        tableinfo = 'table name = %s, column number = %s, entry number = %s\n' \
                    % (self.name, len(self.columns), self.amount)
        columnsinfo = ['{0[0]:<20}{0[1]:<15}{0[2]:<2}'.format(('COLUMN NAME', ##字符美化输出
                                                               'TYPE',
                                                               'IS PRIMARY KEY'))]
        for column in self.columns:
            columnsinfo.append('{0[0]:<20}{0[1]:<15}{0[2]:<2}'.format(column))
        return '========================== TABLE info ==========================\n' + \
            tableinfo + '\n'.join(columnsinfo)

def get_schema(dbname):
    name, _ = os.path.splitext(dbname) ## 拆分文件名，得到数据库名
    conn = sqlite3.connect(dbname) ## 连接数据库
    crs = conn.cursor() ## 创建游标
    ## >> 获得数据中所有表的名字 << ##
    crs.execute("SELECT name FROM sqlite_master WHERE type='table';")
    db = Database(name) ## 创建db对象
    for tablename in crs.fetchall(): ## 给db信息中添加table的信息
        table = Table(tablename[0]) ## 根据表名称，创建表对象
        ## >> 不经过SELECT *, 得到表中所有列的属性细节 << ##
        crs.execute("PRAGMA table_info(%s)" %(tablename[0])) ## 取得列信息
        for info in crs.fetchall(): ## 填写 table.columns
            table.columns.append((str(info[1]), str(info[2]), str(info[5]))  )
        crs.execute("SELECT count(*) FROM %s" %(tablename[0]))
        table.amount = crs.fetchone()[0] ## 填写 table.amount
        db.tables[tablename[0]] = table
    return db

if __name__ == "__main__":
    db = get_schema('EMR.db')
    print db 
    print db.patient