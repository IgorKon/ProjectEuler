# Arranged probability

# Problem 100
# If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, 
# and two discs were taken at random, it can be seen that the probability of taking two blue discs, 
# P(BB) = (15/21)×(14/20) = 1/2.
# The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, 
# is a box containing eighty-five blue discs and thirty-five red discs.
# By finding the first arrangement to contain over 10**12 = 1,000,000,000,000 discs in total, 
# determine the number of blue discs that the box would contain.
# https://projecteuler.net/problem=100

import math
import datetime

start_time = datetime.datetime.now()
i_limit = 1000000000000
blue_count = 15
i_count = 21
while i_count < i_limit:
    b = 3 * blue_count + 2 * i_count - 2
    i = 4 * blue_count + 3 * i_count - 3
    blue_count = b
    i_count = i
stop_time = datetime.datetime.now()
print(stop_time - start_time)
print(blue_count, i_count)
