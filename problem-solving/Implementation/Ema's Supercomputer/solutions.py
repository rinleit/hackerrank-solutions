#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoPluses function below.
from itertools import product
def twoPluses(grid):
    n, m = len(grid), len(grid[0]) # g[i][j]=1 if 'G' else 0
    g = [ [ int(v=='G') for v in row ] for row in grid ]
    for i,j in product(range(n),range(m)) :
        if g[i][j] == 0 : continue

        for r in range( 1, min( 1+i, 1+j, n-i, m-j ) ):
            a, b, c, d = i-r, i+r, j-r, j+r
            if 0 in (g[a][j],g[b][j],g[i][c],g[i][d]): break            
            g[i][j] = r+1 # g[i][j] becomes its plus' radius
    
    def overlap(): # internal function for cleaner logic
        u,v, x,y = abs(k-i),abs(l-j), min(d,e),max(d,e)
        if u == 0 : return v <= x+y
        if v == 0 : return u <= x+y
        return (u<=x and v<=y) or (v<=x and u<=y)
                
    p = 0 # the running maximum product of areas of pluses
    for i,j in product(range(n),range(m)):
        if g[i][j] == 0 : continue
        for k,l in product(range(i,n),range(m)): # i <= k
            if g[k][l] == 0 : continue

            d, e = g[i][j]-1, g[k][l]-1
            while overlap() and (d or e):
                if d < e : e -= 1 # diminish bigger one
                else : d -= 1
            p = max( p, (1+4*d) * (1+4*e) )
    return p 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
