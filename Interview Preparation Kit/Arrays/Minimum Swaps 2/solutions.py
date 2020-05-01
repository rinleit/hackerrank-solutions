#!/bin/python3

import math
import os
import random
import re
import sys

def minimumSwaps(arr):
    n = len(arr)
    arr_pos = [0] * (n + 1)
    for pos, val in enumerate(arr):
        arr_pos[val] = pos
    swaps = 0
    arr_sort = sorted(arr)
    for i in range(n):
        if arr[i] != arr_sort[i]:
            swaps += 1
            # get idx need swap
            idx_swap = arr_pos[arr_sort[i]]
            # swap value
            arr[i], arr[idx_swap] = arr_sort[i], arr[i]
            # modified idx swap
            arr_pos[arr[idx_swap]] = idx_swap
    return swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
