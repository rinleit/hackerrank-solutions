#!/bin/python3

import math
import os
import random
import re
import sys
from copy import deepcopy
# Complete the abbreviation function below.
def abbreviation(a, b):
    n = len(a)
    m = len(b)
    dp = [[0]*(m+1) for _ in range(n+1)]
    dp[0][0] = 1
    i = 1
    while i < n+1:    
        if a[i-1].isupper():
            break
        dp[i][0] = 1
        i += 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1]
            elif a[i-1].upper() == b[j-1]:
                dp[i][j] = (dp[i-1][j-1] or dp[i-1][j])
            elif a[i-1].islower():
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = 0
                
    return  "YES" if dp[-1][-1] else "NO"
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
