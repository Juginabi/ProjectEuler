#!/usr/bin/python
# Filename: Problem005.py, projecteuler.net
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# Returns the sum of all the numbers between [first, last]
def ownSum(first, last):
    summary = 0
    i = 1
    while i <= last:
        summary += i
        i+=1
    else:
        print('sum 1-100 is {0}'.format(summary))
        return summary

# Returns the sum squares of all the numbers between [first, last]      
def sumOfSquares(first,last):
    summary = 0
    i = 1
    while i <= last:
        summary += i**2
        print('{0} = {1}^2'.format(summary,i))
        i+=1
    else:
        return summary
        
squareOfSums = ownSum(1,100)**2
sumOfSqrs = sumOfSquares(1,100)
difference = squareOfSums - sumOfSqrs

print('Difference between sum of squares and square of the sums is {0} - {1} = {2}'.format(squareOfSums, sumOfSqrs, difference))       
        
