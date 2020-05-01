#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    c.sort()
    min_cost = 0
    purchase = 0
    n = len(c)
    if k >= n:
        min_cost = sum(c)
    else:
        for cost in c[::-1]:
            pre_purchase = purchase // k
            min_cost += (pre_purchase + 1) * cost
            purchase += 1
    return min_cost


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
