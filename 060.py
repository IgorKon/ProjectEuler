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
# a2 = Utilities.Eratosthenes(max_i // 10)
# a = set()
# a.add(3)
# a.add(7)
# a1_len = len(a1)
# for ii in range(a1_len-1, 1, -1):
#     i = a1[ii]
#     i_len = len(str(i))
#     if i_len == 4:
#         j = int(str(i)[:2])
#         if j in a1:
#             a.add(j)
#         j = int(str(i)[1:3])
#         if j in a1:
#             a.add(j)
#         j = int(str(i)[2:])
#         if j in a1:
#             a.add(j)
#         j = int(str(i)[:3])
#         if j in a1:
#             a.add(j)
#         j = int(str(i)[1:])
#         if j in a1:
#             a.add(j)
#     elif i_len == 3:
#         j = int(str(i)[:2])
#         if j in a1:
#             a.add(j)
#         j = int(str(i)[1:])
#         if j in a1:
#             a.add(j)
#     else:
#         break
res = []
for b in itertools.combinations(a, 5):
    bPrime = True
    for c in itertools.combinations(b, 2):
        i = int(str(c[0]) + str(c[1]))
        bPrime = bPrime and Utilities.IsPrime(i)
        if not bPrime:
            break
        i = int(str(c[1]) + str(c[0]))
        bPrime = bPrime and Utilities.IsPrime(i)
        if not bPrime:
            break
    if bPrime:
        res.append(sum(b))

stop_time = datetime.datetime.now()
print(stop_time - start_time)
if len(res) > 0:
    print(min(res))
else:
    print('Not Found')
