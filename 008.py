# Largest product in a series

# Problem 8
# The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832. (file num8.txt)
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

import Utilities

f = open('num8.txt') 
s = f.readline()
n = []
for ch in s:
    n.append(int(ch))
i_start = 0
i_count = 13
i_len = len(n)
max_mult = 0
max_a = []
while True:
    i_stop = i_start + i_count
    if i_stop > i_len: break
    a = n[i_start:i_stop]
    mult = Utilities.Mult(a)
    if max_mult < mult: 
        max_mult = mult
        max_a = a
    i_start += 1

print(max_a, max_mult)
