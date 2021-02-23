# Lattice paths

# Problem 15
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
# there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?
# https://projecteuler.net/problem=15

import datetime
MaxX = 10
MaxY = 10
class Point:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

def MakeNewStep(aa):
    bResult = True
    while bResult:
        d = []
        print(len(aa[0]), "{0:,d}".format(len(aa)))
        for a in aa:
            LastPoint = a[len(a) - 1]
            bB = False
            if LastPoint.X < MaxX:
                b = []
                for p in a:
                    b.append(Point(p.X, p.Y))
                b.append(Point(LastPoint.X + 1, LastPoint.Y))
                d.append(b)
                bB = True
            bC = False
            if LastPoint.Y < MaxY:
                c = []
                for p in a:
                    c.append(Point(p.X, p.Y))
                c.append(Point(LastPoint.X, LastPoint.Y + 1))
                d.append(c)
                bC = True
        bResult = bB or bC
        if bResult:
            aa = d
    return aa
a = []
start_time = datetime.datetime.now()
a.append([Point(0,0)])
a = MakeNewStep(a)
print("{0:,d}".format(len(a)))
stop_time = datetime.datetime.now()
print(stop_time - start_time)
