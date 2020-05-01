#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import product

# Complete the countLuck function below.
def countLuck(matrix, k):
    maps = set() # maps : non-tree grid
    start = None # start : M spots on maps
    finish = None # finish : * spots in maps
    for p in product( range(len(matrix)), range(len(matrix[0])) ):
        if matrix[p[0]][p[1]] == 'X': continue
        maps.add(p)
        if matrix[p[0]][p[1]]=='*': finish = p
        elif matrix[p[0]][p[1]]=='M': start = p
    # next step by step
    steps = [ (-1,0), (1,0), (0,-1), (0,1) ]
    next_steps = lambda p : maps & set((p[0]+i, p[1]+j) for (i,j) in steps)
    # DFS Algorithms
    visited, stack, paths = set(), [start], dict()
    while stack:
        p = stack.pop()
        if p in visited: continue
        if p == finish: break
        visited.add(p)
        for q in next_steps(p):
            if q not in visited:
                stack.append(q)
                paths[q] = p
    # get waves
    curr_step, prev_step, waves  = finish, None, 0
    while (curr_step != None):
        prev_step = curr_step
        curr_step = paths.get(curr_step, None)
        if prev_step != finish and len(next_steps(prev_step) - set([curr_step])) > 1:
            waves += 1
    return "Impressed" if waves == k else "Oops!"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        matrix = []

        for _ in range(n):
            matrix_item = input()
            matrix.append(matrix_item)

        k = int(input())

        result = countLuck(matrix, k)

        fptr.write(result + '\n')

    fptr.close()
