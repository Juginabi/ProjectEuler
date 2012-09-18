#!/usr/bin/python
# Filename: Problem021.py
# Problem: Evaluate the sum of all the amicable numbers under 10000.
import math
taulukko = []
amicables = []

def sOD(x):
    s = 1
    for i in range(2, int(math.sqrt(x)) + 1):
        if (x % i == 0):
            s += i
            s += x / i
    return s

def summa():
    sum = 0
    for i in range(1, 10000):
        x = sOD(i)
        if (sOD(x) == i):
            if (i != x):
                sum += i
    return sum

print ("Amicable sum: ",summa())
