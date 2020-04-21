#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    total_cost = sum(bill) - bill[k]
    b_actual = total_cost / 2
    b_overcharged = int(b - b_actual)
    return b_overcharged if b_overcharged > 0 else 'Bon Appetit'

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    print(bonAppetit(bill, k, b))
