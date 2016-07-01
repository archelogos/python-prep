#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))

    students = 0
    for student in a:
        if student <= 0:
            students += 1

    if students >= k:
        print 'NO'
    else:
        print 'YES'
