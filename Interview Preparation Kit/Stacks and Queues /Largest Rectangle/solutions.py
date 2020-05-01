#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def largestRectangle(h):
    largest, i = 0, 0
    left = [1] * len(h)
    right = [1] * len(h)
    while i < len(h):
        j = i + 1
        while j < len(h) and h[j] >= h[i]:
            left[i] += 1
            j += 1
        j = i - 1
        while j >= 0 and h[j] >= h[i]:
            left[i] += 1
            j -= 1
        largest = max(largest, left[i]*h[i])
        i += 1
    
    i = len(h) - 1
    while i > 0:
        j = i - 1
        while j >= 0 and h[j] >= h[i]:
            right[i] += 1
            j -= 1
        j = i + 1
        while j < len(h) and h[j] >= h[i]:
            right[i] += 1
            j += 1
        largest = max(largest, right[i]*h[i])
        i -= 1
    return largest
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
