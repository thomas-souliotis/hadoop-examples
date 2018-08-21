#!/usr/bin/python3
import sys
maxBytes, maxTokens = 0, 0
for line in sys.stdin:
    if line.strip() != "":
        bytesL, tokensL = line.strip().split('\t')
        bytesL  = int(bytesL)
        tokensL = int(tokensL)
    else:
        bytesL  = 0
        tokensL = 0
    if bytesL > maxBytes:
        maxBytes  = bytesL
    if tokensL > maxTokens:
        maxTokens = tokensL
print(str(maxTokens) + ' ' +  str(maxBytes) )
