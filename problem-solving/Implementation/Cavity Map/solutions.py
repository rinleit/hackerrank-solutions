#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(grid):
    n = len(grid)
    m = len(grid[0])
    for i in range(1, n - 1):
        for j in range(1 , m - 1):
            checks = [grid[i-1][j], grid[i+1][j], grid[i][j-1], grid[i][j+1]]
            count = sum(map(lambda k: isinstance(k, int) and grid[i][j] > k, checks))
            if count == 4: grid[i][j] = 'X'
    return [''.join(map(str, row)) for row in grid]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(list(map(int, grid_item)))

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
