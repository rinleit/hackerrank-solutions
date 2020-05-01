#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    res = []
    arr = defaultdict(lambda: 0)
    for _ in range(q):
        tp, n = input().rstrip().split()
        if tp == '1':
            arr[n] += 1
        elif tp == '2':
            if n in arr:
                arr[n] = max(arr[n] - 1, 0)
        elif tp == '3':
            res += ['1'] if int(n) in set(arr.values()) else ['0']
    fptr.write('\n'.join(res))
    fptr.write('\n')
    fptr.close()
