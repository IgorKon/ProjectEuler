# 10001st prime

# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
# https://projecteuler.net/problem=7

import Utilities
i = 6
n = 13
while True:
    n += 2
    if Utilities.IsPrime(n): i += 1
    if i == 10001: break
print(n)
print(104743)