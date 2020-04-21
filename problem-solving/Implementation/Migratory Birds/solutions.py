#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    n = len(arr)
    counts = [0] * (max(arr) + 1)
    for i in range(n):
        counts[arr[i]] += 1
    return counts.index(max(counts)) # If the same element is present more than once, the method returns the index of the first occurrence of the element

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
