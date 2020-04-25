#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    arr_sort =  sorted(arr)
    arr_zip = list(zip(arr_sort[1:], arr_sort))
    min_diff = arr_zip[0][0] - arr_zip[0][1]
    res = []
    for i,j in arr_zip:
        if i - j < min_diff:
            res = []
            min_diff = abs(i - j)
        if i - j == min_diff:
            res += [j, i]
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
