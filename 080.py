# Square root digital expansion

# Problem 80

# It is well known that if the square root of a natural number is not an integer, then it is irrational. 
# The decimal expansion of such square roots is infinite without any repeating pattern at all.
# The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.
# For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.

# https://projecteuler.net/problem=80

import Utilities
import decimal
decimal.getcontext().prec = 110

nums = list()
for i in range(2,101):
    if not Utilities.IsSquareNum(i):
        nums.append(i)
sm = 0
for i in nums:
    sqr = decimal.Decimal(i).sqrt()
    s1 = 0
    for c in str(sqr)[0:101]:
        if c == '.': 
            continue
        s1 += int(c)
    print(i, s1, sqr)
    sm += s1    
print(sm)