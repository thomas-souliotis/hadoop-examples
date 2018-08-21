#!/usr/bin/python3
import sys
import math
from bitarray import bitarray



n           = 1897987#int(sys.argv[1])
p           = 0.01
m           = -n*math.log(p)/(math.log(2)*math.log(2))
m           = math.ceil(m)
bloomFilter = bitarray()
bloomFilter = m *bitarray('0')
flag        = False

for line in sys.stdin:
    if line.strip() != '':
        val              = line.strip()
        val              = int(val)
        bloomFilter[val] = '1'

if (m>0) and (True in bloomFilter):
    print(bloomFilter)
