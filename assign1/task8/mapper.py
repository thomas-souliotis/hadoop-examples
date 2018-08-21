#!/usr/bin/python3
import sys
import re

key, key2, total, keys, courseMarks, minMark, minIdS = None, None, 0, [], [], 1000000, ''
for line in sys.stdin:
  studentId, courseMark = line.strip().split(' -->')
  courseMarks = re.split(' ',courseMark)
  if len(courseMarks) > 4:
    courseMarks = courseMarks[1:]
    total = 0
    for i in courseMarks:
      ans = re.split('\(|\)|\,',i)
      val = float(ans[1])
      total += val
    total = total / len(courseMarks)
    if total == minMark:
      minIdS =minIds + ', ' + studentId
    if total < minMark:
      minIds = studentId
      minMark = total
print (minIds, minMark,sep='\t')
