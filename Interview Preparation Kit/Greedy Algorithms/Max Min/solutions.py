#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxMin function below.
def maxMin(k, arr):
    arr.sort()
    unfairness = 10**9
    for i in range(len(arr) - k + 1):
        min_unfair = arr[i]
        max_unfair = arr[i+k-1]
        unfairness = min(max_unfair - min_unfair, unfairness)
    return unfairness

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
