# Maximum path sum II

# Problem 67
# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
# 3
# 7 4
# 2 4 6
# 8 5 9 3
# That is, 3 + 7 + 4 + 9 = 23.
# Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle 
# with one-hundred rows.
# NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 2**99 altogether! 
# If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. 
# There is an efficient algorithm to solve it. ;o)
# https://projecteuler.net/problem=67

import datetime

f = open('num67.txt') 
lines = f.readlines()
n = []
i = 0
for line in lines:
    n.append([])
    s_nums = line.split()
    for s in s_nums:
        n[i].append(int(s))
    i += 1

start_time = datetime.datetime.now()
i = len(n) - 2
while i >= 0:
    CountInLine = len(n[i])
    for j in range(CountInLine):
        sum1 = n[i][j] + n[i+1][j]
        sum2 = n[i][j] + n[i+1][j+1]
        if sum1 > sum2:
            n[i][j] = sum1
        else:
            n[i][j] = sum2
    i -= 1

stop_time = datetime.datetime.now()
print(stop_time - start_time)
print(n[0][0])


