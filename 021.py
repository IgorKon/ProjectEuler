# Amicable numbers

# Problem 21
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.
# https://projecteuler.net/problem=21

import Utilities

friends = set()
sum_a = 0
for i in range(3, 10000):
    if i not in friends:
        dividers = Utilities.GetUniqueDividers(i)
        sum_d = sum(dividers)
        if (i != sum_d) and (sum_d not in friends):
            dividers = Utilities.GetUniqueDividers(sum_d)
            sum_d1 = sum(dividers)
            if i == sum_d1: 
                print(i, sum_d)
                friends.add(i)
                friends.add(sum_d)
                sum_a += i
                sum_a += sum_d
print(sum_a)
