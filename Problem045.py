#!/usr/bin/python
# Filename: Problem0012.py, projecteuler.net
# What is the value of the first triangle number to have over five hundred divisors?
from listWorm import search

def triangleNum(n):
    return (n**2 + n)/2

def pentagonNum(n):
    return (3*n**2 - n)/2

def hexagonNum(n):
    return (2*n**2 - n)
     	        
integer = [165, 143, 285]
triList = []
hexList = []
penList = []

for i in range(1,56000):
    triList.append(triangleNum(i))
    hexList.append(hexagonNum(i))
    penList.append(pentagonNum(i))

for i in triList:
    if search(i,hexList):
        if search(i,penList):
            print 'Found num that is tri, hex and pen number: {0}'.format(i)    
