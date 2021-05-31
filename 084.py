# Problem 84
# https://projecteuler.net/problem=84

import datetime
from random import randint, seed

cPos = 0
ccPos = 0
chancePos = 0
cc = [0, 10]
chances = [0, 10, 11, 24, 39, 5]


def MonopolySimulate(diceLimit : int, simulateCount : int) -> str:
    global cPos
    board = list()
    for i in range(40):
        board.append(0)
    doubles = 0
    seed()
    for i in range(simulateCount):
        dice1 = randint(1, diceLimit)
        dice2 = randint(1, diceLimit)
        if dice1 == dice2:
            doubles += 1
        else:
            doubles = 0
        if doubles > 2:
            doubles = 0
            cPos = 10
        else:
            cPos = (cPos + dice1 + dice2) % 40
            if cPos == 7 or cPos == 22 or cPos == 36:
                Chance()
            if cPos == 2 or cPos == 17 or cPos == 33:
                CC()
            if cPos == 30:
                cPos = 10
        board[cPos] += 1

    m1 = board[0]
    i1 = 1
    m2 = board[1]
    i2 = 2
    m3 = board[2]
    i3 = 3

    if m1 < m2:
        m1, m2 = m2, m1
        i1, i2 = i2, i1
    if m2 < m3:
        m2, m3 = m3, m2
        i2, i3 = i3, i2
    if m1 < m2:
        m1, m2 = m2, m1
        i1, i2 = i2, i1
    for i in range(3, 40):
        m = board[i]
        if m > m3:
            if m > m1:
                m2, m3 = m1, m2
                i2, i3 = i1, i2
                m1 = m
                i1 = i
            elif m > m2:
                m2, m3 = m, m2
                i2, i3 = i, i2
            else:
                m3 = m
                i3 = i
    s1 = str(i1)
    if len(s1) == 1:
        s1 = '0' + s1
    s2 = str(i2)
    if len(s2) == 1:
        s2 = '0' + s2
    s3 = str(i3)
    if len(s3) == 1:
        s3 = '0' + s3

    return s1 + s2 + s3

def Chance():
    global cPos, chancePos, chances
    chancePos = (chancePos + 1) % 16

    if chancePos < 6:
        cPos = chances[chancePos]

    if chancePos == 6 or chancePos == 7:
        if cPos == 7:
            cPos = 15
        if cPos == 22:
            cPos = 25
        if cPos == 36:
            cPos = 5

    if chancePos == 8:
        if cPos == 22:
            cPos = 28
        else: 
            cPos = 12

    if chancePos == 9:
        cPos -= 3

def CC():
    global ccPos, cPos, cc
    ccPos = (ccPos + 1) % 16
           
    if ccPos < 2:
        cPos = cc[ccPos]

start_time = datetime.datetime.now()
s = MonopolySimulate(6, 1000000)
stop_time = datetime.datetime.now()

print(stop_time - start_time)
print(s)