# Largest palindrome product

# Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
# https://projecteuler.net/problem=4

import time

def IsPolindromInt(k):
    a = str(k)
    l = int(a[::-1])
    return k == l

def IsPolindromStr(a):
    return a == a[::-1]

max = 0
t_start = time.time()
for i in range(100,1000):
    for j in range(100,1000):
        k = i * j
        if IsPolindromStr(str(k)) and max < k:
            max = k
print(max)
print(time.time() - t_start)