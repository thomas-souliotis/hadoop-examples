#!/usr/bin/python3
import sys

def printFunction(sortedFilenames,key2):
  print(key2 + ' : ',end='')
  print(len(sortedFilenames),end = '')
  print(' : ',end='')
  print('{',end='')
  for i in range(len(sortedFilenames)):
    if i == len(sortedFilenames)-1:
      print (sortedFilenames[i], '}')
    else:
      print (sortedFilenames[i], ', ', end='')

#sum multiple 1's from mapper phase, from each .txt file
#no combination of different txts here, but in reducer
key, key2, previousKey, sum = None, None, None, 0
for line in sys.stdin:
  if line.strip() !='':
    key , val = line.strip().split('\t')
    key = key.split()
    fileName = key[1]
    key = key[0]
    val = int(val)
    if key2 == None:
      sum         = val
      key2        = key
      oldFileName = fileName
    else:
      if key!=key2:
        print(key2 + ' ' + oldFileName + '\t' + str(sum))
        sum         = val
        previousKey = key2
        oldFileName = fileName
        key2        = key
      else:
        if fileName == oldFileName:
          #filename the same
          sum = sum + val
        else:
          #filename different
          print(key2 + ' ' + oldFileName + '\t' + str(sum))
          sum = val
          oldFileName = fileName

if previousKey != key:
  print(key + ' ' + fileName + '\t' + str(sum))
    
