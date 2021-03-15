# Totient permutation

# Problem 70
# Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive
# numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, 
# are all less than nine and relatively prime to nine, φ(9)=6.
# The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.
# Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.
# Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.
# https://projecteuler.net/problem=70

import datetime
import Utilities

def IsPermutation(i, j):
    ai = list(str(i))
    ai.sort(reverse = True)
    aj = list(str(j))
    aj.sort(reverse = True)
    return ai == aj

max_n = 10**7
start_time = datetime.datetime.now()

primes = Utilities.Eratosthenes(5000)
min_prime = 2000
while True:
    if primes[0] < min_prime:
        del primes[0]
    else:
        break

min_n_phi = 10
min_n = 0
l = len(primes)
for i in range(l):
    for j in range(i, l):
        n = primes[i] * primes[j]
        if n > max_n:
            break
        phi_n = (primes[i] - 1) * (primes[j] - 1)
        if IsPermutation(n, phi_n):
            n_phi = n / phi_n
            if min_n_phi > n_phi:
                min_n_phi = n_phi
                min_n = n
stop_time = datetime.datetime.now()
print(stop_time - start_time)

print(min_n,  min_n_phi)
