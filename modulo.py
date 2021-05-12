import random

def invmod(num, mod):
    if mod == 1:
        raise ValueError('Modulo can not be 1.')

    r0 = num
    r1 = mod
    s0 = 1
    s1 = 0

    while r1:
        q = r0 // r1
        [r0, r1] = [r1, r0 - q * r1]
        [s0, s1] = [s1, s0 - q * s1]
    
    if r0 == 1:
        return s0
    else:
        raise ValueError('%d has no inverse mod %d' % (num, mod))