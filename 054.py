# Poker hands

# Problem 54
# https://projecteuler.net/problem=54

import poker

def SplitLine(s):
    a = s.split()
    if len(a) == 10:
        First = poker.CardsHand(a[:5])
        Second = poker.CardsHand(a[5:])
    return First, Second

f = open('num54.txt') 
lines = f.readlines()
iCount = 0
for s in lines:
    First, Second = SplitLine(s)
    if First.IsWon(Second):
        iCount += 1
print(iCount)
