#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    ret = 1
    while n > 0:
        ret *= n
        n -= 1
    return ret

if __name__ == '__main__':
    n = int(input())
    print(extraLongFactorials(n))
