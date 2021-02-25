# Distinct primes factors

# Problem 47
# The first two consecutive numbers to have two distinct prime factors are:
# 14 = 2 × 7
# 15 = 3 × 5
# The first three consecutive numbers to have three distinct prime factors are:
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

import datetime
import Utilities

start_time = datetime.datetime.now()

def SetByDividers(n):
    d = Utilities.GetPrimeDividers(n)
    res = set()
    for k in d.keys():
        res.add(str(k) + '_' + str(d[k]))
    return res

d2 = SetByDividers(640)
d3 = SetByDividers(641)
d4 = SetByDividers(642)

for i in range(643, 1000001):
    d1 = d2
    d2 = d3
    d3 = d4
    d4 = SetByDividers(i)
    if len(d1) == 4 and len(d2) == 4 and len(d3) == 4 and len(d4) == 4:
        if d1.isdisjoint(d2) and d1.isdisjoint(d3) and d1.isdisjoint(d4) and d2.isdisjoint(d3) and d2.isdisjoint(d4) and d3.isdisjoint(d4):
            print(i - 3)
            break

stop_time = datetime.datetime.now()
print(stop_time - start_time)
