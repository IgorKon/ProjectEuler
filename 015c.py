# Lattice paths

# Problem 15
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
# there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?
# https://projecteuler.net/problem=15

import datetime
Max = 10
class Point:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

def MakeNewStep(a):
    iNum = 0
    iOveralRemoved = 0
    while iNum < (Max + Max - 1):
        iNum += 1
        a_len = len(a)
        i = 0
        while i < a_len:
            bXWasChanged = False
            x = a[i].X
            y = a[i].Y
            if a[i].X < Max:
                a[i].X += 1
                bXWasChanged = True
            if a[i].Y < Max:
                if bXWasChanged:
                    a.append(Point(x, a[i].Y + 1))
            i += 1
        i = 0
        while i < len(a):
            if a[i].X == Max or a[i].Y == Max:
                a.pop(i)
                iOveralRemoved += 1
            else:
                i += 1
        print(iNum, "{0:,d}".format(len(a) + iOveralRemoved))
    return iOveralRemoved
a = []
start_time = datetime.datetime.now()
a.append(Point(0,0))
n = MakeNewStep(a)
print("{0:,d}".format(n))
stop_time = datetime.datetime.now()
print(stop_time - start_time)