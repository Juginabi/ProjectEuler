#!/usr/bin/python
# Filename: Problem003.py, projecteuler.net
# Prime factorization

import sys
from atkins import atkins
from listWorm import search

# Function isPrime checks if given parameter is prime number
def isPrime(num):
    
    num = abs(num)
    global largestPrimeFactor
    global number
    global primeFactors
         
    if num == 1:
        print('Is not a prime!')
        return False
    elif num == 2:
        print('Is a prime!')
        return True
    elif not num & 1:
        print('Is NOT a prime!')
        return False
    else:
        #  Trial division: Routine consists in dividing num by each integer i which is greater than 1 and less than or equal to the square root of num.
        maximum = (num**0.5)+1
        i = 3
        while i <= maximum:
            if not i % 1000001:
                print('Checking if prime or not... <iteration at {0} out of {1}>'.format(i, maximum))
            if num % i == 0:
                #print('Number {0} is not prime. It is divisable by {1}'.format(num,i))
                if isPrime(i):
                    if i > largestPrimeFactor:
                        largestPrimeFactor = i
                number = num/i
                return False
            i+=2
        else:
            print('Number {0} is a prime.'.format(num))
            primeFactors.append(num)
            if num > largestPrimeFactor:
                largestPrimeFactor = num
            return True
 # Function isPrime definition ends here
 
number = 0           
largestPrimeFactor = 0
primeFactors = []

number = input('Give a number: ')
#number = 600851475143
originalNum = number

if not number < 0 and number & 1:
    while not isPrime(number):
        continue        
    
    else:
        sys.stdout.write('{0} = '.format(originalNum))
        n = 0
        for i in primeFactors:
            if n == 0:
                sys.stdout.write("%s * " %i)
            elif n != len(primeFactors)-1:
                sys.stdout.write(" %s * " %i)
            else:
                sys.stdout.write(" %s\n" %i)
            n+=1
            
else:
    print('Give positive non even number please!')

