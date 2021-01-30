#!/bin/python3

'''There is a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. 
The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1 or 2
The player must avoid the thunderheads. Determine the minimum number of jumps it will take to jump from the starting postion to the last cloud.
It is always possible to win the game.

For each game, you will get an array of clouds numbered  if they are safe or  if they must be avoided.

Example [0,1,0,0,0,1,0]

Index the array from 0-6 The number on each cloud is its index in the list so the player must avoid the clouds at indices  and 5
They could follow these two paths: 0>2>4>6 or 0>2>3>4>6 The first path takes  jumps while the second takes 4 Return 3'''




import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    if len(c)==1: return 0
    if len(c)==2: return 0 if c[1]==1 else 1
    if c[2]==1:
        return 1 + jumpingOnClouds(c[1:])
    if c[2]==0:
        return 1 + jumpingOnClouds(c[2:])    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
