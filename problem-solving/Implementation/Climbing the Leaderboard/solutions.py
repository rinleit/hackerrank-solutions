#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    ranking = [scores[0]]
    for itm in scores:
        if itm != ranking[-1]:
            ranking.append(itm)
    inx = len(ranking) - 1
    for itm in alice:
        while itm > ranking[inx] and inx >= 0:
            inx -= 1
        if itm == ranking[inx]:
            yield inx + 1
        else:
            yield inx + 2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
