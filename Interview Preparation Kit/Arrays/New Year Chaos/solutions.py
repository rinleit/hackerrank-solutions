#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the minimumBribes function below.
def minimumBribes(arr):
    bribes = defaultdict(lambda: 0)
    cont, n, r = True, len(arr), 0
    while cont:
        cont = False
        for i in range(0, n - 1):
            if arr[i] > arr[i+1]:
                bribes[arr[i]] += 1
                if bribes[arr[i]] > 2:
                    return "Too chaotic"
                arr[i], arr[i+1] = arr[i+1], arr[i]
                r += 1
                cont = True
    return r

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())
        q = list(map(int, input().rstrip().split()))
        res = minimumBribes(q)
        print(res, end='\n')
