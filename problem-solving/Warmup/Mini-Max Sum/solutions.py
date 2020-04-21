#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sum_list = []
    n = len(arr)
    for idx in range(n):
        sum_except = sum([e for i, e in enumerate(arr) if i != idx])
        sum_list.append(sum_except)
    return min(sum_list), max(sum_list)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    a, b = miniMaxSum(arr)
    print(a, b)
