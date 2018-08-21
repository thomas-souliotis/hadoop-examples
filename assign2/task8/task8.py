#!/usr/bin/python3
import sys

def removekey(d, key):
    r = dict(d)
    del r[key]
    return r

table = {}
count = 0
s     = 0.01
e     = 0.0001
w     = 1/e -1
flag  = False
N     = 0
for line in sys.stdin:
  if line.strip() !='':
    line = line.strip()
    N = N + 1
    if count < w:
      if table.get(line) == None:
        table[line] = 1
      else:
        table[line] = table[line] + 1
      count = count + 1
    else:
      if table.get(line) == None:
        table[line] = 1
      else:
        table[line] = table[line] + 1
      for key, val in table.items():
        val = val -1
        if val == 0:
          table = removekey(table,key)
        else:
          table[key] = val
      count = 0


if N > 0:
  threshold = (s - e)*N 
  for key, val in table.items():
    if val >= threshold:
      print(key)
