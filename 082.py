# Path sum: three ways

# Problem 82
# NOTE: This problem is a more challenging version of Problem 81.
# The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any cell in the right column, 
# and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994.
# Find the minimal path sum from the left column to the right column in matrix.txt 
# (right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.
# https://projecteuler.net/problem=82

import datetime

#f = open('num81t.txt') 
f = open('num81.txt') 
lines = f.readlines()
n = []
i = 0
for line in lines:
    n.append([])
    s_nums = line.split(',')
    for s in s_nums:
        n[i].append(int(s))
    i += 1

start_time = datetime.datetime.now()
Limit = len(n)
Column = list()
for i in range(Limit):
    Column.append(0)
step = 1
while step < Limit:
    # column k
    k = Limit - 1 - step
    for i in range(Limit):
        Column[i] = n[i][k]
    for i in range(Limit):
        m_min = n[i][k + 1]
        # from top to cell
        for i1 in range(i):
            m = n[i1][k + 1]
            for i2 in range(i1, i):
                m += n[i2][k]
            if m_min > m:
                m_min = m
        # from bottom to cell
        for i1 in range(Limit - 1, i, -1):
            m = n[i1][k + 1]
            for i2 in range(i1, i, -1):
                m += n[i2][k]
            if m_min > m:
                m_min = m
        Column[i] += m_min
    for i in range(Limit):
        n[i][k] = Column[i]
    step += 1

stop_time = datetime.datetime.now()
print(stop_time - start_time)
print(min(Column))
