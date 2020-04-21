#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.

def is_leap_year(year):
    is_leap_year = 0
    if year <= 1917:
        if year % 4 == 0:
            is_leap_year = 1
    else:
        if year % 400 == 0:
            is_leap_year = 1
        else:
            if year % 4 == 0 and year % 100 != 0:
                is_leap_year = 1
    return is_leap_year

def day_of_months(is_leap):
    if is_leap:
        return [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def dayOfProgrammer(year):
    day_256_th = 256
    month = 1
    while day_256_th > 31:
        if year == 1918 and month == 2:
            # February, 1918 have only 15 days
            day_256_th -= (day_of_months(is_leap_year(year))[month] - 14 + 1)
        else:
            day_256_th -= day_of_months(is_leap_year(year))[month]
        month += 1
    return "{}.{}.{}".format(str(day_256_th).zfill(2), str(month).zfill(2), year)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
