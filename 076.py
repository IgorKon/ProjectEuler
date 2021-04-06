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

def AppendResidualList(lst, n, limit):
    iCount = 0    
    if sum(lst) > limit:
        return
    for j in range(n, 0, -1):
        lst1 = lst[:]
        lst1.append(j)
        if sum(lst1) < limit:
            iCount += AppendResidualList(lst1, j, limit)
        if sum(lst1) == limit:
            iCount += 1
    return iCount


iCount = 0
start_time = datetime.datetime.now()
lst = list()
limit = 100
iCount = AppendResidualList(lst, limit - 1, limit)

stop_time = datetime.datetime.now()
print(stop_time - start_time)

print(iCount)
