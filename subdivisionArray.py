#def birthday(s, d, m):
#    c=0
#    for i in range(len(s)-m+1):
#        if sum(s[i:i+m]) == d:
#            c+=1
    
#    return c   
#can use this and it runs fine but complexity is O(n*m) so we'll use sliding window


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    i=j=0
    summ=0
    c=0
    while j<m:
        summ+=s[j]
        j+=1
    if summ==d:
       c+=1
    
    while j<len(s):
        summ-=s[i]
        summ+=s[j]
        if summ==d:
            c+=1
        i+=1
        j+=1
        
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
