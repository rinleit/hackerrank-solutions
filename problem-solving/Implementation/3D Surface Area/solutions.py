#!/bin/python3

import math
import os
import random
import re
import sys

def countsurfaceArea(A, dir):
    n = len(A)
    m = len(A[0])
    count = 0
    if dir == 'f':
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                count += sum(A[i][:m])
            else:
                count += sum(filter(lambda x: x > 0, map(lambda x: x[0] - x[1], zip(A[i], A[i+1]))))
    elif dir == 'b':
        for i in range(n):
            if i == 0:
                count += sum(A[i][:m])
            else:
                count += sum(filter(lambda x: x > 0, map(lambda x: x[0] - x[1], zip(A[i], A[i-1]))))
    elif dir == 'l':
        for i in range(m):
            if i == 0:
                tempA = list(zip(*A))
                count += sum(tempA[i][:n])
            else:
                tempA = list(zip(*A))
                count += sum(filter(lambda x: x > 0, map(lambda x: x[0] - x[1], zip(tempA[i], tempA[i-1]))))
    elif dir == 'r':
        for i in range(m - 1, -1, -1):
            if i == m - 1:
                tempA = list(zip(*A))
                count += sum(tempA[i][:n])
            else:
                tempA = list(zip(*A))
                count += sum(filter(lambda x: x > 0, map(lambda x: x[0] - x[1], zip(tempA[i], tempA[i+1]))))
    elif dir in ['u', 'd']:
        return n*m

    return count

# Complete the surfaceArea function below.
def surfaceArea(A):
    directions = ['f', 'b', 'r', 'l', 'u', 'd']
    area = 0
    for dir in directions:
        area += countsurfaceArea(A, dir)
    return area

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
