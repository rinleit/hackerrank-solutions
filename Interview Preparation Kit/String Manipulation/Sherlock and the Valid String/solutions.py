#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter, defaultdict
from functools import reduce

# Complete the isValid function below.
def isValid(s):
    s_counter = Counter(s)
    if len(set(s_counter.values())) == 1:
        return 'YES'
    elif len(set(s_counter.values())) > 2:
        return 'NO'
    else:
        splits = defaultdict(list)
        for k, v in s_counter.items(): splits[v].append(k)
        # Both two list has more than 1 element : return NO
        count = sum([int(len(v) > 1) for v in splits.values()])
        if count > 1: return 'NO'
        # element can remove only one character to become vaild string : return YES
        if 1 in splits and len(splits[1]) == 1: return 'YES'
        vaild = abs(reduce(lambda x, y: x - y, splits.keys())) == 1
        if vaild: return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
