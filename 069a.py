# Totient maximum

# Problem 69
# https://projecteuler.net/problem=69

import datetime
import Utilities

max_i = 1000000

start_time = datetime.datetime.now()
primes = Utilities.Eratosthenes(200)
max_n_phi = 0
max_n = 0
res = 1
i = 0
while True:
    res1 = res * primes[i]
    i += 1
    if res1 > max_i:
        break
    res = res1

stop_time = datetime.datetime.now()
print(stop_time - start_time)

print(res)
