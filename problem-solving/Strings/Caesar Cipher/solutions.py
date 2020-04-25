#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
alphabets = 'abcdefghijklmnopqrstuvwxyz'

def rotated(k):
    k = k % len(alphabets)
    return alphabets[k:] + alphabets[:k]

def caesarCipher(s, k):
    alphabets_rotated = rotated(k)
    res = ''
    for c in s:
        if c.lower() in alphabets:
            char = alphabets_rotated[alphabets.index(c.lower())]
            if ord(c.lower()) - ord(c) != 0: char = char.upper()
            res += char
        else:
            res += c
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
