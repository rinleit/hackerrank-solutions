#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    n = len(arr)
    po, ne, ze = 0, 0, 0 
    for i in arr:
        if i > 0:
            po += 1
        elif i < 0:
            ne += 1
        else:
            ze += 1
    print("%.6f" % (po/n))
    print("%.6f" % (ne/n))
    print("%.6f" % (ze/n))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
