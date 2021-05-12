import random, sys, time
from paillier import PublicKey, PrivateKey, encrypt, decrypt
import pymysql
import env
import fm


pub_key = PublicKey(env.p, env.q)
priv_key = PrivateKey(env.p, env.q)

priv_key.show()

name = fm.convertTextToBigInt(input('Name: '))
print(name)
cp_name = encrypt(name, pub_key)
rv_name = decrypt(cp_name, pub_key, priv_key)
rv_name = fm.convertBigIntToText(rv_name)
print(rv_name)


# salary = int(input('Salary: '))
# cp_salary = encrypt(salary, pub_key)
# rv_salary = decrypt(cp_salary, pub_key, priv_key)
# print(rv_salary)
