#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    min_num = len(a)
    i = len(a) - 1
    while i > 0 and min_num > 1:
        num = i - a.index(a[i])
        min_num = num if num != 0 and num < min_num else min_num
        i -= 1
    if min_num == len(a):
        return -1
    return min_num

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
