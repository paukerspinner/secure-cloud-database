import db
import fm
from paillier import PublicKey, e_add
import env

def insert(table_name, record):
    table_db = db.DB(table_name)
    table_db.insert(record)

def select(table_name, record_id):
    pub_key = PublicKey(env.n, env.g)
    table_db = db.DB(table_name)
    record = table_db.select(record_id, '*')
    return record

def compute_add(table_name, record_id, col_1, col_2):
    pub_key = PublicKey(env.n, env.g)
    table_db = db.DB(table_name)
    record = table_db.select(record_id, '%s, %s' % (col_1, col_2))
    col_1_value = int(record[0])
    col_2_value = int(record[1])
    return e_add(col_1_value, col_2_value, pub_key)

