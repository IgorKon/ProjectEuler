# Sub-string divisibility

# Problem 43
# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.
# https://projecteuler.net/problem=43

import datetime
import itertools

start_time = datetime.datetime.now()

s = '1234567890'
a = [''.join(p) for p in itertools.permutations(s) if p[0] != '0' and (p[5] == '0' or p[5] == '5')]
#a = [''.join(p) for p in permutations(s) if p[0] != '0' and p[5] == '5']
print(len(a))
b=[]
for s1 in a:
    i = int(s1[1:4])
    if i % 2 != 0:
        continue
    i = int(s1[2:5])
    if i % 3 != 0:
        continue
    i = int(s1[3:6])
    if i % 5 != 0:
        continue
    i = int(s1[4:7])
    if i % 7 != 0:
        continue
    i = int(s1[5:8])
    if i % 11 != 0:
        continue
    i = int(s1[6:9])
    if i % 13 != 0:
        continue
    i = int(s1[7:10])
    if i % 17 != 0:
        continue
    b.append(int(s1))
print(b)
print(sum(b))
stop_time = datetime.datetime.now()
print(stop_time - start_time)
