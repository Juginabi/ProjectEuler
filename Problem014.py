#!/usr/bin/python
# Filename: Problem014.py
# Which starting number, under one million, produces the longest Collaz chain?

counter = 999999
longest = 0
spreeStarter = 0

while counter > 1:
    result = counter
    spree = 0
    while result != 1:
        spree += 1
        if result % 2 == 0:
            result = result / 2
        else:
            result = result*3 + 1
    else:
        if spree > longest:
            spreeStarter = counter
            longest = spree
            print 'Longest spree so far is {0}. Chain starter {1}'.format(longest, spreeStarter)
    counter -= 1
else:
    print 'Longest spree was from {0}'.format(spreeStarter)    
         
        
