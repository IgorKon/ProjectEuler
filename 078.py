# Coin partitions

# Problem 78
# Let p(n) represent the number of different ways in which n coins can be separated into piles.
# For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.

# OOOOO
# OOOO   O
# OOO   OO
# OOO   O   O
# OO   OO   O
# OO   O   O   O
# O   O   O   O   O
# Find the least value of n for which p(n) is divisible by one million.
# https://projecteuler.net/problem=78
# https://en.wikipedia.org/wiki/Partition_%28number_theory%29

import datetime
import Utilities
n = 1
p = list()
p.append(1)
start_time = datetime.datetime.now()
while True:
    i = 0
    penta = 1
    p.append(0)
    while penta <= n:
        if i % 4 > 1:
            sign = -1
        else:
            sign = 1
        p[n] += sign * p[n - penta]
        p[n] %= 1000000
        i += 1
        if i % 2 == 0:
            j = i // 2 + 1
        else:
            j = -( i // 2 + 1)
        penta = j * (3 * j - 1) // 2
    if p[n] == 0:
        break
    n += 1

stop_time = datetime.datetime.now()
print(stop_time - start_time)
print(n)
