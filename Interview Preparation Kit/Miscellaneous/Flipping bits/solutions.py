#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flippingBits function below.
def flippingBits(n):
    n_bin = bin(n)[2:].rjust(32, '0')
    invert_n_bin = ''.join(['1' if c == '0' else '0' for c in n_bin])
    return int(invert_n_bin, 2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
