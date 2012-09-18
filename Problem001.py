#!/usr/bin/python
# Filename: Problem001.py, projecteuler.net

sum = 0

for i in range(0,1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i;
    i += 1
else:
    print('Vastaus: {0}'.format(sum))
