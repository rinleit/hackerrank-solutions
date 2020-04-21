#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    n = len(s)
    time_format = s[n-2:n]
    hh, mm, ss = s[:n-2].split(':')
    if time_format == 'AM':
        hh = int(hh) % 12
    if time_format == 'PM':
        hh = int(hh) % 12 + 12
    return "{}:{}:{}".format(str(hh).zfill(2), mm, ss)



if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
