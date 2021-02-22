import datetime
MaxX = 12
MaxY = 12
class Point:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

def MakeNewStep(aa):
    while len(aa[0]) <= (MaxX + MaxY):
        print(len(aa[0]), "{0:,d}".format(len(aa)))
        aa_len = len(aa)
        i = 0
        while i < aa_len:
            a = aa[i]
            LastPoint = a[len(a) - 1]
            bWasAdded = False
            if LastPoint.X < MaxX:
                a.append(Point(LastPoint.X + 1, LastPoint.Y))
                bWasAdded = True
            if LastPoint.Y < MaxY:
                if bWasAdded:
                    c = a[:]
                    c.append(Point(LastPoint.X, LastPoint.Y + 1))
                    aa.append(c)
                else:
                    a.append(Point(LastPoint.X, LastPoint.Y + 1))
            i += 1
    return aa
a = []
start_time = datetime.datetime.now()
a.append([Point(0,0)])
a = MakeNewStep(a)
print("{0:,d}".format(len(a)))
stop_time = datetime.datetime.now()
print(stop_time - start_time)

