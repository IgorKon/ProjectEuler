# Counting fractions in a range

# Problem 73
# Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
# If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:
# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
# It can be seen that there are 3 fractions between 1/3 and 1/2.
# How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?
# https://projecteuler.net/problem=73

import datetime
import math

max_i = 12000
start_time = datetime.datetime.now()
count = 0
for d in range(5, max_i + 1):
    start_n =  d // 3 + 1
    stop_n =  (d - 1) // 2 + 1
    for n in range(start_n, stop_n):
            nod = math.gcd(n, d)
            if nod == 1:
                count += 1

stop_time = datetime.datetime.now()
print(stop_time - start_time)
print(count)
