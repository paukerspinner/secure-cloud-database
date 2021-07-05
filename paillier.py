import primes
import random
import modulo


class PublicKey:
    def __init__(self, n = None, g = None):
        self.n = n
        self.g = g
        self.n_sq = n * n if n else None
    def generate(self, p, q):
        self.n = p * q
        self.g = self.n + 1
        self.n_sq = self.n * self.n
    def show(self):
        print('n = %d' % self.n)
        print('g = %d' % self.g)

class PrivateKey:
    def __init__(self, p, q):
        self.l = (p - 1) * (q - 1)
        n = p * q
        self.m = modulo.invmod(self.l, n)
    def show(self):
        print('l = %d' % self.l)
        print('m = %d' % self.m)


def generateNewKeys(size):
    p =primes.generatePrime(size >> 1)
    q = primes.generatePrime(size >> 1)
    print(p)
    print(q)
    pub_key = PublicKey()
    pub_key.generate(p, q)
    pub_key.show()
    pri_key = PrivateKey(p, q)
    pri_key.show()
    return [pub_key, pri_key]

def encrypt(plain, pub_key: PublicKey):
    r = random.randint(1, pub_key.n)
    # c = g^m * r^n % n^2 = ((g^m % n^2) * (r^n % n^2)) % n^2 = (c1 * c2) % n^2
    c1 = pow(pub_key.g, plain, pub_key.n_sq)
    c2 = pow(r, pub_key.n, pub_key.n_sq)
    cipher = c1 * c2 % pub_key.n_sq
    return cipher

def decrypt(cipher, pub_key: PublicKey, pri_key: PrivateKey):
    x = pow(cipher, pri_key.l, pub_key.n_sq)
    Lx = (x - 1) // pub_key.n
    plain = Lx * pri_key.m % pub_key.n
    return plain

def e_add(cipher_1, cipher_2, pub_key: PublicKey):
    return cipher_1 * cipher_2 % pub_key.n_sq

def e_mul_const(cipher, constant, pub_key: PublicKey):
    return pow(cipher, constant, pub_key.n_sq)

def getBitOfPos(num, pos):
    return (num >> pos) & 1
