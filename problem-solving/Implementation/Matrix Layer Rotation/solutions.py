#!/bin/python3

import math
import os
import random
import re
import sys

def rotate(arr,up,down,left,right): # ROTATING THE CIRCLE BY ONE
    left_up = arr[up][left]
    for i in range(left,right):
        arr[up][i] = arr[up][i+1]
    for j in range(up,down):
        arr[j][right] = arr[j+1][right]
    for i in range(right,left,-1):
        arr[down][i] = arr[down][i-1]
    for i in range(down,up,-1):
        arr[i][left] = arr[i-1][left]
    arr[up+1][left] = left_up

def matrixRotation(matrix, r):
    R = len(matrix)
    C = len(matrix[0])
    # THERE IS NO NEED TO ROTATE THE WHOLE CIRCLE r TIMES
    # JUST ROTATE BY r % total_elements_in_circle
    num_layer = min([R, C]) // 2
    for i in range(num_layer):
        d = (R + C - 2*i)*2 - 4*(i+1)
        for _ in range( r % d ):
            rotate(matrix, i, R-i-1, i, C-i-1)

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
    print_matrix(matrix)
