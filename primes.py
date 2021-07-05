import random, math
import time

def isPropbablyPrime(n, k=128):
    ''' Check if a number n is prime or not using Miller-Rabin primality test '''
    k = int(math.log2(n))
    # find s and m such that n - 1 = 2^s * m, m is odd
    m = n - 1
    s = 0
    while not m & 1:
        m >>= 1
        s += 1

    for i in range(k):
        a = random.randint(2, n - 1)
        b = pow(a, m, n)
        if b % n == 1:
            break
        else:
            for j in range(s+1):
                if b % n == n - 1:
                    break
                b = pow(b, 2, n)
                if j == s:
                    return False
    return True


def generatePrime(size=1024):
    while True:
        num = random.getrandbits(size)
        num |= (1 << size - 1) | 1
        if isPropbablyPrime(num):
            return num