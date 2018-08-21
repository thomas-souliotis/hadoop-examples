#!/usr/bin/python3
import sys

vals = [0]*25
sentences = [None]*25

def findindex(val, vals):
  i = 23
  while (i>=0):
    if val < vals[i]:
      return i+1
    i -= 1
  return 0

#same as mapper
pos = 0
for line in sys.stdin:
  if line.strip() !='':
    sentence , val = line.strip().split('\t')
    val = int(val)
    if val > vals[24]:
      pos = findindex(val,vals)
      temp = vals[pos:24]
      vals[pos] = val
      vals[pos+1:25] = temp
      temp = sentences[pos:24]
      sentences[pos] = sentence
      sentences[pos+1:25] = temp

for i in range(0,25):
  print(sentences[i],vals[i],sep='\t')
