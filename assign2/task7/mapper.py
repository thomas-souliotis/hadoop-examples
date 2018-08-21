#!/usr/bin/python3
import sys
import random
from hashlib import sha1
import math
from bitarray import bitarray

def hashRes(a,m):
    a = sha1(a.encode("utf-8")).digest()
    a = int.from_bytes(a, byteorder='big') % m
    return a


#initializing values
n = 1897987#int(sys.argv[1])
p = 0.01
m = -n*math.log(p)/(math.log(2)*math.log(2))
k = -math.log(p,2)
m = math.ceil(m)
k = math.ceil(k)
for line in sys.stdin:
    if line.strip() != '':
        check = True
        line  = line.strip()
        for i in range(k):
            index = hashRes(str(i)+'_'+line,m)
            print(index)
