#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_sAY s
#

def nonDivisibleSubset(k, s):
    # say for storing frequency  
    # of modulo values 
    N = len(s)
    f = [0 for i in range(k)]
  
    # Fill frequency say with 
    # values modulo k 
    for i in range(N): 
        f[s[i] % k] += 1
  
    # if k is even, then update f[k/2] 
    if (k % 2 == 0): 
        f[k/2] = min(f[k / 2], 1)
  
    # Initialize result by minimum of 1 or 
    # count of numbers giving remainder 0 
    res = min(f[0], 1) 
  
    # Choose maximum of count of numbers 
    # giving remainder i or k-i 
    for i in range(1,(k // 2) + 1): 
        res += max(f[i], f[k - i]) 
  
    return res 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = raw_input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = map(int, raw_input().rstrip().split())

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
