#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    hash_cost_idx = defaultdict(list)
    for idx, c in enumerate(cost):
        hash_cost_idx[c].append(idx + 1)
    for c in cost:
        if money - c in hash_cost_idx:
            if c == money - c and len(hash_cost_idx[c]) > 1:
                return sorted([hash_cost_idx[c][0], hash_cost_idx[c][1]])
            elif c != money - c:
                return sorted([hash_cost_idx[c][0], hash_cost_idx[money-c][0]])
            else:
                continue

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        res = whatFlavors(cost, money)
        print(' '.join(map(str,res)))
