#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    items = []
    while p > m:
        items += [p]
        p -= d
    else:
        items += [m]
    i, count = 0, 0
    n = len(items) - 1
    while s - items[i] >= 0:
        s -= items[i]
        count += 1
        i += int(i < n)
    else:
        return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
