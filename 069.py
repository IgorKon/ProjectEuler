# Totient maximum

# Problem 69
# https://projecteuler.net/problem=69

import datetime
import Utilities

max_i = 1000000

start_time = datetime.datetime.now()

max_n_phi = 0
max_n = 0
for n in range(max_i + 1):
    n_phi = n / Utilities.Phi(n)
    if max_n_phi < n_phi:
        max_n_phi = n_phi
        max_n = n

stop_time = datetime.datetime.now()
print(stop_time - start_time)

print(max_n,  max_n_phi)
