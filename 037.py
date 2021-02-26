# Truncatable primes

# Problem 37
# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits 
# from left to right, and remain prime at each stage: 3797, 797, 97, and 7. 
# Similarly we can work from right to left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
# https://projecteuler.net/problem=37

import datetime
import Utilities

start_time = datetime.datetime.now()
i = 9
iCount = 0
res = []
while iCount < 11:
    i += 2
    b = False
    ii = 0
    if Utilities.IsPrime(i):
        s = str(i)
        iLength = len(s)
        for j in range(1, iLength):
            k = int(s[j::])
            if Utilities.IsPrime(k):
                ii += 1
                k = int(s[:iLength - j])
                if Utilities.IsPrime(k):
                    ii += 1
                else:
                    break
            else:
                break
        if ii == 2*iLength - 2:
            iCount += 1
            res.append(i)
print(sum(res))
print(res)
stop_time = datetime.datetime.now()
print(stop_time - start_time)