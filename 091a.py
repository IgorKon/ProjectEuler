# Right triangles with integer coordinates

# Problem 91
# The points P (x1, y1) and Q (x2, y2) are plotted at integer co-ordinates and are joined to the origin, O(0,0), to form ΔOPQ.
# There are exactly fourteen triangles containing a right angle that can be formed when each co-ordinate lies between 0 and 2 inclusive; that is,
# 0 ≤ x1, y1, x2, y2 ≤ 2.
# Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many right triangles can be formed?
# https://projecteuler.net/problem=91

import datetime
import math

maxx = 50
count = maxx * maxx * 3
start_time = datetime.datetime.now()
for x in range(1, maxx + 1):
    for y in range(1, maxx + 1):
        f = math.gcd(x, y)
        count += min(y * f // x, (maxx - x) * f // y ) * 2

stop_time = datetime.datetime.now()
print(stop_time - start_time)
print(count)
