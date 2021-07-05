import pymysql
from config import DB_INFO
import datetime

class DB:
    def __init__(self, table_name):
        self.table_name = table_name
        self.db = pymysql.connect(host=DB_INFO.HOST, user=DB_INFO.USER, password=DB_INFO.PASSWORD, database=DB_INFO.DATABASE)
        self.cursor = self.db.cursor()

    def insert(self, record):
        # record as dictionary, for example record = { 'id': '163388383', 'firstname': 'Canh', 'lastname': 'Pham'}
        cols = ','.join([key for key in record.keys()])
        values = ','.join(["'%s'" % record[key] for key in record.keys()])
        self.cursor.execute("insert into %s(%s) values(%s)" % (self.table_name, cols, values))
        self.db.commit()
        self.db.close()

    def select(self, record_id, cols_fm):
        self.cursor.execute("select %s from %s where id=%d" % (cols_fm, self.table_name, record_id))
        record = self.cursor.fetchone()
        return record

    def update(self, record_id, col, value):
        self.cursor.execute("update %s set %s = '%s' where id = %d" % (self.table_name, col, value, record_id))
        self.db.commit()

