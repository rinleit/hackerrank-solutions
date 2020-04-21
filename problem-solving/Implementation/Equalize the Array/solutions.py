#!/bin/python

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the equalizeArray function below.
def equalizeArray(arr):
    c = Counter(arr)
    m = max(c, key=c.get)
    result = sum([v for k, v in dict(c).items() if k != m])
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
