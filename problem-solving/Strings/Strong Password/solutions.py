#!/bin/python3

import math
import os
import random
import re
import sys
import re

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    cases = [r'[a-z]', r'[A-Z]', r'[\d]', r'\W+']
    count = 0
    for case in cases:
        if not re.search(case, password):
            count += 1
    return max(count, 6 - n)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
