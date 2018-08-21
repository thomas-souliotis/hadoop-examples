#!/usr/bin/python3
import sys


def printFunc(a,b):
    print(a + ' -> ', end ='')
    for i in range(len(b)-1): 
        print(b[i] + ', ',end='')
    print(b[-1])
    
qList    = []
maxqList = []
key, key2, previousKey, max, maxPos =None, None, None, -1, None
for line in sys.stdin:
  if line.strip() !='':
    key , val = line.strip().split('\t')
    if key2 == None:
      key2 = key
      qList.append(val)
    else:
      if key!=key2:
        if len(qList) > max:
            maxqList = qList
            max      = len(qList)
            maxPos   = key2
        qList = [val]
        previousKey = key2
        key2 = key
      else:
        qList.append(val)

if len(maxqList) == 0:
    if len(qList) != 0:
        printFunc(key,qList)
else:
    printFunc(maxPos,maxqList)
