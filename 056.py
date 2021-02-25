# Powerful digit sum

# Problem 56
# A googol (10**100) is a massive number: one followed by one-hundred zeros; 100**100 is almost unimaginably large: one followed by two-hundred zeros. 
# Despite their size, the sum of the digits in each number is only 1.
# Considering natural numbers of the form, a**b, where a, b < 100, what is the maximum digital sum?
# https://projecteuler.net/problem=56

import datetime

MaxSum = 0
iMax = 0
jMax = 0
start_time = datetime.datetime.now()

for i in range(100):
    for j in range(100):
        snum = str(pow(i, j))
        sum = 0
        for s in snum:
            sum += int(s)
        if MaxSum < sum:
            MaxSum = sum
            iMax = i
            jMax = j

stop_time = datetime.datetime.now()
print(stop_time - start_time)

print(MaxSum, iMax, jMax)
