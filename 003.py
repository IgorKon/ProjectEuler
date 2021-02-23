# Largest prime factor

# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import Utilities

def GetDividers(n):
    m = n
    dividers = []
    i = 2
    while i <= m:
        if m % i == 0:
            dividers.append(i)
            m = m // i
        else:
            i += 1
    return dividers

n=600851475143
dividers = GetDividers(n)
print(dividers)
for i in dividers[::-1]:
    if Utilities.IsPrime(i):
        print(i)
        break
