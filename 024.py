# Lexicographic permutations

# Problem 24
# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 
# 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
# The lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120   201   210
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
# https://projecteuler.net/problem=24

import datetime
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = set()
iCount = 10
start_time = datetime.datetime.now()
R = range(iCount)
for i1 in R:
    for i2 in R:
        if i2 == i1: continue
        for i3 in R:
            if i3 == i1 or i3 == i2: continue
            for i4 in R:
                if i4 == i1 or i4 == i2 or i4 == i3: continue
                for i5 in R:
                    if i5 == i1 or i5 == i2 or i5 == i3 or i5 == i4: continue
                    for i6 in R:
                        if i6 == i1 or i6 == i2 or i6 == i3 or i6 == i4 or i6 == i5: continue
                        for i7 in R:
                            if i7 == i1 or i7 == i2 or i7 == i3 or i7 == i4 or i7 == i5 or i7 == i6: continue
                            for i8 in R:
                                if i8 == i1 or i8 == i2 or i8 == i3 or i8 == i4 or i8 == i5 or i8 == i6 or i8 == i7: continue
                                for i9 in R:
                                    if i9 == i1 or i9 == i2 or i9 == i3 or i9 == i4 or i9 == i5 or i9 == i6 or i9 == i7 or i9 == i8: continue
                                    for i10 in R:
                                        if i10 == i1 or i10 == i2 or i10 == i3 or i10 == i4 or i10 == i5 or i10 == i6 or i10 == i7 or i10 == i8 or i10 == i9: continue
                                        b.add(a[i1] * 1000000000 + a[i2] * 100000000 + a[i3] * 10000000 + a[i4] * 1000000 + a[i5] * 100000 + a[i6] * 10000 + \
                                        a[i7] * 1000 + a[i8] * 100 + a[i9] * 10 + a[i10])
stop_time = datetime.datetime.now()
print(stop_time - start_time)
print("{0:,d}".format(len(b)))
c = list(b)
c.sort()
print("{0:,d}".format(c[999999]))
