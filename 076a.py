# Counting summations

# Problem 76
# It is possible to write five as a sum in exactly six different ways:
# 4 + 1
# 3 + 2
# 3 + 1 + 1
# 2 + 2 + 1
# 2 + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1
# How many different ways can one hundred be written as a sum of at least two positive integers?
# https://projecteuler.net/problem=76

import datetime

start_time = datetime.datetime.now()
lst = list()
limit = 5

for i in range(limit + 1):
    lst.append(0)
lst[0] = 1

for i in range(1, limit):
    for j in range(i, limit + 1):
        lst[j] += lst[j - i]

stop_time = datetime.datetime.now()
print(stop_time - start_time)

print(lst[limit])
