import datetime
from random import randint
import fm
from paillier import PublicKey, PrivateKey, encrypt, decrypt
import env
import server

def analyze_insert_query():
    i = 1
    start_time = datetime.datetime.now()
    delta = datetime.datetime.now() - start_time
    while delta.total_seconds() < 1:
        id = i
        name = fm.convertTextToBigInt('My Name')
        salary = 12000
        bonus = 2000
        record = {
            'id': id,
            'name': encrypt(name, pub_key),
            'salary': encrypt(salary, pub_key),
            'bonus': encrypt(bonus, pub_key)
        }
        server.insert('employees', record)
        i = i + 1
        delta = datetime.datetime.now() - start_time
    print(i)

def analyze_select_query():
    i = 1
    start_time = datetime.datetime.now()
    delta = datetime.datetime.now() - start_time
    while delta.total_seconds() < 1:
        id = randint(1, 50)
        record = server.select('employees', id)
        name = fm.convertBigIntToText(decrypt(int(record[1]), pub_key, priv_key))
        salary = decrypt(int(record[2]), pub_key, priv_key)
        bonus = decrypt(int(record[3]), pub_key, priv_key)
        i = i + 1
        delta = datetime.datetime.now() - start_time
    print(i)

def analyze_select_query_with_addition():
    i = 1
    start_time = datetime.datetime.now()
    delta = datetime.datetime.now() - start_time
    while delta.total_seconds() < 1:
        id = randint(1, 50)
        earning_cp = server.compute_add('employees', id, 'salary', 'bonus')
        earning = decrypt(earning_cp, pub_key, priv_key)
        i = i + 1
        delta = datetime.datetime.now() - start_time
    print(i)

def analyze_update_query_with_multiplication():
    i = 1
    start_time = datetime.datetime.now()
    delta = datetime.datetime.now() - start_time
    while delta.total_seconds() < 1:
        id = randint(1, 50)
        server.update_mul('employees', id, 'bonus', 2)
        i = i + 1
        delta = datetime.datetime.now() - start_time
    print(i)

pub_key = PublicKey(env.n, env.g)
priv_key = PrivateKey(env.p, env.q)


# analyze_insert_query()
# analyze_select_query()
# analyze_select_query_with_addition()
# analyze_update_query_with_multiplication()