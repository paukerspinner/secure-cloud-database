import fm
from paillier import PublicKey, PrivateKey, encrypt, decrypt
import env
import server


pub_key = PublicKey(env.n, env.g)
priv_key = PrivateKey(env.p, env.q)

def insert_employee():
    print('*** Insert employee ***')
    id = int(input('Id: '))
    name = fm.convertTextToBigInt(input('Name: '))
    salary = int(input('Salary: '))
    bonus = int(input('Bonus: '))
    record = {
        'id': id,
        'name': encrypt(name, pub_key),
        'salary': encrypt(salary, pub_key),
        'bonus': encrypt(bonus, pub_key)
    }
    server.insert('employees', record)
    print("Successfully insert!")
    print(record)

def select_employee():
    print('*** Select employee ***')
    id = int(input('Id: '))
    record = server.select('employees', id)
    print(record)
    name = fm.convertBigIntToText(decrypt(int(record[1]), pub_key, priv_key))
    salary = decrypt(int(record[2]), pub_key, priv_key)
    bonus = decrypt(int(record[3]), pub_key, priv_key)
    print('(id, name, salary, bonus) = (%d, %s, %d, %d)' % (id, name, salary, bonus))
    # return (id, name, salary, bonus)

def select_employee_earning():
    ''' Get information (id, name, earning = salary + bonus) '''
    print('*** Compute the total earning (salary + bonus) ***')
    id = int(input('Id: '))
    earning_cp = server.compute_add('employees', id, 'salary', 'bonus')
    print('Before decrypt:', earning_cp)
    earning = decrypt(earning_cp, pub_key, priv_key)
    print('Earning (salary + bonus): %d' % earning)
    return earning

def duplicate_bonus():
    ''' Update bonus '''
    print('*** Duplicate bonus - Homomorphic multiplication of plaintexts ***')
    id = int(input('Id: '))
    server.update_mul('employees', id, 'bonus', 2)