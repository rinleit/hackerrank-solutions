#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import product

# Complete the countLuck function below.
def countLuck(matrix, k):
    g = {} # g : non-tree grid, 
    f = set() # f : feasible spots (end reachable)
    start = None # start : M spots on map
    for p in product( range(len(matrix)), range(len(matrix[0])) ):
        if matrix[p[0]][p[1]] == 'X': continue
        g[p] = None
        if matrix[p[0]][p[1]]=='*':
            end,g[p],f = p,0,set([p])
        elif matrix[p[0]][p[1]]=='M': 
            start = p
    
    change = True ; delta = [ (-1,0), (1,0), (0,-1), (0,1) ]
    nbhd = lambda p : f & set((p[0]+i,p[1]+j) for (i,j) in delta)
    while change: # greedy algorithm to find minimum steps to exit
        change = False # this 'change' allows for isolated patches
        for p in set(g) - f: # code is modifiable for 3 dimensions
            if not nbhd(p) : continue
            change, g[p] = True, 1 + min(g[q] for q in nbhd(p))
            f.add(p)            

    pp, p, waves = None, start, 0 # pp is the previous point p
    while p != end: # only waves wand if new directions appear
        if len(nbhd(p) - set([pp])) > 1: 
            waves += 1
        for q in nbhd(p):
            if g[q] < g[p]: 
                pp, p = p, q
                break        
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
