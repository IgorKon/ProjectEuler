# Singular integer right triangles

# Problem 75
# It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, 
# but there are many more examples.
# 12 cm: (3,4,5)
# 24 cm: (6,8,10)
# 30 cm: (5,12,13)
# 36 cm: (9,12,15)
# 40 cm: (8,15,17)
# 48 cm: (12,16,20)
# In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, 
# and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form 
# exactly three different integer sided right angle triangles.
# 120 cm: (30,40,50), (20,48,52), (24,45,51)
# Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?
# https://projecteuler.net/problem=75
# https://en.wikipedia.org/wiki/Pythagorean_triple
# https://ru.wikipedia.org/wiki/%D0%9F%D0%B8%D1%84%D0%B0%D0%B3%D0%BE%D1%80%D0%BE%D0%B2%D0%B0_%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0

import datetime
import math
start_time = datetime.datetime.now()

limit = 1500000
iCount = 0
m_limit = int(math.sqrt(limit / 2))
tri = dict()

for m in range(2, m_limit):
    for n in range(1, m):
        if (n + m) % 2 == 1 and math.gcd(n, m) == 1:
            m2 = m * m
            n2 = n * n
            a = m2 + n2
            b = m2 - n2
            c = 2 * m * n
            p = a + b + c
            while p <= limit:
                if p in tri:
                    tri[p] += 1
                    if tri[p] == 2:
                        iCount -= 1
                else:
                    tri[p] = 1
                    iCount += 1
                p += a + b + c


stop_time = datetime.datetime.now()
print(stop_time - start_time)

print(iCount)
