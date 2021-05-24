# Path sum: four ways

# Problem 83
# NOTE: This problem is a significantly more challenging version of Problem 81.
# In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by moving left, right, up, and down, 
# is indicated in bold red and is equal to 2297.
# Find the minimal path sum from the top left to the bottom right by moving left, right, up, and down in matrix.txt 
# (right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.
# https://projecteuler.net/problem=83

import datetime
import graph as g

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
Limit = len(n)

start_time = datetime.datetime.now()

grid = g.GridWithWeights(Limit, Limit)
for i in range(Limit):
    for j in range(Limit):
        grid.weights[(i, j)] = n[i][j]

came_from, cost_so_far = g.a_star_search(grid, (0, 0), (79, 79))
path = g.reconstruct_path(came_from, (0, 0), (79, 79))
sum = 0
for loc in path:
    sum += n[loc[0]][loc[1]]

stop_time = datetime.datetime.now()
print(stop_time - start_time)
print(sum)