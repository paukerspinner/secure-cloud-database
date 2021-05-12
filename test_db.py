import db
import fm
from paillier import PublicKey, PrivateKey, encrypt, decrypt, e_add
import env


name = fm.convertTextToBigInt(input('Name: '))
salary = int(input('Salary: '))
bonus = int(input('Bonus: '))

# fn = fm.convertTextToBigInt(input('fn: '))
# ln = fm.convertTextToBigInt(input('ln: '))

pub_key = PublicKey(env.n, env.g)
priv_key = PrivateKey(env.p, env.q)


record = {
    # 'id': id,
    'name': encrypt(name, pub_key),
    'salary': encrypt(salary, pub_key),
    'bonus': encrypt(bonus, pub_key)
}

employees_db = db.DB('employees')
employees_db.insert(record)
