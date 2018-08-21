#!/usr/bin/python3
import sys
import re

studentID, key2,  courseMark, courseMarks = None, None, None, []
for line in sys.stdin:
  if line.strip()!='':
    studentId, courseMark = line.strip().split('\t')
    if studentId != key2:
      if key2:
        print(key2 + ' -->', end = '')
        for i in courseMarks: 
          print(i,end='')
        print('')
      key2 = studentId
      if courseMark == '0':
        courseMarks = ['']
      else:
        courseMarks = [courseMark]
    else:
      if courseMark == '0':
        courseMarks.extend([''])
      else:
        courseMarks.extend([courseMark])

if key2:
   print(key2 + ' -->', end = '')
   for i in courseMarks:              
     print(i,end='')
   print('')

