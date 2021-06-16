# Amicable chains

# Problem 95
# The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. 
# As the sum of these divisors is equal to 28, we call it a perfect number.
# Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220, forming a chain of two numbers. 
# For this reason, 220 and 284 are called an amicable pair.
# Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:
#     12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)
# Since this chain returns to its starting point, it is called an amicable chain.
# Find the smallest member of the longest amicable chain with no element exceeding one million.
# https://projecteuler.net/problem=95

import datetime

def GenerateFactorsSumm(limit : int):
    res = list()
    for i in range(limit + 1):
        res.append(0)
    res[1] = 1
    for i in range(1, limit // 2):
        for j in range(2 * i, limit + 1, i):
            res[j] += i
    return res

limit = 1000000
start_time = datetime.datetime.now()
FactorsSumm = GenerateFactorsSumm(limit)
chain = list()
number_was_used = list()
for i in range(limit + 1):
    number_was_used.append(False)

length = 0
min_a = limit
i = limit + 1
while i > 5:
    i -= 1
    newNumber = i
    chain.clear()
    chain.append(newNumber)
    while True:
        newNumber = FactorsSumm[newNumber]
        if newNumber > limit:
           break 
        if number_was_used[newNumber]:
            break
        if newNumber in chain:
            if newNumber == 1 or newNumber == chain[len(chain) - 1]:
                break
            start_index = chain.index(newNumber)
            len_chain = len(chain) - start_index
            chain_1 = chain[start_index:start_index + len_chain]
            if length < len_chain:
                length = len_chain
                AmicableChain = chain_1[:]
                min_a = min(AmicableChain)
            elif length == len_chain:
                if min(chain_1) < min_a:
                    AmicableChain = chain_1[:]
                    min_a = min(chain_1)
            break
        else:
            chain.append(newNumber)
    for j in chain:
        number_was_used[j] = True


stop_time = datetime.datetime.now()
print(stop_time - start_time)
print(min_a, length)
print(AmicableChain)

