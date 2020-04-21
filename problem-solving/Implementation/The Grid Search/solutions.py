#!/bin/python3

import math
import os
import random
import re
import sys


def check_grid(P, G, i, j, r_p, c_p):
    next_row = 0
    for i in range(i,  i + r_p):
        if P[next_row] != G[i][j:j + c_p]:
            return False
        next_row += 1
    return True

def gridSearch(G, P):
    r_g = len(G)
    c_g = len(G[0])
    r_p = len(P)
    c_p = len(P[0])
    for i in range(r_g - r_p + 1):
        for j in range(c_g - c_p + 1):
            if check_grid(P, G, i, j, r_p, c_p):
                return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
