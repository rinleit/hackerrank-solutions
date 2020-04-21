#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fairRations function below.
def fairRations(B):
    n, count = len(B), 0
    for i in range(n - 1):
        if B[i] % 2 != 0:
            B[i+1] += 1
            count += 2
    return count if B[-1] % 2 == 0 else 'NO'
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()
