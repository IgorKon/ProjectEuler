# Coded triangle numbers

# Problem 42
# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. 
# For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number 
# then we shall call the word a triangle word. Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing 
# nearly two-thousand common English words, how many are triangle words?
# https://projecteuler.net/problem=42

import datetime
import Utilities

start_time = datetime.datetime.now()

def NumberByWord(s):
    a = bytearray('a', 'ascii')
    b = bytearray(s.lower(), 'ascii')
    return sum([i - a[0] + 1 for i in b])

f = open('num42.txt') 
s = f.readlines()
f.close()
a = []
for s1 in s:
    b = s1.replace('"', '').split(",")
    for s2 in b:
        i = NumberByWord(s2)
        a.append(i)
j = max(a)
c = Utilities.TriangularNumbers(j)
iCount = 0
for k in a:
    if k in c:
        iCount += 1
print(iCount)

stop_time = datetime.datetime.now()
print(stop_time - start_time)
