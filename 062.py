# Cubic permutations

# Problem 62
# The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). 
# In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
# Find the smallest cube for which exactly five permutations of its digits are cube.
# https://projecteuler.net/problem=62

import datetime
import itertools
import Utilities

class CubeData:
    def __init__(self, first):
        self.FirstNumber = first
        self.Count = 1

start_time = datetime.datetime.now()

cubes = dict()
bFound = False
for i in range(346, 10000):
    q = i * i * i
    a = list(str(q))
    a.sort(reverse = True)
    s1 = int(''.join(s for s in a))
    if s1 in cubes.keys():
        cubes[s1].Count += 1
        if cubes[s1].Count == 5:
            bFound = True
            found = cubes[s1]
            break
    else:
        cubes[s1] = CubeData(i)

stop_time = datetime.datetime.now()
print(stop_time - start_time)

if bFound:
    print(found.FirstNumber, found.FirstNumber ** 3)
else:
    print('Not found')