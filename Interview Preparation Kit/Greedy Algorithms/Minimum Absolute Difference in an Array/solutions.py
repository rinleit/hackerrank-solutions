#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    if len(set(arr)) != len(arr):
        return 0
    arr.sort()
    min_diff = None
    for i in range(1, len(arr)):
        if min_diff is None:
            min_diff = abs(arr[i] - arr[i-1])
        if abs(arr[i] - arr[i-1]) < min_diff:
            min_diff = abs(arr[i] - arr[i-1])
    return min_diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
