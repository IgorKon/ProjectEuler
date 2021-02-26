# Prime pair sets

# Problem 60
# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in 
# any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. 
# The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.
# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
# https://projecteuler.net/problem=60

import datetime
import Utilities
import itertools

start_time = datetime.datetime.now()

max_i = 1000

a = Utilities.Eratosthenes(max_i)
del a[0]
del a[1]

GoodPairs = set()

for b in itertools.combinations(a, 2):
    bPrime = True
    i = int(str(b[0]) + str(b[1]))
    bPrime = bPrime and Utilities.IsPrime(i)
    i = int(str(b[1]) + str(b[0]))
    bPrime = bPrime and Utilities.IsPrime(i)
    if bPrime:
        GoodPairs.add((b[0], b[1]))

stop_time = datetime.datetime.now()
print(stop_time - start_time)

res = []
badPairs = set()
for b in itertools.combinations(a, 5):
    bPrime = True
    for p in badPairs:
        if p[0] in b and p[1] in b:
            bPrime = False
            break
    if bPrime:
        for c in itertools.combinations(b, 2):
            i = int(str(c[0]) + str(c[1]))
            bPrime = bPrime and Utilities.IsPrime(i)
            if not bPrime:
                badPairs.add((c[0], c[1]))
                break
            i = int(str(c[1]) + str(c[0]))
            bPrime = bPrime and Utilities.IsPrime(i)
            if not bPrime:
                badPairs.add((c[0], c[1]))
                break
        if bPrime:
            res.append(sum(b))

stop_time = datetime.datetime.now()
print(stop_time - start_time)
if len(res) > 0:
    print(min(res))
else:
    print('Not Found')
