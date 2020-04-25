
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def binarySearch(arr, value):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = l + (r - l)//2
        if arr[mid] == value:
            return True
        elif value > arr[mid]:
            l = mid + 1
        elif value < arr[mid]:
            r = mid - 1
    return False

def pairs(k, arr):
    count = 0
    arr_sort = sorted(arr)
    for i in arr:
        if binarySearch(arr_sort, i - k):
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
