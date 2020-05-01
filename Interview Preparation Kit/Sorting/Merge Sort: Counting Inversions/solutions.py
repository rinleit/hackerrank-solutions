#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countInversions function below.
def merge(arr, left, right):
    l, r, k, cnt = 0, 0, 0, 0
    len_l = len(left)
    len_r = len(right)
    while l < len_l and r < len_r:
        if left[l] <= right[r]:
            arr[k] = left[l]
            l += 1
        else:
            arr[k] = right[r]
            r += 1
            cnt += len_l - l
        k += 1
    while l < len_l:
        arr[k] = left[l]
        l += 1
        k += 1
    while r < len_r:
        arr[k] = right[r]
        r += 1
        k += 1
    return cnt

def merge_sort(arr):
    count_inversion = 0
    mid = len(arr)//2
    if mid > 0:
        left = arr[:mid]
        right = arr[mid:]
        count_inversion += merge_sort(left)
        count_inversion += merge_sort(right)
        count_inversion += merge(arr, left, right)
    return count_inversion


def countInversions(arr):
    return merge_sort(arr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
