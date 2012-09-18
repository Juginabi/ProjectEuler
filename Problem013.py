#!/usr/bin/python
# Filename: Problem013.py
# What are the 1st ten digits of the sum of one hundred 50digit numbers (100x50.txt)

FILE = open('100x50.txt')
running = True
result = 0

while running:
    testaus = FILE.readline().rstrip('\n')
    if testaus == "":
        running = False
        break
    calc = int(testaus)
    result += calc
print 'Sum of all numbers are {0}'.format(result)
