#!/usr/bin/python
# Filename: Problem011.py
# What is the greatest product of four adjacent numbers in any direction (up, down, left, right, or diagonally) in the 20x20 grid?

FILE = open('20x20_grid.txt')
running = True
result = 0
listOfNumbers = []
finalList = []
largestFactor = 0

# This while loop parses 20x20 grid of numbers from file and prepares it as two dimensional list of integers
while running:
    testaus = FILE.read(3)
    if testaus == "":
        break
    if testaus[0] == '0':
        result = int(testaus)
        listOfNumbers.append(result)
        if testaus[2] == '\n':
            finalList.append(listOfNumbers)
            listOfNumbers = []
        testaus = ""
    else:
        result = int(testaus)
        listOfNumbers.append(result)
        result = 0
        if testaus[2] == '\n':
            finalList.append(listOfNumbers)
            listOfNumbers = []
        testaus = ""

i = 0
j = 0

while i < 20:
    while j < 20:
        if j < 16:
            result = finalList[i][j] * finalList[i][j+1] * finalList[i][j+2] * finalList[i][j+3]
            if  result > largestFactor:
                largestFactor = result
                print 'Largest factor so far: {0}. Row: {1}, column: {2} right.'.format(largestFactor, i, j )
        if i < 16:
            result = finalList[i][j] * finalList[i+1][j] * finalList[i+2][j] * finalList[i+3][j]
            if result > largestFactor:
                largestFactor = result
                print 'Largest factor so far: {0}. Row: {1}, column: {2} down.'.format(largestFactor, i, j )
        if i < 16 and j < 16:
            result = finalList[i][j] * finalList[i+1][j+1] * finalList[i+2][j+2] * finalList[i+3][j+3]
            if result > largestFactor:
                largestFactor = result
                print 'Largest factor so far: {0}. Row: {1}, column: {2} diagonal down right.'.format(largestFactor, i, j)
        if i < 15 and j > 3:
            result = finalList[i][j] * finalList[i+1][j-1] * finalList[i+2][j-2] * finalList[i+3][j-3]
            if result > largestFactor:
                largestFactor = result
                print 'Largest factor so far: {0}. Row: {1}, column: {2} diagonal down left.'.format(largestFactor, i, j)
        j+=1
    j = 0
    i+=1

i = 0
j = 0

