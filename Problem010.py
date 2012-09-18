#!/usr/bin/python
# Filename: Problem010.py, projecteuler.net. Sum of all primes under 2M
from atkins import atkins

sumOfPrimes = 0
primeList = atkins(2000000)
for i in primeList:
    sumOfPrimes += i
print('Sum of all primes smaller than 2Million = {0}'.format(sumOfPrimes))

