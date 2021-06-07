# Cube digit pairs

# Problem 90
# Each of the six faces on a cube has a different digit (0 to 9) written on it; 
# the same is done to a second cube. By placing the two cubes side-by-side in different positions we can form a variety of 2-digit numbers.
# In fact, by carefully choosing the digits on both cubes it is possible to display all of the square numbers below one-hundred: 
# 01, 04, 09, 16, 25, 36, 49, 64, and 81.
# For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on one cube and {1, 2, 3, 4, 8, 9} on the other cube.
# However, for this problem we shall allow the 6 or 9 to be turned upside-down so that an arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows 
# for all nine square numbers to be displayed; otherwise it would be impossible to obtain 09.
# In determining a distinct arrangement we are interested in the digits on each cube, not the order.
# {1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
# {1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}
# But because we are allowing 6 and 9 to be reversed, the two distinct sets in the last example both represent the extended set {1, 2, 3, 4, 5, 6, 9} 
# for the purpose of forming 2-digit numbers.
# How many distinct arrangements of the two cubes allow for all of the square numbers to be displayed?
# https://projecteuler.net/problem=90

import datetime
import itertools

start_time = datetime.datetime.now()
a1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
a2 = (0, 1, 2, 3, 4, 5, 8)
sq2 = [(0, 1), (0, 4), (2, 5), (8, 1)]
sq3 = [(0, 6, 9), (1, 6, 9), (3, 6, 9), (4, 6, 9)]
count = 0
res = set()
for a in itertools.combinations(a1, 6):
    for b in itertools.combinations(a1, 6):
        bRes = False
        for c in a2:
            bRes = (c in a) or (c in b)
            if not bRes:
                break
        if not bRes:
            continue
        if not ((6 in a) or (6 in b) or (9 in a) or (9 in b)):
            continue
        for c in sq2:
            bRes = (c[0] in a and c[1] in b) or (c[0] in b and c[1] in a)
            if not bRes:
                break
        if not bRes:
            continue
        for c in sq3:
            bRes = ((c[0] in a) and ((c[1] in b) or (c[2] in b))) or ((c[0] in b) and ((c[1] in a) or (c[2] in a)))
            if not bRes:
                break
        if bRes:
            s1 = str(a[0]) + str(a[1]) + str(a[2]) + str(a[3]) + str(a[4]) + str(a[5])
            s2 = str(b[0]) + str(b[1]) + str(b[2]) + str(b[3]) + str(b[4]) + str(b[5])
            i1 = int(s1)
            i2 = int(s2)
            old_count = len(res)
            res.add((i1, i2))
            res.add((i2, i1))
            if len(res) == (old_count + 2):
                count += 1

stop_time = datetime.datetime.now()
print(stop_time - start_time)
print(count)
