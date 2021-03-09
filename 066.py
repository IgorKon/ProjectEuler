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

maxx = 0
maxy = 0
maxd = 0
for D in range(2, 1001):
    sq = int(math.sqrt(D))
    if sq * sq == D:
        continue
    m, d, a = 0, 1, sq
    numm1, num = 1, a
    denm1, den = 0, 1
    while (num * num - D * den * den) != 1:
        m = d * a - m
        d = (D - m * m) // d
        a = (sq + m) // d
        numm2, numm1 = numm1, num
        num = a * numm1 + numm2

        denm2, denm1 = denm1, den
        den = a * denm1 + denm2

    if maxx < num:
        maxx = num
        maxy = den
        maxd = D

stop_time = datetime.datetime.now()
print(stop_time - start_time)
print(maxx, maxy, maxd)
