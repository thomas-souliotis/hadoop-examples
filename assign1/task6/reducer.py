#!/usr/bin/python3
import sys
import math

key, key2, total, keys, vals, result = None, None, 0, [], [] , 0
for line in sys.stdin:
  if line.strip()!='':
    key , val  = line.strip().split('\t')
    val = float(val)
    if key != key2:
        if key2:
            result = 0.0
            for i in range(0,len(vals)):
              result += -(vals[i] / total) * math.log2((vals[i] / total)) 
            print (key2, round(result,10), sep=' ')
        key2 = key
        total = val
        vals = [val]
    else: 
        vals.extend([val])
        total = total + val

if key2:
    result = 0.0
    for i in range(0,len(vals)):
        result += -(vals[i] / total) * math.log2((vals[i] / total))
    print (key2, round(result,10), sep=' ')

