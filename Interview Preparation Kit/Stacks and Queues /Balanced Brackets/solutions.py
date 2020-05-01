#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
open_brackets =  {'{':'}', '(':')', '[':']'}
close_brackets = {'}':'{', ')':'(', ']':'['}
def isBalanced(s):
    opened, closed = [], []
    for k in range(len(s)):
        if s[k] in open_brackets.keys():
            opened.append(s[k])
        elif s[k] in close_brackets.keys():
            closed.append(s[k])
            if not opened or open_brackets.get(opened.pop()) != closed.pop():
                return 'NO'
    return 'YES' if not opened else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
