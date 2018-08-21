#!/usr/bin/python3
import sys
import re

for line in sys.stdin:
  #all the splitted correspond to the split of each of the unwanted characters
  splitted, splitted5 =[], []
  splitted = re.split(' |\t|\n|\r|\f',line)
  for i in splitted:
    if i!='':
      splitted5.append(i)
  tokens = len(splitted5)
  if tokens > 3:
    for i in range (0, tokens - 3):
      print (splitted5[i]+ ' ' + splitted5[i+1] + ' ' + splitted5[i+2] + ' ' + splitted5[i+3] + '\t1')
