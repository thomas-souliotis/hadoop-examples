#!/usr/bin/python3
import sys
import math

key, key2, total, keys, vals = None, None, 0, [], []
for line in sys.stdin:
  if line.strip()!='':
    sentence , val = line.strip().split('\t')
    sentenceArray  = sentence.split(' ')
    sentence = sentenceArray[3]
    key =  sentenceArray[0] + ' ' + sentenceArray[1] + ' ' +sentenceArray[2]
    print(key, val,sep='\t')
