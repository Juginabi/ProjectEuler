#!/usr/bin/python
# Filename: Problem035.py
# Problem: Circular primes under million. 

from atkins import atkins
from listWorm import search

maximi = 999999
counter = 0
circulars = 0

def hasEvenDigits(n):
    strNum = str(n)
    if '0' in strNum or '2' in strNum or '4' in strNum or '6' in strNum or '8' in strNum:
        return True
    else:
        return False
 
#populate primeList
primeList = atkins(maximi)

while maximi > 1:
    if maximi == 2 or not hasEvenDigits(maximi):
        if search(maximi,primeList):
            iterator = 0
            tested = maximi
            while iterator < len(str(maximi)):
                origStr = list(str(tested))
                newStr = list(str(tested))
                while len(origStr) < len(str(maximi)):
                    origStr.insert(0, "0")
                    newStr.insert(0, "0")
                counter = 0
                while counter < len(str(maximi)):
                    newStr[counter-1] = origStr[counter]
                    counter += 1
                tested = int("".join(newStr))
                if search(tested,primeList):
                    if iterator == len(str(maximi))-1:
                        circulars += 1
                    pass
                else:
                    break
                iterator += 1
    counter = 0
    maximi -= 2
    if maximi == 1:
        maximi += 1
    elif maximi == 2:
        maximi = 1          
else:
    print 'Circular primes found: {0}'.format(circulars)
