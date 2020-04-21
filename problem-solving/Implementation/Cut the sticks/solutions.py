
#!/bin/python

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    l = len(arr)
    c = Counter(arr)
    ks = sorted(c)
    for k in ks:
        yield l
        l -= c[k]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
