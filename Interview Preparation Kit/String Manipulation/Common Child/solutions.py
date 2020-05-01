#!/bin/python3

import os
import sys


#Complete the commonChild function below.
def commonChild(s1, s2):
    n = len(s1)
    s1 = " " + s1
    s2 = " " + s2
    cells = [[0] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if s1[i] == s2[j]:
                cells[i][j] = cells[i-1][j-1] + 1
            elif cells[i-1][j] > cells[i][j-1]:
                cells[i][j] = cells[i-1][j]
            else:
                cells[i][j] = cells[i][j-1]
    return cells[-1][-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
