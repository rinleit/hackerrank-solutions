#!/bin/python

import math
import os
import random
import re
import sys

# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    return sum([arr.count(i + d) and arr.count(i + 2*d) for i in arr])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = raw_input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = map(int, raw_input().rstrip().split())

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
