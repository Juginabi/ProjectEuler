#!/usr/bin/python
# Filename: Problem020.py
# Problem: Sum of digits of 100!
import math

number = math.factorial(100)
numberT = str(number)
sumOfNumber = 0

for i in numberT:
    sumOfNumber += int(i)
else:
    print 'sum of digits were: {0}'.format(sumOfNumber)
