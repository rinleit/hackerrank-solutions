#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotRight(a, d):
    n = len(a)
    res = [0] * n
    for i in range(n):
        new_idx = (i + d % n) % n
        res[new_idx] = a[i]
    return res

def rotLeft(a, d):
    n = len(a)
    res = [0] * n
    for i in range(n):
        new_idx = (n + i - d % n) % n
        res[new_idx] = a[i]
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
