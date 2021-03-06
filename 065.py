# Convergents of e

# Problem 65

# https://projecteuler.net/problem=65

import datetime

start_time = datetime.datetime.now()

numerator = 1
denominator = 1
iCount = 0
denominators = []
denominators.append(2)
start = 98
j = 0
for i in range (33):
    j += 2
    denominators.append(1)
    denominators.append(j)
    denominators.append(1)

for i in range(start, -1, -1):
    d = denominators[i]
    numerator, denominator = denominator, d * denominator + numerator

stop_time = datetime.datetime.now()
print(stop_time - start_time)

print(denominator, numerator, denominator / numerator)
sd = str(denominator)
a = [int(s) for s in sd]
print(sum(a))