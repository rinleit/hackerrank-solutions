#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the strangeCounter function below.
def strangeCounter(t):
    cycles = math.ceil(math.log2(t/3 + 1) - 1)
    value_at_cycles = (1 << cycles) * 3
    time_at_cycles = ((1 << cycles) - 1) * 3 + 1
    return value_at_cycles - abs(t - time_at_cycles)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
