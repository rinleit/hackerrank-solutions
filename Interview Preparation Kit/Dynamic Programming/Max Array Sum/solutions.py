#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    pre_pre = arr[0]
    pre = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        curr_sum = max(pre, pre_pre + arr[i])
        curr_sum = max(curr_sum, arr[i])
        pre_pre = pre
        pre = curr_sum
    return pre


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
