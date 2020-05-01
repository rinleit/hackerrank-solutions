#!/bin/python3
import os
import sys
from collections import Counter

def reverseShuffleMerge(s):
    s = s[::-1]
    cnt = Counter(s)
    need = {k: cnt[k]//2 for k in cnt.keys()}
    left = {k: cnt[k] for k in cnt.keys()}
    res = []
    for c in s:
        left[c] -= 1
        if not need[c]:
            continue
        need[c] -= 1
        while res and res[-1] > c and left[res[-1]] > need[res[-1]]:
            need[res[-1]] += 1
            res.pop()
        res.append(c)

    return ''.join(res)
    



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = reverseShuffleMerge(s)

    fptr.write(result + '\n')

    fptr.close()
