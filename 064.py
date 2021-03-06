# Odd period square roots

# Problem 64
# https://projecteuler.net/problem=64
# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion
# https://www.mathblog.dk/project-euler-continued-fractions-odd-period/

import datetime
import math

start_time = datetime.datetime.now()

max = 10000
res = 0
for i in range(2, max + 1):
    limit = int(math.sqrt(i))
    if limit * limit == i:
        continue
    period = 0
    d = 1
    m = 0
    a = limit
    while True:
        m = d * a - m
        d = (i - m * m) // d
        a = (limit + m) // d
        period += 1
        if a == 2 * limit:
            break
    if period % 2 == 1:
        res += 1

stop_time = datetime.datetime.now()
print(stop_time - start_time)

print(res)
