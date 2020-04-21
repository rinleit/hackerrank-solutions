#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    liked, shared, i = 0, 5, 0
    while i < n:
        liked += math.floor(shared/2)
        shared = math.floor(shared/2) * 3
        i += 1
    return liked


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
