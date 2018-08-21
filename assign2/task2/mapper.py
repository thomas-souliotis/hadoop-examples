#!/usr/bin/python3
import sys
import re
import xml.etree.ElementTree as ET


def findindex(val, vals):
  i = 8
  while (i>=0):
    if val < vals[i]:
      return i+1
    i -= 1
  return 0

max         = -1
left, right = None, None
vals        = [-1]*10
ids         = [None]*10
pos         = 0

#every mapper finds its top 10 vals and sends them
#This holds since max_10(whole) = max_10(max_10(part1) || max 10(part2)||...)
for line in sys.stdin:
  if line.strip() != '':
    line = line.strip()
    a    = ET.fromstring(line)
    qId  = a.get('Id')
    rId  = a.get('PostTypeId')
    if rId == '1':
      val = a.get('ViewCount')
      val = int(val)
      if (val > max):
        max = val
      if val > vals[9]:
        pos = findindex(val,vals)
        temp = vals[pos:9]
        vals[pos] = val
        vals[pos+1:10] = temp
        temp = ids[pos:9]
        ids[pos] = qId
        ids[pos+1:10] = temp  

#print the top 10
for i in range(0,10):
  print(vals[i],ids[i],sep='\t')
