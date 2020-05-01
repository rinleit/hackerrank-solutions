#!/bin/python3

import os
import sys
from bisect import insort

# Complete the luckBalance function below.
def luckBalance(k, contests):
    sum_luck = 0
    imp_contests = []

    for L, T in contests:
        if T: insort(imp_contests, L)
        sum_luck += L

    n = len(imp_contests)
    min_loss = sum(imp_contests[:n-k])
    return sum_luck if n <= k else sum_luck - 2*min_loss

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
