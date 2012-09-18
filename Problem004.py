#!/usr/bin/python
# Filename: Problem004.py, projecteuler.net
# Largest palindrome numeral made from product of two 3-digit numbers

def reverse(number):
    numList = list(str(number))
    length = len(numList) - 1
    reverseNum = []
    
    while length >= 0:
        reverseNum.append(numList[length])
        length-=1
    return int("".join(reverseNum))
    
firstNum = 999
secondNum = 999
product = 0
reverseProduct = 0
largestPalindrome = 0

while firstNum > 99:
    while secondNum > 99:
        product = firstNum * secondNum
        reverseProduct = reverse(product)
        if product == reverseProduct and reverseProduct > largestPalindrome:
            print('FOUND: {0} * {1} = {2} and reverse is {3}'.format(firstNum, secondNum, product, reverseProduct))
            largestPalindrome = reverseProduct
        secondNum-=1
    secondNum = 999
    firstNum-=1
    if firstNum * secondNum < largestPalindrome:
        print('No longer possible to have product larger than {0}'.format(largestPalindrome))
        firstNum = 0
else:    
    print('Largest palindrome was {0}'.format(largestPalindrome))
