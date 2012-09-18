#!/bin/python
# If all numbers were written in words from 1-1000, how many letters would be used?

def countDigits(n):
    strN = str(n)
    digits = 0
    for i in strN:
        if i == '-' or i == ' ' or i == '\n':
            continue
        else:
            digits += 1
    return digits

digitNames = {0:'',1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen',19:'nineteen', 20:'twenty', 30:'thirty',40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety', 100:'hundred', 1000:'thousand'}
counter = 0
name = ""

for number in range(1,1001):
    if number < 20:
        name = digitNames[number]
    elif len(str(number)) == 2 and not number % 10:
        name = digitNames[int(str(number)[0])*10]
    elif len(str(number)) == 2:
        name = digitNames[int(str(number)[0])*10] +"-"+ digitNames[int(str(number)[1])]
    elif len(str(number)) == 3 and not number % 100:
        name = digitNames[int(str(number)[0])] +" "+digitNames[100]
    elif len(str(number)) == 3 and int(str(number)[1]) == 0:
        name = digitNames[int(str(number)[0])] +" "+digitNames[100] +" and "+ digitNames[int(str(number)[2])]
    elif len(str(number)) == 3 and int(str(number)[1]) == 1 and int(str(number)[2]) == 0:
        name = digitNames[int(str(number)[0])] +" "+digitNames[100] +" and "+ digitNames[10]
    elif len(str(number)) == 3 and int(str(number)[1]) == 1 and not int(str(number)[2]) == 0:
        name = digitNames[int(str(number)[0])] +" "+digitNames[100] +" and "+ digitNames[int(str(number)[1]+str(number)[2])]
    elif len(str(number)) == 3 and int(str(number)[1]) == 2 and int(str(number)[2]) == 0:
        name = digitNames[int(str(number)[0])] +" "+digitNames[100] +" and "+ digitNames[20]
    elif len(str(number)) == 3:
        name = digitNames[int(str(number)[0])] +" "+digitNames[100] +" and "+ digitNames[int(str(number)[1])*10] +"-"+ digitNames[int(str(number)[2])]
    elif len(str(number)) == 4:
        name = digitNames[int(str(number)[0])] + " " + digitNames[number]
    counter += countDigits(name)
print 'Sum of letters: {0}'.format(counter)    
        
        
