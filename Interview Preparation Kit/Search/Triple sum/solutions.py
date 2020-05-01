#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the triplets function below.

from bisect import bisect

def triplets_bisect(a, b, c):
    a, b, c = sorted(set(a)), set(b), sorted(set(c))
    return sum((bisect(a, x) * bisect(c, x) for x in b))

def triplets(a, b, c):
    a = list(sorted(set(a)))
    b = list(sorted(set(b)))
    c = list(sorted(set(c)))
    bi = 0
    ai = 0
    ci = 0
    ans = 0
    while bi < len(b):
        while ai < len(a) and a[ai] <= b[bi]:
            ai += 1
        while ci < len(c) and c[ci] <= b[bi]:
            ci += 1
        ans += ai * ci
        bi += 1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
