#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

# Complete the weightedUniformStrings function below.
def ords(c):
    return ord(c) - ord('a') + 1

def weightedUniformStrings(s, queries):
    res = reduce(lambda x, y: x + ' %s' % (y) if x[-1] != y else x + y , s)
    splits = res.split(' ')
    weights = set()
    for c in splits:
        for i in range(1, len(c) + 1):
            weights.add(int(ords(c[0])*i))
    return map(lambda q: 'Yes' if q in weights else 'No', queries)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
