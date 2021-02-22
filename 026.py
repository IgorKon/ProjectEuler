from decimal import Decimal, getcontext
import re

# Problem 26
# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

def GetPeriodLength(s):
    result = max(re.findall(r'((\w+?)\2+)', s), key=lambda t: len(t[0]))
    if len(result) < 2:
        return ""
    return result[1]

getcontext().prec = 15000
b_max = ''
max_len = 0
i_max = 0
for i in range(3, 1000):
    s = '{0:.15000f}'.format(Decimal(1.0) / Decimal(i))
    b = GetPeriodLength(s[2::])
    b_len = len(b)
    if max_len < b_len:
        max_len = b_len
        b_max = b
        i_max = i
print(i_max, max_len, b_max)
print('{0:.15000f}'.format(Decimal(1.0) / Decimal(i_max)))
