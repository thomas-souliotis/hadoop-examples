#!/usr/bin/python3
import sys
import re
maxTokens    = 0
maxBytes     = 0
for line in sys.stdin:
  #all the splitted correspond to the split of each of the unwanted characters
  splitted, splitted5 = [], []
  #splitted = line.split(' ')
  #splitted1  =  [ x.split('\t') for x in splitted ]
  #for i in range (0,len(splitted1)):
   #   splitted2 = splitted2 + splitted1[i]
  #splitted2 =  [ x.split('\n') for x in splitted2 ]
  #for i in range (0,len(splitted2)):
      #splitted3 = splitted3 + splitted2[i]
  #splitted3 =  [ x.split('\r') for x in splitted3 ]
  #for i in range (0,len(splitted3)):
   #   splitted4 = splitted4 + splitted3[i]  
  #splitted4 =  [ x.split('\f') for x in splitted4 ]
  #for i in range (0,len(splitted4)):
      #if splitted4[i]!= ['']:
        #splitted5 = splitted5 + splitted4[i]
  splitted = re.split(' |\t|\n|\r|\f',line)
  for i in splitted:
    if i!='':
      splitted5.append([i])
  #finally the number of the tokens are the length of the last list
  tokens   = len(splitted5)
  if tokens > maxTokens :
    maxTokens = tokens
  #just the control to find the maxLength Line
  if len(line)-1 > maxBytes :
    maxBytes = len(line)-1
print ( str(maxTokens) + '\t' + str(maxBytes) )
