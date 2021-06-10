# Right triangles with integer coordinates

# Problem 91
# The points P (x1, y1) and Q (x2, y2) are plotted at integer co-ordinates and are joined to the origin, O(0,0), to form ΔOPQ.
# There are exactly fourteen triangles containing a right angle that can be formed when each co-ordinate lies between 0 and 2 inclusive; that is,
# 0 ≤ x1, y1, x2, y2 ≤ 2.
# Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many right triangles can be formed?
# https://projecteuler.net/problem=91

import datetime
import itertools

maxx = 50
count = 0
start_time = datetime.datetime.now()
for x1 in range(maxx + 1):
    for y1 in range(maxx + 1):
        if x1 == 0 and y1 == 0:
            continue
        for x2 in range(x1, maxx + 1):
            for y2 in range(y1, maxx + 1):
                if (x2 == 0 and y2 == 0) or (x1 == x2 and y1 == y2):
                    continue
                sq1 = x1 * x1 + y1 * y1
                sq2 = x2 * x2 + y2 * y2
                diff_x = x1 - x2
                diff_y = y1 - y2
                sq3 = diff_x * diff_x + diff_y * diff_y
                if ((sq1 + sq2) == sq3) or ((sq1 + sq3) == sq2) or ((sq2 + sq3) == sq1):
                    count += 1

stop_time = datetime.datetime.now()
print(stop_time - start_time)
print(count)
