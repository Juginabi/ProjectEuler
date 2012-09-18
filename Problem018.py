#!/usr/bin/python
# Filename: Problem011.py
# What is the greatest sum from top to bottom in pyramid of numbers?

FILE = open('15levelPyramid.txt')
line = []
listOfNums = []
joku = "joku"
# Luetaan pyramidi taulukkoon.
while joku != "":
    joku = FILE.readline()
    joku = joku.strip('\n')
    joku = joku.strip('\r')
    rem = joku[:]
    while len(rem) > 0:
        line.append(int(rem[:2]))
        rem = rem[3:]
    listOfNums.append(line)
    line = []

listOfNums.pop()
paraIndex = 0
while len(listOfNums) != 1:
    length = len(listOfNums)
    length_1 = length-1
    length_2 = length-2
    if listOfNums[length_1][paraIndex] > listOfNums[length_1][paraIndex+1]:
        listOfNums[length_2][paraIndex] += listOfNums[length_1][paraIndex]
    else:
        listOfNums[length_2][paraIndex] += listOfNums[length_1][paraIndex+1]
    if paraIndex < len(listOfNums[length_2]):
        paraIndex += 1
        if paraIndex == len(listOfNums[length_2]):
            paraIndex = 0
            listOfNums.pop()
print 'Maximi summa: {0}'.format(listOfNums[0][0])
        
        
        










