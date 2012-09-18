# Better search algorithm for searching large prime-lists
# Author: Jukka Vatjus-Anttila

def search(prime, primeList):
    MAX = len(primeList)-1
    MIN = 0
    
    for counter in range(1, 15):
        index = int((MAX+MIN)/2)
        if prime > primeList[index]:
            MIN = index
        else:
            MAX = index
    counter = 0
    index = (MAX-MIN)/2
    while counter <= index:
       if prime == primeList[MIN+counter] or prime == primeList[MAX-counter]:
           return True
       counter += 1
    return False
     
