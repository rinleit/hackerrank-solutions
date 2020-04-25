#!/bin/python3

import math
import os
import random
import re
import sys

def sol(a):
    m = {}
    for i in range(len(a)):
        m[a[i]] = i 
        
    sorted_a = sorted(a)
    ret = 0
    
    for i in range(len(a)):
        if a[i] != sorted_a[i]:
            ret += 1
            ind_to_swap = m[ sorted_a[i] ]
            a[i], a[ind_to_swap] = sorted_a[i], a[i]
            m[ a[i] ] = m[ sorted_a[i]]
    return ret

if __name__ == '__main__':
    input()
    a = [int(i) for i in input().split(' ')]
    asc=sol(list(a))
    desc=sol(list(reversed(a)))
    print(min(asc,desc))

