#!/bin/python3

import os
import sys
from functools import lru_cache

# Complete the stepPerms function below.
# A(n) = A(n - 1) + A(n - 2) + A(n - 3)
# A(1)=1; A(2)=2; A(3)=4.

MODULE = 10000000007
@lru_cache(maxsize=256)
def stepPerms(n):
    if (n == 1):
        return 1
    elif (n == 2):
        return 2
    elif (n == 3):
        return 4
    else:
        return (stepPerms(n-1) % MODULE + \
                stepPerms(n-2) % MODULE + \
                stepPerms(n-3) % MODULE) % MODULE

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()
