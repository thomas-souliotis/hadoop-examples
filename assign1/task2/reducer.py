#!/usr/bin/python3
import sys
key2, key, total,keyprevious = None, None, 0 , None
for line in sys.stdin:
    key2, count = line.strip().split('\t')
    count = int(count)
    if key2!=key:
        if total==1:
            print (key)
        key, total, keyPrevious = key2, count, key
    else:
        total += count
if key2!=keyPrevious:
    print(key2)
