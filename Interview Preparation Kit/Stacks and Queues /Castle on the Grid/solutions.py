#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumMoves function below.
def minimumMoves(grid, startX, startY, goalX, goalY):
    n, m = len(grid), len(grid[0])
    goal = (goalX, goalY)
    start = (startX, startY)
    maps = set()
    for i in range(n):
        for j in range(m):
            if grid[i][j] != 'X': maps.add((i, j))
    steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    moves = lambda point, step: (point[0] + step[0], point[1] + step[1])
    stack = [(start, 0)]
    visited = set([start])
    while stack:
        curr_p, val = stack.pop(0)
        for step in steps:
            next_p = curr_p
            while True:
                next_p = moves(next_p, step)
                if next_p in maps:
                    if next_p == goal:
                        return val +1
                    elif next_p not in visited:
                        visited.add(next_p)
                        stack += [(next_p, val+1)]
                else: break
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    startXStartY = input().split()

    startX = int(startXStartY[0])

    startY = int(startXStartY[1])

    goalX = int(startXStartY[2])

    goalY = int(startXStartY[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()
