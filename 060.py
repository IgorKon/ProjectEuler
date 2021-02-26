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

max_i = 10000

a = Utilities.Eratosthenes(max_i)
del a[0]
del a[1]
a_len = len(a)
GoodPairs = set()

for b in itertools.combinations(a, 2):
    i = int(str(b[0]) + str(b[1]))
    if Utilities.IsPrime(i):
        i = int(str(b[1]) + str(b[0]))
        if Utilities.IsPrime(i):
            GoodPairs.add((b[0], b[1]))

stop_time = datetime.datetime.now()
print(stop_time - start_time)

res = []
# for ii1 in range(a_len):
#     i1 = a[ii1]
#     for ii2 in range(ii1, a_len):
#         i2 = a[ii2]
#         if (i1, i2) in GoodPairs:
#             for ii3 in range(ii2, a_len):
#                 i3 = a[ii3]
#                 if (i1, i3) in GoodPairs and (i2, i3) in GoodPairs:
#                     for ii4 in range(ii3, a_len):
#                         i4 = a[ii4]
#                         if (i1, i4) in GoodPairs and (i2, i4) in GoodPairs and\
#                            (i3, i4) in GoodPairs:
#                            for ii5 in range(ii4, a_len):
#                                i5 = a[ii4]
#                                if (i1, i5) in GoodPairs and (i2, i5) in GoodPairs and\
#                                    (i3, i5) in GoodPairs and (i4, i5) in GoodPairs:
#                                    res.append(i1 + i2 + i3 + i4 + i5)

for i1 in a:
     for i2 in a:
         if (i1, i2) in GoodPairs:
             for i3 in a:
                 if (i1, i3) in GoodPairs and (i2, i3) in GoodPairs:
                     for i4 in a:
                         if (i1, i4) in GoodPairs and (i2, i4) in GoodPairs and\
                            (i3, i4) in GoodPairs:
                            for i5 in a:
                                if (i1, i5) in GoodPairs and (i2, i5) in GoodPairs and\
                                    (i3, i5) in GoodPairs and (i4, i5) in GoodPairs:
                                    print(i1, i2, i3, i4, i5)
                                    res.append(i1 + i2 + i3 + i4 + i5)

stop_time = datetime.datetime.now()
print(stop_time - start_time)

print('Good pairs count:', len(GoodPairs))
if len(res) > 0:
    print(min(res))
else:
    print('Not Found')
