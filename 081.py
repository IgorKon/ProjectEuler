# Path sum: two ways

# Problem 81
# In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, 
# is indicated in bold red and is equal to 2427.
# Find the minimal path sum from the top left to the bottom right by only moving right and down in matrix.txt (right click and "Save Link/Target As..."), 
# a 31K text file containing an 80 by 80 matrix.
# https://projecteuler.net/problem=81

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
bIs_I_Ok = True
bIs_J_Ok = True
step = 1
while step < Limit:
    k = Limit - 1 - step
    for i in range(Limit - 1, k, -1):
        if i == Limit - 1:
            n[i][k] += n[i][k + 1] 
        else:
            if n[i][k + 1] < n[i + 1][k]:
                n[i][k] += n[i][k + 1]
            else:
                n[i][k] += n[i + 1][k]
    for j in range(Limit - 1, k - 1, -1):
        if j == Limit - 1:
            n[k][j] += n[k + 1][j] 
        else:
            if n[k + 1][j] < n[k][j + 1]:
                n[k][j] += n[k + 1][j]
            else:
                n[k][j] += n[k][j + 1]
    step += 1

stop_time = datetime.datetime.now()
print(stop_time - start_time)
print(n[0][0])
