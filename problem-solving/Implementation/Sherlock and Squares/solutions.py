#!/bin/python

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    return int(math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        ab = raw_input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
