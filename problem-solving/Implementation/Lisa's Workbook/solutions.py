#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):
    page_number, count = 0, 0
    for problems in arr:
        for p in range(0, problems, k):
            chapter_with_problems = list(range(p, problems))[:k]
            # print(chapter_with_problems) 
            if page_number in chapter_with_problems:
                count += 1
            page_number += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
