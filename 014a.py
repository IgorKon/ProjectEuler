# Longest Collatz sequence

# Problem 14
# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.
# https://projecteuler.net/problem=14

def CollatzCount(n, count = 1):
    if(n == 1):
        return count
    if n % 2 == 0:
        n /= 2
    else:
        n = 3 * n + 1
    count += 1
    return CollatzCount(n, count)

max = 1
n_max = 1
for i in range(3, 1001):
    c = CollatzCount(i)
    if max < c:
        max = c
        i_max = i
print(i_max, max)
