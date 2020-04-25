#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

def meet_pattern(s):
    return all(s[i-1] != s[i] for i in range(1, len(s)))

def alternate(s):
    letters = set(s)
    max_len = 0
    for pair in combinations(letters, 2):
        substr = "".join(i for i in s if i in pair)
        if meet_pattern(substr):
            max_len = max(max_len, len(substr))
    return max_len


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
