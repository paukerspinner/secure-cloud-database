import random, sys, time
from paillier import PublicKey, PrivateKey, encrypt, decrypt, e_add
import pymysql
import env
import fm

db = pymysql.connect(host="localhost", user="pauker", password="Canh1997", database="vkr")

cursor = db.cursor()

# id = int(input('id: '))
name = fm.convertTextToBigInt(input('Name: '))
salary = int(input('Salary: '))
bonus = int(input('Bonus: '))

# fn = fm.convertTextToBigInt(input('fn: '))
# ln = fm.convertTextToBigInt(input('ln: '))

pub_key = PublicKey(env.p, env.q)
priv_key = PrivateKey(env.p, env.q)


record = {
    # 'id': id,
    'name': encrypt(name, pub_key),
    'salary': encrypt(salary, pub_key),
    'bonus': encrypt(bonus, pub_key)
}



cols = ','.join([key for key in record.keys()])
values = ','.join(["'%s'" % record[key] for key in record.keys()])

x = cursor.execute("insert into employees(" + cols +  ") values(" + values + ")")

db.commit()

db.close()