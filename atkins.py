#!/usr/bin/python
# Filename: atkins.py
# Sieve of atkins returns primeList containing all primes under given limit

def atkins(primeLimit):
    primeList = [2,3]
    limit = primeLimit
    primeSieve = [False] * (limit+1)
    sqrt = int(limit**0.5)+1
    primeappend = primeList.append

    for x in xrange(1,sqrt):
        xx = x*x
        for y in xrange(1,sqrt):
            yy = y*y
            n = 4*xx + yy
            if n <= limit:
                if (n % 12 == 1 or n % 12 == 5):
                    primeSieve[n] = not primeSieve[n]
                
            n = 3*xx + yy
            if n <= limit and n % 12 == 7:
                primeSieve[n] = not primeSieve[n]
            
            if x > y:    
                n = 3*xx - yy
                if n <= limit and n % 12 == 11:
                    primeSieve[n] = not primeSieve[n]  
                     
    for i in xrange(5,sqrt):
        if primeSieve[i]:
            s = i**2
            for k in xrange(s,limit,s):
                primeSieve[k] = False
                  
    for z in xrange(5,limit,2):
        if primeSieve[z]:
            primeappend(z)
    return primeList

def main():
    #number = input('Give a top limit for prime hunting: ')
    number = 999999
    primeList = atkins(number)
    print 'All primes under one million calculated! Len = {0}'.format(len(primeList))  
    
if __name__ == "__main__":
    main()
