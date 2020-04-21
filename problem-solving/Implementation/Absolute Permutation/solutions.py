#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the absolutePermutation function below.
def absolutePermutation(n, k):
    if k == 0:
        return list(range(1, n+1))
    elif (n/k % 2) != 0:
        return [-1]
    else:
        res = list()
        for i in range(1, n + 1):
            if 1 <= i + k <= n:
                res.append(i+k)
            if i % k == 0:
                k = (-1) * k
        return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
