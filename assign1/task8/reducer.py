#!/usr/bin/python3
import sys
import re


total, minMark, minIdS = 0,  1000000, []
for line in sys.stdin:
 if line.strip()!='':
  studentId, courseMark = line.strip().split('\t')
  val = float(courseMark)
  if val < minMark:
    minMark = val
    minIds  = [studentId]
  if val == minMark and (studentId not in minIds):
    minIds.extend([studentId])
print('Min ids are:')
for ids in minIds:
  print (ids)
print ('Min mark is:', minMark,sep='\t')
