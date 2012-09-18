#!/usr/bin/python
# Filename: Problem021.py
# Problem: Evaluate the sum of all the amicable numbers under 10000.
taulukko = []
amicables = []

def getDivisors(divs):
    taulukko = []
    i = 1
    while i <= divs/2:
        if divs%i == 0:
            taulukko.append(i)
        i+=1
    return taulukko

def summa(list):
    sum = 0
    for x in list:
        sum += x
    return sum

counter = 2

while counter <= 10000:
    # Divisors for current counter value
    divisors = getDivisors(counter)
    # Sum for current counter value
    sum = summa(divisors)

    divisors2 = getDivisors(sum)
    sum2 = summa(divisors2)
    
    if sum2 == counter and sum2 !=  sum:
        print("Amicable pair found: ", counter)
        amicables.append(counter)    
    # All amicable numbers under 10k are even. Cheat.
    #counter += 1
    counter += 2

print ("Amicable pairs =", amicables)

aSum = summa(amicables)
print ("Amicable sum: ",aSum)
