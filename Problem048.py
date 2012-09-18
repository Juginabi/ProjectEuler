base = 1
summa = 0

for base in xrange(1,1000):
    summa += base**base
strSumma = str(summa)
print strSumma[-10:]
