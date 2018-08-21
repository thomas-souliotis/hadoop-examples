#!/usr/bin/python3
import sys
import xml.etree.ElementTree as ET

for line in sys.stdin:
  if line.strip() != '':
    line     = line.strip()
    a        = ET.fromstring(line)
    ansORqId = a.get('Id')
    rId      = a.get('PostTypeId')
    if rId == '1':
      answer = a.get('AcceptedAnswerId')
      if (answer != None) and (ansORqId != None):
        print(answer + ' ' + ansORqId + '\t1')
    elif rId =='2':
      question = a.get('ParentId')
      name     = a.get('OwnerUserId')
      if (question != None) and (ansORqId != None) and (name != None):
        print(ansORqId + ' ' + question + '\t2' + name)


