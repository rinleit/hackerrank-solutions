#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

# Complete the funnyString function below.
def funnyString(s):
    n = len(s)
    r = s[::-1]
    r_ords = [*map(ord, r)]
    s_ords = [*map(ord, s)]
    r_diff = []
    s_diff = []
    for i in range(1, n):
        r_diff += [abs(r_ords[i]-r_ords[i-1])]
        s_diff += [abs(s_ords[i]-s_ords[i-1])]
    if r_diff == s_diff:
        return 'Funny'
    return 'Not Funny'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
