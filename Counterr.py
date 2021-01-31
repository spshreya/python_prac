#!/bin/python3

''' if a list is in another list 
one two three     in     one two three four
but not like
one two two       in    one two three four (can not repeat values)
Counter(list1) - Counter(list2) will give an empty dictionary if it can be completely found in the second list'''



import math
import os
import random
import re
import sys
from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    if (Counter(note)-Counter(magazine))=={}:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
