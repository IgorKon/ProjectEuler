# Largest exponential

# Problem 99
# Comparing two numbers written in index form like 2**11 and 3*7 is not difficult, as any calculator would confirm that 2*11 = 2048 < 3*7 = 2187.
# However, confirming that 632382**518061 > 519432**525806 would be much more difficult, as both numbers contain over three million digits.
# Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair 
# on each line, determine which line number has the greatest numerical value.
# NOTE: The first two lines in the file represent the numbers in the example given above.
# https://projecteuler.net/problem=99

import datetime
import math

start_time = datetime.datetime.now()

f = open('num99.txt') 
lines = f.readlines()
i = 0
n_max_0 = 1
n_max_1 = 1
i_max = 0
n_max = 0
for line in lines:
    i += 1
    s_nums = line.replace('\n', '').split(',')
    n0 = int(s_nums[0])
    n1 = int(s_nums[1])
    n = math.log(n0) * n1
    if n > n_max:
        n_max_0 = n0
        n_max_1 = n1
        n_max = n
        i_max = i

stop_time = datetime.datetime.now()
print(stop_time - start_time)
print(i_max, n_max_0, n_max_1)
