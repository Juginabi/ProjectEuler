alphabets = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6, 'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10, 'K' : 11, 'L' : 12, 'M' : 13, 'N' : 14, 'O' : 15, 'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20, 'U' : 21, 'V' : 22, 'W' : 23, 'X' : 24, 'Y' : 25, 'Z' : 26}
result = []

with open('names.txt','r') as nameFile:
    names = nameFile.read()
    lalla = names.split(",")
    for i in range(0,len(lalla)):
        result.append(lalla[i].replace("\"",""))
    nameFile.close()

result.sort()
position = 1
nameSum = 0
finalSum = 0
for i in result:
    for j in i:
        nameSum += alphabets[j]
    finalSum += nameSum*position
    nameSum = 0
    position += 1
print("Final sum:", finalSum)
