#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())

    divisible = 0

    for digit in list(str(n)):
        if int(digit) != 0:
            if n % int(digit) == 0:
                divisible += 1

    print divisible        
