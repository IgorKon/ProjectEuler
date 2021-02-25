# Consecutive prime sum

# Problem 50
# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
# Which prime, below one-million, can be written as the sum of the most consecutive primes?
# https://projecteuler.net/problem=50

import datetime
import Utilities

start_time = datetime.datetime.now()

max_i = 999999

a = Utilities.Eratosthenes(max_i)
a_len = len(a)
b = []
sum = 0
for i in range(1, a_len):
    sum += a[i - 1]
    b.append(sum)

b_len = len(b)
ds_max = 0
curr_number = 0
for i in range(curr_number, b_len):
    for j in range(i - curr_number + 1, 0, -1):
        ds = b[i] - b[j]
        if ds > max_i:
            break
        if ds in a:
            curr_number = i - j
            ds_max = ds

print(ds_max, curr_number)

stop_time = datetime.datetime.now()
print(stop_time - start_time)
