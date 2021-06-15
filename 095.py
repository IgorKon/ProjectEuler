# Amicable chains

# Problem 95
# The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. 
# As the sum of these divisors is equal to 28, we call it a perfect number.
# Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220, forming a chain of two numbers. 
# For this reason, 220 and 284 are called an amicable pair.
# Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:
#     12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)
# Since this chain returns to its starting point, it is called an amicable chain.
# Find the smallest member of the longest amicable chain with no element exceeding one million.
# https://projecteuler.net/problem=95

import math
import datetime

def IsSqr(n):
    x = math.ceil((math.sqrt(n)))
    return (x * x == n)

def GetDevidersSumm(n):
    res = 1
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            res += i
    # if IsSqr(n):
    #     res -= 1
    return res

limit = 1000000
start_time = datetime.datetime.now()
l = list()
length = 0

i = 6
while i < limit:
    i += 1
    summ = i
    l.clear()
    while True:
        summ = GetDevidersSumm(summ)
        if summ > limit:
           break 
        if summ in l:
            if summ == l[0]:
                if length < len(l):
                    length = len(l)
                    AmicableChain = l[:]
            break
        else:
            l.append(summ)


stop_time = datetime.datetime.now()
print(stop_time - start_time)
print(length)
print(AmicableChain)

