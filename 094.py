# Almost equilateral triangles

# Problem 94
# It is easily proved that no equilateral triangle exists with integral length sides and integral area. However, the almost equilateral triangle 5-5-6 
# has an area of 12 square units.
# We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by no more than one unit.
# Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed 
# one billion (1,000,000,000).
# https://projecteuler.net/problem=94
#https://www.mathblog.dk/project-euler-94-almost-equilateral-triangles/

import datetime

start_time = datetime.datetime.now()

limit = 1000000000
iCount = 0
summ_p = 0
x = 2
y = 1
bNotSkip = False
while True:
    aTimes3 = 2 * x - 1
    areaTimes3 = y * (x - 2)
    if aTimes3 > limit:
        break
    if bNotSkip and aTimes3 % 3 == 0 and areaTimes3 % 3 == 0:
        summ_p += aTimes3 + 1
    bNotSkip = True
    aTimes3 = 2 * x + 1
    areaTimes3 = y * (x + 2)
    if aTimes3 % 3 == 0 and areaTimes3 % 3 == 0:
        summ_p += aTimes3 - 1
    nextx = 2 * x + 3 * y
    nexty = 2 * y + x
    x = nextx
    y = nexty

stop_time = datetime.datetime.now()
print(stop_time - start_time)
print(summ_p)
