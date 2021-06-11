# Square digit chains

# Problem 92
# A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.
# For example,
# 44 → 32 → 13 → 10 → 1 → 1
# 85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89
# Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number 
# will eventually arrive at 1 or 89.
# How many starting numbers below ten million will arrive at 89?
# https://projecteuler.net/problem=92

import datetime
import itertools
import Utilities

sa = '0123456789'
def DigitsSquareSumm(i : int) -> int:
    summ = 0
    while i > 0:
        j = i % 10
        summ += j * j
        i //= 10
    return summ

def CountByDigits(s : str) -> int:
    f = Utilities.factorial(len(s))
    d = dict()
    for i in range(10):
        d[i] = 0
    for s1 in s:
        d[int(s1)] += 1
    for i in range(10):
        k = d[i]
        if k > 1:
            f //= Utilities.factorial(k)
    return f

maxx = 10000000
max1 = 9 * 9 * 7
cashe89 = set()
start_time = datetime.datetime.now()
for i in range(1, max1 + 1):
    j = i
    i_start = i
    while True:
        if j == 89:
            cashe89.add(i_start)
            break
        if j == 1:
            break
        j = DigitsSquareSumm(j)
count89 = 0
i = 0
for s in itertools.combinations_with_replacement(sa, 7):
    i += 1
    sd = ''
    for s1 in s:
        sd += s1
    j = DigitsSquareSumm(int(sd))
    if j in cashe89:
        count89 += CountByDigits(sd)

stop_time = datetime.datetime.now()
print(stop_time - start_time)
print(count89, i)
