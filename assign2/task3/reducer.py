#!/usr/bin/python3
import sys


key, key2, previousKey, sum, question = None, None, None, 0, False
for line in sys.stdin:
  if line.strip() !='':
    key , val = line.strip().split('\t')
    charId    = val[0] 
    if charId == '2':
      personId  = val[1:]
      ans, qId = key.split() 
    if key2 == None:
      key2 = key
    else:
      if key == key2:
        print(personId+ '\t' +qId)
        key2 = None
      else:
        key2 = key
