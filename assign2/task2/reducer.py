#!/usr/bin/python3
import sys

count = 0
for line in sys.stdin:
  if line.strip() !='':
    if count < 10:
      line = line.strip()
      left,right = line.split('\t')
      if right != 'None':
        print(left,right,sep=' ')
        count = count +1

