import datetime
MaxX = 12
MaxY = 12

class Point:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

class Path:
    def __init__(self, a):
        self.Points = a[:]
        self.Complete = False

    def Add(self, x, y):
        self.Points.append(Point(x, y))

    def LastPoint(self):
        return self.Points[len(self.Points) - 1]

def Run(aa):
    SummuryCompletePathCount = 0
    CompleteCount = 0
    while CompleteCount < len(aa):
        print("{0:,d}".format(len(aa)))
        i = 0
        CompleteCount = 0
        while i < len(aa):
            a = aa[i]
            if a.Complete:
                i += 1
                CompleteCount += 1
                continue
            lastPoint = a.LastPoint()
            bNeedToCompleteA = ((lastPoint.X + 1) == MaxX)
            if lastPoint.Y + 1 < MaxY:
                if bNeedToCompleteA:
                    # Insert One New Point Only to the Path
                    SummuryCompletePathCount += 1
                    bNeedToCompleteA = False
                    a.Add(lastPoint.X, lastPoint.Y + 1)
                    i += 1
                else:
                    # Insert One New Point to the Path and Clone and Add the New Path
                    b = Path(a.Points)
                    b.Add(lastPoint.X, lastPoint.Y + 1)
                    aa.insert(i, b)
                    a.Add(lastPoint.X + 1, lastPoint.Y)
                    i += 2
            else:
                if bNeedToCompleteA:
                    # Complete the Path
                    a.Complete = True
                    SummuryCompletePathCount += 2
                    i += 1
                else:
                    a.Add(lastPoint.X + 1, lastPoint.Y)
                    SummuryCompletePathCount += 1
                    i += 1
    return SummuryCompletePathCount
a = []
start_time = datetime.datetime.now()
a.append(Path([Point(0,0)]))
PathCount = Run(a)
print("{0:,d}".format(PathCount))
stop_time = datetime.datetime.now()
print(stop_time - start_time)

