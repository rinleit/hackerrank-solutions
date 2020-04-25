#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
alphabets = 'abcdefghijklmnopqrstuvwxyz'
def pangrams(s):
    s = filter(lambda c: c != ' ', map(lambda c: str(c).lower(), s))
    if set(s) == set(alphabets):
        return 'pangram'
    return 'not pangram'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
