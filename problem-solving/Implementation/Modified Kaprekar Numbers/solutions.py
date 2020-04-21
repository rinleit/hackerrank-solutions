#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    results = []
    for i in range(p, q+1):
        b = pow(i, 2) % pow(10, len(str(i)))
        a = (pow(i, 2) - b) / pow(10, len(str(i)))
        if i == a + b:
            results += [i]
    return results

if __name__ == '__main__':
    p = int(input())

    q = int(input())

    results = kaprekarNumbers(p, q)
    if not results:
        print("INVALID RANGE")
    else:
        print(" ".join(map(str, results)))
