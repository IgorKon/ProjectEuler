# Digit factorial chains

# Problem 74
# The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:
# 1! + 4! + 5! = 1 + 24 + 120 = 145
# Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:
# 169 → 363601 → 1454 → 169
# 871 → 45361 → 871
# 872 → 45362 → 872
# It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,
# 69 → 363600 → 1454 → 169 → 363601 (→ 1454)
# 78 → 45360 → 871 → 45361 (→ 871)
# 540 → 145 (→ 145)
# Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.
# How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
# https://projecteuler.net/problem=74

import datetime
import math

def NextNumberSlow(n, f, sf):
    s = sorted(str(n), reverse = True)
    n1 = int(''.join(c for c in s))
    if n1 in sf:
        return sf[n1]
    a = list(int(c) for c in s)
    sfn = sum([f[i] for i in a])
    sf[n] = sfn
    return sfn

def NextNumber(n, f, sf):
    n1 = n
    sfn = 0
    while n1 > 0:
        sfn += f[n1 % 10]
        n1 //= 10
    sf[n] = sfn
    return sfn

def ChainLength(i, f, sf):
    a = set()
    a.add(i)
    i1 = i
    while True:
        if i1 in sf:
            i1 = sf[i1]
        else:
            i1 = NextNumber(i1, f, sf)
        if i1 in a:
            return len(a)
        else:
            a.add(i1)

max_i = 10**6
start_time = datetime.datetime.now()
count = 0
f = dict()
for i in range(0, 10):
    f[i] = math.factorial(i)

sf = dict()
for i in range(max_i, 69, -1):
    cl = ChainLength(i, f, sf)
    if cl == 60:
        count += 1

stop_time = datetime.datetime.now()
print(stop_time - start_time)
print(count)
