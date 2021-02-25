# Double-base palindromes

# Problem 36
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)
# https://projecteuler.net/problem=36

import datetime
import Utilities

def IntToBinary(i):
    s2 = ''
    i2 = 1
    while i2 <= i:
        if i & i2 > 0:
            s2 = '1' + s2
        else:
            s2 = '0' + s2
        i2 *= 2
    return s2

start_time = datetime.datetime.now()
res2 = []
res10 = []
for i in range(1000000):
    if Utilities.IsPalindromeStr(str(i)):
        s2 = IntToBinary(i)
        if  Utilities.IsPalindromeStr(s2):
            res10.append(i)
            res2.append(s2)
stop_time = datetime.datetime.now()
print(stop_time - start_time)
print(sum(res10))

