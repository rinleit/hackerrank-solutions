#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the acmTeam function below.
def acmTeam(topic, n, m):
    teams = []
    for i in range(n):
        for j in range(i+1, n):
            num_topic = m - list(zip(topic[i], topic[j])).count(('0','0'))
            teams += [num_topic]
    max_num_topic = max(teams)
    return [max_num_topic, teams.count(max_num_topic)]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic, n, m)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
