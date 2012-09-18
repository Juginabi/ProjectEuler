#!/usr/bin/python
# Filename: Problem002.py, projecteuler.net

sum = 2
firstNum = 1
secondNum = 2
thirdNum = 0

while thirdNum < 4000000:
    thirdNum = firstNum + secondNum
    if thirdNum % 2 == 0:
        sum += thirdNum
    firstNum = secondNum
    secondNum = thirdNum
else:
    print('Sum is: {0}'.format(sum))
