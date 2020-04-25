#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the connectedCell function below
def connectedCell(matrix):
    mx = 0
    filled = [(x, y) for x, row in enumerate(matrix) for y, v in enumerate(row) if v == 1]
    while filled:
        region = [filled.pop()]
        count = 0
        while region:
            p_x, p_y = region.pop()
            count += 1
            for f_x, f_y in list(filled):
                if abs(p_x - f_x) <= 1 and abs(p_y - f_y) <= 1:
                    region.append((f_x, f_y))
                    filled.remove((f_x, f_y))
        else:
            mx = max(mx, count)
    return mx

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()
