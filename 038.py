# Pandigital multiples

# Problem 38
# Take the number 192 and multiply it by each of 1, 2, and 3:
# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, 
# which is the concatenated product of 9 and (1,2,3,4,5).
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer 
# with (1,2, ... , n) where n > 1?
# https://projecteuler.net/problem=38

import datetime

def IsPanDigit(s):
    if len(s) == 9:
        if '1' in s and '2' in s and '3' in s and '4' in s and '5' in s and '6' in s and '7' in s and '8' in s and '9' in s:
            return True
    return False

def UnitedMult(i, a):
    s = ''
    for j in a:
        s += str(i * j)
    return int(s)

start_time = datetime.datetime.now()
i = 8
maxUM = 9
maxA = []
while True:
    i += 1
    a = [1, 2]
    um = UnitedMult(i, a)
    if um > 987654321:
        break
    j = 2
    while um <= 987654321:
        if IsPanDigit(str(um)):
            if maxUM < um:
                maxI = i
                maxUM = um
                maxA = a[:]
        j += 1
        a.append(j)
        um = UnitedMult(i, a)

stop_time = datetime.datetime.now()
print(stop_time - start_time)

print(maxI)
print(maxA)
print(maxUM)
