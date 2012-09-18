#!/usr/bin/python
# Filename: Problem016.py
# Problem: Sum of digits of 2^1000
import math

number = 2**1000
numberT = str(number)
sumOfNumber = 0

for i in numberT:
    sumOfNumber += int(i)
else:
    print 'sum of digits were: {0}'.format(sumOfNumber)


