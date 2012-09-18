#!/usr/bin/python
# Filename: Problem034.py
# Problem: Curious numbers. 145 = 1! + 4! + 5! = 145

import math

counter = 135
curiousList = []
total = 0

for k in xrange(1,1000000):
    strNum = str(counter)
    for i in strNum:
        total += math.factorial(int(i))
    if total == counter:
        curiousList.append(counter) 
    total = 0
    counter += 1
else:
    print 'Curious list = {0}'.format(curiousList)
    summa = 0
    for i in curiousList:
        summa += i
    print 'Sum of curious list numbers are {0}'.format(summa)
