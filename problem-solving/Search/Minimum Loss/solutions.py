#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the minimumLoss function below.
def minimumLoss(price):
    n = len(price)
    hash_map = defaultdict(int)
    for i in range(n):
        hash_map[price[i]] = i
    nums = sorted(hash_map, reverse=True)
    min_cost = nums[0] - nums[-1]
    for i in range(n - 1):
        if (hash_map[nums[i]] < hash_map[nums[i+1]]):
            min_cost = min(nums[i]-nums[i+1], min_cost)
    return min_cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
