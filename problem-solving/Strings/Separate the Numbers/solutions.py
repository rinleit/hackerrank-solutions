#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the separateNumbers function below.
def separateNumbers(s):
    n = len(s)
    step = n//2
    i = 1
    while i <= step:
        res = ''
        start_number = int(s[:i])
        while len(res) < n:
            res += str(start_number)
            start_number += 1
        if res == s:
            print('YES', int(s[:i]))
            return
        i += 1
    print('NO')

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
