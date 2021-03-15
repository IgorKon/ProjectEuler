# Counting fractions

# Problem 72
# Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
# If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:
# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
# It can be seen that there are 21 elements in this set.
# How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?
# https://projecteuler.net/problem=72

# So we need to calculate sum(psi(n)) for n [2..1000000]

import datetime

max_i = 10**6
res = dict()
count = 0

start_time = datetime.datetime.now()

phi = list(range(0, max_i + 1))
for i in range(2, max_i + 1):
    if phi[i] == i:
        for j in range(i, max_i + 1, i):
            phi[j] = phi[j] // i * (i - 1)
    count += phi[i]

stop_time = datetime.datetime.now()
print(stop_time - start_time)
print(count)