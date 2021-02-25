# Goldbach's other conjecture

# Problem 46
# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
# 9 = 7 + 2 * 1**2
# 15 = 7 + 2 * 2**2
# 21 = 3 + 2 * 3**2
# 25 = 7 + 2 * 3**2
# 27 = 19 + 2 * 2**2
# 33 = 31 + 2 * 1**2
# It turns out that the conjecture was false.
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
# https://projecteuler.net/problem=46

import datetime
import Utilities

start_time = datetime.datetime.now()

max_i = 1000000

p_list = Utilities.Eratosthenes(max_i)
p_set = set(p_list)
print(max_i, len(p_list))
for i in range(9, max_i, 2):
    if not (i in p_set):
        j = 0
        NotFound = True
        while True:
            pp = p_list[j]
            if (i - pp) < 2:
                break
            d = i - pp
            if Utilities.IsSquare(d // 2):
                NotFound = False
                break
            j += 1
        if NotFound:
            print(i)
            break

stop_time = datetime.datetime.now()
print(stop_time - start_time)
