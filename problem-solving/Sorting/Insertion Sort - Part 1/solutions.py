#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    key = arr[-1]
    n = len(arr) - 2
    while n >= 0 and key < arr[n]:
        arr[n + 1] = arr[n]
        print(' '.join(map(str, arr)))
        n -= 1
    arr[n+1] = key
    print(' '.join(map(str, arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
