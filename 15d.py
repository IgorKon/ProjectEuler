import datetime
Max = 20
Cache = {}

def MakeKey(x, y):
    if x < y:
        return str(Max - x) + " " + str(Max - y)
    else:
        return str(Max - y) + " " + str(Max - x)

def IsLastStep(x, y):
    return ((x == Max) or (y == Max))

def MakeNewStep(x, y):
    i = 0
    if IsLastStep(x, y):
        return 1
    key = MakeKey(x, y)
    if not (key in Cache):
        if x < Max:
            i += MakeNewStep(x + 1, y)
        if y < Max:
            i += MakeNewStep(x, y + 1)
        Cache[key] = i
    return Cache[key]

start_time = datetime.datetime.now()
n = MakeNewStep(0, 0)
print("{0:,d}".format(n))
stop_time = datetime.datetime.now()
print(stop_time - start_time)
print("{0:,d}".format(len(Cache)))
