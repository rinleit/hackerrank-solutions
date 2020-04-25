#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
from functools import reduce


def mergeIntervals(arr): 
    # Sorting based on the increasing order  
    # of the start intervals 
    arr.sort(key = lambda x: x[0])
    # array to hold the merged intervals 
    m = [] 
    s = -10000
    max = -100000
    for i in range(len(arr)): 
        a = arr[i] 
        if a[0] > max: 
            if i != 0: 
                m.append([s,max]) 
            max = a[1] 
            s = a[0] 
        else: 
            if a[1] >= max: 
                max = a[1] 
    # 'max' value gives the last point of  
    # that particular interval 
    # 's' gives the starting point of that interval 
    # 'm' array contains the list of all merged intervals 
    if max != -100000 and [s, max] not in m: 
        m.append([s, max])
    return m 

# Complete the gridlandMetro function below.
def gridlandMetro(n, m, k, track):
    track = set(track)
    rows = defaultdict(list)
    for r, c1, c2 in track:
        rows[r].append([c1, c2])
    metros = m*n
    places = 0
    for _, cols in rows.items():
        cols = mergeIntervals(cols)
        for i, j in cols:
            places += j - i + 1
    return metros - places

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nmk = input().split()

    n = int(nmk[0])

    m = int(nmk[1])

    k = int(nmk[2])

    track = []

    for _ in range(k):
        track.append(tuple(map(int, input().rstrip().split())))

    result = gridlandMetro(n, m, k, track)

    fptr.write(str(result) + '\n')

    fptr.close()
