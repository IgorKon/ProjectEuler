# Champernowne's constant

# Problem 40
# An irrational decimal fraction is created by concatenating the positive integers:
# 0.123456789101112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part, find the value of the following expression.
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
# https://projecteuler.net/problem=40

import datetime
import Utilities

start_time = datetime.datetime.now()

s = '123456789101'
frame_start_index = 1
frame_max_length = 100
next_index = 100
i = 10
iMaxCount = 5
res = []
while True:
    i += 1
    s = s + str(i)
    len_s = len(s)
    if frame_start_index + len_s - 1 > next_index:
        res.append(int(s[next_index - frame_start_index + 1]))
        if len(res) == iMaxCount:
            break
        next_index *= 10
    if  len_s > frame_max_length:  
        frame_start_index += frame_max_length
        s = s[frame_max_length:]
print(res)
print(Utilities.Mult(res))
stop_time = datetime.datetime.now()
print(stop_time - start_time)
