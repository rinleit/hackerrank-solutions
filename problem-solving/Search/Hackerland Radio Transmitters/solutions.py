#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerlandRadioTransmitters function below.
def hackerlandRadioTransmitters(x, k):
    transmitters, i = 0, 0
    x.sort()
    while i < len(x):
        t = x[i]

        while i < len(x) and x[i] - t <= k: 
            i += 1
            
        transmitters += 1 # build a antenna

        t = x[i-1]
        while i < len(x) and x[i] - t <= k:
            i += 1
    return transmitters


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()
