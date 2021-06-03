# Product-sum numbers

# Problem 88
# A natural number, N, that can be written as the sum and product of a given set of at least two natural numbers, {a1, a2, ... , ak} is called 
# a product-sum number: N = a1 + a2 + ... + ak = a1 × a2 × ... × ak.
# For example, 6 = 1 + 2 + 3 = 1 × 2 × 3.
# For a given set of size, k, we shall call the smallest N with this property a minimal product-sum number. 
# The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows.
# k=2: 4 = 2 × 2 = 2 + 2
# k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
# k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
# k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
# k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6
# Hence for 2≤k≤6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30; note that 8 is only counted once in the sum.
# In fact, as the complete set of minimal product-sum numbers for 2≤k≤12 is {4, 6, 8, 12, 15, 16}, the sum is 61.
# What is the sum of all the minimal product-sum numbers for 2≤k≤12000?
# https://projecteuler.net/problem=88

import datetime
import math

start_time = datetime.datetime.now()

m : int = 12000
maxNum : int = 2 * m
numFactors : int = int(math.log2(maxNum))
f : list = []
f.append(1)
for i in range(1, numFactors):
    f.append(0)
k : list = [2*i for i in range(m)]
k[1] = 0

curMaxFactor : int = 1
j : int = 0

while True:
    if j == 0:
        if curMaxFactor == numFactors:
            break
        if f[0] < f[1]:
            f[0] += 1
        else:
            curMaxFactor += 1
            f[curMaxFactor - 1] = 1000000000
            f[0] = 2
        j += 1
        f[1] = f[0] - 1
    elif j == curMaxFactor - 1:
        f[j] += 1
        summ : int = 0
        prod : int = 1
        for i in range(curMaxFactor):
            prod *= f[i]
            summ += f[i]
        if prod > maxNum:
            j -= 1
        else:
            pk : int = prod - summ + curMaxFactor
            if pk < m and prod < k[pk]:
                k[pk] = prod
    elif f[j] < f[j + 1]:
        f[j] += 1
        f[j + 1] = f[j] - 1
        j += 1
    elif f[j] >= f[j + 1]:
        j -= 1

stop_time = datetime.datetime.now()
print(stop_time - start_time)
result : set = set()
for i in k:
    result.add(i)
print(sum(result))