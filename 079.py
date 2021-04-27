# Passcode derivation

# Problem 79
# A common security method used for online banking is to ask the user for three random characters from a passcode. 
# For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

# The text file, keylog.txt, contains fifty successful login attempts.
# Given that the three characters are always asked for in order, analyse the file so as 
# to determine the shortest possible secret passcode of unknown length.
# https://projecteuler.net/problem=79

import datetime
import Utilities

f = open('num79.txt')
a = f.readlines()
b = set(a)
d = dict()
index = 0
for i in b:
    s = str(i)
    for c in s:
        if c != '\n' and (not c in d.keys()):
            d[c] = index
            index += 1
count = 0
while True:
    for i in b:
        s = str(i)
        c1 = s[0]
        c2 = s[1]
        c3 = s[2]
        c1_key = d[c1]
        c2_key = d[c2]
        c3_key = d[c3]
        if c2_key <= c1_key:
            c2_key = c1_key + 1
            d[c2] = c2_key
        if c3_key <= c2_key:
            c3_key = c2_key + 1
            d[c3] = c3_key
    count += 1
    v = d.values()
    if len(set(v)) == len(v):
        break
list_d = list(d.items())
list_d.sort(key=lambda i: i[1])
for i in list_d:
    print(i[0], end=' ')
