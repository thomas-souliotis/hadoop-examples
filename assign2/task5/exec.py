#!/usr/bin/python3
import sys
import random

line_number = 0
reservoir   = []
k           = 100
for line in sys.stdin:
    if line.strip != '':
        line_number += 1
        if len( reservoir ) < k:
            reservoir.append(line.strip())
        else:
            rand = int(random.random() * line_number)
            if rand < k:
                reservoir[rand] = line.strip()
        
if line_number != 0:
    for i in range(len(reservoir)):
      print(reservoir[i])

