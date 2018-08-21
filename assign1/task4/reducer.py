#!/usr/bin/python3
import sys
key2, key, total = None, None, 0 
for line in sys.stdin:
    key2, count = line.strip().split('\t')
    count = int(count)
    if key2!=key:
        if key!=None:
          print (key,total,sep='\t')
        key, total = key2, count
    else:
        total += count
if key:
    print(key,total,sep='\t')
