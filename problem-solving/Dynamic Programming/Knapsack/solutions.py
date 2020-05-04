#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the unboundedKnapsack function below.
def unboundedKnapsack(k, arr):
    d = [0] * (k + 1)
    for i in range(1, k + 1):
        numbers = [d[i-v] + v for v in arr if v <= i]
        if numbers: d[i] = max(numbers)
    return d[-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    results = []
    for _ in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        arr = list(map(int, input().rstrip().split()))

        results.append(unboundedKnapsack(k, arr))

    fptr.write('\n'.join(map(str, results)))

    fptr.close()
