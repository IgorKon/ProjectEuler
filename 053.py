# Combinatoric selections

# Problem 53
# There are exactly ten ways of selecting three from five, 12345:
# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
# In combinatorics, we use the notation, (5 / 3) = 10.
# In general, (n / r) = n! / (r! * (n - r)!), where 
# n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1, and 0! = 1.
# It is not until n = 23, that a value exceeds one-million: (23 / 10) = 1,144,066.
# How many, not necessarily distinct, values of (n / r) for 1 <= n <= 100, are greater than one-million?
# https://projecteuler.net/problem=53

import datetime
import Utilities

def GetFactorials(n):
    ff = 1
    f = []
    f.append(1)
    for i in range(1, n + 1):
        ff = ff * i
        f.append(ff) 
    return f

start_time = datetime.datetime.now()

fact = GetFactorials(100)

iMil = 0
for i in range(101):
    if fact[i] > 1000000:
        iMil = i
        break
iCount = 0
for i in range(iMil, 101):
    for j in range(1, i + 1):
        d = fact[i] / (fact[j] * fact[i - j])
        if d > 1000000:
            iCount += 1

stop_time = datetime.datetime.now()
print(stop_time - start_time)

print(iCount)