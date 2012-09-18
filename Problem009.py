#!/usr/bin/python
# Filename: Problem009.py
# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.

# Euclid's formula: a = m^2 - n^2, b = 2mn, c = m^2 + n^2
a = 0   # Pythagora triangle shorter leg
b = 0   # Pythagora triangle longer leg
c = 0   # Pythagor triangle hypothenuse
m = 0   # Arbiraty positive integer m>n
n = 0   # Arbitary positive integer n<m

sumABsquare = 0
squareC = 0
running = True

while m < 1000:
    while n < m:
        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2
        if a+b+c == 1000:
            print('Pythagoran triplet found which has a + b + c = 1000!')
            print('{0} + {1} + {2} = 1000.\tProduct a * b * c = {3}'.format(a,b,c,a*b*c))
            m = 1000
            break
        n+=1
    n=1
    m+=1
