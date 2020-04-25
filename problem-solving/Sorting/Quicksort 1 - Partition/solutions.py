#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the quickSort function below.
def quickSort(arr):
    left = []
    equal = []
    right = []
    if len(arr) > 1:
        p = arr[0]
        for i in arr:
            if i == p:
                equal += [i]
            elif i < p:
                left += [i]
            elif i > p:
                right += [i]
        return left + equal + right
    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
