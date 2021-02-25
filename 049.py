# Prime permutations

# Problem 49
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: 
# (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, 
# but there is one other 4-digit increasing sequence.
# What 12-digit number do you form by concatenating the three terms in this sequence?
# https://projecteuler.net/problem=49

import datetime
import Utilities
from itertools import permutations

start_time = datetime.datetime.now()

max_i = 9999

a = Utilities.Eratosthenes(max_i)
b = [i for i in a if i > 1000]
icount = 0
bFound = False
for i in b:
    c = set(int(k) for k in str(i))
    d = [j for j in b if j > i and (set((int(m) for m in str(j))) == c)]
    for j in d:
        for k in d:
            if k > j:
                if j - i == k - j:
                    print(i, j, k)
                    icount += 1
                    if icount == 2:
                        bFound = True
                        break
        if bFound:
            break
    if bFound:
        break
                
stop_time = datetime.datetime.now()
print(stop_time - start_time)
