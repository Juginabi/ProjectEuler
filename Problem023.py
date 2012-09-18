#!/usr/bin/python
# Filename: Problem023.py
# Problem: Abundants
import math
import itertools

taulukko = []
amicables = []

def getSumOfDivisors(luku):
    summa = 1
    i = 1
    for i in range(2, int(math.sqrt(luku))+1):
        if luku%i == 0:
            summa += i
            if (i != luku / i):
                summa += luku / i 
    return summa

lista = [False]*28124
abundants = []
sumInts = 0

for i in range(12, 28124):
    if getSumOfDivisors(i) > i:
        abundants.append(i)

combs = itertools.combinations_with_replacement(abundants,2)

print("1: Abundant numbers found!")

for x in combs:
    i = x[0] + x[1]
    if (i < 28124):
        lista[i] = True

print("2: Done!")

for j in range(0,len(lista)):
    if lista[j] == False:
        sumInts += j

print ("3: Summa:", sumInts)
