# Power digit sum

# Problem 16
# 2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2**1000?
# https://projecteuler.net/problem=16

n = 2 << 1000
s_n = str(n)
sum_n = sum([int(s) for s in s_n])
print("{0:,d}".format(n))
print("{0:,d}".format(sum_n))