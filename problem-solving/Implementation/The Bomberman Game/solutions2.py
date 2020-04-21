#!/bin/python3

import math
import os
import random
import re
import sys

BOOMM = 3
EMPTY = 0
DETON = 1

def downtime(grid):
    global r, c
    for i in range(r):
        for j in range(c):
            if grid[i][j] != EMPTY:
                grid[i][j] -= 1

def placeBom(grid):
    global r, c
    for i in range(r):
        for j in range(c):
            if grid[i][j] == EMPTY:
                grid[i][j] = BOOMM

def detonating(grid):
    global r, c
    for i in range(r):
        for j in range(c):
            if grid[i][j] == DETON:
                if i - 1 >= 0 and grid[i - 1][j] != DETON:
                    grid[i - 1][j] = EMPTY
                if i + 1 < r and grid[i + 1][j] != DETON:
                    grid[i + 1][j] = EMPTY
                if j - 1 >= 0 and grid[i][j - 1] != DETON:
                    grid[i][j - 1] = EMPTY
                if j + 1 < c and grid[i][j + 1] != DETON:
                    grid[i][j + 1] = EMPTY

def bomberMan(n, grid):
    global r, c
    r = len(grid)
    c = len(grid[0])
    if n % 2 == 0:
        return ['O'*c for _ in range(r)]
    else:
        i = 1
        while i <= n:
            detonating(grid)
            downtime(grid)
            if i % 2 == 0:
                placeBom(grid)
            i += 1
    return print_grid(grid)

def print_grid(grid):
    res = []
    for row in grid:
        res += [''.join(map(lambda x: '.' if x == 0 else 'O', row))]
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    rcn = input().split()

    r = int(rcn[0])

    c = int(rcn[1])

    n = int(rcn[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid_item =  list(map(lambda x: 0 if x == '.' else 3, grid_item))
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
