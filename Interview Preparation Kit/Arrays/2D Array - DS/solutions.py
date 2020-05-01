#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.

def getValHourGlass(arr, ipx, ipy):
    val = 0
    patterns = [(0, 0),(0, 1),(0, 2),
                       (1, 1),
                (2, 0),(2, 1),(2, 2)]
    for i, j in patterns:
        val += arr[ipx+i][ipy+j]
    return val

def hourglassSum(arr):
    max_sum = (-10**7)
    r, c = len(arr), len(arr[0])
    for i in range(r - 2):
        for j in range(c - 2):
            val = getValHourGlass(arr, i, j)
            max_sum = max(max_sum, val)
    return max_sum
   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
