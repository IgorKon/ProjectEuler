# Prime power triples

# Problem 87
# The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. 
# In fact, there are exactly four numbers below fifty that can be expressed in such a way:

# 28 = 2**2 + 2**3 + 2**4
# 33 = 3**2 + 2**3 + 2**4
# 49 = 5**2 + 2**3 + 2**4
# 47 = 2**2 + 3**3 + 2**4

# How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?
# https://projecteuler.net/problem=87

import datetime
import Utilities
import math

m = 50000000
primes = Utilities.Eratosthenes(int(math.sqrt(m)) + 1)

start_time = datetime.datetime.now()
count = 0

powers = []
temp = primes[:]
i = 0
count = len(primes)
for k in range(3):
    for i in range(count):
        temp[i] *= primes[i]
    powers.append(temp[:])
result = set()
for i in range(count):
    for j in range(count):
        for k in range(count):
            n = powers[0][i] + powers[1][j] + powers[2][k]
            if n > m:
                break
            result.add(n)

stop_time = datetime.datetime.now()
print(stop_time - start_time)
print(len(result))

