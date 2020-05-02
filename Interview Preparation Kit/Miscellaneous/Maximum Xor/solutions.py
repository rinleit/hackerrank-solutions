#!/bin/python3

import math
import os
import random
import re
import sys

class Trie:
    def __init__(self):
        self.root = dict()
    
    def build(self, arr):
        for n in arr:
            self.add(n)

    def add(self, number):
        word = "{:032b}".format(number)
        curr = self.root
        for c in word:
            c = int(c)
            if c not in curr:
                curr[c] = dict()
                curr['*'] = False
            curr = curr[c]
        curr['*'] = True
    
    def find_best_number_to_xor(self, number):
        word = "{:032b}".format(number)
        curr = self.root
        best_number = ''
        for c in word:
            c = int(c)
            xor = c ^ 1
            c = xor if xor in curr else c
            curr = curr[c]
            best_number += str(c)
        return int(best_number, 2)

# Complete the maxXor function below.
def maxXor(arr, queries):
    trie = Trie()
    trie.build(arr)
    for v in queries:
        yield (v ^ trie.find_best_number_to_xor(v))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    queries = []

    for _ in range(m):
        queries_item = int(input())
        queries.append(queries_item)

    result = maxXor(arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
