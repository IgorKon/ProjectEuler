# Cyclical figurate numbers

# Problem 61
# Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are all figurate (polygonal) numbers and are 
# generated by the following formulae:

# Triangle	 	P3,n=n(n+1)/2	 	1, 3, 6, 10, 15, ...
# Square	 	P4,n=n2	 	1, 4, 9, 16, 25, ...
# Pentagonal	 	P5,n=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
# Hexagonal	 	P6,n=n(2n−1)	 	1, 6, 15, 28, 45, ...
# Heptagonal	 	P7,n=n(5n−3)/2	 	1, 7, 18, 34, 55, ...
# Octagonal	 	P8,n=n(3n−2)	 	1, 8, 21, 40, 65, ...
# The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three interesting properties.

# The set is cyclic, in that the last two digits of each number is the first two digits of the next number 
# (including the last number with the first).
# Each polygonal type: triangle (P3,127=8128), square (P4,91=8281), and pentagonal (P5,44=2882), 
# is represented by a different number in the set.
# This is the only set of 4-digit numbers with this property.
# Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: 
# triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different number in the set.
# https://projecteuler.net/problem=61

import datetime
import Utilities


def MakeStep(sources, res, iLast, iLength):
    for i in range(6):
        if res[i] != 0:
            continue
        for j in range(len(sources[i])):
            bUnique = True
            for k in range(6):
                if sources[i][j] == res[k]:
                    bUnique = False
                    break
            if bUnique and (sources[i][j] // 100) == (res[iLast] % 100):
                res[i] = sources[i][j]
                if iLength == 5:
                    if (res[5] // 100) == (res[i] % 100):
                        return True
                if MakeStep(sources, res, i, iLength + 1):
                    return True
        res[i] = 0
    return False

start_time = datetime.datetime.now()

max_i = 9999
min_i = 1000

sources = list()
sources.append(list(Utilities.TriangularNumbers(max_i, min_i)))
sources.append(list(Utilities.SquareNumbers(max_i, min_i)))
sources.append(list(Utilities.PentagonalNumbers(max_i, min_i)))
sources.append(list(Utilities.HexagonalNumbers(max_i, min_i)))
sources.append(list(Utilities.HeptagonalNumbers(max_i, min_i)))
sources.append(list(Utilities.OctagonalNumbers(max_i, min_i)))

iCount = 0
res = list()
for i in range(6):
    res.append(0)

for i in range(len(sources[5])):
    res[5] = sources[5][i]
    if MakeStep(sources, res, 5, 1):
        break

stop_time = datetime.datetime.now()
print(stop_time - start_time)

if len(res) > 0:
    print(res)
    print(sum(res))
else:
    print('Not found')
