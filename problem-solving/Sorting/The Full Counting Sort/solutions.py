#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):
    res = [ [] for _ in range(len(arr)) ]
    k = len(arr)//2
    for idx, (i, c) in enumerate(arr):
        if idx < k:
            c = '-'
        res[int(i)] += [c]
    return map(lambda x: ' '.join(x), res)

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    results = countSort(arr)
    print(' '.join(results).strip())
