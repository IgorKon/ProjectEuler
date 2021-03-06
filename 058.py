# Spiral primes

# Problem 58
# Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49

# It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is 
# that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.
# If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. 
# If this process is continued, what is the side length of the square spiral for which the ratio of primes along 
# both diagonals first falls below 10%?
# https://projecteuler.net/problem=58

import datetime
import Utilities

def GetDiagonalNums():
    res = [1, 1, 1, 1]
    iDiagNumber = 0
    while True:
        iDiagNumber += 1
        increment = 2 * iDiagNumber
        res[0] = res[3] + increment
        res[1] = res[0] + increment
        res[2] = res[1] + increment
        res[3] = res[2] + increment
        yield res

iDiagNumber = 0
iOverallCount = 1
iPrimeCount = 0
diagonalGenerator = GetDiagonalNums()
percent = 100

start_time = datetime.datetime.now()

for d in diagonalGenerator:
    iDiagNumber += 1
    iOverallCount += 4
    for i in d:
        if Utilities.IsPrime(i):
            iPrimeCount += 1
    percent = iPrimeCount / iOverallCount
    if percent < 0.1:
        break

stop_time = datetime.datetime.now()
print(stop_time - start_time)

print(2 * iDiagNumber + 1)
