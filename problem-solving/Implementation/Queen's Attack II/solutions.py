#!/bin/python3

import math
import os
import random
import re
import sys

def get_moves(start_position, direction):
    global board_shape, obstacles_spot
    height, width = board_shape
    r, c = start_position
    counts = 0
    while True:
        r -= direction.count('n')
        r += direction.count('s')
        c += direction.count('e')
        c -= direction.count('w')
        if 1 <= r <= height and 1 <= c <= width and (r, c) not in obstacles_spot:
            counts += 1
        else:
            break
    return counts

def queen_moves(spot):
    directions = ['n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw']
    count_moves = 0
    for direction in directions:
        count_moves += get_moves(spot, direction)
    return count_moves

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    global board_shape, obstacles_spot
    board_shape = (n, n)
    obstacles_spot = set(obstacles)
    return queen_moves((r_q, c_q))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(tuple(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
