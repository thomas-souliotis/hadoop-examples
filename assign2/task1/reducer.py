#!/usr/bin/python3
import sys

def printFunction(sortedFilenames,key2):
  print(key2 + ' : ',end='')
  print(len(sortedFilenames),end = '')
  print(' : ',end='')
  print('{',end='')
  for i in range(len(sortedFilenames)):
    if i == len(sortedFilenames)-1:
      a = sortedFilenames[i]
      print("({0}, {1})".format(a[0], a[1]),end='')
      print ('}')
    else:
      a = sortedFilenames[i]
      print("({0}, {1})".format(a[0], a[1]),end='')
      print(', ',end='')

fileNames = {}
key, key2, previousKey, sum =None, None, None, 0
for line in sys.stdin:
  if line.strip() !='':
    key , val = line.strip().split('\t')
    key = key.split()
    fileName = key[1]
    key = key[0]
    val = int(val)
    #key2 is not initialized yet, so initialize
    if key2 == None:
      fileNames[fileName] = val
      key2 = key
    else:
      if key!=key2:
        #key is different now, so we sort and print
        sortedFilenames = sorted(fileNames.items(), key=lambda s: s[0])
        printFunction(sortedFilenames,key2)
        #restore the values
        fileNames = {}
        fileNames[fileName] = val
        previousKey = key2
        key2 = key
      else:
        if fileNames.get(fileName) == None:
          #filename does not exist for this key, store it
          fileNames[fileName] = val
        else:
          #filename already exists for this key update it
          fileNames[fileName] =fileNames[fileName] + val          

if previousKey != key:
#key is different now, so we sort and print
  sortedFilenames = sorted(fileNames.items(), key=lambda s: s[0])
  printFunction(sortedFilenames,key)
