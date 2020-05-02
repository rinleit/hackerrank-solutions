#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxCircle function below.
def maxCircle(queries):
    links  = {} # reference for which set they are in
    length = {} # collection of the lengths
    results = []
    maxl = 2

    def getroot(x):
        while x != links[x]:
            x = links[x]
        return x

    def init(x):
        if x in links:
            return getroot(x)
        length[x] = 1
        links[x] = x
        return x

    for a,b in queries:
        a = init(a)
        b = init(b)
        if a != b:
            if length[b]>length[a]: a,b=b,a
            links[b] = a
            length[a] += length[b]
            maxl = max(maxl,length[a])
        results.append(maxl)
    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = maxCircle(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
