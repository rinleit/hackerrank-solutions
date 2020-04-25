#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the icecreamParlor function below.
def icecreamParlor(m, arr):
    data = {}
    for idx, v in enumerate(arr):
        if v not in data:
            data[v] = [idx + 1]
        else:
            data[v].append(idx + 1)
    for v in arr:
        if m - v in data and v != (m - v):
            return sorted([data[v][0], data[m - v][0]])
        elif m - v in data and v == (m - v):
            if len(data[v]) > 1:
                return sorted([data[v][0], data[v][1]])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
