
# Pandigital products

# Problem 32
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, 
# the 5-digit number, 15234, is 1 through 5 pandigital.
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
# https://projecteuler.net/problem=32

import datetime
import re

def IsPanDigit(i, j, k):
    s = str(i) + str(j) + str(k)
    if len(s) != 9: return False
    m = re.findall(r'(\d).*\1', s)
    if len(m) != 0:
        return False
    a = [int(s1) for s1 in s]
    a.sort()
    res = (a == [1,2,3,4,5,6,7,8,9])
    return res
def IsSingleNotZeroDigit(n):
    s = str(n)
    if s.find("0") != -1: return False
    if len(s) == 1:
        return True
    # trying to find duplicate numbers 
    m = re.findall(r'(\d).*\1', s)
    return (len(m) == 0)
def ContainTheSameDigits(i, j):
    si = str(i)
    sj = str(j)
    for s in si:
        if s in sj:
            return True
    return False

start_time = datetime.datetime.now()
a = []
for i in range(10000):
    if IsSingleNotZeroDigit(i):
        a.append(i)
stop_time = datetime.datetime.now()
print(stop_time - start_time)
start_time = datetime.datetime.now()
b = {}
b[7254] = '39,186'
L = len(a)
i1 = 0
dt1 = stop_time - start_time
dt2 = stop_time - start_time
dt3 = stop_time - start_time
dt4 = stop_time - start_time
while i1 < L:
    i2 = i1
    while i2 < L - 1:
        i2 += 1
        m1 = a[i1]
        m2 = a[i2]
        k = m1 * m2
        if len(str(k)) != 4:
            continue
        t1 = datetime.datetime.now()
        if ContainTheSameDigits(m1, m2):
            dt1 += datetime.datetime.now() - t1
            continue
        dt1 += datetime.datetime.now() - t1
        t1 = datetime.datetime.now()
        if not IsSingleNotZeroDigit(k):
            dt2 += datetime.datetime.now() - t1
            continue
        dt2 += datetime.datetime.now() - t1
        t1 = datetime.datetime.now()
        if (k in b):
            dt3 += datetime.datetime.now() - t1
            continue
        dt3 += datetime.datetime.now() - t1
        t1 = datetime.datetime.now()
        if IsPanDigit(m1, m2, k):
            b[k] = str(m1) + ',' + str(m2)
        dt4 += datetime.datetime.now() - t1
    i1 += 1
a = list(b)
print('ContainTheSameDigits - ',dt1)
print('IsSingleNotZeroDigit - ',dt2)
print('In B - ',dt3)
print('IsPanDigit - ',dt4)
stop_time = datetime.datetime.now()
print('Overal - ',stop_time - start_time)
print("{0:,d}".format(sum(a)))
#print("{0:,d}".format(len(result)))
print(b)