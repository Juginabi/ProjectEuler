#!/usr/bin/python
# Filename: Problem005.py, projecteuler.net
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

running = True
counter = 380

while running:
    if counter % 11 == 0 and counter % 17 == 0:
        if counter % 13 == 0 and counter % 16 == 0:
            if counter % 15 == 0 and counter % 18 == 0:
                if counter % 14 == 0 and counter % 12 == 0:
                        print('Smalles number evenly divisible by 1-20 is {0}'.format(counter))
                        running = False
    counter += 380 # First number divisible by 19 and 20
