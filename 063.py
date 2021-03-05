# Powerful digit counts

# Problem 63
# The 5-digit number, 16807=7**5, is also a fifth power. Similarly, the 9-digit number, 134217728=8**9, is a ninth power.
# How many n-digit positive integers exist which are also an nth power?
# https://projecteuler.net/problem=63

import datetime

start_time = datetime.datetime.now()
# counting the first pow for 1-9 numbers - we already have 9 at the start
iCount = 9
for i in range(2, 10):
    pow_i = i
    bFound = False
    # starts with square (pow = 2)
    for j in range(2, 100):
        pow_i *= i
        s = str(pow_i)
        if len(s) == j:
            iCount += 1
            bFound = True
        else:
            if bFound:
                break

stop_time = datetime.datetime.now()
print(stop_time - start_time)

print(iCount)