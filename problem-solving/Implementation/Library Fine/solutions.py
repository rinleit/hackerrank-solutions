#!/bin/python

import math
import os
import random
import re
import sys

# Complete the libraryFine function below.
def libraryFine(d1, m1, y1, d2, m2, y2):
    years = y1 - y2
    months = m1 - m2
    days = d1 - d2
    if years > 0:
        return 10000
    if years < 0 or \
        (years == 0 and months < 0) or \
            (years == 0 and months == 0 and days < 0):
        return 0
    if months == 0:
        return int(15*days)
    else:
        return int(500*months)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    d1M1Y1 = raw_input().split()

    d1 = int(d1M1Y1[0])

    m1 = int(d1M1Y1[1])

    y1 = int(d1M1Y1[2])

    d2M2Y2 = raw_input().split()

    d2 = int(d2M2Y2[0])

    m2 = int(d2M2Y2[1])

    y2 = int(d2M2Y2[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + '\n')

    fptr.close()
