# Diophantine equation

# Problem 66
# Consider quadratic Diophantine equations of the form:
# x**2 – Dy**2 = 1
# For example, when D=13, the minimal solution in x is 649**2 – 13×180**2 = 1.
# It can be assumed that there are no solutions in positive integers when D is square.
# By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:
# 3**2 – 2×2**2 = 1
# 2**2 – 3×1**2 = 1
# 9**2 – 5×4**2 = 1
# 5**2 – 6×2**2 = 1
# 8**2 – 7×3**2 = 1
# Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.
# Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.
# https://projecteuler.net/problem=66

import datetime
import math

start_time = datetime.datetime.now()
sq1 = []
for x in range(2, 1001):
    sq1.append(x * x)

sq10 = sq1[:]
for x in range(1001, 10001):
    sq10.append(x * x)

l = len(sq10)
res = []
maxx = 0
maxy = 0
maxd = 0
for D in range(2, 1001):
    if D in sq1:
        continue
#    a = [(x2, y2) for x2 in sq1 for y2 in sq1 if x2 - D*y2 == 1]
    for ix in range(1, l):
        x2 = sq10[ix]
        if x2 < D:
            continue
        for iy in range(ix):
            y2 = sq10[iy]
            diff = x2 - D * y2
            if diff == 1:
                if maxx < x2:
                    maxx = x2
                    maxy = y2
                    maxd = D
            elif diff < 0:
                break

stop_time = datetime.datetime.now()
print(stop_time - start_time)

print(int(math.sqrt(maxx)), int(math.sqrt(maxy)), maxd)
#print(a)