#!/usr/bin/python3
import sys
import os

filename, filenameC = '', ''
for line in sys.stdin:
  if line.strip()!='':
    line   = line.strip()
    tokens =line.split()
    filenameC = (os.environ["mapreduce_map_input_file"]).split('/')
    filename = filenameC[-1]
    for token in tokens:
      print(token + ' ' + filename + '\t1' )

