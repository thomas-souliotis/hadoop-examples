#!/usr/bin/python3
import sys
import re

key, key2, total, keys, vals = None, None, 0, [], []
for line in sys.stdin:
  if line.strip()!='':
    if line[0] == 'm':
      #name , studentId, course, mark = line.strip().split(' ')
      res = re.split(' ',line.strip())
      print(res[3],' (' + res[9] + ',' + res[6] + ') ', sep='\t') #every column is seperated with 2 spaces
    else:
      res = re.split(' ',line.strip())
      # 0 means no value
      print(res[3],'0', sep='\t')
