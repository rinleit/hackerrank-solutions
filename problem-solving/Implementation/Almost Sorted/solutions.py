#!/bin/python3

import math
import os
import random
import re
import sys
from copy import copy

# Complete the almostSorted function below.
def almostSorted(arr):
    if arr == sorted(arr):
        print('yes')
        return

    n = len(arr)
    new_arr = list(map(lambda x: x[0] - x[1], zip(sorted(arr), arr)))
    new_arr_filter = list(filter(lambda x: x != 0, new_arr))
    set_arr = sorted(list(set(new_arr_filter)))
    
    if new_arr.count(0) == n - 2:
        print('yes')
        print('swap', new_arr.index(set_arr[0]) + 1, new_arr.index(set_arr[-1]) + 1)
        return
    
    n_new_arr = len(new_arr_filter)
    k = n_new_arr//2
    s1 = sum(new_arr_filter[:-k])
    s2 = sum(new_arr_filter[-k:])
    start_idx = new_arr.index(set_arr[0])
    end_idx = new_arr.index(set_arr[-1])
    if  s1 + s2 == 0 and n_new_arr % 2 == 0 and new_arr[start_idx:end_idx].count(0) <= 1:
            print('yes')
            print('reverse', start_idx + 1, end_idx + 1)
            return

    print('no')

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    almostSorted(arr)
    
