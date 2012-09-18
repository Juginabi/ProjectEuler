from atkins import atkins
from listWorm import search
from random import *

maximi = 1000000
primeList = atkins(maximi)
#print(len(primeList))
i=0
while i < 1000:
    # Jos LSB bit eri kuin 1 niin luku ei voi olla prime.
    if not i & 1:
        i += 1
        continue
    # Luvulla mahdollisuus olla prime.
    search(randint(0,1000000-1), primeList)
    i += 1
