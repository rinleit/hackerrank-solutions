#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    # Returns total number of anagram 
    # substrings in s 
    n = len(s) 
    mp = dict() 
    # loop for length of substring 
    for i in range(n): 
        sb = '' 
        for j in range(i, n): 
            sb = ''.join(sorted(sb + s[j])) 
            # increase count corresponding 
            # to this dict array 
            mp[sb] = mp.get(sb, 0) + 1
    anas = 0
      
    # loop over all different dictionary  
    # items and aggregate substring count 
    for k, v in mp.items(): 
        anas += (v*(v-1))//2
    return anas 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
