#!/bin/python

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def CounterCommonStrLongest(s, t):
    n = min(len(s), len(t))
    count = 0
    for i in range(n):
        if s[i] == t[i]:
            count += 1
        else:
            break
    return count

def appendAndDelete(s, t, k):
    if k >= len(t)*2:
        return 'Yes'
    else:
        n = CounterCommonStrLongest(s, t)
        min_del = len(s) - n
        min_append = len(t) - n
        min_actions = min_del + min_append
        leave_actions = k - min_actions
        if leave_actions % 2 != 0 or leave_actions < 0:
            return 'No'
        else:
            return 'Yes'
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    t = raw_input()

    k = int(raw_input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
