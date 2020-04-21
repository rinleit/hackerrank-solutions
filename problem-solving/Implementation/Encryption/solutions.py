#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    n = math.sqrt(len(s))
    row, col = math.floor(n), math.ceil(n) 
    encryption = []
    for i in range(0, len(s), col):
        temp_str = s[i:i+col].ljust(col, " ")
        encryption += [temp_str]
    results = map(lambda s: ''.join(s).strip(), list(zip(*encryption)))
    return " ".join(results)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
