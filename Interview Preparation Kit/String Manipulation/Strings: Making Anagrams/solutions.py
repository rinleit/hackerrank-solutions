#!/bin/python3

import math
import os
import random
import re
from collections import Counter
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    counter_a = Counter(a)
    counter_b = Counter(b)
    set_in_a_nin_b = counter_a - counter_b
    set_in_b_nin_a = counter_b - counter_a
    set_merge = dict(**set_in_a_nin_b, **set_in_b_nin_a)
    return sum(set_merge.values())
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
