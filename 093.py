# Arithmetic expressions

# Problem 93
# By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and making use of the four arithmetic operations (+, −, *, /) 
# and brackets/parentheses, it is possible to form different positive integer targets.
# For example,
# 8 = (4 * (1 + 3)) / 2
# 14 = 4 * (3 + 1 / 2)
# 19 = 4 * (2 + 3) − 1
# 36 = 3 * 4 * (2 + 1)
# Note that concatenations of the digits, like 12 + 34, are not allowed.
# Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different target numbers of which 36 is the maximum, 
# and each of the numbers 1 to 28 can be obtained before encountering the first non-expressible number.
# Find the set of four distinct digits, a < b < c < d, for which the longest set of consecutive positive integers, 1 to n, 
# can be obtained, giving your answer as a string: abcd.
# https://projecteuler.net/problem=93

import datetime
import itertools
import Utilities

sa = '123456789'
op = ['+', '-', '*', '/']

def CalcNaturals(nums):
    count = 0
    i = 1
    bFound = True
    while bFound:
        if i in nums:
            count += 1
            i += 1
            bFound = True
        else:
            bFound = False
    return count

def GenerateArithmeticString(sd, l) -> str:
    for s in l:
       yield s.format(dgt1 = sd[0], dgt2 = sd[1], dgt3 = sd[2], dgt4 = sd[3])
#       yield s % (sd[0], sd[1], sd[2], sd[3])

start_time = datetime.datetime.now()
count = 0
nums = set()
max_natural_count = 0
result : str = ''
ex_count = 0
l = list()
for opp in itertools.product(op, repeat=3):
    l.append('{dgt1}' + opp[0] + '{dgt2}' + opp[1] + '{dgt3}' + opp[2] + '{dgt4}')
    l.append('({dgt1}' + opp[0] + '{dgt2}' + opp[1] + '{dgt3})' + opp[2] + '{dgt4}')
    l.append('{dgt1}' + opp[0] + '({dgt2}' + opp[1] + '{dgt3})' + opp[2] + '{dgt4}')
    l.append('({dgt1}' + opp[0] + '{dgt2})' + opp[1] + '{dgt3}' + opp[2] + '{dgt4}')
    l.append('{dgt1}' + opp[0] + '({dgt2}' + opp[1] + '{dgt3}' + opp[2] + '{dgt4})')
    l.append('{dgt1}' + opp[0] + '{dgt2}' + opp[1] + '({dgt3}' + opp[2] + '{dgt4})')
    l.append('({dgt1}' + opp[0] + '{dgt2})' + opp[1] + '({dgt3}' + opp[2] + '{dgt4})')
    # l.append('%s' + opp[0] + '%s' + opp[1] + '%s' + opp[2] + '%s')
    # l.append('(%s' + opp[0] + '%s' + opp[1] + '%s)' + opp[2] + '%s')
    # l.append('%s' + opp[0] + '(%s' + opp[1] + '%s)' + opp[2] + '%s')
    # l.append('(%s' + opp[0] + '%s)' + opp[1] + '%s' + opp[2] + '%s')
    # l.append('%s' + opp[0] + '(%s' + opp[1] + '%s' + opp[2] + '%s)')
    # l.append('%s' + opp[0] + '%s' + opp[1] + '(%s' + opp[2] + '%s)')
    # l.append('(%s' + opp[0] + '%s)' + opp[1] + '(%s' + opp[2] + '%s)')

for sd in itertools.combinations(sa, 4):
    nums.clear()
    count = 0
    for ssd in itertools.permutations(sd, 4):
        count += 1
        for s in GenerateArithmeticString(ssd, l):
            try:
                k = eval(s)
                nums.add(k)
            except:
                ex_count += 1
    nat = CalcNaturals(nums)
    if max_natural_count < nat:
        max_natural_count = nat
        result = sd[0] + sd[1] + sd[2] + sd[3]

stop_time = datetime.datetime.now()
print(stop_time - start_time)
print(max_natural_count, result)
