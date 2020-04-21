#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    hours = ("", "one", "two", "three", "four", "five", "six", 
                        "seven", "eight", "nine", "ten", 
                        "eleven", "twelve")
    minutes = ("", "one", "two", "three", "four", "five", "six", 
                        "seven", "eight", "nine", "ten", 
                        "eleven", "twelve", "thirteen", 
                        "fourteen","fifteen", "sixteen", 
                        "seventeen", "eighteen", "ninteen", 
                        "twenty", "twenty one", "twenty two", 
                        "twenty three", "twenty four", 
                        "twenty five", "twenty six", 
                        "twenty seven", "twenty eight", 
                        "twenty nine")

    formats = {
        0: "%s o' clock",
        15: "quarter past %s",    
        30: "half past %s",
        45: "quarter to %s",
    }
    if m % 15 == 0:
        time = formats[m] % hours[h + int(m > 30)]
    else:
        h, m, is_past = (h + 1, 60 - m, 'to') if m > 30 else (h, m, 'past')
        minutes_txt = 'minutes' if m > 1 else 'minute'
        time = "{} {} {} {}".format(minutes[m], minutes_txt, is_past, hours[h])
    
    return time

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
