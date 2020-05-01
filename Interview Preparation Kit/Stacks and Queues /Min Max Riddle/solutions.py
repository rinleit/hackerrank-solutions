#!/bin/python3

import os
import sys


# Complete the riddle function below.
def riddle(arr):
    maxes=[float("-inf")]*len(arr)
    for i in range(0,len(arr)):
        # find biggest window for which i is a minimum
        right=i
        left=i
        while right+1<len(arr) and arr[right+1]>=arr[i]:
            right+=1
        while left-1>=0 and arr[left-1]>=arr[i]:
            left-=1
        for j in range(right-left+1):
            maxes[j]=max(maxes[j],arr[i])
    return maxes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = riddle(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
