#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    e, jump_to = 0, 0
    while e < 100 and jump_to >= 0:
        jump_to = (jump_to + k) % n
        e = e + (3 if c[jump_to] == 1 else 1)
        if jump_to == 0:
            break
    return 100 - e

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
