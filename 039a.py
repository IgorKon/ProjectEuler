# Integer right triangles

# Problem 39
# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, 
# there are exactly three solutions for p = 120.
# {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p ≤ 1000, is the number of solutions maximised?
# https://projecteuler.net/problem=39

import datetime

start_time = datetime.datetime.now()
TheBestRightTriangles = []
TheBestP = 12
for p in range(12, 1001):
    rightTriangles = []    
    for i in range(1, p):
        j = p * p - 2 * p * i
        if j <= 0:
            break
        k = 2 * (p - i)
        if j % k == 0:
            j = j // k
            if i > j:
                break
            tri = [i, j, p - i - j]
            rightTriangles.append(tri[:])
    if len(TheBestRightTriangles) < len(rightTriangles):
        TheBestRightTriangles = rightTriangles[:]
        TheBestP = p
stop_time = datetime.datetime.now()
print(stop_time - start_time)
print(TheBestP)
print(len(TheBestRightTriangles))
print(TheBestRightTriangles)