#!/usr/bin/python
# Filename: Problem0012.py, projecteuler.net
# What is the value of the first triangle number to have over five hundred divisors?

factorList = []

def isPrime(n):
    if n == 1 or n == 0:
        return False
    if n == 2:
        return True
    else:
        maximum = int(n**0.5)+1
        for i in xrange(2,maximum,1):
            if n % i == 0:
                return i
        else:
            return 1

def triangleNum(n):
    return (n**2 + n)/2

def factors(n):
    global factorList
    var = isPrime(n)
    num = n/var
    if var == 1:
        factorList.append(n)
    else:
        factors(var)
        factors(num)
   
def getDiv(n):
    exponents = []
    n.reverse()
    while len(n) > 0:
        counter = n.count(n[-1])
        exponents.append(counter)
        while counter > 0:
            n.pop()
            counter -= 1
    k = 1
    for i in exponents:
        k *= (i+1)
    return k
     	        
integer = 2
largest = 0

while largest <= 500:
    triangle = triangleNum(integer)
    if isPrime(triangle) == 1:
        integer += 1
        continue
    factors(triangle)
    divisors = getDiv(factorList)
    if divisors > largest:
        print 'Most factors found so far is with integer {0} (triangle {1}) with {2} divisors!'.format(integer, triangle, divisors)
        largest = divisors
    integer += 1
else:    
    print '\n{0} is first to have more than 500 divisors ({1} to be exact).'.format(triangleNum(integer-1), largest)
