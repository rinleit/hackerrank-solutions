#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

# Complete the gemstones function below.
def gemstones(arr):
    minerals = map(lambda a: set(a), arr)
    return len(reduce(lambda x, y: x & y, minerals))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
