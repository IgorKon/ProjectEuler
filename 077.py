# Prime summations

# Problem 77
# It is possible to write ten as the sum of primes in exactly five different ways:
# 7 + 3
# 5 + 5
# 5 + 3 + 2
# 3 + 3 + 2 + 2
# 2 + 2 + 2 + 2 + 2
# What is the first value which can be written as the sum of primes in over five thousand different ways?

# https://projecteuler.net/problem=77

import datetime
import Utilities

target = 2
start_time = datetime.datetime.now()
primes = Utilities.Eratosthenes(1000)
while True:
    ways = list()
    for i in range(target+1):
        ways.append(0)
    ways[0] = 1
    for i in range(len(primes)):
        for j in range(primes[i], target + 1):
            ways[j] += ways[j - primes[i]]
    if ways[target] > 5000:
        break
    target += 1

stop_time = datetime.datetime.now()
print(stop_time - start_time)
print(target)
